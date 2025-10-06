from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# Optional: show Chrome visibly
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")  # open full screen
# chrome_options.headless = False  # ensure it's visible

# Create the Chrome driver
# service = Service()  # Selenium 4+ automatically handles ChromeDriver
driver = webdriver.Chrome()

# Open a page
driver.get("https://www.amazon.com/BISSELL%C2%AE-ShotTM-OmniReach-Handheld-Cleaner/dp/B0DCHBC8JJ/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.679a99a5-333c-46b8-a493-b812dbdccbc0&dib=eyJ2IjoiMSJ9.qN1_bdWO6tPLy1pK1TcAxCl6MJGorrqvZOcVOqEqhwZkQYN92QxpcyrRjaPTFaf0D3EwrIooMrf2mep7vsz3nRGGLTLtlmbk9h0mjurq440qtlSRZAFU93E5igZ6LEqC2NDvx2v-EFnxdzAbrKGaG3e4Tk7LLCLZmgc5vD-IEggCf3PNabJPKo_PZ8LJcKnkXxbcJxOy0e2j_umqcVfmnzclfvDqtKQupBesPt_AKSRGi16uyl1mMc9uT-uiy1RSMNsfs4URuozogOoorA18UXlaZPNgDUshcMwpbMIsQtU.5hy0eIRbN4AKJn-IAafA4X3QT8iCZ1lGRd9I1l4cSqs&dib_tag=se&keywords=home+improvement&pd_rd_r=12b058f1-0a0c-4b4a-83fa-79297c4bf486&pd_rd_w=kDuxS&pd_rd_wg=OYtOB&qid=1760475002&refinements=p_36%3A-5000&s=hi&sr=1-2")
price = driver.find_element(By.CLASS_NAME, "aok-offscreen")
print(price.text)
# Confirm it's loaded
print("Page title:", driver.title)

# Keep open for 10 seconds
time.sleep(10)

driver.quit()
