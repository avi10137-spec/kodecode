# 1.
# def is_even(n):
#     if n%2==0:
#         return True
#     return False
# print(is_even(4))
# 2.
# def factorial(n):
#     sumi=1
#     for i in range(1,n+1):
#         sumi*=i
#         print(sumi)
#     return sumi
# print(factorial(5))
# 4.
# def is_palindrom(stri):
#     booli=False
#     stri1=stri[::-1]
#     if stri1==stri:
#         booli=True
    
#     return booli
# print(is_palindrom("avi"))
# 5.
# def digital_root(num):
#        number1=0
#        while n!=0:
#         digit=n%10
#         number1+=digit
#         n=n//10
#         # print(number1)
#         while number1>=10:
#           x=sum_digits1(number1)
#         number1=x
#         if x<10:
#            return x
#        return number1
# def sum_digits1(n):
#     number1=0
#     while n!=0:
#         digit=n%10
#         number1+=digit
#         n=n//10
#     return number1

# print(sum_digits(99995))
# 6.
# def sum_digit(number):
#     counter=0
#     while number:
#         number=number//10
#         counter+=1
        
#     return counter
# print(sum_digit(12345))
# 7.
# def oposite_number(number):
#     number1=str(number)[::-1]
#     print(number1)
#     for char in number1:
#         if char =="0":
#            numbers1=number1.replace(char,"")
#     return numbers1
# print(oposite_number(1230))
# 8.
# def sort_list(listi):
#     i=0
#     counter=len(listi)
#     while counter>0:
#             if listi[i]==0:
#                   x=listi.pop(i)
#                   listi.append(x)
#                   i-=1
#             i+=1
#             counter-=1
#     return listi
# print(sort_list([1,2,3,0,0,5]))
# 9.
# def stat(listi):
#     print(sum(listi),sum(listi)/len(listi),max(listi),min(listi))
# stat([1,2,3,4,5,6,7])
# 10.
# def oposite(listi):
#     for i in range(len(listi)-1):
#         x=listi.pop()
#         listi.insert(i,x)
#     return listi
# print(oposite([1,2,3,4,5]))
# 11.
# def sorti(listi):
#     listi1=[]
#     for i in range(len(listi)):

#         if listi[i] in listi1:
#             continue
#         listi1.append(listi[i])
#     return listi1


# print(sorti([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))
        

            
        


    
    
        
    






