# https://blog.mozilla.org/webdev/2011/01/31/python-scoping-understanding-legb/
# def func1(param=None):
#     def func2():
#         if not param:
#             param = 'default'
#         print param
#     # Just return func2.
#     return func2



# UnboundLocalError: local variable 'param' referenced before assignment


# Solution
def func1(param=None):
    def func2(param2=param):
        if not param2:
            param2 = 'default'
        print param2
    # Just return func2.
    # return func2

if __name__ == '__main__':
   func1('test')