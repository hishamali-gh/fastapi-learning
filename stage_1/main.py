from fastapi import FastAPI # Import the 'FastAPI' class

app = FastAPI() # Create an instance of the application

@app.get('/')
def read_root():
    return {'message': 'Hello, from FastAPI!'}
