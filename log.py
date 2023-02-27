import logging

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(
    fmt=logging.Formatter("%(asctime)s %(levelname)s %(message)s"),
)

logger = logging.getLogger("enigma")
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.propagate = False
