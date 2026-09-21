from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

try:
	driver.get("https://www.google.com/")
	web_element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='q']"))
	)
	driver.execute_script(
		"""
		const searchBox = arguments[0];
		searchBox.value = arguments[1];
		searchBox.dispatchEvent(new Event('input', { bubbles: true }));
		searchBox.form.submit();
		""",
		web_element,
		"wf-energy.com",
	)
	time.sleep(120)
finally:
	driver.quit()