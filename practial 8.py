fh =open("prac 8.txt",'w')
abc=[11,22,3,9,6,5,4]
fh.write("Before Sorting:"+str(abc))
abc.sort()
fh.write("After Sorting:"+str(abc))
fh.close()