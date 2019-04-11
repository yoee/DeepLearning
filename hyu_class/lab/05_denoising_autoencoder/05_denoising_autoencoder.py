#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

keep_prob = tf.placeholder(tf.float32)

random_noise = tf.placeholder(tf.float32, [28*28])
X = tf.placeholder(tf.float32, [None, 28 * 28])
Y = tf.placeholder(tf.float32, [None, 28 * 28])  # ??

# encoder
W1 = tf.Variable(tf.random_uniform([784, 256], -1., 1.))
b1 = tf.Variable(tf.random_uniform([256], -1., 1.))
L1 = tf.sigmoid(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob)

W2 = tf.Variable(tf.random_uniform([256, 64], -1., 1.))
b2 = tf.Variable(tf.random_uniform([64], -1., 1.))
L2 = tf.sigmoid(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob)

# decoder
W3 = tf.Variable(tf.random_uniform([64, 256], -1., 1.))
b3 = tf.Variable(tf.random_uniform([256], -1., 1.))
L3 = tf.sigmoid(tf.matmul(L2, W3) + b3)
L3 = tf.nn.dropout(L3, keep_prob)

W4 = tf.Variable(tf.random_uniform([256, 784], -1., 1.))
b4 = tf.Variable(tf.random_uniform([784], -1., 1.))
decoder = tf.matmul(L3, W4) + b4

cost = tf.reduce_mean(tf.pow(X - decoder, 2))
opt = tf.train.AdamOptimizer(
    learning_rate=0.001,
    beta1=0.9,
    beta2=0.999,
    epsilon=1e-08,
    use_locking=False,
    name='Adam'
).minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(1000):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, _ = mnist.train.next_batch(batch_size)
        batch_xs_noise = [d + np.random.rand(784) for d in batch_xs]
        _, cost_val = sess.run([opt, cost], feed_dict={X:batch_xs_noise, Y:batch_xs, keep_prob: 0.7})
        total_cost += cost_val
    print('Epoch :', '%04d' % (epoch + 1), 'Avg. cost =', '{:.3f}'.format(total_cost / total_batch))


# In[5]:


for i in range(0, 5):
    x, _ = mnist.train.next_batch(1)
    x_noise = [d + np.random.rand(784) for d in x]

    output = sess.run(decoder, feed_dict={ X: x_noise, keep_prob: 0.7})
    
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(np.reshape(x, (28, 28)))
    ax[1].imshow(np.reshape(x_noise, (28, 28)))
    ax[2].imshow(np.reshape(output, (28, 28)))


# In[6]:


saver = tf.train.Saver()
saver.save(sess, 'auto_encoder')


# In[ ]:




