from botasaurus.browser import browser, Driver
import time

@browser(headless=False)
def accela_audit(driver: Driver, data):
    try:
        driver.get('https://www.denvergov.org/AccelaCitizenAccess/Cap/CapHome.aspx?module=Building&TabName=Building')
        time.sleep(10)
        
        print(f'Landed on: {driver.title}')
        
        # Look for the search button or the terms gate
        search_btn = driver.select('a#ctl00_PlaceHolderMain_btnNewSearch')
        if search_btn:
            print('SUCCESS: Search button found.')
        elif 'accept' in driver.page_html.lower():
            print('ALERT: Terms and Conditions gate detected.')
        else:
            print('FAILURE: Content not found. Page might be blank.')
            
        with open('debug_accela.html', 'w') as f:
            f.write(driver.page_html)
    except Exception as e:
        print(f'ERROR: {e}')

if __name__ == "__main__":
    accela_audit()
