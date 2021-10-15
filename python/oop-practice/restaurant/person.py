"""Person functionality"""


from abc import ABC
from datetime import datetime

from .comment import Comment


class Person(ABC):
    """Basic abstract person class"""
    def __init__(self, name, surname=None, phone_number=None, email=None, gender=None, birth_date=None, address=None):
        self._name = name
        self._surname = surname
        self._phone_number = phone_number
        self._email = email
        self._gender = gender
        self._birth_date = birth_date
        self._address = address
        self._comments = []

    def __repr__(self):
        return f'{self.__class__.__name__} {self._name}'

    def make_comment(self, text):
        """Makes a comment"""
        now = datetime.now()
        self._comments.append(Comment(self, now, text))

    def get_all_comments(self):
        """Gets all the person's comment"""
        return self._comments
