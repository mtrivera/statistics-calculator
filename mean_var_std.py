import numpy as np

def calculate(list):
    # Returns a dictionary
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')