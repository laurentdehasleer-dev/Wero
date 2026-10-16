// Script pour formater le montant en euros
document.addEventListener('DOMContentLoaded', () => {
    const amountInput = document.getElementById('amount');
    
    if (amountInput) {
        amountInput.addEventListener('input', (e) => {
            // Récupérer seulement les chiffres
            let value = e.target.value.replace(/[^0-9.]/g, "");
            
            // Gérer le point décimal
            if (value.includes('.')) {
                let parts = value.split('.');
                value = parts[0] + '.' + parts[1].substring(0, 2);
            }
            
            // Formater avec 2 décimales
            if (value && !isNaN(value)) {
                let num = parseFloat(value);
                e.target.value = num.toFixed(2) + ' €';
            } else {
                e.target.value = value;
            }
        });
    }
});
