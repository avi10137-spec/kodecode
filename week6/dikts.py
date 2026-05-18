# exesrise
# 1.
# def sum_values(dicti):
#     sumi=0
#     for val in dicti.values():
#         sumi += val
#     return sumi
# 2.
# def get_maxi(dicti):
#     maxi=0
#     maxi_key=""
#     for key, val in dicti.items():
#         if val > maxi:
#             maxi = val
#             maxi_key=key
#     return maxi_key
# print(get_maxi({"a": 3, "b": 7, "c": 9}))
# 3.
# def count_char(stri):
#     dicti={}
#     for key in stri:
#         if key in dicti:
#             dicti[key] +=1
#         else:
#             dicti[key] =1
#     return dicti
# print(count_char("banana"))
# # 4.
# def invert_dicti(dicti):
#     dicti2={}
#     for k , v in dicti.items():
#         dicti2[v]=k
#     return dicti2
# print(invert_dicti({"a": 1, "b": 2}))
# 5.
# def mergi(dict1,dict2):
#     for key ,val in dict2.items():
#         if key in dict1:
#             dict1[key]= dict2[key]
#         else:
#             dict1[key] = dict2[key]
#     return dict1
# print(mergi( {"a": 1, "b": 2}, {"b": 20, "c": 30}))
# 6.
# def filter_dicti(dicti,num):
#     dicti2={}
#     for key ,val in dicti.items():
#         if val > num:
#             dicti2 [key] = val
#     return dicti2
# print(filter_dicti({"a": 1, "b": 5, "c": 3, "d": 8}, 3))
# 7.  
# def group_first_letter(list):
#     dicti={}
#     for word in list:
#         if word[0]in dicti:
#             dicti[word[0]].append(word)
#         else:
#             dicti[word[0]]=[word]
#     return dicti
# print(group_first_letter( ["apple", "ant", "banana", "berry", "cherry"]))
# 8.
# def word_frequncy(stri):
#     dicti={}
#     listi=stri.split(" ")
#     for word in listi:
#         if word in dicti:
#             dicti[word] +=1
#         else:
#             dicti[word] =1
#     return dicti
# print(word_frequncy("the cat sat on the mat"))
# 9.
# def commen_keys(dict1,dict2):
#     listi=[]
#     for k in dict2:
#         if k in dict1:
#             listi.append(k)
#     return sorted(listi)
# print(commen_keys( {"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7}))
def most_frequent(dicti):
    dicti2={}
    for key,val in dicti.items():
        if val in dicti2.values():
            dicti2[val]+=1
        else:
            dicti2[val]=1
    maxi=0
    maxi_key=""
    for key,val in dicti2.items():
        if val > maxi:
            maxi = val
            maxi_key = key



    return maxi_key
print(most_frequent( {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}))








