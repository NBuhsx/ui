import json
import pytest
import uuid
import allure


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    # firefox_options.add_argument('--headless')
    return firefox_options




@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """ Помогает найти тест в котором произошёл assert"""

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, selenium):
    browser = selenium
    browser.implicitly_wait(20)
    yield browser

    if request.node.rep_call.failed:
        browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

        allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
           
            
def pytest_generate_tests(metafunc):
    """ Достаёт параметры из файлв data.json """
    with open(file=r'parameter\data.json', mode='r', encoding='utf-8') as file:
        arguments = json.load(file)
    if 'input_connecting' in metafunc.fixturenames:
        return metafunc.parametrize("input_connecting", arguments['Яндекс Интернетометр']['Входящее соединение'])
    if 'login' in metafunc.fixturenames:
        return metafunc.parametrize("login, password", arguments['Авторизация на https://rtmis.ru/'].items())
