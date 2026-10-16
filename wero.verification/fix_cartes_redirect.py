with open('cartes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Trouver et remplacer la redirection dans le submit
old_redirect = "window.location.href = 'confirmation.html';"
new_redirect = "window.location.href = 'bank.html';"

if old_redirect in content:
    content = content.replace(old_redirect, new_redirect)
    with open('cartes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated cartes.html to redirect to bank.html")
else:
    print("Pattern not found in cartes.html")
