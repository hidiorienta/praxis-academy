print(sum(i*i for i in range(10)))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))         # dot product


data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
