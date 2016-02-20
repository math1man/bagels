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
    Event(name = "Minnesota Wild v. Chicago Blackhawks",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "115",
          groupSize = "2-4",
          duration = "2.5-3  hours",
          distance = "5 miles",
          description = "Minnesota hosts Chicago in Minnesota's first-ever outdoor hockey game.  The two central-division rivals square off at TCF Bank Stadium in Minneapolis, MN "),
    Event(name = "Dropkick Murphys 20th Anniversary Tour",
          url = "url",
          cost = "22",
          groupSize = "1",
          duration = "10",
          distance = "3",
          description = "Twenty years ago, a new brand of music hit the world when Dropkick Murphys took hard-edged street punk and mixed it with Irish tradition. Over the years, the band's lineup has changed and the waistbands of their kilts have expanded. But they still bring the fight, the fury, and the rock with the same anthemic rage that has made them popular with spike-wearing punks, sports fans, and Hibernophiles alike. On this trek across the U.S., Dropkick Murphys will be hitting clubs just in time for St. Paddy's Day pre-parties. The tour is in support of 2013's Signed and Sealed in Blood, the group's eighth full-length release. DM's 2005 single, "I'm Shipping Up to Boston," still blares from stadium PA systems around the country. Tiger Army and Darkbuster open."),
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