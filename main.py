import unittest
from selenium import webdriver
import page
import time


class LumaTesting(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome(" e")
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.driver.maximize_window()

    def test_Search(self):
        SearchPage=page.SearchPage(self.driver)
        main_page = page.MainPage(self.driver)
        main_page.SearchTest("men hoodie")
        time.sleep(5)
        #print("search",SearchPage.is_result_found())
        assert SearchPage.is_result_found() 

    def test_Buy(self):
        main_page = page.MainPage(self.driver)
        main_page.Buy_Product()
        assert main_page.is_title_matches("Radiant Tee")
        time.sleep(5)
        self.driver.implicitly_wait(10)
        Product_Page=page.Product_Page(self.driver)
        Product_Page.Select_ProductSize()
        Product_Page.Select_Color()
        Product_Page.Click_AddToCard_Button()
        self.driver.implicitly_wait(5)
        #print(Product_Page.is_Product_AddedToCard())
        assert Product_Page.is_Product_AddedToCard()
        time.sleep(5)


         
         




    def test_login(self):
        main_page = page.MainPage(self.driver)
        print(main_page.is_title_matches("Home Page"))
        assert main_page.is_title_matches("Home Page")
        
        main_page.click_login_button()
        login_page=page.LogInPage(self.driver)
        print(login_page.is_LogIn_found())
        assert login_page.is_LogIn_found()

        login_page.Fname_element="ghassen"
        login_page.Lname_element="ben samir"
        login_page.Email_element="d4957b4363@fireboxmail.lol"
        login_page.Password_element="Igbs*m#E(6489N7&"
        login_page.PasswordConfirm_element="Igbs*m#E(6489N7&"

        login_page.click_CreateAccount_button()
        MyAccountPage=page.MyAccount(self.driver)
        time.sleep(5)
        #print( MyAccountPage.is_account_created())
        assert MyAccountPage.is_account_created()


    def test_signIn(self):
        main_page = page.MainPage(self.driver)
        main_page.SignIn()
        print(main_page.is_title_matches("Customer Login"))
        time.sleep(5)
        SignIn_Page=page.SignIn_Page(self.driver)
        SignIn_Page.EmailSignInElement="d4957b4363@fireboxmail.lol"
        SignIn_Page.PasswordSignInElement="Igbs*m#E(6489N7&"
        SignIn_Page.click_SignIn_button()
        time.sleep(10)
        


    def tearDown(self) :
            self.driver.close()







if __name__=="__main__":
    unittest.main()