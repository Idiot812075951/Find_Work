import random,math

arr = [64, 34, 25, 12, 22, 11, 90]

def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]: #表示，如果j大于0并arr[j]不是最小值，那么j指针就会前移
            arr[j + 1] = arr[j] #这一步是把其余元素后移，腾出位置
            j -= 1
        arr[j + 1] = key #这一步是插入
def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:  # 递归的退出条件
        return ##注意，这里如果返回arr，那么会是none，因为没有值了，指针指向空
    mid = alist[start]  # 设定起始的基准元素
    low = start  # low为序列左边在开始位置的由左向右移动的游标
    high = end  # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[low] = mid  # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后
def Selectionsort(list1):
    for i in range(len(list1)):

        min_idx = i
        for j in range(i + 1, len(list1)):
            if list1[min_idx] > list1[j]:
                min_idx = j

        list1[i], list1[min_idx] = list1[min_idx], list1[i]

def heapify(arr, n, i): #用来调整小顶堆的函数，n的值确定了二叉树的样子，二叉树是唯一的
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r

    if largest !=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heapSort(arr):
    n=len(arr)

    for i in range(n,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))
def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0));
    return result

def bucket_sort_simplify(arr, max_num):  #  a=bucket_sort_simplify(arr,max(arr)),print(a)
    """
    简化版
    """
    buf = {i: [] for i in range(int(max_num)+1)}  # 不能使用[[]]*(max+1)，这样新建的空间中各个[]是共享内存的
    arr_len = len(arr)
    for i in range(arr_len):
        num = arr[i]
        buf[int(num)].append(num)  # 将相应范围内的数据加入到[]中
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(sorted(buf[i]))  # 这里还需要对一个范围内的数据进行排序，然后再进行输出
    return arr
def countingSort(arr, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr
def shell_sort(alist):
    #这里的step相当于是，gap，增量，分成几个堆
    step = len(alist) // 2 #相当于是int(len(alist)/2)
    while step > 0:
        for i in range(step, len(alist)):
            # 在索引为step到len（L）上，比较L[i]和L[i-step]的大小
            while i >= step and alist[i] < alist[i - step]:
                # 这里可以调整step从小到大或者从大到小排列
                alist[i], alist[i - step] = alist[i - step], alist[i]
                i -= step
        step //= 2

########################################################################################################################
#上面对应的是1~9编号的排序算法，下面是自己默写的函数
########################################################################################################################
def zc_bubblesort(list1):
    n=len(list1)
    for i in range(n):
        for j in range(n-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]

    return list1
def zc_insertionSort(list1):
    n=len(list1)

    for i in range(n):
        key=list1[i]
        j=i-1

        while j>=0 and list1[j]>key:
            list1[j+1]=list1[j]  #后移，腾位置
            j -=1
        list1[j+1]=key  #插入



def zc_QuickSort(list1,start,end):
    mid = list1[start]
    if start>=end:
        return

    low=start
    high=end

    while low<high:
        while low<high and list1[high]>mid:
            high -=1
        list1[low]=list1[high]

        while low<high and list1[low]<mid:
            low +=1
        list1[high]=list1[low]

    list1[low]=mid
    zc_QuickSort(list1,start,low-1)
    zc_QuickSort(list1,low+1,end)


def quick(list1,start,end):
    if start>end:
        return

    mid=list1[start]
    low=start
    high=end

    while low<high:
        while low<high and list1[high]>=mid:
            high -=1
        list1[low]=list1[high]

        while low<high and list1[low]<=mid:
            low +=1
        list1[high]=list1[low]

    list1[low]=mid
    quick(list1,start,low-1)
    quick(list1,low+1,end)




def zc_Selectionsort(list1):
    n=len(list1)

    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if list1[j]<list1[min_idx]:
                min_idx=j
        list1[min_idx],list1[i]=list1[i],list1[min_idx]





def select(list1):
    n=len(list1)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if list1[j]<list1[min_idx]:
                min_idx=j
        list1[i],list1[min_idx]=list1[min_idx],list1[i]


# def heapify(arr, n, i): #用来调整小顶堆的函数，n的值确定了二叉树的样子，二叉树是唯一的
#     largest = i
#     l = 2 * i + 1  # left = 2*i + 1  这里代表i的左节点
#     r = 2 * i + 2  # right = 2*i + 2  代表i的右节点
#
#
#     #比如，长度为7的列表
#     #那么节点索引应该是，
#     #     (1)
#     #  （3  , 4）
#     #（7,8)  （9,10）
#
#
#     #2i+1<n    2i<n-1   i<(n-1)/2   (n-1)/2这玩意儿代表父节点
#     if l < n and arr[i] < arr[l]:
#         largest = l
#
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # 交换
#
#         heapify(arr, n, largest)
# def heapSort(arr):
#     n = len(arr)
#
#     # Build a maxheap.
#     for i in range(n, -1, -1):  #如果是range(8,-1,-1)结果是76543210，注意，区间是(8,-1),所以包括0
#         heapify(arr, n, i)  #执行函数heapify(arr, n, i)，n不变，i一直逆序，如heapify(arr, 8, 7)，heapify(arr, 8, 6)，heapify(arr, 8, 5)……heapify(arr, 8, 0)
#
#         # 一个个交换元素
#     for i in range(n - 1, 0, -1):  #如果是range(8,0,-1)结果是7654321，注意，这里到1就截止了
#         arr[i], arr[0] = arr[0], arr[i]  # i只能取到1，不能为0，就是交换位置
#         heapify(arr, i, 0)


# n=8
#for i in range(n,-1,-1):
#    print(i)
# for i in range(n-1,-1,-1):
#     print(i)






def zc_merageSort(arr):
    if len(arr)<2:
        return arr
    middle=math.floor(len(arr)/2)
    left=arr[middle:]
    right=arr[:middle]

    return zc_merge(zc_merageSort(left),zc_merageSort(right))


def zc_merge(left,right):
    reslult=[]

    while left and right:
        if left[0]<=right[0]:
            reslult.append(left.pop(0))
        else:
            reslult.append(right.pop(0))

    while left:
        reslult.append(left.pop(0))
    while right:
        reslult.append(right.pop(0))

    return  reslult



def zc_bucket_sort_simplify(arr, max_num):  #  a=bucket_sort_simplify(arr,max(arr)),print(a)
    """
    简化版
    """
    buf = {i: [] for i in range(int(max_num)+1)}  # 不能使用[[]]*(max+1)，这样新建的空间中各个[]是共享内存的
    arr_len = len(arr)
    for i in range(arr_len):
        num = arr[i]
        buf[int(num)].append(num)  # 将相应范围内的数据加入到[]中
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(sorted(buf[i]))  # 这里还需要对一个范围内的数据进行排序，然后再进行输出
    return arr


def zc_countingSort(arr, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr


def zc_shell_sort(alist):
    #这里的step相当于是，gap，增量，分成几个堆
    step = len(alist) // 2 #相当于是int(len(alist)/2)
    while step > 0:
        for i in range(step, len(alist)):
            # 在索引为step到len（L）上，比较L[i]和L[i-step]的大小
            while i >= step and alist[i] < alist[i - step]:
                # 这里可以调整step从小到大或者从大到小排列
                alist[i], alist[i - step] = alist[i - step], alist[i]
                i -= step
        step //= 2







n = len(arr)
print("排序后")


a=bucket_sort_simplify(arr,max(arr))
print(a)

