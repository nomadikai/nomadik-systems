from botasaurus.browser import browser, Driver
import time
import json

@browser(headless=True)
def scrape_map_data(driver: Driver, data):
    # Arvada's Interactive Development Map often lists active permits
    # This is a high-value side-door for fresh addresses
    url = "https://arvada.org/about/maps/interactive-maps"
    driver.get(url)
    time.sleep(5)
    
    leads = []
    # Attempt to find links or text that indicate current projects
    elements = driver.select_all('a, span, div')
    for el in elements:
        text = el.text.strip()
        # Look for "Permit", "Project", or "Address" patterns
        if any(key in text for key in ["Permit", "Active", "Development"]):
            leads.append({"content": text, "source": "Arvada Map Portal"})
            
    return leads[:10]

if __name__ == "__main__":
    print(json.dumps(scrape_map_data(), indent=2))
