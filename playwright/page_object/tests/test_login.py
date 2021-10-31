from page_object.pages.login import Login

user = {
    "username": "test",
    "password": "password"
}

class TestLogin:
    def test_valid_login(self, page):
        login_page = Login(page)
        login_page.navigate()
        login_page.submit_login_form(user)
