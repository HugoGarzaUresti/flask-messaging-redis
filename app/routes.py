from flask import request, jsonify, current_app as app
from .redis_client import redis_client, get_messages

@app.route('/publish', methods=['POST'])
def publish_message_route():
    message = request.json.get('message')
    if not message:
        return jsonify({"error": "No message provided"}), 400
    redis_client.publish('flask_channel', message)
    return jsonify({"status": "Message published"}), 200

@app.route('/subscribe', methods=['GET'])
def subscribe_messages():
    messages = get_messages()
    return jsonify({"messages": messages}), 200
