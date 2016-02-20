import random
from event import Event
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'event'
'''
class EventSelector:

    def __init__(self):

        self.events = set()


    def select_event(self, user):

        valid_events = self.events - user.rejected_events
        choice = random.sample(valid_events, 1)
        user.rejected_events.add(choice)
        return choice

    def collect_events(self):

        self.events = {Event("Walker"), Event("Mall of America")}

'''


# package = 'Hello' --- first thing in file


class Event(messages.Message):
  """Greeting that stores a message."""
  name = messages.StringField(1)
  url = messages.StringField(2)
  cost = messages.StringField(3)
  groupSize = messages.StringField(4)
  duration = messages.StringField(5)
  distance = messages.StringField(6)
  description = messages.StringField(7)


class EventCollection(messages.Message):
  """Collection of Greetings."""
  items = messages.MessageField(Event, 1, repeated=True)


STORED_EVENTS = EventCollection(items=[
    Event(name = "hella fun",
          url = "https://www.google.com",
          cost = "100",
          groupSize = "4",
          duration = "3",
          distance = "5",
          description = "this is dope yo"),
    Event(name = "asdf fun",
          url = "https://www.yahoo.com",
          cost = "22",
          groupSize = "1",
          duration = "10",
          distance = "3",
          description = "this is da best"),
    Event(name = "were good",
          url = "https://www.reddit.com",
          cost = "99",
          groupSize = "1",
          duration = "7",
          distance = "30",
          description = "420 blaze it"),
])


@endpoints.api(name='events', version='v1')
class EventsApi(remote.Service):
  """Events API v1."""

  @endpoints.method(message_types.VoidMessage, EventCollection,
                    path='events', http_method='GET',
                    name='eventsApi.listEvents')
  def events_list(self, unused_request):
    return STORED_EVENTS

  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))

  @endpoints.method(ID_RESOURCE, Event,
                    path='events/{id}', http_method='GET',
                    name='eventsApi.getEvent')
  def greeting_get(self, request):
    try:
      return random.choice(STORED_EVENTS.items)
    except (IndexError, TypeError):
      raise endpoints.NotFoundException('Event %s not found.' %
                                        (request.id,))

APPLICATION = endpoints.api_server([EventsApi])