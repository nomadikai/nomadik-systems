from botasaurus.browser import browser, Driver
import json

@browser(headless=True)
def scrape_maps_leads(driver: Driver, data):
    search_query = data.get("query", "Roofing Arvada")
    # Using direct google maps URL for better parsing
    driver.get(f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}")
    
    # Wait for the results to load
    driver.wait_for_element('div[role="feed"]', timeout=30)
    
    leads = []
    results = driver.select_all('a[href*="/maps/place/"]')
    
    for res in results[:10]:
        try:
            name = res.get_attribute("aria-label")
            if name:
                leads.append({"name": name, "source": "Google Maps", "status": "Found"})
        except:
            continue
            
    return leads

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "Plumbers Arvada"
    print(json.dumps(scrape_maps_leads(data={"query": q}), indent=2))
