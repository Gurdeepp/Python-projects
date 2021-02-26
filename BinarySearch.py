pos = -1


def search(lst, src):
    l = 0
    u = len(lst) - 1
    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == src:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < src:
                l = mid + 1
            else:
                u = mid - 1
    return False


lst = []
n = int(input("Enter the no. of elements"))
for i in range(n):
    e = int(input("Enter the elements one by one"))
    lst.append(e)

print("Your elements are", lst)
src = int(input("What do you want to search for?"))
if search(lst, src):
    print("found at", pos + 1)
else:
    print("Not Found")
