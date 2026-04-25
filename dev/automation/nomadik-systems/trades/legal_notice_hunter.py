from botasaurus.browser import browser, Driver
import json

@browser(headless=True)
def get_legal_notices(driver: Driver, data):
    # Searching for official legal publications of permits in Denver Metro
    queries = [
        'site:denvergov.org "building permit" "issued"',
        'site:arvada.org "permit" "granted"',
        '"building permit" Lakewood CO "issued"'
    ]
    
    leads = []
    for q in queries:
        url = f"https://www.google.com/search?q={q.replace(' ', '+')}&tbs=qdr:w"
        driver.get(url)
        driver.wait_for_element('body')
        
        # Capture snippet text which often contains the address/owner
        results = driver.select_all('div.vv77sc, div.VwiC3b')
        for res in results:
            leads.append({"text": res.text, "source": "Public Notice"})
            
    return leads

if __name__ == "__main__":
    print(json.dumps(get_legal_notices(), indent=2))
