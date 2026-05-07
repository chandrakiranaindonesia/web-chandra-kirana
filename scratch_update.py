import os
import re
import sys

files_to_update = ['index.html', 'layanan.html', 'legalitas.html', 'testimoni.html', 'kontak.html', 'portofolio.html', 'tentang-kami.html']

css_to_add = """
        .nav-dropdown {
            position: relative;
            display: inline-block;
        }

        .nav-dropdown .dropbtn {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: var(--navy);
            min-width: 220px;
            box-shadow: 0px 8px 24px rgba(0,0,0,0.3);
            z-index: 100;
            top: 100%;
            left: 0;
            padding: 10px 0;
            border-top: 2px solid var(--green);
            border-radius: 0 0 4px 4px;
        }

        .dropdown-content a {
            color: rgba(250, 250, 248, 0.7) !important;
            padding: 12px 20px;
            text-decoration: none;
            display: block;
            text-align: left;
            text-transform: none !important;
            letter-spacing: 0.05em !important;
            font-size: 13px !important;
            font-weight: 400 !important;
        }

        .dropdown-content a::after {
            display: none !important;
        }

        .dropdown-content a:hover {
            background-color: rgba(255, 255, 255, 0.05);
            color: var(--green) !important;
        }

        .nav-dropdown:hover .dropdown-content {
            display: block;
        }

        .mobile-nav-dropdown {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }

        .mobile-nav-dropdown-btn {
            font-family: var(--font-heading);
            font-size: 36px;
            font-weight: 600;
            color: var(--white);
            background: none;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 0;
            margin: 0;
        }

        .mobile-nav-dropdown-content {
            display: none;
            flex-direction: column;
            align-items: center;
            width: 100%;
            margin-top: 20px;
            gap: 20px;
        }

        .mobile-nav-dropdown-content.open {
            display: flex;
        }

        .mobile-nav-dropdown-content a {
            font-size: 24px !important;
            color: rgba(255, 255, 255, 0.7) !important;
        }

        .mobile-nav-dropdown-content a:hover {
            color: var(--green) !important;
        }
"""

desktop_dropdown_html = """                <div class="nav-dropdown">
                    <a href="#" class="dropbtn{active_class}">Layanan <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M6 9l6 6 6-6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                    <div class="dropdown-content">
                        <a href="layanan.html">Layanan Utama</a>
                        <a href="portofolio.html">Portofolio Proyek</a>
                    </div>
                </div>"""

mobile_dropdown_html = """        <div class="mobile-nav-dropdown">
            <button class="mobile-nav-dropdown-btn" onclick="toggleMobileDropdown()">Layanan <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M6 9l6 6 6-6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
            <div class="mobile-nav-dropdown-content" id="mobileNavDropdown">
                <a href="layanan.html" onclick="closeMobileMenu()">Layanan Utama</a>
                <a href="portofolio.html" onclick="closeMobileMenu()">Portofolio Proyek</a>
            </div>
        </div>"""

js_to_add = """
        function toggleMobileDropdown() {
            document.getElementById('mobileNavDropdown').classList.toggle('open');
        }
"""

for file_name in files_to_update:
    file_path = os.path.join(r"d:\CODEVELA\web-chandra-kirana", file_name)
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add CSS
    if '.nav-dropdown' not in content:
        content = content.replace('</style>', css_to_add + '\n    </style>')

    # Desktop replacement
    # We look for `<nav>...</nav>` block, and inside replace Layanan
    # Note: it could be `<a href="layanan.html">Layanan</a>` or `<a href="layanan.html" class="active">Layanan</a>`
    
    # We will use regex to find the desktop layanan
    # It usually looks like \s*<a href="layanan\.html"[^>]*>Layanan</a>
    
    # Let's be careful not to replace the mobile menu accidentally if it matches.
    # The desktop menu is inside <nav>...</nav>.
    
    # Find the nav block
    nav_match = re.search(r'<nav>(.*?)</nav>', content, re.DOTALL)
    if nav_match:
        nav_inner = nav_match.group(1)
        # Check if active
        is_active = 'class="active"' in nav_inner and 'layanan.html' in nav_inner.split('class="active"')[0].split('<a href="')[-1]
        
        # actually, a better regex for desktop
        desktop_regex = r'(\s*)<a href="layanan\.html"(?: class="active")?>Layanan</a>'
        match = re.search(desktop_regex, nav_inner)
        if match:
            indent = match.group(1)
            active_str = ' active' if 'class="active"' in match.group(0) else ''
            new_desktop = desktop_dropdown_html.replace('{active_class}', active_str)
            # Add indentation
            new_desktop_lines = new_desktop.split('\n')
            new_desktop = '\n'.join([indent + line.lstrip() for line in new_desktop_lines])
            
            nav_inner_replaced = nav_inner.replace(match.group(0), new_desktop)
            content = content.replace(nav_match.group(0), f'<nav>{nav_inner_replaced}</nav>')

    # Mobile replacement
    mobile_regex = r'\s*<a href="layanan\.html" onclick="closeMobileMenu\(\)"(?: style="[^"]*")?>Layanan</a>'
    mobile_match = re.search(mobile_regex, content)
    if mobile_match:
        content = content.replace(mobile_match.group(0), '\n' + mobile_dropdown_html)

    # Add JS toggle logic
    if 'function toggleMobileDropdown()' not in content:
        content = content.replace('</script>', js_to_add + '\n    </script>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {file_name}")

print("Done")
