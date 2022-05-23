import numpy as np
# np1 = np.array([1,2,3])
# np2 = np.array([4,5,6,7])

# print(np2.ndim) #維度
# print(np2.shape) #型態 幾筆資料

# np3 = np.zeros([1,2])
# np4 = np.ones([2,2])
# print(np3)


# np1 = np.linspace(2,10,5) ＃(起始,終點,間距)
# np2 = np.arange(1,6)      # (按照順序排出來)
# print(np1)
# print(np2)


#抓取位置
# np1 = np.array([[1,2,3,4,5],[4,6,9,5,6]])
# print(np1[[1,1],[3,2]])  #（np1[[列,列],[欄,欄]]）


#加減乘除
# np1 = np.array([1,2,3,])
# np2 = np.array([2,4,6])
# print(np1-np2)


#dot點積 列*欄 2*3,3*2 = 2*2
# np1 = np.array([[1,2,3],[2,4,1]])
# np2 = np.array([[1,1],[2,2],[3,3]])
#[1,2,3]*[1,2,3] [2,4,1]*[1,2,3]
# print(np1.dot(np2))


#inner內積  2*3,1*3 = 2*1
# np1 = np.array([[1,2,3],[2,3,4]])
# np2 = np.array([[1,2,1]])
# print(np.inner(np1,np2))


#outer外積 1*3,2*2 = 3*4
# np1 = np.array([1,2,3])
# np2 = np.array([[2,2],[1,1]])
# print(np.outer(np1,np2))


# np1 = np.array([1,2,3,4])
# np2 = np.array([5,6,7,8])
# print(np.append(np1,5))       #加入5
# print(np.append(np1,np2))     #加入np2
# print(np.insert(np1,2,6))     #在np1中的第2個位置加入6
# print(np.delete(np1,[3]))     #刪除np1中第三個位置的值


# np1 = np.array([[1,2],[3,4]])
# np2 = np.array([[5,6],[7,8]])
# print(np.vstack((np1,np2))) #垂直合併
# print(np.hstack((np1,np2))) #水平合併
# print(np.vsplit(np1,2))     #垂直切割
# print(np.hsplit(np1,2))     #水平切割

