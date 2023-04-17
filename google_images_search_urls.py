from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
# navigate to the Google Images search results page
search_term = "cute puppies"
google_images_url = f"https://www.google.com/search?q={search_term}&tbm=isch"
driver.get(google_images_url)

# find all the image divs and extract their links
image_divs = driver.find_elements(By.CLASS_NAME,'isv-r')

for image_div in image_divs[1:]:
    img_tag = image_div.find_element(By.TAG_NAME, 'img')
    img_tag.click()
    time.sleep(3)
    
    # Find the div tag that appears with class name 'iPVvYb' after clicking the image
    final_image_div = driver.find_element(By.CLASS_NAME, 'iPVvYb')
    if final_image_div:
        print(final_image_div.get_attribute('src'))
        
    time.sleep(3)

driver.quit() 
