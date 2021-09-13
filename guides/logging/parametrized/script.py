import logging
import time

# +
import sys

# + tags=["parameters"]
upstream = None
product = None
logging_level = None

# +
logging.basicConfig(level=getattr(logging, logging_level.upper()),
                    stream=sys.stdout)
logger = logging.getLogger(__name__)

# +
logger.debug('[script log] This is a message for debugging')

for step in range(1, 4):
    time.sleep(1)
    logger.info(f'[script log] Finished step {step}...')

logger.info('[script log] Done.')
