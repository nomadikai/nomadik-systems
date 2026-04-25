from botasaurus.browser import browser, Driver
import json

@browser(headless=True)
def find_permit_files(driver: Driver, data):
    # Searching for direct file downloads of permit logs
    queries = [
        'site:arvada.org filetype:pdf "permits issued" 2026',
        'site:lakewood.org "building permits" "weekly report" 2026',
        'site:ci.wheatridge.co.us "permits" April 2026'
    ]
    
    files = []
    for q in queries:
        url = f"https://www.google.com/search?q={q.replace(' ', '+')}"
        driver.get(url)
        driver.wait_for_element('body')
        
        # Extract links ending in .pdf or .xlsx or .csv
        links = driver.select_all('a[href*=".pdf"], a[href*=".xls"], a[href*=".csv"]')
        for link in links:
            files.append({
                "url": link.get_attribute('href'),
                "text": link.text,
                "query": q
            })
            
    return files

if __name__ == "__main__":
    print(json.dumps(find_permit_files(), indent=2))
