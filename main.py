from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Сервер запущен — парсер TikTok и Instagram готов к настройке."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
