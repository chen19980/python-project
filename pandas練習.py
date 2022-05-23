import pandas as pd

# phone = pd.Series(["amy","bob"]) #index=
# car =pd.Series(["a","b"])
# phone[1] = "CHEN"
# com = phone.append(car,ignore_index=True) #忽略原始索引值
# print(phone) 
# print("------------")
# print(phone.str.upper())
# print("------------")
# print(phone.str.lower())
# print("------------")
# print(phone.str.cat(sep=":"))
# print("------------")
# print(phone.str.contains("o"))
# print("------------")
# print(phone.str.replace("amy","CHEN"))

# data = {
#     "name":["bob","chen","amy"],
#     "sex":["M","M","F"],
#     "grade":["B","A","c"],
# }

# x = pd.DataFrame(data)

# y = pd.DataFrame({
#     "name":["john","elen"],
#     "sex":["F","M"],
#     "grade":[56,90]
# })


# x.insert(2,column="age",value=[22,24,25])
# x.index=["a","b","c"]
# y.columns= ["name","grade"]

# print(x[["name","sex"]])
# print(x[:2])
# x.iat[1,0] = "Leo"
# print(x)
# print(x[:1])
# print(y)


#排版專用
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)


# newdata = x.drop(["sex"],axis = 1)

# newdata = pd.concat([x,y],ignore_index=True)
# print(newdata)

# data = {
#     "name":["bob","chen","amy"],
#     "sex":[None,"M","F"],
#     "grade":["B",None,"c"],
# }

# data = pd.DataFrame(data)
# print(data.dropna())

# data = {
#     "name":["bob","bob","amy"],
#     "sex":["M","M","F"],
#     "grade":["B","B","c"],
# }

# data = pd.DataFrame(data)
# data = data.drop_duplicates()
# print(data)



data = {
    "name":["bob","bob","amy"],
    "sex":["M","M","F"],
    "grade":[80,70,60],
}

data = pd.DataFrame(data)
data.index=[2,3,4]
data = data.sort_values(["grade"],ascending=0)
print(data)

# print(data[data["name"].isin(["bob"])])

# print(data["grade"]>70)
# print(data[data["grade"]>65])


