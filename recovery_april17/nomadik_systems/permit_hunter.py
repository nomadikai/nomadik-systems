from botasaurus.browser import browser, Driver, Wait
import json
from datetime import datetime

@browser(
    reuse_driver=True,
    headless=True,
    block_images=True,
)
def run_harvest(driver: Driver, data):
    # 1. Access the Portal
    url = "https://lakw-trk.aspgov.com/eTRAKiT/Search/permit.aspx"
    driver.google_get(url)
    print(f"[{datetime.now()}] Portal Accessed via Nomadik-C2.")

    # 2. Interact with the ASP.NET Search Form
    try:
        # Search for 'ROOF' in the Search box
        driver.type('#cphMain_txtSearch', 'ROOF')
        # Click the Search button
        driver.click('#cphMain_btnSearch')
        print("Search submitted. Waiting for results...")
        
        # Wait for the results table to load (Wait.SHORT = 4s)
        driver.wait_for_element('#cphMain_rgSearchRslts_ctl00', wait=Wait.SHORT)
    except Exception as e:
        print(f"Interaction Error: {e}")

    # 3. Extract the Table Data
    results = []
    # Selector for the rows in the Telerik RadGrid
    rows = driver.select_all('#cphMain_rgSearchRslts_ctl00 tbody tr')
    
    for row in rows:
        cells = row.select_all('td')
        if len(cells) >= 6:
            results.append({
                "permit_no": cells[0].text.strip(),
                "site_address": cells[1].text.strip(),
                "type": cells[2].text.strip(),
                "status": cells[3].text.strip(),
                "description": cells[4].text.strip(),
                "date_issued": cells[5].text.strip(),
                "timestamp": str(datetime.now())
            })

    return results

if __name__ == "__main__":
    print("Initiating Deep Harvest...")
    results = run_harvest()
    
    output_path = '/home/nomadik/nomadik_systems/leads_harvested.json'
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=4)
        
    print(f"Optimization Complete: {len(results)} leads harvested to {output_path}")
