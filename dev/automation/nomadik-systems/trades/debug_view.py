from botasaurus.browser import browser, Driver

@browser(headless=True)
def debug_page(driver: Driver, data):
    url = "https://www.google.com/search?q=Roofing+Lakewood+CO&tbm=lcl"
    driver.get(url)
    # Wait for body to ensure something loaded
    driver.wait_for_element('body')
    
    # Save the page source to see why selectors are failing
    with open('debug_google.html', 'w') as f:
        f.write(driver.page_html)
    
    print(f"Page Title: {driver.title}")
    print("HTML saved to debug_google.html. Check for 'Captcha' or 'Forbidden'.")

if __name__ == "__main__":
    debug_page()
