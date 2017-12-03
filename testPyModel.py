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
        self.name = field.CharField(max_length=20, unique=True)
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
    """
        In this case, it will generate a sql:
        INSERT INTO TESTMODEL (NAME, PHONE, SEX, DATE) VALUES ( 'test', '18629508095', 'male', '2017/12/1' )
    """
    model = TestModel()
    model.name = 'test'
    model.phone = '18629508095'
    model.sex = 'male'
    model.date = '2017/12/1'

    model.save()

def test_update_table():
    """
        In the example above, we did'n specify any field that is unique
        What if we want to set NAME field is unique?
    """
    #This is to test update field's property
    model = TestModel()
    model.update_table()
    #TODO Add field to an exist table
    #TODO Delete field to an exist table

def test_get_data():
    """
        Get data by the given condition
    """
    model = TestModel()
    results = model.get_all(name='Leo', sex='Male', phone='18629508095')
    print(results)
def test_update_data():
    pass


def main():
    #test_save_data()
    test_get_data()

if __name__ == '__main__':
    main()
