def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2) # 5/2 = 2 # Python 3 2.0
div1(5.,2) # 5.0/2 = 2.5 # Python 3 2.5 
div2(5,2)  # 5//2 = 2 # Python 3  2
div2(5.,2.) # 5.0//2.0 = 2.0s # Python 3 2.0