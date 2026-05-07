import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change 1: Increase font size for "KONTRAKTOR"
    # The CSS is:
    #         .logo-text span {
    #             display: block;
    #             font-weight: 300;
    #             font-size: 10px;
    #             letter-spacing: 0.18em;
    # ...
    content = content.replace(
        '.logo-text span {\n            display: block;\n            font-weight: 300;\n            font-size: 10px;',
        '.logo-text span {\n            display: block;\n            font-weight: 300;\n            font-size: 12px;'
    )

    if filepath == 'index.html':
        # Change 2: Increase font size for "- CV CHANDRA KIRANA INDONESIA" in hero
        # The CSS is:
        #         .hero-eyebrow span {
        #             font-size: 11px;
        content = content.replace(
            '.hero-eyebrow span {\n            font-size: 11px;',
            '.hero-eyebrow span {\n            font-size: 16px;'
        )
        
        # Change 3: Brighter green for .btn-primary
        #         .btn-primary {
        #             ...
        #             background: var(--green);
        # Change to var(--green-light)
        btn_primary_old = "        .btn-primary {\n            display: inline-flex;\n            align-items: center;\n            gap: 10px;\n            background: var(--green);"
        btn_primary_new = "        .btn-primary {\n            display: inline-flex;\n            align-items: center;\n            gap: 10px;\n            background: var(--green-light);"
        content = content.replace(btn_primary_old, btn_primary_new)
        
        # Change 4: 10+ Tahun pengalaman -> 1+ Tahun Beroperasi, 150+ proyek -> 15+
        stats_old = """        <div class="hero-stats">
            <div class="stat-item">
                <div class="stat-number">10<sup>+</sup></div>
                <div class="stat-label">Tahun Pengalaman</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">150<sup>+</sup></div>
                <div class="stat-label">Proyek Selesai</div>
            </div>"""
        
        stats_new = """        <div class="hero-stats">
            <div class="stat-item">
                <div class="stat-number">1<sup>+</sup></div>
                <div class="stat-label">Tahun Beroperasi</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">15<sup>+</sup></div>
                <div class="stat-label">Proyek Selesai</div>
            </div>"""
        
        content = content.replace(stats_old, stats_new)

        # Also update the text to add "INDONESIA" just in case the user wanted it added to the text.
        # "<span>CV Chandra Kirana</span>" -> "<span>- CV CHANDRA KIRANA INDONESIA</span>"
        content = content.replace("<span>CV Chandra Kirana</span>", "<span>- CV CHANDRA KIRANA INDONESIA</span>")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates applied to all HTML files.")
