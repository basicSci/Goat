from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # check homepage
        self.browser.get(self.live_server_url)

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
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy feathers')

        #Add another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacocks')
        inputbox.send_keys(Keys.ENTER)

        # Page updates and shows both items
        self.check_for_row_in_list_table('1: Buy feathers')
        self.check_for_row_in_list_table('2: Use peacocks')

        # Now a new user

        ## We use a new browser session to check info flow
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # New user Francis visits; check no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy feathers', page_text)
        self.assertNotIn('Use peacocks', page_text)

        # Francis starts new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy feathers', page_text)
        self.assertIn('Buy milk', page_text)


        self.fail('Finish the test!')

        #will add story here...

