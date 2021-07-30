from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
# Create your tests here.



class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')#resolve 反向解析根路径 “/”看是否能找到home_page函数
        self .assertEqual(found.func, home_page)

    def  test_home_page_returns_correct_html(self):
        request = HttpRequest()
        reponse = home_page(request)
        self.assertTrue(reponse.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', reponse.content)
        self.assertTrue(reponse.content.endswith(b'</html>'))
