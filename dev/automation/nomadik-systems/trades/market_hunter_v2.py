from botasaurus.browser import browser, Driver
import json

@browser(headless=True)
def extract_leads(driver: Driver, data):
    # Direct search for trade businesses in Arvada/Lakewood
    url = "https://www.google.com/search?q=Roofing+Contractors+Lakewood+CO&tbm=lcl"
    driver.get(url)
    
    # Wait for the main results container
    driver.wait_for_element('body')
    
    leads = []
    # Target all link elements that likely contain business names in the Lite view
    potential_names = driver.select_all('div, span, a')
    
    # Heuristic: Find elements that look like business titles
    for el in potential_names:
        text = el.text.strip()
        # Look for common contractor keywords to filter noise
        if any(word in text.lower() for word in ['roofing', 'construction', 'exteriors', 'plumbing']):
            if len(text) > 5 and len(text) < 50:
                leads.append({"name": text, "status": "Lead Found"})
    
    # Deduplicate
    unique_leads = list({v['name']:v for v in leads}.values())
    return unique_leads[:15]

if __name__ == "__main__":
    print(json.dumps(extract_leads(), indent=2))
