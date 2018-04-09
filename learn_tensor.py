import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
result = sess.run(product)
print(result)


b = tf.constant(0.1, shape=[3])
print(sess.run(b))

c = tf.truncated_normal(shape=[5, 5, 1, 3], mean=0, stddev=1)
print(sess.run(c))
sess.close()