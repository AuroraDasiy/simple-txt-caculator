file=open('1.txt','r+')
list1=[]
a=file.readlines()  #list
file.seek(0)
b=[]
for i in range(0,len(a)):
    a[i]=list(a[i])
    for i1 in a[i]:
        if i1=='\n':
            del a[i][-1] #del \n
    a[i]=''.join(a[i])
    c=eval(a[i])
    b.append(c)
file.close()
file=open('1.txt','w+')
for i in range(0,len(a)):
    file.write(a[i])
    file.write('={}\n'.format(b[i]))

