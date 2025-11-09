
import pytest
import allure
from pages.main_pages import MainPage


FAQ_INDEXES = list(range(8))
FAQ_IDS = [f"faq-{i}" for i in FAQ_INDEXES]


class TestDropdownList:

    @allure.title("Каждый пункт FAQ раскрывается и показывает корректный ответ")
    @allure.description("Проверяет поочерёдно пункты FAQ.")
    @pytest.mark.parametrize("index", FAQ_INDEXES, ids=FAQ_IDS)
    def test_list_page(self, driver, index):
        page = MainPage(driver)
        with allure.step(f"Клик по вопросу FAQ #{index} и проверка раскрытия"):
            page.full_test(index)
            assert page.get_activ_element(index), f"FAQ #{index} не стал активным после клика"
