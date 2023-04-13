import requests
from bs4 import BeautifulSoup

# URL halaman CapCut dengan ID templat
url = " "

# Mengirim permintaan GET ke server CapCut dan mengunduh halaman web
response = requests.get(url)

# Membuat objek BeautifulSoup untuk mem-parsing halaman HTML
soup = BeautifulSoup(response.content, "html.parser")

# Mencari elemen video dengan tag "video" dan mengambil atribut "src"
video_url = soup.find("video")["src"]

# Nama file output
file_name = "output.mp4"

# Mengirim permintaan GET ke server CapCut dan mengunduh file video
response = requests.get(video_url)

# Menyimpan file video ke sistem lokal
with open(file_name, "wb") as f:
    f.write(response.content)
