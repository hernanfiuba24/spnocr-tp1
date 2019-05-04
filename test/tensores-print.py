import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

escalar = tf.constant([2])
vector = tf.constant([3,3,3,])
matrix = tf.constant([[3,3,3,],[3,3,3,],[3,3,3,]])
tensor = tf.constant([[[3,3,3,],[3,3,3,],[3,3,3,]],[[3,3,3,],[3,3,3,],[3,3,3,]],[[3,3,3,],[3,3,3,],[3,3,3,]]])
with tf.Session() as session:
    print()
    result = session.run(escalar)
    print(result)
    print()
    result = session.run(vector)
    print(result)
    print()
    result = session.run(matrix)
    print(result)
    print()
    result = session.run(tensor)
    print(result)
    print()
    
    
    

