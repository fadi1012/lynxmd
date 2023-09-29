# lynx.md home assignment - Fadi Zaboura

## Non-Blocking Producer/Consumer Stream Processing Service

This service consumes an infinite stream of lines of event data encoded in JSON, gathers statistics about the events,
and exposes the statistics through an HTTP API.

## Getting Started

Follow these instructions to set up and run the service.

### Prerequisites

- Python 3.6 or higher
- Docker (optional)


## Note that for easier run, I've pushed the image to a public registry 
```bash
docker pull fadizaboura/lynxmd:event-service
docker run -p 9090:9090 event-service
```

## I've added an extra step for you to view things
http://localhost:9090/static/index.html
will open a simple html page that shows the event status and word stats value with a simple refresh mechanism


### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Service

Start the service:

```bash
python app/static.py
```

The service will run on port 9090 by default.

You can now use an HTTP client like curl or a web browser to access the following endpoints:

- http://localhost:9090/events/CountByEventType: Returns event counts by event type.
- http://localhost:9090/events/CountWords: Returns word appearance counts in event data.

## Dockerization (Optional)

To build and run the service in a Docker container:

```bash
docker build -t event-service .
docker run -p 9090:9090 event-service
```

## Running Tests

To run tests, you'll need to install pytest:

```bash
pip install pytest
```

Then run the tests:

```bash
pytest tests/
```

**Notes**:

1. This service does not use a third-party queue ( like Redis) to avoid over-engineering.

2. supervisor.py: The purpose of supervisor.py is to manage the concurrent execution of multiple components of our
   application, such as the producer, FastAPI app, and consumer. It coordinates their startup and termination. The
   primary role of supervisor.py is to ensure that all necessary components are running simultaneously to create a
   functioning application.

3. why are we using Threads and not Subprocesses:

* The use of threads in this scenario allows for efficient sharing of the event queue without the need for complex
  inter-process communication (IPC).

* Shared Queue: Using a shared queue (in-memory queue) with threads allows for a simple and efficient way to pass data
  between the producer and the consumer. Threads within the same process can safely enqueue and dequeue data from the
  shared queue without the complexities associated with IPC. This approach simplifies the design and coordination of the
  application.

* In summary, supervisor.py coordinates the execution of threads for the producer, FastAPI app, and consumer. Threads
  are chosen over subprocesses because they provide a straightforward way to share data like the event queue within the
  same process, making the application design more manageable and efficient.

4. In order to achieve a NON-blocking mechanism, I started the consumer in separate coroutine, coroutines are Non
   blocking, meaning that they will allow the service to continue processing other tasks while waiting for an event to
   be consumed, this helps the service from getting blocked by slow consuming of events.

5. I did not use any DB to store the event types and event words, it's stored in a simple dictionary.