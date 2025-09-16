import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="UI language, e.g. en, es, fr, ru"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    options.add_argument(f"--lang={user_language}")

    print(f"\nStart Chrome with UI language: {user_language}")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)

    yield driver
    print("\nQuit browser")
    driver.quit()
