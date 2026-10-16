import os
import re

# Lister tous les fichiers HTML de banques
bank_files = [
    'bcp.html', 'savoie.html', 'dupuy.html', 'marze.html', 'palatine.html',
    'populaire.html', 'bnp.html', 'caisse-epargne.html', 'cic.html',
    'credit-agricole.html', 'cooperatif.html', 'maritime.html', 'nickel.html',
    'credit-mutuel.html', 'hello-bank.html', 'fortuneo.html', 'banque-postale.html',
    'lcl.html', 'monabanq.html', 'societe-generale.html', 'wero.html'
]

print("Checking redirects in bank files:\n")
redirect_pattern = r"window\.location\.href\s*=\s*['\"]([^'\"]+)['\"]"
needs_fix = []

for bank_file in bank_files:
    if os.path.exists(bank_file):
        with open(bank_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        matches = re.findall(redirect_pattern, content)
        if matches:
            for match in matches:
                if 'confirmation.html' in match:
                    print(f"OK {bank_file}: redirects to confirmation.html")
                else:
                    print(f"NEED FIX {bank_file}: redirects to {match}")
                    needs_fix.append((bank_file, match))
        else:
            print(f"NO REDIRECT {bank_file}")
    else:
        print(f"NOT FOUND {bank_file}")

print(f"\nTotal files needing fix: {len(needs_fix)}")
for file, redirect in needs_fix:
    print(f"  - {file} -> {redirect}")
