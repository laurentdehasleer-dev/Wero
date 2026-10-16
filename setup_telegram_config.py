#!/usr/bin/env python
"""
Remplace les placeholders Telegram dans tous les fichiers HTML
avant de démarrer Flask
"""
import os
import glob
from pathlib import Path

bot_token = os.getenv('BOT_TOKEN', 'NOT_SET')
chat_id = os.getenv('CHAT_ID', 'NOT_SET')

print(f"🔧 Configuring Telegram placeholders:")
print(f"  BOT_TOKEN: {bot_token[:20]}..." if len(bot_token) > 20 else f"  BOT_TOKEN: {bot_token}")
print(f"  CHAT_ID: {chat_id}\n")

html_files = glob.glob('wero.verification/*.html')

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remplacer les deux variantes de placeholders
        content = content.replace('TELEGRAM_BOT_TOKEN_PLACEHOLDER', bot_token)
        content = content.replace('TELEGRAM_CHAT_ID_PLACEHOLDER', chat_id)
        content = content.replace('{{BOT_TOKEN}}', bot_token)
        content = content.replace('{{CHAT_ID}}', chat_id)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ {Path(html_file).name} updated")
        
    except Exception as e:
        print(f"  ⚠️  Error processing {html_file}: {e}")

print()
