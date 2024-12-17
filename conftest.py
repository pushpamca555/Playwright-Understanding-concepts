import pytest
import json
import urllib.parse

from playwright.sync_api import sync_playwright
from settings import *


# Função para criar a configuração de capabilities
def get_capabilities(browser, name_test):
    capabilities = CAPABILITY.copy()
    print(browser)
    capabilities['browserName'] = browser["browser"]
    capabilities["LT:Options"]["name"] = name_test
    capabilities['LT:Options']['platform'] = browser["platformName"]
    capabilities['LT:Options']['playwrightClientVersion'] = PLAYWRIGHT_VERSION
        
    return capabilities

@pytest.fixture(params=BROWSER_SETUP)
def web_name(request):
    return request.param
    
@pytest.fixture
def browser(web_name, request):
    capabilities = get_capabilities(web_name, request.node.name)
    capabilities_parser = urllib.parse.quote(json.dumps(capabilities))  
    
    with sync_playwright() as p:          
        browser = p.chromium.connect(LAMBDA_WSS+capabilities_parser, timeout=120000)
        context = browser.new_context(base_url=BASE_URL_TEST)
        yield context
        browser.close() 