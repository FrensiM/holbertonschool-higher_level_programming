#!/usr/bin/python3
'''class that inherits'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        txt = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        txt += " - {}".format(self.width)
        return txt
