def hanoi(n,f,h,t):  #n is the number of disks. fht are the names used from, helper, to
    print("{}n = {}, f = {}, h = {}, t = {}".format(" "*(4-n),n,f,h,t))
    if n==0:
        return
    else:
        hanoi(n-1,f,t,h)
        print("{} Move disk from {} to {}".format(" "*(4-n),f,t))
        hanoi(n-1,h,f,t)