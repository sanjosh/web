
Page object 

Playwright ElementHandle is DOM object

```
class Login:
    def __init__(self, page):
        self.page = page
```

The pytest-playwright package provides simple fixtures for use within tests, such as the page fixture which automates browser setup.

It can also be configured to take screenshots upon failure which is helpful in debugging flakey or failing tests.

```
pytest to run headlessly
pytest --headful to run in a headful state
```

https://medium.com/analytics-vidhya/page-object-modeling-with-python-and-playwright-3cbf259eedd3

