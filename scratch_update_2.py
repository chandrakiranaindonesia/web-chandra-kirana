import os
import re

files_to_update = ['index.html', 'layanan.html', 'legalitas.html', 'testimoni.html', 'kontak.html', 'portofolio.html', 'tentang-kami.html']

scrolled_css = """
        /* Scrolled Navbar Theme */
        header.scrolled {
            background: var(--white) !important;
            backdrop-filter: none !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
        }
        header.scrolled nav a { color: var(--navy) !important; }
        header.scrolled nav a:hover { color: var(--green-light) !important; }
        header.scrolled nav a.active { color: var(--green-light) !important; }
        header.scrolled .logo-text { color: var(--navy) !important; }
        header.scrolled .logo-text span { color: var(--green-light) !important; }
        header.scrolled .nav-cta { border-color: var(--green-light) !important; color: var(--green-light) !important; }
        header.scrolled .nav-cta:hover { background: var(--green-light) !important; color: var(--white) !important; }
        header.scrolled .hamburger span { background: var(--navy) !important; }
        header.scrolled .nav-dropdown .dropbtn { color: var(--navy) !important; }
        header.scrolled .nav-dropdown:hover .dropbtn { color: var(--green-light) !important; }
        header.scrolled .dropdown-content { background-color: var(--white) !important; border-top: 2px solid var(--green-light) !important; box-shadow: 0px 8px 24px rgba(0,0,0,0.1) !important; }
        header.scrolled .dropdown-content a { color: var(--navy) !important; }
        header.scrolled .dropdown-content a:hover { background-color: var(--cream) !important; color: var(--green-light) !important; }
        header.scrolled .mobile-nav-dropdown-btn { color: var(--navy) !important; }
        header.scrolled .mobile-close { color: var(--navy) !important; }
"""

lighter_green_css = """
        /* Lighter green for normal navbar */
        nav a::after { background: var(--green-light) !important; }
        nav a.active { color: var(--green-light) !important; }
        .nav-cta { border-color: rgba(34, 197, 94, 0.5) !important; color: var(--green-light) !important; }
        .nav-cta:hover { background: var(--green-light) !important; color: var(--navy) !important; border-color: var(--green-light) !important; }
        .logo-text span { color: var(--green-light) !important; }
        .dropdown-content { border-top: 2px solid var(--green-light) !important; }
        .dropdown-content a:hover { color: var(--green-light) !important; }
        .mobile-nav-dropdown-content a:hover { color: var(--green-light) !important; }
        .nav-dropdown .dropbtn.active { color: var(--green-light) !important; }
"""

for file_name in files_to_update:
    file_path = os.path.join(r"d:\CODEVELA\web-chandra-kirana", file_name)
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update dropdown animation
    content = re.sub(
        r'display:\s*none;\s*position:\s*absolute;\s*background-color:\s*var\(--navy\);',
        'display: block; visibility: hidden; opacity: 0; transform: translateY(10px); transition: all 0.3s ease; position: absolute; background-color: var(--navy);',
        content
    )
    
    content = re.sub(
        r'\.nav-dropdown:hover \.dropdown-content\s*\{\s*display:\s*block;\s*\}',
        '.nav-dropdown:hover .dropdown-content { visibility: visible; opacity: 1; transform: translateY(0); }',
        content
    )

    # 2. Add header.scrolled styles
    if '/* Scrolled Navbar Theme */' not in content:
        content = content.replace('</style>', scrolled_css + '\n    </style>')

    # 3. Add lighter green styles
    if '/* Lighter green for normal navbar */' not in content:
        content = content.replace('</style>', lighter_green_css + '\n    </style>')

    # 4. Remove standalone Portofolio from Desktop nav
    desktop_portofolio_regex = r'\s*<a href="portofolio\.html"(?: class="active")?>Portofolio</a>'
    content = re.sub(desktop_portofolio_regex, '', content)

    # 5. Remove standalone Portofolio from Mobile menu
    mobile_portofolio_regex = r'\s*<a href="portofolio\.html" onclick="closeMobileMenu\(\)"(?: class="active")?>Portofolio</a>'
    content = re.sub(mobile_portofolio_regex, '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {file_name}")

print("Done")
