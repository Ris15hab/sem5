# def twosCompliment(x):
#     result = ""
#     for i in range(len(x)):
#         if(x[i] == '1'):
#             result = result+'0'
#         else:
#             result = result+'1'
#     result = bin(int(result,2)+int('1',2)).replace('0b','')
#     return result

# def boothMutliplier(x,y):
#     bin_m = bin(abs(x)).replace('0b','')
#     bin_q = bin(abs(y)).replace('0b','')

#     if len(bin_m)>len(bin_q):
#         max_len = len(bin_m)
#     else:
#         max_len = len(bin_q)
    
#     bin_m = bin_m.zfill(max_len+1)
#     bin_q = bin_q.zfill(max_len+1)

#     if x<0:
#         bin_m = twosCompliment(bin_m).zfill(max_len+1)
#     if y<0:
#         bin_q = twosCompliment(bin_q).zfill(max_len+1)
    
#     a='0'
#     a = a.zfill(max_len+1)
#     qo = '0'
#     m = bin_m
#     minus_m = twosCompliment(bin_m)
#     q= bin_q
#     n = max_len+1

#     # print(f"m{m}\tminusm{minus_m}\tq{q}")

#     while n:
#         if qo=='0' and q[max_len]=='1':
#             a = bin(int(a,2)+int(minus_m,2)).replace('0b','')
#             if len(a)>max_len+1:
#                 a=a[1:]
#             a = a.zfill(max_len+1)
        
#         elif qo=='1' and q[max_len]=='0':
#             a = bin(int(a,2)+int(m,2)).replace('0b','')
#             if len(a)>max_len+1:
#                 a=a[1:]
#             a = a.zfill(max_len+1)
        
#         merged = a+q+qo
#         result = merged[0]
#         temp = len(merged)-1
#         result = result + merged[0:temp]
#         a = result[0:max_len+1]
#         q = result[max_len+1:(max_len+1)*2]
#         qo = result[-1]
#         n-=1
#         # print(f"merged{merged}\tresult{result}\t a{a}\tq{q}\tqo{qo}")
    
#     result = a+q
    
#     # taking 2's compliment if result is neagtive
#     if(result[0]=='1'):
#         print(f"The result obtained in binary = {result}")
#         result = twosCompliment(result).zfill(max_len)
#         result = int(result,2)
#         print(f"The result {x} x {y} = {-1*result}")
#     else:
#         print(f"The result obtained in binary = {result}")
#         result = int(result,2)
#         print(f"The result {x} x {y} = {result}")

# a  = int(input("Enter the first number: "))
# b  = int(input("Enter the second number: "))
# boothMutliplier(a,b)

# def twosCompliment(x):
#     result = ""
#     for i in range(len(x)):
#         if(x[i]=='1'):
#             result+='0'
#         else:
#             result+='1'
#     result = bin(int(result,2)+int('1',2)).replace('0b','')
#     return result

# def restoring(x,y):
#     bin_q = bin(x).replace('0b','')
#     bin_m = bin(y).replace('0b','')

#     if len(bin_m) > len(bin_q):
#         max_len = len(bin_m)
#     else:
#         max_len = len(bin_q)
    
#     bin_q = bin_q.zfill(max_len)
#     bin_m = bin_m.zfill(max_len+1)

#     a='0'
#     a=a.zfill(max_len+1)
#     m=bin_m
#     minus_m= twosCompliment(m).zfill(max_len+1)
#     q=bin_q
#     n=max_len

#     while n:
#         merged = a+q
#         a = merged[1:max_len+2]
#         q = merged[max_len+2:]

#         if a[0]=='1':
#             a=bin(int(a,2)+int(m,2)).replace('0b','')
#             if len(a)>max_len+1:
#                 a=a[1:]
#             a=a.zfill(max_len+1) 
#         elif a[0]=='0':
#             a=bin(int(a,2)+int(minus_m,2)).replace('0b','')
#             if len(a)>max_len+1:
#                 a=a[1:]
#             a=a.zfill(max_len+1)
        
#         if a[0]=='1':
#             q+='0'
#         else:
#             q+='1'
#         n-=1
    
#     if a[0]=='1':
#         a=bin(int(a,2)+int(m,2)).replace('0b','')
#         if(len(a)>max_len+1):
#             a = a[1:]
#         a = a.zfill(max_len+1)
    
#     print(f"Quotient in binary form: {q}")
#     print(f"Remainder in binary form: {a}")
#     q=int(q,2)
#     a=int(a,2)
#     print(f"Quotient in decimal form: {q}")
#     print(f"Remainder in decimal form: {a}")


# a  = int(input("Enter the divident: "))
# b  = int(input("Enter the divisor: "))
# restoring(a,b)

