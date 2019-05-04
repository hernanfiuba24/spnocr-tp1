import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

matrix_one = tf.constant([[1,2,3],[2,3,4],[3,4,5]])
matrix_two = tf.constant([[2,2,2],[2,2,2],[2,2,2]])
#SUMA DE MATRICES
first_operation = tf.add(matrix_one, matrix_two)
#SUMA DE MATRICES USANDO EL OPERADOR +
second_operation = matrix_one + matrix_two
#MULTIPLICACIÓN DE MATRICES
third_operation = tf.matmul(matrix_one, matrix_two)

with tf.Session() as session:
    result = session.run(first_operation)
    print('Defined using tensorflow function :')
    print(result)
    result = session.run(second_operation)
    print('Defined using normal expression :')
    print(result)
    result = session.run(third_operation)
    print('Defined using tensorflow function :')
    print(result)