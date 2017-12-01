"""
    Model object for python,
    let the SQL go away
    @author leoluo
"""
from .connectors import DB
from .utils import insert_sql
from .field import Field
from .utils import wrapper_str
from .sql import SQL
from .sql import MySQL
from .settings import db

class Model(object):
    def __init__(self, **kwargs):
        #self.connection = get_connection()
        #self.cursor = self.connection.cursor()
        self.kwargs = kwargs
        class_name = str(self.__class__)
        name = class_name.split('.')[1]
        self.table_name = name.split("'")[0].upper()
        self.ignores = ['DB', 'table_name', 'connection', 'cursor', 'ignores', 'kwargs']
        self.connection = DB.get_connection()
        self.cursor = self.connection.cursor()

    def save(self):
        result = self.__remove_field()
        sql = insert_sql(result, self.table_name)
        print(sql)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            if '1052' in str(e):
                print(True)
            self.connection.rollback()
            return
        self.connection.commit()

    def __remove_field(self):
        """
            Remove unnessary field
            @return dict
        """
        result = {}
        for key, value in self.__dict__.items():
            if key in self.ignores:
                continue
            result[key] = value

        for key, value in result.items():
            if isinstance(value, Field):
                result[key] = None
        return result

    def create_table(self):
        """Craete a table
           Named as the class' name
        """
        sql = "CREATE TABLE "
        data = ''

        for key, value in self.__dict__.items():
            if key in self.ignores:
                continue
            tmp = key.upper() + ' ' + str(value) + ', '
            data += tmp

        data = data[:-2]

        class_name = str(self.__class__)
        name = class_name.split('.')[1]
        table_name = name.split("'")[0].upper()

        sql += table_name + ' ('
        sql += data + ' )' + ""
        print(sql)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            #error_code = e[0]#1050 -> already exists
            print(e)

    def update_table(self):
        """
            Update a table named as class' name
            ALTER TABLE app_comment
            CHANGE BODY BODY TEXT CHARSET utf8 COLLATE utf8_general_ci NULL,
            change ID ID varchar(20)
        """
        sql = None
        if db.get('type').upper() == 'MYSQL':
            sql = MySQL.update_table_sql(self.table_name, self.__get_field())
        #TODO: Other database
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

    def update_data(self):
        """
            Update model's data
        """
        table = self.table_name

        sql = SQL.update_data_sql(table, data, condition)

    def __reset(self):
        #Set all attributes to None
        for key, value in self.__dict__.items():
            if key not in self.ignores:
                setattr(self, key, None)

    def __get_field(self):
        """
            This method is to get model's field
            Except from unnessary property
            @return
             dict
             {'date': <pymodel.field.CharField object at 0x000001D8CB8E6EF0>, 'sex': <pymodel.field.CharField object at 0x000001D8CB8E6EB8>, 'name': <pymodel.field.CharField object at 0x000001D8CB8E6E48>, 'phone': <pymodel.field.CharField object at 0x000001D8CB8E6E80>}
        """
        result = {}
        for key, value in self.__dict__.items():
            if key not in self.ignores:
                result[key] = value

        return result

    def get_all(self, **kwargs):
        """
            Get all results
            @return
            [model, model]
        """
        sql = None
        if not kwargs:
            sql = SQL.select_all_sql(self.table_name)
        else:
            sql = SQL.select_by_condition_sql(self.table_name, kwargs)
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.connection.close()

def main():
    model = Model()
    test = Test()
    print(test.update_data())

if __name__ == '__main__':
    main()
