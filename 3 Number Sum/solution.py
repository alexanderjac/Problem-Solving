def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array)-2):
        lptr =i+1
        rptr = len(array) -1
        while lptr<rptr:
            if array[i] + array[lptr] + array[rptr] == targetSum:
                result.append([array[i], array[lptr], array[rptr]])
                lptr+=1
                rptr-=1
            elif array[i] + array[lptr] + array[rptr] >targetSum:
                rptr -=1
            else:
                lptr +=1
    return result
    

