from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.example.com")
text = element.text

print(text)

driver.quit()
