import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Custom Title",
    description="""Custom description.""",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get('/')
async def home():
    return 'none'



if __name__ == "__main__":
    uvicorn.run(app, port=4000)
