import time
from PIL import Image

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class WebElement(object):
    def __init__(self, **kwargs):
        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout:int=10):
        """ Поиск элемента. """
        try: element = WebDriverWait(self._web_driver, timeout).until(
               EC.element_to_be_clickable(self._locator))
           
        except:element = None
        return element
    
    def wait_to_be_clickable(self, timeout:int=10, check_visibility:bool=False):
        """ Подождите, пока элемент будет готов к щелчку. """
        try: element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator))
        except: element = None
        if check_visibility:
            self.wait_until_not_visible()
        return element
    
    def is_clickable(self, timeout:int=1, check_visibility:bool=True):
        """ Проверить, готов ли элемент к щелчку или нет. """
        element = self.wait_to_be_clickable(timeout=timeout, check_visibility=check_visibility)
        return element if element else None

    def is_visible(self):
        """ Проверить, виден ли элемент. """
        element = self.find(timeout=0.1)
        return element.is_displayed() if element else False
    
    def wait_until_not_visible(self, timeout=10):
        element = None
        try: element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator))
        except: element = None
        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self._web_driver.execute_script(js, element)
            while not visibility and timeout <= 0:
                time.sleep(0.5)
                timeout -= 1
                visibility = self._web_driver.execute_script(js, element)
        return element
    
    def send_keys(self, keys:str, wait:int=1, click:bool=False, clear:bool=False, enter:bool=False):
        element = self.find(timeout=wait)
        if element:
            if click: element.click()
            if clear: element.clear()
            element.send_keys(keys) if enter else element.send_keys(keys + '\ue007')
            return True
        else:
            return False
    
    def get_text(self):
        """ Получить текст из тега"""
        element = self.find()
        if element:
            try:  text = str(element.text)
            except: text = None
            return text
        else: return False

    def get_attribute(self, attr_name):
        """ Получить атрибут элемента. """
        element = self.find()
        return element.get_attribute(attr_name) if element else False
    
    def _set_value(self, value, clear=True, ):
        """ Задайте значение входному элементу. """
        element = self.find()
        if element:
            if clear:
                element.clear()
                element.send_keys(value)
    
    def human_click(self, timeout=10, hold_seconds=0, x_offset:int=1, y_offset:int=1):
        """ Человеческое нажатие. """
        element = self.wait_to_be_clickable(timeout=timeout)
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                pause(hold_seconds).click(on_element=element).perform()
            return True
        else: return False

    def click(self, timeout:int=1):
        """ Нажатие """
        element = self.wait_to_be_clickable(timeout=timeout)
        print(f'driver: {element}')
        if element:
            try: 
                element.click()
                return True
            except: 
                print('No clicable')
        else: return False

    def right_mouse_click(self, x_offset=0, y_offset=0, hold_seconds=0):
        """ Нажатие правой кнопки """
        element = self.wait_to_be_clickable()
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).context_click(on_element=element).perform()
        else:
            return False
    
    def screenshot_elements(self, filename:str):
        """ Скриншот веб элемента """
        element = self.find()
        if element:
            location = element.location_once_scrolled_into_view;  size = element.size
            x = int(location['x']);      y = int(location['y'])
            w = int(size['width']);      h = int(size['height'])
            self._web_driver.save_screenshot(filename)
            fullImg = Image.open(filename)
            cropImg = fullImg.crop((int(x), int(y), int(w), int(h))) 
            cropImg.save(filename)

    def scroll_to_element(self):
        """ Прокрутите страницу до элемента. """
        element = self.find()
        if element:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            element.send_keys(Keys.DOWN)
        except Exception as e:
            pass  # Just ignore the error if we can't send the keys to the element

    def delete(self):
        """ Удаляет элемент со страницы. """
        element = self.find()
        if element:
            self._web_driver.execute_script("arguments[0].remove();", element)
        

    def jsScript(self, js:str):
        """ Создаёт и запускает JavaScripts """
        element = self.find()
        if element:
            self._web_driver.execute_script(js, element)

    def Action(self, hold_seconds, keys):
        element = self.find()
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element(element).pause(hold_seconds).send_keys(keys)
    
    def move_by_offset(self, x_offset:int, y_offset:int):
        actions = ActionChains(self._web_driver)
        actions.move_by_offset(x_offset, y_offset).click().perform()


    
class ManyWebElements(WebElement):
    def __getitem__(self, item):
        """ Получите список элементов и попробуйте вернуть требуемый элемент. """
        elements = self.find()
        return elements[item]

    def find(self, timeout=10):
        """ Поис элементов """
        try: elements = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_all_elements_located(self._locator))
        except: elements = []
        return elements

    def count(self):
        """ Количество элементов """
        elements = self.find()
        return len(elements) if elements else None

    def get_text(self):
        """ Поиск теста в элементов """
        result = []
        elements = self.find()
        if elements:
            for element in elements:
                try: result.append(str(element.text))
                except: continue
        return result
        

    def get_attribute(self, attr_name):
        """Поиск значения атрибута"""
        results = []
        elements = self.find()
        if elements:
            for element in elements:
                try: results.append(element.get_attribute(attr_name))
                except: continue
            return results
            