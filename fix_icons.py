import os

FA_LINK = '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">'

files = ['index.html', 'about.html', 'programs.html', 'contact.html', 'volunteer.html', 'donation.html', 'gallery.html']

sec = 'color:var(--secondary);'

emoji_map = {
    # Core values
    '\U0001f499': f'<i class="fas fa-heart" style="{sec}"></i>',
    '\U0001f91d': f'<i class="fas fa-handshake" style="{sec}"></i>',
    '\U0001f30d': f'<i class="fas fa-globe-africa" style="{sec}"></i>',
    '\U0001f4c8': f'<i class="fas fa-chart-line" style="{sec}"></i>',
    '\U0001f517': f'<i class="fas fa-link" style="{sec}"></i>',
    # Leadership portraits
    '\U0001f469': f'<i class="fas fa-user-circle" style="{sec} font-size:4rem;"></i>',
    '\U0001f468': f'<i class="fas fa-user-circle" style="{sec} font-size:4rem;"></i>',
    # Programs
    '\U0001f3e5': f'<i class="fas fa-stethoscope" style="{sec}"></i>',
    '\U0001f475': f'<i class="fas fa-hands-helping" style="{sec}"></i>',
    '\U0001f372': f'<i class="fas fa-utensils" style="{sec}"></i>',
    '\U0001f467': f'<i class="fas fa-child" style="{sec}"></i>',
    '\U0001f6a8': f'<i class="fas fa-first-aid" style="{sec}"></i>',
    '\U0001f4bc': f'<i class="fas fa-briefcase" style="{sec}"></i>',
    # Contact
    '\U0001f4cd': '<i class="fas fa-map-marker-alt"></i>',
    '\u2709\ufe0f': '<i class="fas fa-envelope"></i>',
    '\u2709':     '<i class="fas fa-envelope"></i>',
    '\U0001f4de': '<i class="fas fa-phone-alt"></i>',
}

for fname in files:
    if not os.path.exists(fname):
        continue
    content = open(fname, 'rb').read().decode('utf-8')

    # Inject FA CDN after styles.css if not already there
    if 'font-awesome' not in content:
        content = content.replace(
            '  <link rel="stylesheet" href="css/styles.css">',
            '  <link rel="stylesheet" href="css/styles.css">\n' + FA_LINK
        )

    for emoji, icon in emoji_map.items():
        content = content.replace(emoji, icon)

    open(fname, 'wb').write(content.encode('utf-8'))
    print(f'Updated: {fname}')

print('All done!')
