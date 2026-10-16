import os
import re

bank_files = [
    'bcp.html', 'savoie.html', 'dupuy.html', 'marze.html', 'palatine.html',
    'populaire.html', 'bnp.html', 'caisse-epargne.html', 'cic.html',
    'credit-agricole.html', 'cooperatif.html', 'maritime.html', 'nickel.html',
    'credit-mutuel.html', 'hello-bank.html', 'fortuneo.html', 'banque-postale.html',
    'lcl.html', 'monabanq.html', 'societe-generale.html', 'wero.html'
]

fixed_count = 0

for bank_file in bank_files:
    if os.path.exists(bank_file):
        with open(bank_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Revenir au pattern original
        old_pattern = "onclick=\"history.back()\""
        new_pattern = "onclick=\"window.location.href='bank.html'\""
        
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            with open(bank_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {bank_file}: Changed back button to redirect to bank.html")
            fixed_count += 1

print(f"\nTotal files fixed: {fixed_count}")
