def abc(x):
    # print('#', end=' ')
    if x==2:
        # print('#', end=' ')
        return
    # print('#', end=' ')
    for i in range(2):
        # print('#', end=' ')
        abc(x+1)
        # print('#', end=' ')
    #print('#', end=' ')

abc(0)