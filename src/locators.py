from selenium.webdriver.common.by import By


nps_locators = {
    "Close Button": (
        By.XPATH,
        '//div[@class="NPS__close"]'),
    "Feedback Input": (
        By.XPATH,
        '//div[@class="NPS__feedback-textarea-container"]'),
    "Feedback Label": (
        By.XPATH,
        '//div[@class="NPS__feedback-title"]'),
    "Feedback Textarea": (
        By.XPATH,
        '//textarea[@class="NPS__feedback-textarea"]'),
    "General Rate Button": (
        By.XPATH,
        '//div[@class="NPS__buttons"]'
        '//div[contains(@class,"NPS__button")]/div'),
    "Main Window": (
        By.XPATH,
        '//div[@class="NPS"]'),
    "Send Button": (
        By.XPATH,
        '//button[@class="NPS__feedback-send"]'),
    "Title Like": (
        By.XPATH,
        '//div[@class="NPS__like-title"]'),
    "Title Not Like": (
        By.XPATH,
        '//div[@class="NPS__not-like-title"]'),
    "Title Welcome": (
        By.XPATH,
        '//div[@class="NPS__message"]')
}
