import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
train = mnist.train

x = tf.placeholder("float32", [None, 784])

w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, w) + b)
y_ = tf.placeholder("float32", [None, 10])

coress = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(coress)
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
for i in range(1000):
    batch_x, batch_y = train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_x, y_: batch_y})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))