from event import Event

class User:
    """
    The User class maintains the user's data, such as which events they like and which they have rejected in the past.
    """

    def __init_(self, budget = 100, range = 100, like = {}, rejected_events = set()):

        self.budget = budget
        self.range = range
        self.like = like
        self.rejected_events = rejected_events

    def update(self, path):
        """
        Update the user object by reading from the user's preferences file.

        :param path: string path to config file
        :return: None
        """

        self.like = {"Art": True, "Sports": False}
        self.rejected_events = {Event("Sculpture Garden"), Event("Animal Shelter")}