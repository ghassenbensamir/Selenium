from Locator import * 
from element import BasePageElement
from selenium.webdriver.common.keys import Keys


class SearchFnameelement(BasePageElement):
    locator="firstname"


class Searchlnameelement(BasePageElement):
    locator="lastname"

class SearchEmailelement(BasePageElement):
    locator="email"


class SearchPasswordelement(BasePageElement):
    locator="password"

class SearchPasswordConfirmelement(BasePageElement):
    locator="password_confirmation"

class SearchEmailSignInelement(BasePageElement):
    locator="login[username]"

class SearchPasswordSignInElement(BasePageElement):
    locator="login[password]"


class BasePage(object):
    """Base class to initialize the base page that will be called from all"""
    def __init__(self,driver) :
        self.driver=driver

class MainPage(BasePage):
   
    def is_title_matches(self,title):
        return title in self.driver.title
    
    def click_login_button(self):
        element=self.driver.find_element(*MainPageLocator.LOGIN_BUTTON)
        element.click()
    
    def SearchTest(self,value):
        element=self.driver.find_element(*MainPageLocator.Search_Bar)
        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.RETURN)
    
    def Buy_Product(self):
        element=self.driver.find_element(*MainPageLocator.Product)
        element.click()


    def SignIn(self):
        element=self.driver.find_element(*MainPageLocator.SIGN_IN)
        element.click()

       

class LogInPage(BasePage):
    Fname_element=SearchFnameelement()
    Lname_element=Searchlnameelement()
    Email_element=SearchEmailelement()
    Password_element=SearchPasswordelement()
    PasswordConfirm_element=SearchPasswordConfirmelement()


    def is_LogIn_found(self):
        return "Create New Customer Account"  in self.driver.page_source
    

    def click_CreateAccount_button(self):
        element=self.driver.find_element(*LoginPageLocator.CREATE_ACCOUNT_BUTTON)
        element.click()

class MyAccount(BasePage):
    def is_account_created(self):
        return "My Account" in self.driver.title


class SearchPage(BasePage):
    def is_result_found(self):
       return "Your search returned no results." not in self.driver.page_source
    

class Product_Page(BasePage):
   def Select_ProductSize(self):
       element=self.driver.find_element(*ProductPageLocator.Size_Selection)
       element.click()

   def Select_Color(self):
       element=self.driver.find_element(*ProductPageLocator.Color_Selection)
       element.click()

   def Click_AddToCard_Button(self):
       element=self.driver.find_element(*ProductPageLocator.AddToCard_Button)
       element.click()

   def is_Product_AddedToCard(self):
       element=self.driver.find_element(*ProductPageLocator.Card_BUTTON)
       element.click()
       self.driver.implicitly_wait(5)
       msg=self.driver.find_element(*ProductPageLocator.Msg)
       print(msg.text)
       return "You have no items in your shopping cart." != msg.text
   

class SignIn_Page(BasePage):
    EmailSignInElement=SearchEmailSignInelement()
    PasswordSignInElement=SearchPasswordSignInElement()

    def click_SignIn_button(self):
        element=self.driver.find_element(*SignInPageLocator.SIGN_IN_BUTTON)
        element.click()
