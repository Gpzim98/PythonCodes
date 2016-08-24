def f(args):
    print(type(args))
    for i in args:
       print i

print('>>>') 
f([1,2,2])
t = (2,3,4,4)
f(t)
l = [3,3,3]
f(l)

def f2(**args):
    print(type(args))
    for name, value in args.items():
        print name, value

f2(key1=10, key2=20)
f2(**{'g': 99, 'h':100})
