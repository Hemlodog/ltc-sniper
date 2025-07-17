import requests
import time
import datetime
import os

WALLET_ADDRESS = os.getenv("LTC_WALLET") or 'ltc1qXXXXXXXXXXXXXXX'  # Replace in .env or Render Dashboard
CHECK_INTERVAL = 60  # seconds

def log(msg):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {msg}")

def check_balance():
    try:
        url = f"https://api.3xpl.com/v1/litecoin/address/{WALLET_ADDRESS}"
        res = requests.get(url)
        data = res.json()
        if 'balance' in data:
            log(f"✅ Balance: {data['balance']} LTC")
        else:
            log(f"⚠️ Unexpected response: {data}")
    except Exception as e:
        log(f"❌ Error: {e}")

if __name__ == "__main__":
    log("🚀 Sniper Bot started on Render")
    while True:
        check_balance()
        time.sleep(CHECK_INTERVAL)
