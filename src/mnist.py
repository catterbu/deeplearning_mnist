"""This file is to work on neural nets and deep learning using MNIST dataset"""

import numpy as np
import h5py

with h5py.File('/media/catterbu/Windows8_OS/Users/catterbu/Documents/dev/research/mnist_dataset/train_small.h5', 'r') as hf:
	# print('List of arrays in this file: \n', hf.keys())
	# print('List of items in the base directory:', hf.items())
	hf_0 = hf.get('0')
	print(u'\nlist of items in 0:', hf_0.items())
