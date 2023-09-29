import unittest
from unittest.mock import patch, Mock
import queue

import app


class TestMainConsumer(unittest.TestCase):

    @patch('consumer.asyncio.run')
    def test_main_consumer(self, mock_asyncio_run):
        # Create a mock event_queue
        event_queue = Mock(spec=queue.Queue)

        # Create a mock EventService
        event_service = Mock()

        # Mock the behavior of the event_queue's get method
        event_queue.get.side_effect = [
            '{"event_type": "foo", "data": "data1"}',
            '{"event_type": "bar", "data": "data2"}',
            queue.Empty()  # To simulate the end of processing
        ]

        # Call the main_consumer function with the mock event_queue and event_service
        app.main_consumer(event_queue)

        # Assertions
        mock_asyncio_run.assert_called_once()  # Ensure asyncio.run was called once

        # Ensure the event_service's process_event was called with the expected events
        event_service.process_event.assert_has_calls([
            Mock({"event_type": "foo", "data": "data1"}),
            Mock({"event_type": "bar", "data": "data2"})
        ], any_order=True)


if __name__ == '__main__':
    unittest.main()
