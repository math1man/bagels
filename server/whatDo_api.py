# import random
from event import Event
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'whatDo'

class Event(messages.Message):
  """Greeting that stores a message."""
  message = messages.StringField(1)


class EventCollection(messages.Message):
  """Collection of Greetings."""
  items = messages.MessageField(Event, 1, repeated=True)


STORED_EVENTS = EventCollection(items=[
    Event(message='This is event 1!'),
    Event(message='This is event 2!'),
])


@endpoints.api(name='whatDo', version='v1')
class WhatDoApi(remote.Service):
  """WhatDo API v1."""

  @endpoints.method(message_types.VoidMessage, EventCollection,
                    path='whatDo', http_method='GET',
                    name='whatDo.listEvents')
  def events_list(self, unused_request):
    return STORED_EVENTS

  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))

  @endpoints.method(ID_RESOURCE, Event,
                    path='events/{id}', http_method='GET',
                    name='events.getEvent')
  def greeting_get(self, request):
    try:
      return STORED_EVENTS.items[request.id]
    except (IndexError, TypeError):
      raise endpoints.NotFoundException('Event %s not found.' %
                                        (request.id,))

APPLICATION = endpoints.api_server([WhatDoApi])