from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "It's FastApi Boilerplate-Pro"}
