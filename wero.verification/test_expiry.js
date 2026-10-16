// Fonction pour valider que la date d'expiration est dans le futur
function isExpiryDateValid(expiryStr) {
    // Format: MM/AA
    if (!expiryStr || expiryStr.length !== 5 || !expiryStr.includes('/')) {
        return { valid: false, message: 'Format invalide (MM/AA)' };
    }
    
    const [monthStr, yearStr] = expiryStr.split('/');
    const month = parseInt(monthStr, 10);
    const year = parseInt(yearStr, 10);
    
    // Valider le mois (01-12)
    if (isNaN(month) || month < 1 || month > 12) {
        return { valid: false, message: 'Mois invalide (01-12)' };
    }
    
    // Valider l'année (2 chiffres)
    if (isNaN(year) || yearStr.length !== 2) {
        return { valid: false, message: 'Année invalide (AA)' };
    }
    
    // Convertir AA en année complète (assume 20XX)
    const fullYear = 2000 + year;
    
    // Créer une date pour le dernier jour du mois d'expiration à 23:59:59
    const expiryDate = new Date(fullYear, month, 0, 23, 59, 59);
    
    // Obtenir la date actuelle
    const today = new Date();
    
    // Vérifier si la date d'expiration est dans le futur
    if (expiryDate < today) {
        return { 
            valid: false, 
            message: 'Carte expirée (expiration: ' + monthStr + '/' + yearStr + ')' 
        };
    }
    
    return { valid: true, message: 'Date valide' };
}

// Cas de test
const today = new Date();
const currentMonth = String(today.getMonth() + 1).padStart(2, '0');
const currentYear = String(today.getFullYear()).slice(-2);
const futureYear = String(today.getFullYear() + 2).slice(-2);

const testCases = [
    { input: '12/' + futureYear, expected: true, desc: 'Décembre 2028 (futur)' },
    { input: '12/27', expected: true, desc: 'Décembre 2027 (futur)' },
    { input: currentMonth + '/' + currentYear, expected: true, desc: 'Mois/année actuel (valide)' },
    { input: '01/24', expected: false, desc: 'Janvier 2024 (passé)' },
    { input: '12/23', expected: false, desc: 'Décembre 2023 (passé)' },
    { input: '00/25', expected: false, desc: 'Mois 00 (invalide)' },
    { input: '13/25', expected: false, desc: 'Mois 13 (invalide)' },
    { input: '12/2', expected: false, desc: 'Année avec 1 chiffre (invalide)' },
];

console.log('\n==== TEST VALIDATION EXPIRATION ====\n');
let allPass = true;

testCases.forEach((test, i) => {
    const result = isExpiryDateValid(test.input);
    const pass = result.valid === test.expected;
    allPass = allPass && pass;
    
    const icon = pass ? 'PASS' : 'FAIL';
    console.log(`[${icon}] Test ${i+1}: ${test.desc}`);
    console.log(`  Input:    "${test.input}"`);
    console.log(`  Expected: ${test.expected}`);
    console.log(`  Got:      ${result.valid} (${result.message})`);
    console.log('');
});

console.log('====================');
console.log(allPass ? 'TOUS LES TESTS PASSENT!' : 'DES TESTS ECHOUENT');
console.log('====================\n');
