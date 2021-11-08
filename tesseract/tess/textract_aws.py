'''
https://www.crosstab.io/articles/amazon-textract-review
'''
import boto3

s3 = boto3.client("s3")
textract = boto3.client("textract")

filename = "<<your filename>>"
file_path = "<<local path to your file, including the filename>>"
bucket = "<<your S3 bucket here>>"

s3.upload_file(file_path, bucket, filename)

doc_spec = {"S3Object": {"Bucket": bucket, "Name": filename}}

response = textract.start_document_analysis(
    DocumentLocation=doc_spec, FeatureTypes=["FORMS"]
)
print(response["JobId"])

import time

def poll_textract_job(
    job_id: str,
    initial_delay: float = 10,
    poll_interval: float = 2.5,
    max_attempts: int = 50,
) -> dict:
    """Poll for completed results for a given Textract job."""

    time.sleep(initial_delay)
    attempt = 0
    job_status = None

    while attempt < max_attempts:
        response = textract.get_document_analysis(JobId=job_id)
        job_status = response["JobStatus"]

        if job_status != "IN_PROGRESS":
            break

        time.sleep(poll_interval)  # Remember that `get` attempts are throttled.
        attempt += 1

    return job_status

def get_textract_results(job_id):
    response = textract.get_document_analysis(JobId=job_id)
    pages = [response]

    while "NextToken" in response:
        time.sleep(0.25)

        response = textract.get_document_analysis(
            JobId=job_id, NextToken=response["NextToken"]
        )

        pages.append(response)

    return pages


job_status = poll_textract_job(response["JobId"])

if job_status == "SUCCEEDED":
    pages = get_textract_results(response["JobId"])
    print(f"Pages: {len(pages)}\nBlocks: {sum([len(p['Blocks']) for p in pages])}")

import pandas as pd

def filter_key_blocks(blocks: dict) -> list:
    """Identify blocks that are keys in extracted key-value pairs."""
    return [
        k
        for k, v in blocks.items()
        if v["BlockType"] == "KEY_VALUE_SET" and "KEY" in v["EntityTypes"]
    ]

def identify_block_children(block: dict) -> list:
    """Extract the blocks IDs of the given block's children.

    Presumably, order matters here, and the order needs to be maintained through text
    concatenation to get the full key text.
    """

    child_ids = []

    if "Relationships" in block.keys():
        child_ids = [
            ix
            for link in block["Relationships"]
            if link["Type"] == "CHILD"
            for ix in link["Ids"]
        ]

    return child_ids

def concat_block_texts(blocks: list) -> str:
    """Combine child block texts to get the text for an abstract block."""
    return " ".join([b["Text"] for b in blocks])

def identify_value_block(block: dict) -> str:
    """Given a key block, find the ID of the corresponding value block."""
    return [x for x in block["Relationships"] if x["Type"] == "VALUE"][0]["Ids"][0]

def build_pairs_dataframe(blocks: dict):
    """Convert raw Textract output into a DataFrame of key-value pairs."""
    results = []
    key_ids = filter_key_blocks(blocks)

    for k in key_ids:
        child_ids = identify_block_children(blocks[k])
        child_blocks = [blocks[c] for c in child_ids]
        key_text = concat_block_texts(child_blocks)

        v = identify_value_block(blocks[k])
        child_ids = identify_block_children(blocks[v])
        child_blocks = [blocks[c] for c in child_ids]
        value_text = concat_block_texts(child_blocks)

        result = {
            "key_id": k,
            "key_text": key_text,
            "key_confidence": blocks[k]["Confidence"],
            "value_id": v,
            "value_text": value_text,
            "value_confidence": blocks[v]["Confidence"],
        }

        results.append(result)

    return pd.DataFrame(results)

## Run it!
blocks = {block["Id"]: block for page in pages for block in page["Blocks"]}
df_pairs = build_pairs_dataframe(blocks=blocks)
df_pairs[["key_text", "key_confidence", "value_text", "value_confidence"]].head()