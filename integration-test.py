import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000')

    def test_add_update_and_delete_item(self):
        item_text = 'NewItem'
        input_element = self.driver.find_element(By.NAME, 'item')
        input_element.send_keys(item_text)
        input_element.send_keys(Keys.RETURN)
        self.assertIn(item_text, self.driver.page_source)
        time.sleep(2)

        item_update_text = "UpdateItem"
        input_update_element = self.driver.find_element(By.NAME, 'new_item')
        input_update_element.send_keys(item_update_text)
        input_update_element.send_keys(Keys.RETURN)
        self.assertIn(item_update_text, self.driver.page_source)
        time.sleep(2)

        delete_button = self.driver.find_element(By.XPATH, "//a[@href='/delete/0']")
        delete_button.click()
        self.assertNotIn(item_text, self.driver.page_source)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
