from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    # Заполняем поле пароль
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_login_button = page.get_by_test_id('registration-page-registration-button')
    registration_login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_header).to_be_visible()

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)
