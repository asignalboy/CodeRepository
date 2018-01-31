#!/usr/bin/pyhton
'''
import input_data
mnist=input_data.read_data_sets('MNIST_data',one_hot=True)
import tensorflow as tf
sess=tf.InteractiveSession()
x=tf.placeholder("float",shape=[None,784])
y_=tf.placeholder("float",shape=[None,10])
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
sess.run(tf.initialize_all_variables())
y=tf.nn.softmax(tf.matmul(x,w)+b)
cross_entropy=-tf.reduce_sum(y_*tf.log(y))
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
for i in range(1000):
    batch=mnist.train.next_batch(50)
    train_step.run(feed_dict={x:batch[0],y_:batch[1]})
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,'float'))
print accuracy.eval(feed_dict={x:mnist.test.images,y_:mnist.test.labels})
'''
def weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial=tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

w_conv1=weight_variable([5,5,1,32])
b_conv1=bias_variable([32])

x_image=tf.reshape(x,[-1,28,28,1])

h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
h_pool1=max_pool_2x2(h_conv1)

w_conv2=weight_variable([5,5,32,64])
b_conv2=bias_variable([64])
h_conv2=tf.nn.relu(conv2d(h_pool1,w_conv2)+b+conv2d)
h_pool2=max_pool_2x2(h_conv2)


