with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: Change mobile-menu from left: 0 to right: 0
old_mobile_menu = """        /* ================= MOBILE MENU ================= */
        #mobile-menu {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
            background-color: var(--white);
            border-bottom: 1px solid var(--gray-medium);
            position: absolute;
            width: 100%;
            left: 0;
            top: 100%;"""

new_mobile_menu = """        /* ================= MOBILE MENU ================= */
        #mobile-menu {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
            background-color: var(--white);
            border-bottom: 1px solid var(--gray-medium);
            position: absolute;
            width: 100%;
            right: 0;
            top: 100%;"""

content = content.replace(old_mobile_menu, new_mobile_menu)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mobile menu position")
