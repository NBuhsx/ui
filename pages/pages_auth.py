from .base import WebPage
from .elements import WebElement





class RTmis(WebPage):
    def __init__(self, web_driver: object):
        super().__init__(web_driver)

    url = 'https://demo.rtmis.ru/'
    login = WebElement(xpath='//input[@id="promed-login"]')
    password = WebElement(xpath='//input[@id="promed-password"]')
    auth = WebElement(xpath='//button[@id="auth_submit")]')

    error = WebElement(xpath='//span[@id="login-message"]')