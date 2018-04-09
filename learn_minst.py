import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
train = mnist.train
print(train.images[0].size)

