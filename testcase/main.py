import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        service = Service(r"C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.python.org/")
    
    def test_search_in_python_org(self):
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.") 
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        self.assertTrue(search_result_page.is_results_found(), "No results found.") 
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()