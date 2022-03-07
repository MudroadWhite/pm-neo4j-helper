# https://github.com/miloyip/json-tutorial/blob/master/

# JSON-text = ws value ws
# ws = *(%x20 / %x09 / %x0A / %x0D)
# value = null / false / true
# null  = "null"
# false = "false"
# true  = "true"

BUFFER_SIZE = 1024

class JsonType:
    NULL = 0,
    FALSE = 1,
    TRUE = 2,
    NUMBER = 4,
    STRING = 8,
    ARRAY = 16,
    OBJECT = 32

class JsonParseErrorType:
    OK = 0,
    EXPECT_VALUE = 1,
    INVALID_VALUE = 2,
    ROOT_NOT_SINGULAR = 3

class JsonContext:
    pos = 0
    json = None

    def __init__(self, json):
        self.json = json

class JsonValue:
    u = None # Union {Double; {Char; Length;}}
    def __init__(self, type):
        self.type = type
        pass
    pass

def parse(v, json):
    # assert value != Null
    c = JsonContext() # TODO
    c.json = json
    v.type = JsonType.NULL
    ## JSON text = ws value ws
    # whitespace
    c = parse_whitespace(c)
    # value
    c = parse_value(c, v)
    # whitespace
    c = parse_whitespace(c)
    # TODO: ROOT_NOT_SINGULAR if meets any other characters
    pass



    pass

def get_type(v):
    # TODO: v != None / NULL
    pass

def parse_whitespace(c):
    while (c.json(c.pos) == ' ' or  c.json(c.pos) == '\t' or c.json(c.pos) == '\n' or c.json(c.pos) == '\r'):
        c.pos += 1
    return c

def parse_null(c, v):
    # TODO: expect c[pos] == 'n'
    # TODO: array out of index
    if not (c.json[c.pos+1] == 'u' and c.json[c.pos+2] == 'l' and c.json[c.pos+3] == 'l'):
        return JsonParseErrorType.INVALID_VALUE
    c.pos += 3
    v.type = JsonType.NULL
    return JsonParseErrorType.OK

def parse_true(c, v):
    # TODO: expect c[pos] == 't'
    # TODO: array out of index
    if not (c.json[c.pos+1] == 'r' and c.json[c.pos+2] == 'u' and c.json[c.pos+3] == 'e'):
        return JsonParseErrorType.INVALID_VALUE
    c.pos += 3
    v.type = JsonType.TRUE
    return JsonParseErrorType.OK
    pass

def parse_false(c, v):
    # TODO: expect c[pos] == 'f'
    # TODO: array out of index
    if not (c.json[c.pos+1] == 'a' and c.json[c.pos+2] == 'l' and c.json[c.pos+3] == 's' and c.json[c.pos+4] == 'e'):
        return JsonParseErrorType.INVALID_VALUE
    c.pos += 3
    v.type = JsonType.FALSE
    return JsonParseErrorType.OK
    pass

def parse_value(c, v):
    j = c.json[c.pos]
    if j == 'n':
        return parse_null(c, v)
    elif j == 't':
        return parse_true(c, v)
    elif j == 'f':
        return parse_false(c, v)
    elif j == '\0':
        return JsonParseErrorType.EXPECT_VALUE
    else:
        return JsonParseErrorType.INVALID_VALUE
    pass