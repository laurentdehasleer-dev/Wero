from PIL import Image, ImageDraw
import os

os.makedirs('images', exist_ok=True)

images_to_create = [
    ('wero.jpg', 300, 100, 'Wero Logo', '#FFF69C'),
    ('icon.png', 64, 64, 'Icon', '#000000'),
    ('image1.png', 800, 400, 'Main Image', '#4C84FF'),
    ('paylib.png', 300, 300, 'Paylib', '#FF59FF'),
    ('liberte.png', 300, 300, 'Liberté', '#6BFFEA'),
    ('securite.png', 300, 300, 'Sécurité', '#4C84FF'),
    ('telephone.png', 300, 400, 'Phone', '#FFF69C'),
    ('avion.svg', 120, 120, 'Plane', '#000000'),
    ('bcp.png', 150, 80, 'BCP', '#F9FAFB'),
    ('palatine.png', 150, 80, 'Palatine', '#F9FAFB'),
    ('banque-populaire.png', 150, 80, 'BP', '#F9FAFB'),
    ('banque-savoie.jpg', 150, 80, 'Savoie', '#F9FAFB'),
    ('bnp.jfif', 150, 80, 'BNP', '#F9FAFB'),
    ('bred.jpeg', 150, 80, 'BRED', '#F9FAFB'),
    ('caisse-epargne.png', 150, 80, 'CEL', '#F9FAFB'),
    ('cic.png', 150, 80, 'CIC', '#F9FAFB'),
    ('credit-agricole.svg', 150, 80, 'CA', '#F9FAFB'),
    ('cooperatif.jpeg', 150, 80, 'Coop', '#F9FAFB'),
    ('maritime.png', 150, 80, 'Maritime', '#F9FAFB'),
    ('fortuneo.svg.png', 150, 80, 'Fortuneo', '#F9FAFB'),
    ('credit-mutuel.png', 150, 80, 'CM', '#F9FAFB'),
    ('cmb.png', 150, 80, 'CMB', '#F9FAFB'),
    ('cmso.png', 150, 80, 'CMSO', '#F9FAFB'),
    ('hello-bank.png', 150, 80, 'Hello', '#F9FAFB'),
    ('banque-postale.png', 150, 80, 'Postale', '#F9FAFB'),
    ('lcl.png', 150, 80, 'LCL', '#F9FAFB'),
    ('bm.jpg', 150, 80, 'BM', '#F9FAFB'),
    ('monabanq.png', 150, 80, 'Monabanq', '#F9FAFB'),
    ('societe-generale.png', 150, 80, 'SG', '#F9FAFB'),
    ('revolut.jpg', 150, 80, 'Revolut', '#F9FAFB'),
    ('sme.svg', 150, 80, 'SME', '#F9FAFB'),
]

for filename, width, height, text, bg_color in images_to_create:
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    text_bbox = draw.textbbox((0, 0), text)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, fill='#000000')
    
    path = os.path.join('images', filename)
    # Convertir .svg en .png pour PIL
    if filename.endswith('.svg'):
        path = path.replace('.svg', '.png')
    img.save(path)
    print(f"[OK] {filename}")

print("\nImages creees avec succes!")
