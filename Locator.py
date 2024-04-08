from selenium.webdriver.common.by import By


class MainPageLocator(object):
    LOGIN_BUTTON=(By.LINK_TEXT,"Create an Account")
    Search_Bar=(By.ID,"search")
    Product=(By.XPATH,'//*[@id="maincontent"]/div[3]/div/div[2]/div[3]/div/div/ol/li[1]')
    SIGN_IN=(By.LINK_TEXT,"Sign In")

class LoginPageLocator(object):
    CREATE_ACCOUNT_BUTTON=(By.CLASS_NAME,"submit")

class ProductPageLocator(object):
    Size_Selection=(By.ID,"option-label-size-143-item-169")
    Color_Selection=(By.ID,"option-label-color-93-item-50")
    AddToCard_Button=(By.ID,"product-addtocart-button")
    Card_BUTTON=(By.LINK_TEXT,"My Cart")
    Msg=(By.ID,"ui-id-1")


class SignInPageLocator(object):
    SIGN_IN_BUTTON=(By.ID,"send2")