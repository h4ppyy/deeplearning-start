import tensorflow as tf

print('tf.test.gpu_device_name() => ', tf.test.gpu_device_name())

if tf.test.gpu_device_name(): 
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")