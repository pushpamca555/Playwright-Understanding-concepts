class SimpleFormDemo:
    def __init__(self, page) -> None:
        self.page = page
        self.name_uri = "simple-form-demo"
        self.input_user_message = self.page.locator("input[id='user-message']")
        self.button_get_checked_value = self.page.locator("#showInput")
        self.text_message =  self.page.locator("#message")
        
    def enter_message(self, message):
        self.input_user_message.fill(message)
    
    def click_check_value(self):
        self.button_get_checked_value.click()
    
    def get_value_message(self):
        self.text_message.inner_text()
        
    
    