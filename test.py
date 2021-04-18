'''
Given a list of strings that contain numerical values i.e. ["12345", "012-345", "123-45", "012345", "123450", "", None,"-01234"]

Create a function that cleans all the strings by removing the leading 0's and any "-" characters.Given a list of strings that contain numerical values i.e. ["12345", "012-345", "123-45", "012345", "123450", "", None]

Create a function that cleans all the strings by removing the leading 0's and any "-" characters.
'''

def cleanlist(iplist):

    return [x.replace('-','').lstrip('0') if x is not None else None for x in iplist]

print(cleanlist(["12345", "012-345", "123-45", "012345", "123450", "", None,"-01234"]))