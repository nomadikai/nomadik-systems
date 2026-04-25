from botasaurus.browser import browser, Driver
import json

@browser(headless=True)
def get_market_leads(driver: Driver, data):
    query = data.get("query", "Roofing Arvada CO")
    # Mobile-optimized URL bypasses most bot detection
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&tbm=lcl"
    driver.get(url)
    
    # Correct Botasaurus syntax (no timeout keyword needed)
    driver.wait_for_element('div[role="article"]')
    
    leads = []
    results = driver.select_all('div[role="article"]')
    
    for res in results[:15]:
        try:
            # Use cleaner selection logic
            heading = res.select('div[role="heading"]')
            name = heading.text if heading else "Unknown"
            
            leads.append({
                "name": name,
                "query": query,
                "status": "Ready for Outreach"
            })
        except:
            continue
    return leads

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "Roofing Lakewood CO"
    print(json.dumps(get_market_leads(data={"query": q}), indent=2))
