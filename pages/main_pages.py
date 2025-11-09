from pages.base_pages import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver, time=5):
        super().__init__(driver, time)

    @allure.step("FAQ #{index}: элемент помечён как активный")
    def get_activ_element(self, index: int):
        return self.get_element_attribute(self.locators.FAQ_QUESTION(index), "aria-disabled") == "true"

    @allure.step("FAQ #{index}: клик по вопросу")
    def click_on_the_list(self, index: int):
        self.click_on_element(self.locators.FAQ_QUESTION(index))

    @allure.step("FAQ #{index}: ждать видимости вопроса")
    def get_explicit_wait_for_an_element_dropdown(self, index: int):
        return self.wait_for_element_visible(self.locators.FAQ_QUESTION(index))

    @allure.step("FAQ #{index}: получить текст ответа")
    def get_text_list(self, index: int):
        return self.get_element_text(self.locators.FAQ_ANSWER(index))

    @allure.step("FAQ #{index}: ждать видимости ответа")
    def wait_for_faq_answer_visible(self, index: int):
        return self.wait_for_element_visible(self.locators.FAQ_ANSWER(index))

    @allure.step('Клик по логотипу «Яндекс»')
    def click_on_the_yandex(self):
        self.click_on_element(self.locators.LOGO_YANDEX)

    @allure.step('Клик по логотипу «Самокат»')
    def click_on_the_sco(self):
        self.click_on_element(self.locators.LOGO_SCOOTER)

    @allure.step("FAQ #{index}: полный путь (скролл → клик → ожидание ответа)")
    def full_test(self, index: int):
        with allure.step("Прокрутить к блоку FAQ"):
            self.scroll_to_element(self.locators.FAQ_CONTAINER)

        with allure.step("Ждать видимости вопроса"):
            self.get_explicit_wait_for_an_element_dropdown(index)

        with allure.step("Клик по вопросу"):
            self.click_on_the_list(index)

        with allure.step("Ждать ответа"):
            self.wait_for_faq_answer_visible(index)