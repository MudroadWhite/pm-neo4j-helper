BUFFER_SIZE = 1024

class JsonType:
    BEGIN_OBJECT = 1
    END_OBJECT = 2
    BEGIN_ARRAY = 4
    END_ARRAY = 8
    NULL = 16
    NUMBER = 32
    STRING = 64
    BOOLEAN = 128
    SEP_COLON = 256
    SEP_COMMA = 512
    END_DOCUMENT = 1024


class JsonToken:
    def __init__(self, tt, v):
        self.tokenType = tt
        self.value = v

# Python reader class???
class CharReader:
    def __init__(self, reader):
        self.reader = reader
        self.buffer_size = BUFFER_SIZE
        self.pos = 0

    def peak(self):
        pass

    def next(self):
        pass

    def back(self):
        pass

    def hasMore(self):
        pass

    def fillBuffer(self):
        pass