import tensorflow as tf

x_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_data = [[0], [0], [0], [1]]

X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_uniform([2, 1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

logits = tf.add(tf.matmul(X, W), b)
output = tf.nn.sigmoid(logits)

cost = tf.reduce_mean(tf.square(output - Y))
opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op = opt.minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(100):
        for x, y in zip(x_data, y_data):
            _, cost_val = sess.run([train_op, cost], feed_dict={X:[x], Y:[y]})
        print(step, cost_val, sess.run(W), sess.run(b))
    print(sess.run(output, feed_dict={X:x_data}))
