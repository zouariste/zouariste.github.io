import os
import requests
from bs4 import BeautifulSoup
import shutil

FOLLOWINGS_FILE = "followings.html"
FOLLOWERS_FILE = "followers.html"
OUTPUT_FILE = "unfollowers.html"
IMG_DIR = "images"

# Reset image folder
if os.path.exists(IMG_DIR):
    shutil.rmtree(IMG_DIR)
os.makedirs(IMG_DIR, exist_ok=True)

def extract_profiles(file_path):
    """Extract (name, img_url, profile_link) from an Instagram export file"""
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        profiles = {}

        for tag in soup.find_all('div', {'class': 'html-div'}):
            img = tag.find("img")
            link = tag.find("a")

            if not img or not link:
                continue

            alt = img.get("alt", "")
            username = alt.split("'s")[0] if alt else "Unknown"
            img_url = img.get("src")
            profile_link = "https://www.instagram.com" + link.get("href")

            profiles[username.lower()] = (username, img_url, profile_link)

        return profiles

# Extract both sets
followings = extract_profiles(FOLLOWINGS_FILE)
followers = extract_profiles(FOLLOWERS_FILE)

# Find unfollowers = followings - followers
unfollowers = {
    user: followings[user]
    for user in followings
    if user not in followers
}
# Download images
local_profiles = []
for username, (name, img_url, profile_link) in unfollowers.items():
    filename = os.path.join(IMG_DIR, name.replace(" ", "_") + ".jpg")
    try:
        r = requests.get(img_url, timeout=10)
        if r.status_code == 200:
            with open(filename, "wb") as f_img:
                f_img.write(r.content)
    except Exception as e:
        print(f"⚠️ Could not download {img_url}: {e}")
        filename = ""

    local_profiles.append((username, filename, profile_link))

# Generate HTML
html_output = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Unfollowers</title>
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
<h2 style="text-align:center;">People You Follow But Who Don’t Follow You Back</h2>
<div class="container">
"""

for name, img_path, profile_link in local_profiles:
    html_output += f"""
    <a href="{profile_link}" target="_blank" style="text-decoration:none; color:inherit;">
        <div class="card">
            <img src="{img_path}" alt="{name}">
            <div>{name}</div>
        </div>
    </a>
    """


html_output += """
</div>
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"✅ Found {len(local_profiles)} unfollowers → {OUTPUT_FILE}")
