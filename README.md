# Flask Messaging with Redis

This guide walks you through the process of creating a simple messaging application using Flask and Redis.

## What You Will Build

You will build an application that uses Flask to publish and subscribe to messages via Redis. This application will demonstrate the use of Redis for message brokering in a Flask web application.

## What You Need

- Python 3.x
- Redis Server
- pip (Python package installer)

### Set Up the Redis Server

Make sure you have a Redis server running on your localhost at the default port. You can download and run Redis from [Redis.io](https://redis.io/download).

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/flask-messaging-redis
    cd flask-messaging-redis
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Ensure Redis server is running.**

2. **Start the Flask application:**

    ```sh
    python run.py
    ```

3. **Publish a message:**

    ```sh
    curl -X POST http://localhost:8080/publish -H "Content-Type: application/json" -d '{"message":"Hello, Redis!"}'
    ```

4. **Subscribe to messages:**

    ```sh
    curl http://localhost:8080/subscribe
    ```

### Built With

- **Flask** - The web framework used.
- **redis-py** - Redis client for Python.

### Acknowledgments

- Inspired by the [Spring Boot guide for messaging with Redis](https://spring.io/guides/gs/messaging-redis)