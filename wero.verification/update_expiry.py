with open('cartes.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_validation = '''const expiryRegex = /^(0[1-9]|1[0-2])\/([0-9]{2})$/;
                if (!expiry.value || !expiryRegex.test(expiry.value)) { addError(expiry, 'error-expiry'); isValid = false; }
                else { removeError(expiry, 'error-expiry'); }'''

new_validation = '''const expiryRegex = /^(0[1-9]|1[0-2])\/([0-9]{2})$/;
                if (!expiry.value || !expiryRegex.test(expiry.value)) { 
                    addError(expiry, 'error-expiry'); 
                    isValid = false; 
                } else {
                    // Verifier que la date est dans le futur
                    const [monthStr, yearStr] = expiry.value.split('/');
                    const month = parseInt(monthStr, 10);
                    const year = parseInt(yearStr, 10);
                    const fullYear = 2000 + year;
                    const expiryDate = new Date(fullYear, month, 0, 23, 59, 59);
                    const today = new Date();
                    
                    if (expiryDate < today) {
                        addError(expiry, 'error-expiry');
                        document.getElementById('error-expiry').textContent = 'Carte expirée';
                        isValid = false;
                    } else {
                        removeError(expiry, 'error-expiry');
                    }
                }'''

if old_validation in content:
    content = content.replace(old_validation, new_validation)
    with open('cartes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated cartes.html with future expiry validation")
else:
    print("Pattern not found")
