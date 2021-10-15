import logging


class Log:
    def __init__(self, file_name):
        self.file_name = file_name
        self.logger = logging.getLogger(__name__)
        self._set_log()

    def _set_log(self):
        self.logger.setLevel(logging.INFO)
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('game.log')
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.INFO)
        c_format = logging.Formatter('%(message)s')
        f_format = logging.Formatter('%(asctime)s - %(message)s', "%Y-%m-%d %H:%M:%S")
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

    def clear_log(self):
        with open(self.file_name, 'w'):
            pass
