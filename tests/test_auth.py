import allure
from pages.pages_auth import RTmis


@allure.feature('Авторизация на https://rtmis.ru/')
@allure.story('Тест с авторизации с рандомизируемыми данными')
def test_auth(web_browser, login:str, password:str):
    web = RTmis(web_browser)
    
    with allure.step(f"Открываем {web.url}"):
      web.get(url=web.url)
    with allure.step("Заполняем форму (логин:пароль)"):
      assert web.login.send_keys(login)
      assert web.password.send_keys(password)
    with allure.step("Нажимаем на кнопку войти"):
      web.auth.human_click()
    with allure.step("Определям на странице сообщение об ошибке авторизации"):
        assert not web.error.is_visible()
 
