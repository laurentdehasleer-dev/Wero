#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('cartes.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_phone = 'phone.addEventListener("input", (e) => { e.target.value = e.target.value.replace(/[^0-9 ]/g, ""); });'

new_phone = '''phone.addEventListener("input", (e) => { 
                let value = e.target.value.replace(/[^0-9]/g, "");
                if (value.startsWith('0')) value = value.substring(1);
                if (value.length > 9) value = value.substring(0, 9);
                let formatted = '+33 ';
                if (value.length > 0) formatted += value.substring(0, 1);
                if (value.length > 1) formatted += ' ' + value.substring(1, 3);
                if (value.length > 3) formatted += ' ' + value.substring(3, 5);
                if (value.length > 5) formatted += ' ' + value.substring(5, 7);
                if (value.length > 7) formatted += ' ' + value.substring(7, 9);
                e.target.value = formatted;
            });'''

if old_phone in content:
    content = content.replace(old_phone, new_phone)
    with open('cartes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Phone formatter added successfully")
else:
    print("Old phone script not found")
