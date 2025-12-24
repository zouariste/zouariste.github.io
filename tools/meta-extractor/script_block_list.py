from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import base64

# Load your HTML
with open("sample-blocks.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
users = soup.find_all("div", class_="x1obq294")  # adjust if needed

html_content = "<html><body><h1>User List</h1><div style='display:flex; flex-wrap: wrap;'>"

for user in users:
    # Extract name
    name_tag = user.find("span", string=True)
    if not name_tag:
        continue
    name = name_tag.get_text(strip=True)

    # Extract photo URL
    img_tag = user.find("image")
    if not img_tag or not img_tag.has_attr("xlink:href"):
        continue
    photo_url = img_tag["xlink:href"]

    # Download and resize image
    response = requests.get(photo_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((150, 150))  # bigger and clear

    # Convert to base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Add to HTML
    html_content += f"""
    <div style='margin:10px; text-align:center;'>
        <img src='data:image/png;base64,{img_str}' width='150' height='150'><br>
        <span>{name}</span>
    </div>
    """

html_content += "</div></body></html>"

# Save HTML
with open("user_list.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: user_list.html")
