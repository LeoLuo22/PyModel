"""
    This file supplies different of SQL
"""
from .utils import wrapper_str

class SQL():
    def __init__(self):
        pass

    @staticmethod
    def update_data_sql(table, data, condition):
        """
            Generate a SQL used for update data of a table
            @param table, str
            @param data, dict, data want to be updated
            @param condition, dict
            IN: update_data('app_comment', {'title': 'ss'}, {'ID': '1212'})
            OUT: UPDATE app_comment SET B = '1', C = 2, A = 'a' WHERE ID = '1212'
        """
        if not isinstance(table, str):
            raise ValueError("table must be str")
        if not isinstance(data, dict):
            raise ValueError('data must be dict')
        if not isinstance(condition, dict):
            raise ValueError('condition must be dict')

        data_sql = ""

        sql = "UPDATE " + table + " SET "
        tmp = ""
        for key, value in data.items():
            if isinstance(value, str):
                tmp = key.upper() + " = " + wrapper_str(value) + ", "
            else:
                tmp = key.upper() + " = " + str(value) + ", "
            data_sql += tmp
        data_sql = data_sql[:-2]

        condition_sql = " WHERE "
        for key, value in condition.items():
            if isinstance(value, str):
                tmp = key.upper() + " = " + wrapper_str(value) + ' AND '
            else:
                tmp = key.upper() + " = " + str(value) + ' AND '
            condition_sql += tmp
        condition_sql = condition_sql[:-5]
        sql = sql + data_sql + condition_sql

        return sql

    @staticmethod
    def select_all_sql(table_name):
        """
            Get all models
        """
        sql = "SELECT * FROM " + table_name
        return sql

    @staticmethod
    def select_by_condition_sql(table_name, kwargs):
        sql = "SELECT * FROM " + table_name + " " + "WHERE "
        for key, value in kwargs.items():
            if value == 'null':
                tmp = key.upper() + " is " + value + " AND "
            else:
                tmp = key.upper() + " = " + wrapper_str(value) + " AND "
            sql += tmp

        return sql[:-5]

class MySQL():
    def __init__(self):
        pass

    @staticmethod
    def update_table_sql(table_name, kwargs):
        """
            Generate a sql to update an exist table
            @param kwargs
             dict, {'BODY': 'Text', 'ID': 'VARCHAR(20)'}

            ALTER TABLE app_comment
            CHANGE BODY BODY TEXT CHARSET utf8 COLLATE utf8_general_ci NULL,
            change ID ID varchar(20)
            @return
             ALTER TABLE test CHANGE ID ID VARCHAR(20), CHANGE BODY BODY TEXT
        """
        sql = "ALTER TABLE " + table_name + " "

        for key,value in kwargs.items():
            if not isinstance(value, str):
                value = str(value)
            tmp = "CHANGE " + key.upper() + " " + key.upper() + " " + value.upper() + ", "
            sql += tmp

        return sql[:-2]

    @staticmethod
    def add_column_sql(table_name, kwargs):
        """
            ALTER TABLE `boc`.`testmodel`
            ADD COLUMN `shit` VARCHAR(45) NULL AFTER `fuck`,
            ADD COLUMN `sda` VARCHAR(45) NULL AFTER `shit`;

            Add column to an exist table
        """
        sql = "ALTER TABLE " + table_name + " "
        for key, value in kwargs.items():
            tmp = "ADD COLUMN " + key + " " + value.upper() + ", "
            sql += tmp

        return sql[:-2]

    @staticmethod
    def update_data_sql(table_name, kwargs, condition):
        #UPDATE `boc`.`app_comment` SET `VERSION`='3.1.2', `KEYWORDS`='hahah' WHERE `ID`='1000030498';
        if len(kwargs) == 0 or kwargs is None:
            #TODO log
            return
        sql = "UPDATE " + table_name + " SET "
        for key, value in kwargs.items():
            if isinstance(value, str):
                value = wrapper_str(value)
            else:
                value = str(value)
            tmp = key + " = " + value + ", "
            sql += tmp

        sql = sql[:-2]
        cond = " WHERE "
        for key, value in condition.items():
            if isinstance(value, str):
                value = wrapper_str(value)
            else:
                value = str(value)
            tmp = key + " = " + value + " AND "
            cond += tmp

        return sql + cond[:-5]


def main():
    #print((1062, "Duplicate entry '1939223019' for key 'PRIMARY'")[0])
    print(MySQL.update_table_sql('test', {'BODY': 'Text', 'id': 'VARCHAR(20)'}))

if __name__ == '__main__':
    main()
