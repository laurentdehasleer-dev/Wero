with open('cartes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: form-row responsive
old_form_row = """        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }"""

new_form_row = """        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        
        @media (max-width: 480px) {
            .form-row {
                grid-template-columns: 1fr;
            }
        }"""

content = content.replace(old_form_row, new_form_row)

# Fix 2: form-container padding on mobile
old_form_container = """        .form-container {
            background-color: var(--wero-yellow);
            border: 1px solid var(--black);
            border-radius: 1rem;
            width: 100%;
            max-width: 550px;
            padding: 2.5rem 1.5rem;
        }

        @media (min-width: 768px) { .form-container { padding: 3rem 3rem; } }"""

new_form_container = """        .form-container {
            background-color: var(--wero-yellow);
            border: 1px solid var(--black);
            border-radius: 1rem;
            width: 100%;
            max-width: 550px;
            padding: 1.5rem 1rem;
        }

        @media (min-width: 480px) { .form-container { padding: 2rem 1.5rem; } }
        @media (min-width: 768px) { .form-container { padding: 3rem 3rem; } }"""

content = content.replace(old_form_container, new_form_container)

# Fix 3: back button position
old_back_btn = """        @media (max-width: 768px) {
            .back-to-bank-btn {
                top: 70px;
                left: 15px;
                padding: 8px 14px;
                font-size: 11px;
                z-index: 1001;
            }
        }"""

new_back_btn = """        @media (max-width: 768px) {
            .back-to-bank-btn {
                top: 60px;
                left: 10px;
                padding: 8px 12px;
                font-size: 11px;
                z-index: 1001;
            }
        }
        
        @media (max-width: 480px) {
            .back-to-bank-btn {
                top: 55px;
                left: 8px;
                padding: 6px 10px;
                font-size: 10px;
            }
        }"""

content = content.replace(old_back_btn, new_back_btn)

# Fix 4: main padding on mobile
old_main = """        main {
            flex: 1;
            width: 100%;
            max-width: 1280px;
            margin: 0 auto;
            padding: 4rem 1.25rem 6rem;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        @media (min-width: 468px) { main { padding-top: 6rem; padding-bottom: 8rem; } }"""

new_main = """        main {
            flex: 1;
            width: 100%;
            max-width: 1280px;
            margin: 0 auto;
            padding: 2rem 0.75rem 4rem;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        @media (min-width: 480px) { main { padding: 3.5rem 1rem 6rem; } }
        @media (min-width: 768px) { main { padding: 4rem 1.25rem 6rem; } }"""

content = content.replace(old_main, new_main)

# Fix 5: page-title font size on mobile
old_title = """        .page-title {
            font-size: 1.75rem;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: -0.05em;
            line-height: 0.9;
            color: var(--black);
            text-align: center;
            margin-bottom: 1rem;
        }

        @media (min-width: 768px) { .page-title { font-size: 2.5rem; } }"""

new_title = """        .page-title {
            font-size: 1.25rem;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: -0.05em;
            line-height: 0.9;
            color: var(--black);
            text-align: center;
            margin-bottom: 1rem;
        }

        @media (min-width: 480px) { .page-title { font-size: 1.5rem; } }
        @media (min-width: 768px) { .page-title { font-size: 2.5rem; } }"""

content = content.replace(old_title, new_title)

with open('cartes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed cartes.html responsive design")
