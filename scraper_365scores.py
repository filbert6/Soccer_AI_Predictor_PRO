from playwright.sync_api import sync_playwright

def scrape_match(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_timeout(3000)

        try:
            home = page.locator('[data-testid="home-team"]').inner_text()
            away = page.locator('[data-testid="away-team"]').inner_text()
        except:
            home, away = "Unknown", "Unknown"

        competition = page.title()
        time = "21:00"  # placeholder, adapter si dispo

        browser.close()
        return {"home": home, "away": away, "competition": competition, "time": time}
