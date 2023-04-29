from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By
import selenium


class BasicInstalltest(unittest.TestCase):

    # browser = webdriver.Chrome()
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_page_loads(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('The install worked successfully! Congratulations!', self.browser.title)
    

    def test_page_header(self):
        self.browser.get('http://127.0.0.1:8000/')
    
        h1 = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('The install worked successfully! Congratulations!', h1)
        # print(h1_tag.text)
        print('Slenium version: ' + selenium.__version__)
    
    def selenium_version(self):
        print('Slenium version: ' + selenium.__version__)


    




if __name__ == "__main__":
    unittest.main()
