import sys
import time
import concord
import numpy as np
from concord.computation import (
    Computation,
    Metadata,
    serve_computation
)
from generators import test1

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def time_millis():
    return int(round(time.time() * 1000))


class Generator(Computation):
    def __init__(self):
        self.words = ['foo', 'bar', 'baz', 'fiz', 'buzz']
        self.X = test1()
        self.indx = 0

    def sample(self):
        """returns a random word"""
        import random
        return random.choice(self.words)

    def init(self, ctx):
        logger.info("Source initialized")
        ctx.set_timer('loop', time_millis())

    def process_timer(self, ctx, key, time):
        # stream, key, value. empty value, no need for val
        ctx.produce_record("data", 'value', str(self.X[self.indx]))
        self.indx += 1

        # emit records every 100ms
        ctx.set_timer("main_loop", time_millis() + 1000)

    def process_record(self, ctx, record):
        raise Exception('process_record not implemented')

    def metadata(self):
        return Metadata(
            name='generator',
            istreams=[],
            ostreams=['data'])

logger.info("Main")
serve_computation(Generator())
