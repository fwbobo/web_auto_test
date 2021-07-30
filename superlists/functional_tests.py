from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Chrome(r'E:\chromedriver.exe')
        self.wb.implicitly_wait(5)

    def tearDown(self):
        self.wb.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        #伊丽丝听说有一个很酷的在线代办事项应用
        #她去看了这个应用的首页
        self.wb.get(' http://127.0.0.1:8000/')

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
        inputbox.send_keys('buy peacock feathers')

        #她按了回车之后，页面更新了
        #代办事项表格中显示了1：buy peacock feathers
        inputbox.send_keys(Keys.ENTER)

        #time.sleep(10)#在这个代码的位置停止10 s
        table = self.wb.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1：buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        #页面上有显示了一个文本框，可以输入其他待办事项
        #她输入了use peacock to make a fly（使用孔雀羽毛做假的苍蝇）
        #伊丽丝做事很有条例
        self.fail('Finish the test')#提醒测试结束

        #页面再次更新时，她的清单中显示了这两个待办事项


if __name__ == '__main__':
    unittest.main(warnings='ignore')
