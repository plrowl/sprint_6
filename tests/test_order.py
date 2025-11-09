# tests/test_order_page.py
import pytest
import allure
from pages.order_pages import OrderPage
from data import Data


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
class TestOrderPage:

    @allure.title("Позитивный сценарий оформить самокат")
    @allure.description("Проверяет оформление заказа через кнопки «Заказать»")
    @pytest.mark.parametrize(
        "button, users",
        [
            ("top",    Data.USER_1),
            ("bottom", Data.USER_2),
        ],
        ids=["top-button", "bottom-button"]
    )
    def test_order_a_scooter(self, driver, button, users):
        page = OrderPage(driver)

        with allure.step(f'Выбирает кнопку "{button}" и открываем форму заказа'):
            btn_locator = page.get_order_button(button)
            page.scroll_to_element(btn_locator)
            page.click_on_element(btn_locator)

        with allure.step("Заполняем форму личных данных"):
            page.full_form_user(users)

        with allure.step("Заполняет форму аренды"):
            page.full_form_rent(users)

        with allure.step('Проверяет появление окна «Посмотреть статус»'):
            assert page.successful_rental() is True
