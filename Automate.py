from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"


client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'https://example.com/oauth2callback'
scope = ['https://www.googleapis.com/auth/forms']


driver = webdriver.Firefox()
driver.get(form_url)

try:
   
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="entry.XXXXXXXX"]'))  # Replace with actual form field selector
    )

    form_data = {
        "Full Name": "Satya Prakash",
        "Contact Number": "9341228341",
        "Email ID": "prakashsatya76453@example.com",
        "Full Address": "A Block, Sec 62, Noida",
        "Pin Code": "201014",
        "Date of Birth": "27/02/2002",
        "Gender": "Male"
    }

    for field_name, field_value in form_data.items():
        try:
            input_element = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'input[name="{field_name}"]'))
            )
            input_element.send_keys(field_value)
        except Exception as e:
            print(f"Error filling field {field_name}: {e}")

   
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    submit_button.click()

   
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="alert"]'))
    )
    print("Form submitted successfully!")

finally:
    driver.quit()
