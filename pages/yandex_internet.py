from .base import WebPage
from .elements import WebElement





class YandexInternet(WebPage):
    def __init__(self, web_driver: object):
        super().__init__(web_driver)

    url = 'https://yandex.ru/internet'
    measure = WebElement(xpath='//div[@class="toolbar__item"]/button[1]')
    measure_again = WebElement(xpath="//span[contains(text(), 'Измерить ещё раз')]")
    search_field = WebElement(xpath="//div[@class='speed-progress-bar__detailed'][1]")
   