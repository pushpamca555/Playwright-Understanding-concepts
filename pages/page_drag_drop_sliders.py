class DragDropSliders:
    def __init__(self, page) -> None:
        self.page = page
        self.slider = "input[value='{}']"
        self.range_success =  self.page.locator("#rangeSuccess")
        
    def do_slider(self, slider_number_start, slider_number_end):
        slider_number_start = int(slider_number_start)
        slider_number_end = int(slider_number_end)
        slider = self.page.locator(self.slider.format(slider_number_start))
        slider_box = slider.bounding_box()
        
        x_offset = slider_box['width'] * ((slider_number_end - 2) / 100)
        y_offset = 0
        
        slider.drag_to(slider, source_position={ "x": 0, "y": 0 }, 
                       target_position={ "x": x_offset, "y": y_offset })