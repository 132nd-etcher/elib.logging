# coding=utf-8
import logging


class QueuedLoggingHandler(logging.Handler):

    def __init__(self, queue):
        logging.Handler.__init__(self, level=logging.DEBUG)
        self.queue = queue

    def emit(self, record):
        self.queue.put(record)
