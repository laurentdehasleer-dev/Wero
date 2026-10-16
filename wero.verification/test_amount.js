// Fonction de formatage montant avec € immuable
function formatAmount(input) {
    let value = input.replace(/[^0-9.,]/g, "");
    
    // Garder seulement chiffres et virgule/point
    let formatted = value;
    
    // Remplacer point par virgule si nécessaire
    if (formatted.includes('.')) {
        formatted = formatted.replace('.', ',');
    }
    
    return formatted + ' €';
}

// Cas de test
const testCases = [
    { input: '5', expected: '5 €', desc: 'Un chiffre' },
    { input: '50', expected: '50 €', desc: 'Deux chiffres' },
    { input: '50.00', expected: '50,00 €', desc: 'Avec décimales' },
    { input: '50,00', expected: '50,00 €', desc: 'Avec virgule' },
    { input: '100€', expected: '100 €', desc: 'Avec € déjà présent' },
    { input: '100.50 €', expected: '100,50 €', desc: 'Avec € et décimales' },
    { input: '1234.56', expected: '1234,56 €', desc: 'Montant plus gros' },
];

console.log('\n==== TEST FORMATAGE MONTANT ====\n');
let allPass = true;

testCases.forEach((test, i) => {
    const result = formatAmount(test.input);
    const pass = result === test.expected;
    allPass = allPass && pass;
    
    const icon = pass ? 'PASS' : 'FAIL';
    console.log(`[${icon}] Test ${i+1}: ${test.desc}`);
    console.log(`  Input:    "${test.input}"`);
    console.log(`  Expected: "${test.expected}"`);
    console.log(`  Got:      "${result}"`);
    console.log('');
});

console.log('====================');
console.log(allPass ? 'TOUS LES TESTS PASSENT!' : 'DES TESTS ECHOUENT');
console.log('====================\n');
