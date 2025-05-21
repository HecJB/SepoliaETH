from playwright.sync_api import sync_playwright

# Replace with your Sepolia wallet address
SEPOLIA_ADDRESS = "0xYourSepoliaAddressHere"

def claim_sepolia_eth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to run in background
        page = browser.new_page()
        page.goto("https://cloud.google.com/application/web3/faucet/ethereum/sepolia")

        # Wait for page to load and find the address input
        page.wait_for_selector('input[type="text"]')
        page.fill('input[type="text"]', SEPOLIA_ADDRESS)

        # Click the submit/request button (may need to adjust selector)
        page.click('button:has-text("Send")')

        # Wait for confirmation or manual CAPTCHA solving
        print("Please solve CAPTCHA if prompted. Waiting for 60 seconds...")
        page.wait_for_timeout(60000)  # Wait 60 seconds

        browser.close()

if __name__ == "__main__":
    claim_sepolia_eth()
