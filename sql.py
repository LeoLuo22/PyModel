"""
    This file supplies different of SQL
"""
#from .utils import wrapper_str

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

def main():
    print((1062, "Duplicate entry '1939223019' for key 'PRIMARY'")[0])

if __name__ == '__main__':
    main()
