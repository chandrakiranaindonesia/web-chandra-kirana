import os
import re

files_to_update = ['layanan.html', 'legalitas.html', 'testimoni.html', 'kontak.html', 'portofolio.html']
target_font_url = 'https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Inter:wght@300;400;500;600&display=swap'

root_replacement = """        :root {
            --navy: #0c3555;
            --navy-mid: #144b75;
            --navy-light: #1b6092;
            --green: #16A34A;
            --green-dark: #15803D;
            --green-light: #22C55E;
            --gold: #16A34A;
            --gold-light: #22C55E;
            --white: #FFFFFF;
            --off-white: #F8F9FA;
            --cream: #F8F9FA;
            --cream-dark: #F1F5F9;
            --gray-text: #4B5563;
            --gray-light: #CBD5E1;
            --font-heading: 'Montserrat', sans-serif;
            --font-body: 'Inter', sans-serif;
            --transition: 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }"""

for file in files_to_update:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Font URL
    content = re.sub(
        r'https://fonts\.googleapis\.com/css2\?family=Cormorant\+Garamond[^"\'<]+',
        target_font_url,
        content
    )

    # Replace Root variables
    content = re.sub(
        r':root\s*\{[^}]+\}',
        root_replacement,
        content
    )

    # Replace fonts in CSS
    content = content.replace("'DM Sans', sans-serif", 'var(--font-body)')
    content = content.replace("'Cormorant Garamond', serif", 'var(--font-heading)')
    
    # Body background in CSS
    content = content.replace('background: var(--cream); color: var(--navy);', 'background: var(--white); color: var(--navy);')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated files.')
