from Pages.BasePage import BasePage


class SignInScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self):
        self.wait_for_element_to_be_visible('EMAIL_INPUT').send_keys('iamniralshah@gmail.com')

    def click_next_button(self):
        self.wait_for_element_to_be_visible('SIGN_IN_NEXT').click()

    def enter_password(self):
        self.wait_for_element_to_be_visible('PASSWORD_INPUT').send_keys('Vasupujy@3')

    def click_sign_in_button(self):
        self.wait_for_element_to_be_visible('SIGN_IN_FINAL_BUTTON').click()




