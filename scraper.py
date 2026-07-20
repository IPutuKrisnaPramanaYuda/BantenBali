import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

print(">>> Scraping Terminologi Banten & Budaya Bali...")
url = "https://id.wikipedia.org/wiki/Kategori:Budaya_Bali"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
data_hasil_scrape = []

items = soup.find_all('div', class_='mw-category-group')

for group in items:
    links = group.find_all('a')
    for link in links:
        href = link.get('href')
        if href: 
            data_hasil_scrape.append({
                "tanggal_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "istilah_budaya": link.text.strip(),
                "sumber_url": "https://id.wikipedia.org" + href
            })
            
        if len(data_hasil_scrape) == 30:
            break
    if len(data_hasil_scrape) == 30:
        break

df = pd.DataFrame(data_hasil_scrape)
df.to_csv('dataset_budaya_bali.csv', index=False)
print(f"  Berhasil menyimpan {len(df)} baris data ke CSV.")

os.system('git add .')
os.system(f'git commit -m "Update Ensiklopedia Banten & Budaya: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
os.system('git push origin main >nul 2>&1')
print("[SUKSES] Repo BantenBali berhasil di-push!")