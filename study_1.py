
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 3, 4]
w = 2
learning_rate = 0.01

for learning_cnt in range(0, 520):
    for i in range(0, len(x)):
        sum = 2 * (w * x[i] - y[i]) * x[i]
    update_w = learning_rate * ( sum / len(x) )
    w = w - update_w
    print('learning_cnt = {}, w = {}'.format(learning_cnt, w))