from tempfile import mkdtemp
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service

from src.settings import CHROMEDRIVER_PATH, CHROMIUM_PATH

class SeleniumScraper():
    def __init__(self):
        self.driver_options = [
            "--headless", # Hide the GUI
            "--no-sandbox", # No protection needed
            "--window-size=1280x1696", # Setup a fixed screens size
            "--single-process", # Lambda only give us only one CPU
            "--no-zygote", # Don't create zygote processes because Lambda give us only one CPU
            "--disable-dev-shm-usage", # Create temporary folder for shared memory files
            "--disable-dev-tools", # Disable Chrome dev tools
            f"--user-data-dir={mkdtemp()}", # Create temporary folder to user data
            f"--data-path={mkdtemp()}", # Create temporary folder to browser data
            f"--disk-cache-dir={mkdtemp()}",
        ]
        
    def _make_driver_options(self):
        options = ChromeOptions()
        options.binary_location = CHROMIUM_PATH
        for option in self.driver_options:
            option.add_argument(option)

    def create_driver(self):
        service = Service(CHROMEDRIVER_PATH)
        return Chrome(service=service, options=options)        
