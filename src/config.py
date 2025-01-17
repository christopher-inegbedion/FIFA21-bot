from selenium import webdriver
import platform
import os


def create_driver():
    system = platform.system()

    if system == 'Darwin':
        path = 'chrome_mac/chromedriver'
    elif system == 'Linux':
        path = 'chrome_linux/chromedriver'
    elif system == 'Windows':
        path = os.getcwd() + '\chrome_windows\chromedriver.exe'
    else:
        raise OSError(f'Operating system {system} is not supported')

    driver = webdriver.Chrome(
        executable_path=path
    )
    driver.maximize_window()

    return driver


URL = "https://www.ea.com/fifa/ultimate-team/web-app/"

EA_EMAIL = "EA@e.ea.com"

PLAYER = {
    "name": "ake",
    "cost": 5200,
}

INCREASE_COUNT = 10

LOGIN_MANUALLY = True

# Credentials - fill in if LOGIN_MANUALLY is False

USER = {
    "email": "playstationgame245@gmail.com",
    "password": "Children1",
}

EMAIL_CREDENTIALS = {
    "email": "your_email@example.com",
    "password": "your_password",
}
