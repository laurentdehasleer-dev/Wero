import re

with open('cartes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Update viewport meta tag
old_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
new_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">'
content = content.replace(old_viewport, new_viewport)

# Fix 2: Change input font-size from 0.875rem to 16px (prevents iOS auto-zoom)
old_input = """        .form-group input {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid var(--black);
            border-radius: 0.5rem;
            background-color: var(--white);
            font-family: inherit;
            font-size: 0.875rem;
            font-weight: 500;
            color: var(--black);
            outline: none;
            transition: box-shadow 0.2s;
            text-align: left;
        }"""

new_input = """        .form-group input {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid var(--black);
            border-radius: 0.5rem;
            background-color: var(--white);
            font-family: inherit;
            font-size: 16px;
            font-weight: 500;
            color: var(--black);
            outline: none;
            transition: box-shadow 0.2s;
            text-align: left;
            -webkit-appearance: none;
            appearance: none;
        }"""

content = content.replace(old_input, new_input)

# Fix 3: Add prevent zoom on input:focus
old_focus = """        .form-group input:focus {
            box-shadow: 0 0 0 2px rgba(0,0,0,0.1);
        }"""

new_focus = """        .form-group input:focus {
            box-shadow: 0 0 0 2px rgba(0,0,0,0.1);
            transform: none;
        }"""

content = content.replace(old_focus, new_focus)

# Fix 4: Add style for body to prevent zoom on select/textarea
old_body = """        body {
            background-color: var(--white);
            color: var(--black);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }"""

new_body = """        body {
            background-color: var(--white);
            color: var(--black);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            -webkit-touch-callout: none;
        }
        
        input, select, textarea {
            font-size: 16px;
            -webkit-appearance: none;
            appearance: none;
        }"""

content = content.replace(old_body, new_body)

# Fix 5: Prevent pinch zoom on all elements
old_universal = """        * {
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            margin: 0;
            padding: 0;
        }"""

new_universal = """        * {
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            margin: 0;
            padding: 0;
            -webkit-user-scalable: no;
            user-scalable: no;
            -webkit-touch-callout: none;
        }"""

content = content.replace(old_universal, new_universal)

with open('cartes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed zoom issues in cartes.html")
