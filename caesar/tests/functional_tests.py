from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time
import unittest

MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1280, 720)

    def tearDown(self):
        self.browser.quit()

    def wait_for_text_in_table(self, table_id, text_to_find, row_or_col):
        self.wait_for(lambda:self.assertIn(text_to_find, [element.text for element in self.browser.find_element_by_id(table_id).find_elements_by_tag_name(row_or_col)]))

    def wait_for(self, fct):
        start_time = time.time()
        while True:
            try:
                return fct()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    self.browser.save_screenshot('screenshot.png')
                    print('BROWSER_GET_LOG: '+str(self.browser.get_log('har')))
                    print('BROWSER_GET_HTML: '+str(self.browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")))
                    raise e
                time.sleep(0.5)

    def test_user_can_do_that(self):
        # Edith has heard about a cool new online to-do app.
        #  She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title
        self.assertIn('Fifi', self.browser.title)

        # Satisfied, she goes back to sleep
        self.fail('Finish the test!')


# That’s how a Python script checks if it’s been executed from the command line,
# rather than just imported by another script
if __name__ == '__main__':
    unittest.main(warnings='ignore')

