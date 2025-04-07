thislist = [100, 50, 65, 82, 23]

my_list2 = [a-50 for a in thislist]
"""
-infinity                               +infinity
<-----------------0---------------------->
.. -5 -4 -3 -2 -1 0 1 2 3 4 5 6 ...

abs(-5) = 5
abs(5)  = 5

abs(-2) = 2
abs(2)  = 2

-5 <? +3 True
|-5| <? |+3| = False
5 > 3 
"""

print(my_list2)

def myfunc(n):
  return abs(n - 50)
"""
myfunc(23) ->  27

"""

thislist.sort(key = myfunc)
print(thislist)