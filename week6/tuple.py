# exesisise
# 1.
# def sum_tapi(tuple):
#     sumi=0
#     for item in tuple:
#         sumi+=item
#     return sumi
# print(sum_tapi((1,2,3)))
# 2.
# def max_tapi(tuple):
#     maxi=0
#     for item in tuple:
#         if item > maxi:
#             maxi = item
#     return maxi
# print(max_tapi((1,2,3)))
# 3.
def count_in_tapi(tuple,val):
    sumi_of_val=0
    for item in tuple:
        if item == val:
            sumi_of_val += 1
    return sumi_of_val
print(count_in_tapi((1,1,2,2,2),2))
# 4.
# def revers_tupi(tuple):
#     tupi2=()
#     for i in range(len(tuple)):
#         tupi2 += (tuple[-1-i],)
#     return tupi2
# print(revers_tupi((1,2,3,4)))
# 5.
#     new_tupi=()
#     for i in range(0,len(tuple),2):
#         print(tuple[i])
#         a = (tuple[i+1],tuple[i])
#         new_tupi += (a,)
#     return new_tupi
# print((swap_pairs((1,2,3,4,5,6))))
# 6.
# def maxi_and_min(tuple):
    
#     maxi=0
#     mini=tuple[0]
#     for i in range(len(tuple)):
#         if tuple[i]>maxi:
#             maxi = tuple[i]
#         if tuple[i]< mini:
#             mini = tuple[i]
#     return maxi,mini
# print(maxi_and_min((1,2,3,4,5,6)))
# # 7.
# def distance(tupi1,tupi2):
#     return ((tupi1[0]-tupi2[0])**2)+((tupi1[1]-tupi2[1])**2)**0.5
# print(distance((0,0),(3,4)))
# 8.
# def mergi(tupi1,tupi2):
#     return tuple(sorted(tupi1+tupi2))
# 9.
# def frequency_table(tuple):
#     new_tuple=()
#     for item in tuple:
#         counter=count_in_tapi(tuple,item)
#         tupi=item,counter
#         if tupi in new_tuple:
#             continue
#         new_tuple += tupi,
#     return new_tuple
# print(frequency_table( ("a", "b", "a", "c", "b", "a") ))
# 10.
def rotate(tuple,val):
    first_tuple=tuple[-val:]
    last_tuple=tuple[:-val]
    final=first_tuple+last_tuple
    return final
print(rotate((1,2,3,4,5),2))
#    if val> len(listi):
#       val=val%len(listi)
#       print(val)
# rotate([1, 2, 3, 4, 5],8)

    

    
    
    


