class InputFormSubmit:
    
    def __init__(self, page) -> None:
        self.page = page
        self.input_country = self.page.locator("select[name='country']")
        self.input_name = self.page.locator("#name")
        self.success_message = self.page.locator(".success-msg")
    
    def fill_all_fields(self, data):
        for field_name, value in data.items():
            
            if field_name == "country":
                self.select_option(value)
                continue
                
            self.page.get_by_placeholder(field_name, exact=True).fill(value)
    
    def submit_form(self):
        self.page.get_by_role("button", name="Submit").click()
        
    def select_option(self, option):    
        self.input_country.select_option(option)
        
    
    