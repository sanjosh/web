

class Login:
    def __init__(self, page):
        self.page = page

    @property
    def new_user_button(self):
        return self.user_form.wait_for_selector("#newUser")

    @property
    def password_field(self):
        return self.user_form.wait_for_selector("#password")

    @property
    def submit_button(self):
        return self.user_form.wait_for_selector("#login")

    @property
    def user_form(self):
        return self.page.wait_for_selector("#userForm")

    @property
    def username_field(self):
        return self.user_form.wait_for_selector("#userName")

    def submit_login_form(self, user):
        self.username_field.fill(user["username"])
        self.password_field.fill(user["password"])
        self.submit_button.click()

    def navigate(self):
        self.page.goto("https://www.demoqa.com/login")