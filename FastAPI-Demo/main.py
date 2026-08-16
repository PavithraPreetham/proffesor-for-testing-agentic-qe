from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def show():
    return "Hello World"


@app.get("/products")
def get_products():
    return {"name": "laptop", "price": "28638"}


@app.get("/login")
def login():
    return {"message": "loggedin"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
