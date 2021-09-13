import logging
from pathlib import Path
import time


def function(product, logging_level):
    logging.basicConfig(level=getattr(logging, logging_level.upper()))
    logger = logging.getLogger(__name__)

    logger.debug('[function log] This is a message for debugging')

    for step in range(1, 4):
        time.sleep(1)
        logger.info(f'[function log] Finished step {step}...')

    logger.info('[function log] Done.')

    Path(product).touch()
