from hyperliquid.exchange import Exchange  # Make sure you're using correct import from the SDK
import os
import time
from db import leagues_table
from tinydb import Query

# Instantiate Hyperliquid client
client = Exchange(wallet=None, base_url="https://api.hyperliquid.xyz")

def fetch_pnl(wallet_address: str):
    """
    Fetch the PnL for a specific wallet on Hyperliquid.
    """
    try:
        account = client.get_account(wallet_address)
        return account.get('pnl', 0)
    except Exception as e:
        print(f"Error fetching PnL for {wallet_address}: {e}")
        return None

def sync_pnls_periodically():
    while True:
        leagues = leagues_table.all()
        for league in leagues:
            for participant in league["participants"]:
                pnl = fetch_pnl(participant)
                if pnl is not None:
                    leagues_table.update({"pnl": pnl}, Query().join_code == league["join_code"])
        time.sleep(300)  # Sync every 5 minutes
