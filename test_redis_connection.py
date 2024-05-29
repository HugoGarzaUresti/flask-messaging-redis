import redis

try:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.ping()
    print("Connected to Redis!")
except redis.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")
