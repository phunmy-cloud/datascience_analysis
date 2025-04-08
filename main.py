import numpy as np
import pandas as pd
arr = np.array([1, 2, 3, 4, 5, 6]) # one diamension
print(arr)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# array indexing
print(arr[0])
print(arr[4])
print(arr[-2])
print(arr[1:]) # start from index 1 to the end
print(arr2[1, 0])

#maths operation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a * b)
print(np.dot(a,b))
print(np.mean(a))
print(np.mean(b))

#pandas operations

ds = pd.Series([10, 20, 40, 50]) #series data
print(ds)

#dataframe

data = {
    'name': ["adesoji", "adebola", "adewumi"],
    "age": [26, 30, 32],
    "city": ["lagos", "kano", "abuja"]
}
df = pd.DataFrame(data)
print(df)


