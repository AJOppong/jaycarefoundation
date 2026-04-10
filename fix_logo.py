import os
import re

directory = r"c:\Users\user\Desktop\ngo"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the style attribute robustly to scale the logo up significantly.
        # Setting a base height of 90px and scaling by 2.2x to make the text massive.
        new_style = 'style="height: 90px; transform: scale(2.2); transform-origin: left center; mix-blend-mode: multiply;"'
        
        content = re.sub(
            r'style="height:\s*130px;\s*margin:\s*-30px\s+0\s+-30px\s+-15px;\s*mix-blend-mode:\s*multiply;"',
            new_style,
            content
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

css_path = os.path.join(directory, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Expand navbar min-height to accommodate the larger logo
css_content = re.sub(r'min-height:\s*90px;', 'min-height: 110px;', css_content)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Logo scaled aggressively via CSS transform.")
