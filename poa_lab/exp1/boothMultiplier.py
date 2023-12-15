def twosCompliment(a):
    result = ""
    for i in range(len(a)):
        if a[i]=='1':
            result+='0'
        else:
            result+='1'
    result = bin(int(result,2)+int('1',2)).replace('0b','')
    return result

def boothMutliplier(x,y):
    # converting to binary 
    bin_m = bin(abs(x)).replace('0b','')
    bin_q = bin(abs(y)).replace('0b','')

    # checking max length
    if len(bin_m)>len(bin_q):
        max_len=len(bin_m)
    else:
        max_len=len(bin_q)
    
    # adding one sign bit 
    max_len+=1

    # setting equal number of bits
    bin_m = bin_m.zfill(max_len)
    bin_q = bin_q.zfill(max_len)

    # checking if m or q is negative
    if x<0:
        bin_m = twosCompliment(bin_m).zfill(max_len)
    if y<0:
        bin_q = twosCompliment(bin_q).zfill(max_len)

    # initialisation
    bin_a='0'
    a = bin_a.zfill(max_len)
    q = bin_q
    m = bin_m
    minus_m = twosCompliment(bin_m).zfill(max_len)
    qo = '0'
    n = max_len

    # calculations
    while(n):
        # '10' condition
        if q[max_len-1]=='1' and qo =='0':
            a = bin(int(a,2)+int(minus_m,2)).replace('0b','')
            if(len(a)>max_len):
                a=a[1:]
            a=a.zfill(max_len)
        
        # '01' condition
        elif q[max_len-1]=='0' and qo =='1':
            a = bin(int(a,2)+int(m,2)).replace('0b','')
            if(len(a)>max_len):
                a=a[1:]
            a=a.zfill(max_len)
        
        # arithematic right shift operation
        merged = a+q+qo
        result = merged[0]
        for i in range(len(merged)-1):
            result +=merged[i]
        a=result[0:max_len]
        q=result[max_len:max_len*2]
        qo=result[-1]
        n-=1
    
    #result 
    result = a+q
    
    # taking 2's compliment if result is neagtive
    if(result[0]=='1'):
        print(f"The result obtained in binary = {result}")
        result = twosCompliment(result).zfill(max_len)
        result = int(result,2)
        print(f"The result {x} x {y} = {-1*result}")
    else:
        print(f"The result obtained in binary = {result}")
        result = int(result,2)
        print(f"The result {x} x {y} = {result}")

a  = int(input("Enter the first number: "))
b  = int(input("Enter the second number: "))
boothMutliplier(a,b)