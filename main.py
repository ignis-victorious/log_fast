#
#  Import LIBRARIES
import uvicorn
from fastapi import FastAPI

#  Import FILES
#  # #


app: FastAPI = FastAPI()


@app.get(path="/")
async def index() -> dict[str, str]:
    return {"message": "Hello"}


@app.get(path="/upload-videos")
async def upload_videos() -> dict[str, str]:
    return {"message": "Video Uploaded"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)

#
#  Import LIBRARIES

#  Import FILES
#  # #
