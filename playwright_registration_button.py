from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # кнопка "Registration" находится в состоянии disabled
    logging_button = page.get_by_test_id('registration-page-registration-button')
    expect(logging_button).to_be_disabled()

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле пользователь
    password_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input.fill("password")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # кнопка "Registration" находится в состоянии disabled
    # logging_button = page.get_by_test_id('registration-page-registration-button')
    expect(logging_button).not_to_be_disabled()

    page.wait_for_timeout(5000)
