import os
import requests
from bs4 import BeautifulSoup

INPUT_FILE = "sample-followers.html"
OUTPUT_FILE = "output-ahmedsana.html"
IMG_DIR = "images"

os.makedirs(IMG_DIR, exist_ok=True)

def extract_name(alt_text):
    username = alt_text.split("'s")[0]
    parts = username.replace(".", " ").split()
    return " ".join(p.capitalize() for p in parts)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

profiles = []
for span in soup.find_all("span", {"class": "xjp7ctv"}):
    img = span.find("img")
    link = span.find("a")
    if not img or not link:
        continue

    alt = img.get("alt", "")
    name = extract_name(alt) if alt else "Unknown"
    img_url = img.get("src")
    profile_link = "https://www.instagram.com" + link.get("href")

    # Download image
    filename = os.path.join(IMG_DIR, name.replace(" ", "_") + ".jpg")
    try:
        r = requests.get(img_url, timeout=10)
        if r.status_code == 200:
            with open(filename, "wb") as f_img:
                f_img.write(r.content)
    except Exception as e:
        print(f"⚠️ Could not download {img_url}: {e}")
        continue

    profiles.append((name, filename, profile_link))

# Generate HTML with local images
html_output = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Instagram Profiles</title>
<style>
body { font-family: Arial, sans-serif; background: #fafafa; }
.container { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; padding: 20px; }
.card { background: white; border-radius: 12px; padding: 15px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
.card img { width: 150px; height: 150px; border-radius: 50%; object-fit: cover; }
.card a { text-decoration: none; color: #3897f0; font-weight: bold; display: block; margin-top: 10px; }
.card .name { margin-top: 8px; font-size: 18px; font-weight: 600; color: #333; }
</style>
</head>
<body>
<div class="container">
"""

for name, img_path, profile_link in profiles:
    html_output += f"""
    <div class="card">
        <img src="{img_path}" alt="{name}">
        <a href="{profile_link}" target="_blank">{name}</a>
    </div>
    """

html_output += """
</div>
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"✅ Extracted {len(profiles)} profiles into {OUTPUT_FILE}")
os.rmdir(IMG_DIR)
