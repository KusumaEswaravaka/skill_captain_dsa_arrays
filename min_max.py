#finding max value

arr = [10,2,3,4,5]

max = arr[0]
n = len(arr)

for i in range(1,n):
  if arr[i] > max:
    max = arr[i]
print(max)

#find min value

arr = [10,2,3,4,50]
min = arr[0]
n = len(arr)

for i in range(1,n):
  if arr[i] < min:
    min = arr[i]
print(min)


    
