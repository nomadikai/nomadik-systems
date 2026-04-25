from botasaurus.browser import browser, Driver

@browser(
    headless=True,
    reuse_driver=True,
    block_images=True,
    window_size=(1920, 1080)
)
def run_scraper(driver: Driver, data):
    """Standardized engine to execute trade-specific logic."""
    trade_logic = data.get("logic_func")
    return trade_logic(driver, data.get("params"))
