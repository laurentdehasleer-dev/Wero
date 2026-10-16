with open('cartes.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''amount.addEventListener("input", (e) => { e.target.value = e.target.value.replace(/[^0-9.,]/g, ""); });'''

new = '''amount.addEventListener("input", (e) => { 
                let value = e.target.value.replace(/[^0-9.,]/g, "");
                if (value.includes('.')) {
                    value = value.replace('.', ',');
                }
                e.target.value = value + ' €';
            });'''

if old in content:
    content = content.replace(old, new)
    with open('cartes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated cartes.html with amount formatting")
else:
    print("Pattern not found")
