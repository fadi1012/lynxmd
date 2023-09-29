import json
import asyncio
import queue

from producer import event_service


# Define a coroutine to consume and process events from the shared queue
async def consume_events(event_queue):
    while True:
        try:
            # Dequeue an event from the shared queue
            event_json = event_queue.get(timeout=1)
            event = json.loads(event_json)
            # Process the event using the EventService
            event_service.process_event(event)
        except queue.Empty:  # Corrected exception handling
            # No events in the queue, continue or perform other tasks
            await asyncio.sleep(0.1)
        except json.JSONDecodeError:
            print("Error decoding JSON: ", event_json)
        except Exception as e:
            print("Error processing event: ", str(e))


def main_consumer(event_queue: queue.Queue) -> None:
    # Start the event consumer as a separate coroutine
    asyncio.run(consume_events(event_queue))
