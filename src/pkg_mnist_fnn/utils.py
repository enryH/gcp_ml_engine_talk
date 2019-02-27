import os
import numpy as np

def load_data(rel_path='./data/'):
    """
    Load data in memory from local source, from data-repository
    or bucket (ToDo)

    Return
    -----
    x_train: numpy.array
        Shape: (60000, 28, 28)
    y_train: numpy.array
        Shape: (10000, )
    x_test: numpy.array
        s
    y_test: numpy.array
    """
    try:
        path = os.path.normpath(os.getcwd() + "/" + rel_path + "/mnist.npz")
        with np.load(path) as f:
            x_train, y_train = f['x_train'], f['y_train']
            x_test, y_test = f['x_test'], f['y_test']
            print("Loaded data from {}".format(path))  
        return (x_train, y_train), (x_test, y_test)
    except Exception:
        try:
            from tensorflow.keras.datasets import mnist
            return mnist.load_data() # (x_train, y_train), (x_test, y_test)
        except Exception:
            raise Exception("Not Connection to Server: Download manually to ./data/ from {}".format(
            "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"
            ))