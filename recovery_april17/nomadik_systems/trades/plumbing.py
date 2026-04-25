def scrape_plumbing_permits(driver, params):
    driver.get("https://etrakit.lakewood.org/eTRAKiT/Search/permit.aspx")
    driver.select('#cphMain_ctl00_ddlSearchType', value='PERMIT')
    driver.type('#cphMain_ctl00_txtSearchString', 'PLUMB')
    driver.click('#cphMain_ctl00_btnSearch')
    print(f"[*] Navigated to Lakewood Plumbing for {params['city']}")
    return {"leads": [], "trade": "Plumbing"}
