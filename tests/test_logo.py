# tests/test_logo.py
import allure
from pages.main_pages import MainPage
from url import Url


@allure.feature("Навигация через логотипы")
class TestLogo:

    @allure.story("Переход в Дзен через логотип Яндекс")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Клик по логотипу «Яндекс» открывает Дзен в новой вкладке")
    @allure.description("С главной страницы клик по логотипу «Яндекс», переключает на новую вкладку и проверяет URL Дзена.")
    def test_transition_from_home_page_in_dzen(self, driver):
        page = MainPage(driver, time=10)

        with allure.step("Клик по логотипу «Яндекс»"):
            page.click_on_the_yandex()

        with allure.step("Переключение на последнюю открытую вкладку"):
            page.go_to_the_last_tab()

        with allure.step("Ожидание URL Дзена"):
            page.wait_url(Url.url_dzen)

        with allure.step("Проверка: текущий URL — это Дзен"):
            assert page.return_url() == Url.url_dzen, f"Ожидали {Url.url_dzen}, получили {page.return_url()}"

    @allure.story("Переход на главную страницу через логотип «Самокат»")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Клик по логотипу «Самокат» возвращает на главную")
    @allure.description("Со страницы оформления заказа кликает по логотипу «Самокат» и проверяет, что попали на главную.")
    def test_transition_from_order_page_to_main(self, driver):
        page = MainPage(driver, time=10)

        with allure.step("Открыть форму заказа (верхняя кнопка «Заказать»)"):
            page.click_order_button_top()

        with allure.step("Клик по логотипу «Самокат» для возврата на главную"):
            page.click_on_the_sco()

        with allure.step("Ожидание URL главной страницы"):
            page.wait_url(Url.url_page)

        with allure.step("Проверка: текущий URL — главная страница"):
            assert page.return_url() == Url.url_page, f"Ожидали {Url.url_page}, получили {page.return_url()}" 