#自動測試的網站：NETFLIX
import pytest, os, time
from playwright.sync_api import sync_playwright, Page, Browser
Script = os.path.basename(__file__)

class TestPlaywright01:
    ### Set Class ###
    def setup_class(self):
        print("\n*** Start: Playwright Frontend Tests ***")
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        
    def teardown_class(self):
        self.browser.close()
        self.playwright.stop()
        print("\n*** End: Playwright Frontend Tests ***")
    
    ### Set Method ###
    def setup_method(self):
        print("\n--- start test ---")
        self.page = self.browser.new_page()
        
    def teardown_method(self):
        self.page.close()
        print("--- end test ---")
    
    ### Frontend Tests ###
    def test01_netflix_webopen(self):
        print("Testing Netflix webpage opening function")
        
        self.page.goto("https://www.netflix.com/tw/")
        time.sleep(3)
        assert "netflix台灣讓您在線上觀賞節目與電影" in self.page.title().lower()
    
   
if __name__ == '__main__':
    pytest.main(["-s", Script + "::TestPlaywright01::test01_netflix_webopen"])