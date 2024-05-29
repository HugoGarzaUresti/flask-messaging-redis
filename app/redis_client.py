import redis
import threading
import queue

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

CHANNEL = 'flask_channel'
message_queue = queue.Queue()

def redis_subscribe():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(CHANNEL)
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            message_queue.put(message['data'])

def start_subscriber():
    thread = threading.Thread(target=redis_subscribe)
    thread.daemon = True
    thread.start()

def get_messages():
    messages = []
    while not message_queue.empty():
        messages.append(message_queue.get())
    return messages

start_subscriber()
