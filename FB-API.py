import requests
import json
import jieba
import operator
import pandas as pd

# wd = pd.DataFrame([[]])
# wd.append({},ignore_index=True)
# print(wd)

token = "EABKk1WPoWjsBAJalwXBuG7z5XoxSmIhWNKgNKYbJP2bQQ7W8QaYPwVw3fP7aLiNL3Dxrj2p6krgkZC521eVJbaACX6srcR19TduKC5cSEJ9TGtpBsIQIZCGOmGhyUZA9rdK29sM5UCtN8BlYyYoizMqfym8GPXvwe0fZCyIRh6XinDAW1uGI3kKZCjGZC13cl70F4NEBcDRd9Ig144moW4BMFJhmUH6lhR0BJRmhQQ5FdMnKwR1zZCH"
res = requests.get("https://graph.facebook.com/v13.0/me/posts?access_token=" + token)
jd = json.loads(res.text)
word = []

while "paging" in jd:
    for post in jd["data"]:
        if "message" in post:
            word += jieba.cut(post["message"])
    res = requests.get(jd["paging"]["next"])
    jd = json.loads(res.text)

dic_w = {}
for ele in word:
    if ele not in dic_w:
        dic_w[ele] = 1
    else:
        dic_w[ele] +=1

sort_w = sorted(dic_w.items(),key=operator.itemgetter(1),reverse=True)
no_word = [".",",","!","~","。"," ","(",")","[","]","/","6996669999999969999999966699666666699"]
dic_sort = {}

for ele in sort_w:
    dic_sort[ele[0]]=ele[1]
for w in no_word:
    for x in dic_sort:
        if w in x :
            dic_sort[x]=0

print(dic_sort)

# for w in no_word:
#     for ele in sort_w:
#         if w in ele[0]:
#             dic_sort[ele[0]] = 0
#         else:
#             for x in no_word:
#                 if x not in ele[0]:
#                     dic_sort[ele[0]] = sort_w[1]


# for ele in dic_sort:
#     if len(ele[0])>= 3 or ele[1]>8:
#         print(ele[0],ele[1])




wd = pd.DataFrame([[None,None]])
wd.columns=["word","count"]
nd = wd
for ele in dic_sort:
    if len(ele)>=3:
        nd = nd.append({"word":ele,"count":dic_sort[ele]},ignore_index=True)

print(nd)



dic_w={"word":[],"count":[]}
for ele in word:
    if ele not in dic_w["word"]:
        dic_w["word"].append(ele)
        dic_w["count"].append(1)
    else:
        dic_w["count"][dic_w["word"].index(ele)]+=1

print(dic_w)