
import matplotlib.pyplot as plt
import gzip
import _pickle as cPickle
import sys
import numpy as np

def plot_mnist_images(images, cls_true, cls_pred=None):
    assert len(images) == len(cls_true) == 25

    # create figure with 3x3 sub-plots.
    fig, axes = plt.subplots(5, 5, figsize=(18, 15))
    fig.subplots_adjust(hspace=0.2, wspace=0.2)

    for i, ax in enumerate(axes.flat):
        # plot image
        # ax.imshow(images[i], cmap='binary')
        ax.imshow(images[i], cmap=plt.cm.gray)

        # show true and predicted classes.
        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

        ax.set_xlabel(xlabel)

        # remove ticks from the plot.
        ax.set_xticks([])
        ax.set_yticks([])

    # ensure the plot is shown correctly with multiple plots in a single Notebook cell.
    plt.show()


def plot_acc_loss(history, epochs):

    # plot the training loss and accuracy
    fig = plt.figure(figsize=(9, 3), dpi=100)
    plt.subplots_adjust(wspace=0.6)
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    ax1.plot(np.arange(0, epochs), history.history['acc'], 'b', label='training accuracy')
    ax1.plot(np.arange(0, epochs), history.history['val_acc'], 'r', label='validation accuracy');
    ax1.set_title('Accuracy')
    ax1.set_xlabel("Number of epoch ")
    ax1.set_ylabel("Accuracy")
    ax1.legend(loc="best")

    ax2.plot(np.arange(0, epochs), history.history["loss"], label="training loss")
    ax2.plot(np.arange(0, epochs), history.history["val_loss"], label="validation loss")
    ax2.set_title("Loss")
    ax2.set_xlabel("Number of epoch ")
    ax2.set_ylabel("Loss")
    ax2.legend(loc="best");

    print('Loss:')
    print('  - loss [training dataset]: {0:.3f}'.format(history.history['loss'][-1]))
    print('  - loss [validation dataset: {0:.3f}'.format(history.history['val_loss'][-1]))
    print('')
    print('Accuracy:')
    print('  - accuracy [training dataset]: {:.2f}%'.format(100 * history.history['acc'][-1]))
    print('  - accuracy [validation dataset: {:.2f}%'.format(100 * history.history['val_acc'][-1]))


def load_data(path):
    # get mnist data, split between train and test sets
    f = gzip.open(path, 'rb')
    if sys.version_info < (3,):
        data = cPickle.load(f)
    else:
        data = cPickle.load(f, encoding='bytes')
    f.close()
    return data




from matplotlib import pyplot as plt
import numpy as np
import json

def plot_mnist_testdata(): 
    with open("data/test.json", "r") as f:
        images = f.readlines()
    plt.figure(figsize=(20,4))
    for i, image in enumerate(images):
        if i < 4:
            image = json.loads(image)
            image = np.array(image['x'])   
            plt.subplot(1, 5, i+1)
            plt.imshow(np.reshape(image, (28,28)), cmap=plt.cm.gray)

import os
def setwd():
    WORKINGDIR = os.getcwd()
    folders = WORKINGDIR.split('/')
    if folders.pop() == 'notebook':  # or a list: in ['notebook', 'src', etc.]
      WORKINGDIR = '/'.join(folders)
      print("Changed to New working directory:\t{}".format(WORKINGDIR))
    else:
      print("Current Working direcotory is kept:\t{}".format(WORKINGDIR))
    os.chdir(WORKINGDIR)