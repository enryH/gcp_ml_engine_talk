import os
import numpy as np

from io import BytesIO
import tensorflow as tf
import numpy as np
from tensorflow.python.lib.io import file_io


def load_data(path='./data/'):
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
        _path = os.path.normpath(path)
        with np.load(_path) as f:
            x_train, y_train = f['x_train'], f['y_train']
            x_test, y_test = f['x_test'], f['y_test']
            print("Loaded data from {}".format(_path))
        return (x_train, y_train), (x_test, y_test)
    except Exception:
        try:
            f = BytesIO(file_io.read_file_to_string(
                filename=path,
                binary_mode=True
            ))
            data = np.load(f)
            with data as f:
                x_train, y_train = f['x_train'], f['y_train']
                x_test, y_test = f['x_test'], f['y_test']
                print("Loaded data from {}".format(path))
            return (x_train, y_train), (x_test, y_test)
        except Exception:
            try:
                from tensorflow.keras.datasets import mnist
                (x_train, y_train), (x_test, y_test) = mnist.load_data()
                return (x_train, y_train), (x_test, y_test)
            except Exception:
                raise Exception("Not Connection to Server: Download manually to ./data/ from {}".format(
                    "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"
                ))
