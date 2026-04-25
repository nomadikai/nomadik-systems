def scrape_roofing_permits(driver, params):
    driver.get("https://etrakit.lakewood.org/eTRAKiT/Search/permit.aspx")
    driver.select('#cphMain_ctl00_ddlSearchType', value='PERMIT')
    driver.type('#cphMain_ctl00_txtSearchString', 'ROOF')
    driver.click('#cphMain_ctl00_btnSearch')
    print(f"[*] Navigated to Lakewood Roofing for {params['zip_code']}")
    return {"leads": [], "trade": "Roofing"}
