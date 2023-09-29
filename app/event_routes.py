from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from producer import event_service

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/events/CountByEventType',
         response_model=dict,
         response_description="Count of events by event type (CountByEventType)",
         responses={404: {'model': str, 'description': 'Event not found'}})
async def get_event_stats():  # Pass event_service as a parameter
    """
    Returns the count of events by event type.

      Response Example:
    ```json
    { "foo": 3, "bar": 1 }
    ```
    """
    return event_service.get_event_counts()


@app.get('/events/CountWords',
         response_model=dict,
         response_description="Count of events by event type (countWords)",
         responses={404: {'model': str, 'description': 'Word not found'}},
         )
async def get_word_stats():
    """
     Returns the count of events by event type.

       Response Example:
     ```json
     { "lorem": 2, "ipsum": 1 }
     ```
     """
    return event_service.get_word_counts()
