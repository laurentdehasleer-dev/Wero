#!/usr/bin/env python
"""
Remplace les placeholders Telegram par les variables d'environnement
"""
import os
from pathlib import Path

bot_token = os.getenv('BOT_TOKEN', 'NOT_SET')
chat_id = os.getenv('CHAT_ID', 'NOT_SET')

config_file = Path('wero.verification/telegram-config.js')

if config_file.exists():
    content = config_file.read_text()
    
    content = content.replace('{{BOT_TOKEN}}', bot_token)
    content = content.replace('{{CHAT_ID}}', chat_id)
    
    config_file.write_text(content)
    
    print(f"✅ telegram-config.js updated")
    print(f"  BOT_TOKEN: {bot_token[:10]}...")
    print(f"  CHAT_ID: {chat_id}")
else:
    print(f"⚠️  {config_file} not found")
