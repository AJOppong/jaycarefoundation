import re

fname = 'contact.html'
content = open(fname, 'rb').read().decode('utf-8')

old_str = '''         <!-- Map Embed Placeholder -->
         <div style="width: 100%; height: 250px; background-color: var(--accent); border-radius: var(--radius-lg); display: flex; align-items: center; justify-content: center; color: var(--text-secondary); margin-top: 2rem; box-shadow: var(--shadow-sm);">
           Google Maps Placeholder
         </div>'''

new_str = '''         <!-- Google Maps Embed -->
         <div style="width: 100%; height: 250px; border-radius: var(--radius-lg); overflow: hidden; margin-top: 2rem; box-shadow: var(--shadow-sm);">
           <iframe src="https://www.google.com/maps?q=Goaso,+Ahafo+Region,+Ghana&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
         </div>'''

if old_str in content:
    content = content.replace(old_str, new_str)
    print('Replaced exact match.')
else:
    content = re.sub(r'<!-- Map Embed Placeholder -->.*?</div>', new_str, content, flags=re.DOTALL)
    print('Replaced via regex.')

open(fname, 'wb').write(content.encode('utf-8'))
