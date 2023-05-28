import numpy

# a = numpy.array([1,2,3,4]).reshape(2,2)
# c = numpy.arange(1,10+1).reshape(5,2)
# print(a)
# print(c)
a = numpy.array([[1,2,3], [4,5,6]])
b = numpy.ones([3,1])
c = numpy.array([[4,5, 6], [7,8,9]])
print(a, end="\n\n")
print(b, end="\n\n")
print(c, end="\n\n")
perkalianMatriks = numpy.dot(a,b)
print(perkalianMatriks)