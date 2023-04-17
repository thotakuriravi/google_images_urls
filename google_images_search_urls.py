from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
# navigate to the Google Images search results page
search_term = "cute puppies"
google_images_url = f"https://www.google.com/search?q={search_term}&tbm=isch"
driver.get(google_images_url)

# find all the image divs and extract their links
image_divs = driver.find_elements( By.CLASS_NAME,'isv-r')

i = 0
for image_div in image_divs[1:]:
    try:
        img_tag = image_div.find_element(By.TAG_NAME, 'img')
        img_tag.click()
        time.sleep(1)
        
        # Find the div tag that appears with class name 'iPVvYb' after clicking the image
        final_image_div = driver.find_elements(By.CLASS_NAME, 'iPVvYb')[0]
        if final_image_div:
            url = final_image_div.get_attribute('src')
            response = requests.get(url, stream=True)
            with open(f"images/{promt}_{i+1}.jpg", "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
                i = i+1
            del response
    except:
        continue
    # time.sleep(1)

driver.quit() 
