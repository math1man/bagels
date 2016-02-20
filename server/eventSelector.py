import random
# from event import Event
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
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = "Minnesota hosts Chicago in Minnesota's first-ever outdoor hockey game.  The two central-division rivals square off at TCF Bank Stadium in Minneapolis, MN "),
    Event(name = "Dropkick Murphys 20th Anniversary Tour",
          url = "http://www.citypages.com/event/dropkick-murphys-20th-anniversary-tour-8048046",
          cost = "Free! With ",
          groupSize = "1",
          duration = "",
          distance = "3",
          description = "Twenty years ago, a new brand of music hit the world when Dropkick Murphys took hard-edged street punk and mixed it with Irish tradition. Over the years, the band's lineup has changed and the waistbands of their kilts have expanded. But they still bring the fight, the fury, and the rock with the same anthemic rage that has made them popular with spike-wearing punks, sports fans, and Hibernophiles alike. On this trek across the U.S., Dropkick Murphys will be hitting clubs just in time for St. Paddy's Day pre-parties."),
    Event(name = "Como Zoo Conservatory",
          url = "http://www.comozooconservatory.org/plan/#/visitor-guide",
          cost = "Free! With suggested $3 donation.",
          groupSize = "Any size!",
          duration = "1-5 hours",
          distance = "6.2 miles",
          description = "Enjoy exotic plants and beautiful displays in our various gardens. Learn more about a few of our animals before your visit."),
    '''Event(name = "Google Developers Group - the Nerdery",
          url = "http://www.meetup.com/gdg-tc/",
          cost = "Free, but coding experience recommended",
          groupSize = "1+",
          duration = "3 hours",
          distance = "8.9 miles",
          description = "Study Jams are community-organized study groups around Google online developer courses. The goal is to support as many students as possible in completing the course, thereby raising the technical level of the community."),
     Event(name = "Go ice-skating outdoors! - Do Something!",
          url = "",
          cost = "Skate rental and modest rink fees! ",
          groupSize = "As many as you want",
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = " "),
     Event(name = "Minnesota Wild v. Chicago Blackhawks",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "115",
          groupSize = "2-4",
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = " "),
     Event(name = "Merlin's Rest Pub - Minneapolis, MN",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "$9-15 per person",
          groupSize = "Call ahead for parties bigger than 6!",
          duration = "Half-hour to 2 hours",
          distance = "3 mi.",
          description = "Whether your taste is for a hearty meal of Bangers and Mash or our authentic Fish and Chips (voted best Fish & Chips in the Twin Cities) you can wash it down with the finest beers of this land or any other – and the most comprehensive list of Irish and Scotch Whisky in all of Minnesota."),
     Event(name = "Minnesota Wild v. Chicago Blackhawks",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "115",
          groupSize = "2-4",
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = " "),
     Event(name = "Minnesota Wild v. Chicago Blackhawks",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "115",
          groupSize = "2-4",
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = " "),
     Event(name = "Minnesota Wild v. Chicago Blackhawks",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "115",
          groupSize = "2-4",
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = " "),
     Event(name = "Minnesota Wild v. Chicago Blackhawks",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "115",
          groupSize = "2-4",
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = " "),
     Event(name = "Minnesota Wild v. Chicago Blackhawks",
          url = "http://espn.go.com/video/clip?id=14808471&ex_cid=espnapi_public",
          cost = "115",
          groupSize = "2-4",
          duration = "2.5-3 hours",
          distance = "5 miles",
          description = " "),'''
])


@endpoints.api(name='events', version='v1')
class EventsApi(remote.Service):
  """Events API v1."""

  @endpoints.method(message_types.VoidMessage, EventCollection,
                    path='events/list', http_method='GET',
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