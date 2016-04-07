a = 9999
b = 123
def bigsum(a,b):
    temp_a = []
    temp_b = []
    for each in range(len(str(a))-len(str(b))):
        temp_b.append(0)

    for i in range(len(str(b))):
        temp_b.append(str(b)[i])

    for i in range(len(str(a))):
        temp_a.append(str(a)[i])
    print (temp_a,temp_b)
    carry = 0
    result = []
    for i in range(len(temp_a)-1,-1,-1):
       c_s = int(temp_a[i])+int(temp_b[i])+carry
       if i == 0:
           result.append(c_s)
           return result
       if len(str(c_s))>1:
           carry = int(str(c_s)[:len(str(c_s))-1])
           c_s = int(str(c_s)[len(str(c_s))-1])
       else:
           carry = 0
       result.append(c_s)

    return  result

print (list((reversed(bigsum(a,b)))))






