def shiftMutliplier(m,q):
    # converting to binary 
    bin_m = bin(m).replace('0b','')
    bin_q = bin(q).replace('0b','')

    # checking max length
    if len(bin_m)>len(bin_q):
        max_len=len(bin_m)
    else:
        max_len=len(bin_q)
    
    # setting equal number of bits
    bin_m = bin_m.zfill(max_len)
    bin_q = bin_q.zfill(max_len)
    bin_a = bin(0).replace('0b','')
    bin_a = bin_a.zfill(max_len)
    c='0'
    n=max_len

    # calcucation
    while(n):
        # if Q0 = 1
        if(bin_q[max_len-1]=='1'):
            bin_a = bin(int(bin_m,2)+int(bin_a,2)).replace('0b','')
            if(len(bin_a)>max_len):
                c=bin_a[0]
                bin_a=bin_a[1:]
            bin_a=bin_a.zfill(max_len)
        
        # shift c,a,q
        temp = c+bin_a+bin_q
        c='0'
        bin_a=temp[0:max_len]
        bin_q=temp[max_len:max_len*2]
        n-=1

    # final answer merge
    merged = bin_a+bin_q
    result = int(merged,2)
    print(f"The result obtained in binary = {merged}")
    print(f"The result {m} x {q} = {result}")
    return

a  = int(input("Enter the first number: "))
b  = int(input("Enter the second number: "))
shiftMutliplier(a,b)