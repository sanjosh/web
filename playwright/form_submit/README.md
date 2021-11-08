
from https://scrapingant.com/blog/submit-form-playwright

# select by visibility

```
The more exciting part of this form submission is related to form click.
While the Google.com page has several buttons with this name,
we have to pick the button capable of being clicked.
To select it, we've used a CSS pseudo-selector :visible.

 await page.type('input[name=q]', 'ScrapingAnt is awesome');
 await page.click('input[name=btnK]:visible');
```

# submit file

```
await page.setInputFiles('input[type=file]', 'scrapingant.png');
```

# submit using javascript

```
 await page.evaluate(() => {
        document.querySelector('input[name=q]').value = 'ScrapingAnt is awesome';
        document.querySelector('input[name=btnK]:not([hidden])').click();
    });
```

# playwright

https://playwright.dev/docs/input/