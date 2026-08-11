from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

try:
    service = Service() # pass driver path as constructor, if not dectected automatically
    driver = webdriver.Chrome(service=service)
    print("Chrome browser launch successfully.")

    driver.maximize_window()

    # opening amazon website
    driver.get("https://www.amazon.in")

    time.sleep(3) # wait to load the page
    
    search_box = driver.find_element(By.NAME, "field-keywords")

    # Sending search key in seach box 
    search_box.send_keys("hp laptop i7")
    # search_box.send_keys(Keys.RETURN)

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    
    time.sleep(2) # wait for the secons to load the page

        
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(2)
    # to execute javascript code for scroll
    for i in range(5):
        driver.execute_script("window.scrollBy({top: 300, behavior: 'smooth'});")
        time.sleep(1)

    # when i click the below link the link will be open in new tab so we have also switch the tab 
    # so i am storing the current tab for further use
    original_window = driver.current_window_handle 

    desired_item = "Smartchoice Victus, 13th Gen i7-13620H, 6GB RTX 4050, 16GB"
    link = driver.find_element(By.PARTIAL_LINK_TEXT, desired_item)
    print("link", link, sep="\n")
    if link:
        link.click()

    time.sleep(5) # wait to open and load the page

    # now, swithcing into new tab 
    for window_hangle in driver.window_handles:
        if window_hangle != original_window:
            driver.switch_to.window(window_hangle)
            break

    print("URL:", driver.current_url)

    # data = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal h2")
    # for d in data:
    #     print("Product Title: ", d.text, sep="\n")
    #     if "Smartchoice Victus, 13th Gen i7-13620H, 6GB RTX 4050, 16GB" in d.text:
    #         d.click()
    #         break
    #     else:
    #         continue
    
    # time.sleep(20)


    # time.sleep(10)
    # for elem in driver.find_elements(By.TAG_NAME, "input"):
    #     value = elem.get_attribute("value")
    #     print(value)

    #     if value and value.lower() == "add to cart":
    #         elem.click()
    #         print("Added to cart")
    #         break

        
    #     print(elem.get_attribute("value"))
    #     if elem.get_attribute("value") == "Add to cart":
    #         elem.submit()

    buttons = driver.find_elements(By.ID, "add-to-cart-button")
    # print("Found:", len(buttons))
    
    for b in buttons:
        if b.is_displayed() and b.is_enabled():
            b.click()

    time.sleep(5)

    # Now, going back

    driver.back()

    time.sleep(5)

    driver.quit()
    print("Chrome close successfull")

except Exception as e:
    print(f"An error occurred: {e}")
