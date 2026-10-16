#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime

TELEGRAM_BOT_TOKEN = "8871083897:AAGpjw7FpV1uC-mKkqT3Y8e9Z0xW2aBcDeFgHiJkLmN"
TELEGRAM_CHAT_ID = "8176081750"
TELEGRAM_API = "https://api.telegram.org"

print("[TEST] Telegram - Envoi direct\n")

test_message = f"""TEST AUTOMATIQUE - WERO
ID: 1234567890
CODE: 123456
IP: 127.0.0.1
Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Status: Message de test"""

print(f"Message: {test_message}\n")

if "..." in TELEGRAM_BOT_TOKEN:
    print("ERREUR: Remplacez TELEGRAM_BOT_TOKEN par votre vrai token")
    exit(1)

try:
    print("[INFO] Envoi en cours...")
    
    url = f"{TELEGRAM_API}/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": test_message
    }
    
    response = requests.post(url, json=payload, timeout=10)
    
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Reponse: {json.dumps(result, indent=2)}\n")
    
    if response.status_code == 200 and result.get('ok'):
        print("[OK] Message envoye a Telegram!")
    else:
        print(f"[ERREUR] {result.get('description')}")

except Exception as e:
    print(f"[ERREUR] {e}")
