Sprint_6

Зависимости указаны в requirements.txt
Для установки зависимостей: pip3 install -r requirements.txt
Для запуска тестов: pytest tests

В папке tests три файла с тестами:
test_logo.py проверки переходов по логотипам.
test_main.py проверка корректности текста выпадающего списка на главной.
test_order.py полный пользовательский сценарий заказа с двух различных кнопок.

Для генерации и просмотра веб-версии отчетов allure:
pytest tests --alluredir=allure_results
allure serve allure_results

# sprint_6
