from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():  # Создаем тестовую функцию
    # Открываем браузер с использованием Playwright
    with sync_playwright() as playwright:
        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        # Открываем новую страницу в рамках контекста
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('user.name@gmail.com')

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('username')

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

    # Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверить наличие и текст заголовка "Courses"
        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_header).to_be_visible()
        expect(courses_header).to_have_text('Courses')

        # Проверить наличие и текст блока "There is no results"
        no_result_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_result_text).to_have_text('There is no results')

        # Проверить наличие и видимость иконки пустого блока
        empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_visible()

        # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
        empty_block_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_block_description).to_be_visible()
        expect(empty_block_description).to_have_text("Results from the load test pipeline will be displayed here")
