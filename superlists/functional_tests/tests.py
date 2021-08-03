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
        edit_list_url = self.wb.current_url
        print('******************')
        print(edit_list_url)
        self.assertRegex(edit_list_url, 'lists/.+')#检查字符串和正则表达式是否一样
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
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')

        #现在一个叫弗朗西斯的新用户访问了网站

        ##我们使用一个新的浏览器会话
        ##确保伊丽丝的信息不会从cookie中泄露出来
        self.wb.quit()
        self.wb = webdriver.Chrome(r'E:\chromedriver.exe')

        #弗朗西斯访问主页
        #页面中看不见伊丽丝的清单
        self.wb.get(self.live_server_url)
        page_text = self.wb.find_element_by_tag_name('body').text
        self.assertNotIn('1:Buy peacock feathers', page_text)
        self.assertNotIn('2:Use peacock feathers to make a fly', page_text)

        #弗朗西斯输入一个新待办事项，新建一个清单
        #他不像伊丽丝那么兴趣使然
        inputbox = self.wb.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #弗兰西斯获得了他的唯一URL
        francis_list_url = self.wb.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edit_list_url)

        #这个页面还是没有伊丽丝的清单
        page_text = self.wb.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        #两人都很满意，去睡觉了

    def test_layout_and_styling(self):
        self.wb.get(self.live_server_url)
        self.wb.set_window_size(1024, 768)


        inputbox = self.wb.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2,  #取得X坐标的位置，然后加上size
            512,
            delta=10#表示误差为正负5像素
        )

        # 她新建了一个清单，看见输入框仍完美居中显示
        inputbox.send_keys('testing\n')
        inputbox = self.wb.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,  # 取得X坐标的位置，然后加上size
            512,
            delta=10  # 表示误差为正负5像素
        )






















