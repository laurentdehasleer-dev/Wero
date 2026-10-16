with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: Change align-items: center to align-items: flex-start for mobile menu
content = content.replace(
    "            align-items: center;\n            gap: 0.5rem;\n            background-color: var(--white);\n            border-bottom: 1px solid var(--gray-medium);\n            position: absolute;\n            width: 100%;\n            right: 0;",
    "            align-items: flex-start;\n            gap: 0.5rem;\n            background-color: var(--white);\n            border-bottom: 1px solid var(--gray-medium);\n            position: absolute;\n            width: 100%;\n            right: 0;"
)

# Fix: Change text-align from center to left and padding for mobile items
content = content.replace(
    "        .mobile-menu-item {\n            width: 100%;\n            text-align: center;\n            padding: 0.75rem 0;",
    "        .mobile-menu-item {\n            width: 100%;\n            text-align: left;\n            padding: 0.75rem 1.25rem;"
)

# Fix: Change text-align and padding for mobile-menu-fr
content = content.replace(
    "        #mobile-menu-fr {\n            width: 100%;\n            text-align: center;\n            padding: 1rem 0;",
    "        #mobile-menu-fr {\n            width: 100%;\n            text-align: left;\n            padding: 1rem 1.25rem;"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mobile menu alignment")
