import pytest
from playwright.sync_api import expect, sync_playwright
from pages import page_playground, page_simple_form_demo, page_drag_drop_sliders, page_input_form_submit

def test_scenario_1(browser):    
    page = browser.new_page()
        
    # Page Objects instances
    playground_page = page_playground.PlaygroundPage(page)
    simple_form_demo_page = page_simple_form_demo.SimpleFormDemo(page)
    
    # Open Browser, goto site, select menu and confirm page url
    page.goto("/selenium-playground")        
    playground_page.select_playground_menu("Simple Form Demo")    
    expect(page).to_have_url("/selenium-playground/simple-form-demo")  
    
    # Create a variable with message testing
    message = "Welcome to LambdaTest"
     
    # Enter message, click button Check Value and assert result      
    simple_form_demo_page.enter_message(message)    
    simple_form_demo_page.click_check_value()
    expect(simple_form_demo_page.text_message).to_have_text(message)


def test_scenario_2(browser):    
    page = browser.new_page()
    
    # Page Object Instance
    playground_page = page_playground.PlaygroundPage(page)
    drag_drop_slider_page = page_drag_drop_sliders.DragDropSliders(page)
    
    # Open Browser, goto site, select menu
    page.goto("/selenium-playground")    
    playground_page.select_playground_menu("Drag & Drop Sliders")
    
    # Select percent validation and do slider
    percent_select = "95"
    drag_drop_slider_page.do_slider("15", percent_select)
    
    # Confirm validation slider on range success field
    expect(drag_drop_slider_page.range_success).to_have_text(percent_select)

def test_scenario_3(browser):
    
    DATA_FORM_SUBMIT = {
        "Name": "Wallace Petrucci Neves",
        "Email": "wallacepetrucci@gmail.com",
        "Password": "test123",
        "Company": "KaBuM!",
        "Website": "www.kabum.com.br",
        "country": "US",
        "City": "São Paulo",
        "Address 1": "Rua dos Buritis, 925",
        "Address 2": "Jd Oriental",
        "State": "SP",
        "Zip code": "04321002"
    }
    
    page = browser.new_page()
    
    # Page Objects instances
    playground_page = page_playground.PlaygroundPage(page)
    input_form_submit_page = page_input_form_submit.InputFormSubmit(page)
    
    # Open Browser, goto site and select menu
    page.goto("/selenium-playground")        
    playground_page.select_playground_menu("Input Form Submit")
    
    # Submit and valid required message
    input_form_submit_page.submit_form()    
    is_invalid = input_form_submit_page.input_name.evaluate("el => el.validity.valueMissing")    
    assert is_invalid == True
    
    # Fill all fields and submit form
    input_form_submit_page.fill_all_fields(DATA_FORM_SUBMIT)    
    input_form_submit_page.submit_form()
    
    # Assert message
    expect(input_form_submit_page.success_message).to_have_text("Thanks for contacting us, we will get back to you shortly.")
    