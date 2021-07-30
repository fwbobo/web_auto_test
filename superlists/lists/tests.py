from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.template.loader import render_to_string
# Create your tests here.



class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')#resolve 反向解析根路径 “/”看是否能找到home_page函数
        self .assertEqual(found.func, home_page)

    def  test_home_page_returns_correct_html(self):
        request = HttpRequest()
        reponse = home_page(request)
        expected_html = render_to_string('home.html')
        print('********************************************')
        print(expected_html)
        print('********************************************')
        print(reponse.content.decode())
        #self.assertEqual(expected_html, reponse.content.decode())

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
