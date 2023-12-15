def twosCompliment(a):
    result = ""
    for i in range(len(a)):
        if a[i]=='1':
            result+='0'
        else:
            result+='1'
    result = bin(int(result,2)+int('1',2)).replace('0b','')
    return result

def restoringDivision(x,y):
    # conversion to binary
    bin_q = bin(x).replace('0b','')
    bin_m = bin(y).replace('0b','')

    # checking for maximum length 
    if len(bin_q)>len(bin_m):
        max_len = len(bin_q)
    else:
        max_len = len(bin_m)
    
    bin_q = bin_q.zfill(max_len)
    bin_m = bin_m.zfill(max_len+1)

    # initialisation
    q = bin_q
    m = bin_m
    minus_m = twosCompliment(m).zfill(max_len+1)
    a = '0'
    a = a.zfill(max_len+1)
    n = max_len

    # calculation
    while(n):
        # shilt left
        merged = a+q
        a=merged[1:max_len+2]
        q=merged[max_len+2:]

        # a = a - m
        temp = a
        a = bin(int(a,2)+int(minus_m,2)).replace('0b','')
        if len(a)>max_len+1:
            a=a[1:]
        a = a.zfill(max_len+1)

        # a<0 then performing restoring
        if(a[0]=='1'):
            q = q+'0'
            a = temp
        # a>0
        else:
            q = q+'1'
        n-=1

    
    print(f"Quotient in binary form: {q}")
    print(f"Remainder in binary form: {a}")
    q=int(q,2)
    a=int(a,2)
    print(f"Quotient in decimal form: {q}")
    print(f"Remainder in decimal form: {a}")


a  = int(input("Enter the divident: "))
b  = int(input("Enter the divisor: "))
restoringDivision(a,b)