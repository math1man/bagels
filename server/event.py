class Event:


    def __init__(self, name, catagories = [], time = 0, price = 0):

        self.time = time
        self.catagories = catagories
        self.name = name
        self.price = price
        self.url = ""
        self.location = 0
        self.duration = 0
        self.cost = 0
        self.n_people = 0

