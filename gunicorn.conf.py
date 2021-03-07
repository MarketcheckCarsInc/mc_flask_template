import multiprocessing
import gevent
#More info on gunicorn: 
#1: https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7
#2: https://stackoverflow.com/questions/38425620/gunicorn-workers-and-threads

#workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
worker_class = 'gthread'   #gevent does not work with grpc python , causing issue with reading from bigtable , at the time of this writing
threads = 3

def post_response(worker, req, environ, resp):
    worker.log.info("Worker PID %s", worker.pid)