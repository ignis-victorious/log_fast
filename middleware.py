#
#  Import LIBRARIES
from fastapi import Request
from logger import logger  # type: ignore

#  Import FILES
#  # #


async def log_middleware(request: Request, call_next):
    log_dict: dict[str, str] = {"url": request.url.path, "method": request.method}
    logger.info(msg=log_dict, extra=log_dict)
    # logger.info(msg=log_dict)

    response = await call_next(request)
    return response
