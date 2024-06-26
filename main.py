import uvicorn
from fastapi import FastAPI
from routers.posts import router as posts_router

app = FastAPI()
app.include_router(posts_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")
