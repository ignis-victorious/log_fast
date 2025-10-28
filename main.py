#
#  Import LIBRARIES
import uvicorn
from fastapi import FastAPI

# from fastapi import FastAPI, Request
# from logger import logger  # type: ignore
from starlette.middleware.base import BaseHTTPMiddleware

#  Import FILES
from middleware import log_middleware

#  # #


app: FastAPI = FastAPI()
app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=log_middleware)
# app.add_middleware(middleware_class=log_middleware)

# logger.info(msg="Starting API...")


# @app.middleware(middleware_type="http")
# async def log_middleware(request: Request, call_next):
#     log_dict: dict[str, str] = {"url": request.url.path, "method": request.method}
#     logger.info(msg=log_dict)

#     response = await call_next(request)
#     return response


@app.get(path="/")
async def index() -> dict[str, str]:
    # logger.info(msg="Request to index page")
    return {"message": "Hello"}


@app.get(path="/upload-videos")
async def upload_videos() -> dict[str, str]:
    # logger.info(msg="Request to video-upload page")
    return {"message": "Video Uploaded"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)

#
#  Import LIBRARIES

#  Import FILES
#  # #
