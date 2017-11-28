class Field():
    def __init__(self):
        pass

class CharField(Field):
    def __init__(self, max_length=10, unique=False, required=False):
        self.max_length = max_length
        self.unique = unique
        self.required = required

    def __str__(self):
        base = 'VARCHAR' + '(' + str(self.max_length) + ')'
        if self.required:
            base += ' NOT NULL '
        if self.unique:
            base += ' PRIMARY KEY'

        return base

class IntegerField(Field):
    def __init__(self, default=0, required=False):
        self.default = default
        self.required = required

    def __str__(self):
        base = 'INT'
        if self.required:
            base += ' NOT NULL '
        base += ' DEFAULT ' + str(self.default)

        return base

class FloatField(Field):
    def __init__(self, default=0.0, required=False):
        self.default = default
        self.required = required

    def __str__(self):
        base = 'FLOAT'
        if self.required:
            base += ' NOT NULL '
        base += ' DEFAULT ' + str(self.default)

        return base

class BooleanField(Field):
    def __init__(self, default=False):
        self.default = default

class TextField(Field):
    def __init__(self):
        pass

    def __str__(self):
        return 'TEXT'

def main():
    print(b'\xe2\x9c\x85\xe2\x9c\x85\xf0\x9f\x8c\xb9'.decode())
    print('爱的太快'.encode())
    print('✅✅🌹爱的太快'.encode('utf8').decode('utf8'))
if __name__ ==  '__main__':
    main()
