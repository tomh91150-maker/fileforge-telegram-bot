import os
from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "FileForge Telegram Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(silent=True)

    if not update:
        return jsonify({"ok": True})

    # Telegram update received
    print("Telegram update received:", update)

    return jsonify({"ok": True})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
