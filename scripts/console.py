import os

def start():
    # run main app
    os.system('python src/app.py')


def serve():
    # run server
    os.system('uvicorn src.server:app --reload')