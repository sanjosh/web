
# how to run

```
python -m playwright codegen --target python -o 'google_news_selector.py' -b chromium https://news.google.com

```
https://www.fatalerrors.org/a/0tR11j0.html

# how it works


the "-m" module switch calls `__main__.py`

https://github.com/microsoft/playwright-python/blob/master/playwright/__main__.py

https://github.com/microsoft/playwright-python/blob/29b5a13d1a95114a0c39ce7837352845890d0f1d/playwright/_impl/_driver.py#L28

/home/sandeep/miniconda3/envs/playwright/lib/python3.9/site-packages/playwright/driver/playwright.sh

in file cli.js

https://www.npmjs.com/package/commander

```
async function codegen(options, url, language, outputFile) {
  const {
    context,
    launchOptions,
    contextOptions
  } = await launchContext(options, !!process.env.PWTEST_CLI_HEADLESS, process.env.PWTEST_CLI_EXECUTABLE_PATH);
  await context._enableRecorder({
    language,
    launchOptions,
    contextOptions,
    device: options.device,
    saveStorage: options.saveStorage,
    startRecording: true,
    outputFile: outputFile ? _path.default.resolve(outputFile) : undefined
  });
  await openPage(context, url);
  if (process.env.PWTEST_CLI_EXIT) await Promise.all(context.pages().map(p => p.close()));
}
```

https://github.com/microsoft/playwright/blob/bb77912aeed624f5459c7c1a5459ad03ab820918/packages/playwright-core/src/server/supplements/recorder/recorderApp.ts

https://github.com/microsoft/playwright/blob/dddf70cead58ac374bc1a6f734953e723a034172/tests/inspector/cli-codegen-1.spec.ts#L23-L36
```
page.waitForEvent
recorder.waitForOutput
page.dispatchEvent
```

# doc

https://github.com/microsoft/playwright/blob/ef35bfa0da2f04a2dcd0f701af6faa091997de9e/docs/src/cli.md

https://github.com/microsoft/playwright/blob/4af576d0c7e986ff906d679e38ba4b2383a33147/docs/src/codegen.md
