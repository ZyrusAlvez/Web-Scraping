from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Driver(uc=True)
url = "https://ojtgo.com/"
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()

try:
    # Wait until one of the elements with that class is present
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".fw-bold.m-0.p-0.text-truncate.ng-binding"))
    )

    # Find all elements with the full class string (using CSS selector)
    elements = driver.find_elements(By.CSS_SELECTOR, ".fw-bold.m-0.p-0.text-truncate.ng-binding")

    for el in elements:
        print(el.text)

except Exception as e:
    print("Error:", e)

driver.quit()
