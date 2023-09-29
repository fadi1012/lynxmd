import threading
from queue import Queue

from app.consumer import main_consumer
from producer import main_producer

# Import your producer, FastAPI app, and consumer modules here

# Create a shared event queue
event_queue = Queue()


# Define functions to run the producer, FastAPI app, and consumer concurrently

def run_producer():
    main_producer(event_queue)


def run_fastapi():
    from app.event_routes import app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9090)


def run_consumer():
    main_consumer(event_queue)


# Create threads for each component
producer_thread = threading.Thread(target=run_producer)
fastapi_thread = threading.Thread(target=run_fastapi)
consumer_thread = threading.Thread(target=run_consumer)

# Start the threads
producer_thread.start()
fastapi_thread.start()
consumer_thread.start()

# Wait for the threads to complete
producer_thread.join()
fastapi_thread.join()
consumer_thread.join()
