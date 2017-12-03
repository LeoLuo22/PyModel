try:
    from .utils import wrapper_str
except SystemError:
    from utils import wrapper_str

class Field():
    def __init__(self, pk=False, required=False, default=None):
        self.pk = pk#Primary key
        self.required = required#Whether could be null
        self.default = default#default value

class CharField(Field):
    def __init__(self, max_length=10, pk=False, required=False, default=None):
        super(CharField, self).__init__(pk, required, default)
        self.max_length = max_length

    def __str__(self):
        base = 'VARCHAR' + '(' + str(self.max_length) + ')'
        if self.required:
            base += ' NOT NULL'
        if self.pk:
            base += ' PRIMARY KEY'
        if self.default:
            base += ' DEFAULT ' + wrapper_str(self.default)

        return base

class IntegerField(Field):
    def __init__(self, pk=False, required=False, default=None):
        super(IntegerField, self).__init__(pk, required, default)

    def __str__(self):
        base = 'INT'
        if self.required:
            base += ' NOT NULL'
        if self.default:
            base += ' DEFAULT ' + str(self.default)

        return base

class FloatField(Field):
    def __init__(self, pk=False, required=False, default=None):
        super(FloatField, self).__init__(pk, required, default)

    def __str__(self):
        base = 'FLOAT'
        if self.required:
            base += ' NOT NULL '
        if self.default:
            base += ' DEFAULT ' + str(self.default)

        return base

class BooleanField(Field):
    def __init__(self, pk=False, required=False, default=None):
        super(BooleanField, self).__init__(pk, required, default)

class TextField(Field):
    def __init__(self, pk=False, required=False, default=None):
        super(TextField, self).__init__(pk, required, default)

    def __str__(self):
        return 'TEXT'


def test_charfield():
    name = CharField(max_length=20, default='Leo', pk=True, required=True)
    print(str(name))

def test_integerfield():
    number = IntegerField(required=True, default=1)
    print(str(number))

def main():
    test_charfield()
    test_integerfield()

if __name__ ==  '__main__':
    main()
