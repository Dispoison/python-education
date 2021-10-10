"""Comment class"""


class Comment:
    """Comment made by any person related to the restaurant."""
    def __init__(self, author, comment_date, text):
        self.author = author
        self.comment_date = comment_date
        self.text = text

    def __repr__(self):
        return f'Author: {self.author}\n' \
               f'Date: {self.comment_date.strftime("%b %d %Y %H:%M:%S")}\n' \
               f'Text: {self.text}'
