import os
import glob
images = glob.glob('C:/Users/user/Desktop/ngo/images/WhatsApp Image*')
html = ''
for img in images:
    filename = os.path.basename(img)
    html += f'        <div class="gallery-item" data-src="images/{filename}">\n          <img class="gallery-item-img" src="images/{filename}" alt="Gallery Image">\n        </div>\n'
    
with open('C:/Users/user/Desktop/ngo/gallery_images.txt', 'w', encoding='utf-8') as f:
    f.write(html)
