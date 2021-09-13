import logging
import time

# +
import sys

# + tags=["parameters"]
upstream = None
product = None

# +
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

# +
for step in range(1, 4):
    time.sleep(1)
    logger.info(f'[script log] Finished step {step}...')

logger.info('[script log] Done.')
