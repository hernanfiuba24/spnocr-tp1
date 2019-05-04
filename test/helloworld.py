import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant([20])
b = tf.constant([30])
c = tf.add(a,b)
session = tf.Session()

result = session.run(c)
print(result)
session.close()
