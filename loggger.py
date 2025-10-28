#
#  Import LIBRARIES
import logging
import sys

#  Import FILES
#  #

token: str = ""
# get logger
logger: logging.Logger = logging.getLogger()

# create formatter
formatter: logging.Formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# create formatter
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(filename="app.log")
# better_stack_handler = LogtailHandler(source_token=token)


# set formatters
stream_handler.setFormatter(fmt=formatter)
file_handler.setFormatter(fmt=formatter)

# add handlers to the logger
# logger.handlers = [stream_handler, file_handler, better_stack_handler]
logger.handlers = [stream_handler, file_handler]

# set log-level
logger.setLevel(level=logging.INFO)
