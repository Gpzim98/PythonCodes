print "1 == 1?",
assert 1 == 1
print "sim."

try:
    print "2 == 1?",
    assert 2 == 1, "2 != 1"
except AssertionError, ex:
    print str(ex)
