
import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse
from pathlib import Path

'''
popup
page.onDialog(dialog -> {
    assertEquals("alert", dialog.type());
    assertEquals("", dialog.defaultValue());
    assertEquals("yo", dialog.message());
    dialog.accept();
});
page.evaluate("alert('yo')");

https://python.plainenglish.io/handling-new-windows-with-python-and-playwright-c223a1e846d9

'''

async def handle_popup(popup):
    await popup.wait_for_load_state()
    print(await popup.title())

async def handle_dialog(dialog):
    print(f' dialog is {dialog.message}, {dialog.type}')
    await dialog.accept()

def dump_frame_tree(frame, indent):
    print(indent + frame.name + '@' + frame.url)
    for child in frame.child_frames:
        dump_frame_tree(child, indent + "    ")

def handle_page(page):
    page.wait_for_load_state()
    print(f'handle page {page.url}')

async def run(*, browser, url_list: list, output_dir: Path) -> None:
    for url in url_list:
        url_p = urlparse(url)
        screenshot_file = url_p.netloc + '_' + url_p.path.replace('/', '_') + '.png'
        abs_path = output_dir / screenshot_file
        context = await browser.new_context()
        page = await context.new_page()
        page.on("request", lambda request: print(f'req url={request.url}'))

        page.set_default_timeout(300 * 60) # its in ms
        await page.goto(url, wait_until="networkidle")
        await page.click('text="Continue"')
        await page.click('text="Continue"')
        await page.click('text="Continue"')
        await page.click('text="Continue"')

        page.on("popup", handle_popup)
        page.on("dialog", handle_dialog)
        page.on("page", handle_page)
        dump_frame_tree(page.main_frame, "---   ")
        print(f'page opening is {await page.opener()}')
        # for commerce.gov.in await page.click("img[alt=\"nav-closed\"]")
        await page.screenshot(path=str(abs_path), full_page=True)
        await context.close()

# https://github.com/microsoft/playwright/issues/3151
# https://playwright.dev/python/docs/api/class-browser/#browser-new-context
# cnn.com takes looong time to load
# espncricinfo.com - nothing found

done_url_list = [
    'https://gst.gov.in',
    'https://unifiedportal-mem.epfindia.gov.in/',
]

async def main():
    cur = Path.cwd()
    output_dir = cur / 'screenshots'
    output_dir.mkdir(exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        url_list = [
                    'https://www.tin-nsdl.com/',
                    'https://dol.ny.gov/unemployment-insurance-rate-information',
                    ]
        await run(browser = browser, url_list = url_list, output_dir = output_dir)
        await browser.close()

asyncio.run(main())

