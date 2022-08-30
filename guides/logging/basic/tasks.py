# %%
import logging
from pathlib import Path
import time


# %%
def function(product):
    # uncomment the next line if using Python >= 3.8 on macOS
    # logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(__name__)

    for step in range(1, 4):
        time.sleep(1)
        logger.info(f'[function log] Finished step {step}...')

    logger.info('[function log] Done.')

    Path(product).touch()
