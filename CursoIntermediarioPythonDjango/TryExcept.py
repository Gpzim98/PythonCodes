__author__ = 'gpzim98'
try:
    1/0
    print 'No errors found'
except Exception, e:
    if str(e) == 'integer division or modulo by zero':
        print 'ocorreu um erro: ', str(e)
