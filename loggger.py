#
#  Import LIBRARIES
import logging
import sys

#  Import FILES
#  #


# get logger
logger: logging.Logger = logging.getLogger()

# create formatter
formatter: logging.Formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# create formatter
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(filename="app.log")
# set formatters
stream_handler.setFormatter(fmt=formatter)
file_handler.setFormatter(fmt=formatter)

# add handlers to the logger
logger.handlers = [stream_handler, file_handler]

# set log-level
logger.setLevel(level=logging.INFO)
