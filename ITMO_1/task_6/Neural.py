import random
import numpy as np
import matplotlib.pyplot as plt

class Neural:
    def __init__(self,
                 path_dataset = '', input_dim = 9, output_dim = 2, h_dim = 25, alpha = 0.00001, num_epochs = 1000, batch_size = 30):
