'''
    strip trailing 0 and replace - in a list.
'''
def repl1(list1):
    return [x.rstrip('0').replace('-','') if x is not None else None for x in list1]

print(repl1([None,'0abc','d0ef','0abc0def-sd-sds0','xyz0-','-0','0-']))
