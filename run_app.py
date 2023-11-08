import os
from app import app  

def run_gunicorn():
    os.system("gunicorn -w 30 -b 0.0.0.0:8000 app:app")

if __name__ == '__main__':
    run_gunicorn()
