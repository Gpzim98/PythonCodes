import sys

s1, s2 = "String1", "String2"
obj = object()
f = open("/tmp/out.txt", "w")

print s1     # String1\n
print s1, s2 # String1 String2
print s1,    # String1 
print s2     # String2
print obj    # <object .. 0xXX>
print >>f, s1, s2 # >out.txt
print >>sys.stderr, "ERRO!"
f.close()
