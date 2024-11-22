import time
from selenium.webdriver import Edge
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait

data = []
youtube_video_url = "https://www.youtube.com/watch?v=ldUmt3t-LOQ"

driver_service = Service(r"C:\Users\jakub\OneDrive\Dokumenty\GitHub\Profession_Analytics\Profession_Analytics.Scrapper\JustJoinIT\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=driver_service)
wait = WebDriverWait(driver,15)
driver.get(youtube_video_url)

for item in range(200):
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
    time.sleep(15)

for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
    data.append(comment.text)


df = pd.DataFrame(data, columns=['comment'])
df.head()