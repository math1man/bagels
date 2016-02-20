import random
from event import Event

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