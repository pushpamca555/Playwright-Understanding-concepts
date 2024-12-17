class PlaygroundPage:
    
    def __init__(self, page) -> None:
        self.page = page
        
    
    def select_playground_menu(self, menu_title):
        self.page.get_by_role("link", name=menu_title).click()