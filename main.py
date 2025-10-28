#
#  Import LIBRARIES
import uvicorn
from fastapi import FastAPI
from logger import logger  # type: ignore

#  Import FILES
#  # #


app: FastAPI = FastAPI()

logger.info(msg="Starting API...")


@app.get(path="/")
async def index() -> dict[str, str]:
    logger.info(msg="Request to index page")
    return {"message": "Hello"}


@app.get(path="/upload-videos")
async def upload_videos() -> dict[str, str]:
    logger.info(msg="Request to video-upload page")
    return {"message": "Video Uploaded"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)

#
#  Import LIBRARIES

#  Import FILES
#  # #
