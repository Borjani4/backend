def binary_search(lst,search_item):
    low = 0
    higt = len(lst)-1
    search_res = False

    while low <= higt  and not search_res:
        middle=(low+higt)//2
        guess=-lst[middle]
        if guess==search_item:
            search_res=True
            return search_res
        if guess>search_item:
            higt=middle-1
        else:
            low=middle+1
        return search_res


lst=[3,5,11,12,15,23,34,67,86]
value=34
result=binary_search(lst,value)
if result:
    print('элемент найден!')
else:
    print("Элемент не найден!")



