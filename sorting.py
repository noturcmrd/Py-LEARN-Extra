

a = [1,4,6,3,2,0]
# i = 0
# while True:
#     if a[(i+1)] < a[i]:
#         a[(i+1)], a[i] = a[i], a[(i+1)] 


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan

bubble_sort(a)
print(a)
