
class EventService:
    def __init__(self):
        self.event_counts = {}
        self.word_counts = {}

    def process_event(self, event) -> None:
        try:
            if "event_type" not in event or "data" not in event:
                raise ValueError("Event is missing 'event_type' or 'data' key(s)")

            event_data = event["data"]
            event_type = event["event_type"]

            if event_data and not event_data.isalpha():
                return

            # Update event counts by event type
            self.event_counts[event_type] = self.event_counts.get(event_type, 0) + 1

            # Update word appearance counts in event data
            if "data" in event and event_data:
                self.word_counts[event_data] = self.word_counts.get(event_data, 0) + 1
        except (ValueError, KeyError) as e:
            # Handle corrupt JSON lines, missing keys, or other exceptions
            self.handle_processing_error(e)

    def get_event_counts(self) -> dict:
        return self.event_counts

    def get_word_counts(self) -> dict:
        return self.word_counts

    def handle_processing_error(self, error):
        # You can customize error handling here, such as logging errors
        # For now, simply print the error
        print(f"Error processing event: {error}")
