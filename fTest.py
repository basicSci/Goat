
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # check homepage
        self.browser.get('http://localhost:8000')

        #Note ToDo in title
        self.assertIn('ToDo', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ToDo', header_text)

        # Add to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # Enter some text into text box
        inputbox.send_keys('Buy feathers')

        # Then hit enter, pg updates, displays list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy feathers', [row.text for row in rows])
        self.assertIn('2: Use peacocks', [row.text for row in rows])

        self.fail('Finish the test!')

        #will add story here...

if __name__ == '__main__':
    unittest.main(warnings='ignore')
