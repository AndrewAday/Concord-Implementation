import sys
import concord
import numpy as np
from concord.computation import (
    Computation,
    Metadata,
    serve_computation
)

from generators import hazard, p
from computations import BayesianChangepointDetection
from distributions import Gaussian


import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Bcd(Computation):
    def __init__(self):
        self.dict = {}
        self.pidx = 0 # print index
        self.detector = BayesianChangepointDetection(hazard(p), Gaussian(1, 0, 1, 0.1))

    def init(self, ctx):
        logger.info("Counter initialized")

    def process_timer(self, ctx, key, time):
        raise Exception('process_timer not implemented')

    def process_record(self, ctx, record):
        result = self.detector.step(float(record.data))
        logger.info(record.data)
        # logger.info(result)
        logger.info(result.argmax())
        # self.pidx += 1
        # if self.dict.has_key(record.key):
        #     self.dict[record.key] += 1
        # else:
        #     self.dict[record.key] = 1
        # if (self.pidx % 1024) == 0:
        #     logger.info(self.dict)

    def metadata(self):
        return Metadata(
            name='bcd',
            istreams=['data'],
            ostreams=[])

logger.info("Main")
serve_computation(Bcd())
