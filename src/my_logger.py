import logging

class Default():
    def __init__(self) -> None:
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename="log.log", level=logging.DEBUG, format = LOG_FORMAT)
        self.my_logger = logging.getLogger()
