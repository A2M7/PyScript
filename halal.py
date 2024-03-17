import requests
import os
import time
import sys

def download_file(url, save_path):
    attempt = 1  # Nomor percobaan awal
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("File berhasil diunduh:", save_path)
            sys.exit()  # Menghentikan program setelah berhasil mengunduh
        else:
            print("Percobaan ke-", attempt, ": Gagal mengunduh file:", url, "Status code:", response.status_code)
            print("Menunggu 15 detik sebelum mencoba lagi...")
            time.sleep(15)  # Menunggu 15 detik sebelum mencoba lagi
            attempt += 1  # Menambah nomor percobaan

# URL file yang ingin diunduh
file_url = "https://github.com/antinsp/bonetrojan/archive/refs/heads/main.zip"
# Path lengkap lokasi penyimpanan file di komputer Anda, termasuk nama file
save_location = "/root/trojan-go.zip"

# Fungsi utama yang berjalan satu kali saja
def main():
    download_file(file_url, save_location)

# Panggil fungsi utama
if __name__ == "__main__":
    main()
