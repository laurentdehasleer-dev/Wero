with open('cartes.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''phone.addEventListener("input", (e) => { 
                let value = e.target.value.replace(/[^0-9]/g, "");
                if (value.startsWith('0')) value = value.substring(1);'''

new = '''phone.addEventListener("input", (e) => { 
                let value = e.target.value.replace(/[^0-9]/g, "");
                if (value.startsWith('33')) value = value.substring(2);
                if (value.startsWith('0')) value = value.substring(1);'''

if old in content:
    content = content.replace(old, new)
    with open('cartes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated cartes.html with +33 handling")
else:
    print("Pattern not found")
