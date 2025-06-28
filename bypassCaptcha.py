from seleniumbase import Driver
from bs4 import BeautifulSoup

driver = Driver(uc=True)
url = "https://ojtgo.com/"
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()

try:
    # Get full page source after page loads
    html = driver.page_source

    # Parse using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all elements with the target class
    elements = soup.select(".fw-bold.m-0.p-0.text-truncate.ng-binding")

    for el in elements:
        print(el.text)

except Exception as e:
    print("Error:", e)

driver.quit()
