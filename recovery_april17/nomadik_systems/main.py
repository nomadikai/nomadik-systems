import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.engine import run_scraper
from trades.roofing import scrape_roofing_permits
from trades.plumbing import scrape_plumbing_permits

def main():
    print("[!] Initializing Nomadik Systems Scraper Logic...")
    
    # Run Roofing
    roof_results = run_scraper(data={
        "logic_func": scrape_roofing_permits,
        "params": {"zip_code": "80215", "city": "Lakewood"}
    })
    
    # Run Plumbing
    plumb_results = run_scraper(data={
        "logic_func": scrape_plumbing_permits,
        "params": {"zip_code": "80215", "city": "Lakewood"}
    })
    
    print(f"[DONE] Lead-Gen Cycle Complete.")

if __name__ == "__main__":
    main()
