import allure
from pages.yandex_internet import YandexInternet


@allure.feature('Яндекс Интернетометр')
@allure.story('Измерение скорости входящего соединения')
def test_yandex_internet(web_browser, input_connecting):
    web = YandexInternet(web_browser)
    
    with allure.step(f"Открываем {web.url}"):
        web.get(url=web.url)
    with allure.step("Ищем кнопку 'Измерить'"):
        assert web.measure.click()
    with allure.step("Ожидаем завершения подсчёта"):
        web.wait_page_loaded(
            check_js_complete=True)
    with allure.step("Ищем кнопку 'Измерить ещё раз'"):
        assert web.measure_again.is_visible()
    in_connect = web.search_field.get_text()
    with allure.step("Сравнение текущего показателей и заданого"):
        assert float(in_connect.split(' ')[0]) > input_connecting