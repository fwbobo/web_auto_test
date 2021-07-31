from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import LiveServerTestCase
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.wb = webdriver.Chrome(r'E:\chromedriver.exe')
        self.wb.implicitly_wait(5)

    def tearDown(self):
        self.wb.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.wb.find_element_by_id('id_list_table')
        rows = self.wb.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])#从rows中取出row的text 然后进行assertin

    def test_can_start_a_list_and_retrive_it_later(self):
        #伊丽丝听说有一个很酷的在线代办事项应用
        #她去看了这个应用的首页
        self.wb.get(self.live_server_url)

        #她注意到网页的标题和首部都包含To-Do这个词
        self.assertIn('To-Do', self.wb.title)
        header_text = self.wb.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #应用邀请她输入一个待办事项
        inputbox = self.wb.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #她在一个文本框输入了buy peacock feathers
        #伊丽丝的爱好是用假的苍蝇做鱼儿钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按了回车之后，页面更新了
        #代办事项表格中显示了1：buy peacock feathers
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:Buy peacock feathers')

        #页面上又显示了一个文本框，可以输入其他待办事项
        #她输入了use peacock to make a fly（使用孔雀羽毛做假的苍蝇）
        #伊丽丝做事很有条例
        inputbox = self.wb.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')

        #页面再次更新时，她的清单中显示了这两个待办事项
        table = self.wb.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1:Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2:Use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        #伊丽丝想知道这个网站是否会记住她的清单
        #她看到网站为她生成了唯一的URL
        #页面有一些文字解说这个功能

        self.fail('Finish the test')  # 提醒测试结束
