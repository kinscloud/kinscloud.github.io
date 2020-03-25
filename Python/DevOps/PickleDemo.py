import pickle

data0 = 'hello world'
data1 = list(range(20))[1::2]
data2 = {'x', 'y', 'z'}
data3 = {'a': data0, 'b': data1, 'c': data2}

# print(data0)
# print(data1)
# print(data2)
# print(data3)

output = open('data.pkl', 'wb')

pickle.dump(data0, output)
pickle.dump(data1, output)
pickle.dump(data2, output)
pickle.dump(data3, output)
output.close()

pkl_file = open('data.pkl', 'rb')
data0 = pickle.load(pkl_file)
data1 = pickle.load(pkl_file)
data2 = pickle.load(pkl_file)
data3 = pickle.load(pkl_file)

print(data0)
print(data1)
print(data2)
print(data3)