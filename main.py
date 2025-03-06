from fastapi import FastAPI, Query
from functools import wraps
import os
import argparse

app = FastAPI()
DECORATOR_CONDITION = os.getenv("DECORATOR_CONDITION", "false").lower() == "true"
# Parse command-line arguments
# parser = argparse.ArgumentParser(description="Run FastAPI app with a conditional decorator.")
# parser.add_argument("--decorator-condition", type=str, choices=["true", "false"], default="false",
#                     help="Set the decorator condition (true/false).")
# args = parser.parse_args()
#
# # Convert the argument to a boolean
# DECORATOR_CONDITION = args.decorator_condition.lower() == "true"
def custom_decorator(condition: bool):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if condition:
                response["decorated"] = True
            return response
        return wrapper
    return decorator

@app.get("/")
@custom_decorator(condition=DECORATOR_CONDITION)  # Change this based on your condition
def read_root(decorate: bool = Query(default=False)):
    return {"message": "Hello, World!", "decorated_condition": decorate}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)