# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt
import numpy as np
import torchvision

from utils import load_data, imshow

# %% tags=["parameters"]
upstream = ['load']
# This is a placeholder, leave it as None
product = None


# %%
def show_images(loader, batch_size=4):
    # get some random images
    dataiter = iter(loader)
    images, labels = dataiter.next()

    # show images
    imshow(torchvision.utils.make_grid(images))
    # print labels
    print(' '.join(f'{classes[labels[j]]:5s}' for j in range(batch_size)))


# %%
trainloader, testloader, classes = load_data(upstream['load']['raw'])

# %% [markdown]
# ## Train images sample

# %%
show_images(trainloader)

# %% [markdown]
# ## Test images sample

# %%
show_images(testloader)

# %%
