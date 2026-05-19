# exesrise
# 1.
# def remove_duplicate(listi):
#     return list(set(listi))
# print(remove_duplicate([1, 2, 2, 3, 1, 4, 3]))
# 2.
# def count_unice(listi):
#     seti=set(listi)
#     counter=0
#     for item in seti:
#         counter+=1
#     return counter
# print(count_unice( [1, 2, 2, 3, 1, 4] ))
# 3.
# def commen_element(list1,list2):
#     list3=set(list1) & set(list2)
#     return sorted(list3)
# print(commen_element([1, 2, 3, 4], [3, 4, 5, 6]))
# 4.
# def is_subset(list1,list2):
#     list3= set(list1).symmetric_difference(set(list2))
#     return list3
# print(is_subset([1, 2, 3, 4], [3, 4, 5, 6]))
# 5.
# def is_subset(list1,list2):
#     booli=True
#     for item in set(list1):
#         if item not in list2:
#             booli =False
#     return booli
# print(is_subset( [1, 2, 6], [1, 2, 3, 4, 5]))
# 6.
# def unice_char(stri):
#     seti=set(stri)
#     if len(stri)==len(seti):
#         return True
#     return False
# print(unice_char("abcdea"))
# 7.
# def first_repeated(listi):
#     seti=set()
#     for item in listi:
#         seti.add(item)
#         if item in seti:
#            return item
#         if len(seti)== len(listi):
#            return None
# print(first_repeated([1, 2, 3, 2, 4, 1] ))
# 8.
def ditinct(stri):
    listi=stri.lower().split(" ")
    seti=set(listi)
    return seti
print(ditinct( "The cat and the dog and the bird"))
        


