from enum import Enum
from multiprocessing.dummy import Process
from queue import Queue


from enum import Enum

class Status(Enum):
    Queued = 'Queued'
    Processing = 'Processing'
    Completed = 'Completed'
    Failed = 'Failed'
    