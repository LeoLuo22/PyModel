from pymodel import model
from pymodel import field

"""
    Create a model
"""
class TestModel(model.Model):
    def __init__(self):
        """
            This is where you define your model.
            You should enherited from super class Model.
            Once you finished, use create_table() to save your model.
        """
        super(TestModel, self).__init__()
        self.name = field.CharField(max_length=20)
        self.phone = field.CharField(max_length=20)
        self.sex = field.CharField(max_length=6)
        self.date = field.CharField(max_length=50)

def test_create_table():
    """
        Create a table in database
        In this case, it will generate:
        CREATE TABLE TESTMODEL (DATE VARCHAR(50), PHONE VARCHAR(20), NAME VARCHAR(20), SEX VARCHAR(6) )
    """
    model = TestModel()
    model.create_table()

def test_save_data():
    pass

def test_update_table():
    pass

def test_update_data():
    pass


def main():
    test_create_table()

if __name__ == '__main__':
    main()
