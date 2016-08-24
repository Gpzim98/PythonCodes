def readfile(filename, bytes):
    try:
        f = file(filename)
    except IOError:
        return ""

    try:
        return f.read(bytes)
    except IOError:
        return ""
    finally:
        f.close()
 
print "Nao existe:", readfile("no.txt", 5)
print "Existe:", readfile("yes.txt", 5)

class NotFound(Exception): pass
class InvalidKey(Exception): pass
    
def find(collection, elem):
    try:
        return collection[elem]
    except (KeyError, IndexError), ex:
        raise NotFound("%s not found (%s)." % (elem, ex))
    except TypeError, ex:
        raise InvalidKey("%s is invalid (%s)." % (elem, ex))

a, b = [0], {}

try:
    find(a, 1) # IndexError
except Exception, ex:
    print "Exception: %s" % (ex,)

try:
    find(b, 'spam') # KeyError
except Exception, ex:
    print "Exception: %s" % (ex,)

try:
    find(a, "spam") # TypeError
except Exception, ex:
    print "Exception: %s" % (ex,)

try:
    find(b, 0) # No error
except Exception, ex:
    print "Exception: %s" % (ex,)
else:
    print "Element found."

try:
    find(a, "spam") # TypeError again
except Exception, ex:
    raise # re-raise exception


