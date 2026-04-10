import os
import re

directory = r"c:\Users\user\Desktop\ngo"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We find the logo img tag and place the foundation name directly next to it inside the navbar link
        # Use regex to match the img tag across multiple lines if needed
        content = re.sub(
            r'(<img[^>]+(?:logo\.jpeg|Jacinta\'s Foundation Logo)[^>]*>)\s*</a>',
            r'\1<span style="margin-left: 15px; font-size: 1.6rem; font-weight: 800; color: var(--primary); letter-spacing: -0.5px;">Jacinta\'s <span style="color:var(--secondary)">Foundation</span></span></a>',
            content
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Foundation name added next to logo")
