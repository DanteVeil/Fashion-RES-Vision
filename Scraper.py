# scraper.py (Selenium version)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import requests
# import os

# URL = "https://www.asos.com/men/new-in/new-in-clothing/cat/?cid=6993"

# print("Stage 1: Setting up automated browser with Selenium...")
# try:
#     # Selenium will automatically download and manage the correct driver for Chrome
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#     print("-> Browser set up. Navigating to URL...")
#     driver.get(URL)

#     # Wait for the page to load its content (adjust time if needed)
#     time.sleep(5) 

#     print("-> Page loaded.")

#     # Get the page source after JavaScript has loaded
#     page_source = driver.page_source

# finally:
#     # Always close the browser window
#     driver.quit()

# print("\nStage 2: Parsing HTML response...")
# soup = BeautifulSoup(page_source, 'html.parser')
# print("-> HTML parsed.")

# print("\nStage 3: Finding product containers...")
# products = soup.find_all('div', class_='productHeroContainer_dVvdX')
# print(f"-> Found {len(products)} product containers.")

# if not os.path.exists('images'):
#     os.makedirs('images')

# if not products:
#     print("\nNo products found. The website's HTML may have changed or the class name is incorrect.")
# else:
#     # --- New print statement ---
#     print("\nStage 4: Starting image download loop...")
    
#     # Loop through products and save images
#     for i, product in enumerate(products):
#         img_tag = product.find('img')
#         if img_tag and 'src' in img_tag.attrs:
#             img_url = img_tag['src']
#             if img_url.startswith('//'):
#                 img_url = 'https:' + img_url

#             try:
#                 img_data = requests.get(img_url).content
#                 with open(f'images/product_{i}.jpg', 'wb') as handler:
#                     handler.write(img_data)
                
#                 # --- Modified print statement ---
#                 print(f"-> Downloaded image {i+1}/{len(products)}: product_{i}.jpg")
                
#                 # Add a small delay to be respectful to the server
#                 time.sleep(0.1)

#             except requests.exceptions.RequestException as e:
#                 print(f"Could not download {img_url}. Error: {e}")

# # --- New print statement ---
# print("\nScraping complete.")

# scraper.py (DEBUG version)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# URL = "https://www.asos.com/men/new-in/new-in-clothing/cat/?cid=6993"

# print("Stage 1: Setting up browser...")
# try:
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     print("-> Navigating to URL...")
#     driver.get(URL)
    
#     # Wait for the page to load its content
#     print("-> Waiting for page content to load...")
#     time.sleep(5) 
    
#     # Get the page source after JavaScript has loaded
#     page_source = driver.page_source
#     print("-> Page source captured.")
    
#     # Save the HTML to a file for inspection
#     with open("debug_page.html", "w", encoding="utf-8") as f:
#         f.write(page_source)
#     print("-> HTML saved to debug_page.html. Please inspect this file.")
    
# finally:
#     driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import requests
# import os

# URL = "https://www.asos.com/men/new-in/new-in-clothing/cat/?cid=6993"

# print("Stage 1: Setting up automated browser with Selenium...")
# try:
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get(URL)
#     # Increased wait time to ensure all elements, especially lazy-loaded ones, appear
#     print("-> Waiting 7 seconds for page content to fully load...")
#     time.sleep(7) 
#     page_source = driver.page_source
#     print("-> Page source captured.")
# finally:
#     driver.quit()

# print("\nStage 2: Parsing HTML response...")
# soup = BeautifulSoup(page_source, 'html.parser')
# print("-> HTML parsed.")

# print("\nStage 3: Finding product containers...")
# products = soup.find_all('div', class_='productHeroContainer_dVvdX')
# print(f"-> Found {len(products)} product containers.")

# # --- START OF DEBUG BLOCK ---
# # This will print the HTML of the first product and then stop the script.
# if products:
#     print("\n--- DEBUG: HTML of the first product container ---")
#     # .prettify() makes the HTML output clean and easy to read
#     print(products[0].prettify())
#     print("--- END DEBUG ---")
#     print("\nScript stopped for debugging. Inspect the HTML above to find the correct img tag/attribute.")
# else:
#     print("\nNo product containers were found to debug.")

# # The script will stop here, allowing you to inspect the output.
# exit()
# # --- END OF DEBUG BLOCK ---


# # The code below will not run until you remove the exit() command above.
# print("\nStage 4: Starting image download loop...")

# if not os.path.exists('images'):
#     os.makedirs('images')

# for i, product in enumerate(products):
#     img_tag = product.find('img')
    
#     if img_tag and 'srcset' in img_tag.attrs:
#         img_url = img_tag['attrs']['srcset'].split(', ')[-1].split(' ')[0]
#     elif img_tag and 'src' in img_tag.attrs:
#         img_url = img_tag['src']
#     else:
#         print(f"-> No image found for product {i+1}. Skipping.")
#         continue

#     if img_url.startswith('//'):
#         img_url = 'https:' + img_url

#     try:
#         img_data = requests.get(img_url).content
#         with open(f'images/product_{i}.jpg', 'wb') as handler:
#             handler.write(img_data)
#         print(f"-> Downloaded image {i+1}/{len(products)}: product_{i}.jpg")
#         time.sleep(0.1)
#     except requests.exceptions.RequestException as e:
#         print(f"-> Could not download {img_url}. Error: {e}")

# print("\nScraping complete.")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import requests
# import os

# URL = "https://www.asos.com/men/new-in/new-in-clothing/cat/?cid=6993"

# print("Stage 1: Setting up automated browser with Selenium...")
# try:
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get(URL)
#     print("-> Waiting 7 seconds for page content to fully load...")
#     time.sleep(7) 
#     page_source = driver.page_source
#     print("-> Page source captured.")
# finally:
#     driver.quit()

# print("\nStage 2: Parsing HTML response...")
# soup = BeautifulSoup(page_source, 'html.parser')
# print("-> HTML parsed.")

# print("\nStage 3: Finding product containers...")
# products = soup.find_all('div', class_='productHeroContainer_dVvdX')
# print(f"-> Found {len(products)} product containers.")

# if not os.path.exists('images'):
#     os.makedirs('images')

# if not products:
#     print("\nNo products found. The website's HTML may have changed.")
# else:
#     print("\nStage 4: Starting image download loop...")
#     for i, product in enumerate(products):
#         img_tag = product.find('img')
        
#         # --- THIS IS THE CORRECTED LOGIC ---
#         # Prioritize the 'srcset' attribute for the high-res image
#         if img_tag and 'srcset' in img_tag.attrs:
#             # Access 'srcset' directly. This was the fix.
#             img_url = img_tag['srcset'].split(', ')[-1].split(' ')[0]
#         elif img_tag and 'src' in img_tag.attrs:
#             # Fallback to the 'src' attribute if srcset doesn't exist
#             img_url = img_tag['src']
#         else:
#             print(f"-> No image found for product {i+1}. Skipping.")
#             continue

#         # Ensure the URL has the 'https:' protocol
#         if img_url.startswith('//'):
#             img_url = 'https:' + img_url

#         try:
#             img_data = requests.get(img_url).content
#             with open(f'images/product_{i}.jpg', 'wb') as handler:
#                 handler.write(img_data)
#             print(f"-> Downloaded image {i+1}/{len(products)}: product_{i}.jpg")
#             time.sleep(0.1)
#         except requests.exceptions.RequestException as e:
#             print(f"-> Could not download {img_url}. Error: {e}")

# print("\nScraping complete.")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import os
# import base64 # We need this to decode the image data from the browser

# URL = "https://www.asos.com/men/new-in/new-in-clothing/cat/?cid=6993"

# print("Stage 1: Setting up automated browser...")
# try:
#     # Use headless mode to prevent the browser window from appearing
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless=new")
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     driver.get(URL)
#     print("-> Waiting 7 seconds for page content to fully load...")
#     time.sleep(7)
    
#     page_source = driver.page_source
#     print("-> Page source captured.")

#     print("\nStage 2: Parsing HTML response...")
#     soup = BeautifulSoup(page_source, 'html.parser')
#     print("-> HTML parsed.")

#     print("\nStage 3: Finding product containers...")
#     products = soup.find_all('div', class_='productHeroContainer_dVvdX')
#     print(f"-> Found {len(products)} product containers.")

#     if not os.path.exists('images'):
#         os.makedirs('images')

#     if not products:
#         print("\nNo products found. The website's HTML may have changed.")
#     else:
#         print("\nStage 4: Starting image download loop via browser...")
        
#         for i, product in enumerate(products):
#             img_tag = product.find('img')
            
#             if img_tag and 'srcset' in img_tag.attrs:
#                 img_url = img_tag['srcset'].split(', ')[-1].split(' ')[0]
#             else:
#                 print(f"-> No image found for product {i+1}. Skipping.")
#                 continue

#             if img_url.startswith('//'):
#                 img_url = 'https:' + img_url

#             try:
#                 # --- THIS IS THE NEW DOWNLOAD METHOD ---
#                 # JavaScript to fetch the image and convert it to a Base64 string
#                 js_script = """
#                     return await fetch(arguments[0])
#                       .then(response => response.blob())
#                       .then(blob => new Promise(resolve => {
#                         const reader = new FileReader();
#                         reader.onload = () => resolve(reader.result);
#                         reader.readAsDataURL(blob);
#                       }));
#                 """
                
#                 # Execute the script and get the Base64 data
#                 image_data_base64 = driver.execute_script(js_script, img_url)
                
#                 # Decode the Base64 string to get the raw image bytes
#                 # The result from the browser is "data:image/jpeg;base64,....", so we split and take the second part
#                 image_bytes = base64.b64decode(image_data_base64.split(',')[1])

#                 with open(f'images/product_{i}.jpg', 'wb') as handler:
#                     handler.write(image_bytes)
#                 print(f"-> Downloaded image {i+1}/{len(products)}: product_{i}.jpg")
                
#             except Exception as e:
#                 print(f"-> Could not download {img_url}. Error: {e}")

# finally:
#     if 'driver' in locals():
#         driver.quit()

# print("\nScraping complete.")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
import base64

URL = "https://www.asos.com/men/new-in/new-in-clothing/cat/?cid=6993"
driver = None # Define driver in the global scope

print("Stage 1: Setting up automated browser...")
try:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(URL)
    
    print("-> Page loaded. Scrolling down to load all images...")
    scroll_pause_time = 2
    scrolls = 5
    
    for i in range(scrolls):
        driver.execute_script("window.scrollBy(0, 1000);")
        print(f"-> Scrolled down ({i+1}/{scrolls})... waiting for content to load.")
        time.sleep(scroll_pause_time)
        
    print("-> Scrolling complete.")
    
    page_source = driver.page_source
    print("-> Page source captured.")

    # --- MOVED LOGIC INSIDE THE TRY BLOCK ---

    print("\nStage 2: Parsing HTML response...")
    soup = BeautifulSoup(page_source, 'html.parser')
    print("-> HTML parsed.")

    print("\nStage 3: Finding product containers...")
    products = soup.find_all('div', class_='productHeroContainer_dVvdX')
    print(f"-> Found {len(products)} product containers.")

    if not os.path.exists('images'):
        os.makedirs('images')

    if not products:
        print("\nNo products found. The website's HTML may have changed.")
    else:
        print("\nStage 4: Starting image download loop via browser...")
        
        for i, product in enumerate(products):
            img_tag = product.find('img')
            
            if img_tag and 'srcset' in img_tag.attrs and img_tag['srcset']:
                img_url = img_tag['srcset'].split(', ')[-1].split(' ')[0]
            else:
                print(f"-> No valid image srcset found for product {i+1}. Skipping.")
                continue

            if img_url.startswith('//'):
                img_url = 'https:' + img_url

            try:
                js_script = """
                    return await fetch(arguments[0])
                      .then(response => response.blob())
                      .then(blob => new Promise(resolve => {
                        const reader = new FileReader();
                        reader.onload = () => resolve(reader.result);
                        reader.readAsDataURL(blob);
                      }));
                """
                
                image_data_base64 = driver.execute_script(js_script, img_url)
                image_bytes = base64.b64decode(image_data_base64.split(',')[1])

                with open(f'images/product_{i}.jpg', 'wb') as handler:
                    handler.write(image_bytes)
                print(f"-> Downloaded image {i+1}/{len(products)}: product_{i}.jpg")
                
            except Exception as e:
                print(f"-> Could not download {img_url}. Error: {e}")

finally:
    # This block will now run at the very end, after everything else is done.
    if driver:
        driver.quit()
        print("\nBrowser closed.")

print("\nScraping complete.")