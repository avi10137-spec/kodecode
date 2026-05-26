import logging

def get_loger(name):
    logger = logging.getLogger("payment")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    file_handler = logging.FileHandler("payment.log", encoding="utf8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return
    