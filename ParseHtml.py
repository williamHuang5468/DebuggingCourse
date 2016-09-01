def parseHtml(string):
    '''
    >>> parseHtml("<a>hello</a>")
    "hello
    '''
    TagState = False
    result = ""
    for s in string:
        if s is ">":
            TagState = True
            continue
        elif s is "<":
            TagState = False

        if TagState:
            result += s
    return result

if __name__ == '__main__':
    result = parseHtml("<a>html</a>")
    print(result)
