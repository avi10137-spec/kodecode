# 1.
# listi=[1,2,3,4,5]
# sumi = 0
# for num in listi:
#     sum += num
# print(sum)
# # 2.
# listi=[1,2,3,4,5]
# maxi = listi[0]
# for num in listi:
#     if num > maxi:
#         maxi=num
    
# print(maxi)
# 3.
# def count_valoue(listi,val):
#     counter = 0
#     for number in listi:
#         if number == val:
#             counter+=1
#     return counter
# 4.
# def given_revers(listi):
#     listi2=[]
#     for i in range(len(listi)):
#         listi2.append(listi[-1-i])
#     return listi2
# print(given_revers([1,2,3,4,5]))
# 5.
# def remove_duplicate(listi):
#     listi2=[listi[0]]
#     for i in range(len(listi)):
#         if listi [i] not in listi2:
#             listi2.append(listi[i])
#     return listi2
# print(remove_duplicate([1, 2, 2, 3, 1, 4, 3]))
# 6.
# def given_second(listi):
#     listi2 = sorted(listi,reverse=True)
#     maxi = listi2[0]
#     for num in listi2:
#         if listi2[0] == listi2[-1]:
#             return None
#         if num != maxi:
#             return num
# print(given_second([10,10,10]))
# 7.
# def mergi(list1,list2):
#     list3=[]
#     list3.extend(list1)
#     list3.extend(list2)
#     list3.sort()
#     return list3
# print(mergi([1, 3, 5], [2, 4, 6] ))
# 8.
def rotate(listi,val):
#     first_list=listi[-val:]
#     last_list=listi[:-val]
#     final=first_list+last_list
#     return final
# print(rotate([1, 2, 3, 4, 5],))
   if val> len(listi):
      val=val%len(listi)
      print(val)
rotate([1, 2, 3, 4, 5],8)



        


