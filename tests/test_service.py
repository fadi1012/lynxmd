
from app.event_service import EventService


def test_event_processing():
    service = EventService()

    # Test valid event
    event1 = {"event_type": "foo", "data": "lorem", "timestamp": 1632663984}
    event2 = {"event_type": "foo", "data":"ipsum", "timestamp": 1632663984}
    service.process_event(event1)
    service.process_event(event2)
    assert service.get_event_counts() == {"foo": 2}
    assert service.get_word_counts() == {"lorem": 1, "ipsum": 1}

    # Test corrupt JSON line
    corrupt_event = {"event_type": "bar", "data": "invalid json data", "timestamp": 1632663984}
    service.process_event(corrupt_event)
    assert service.get_event_counts() == {"foo": 2}
    assert service.get_word_counts() == {"lorem": 1, "ipsum": 1}

    # Test missing data key
    invalid_event = {"event_type": "baz", "invalid_data_key": "data"}
    service.process_event(invalid_event)
    assert service.get_event_counts() == {"foo": 2}
    assert service.get_word_counts() == {"lorem": 1, "ipsum": 1}

    event3 = {"event_type": "baz", "data": "lorem"}
    service.process_event(event3)
    assert service.get_event_counts() == {"foo": 2, "baz" :1}
    assert service.get_word_counts() == {"lorem": 2, "ipsum": 1}
