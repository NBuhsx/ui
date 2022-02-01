## Для работы с проектом вам понадобиться: #
* Скачать или клонировать репозиторий с проектом.
* Python 3.7 и ниже. Скачать можно на официально странице по [ссылке](https://www.python.org/downloads/).
* После установки python вам необходимо обновить pip-менеждер, это делается консольной командой: `python -m pip install --upgrade pip`.
* После обновления менеджера установок, вам необходимо установить зависимости. Файл зависимостей **requirements.txt** лежит в каталоге проекта. Для его установки введите команду: `pip install -r requirements.txt` (предварительно в консоли перейдите в проект).
## Для генерация отсчётов Allure и запуска их в браузере вам потребуется: #
* Java скачать можно на официальной странице по [ссылке](https://www.java.com/ru/download/ie_manual.jsp?locale=ru)
* Allure Framework, есть несколько спобов установке, выберите подходящий для вас по [ссылке](https://docs.qameta.io/allure/#_get_started)
## Запуск Тестов #
В cmd перейдите в директорию проекта и введите `pytest -v --driver Chrome` или `pytest -v --driver Firefox`
Вы можете запустить вебраузер в 'безголовом режиме' в файле conftest.py раскомментируйте `chrome_options.add_argument('--headless')`
## Запуск тестов с генерацией отсчётов Allure
В cmd перейдите в директорию проекта и введите `pytest --alluredir="reporst" --driver Chrome` или `pytest --alluredir="reporst" --driver Firefox`
* После завершения выполнения тестов сгенерируйте отсчёт `allure serve "reporst"`
#### **Не выносите файлы и папки из проекта и не запускаете их вне проекта.**
