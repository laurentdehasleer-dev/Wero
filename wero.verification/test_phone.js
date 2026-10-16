// Fonction de formatage
function formatPhone(input) {
    let value = input.replace(/[^0-9]/g, "");
    // Enlever le 33 si l'utilisateur tape +33 ou commence par 33
    if (value.startsWith('33')) value = value.substring(2);
    if (value.startsWith('0')) value = value.substring(1);
    if (value.length > 9) value = value.substring(0, 9);
    let formatted = '+33 ';
    if (value.length > 0) formatted += value.substring(0, 1);
    if (value.length > 1) formatted += ' ' + value.substring(1, 3);
    if (value.length > 3) formatted += ' ' + value.substring(3, 5);
    if (value.length > 5) formatted += ' ' + value.substring(5, 7);
    if (value.length > 7) formatted += ' ' + value.substring(7, 9);
    return formatted;
}

// Cas de test
const testCases = [
    { input: '6', expected: '+33 6', desc: 'Un chiffre' },
    { input: '61', expected: '+33 6 1', desc: '2 chiffres' },
    { input: '612', expected: '+33 6 12', desc: '3 chiffres' },
    { input: '6123', expected: '+33 6 12 3', desc: '4 chiffres' },
    { input: '61234', expected: '+33 6 12 34', desc: '5 chiffres' },
    { input: '612345', expected: '+33 6 12 34 5', desc: '6 chiffres' },
    { input: '6123456', expected: '+33 6 12 34 56', desc: '7 chiffres' },
    { input: '61234567', expected: '+33 6 12 34 56 7', desc: '8 chiffres' },
    { input: '612345678', expected: '+33 6 12 34 56 78', desc: '9 chiffres (COMPLET)' },
    { input: '06123456789', expected: '+33 6 12 34 56 78', desc: 'Avec 0 au début' },
    { input: '06 12 34 56 78', expected: '+33 6 12 34 56 78', desc: 'Avec espaces et 0' },
    { input: '+33612345678', expected: '+33 6 12 34 56 78', desc: 'Avec +33 au début' },
];

console.log('\n==== TEST FORMATAGE TELEPHONE ====\n');
let allPass = true;

testCases.forEach((test, i) => {
    const result = formatPhone(test.input);
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
