import json
import queue
import time
import random

from app.event_service import EventService

event_service = EventService()


class Event(object):
    def __init__(self, ev_type, data):
        self.type = ev_type
        self.data = data
        self.ts = time.time()

    def to_json(self):
        if random.random() < 0.1:
            return json.dumps(
                {"event_type": self.type, "data": "".join([chr(random.randint(0, 255)) for _ in range(0, 10)]),
                 "timestamp": int(self.ts)})
        else:
            return json.dumps({"event_type": self.type, "data": self.data, "timestamp": int(self.ts)})


def main_producer(event_queue: queue.Queue) -> None:
    with open("./config.json", "r+") as fp:
        config = json.load(fp)

    # Enqueue events to the shared event queue
    while True:
        for i in range(random.randint(1, 5)):
            event = Event(random.choice(config.get("event_types")),
                          random.choice(config.get("data")))
            json_event = event.to_json()
            event_queue.put(json_event)  # Enqueue events to the shared event queue
        time.sleep(random.random() * 3)
