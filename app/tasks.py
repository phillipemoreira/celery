from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

if __name__ == '__main__':
    app.start()

@app.task
def add(x, y):
    return x + y
