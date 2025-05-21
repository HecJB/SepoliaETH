
# SepoliaETH

Automate claiming Sepolia ETH from the [Google Cloud Ethereum Sepolia Faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia) using Python and Playwright.

---

## Overview

This project provides a simple Python script to automate the process of requesting Sepolia testnet ETH from the Google Cloud faucet. It uses Playwright to control a Chromium browser, fill in your Sepolia wallet address, and submit the request.

⚠️ **Note:** The faucet may require manual CAPTCHA solving to prevent abuse. This script pauses to allow you to complete that step.

---

## Features

- Automates browser interaction with the Sepolia faucet webpage.
- Supports manual CAPTCHA solving.
- Easy to customize with your Sepolia wallet address.
- Uses Playwright, a modern browser automation library.

---

## Requirements

- Python 3.7+
- [Playwright for Python](https://playwright.dev/python/)

---

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/HecJB/SepoliaETH.git
   cd SepoliaETH
   ```

2. Install dependencies:

   ```
   pip install playwright
   playwright install
   ```

---

## Usage

1. Open the script `claim_sepolia_eth.py` and replace the placeholder with your Sepolia wallet address:

   ```
   SEPOLIA_ADDRESS = "0xYourSepoliaAddressHere"
   ```

2. Run the script:

   ```
   python claim_sepolia_eth.py
   ```

3. The script will open a Chromium browser window, navigate to the faucet page, fill in your address, and click the "Send" button.

4. If a CAPTCHA appears, solve it manually within the browser window.

5. After 60 seconds, the browser will close automatically.

---

## Example

```
from playwright.sync_api import sync_playwright

SEPOLIA_ADDRESS = "0xYourSepoliaAddressHere"

def claim_sepolia_eth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://cloud.google.com/application/web3/faucet/ethereum/sepolia")
        page.wait_for_selector('input[type="text"]')
        page.fill('input[type="text"]', SEPOLIA_ADDRESS)
        page.click('button:has-text("Send")')
        print("Please solve CAPTCHA if prompted. Waiting for 60 seconds...")
        page.wait_for_timeout(60000)
        browser.close()

if __name__ == "__main__":
    claim_sepolia_eth()
```

---

## Important Notes

- This script is intended for educational and testing purposes only.
- Do not abuse or spam the faucet.
- Always keep your private keys secure and never share them.
- Faucet tokens have no real monetary value.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


