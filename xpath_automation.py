from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    driver = webdriver.Chrome()

    driver.get("https://www.amazon.in")
    print("Google page loaded")
    # time.sleep(3)

    driver.maximize_window()
    print("Maximized the window")
    time.sleep(3)

    # driver.refresh()
    # print("Page refreshed")
    # time.sleep(3)

    # when i click the below link the link will be open in new tab so we have also switch the tab 
    # so i am storing the current tab for further use
    original_window = driver.current_window_handle

    # Finding an element of search box of Google
    dropdown = driver.find_element(By.XPATH, "/html/body/div/header/div/div/div[2]/div/form/div/div/div/select")
    select = Select(dropdown)
    select.select_by_visible_text("Amazon Devices")

    # After selection click the search button
    btns = driver.find_elements(By.CLASS_NAME, "nav-input")
    for btn in btns:
        btn_val = btn.get_attribute("value")
        if btn_val.lower() == "go":
            btn.click()
            break
        else:
            continue

    time.sleep(3)

    for i in range(9):
        driver.execute_script("window.scrollBy({top: 200, behavior: 'smooth'});")
        time.sleep(0.5)

    # Desire item name
    desire_title = "Amazon Echo Dot (5th Gen) | Smart speaker with vibrant sound"
    items = driver.find_elements(By.XPATH, "//h2[contains(@class, 'a-size-medium')]")
    for item in items:
        title = item.text.strip()
        print("Product Title:", title, sep="\n")

        if desire_title.lower() in title.lower():
            print("Found the desire item.")
            print("Item Name:", title, sep="\n")
            link = item.find_element(By.XPATH, "./ancestor::a[1]")
            print("URL:", link.get_attribute("href"), sep="\n")
            time.sleep(2)
            link.click()
            break


    # now, swithcing into new tab 
    for window_hangle in driver.window_handles:
        if window_hangle != original_window:
            driver.switch_to.window(window_hangle)
            break

    time.sleep(2)
    # Now, adding the item into cart 
    btn_add_to_cart = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")
    btn_add_to_cart.click()

    time.sleep(2)

    # go back and close the tab
    driver.back()
    print("Navigated back to Page 1 of Amazon Item Detials of Tab2")
    time.sleep(2)

    driver.close()
    print("Close the current tab")
    driver.switch_to.window(original_window)
    print("Switch back to original tab of Amazon Item List")
    time.sleep(2)

    # Back 
    driver.back()
    print("Navigated back to Amazon home page of Tab1")
    time.sleep(2)

    driver.forward()
    print("Navigated forward to Amazon Item List of Tab1")
    time.sleep(5)
    
    driver.quit()
except Exception as e:
    print(f"An error: {e}")