import time

import pytest
from selenium import webdriver
from Config.conftest import browserInstance
from E2E_framework import driver
from Page_object.Login_page import Login_page
from Page_object.add2cart import Add2cart
from Page_object.Checkout import Check_out
from Page_object.agree_btn import Agree
from Page_object.product_selection import Electronic
from Page_object.page3_photo import Page3
from Page_object.shopping_cart import Shopping_cart


class Test_001_login:
    Base_URL = "https://demo.nopcommerce.com/login?returnUrl=%2F"
    username = "er.taufeeqali@gmail.com"
    password = "Ali@1234"


    #opening URL
    def test_login(self,browserInstance):
        driver = browserInstance
        driver.get(self.Base_URL)
        #filling credentials and entering site
        login_page = Login_page(browserInstance)
        login_page.user_name(self.username)
        login_page.password(self.password)
        login_page.agree()
        login_page.click_login()
        #selecting mobile
        electronic_cat = Electronic(browserInstance)
        electronic_cat.click_electronics_photo()
        #page3 mobile photo:
        page3_photo = Page3(browserInstance)
        page3_photo.page3()
        #add2cart:
        cart = Add2cart(browserInstance)
        cart.button_1()
        cart.button_2()
        cart.button_3()
        #shoppingcart_click:
        shopping = Shopping_cart(browserInstance)
        shopping.Scart()
        #agree btn:
        agree_btn = Agree(browserInstance)
        agree_btn.agree()
        #checkout:
        check_out = Check_out(browserInstance)
        check_out.check_btn()
        print("All done")











