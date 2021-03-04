import multiprocessing
import gevent
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
worker_class = 'gthread'
threads = 3

def post_response(worker, req, environ, resp):
    worker.log.info("Worker PID %s", worker.pid)