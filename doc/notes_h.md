# TensorFlow Notes

Where [`tf.keras.Model`](https://github.com/tensorflow/tensorflow/blob/a6d8ffae097d0132989ae4688d224121ec6d8f35/tensorflow/python/keras/engine/training.py#L56) class originates from:
 - [`Network`](https://github.com/tensorflow/tensorflow/blob/a6d8ffae097d0132989ae4688d224121ec6d8f35/tensorflow/python/keras/engine/network.py#L67)
 - [`base_layer.Layer`](https://github.com/tensorflow/tensorflow/blob/a6d8ffae097d0132989ae4688d224121ec6d8f35/tensorflow/python/keras/engine/base_layer.py#L71)
 - [`CheckPointableBase`](https://github.com/tensorflow/tensorflow/blob/a6d8ffae097d0132989ae4688d224121ec6d8f35/tensorflow/python/training/checkpointable/base.py#L482)
- `object`

Saving the model as an object already solves the intital issue of optimization.


# Possible to look at

- [Kubeflow](https://www.kubeflow.org/), [Blog-Post](https://opensource.com/article/18/12/introduction-kubeflow)
- TFX, [TF Data Validation](https://github.com/tensorflow/data-validation), 