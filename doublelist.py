n = [3, 5, 7]

def double_list(a):
    for i in range(0, len(a)):
        a[i] = a[i] * 2
    return (a)
# Don't forget to return your new list!

print (double_list(n))