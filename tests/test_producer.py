import queue
import unittest
from unittest.mock import patch
from producer import Event


class TestProducer(unittest.TestCase):

    @patch('producer.random.random', return_value=0.5)  # Mock random.random() for deterministic testing
    def test_enqueue_event(self, mock_random):
        event = Event("foo", "lorem")
        event_json = event.to_json()

        # Enqueue event
        event_queue = queue.Queue()
        event_queue.put(event_json)

        # Check if the event was enqueued correctly
        self.assertEqual(event_queue.qsize(), 1)
        self.assertEqual(event_queue.get(), event_json)

    # Add more producer tests as needed


if __name__ == '__main__':
    unittest.main()
