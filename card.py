from random import randrange

class Card():

    def __init__(self):
        self.ini = 0

    def get_face_value(self):
        return (randrange(1,13))