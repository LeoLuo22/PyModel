def wrapper_str(value):
    """Use for SQL
        @value str
        @return 'str'
    """
    if not isinstance(value, str):
        raise ValueError("value must be str")
    return "'" + value + "'"

def insert_sql(obj, table):
    """Generate sql if object's field is not None
        @param obj, an object
        @param table, str, table's name
        IN: test = Test()
            test.a = 1
            test.b = 'hello'
            test.c = None
        OUT: INSERT INTO info (B, A) VALUES ( 2, '1' )
    """
    base = 'INSERT INTO ' + table + ' '
    keys = []#保存Value不为None的key
    values = []
    data = obj
    if not isinstance(data, dict):
        data = obj.__dict__
    for key, value in data.items():
        if value:
            keys.append(key)
            values.append(value)

    fields = ''
    for key in keys:
        fields += key.upper() + ', '
    fields = fields[:-2]

    base = base + '(' + fields + ')' + ' VALUES '
    field_values = ''
    for value in values:
        if isinstance(value, str):
            field_values += wrapper_str(value) + ', '
        else:
            field_values += str(value) + ', '
    field_values = field_values[:-2]

    sql = base + '( ' + field_values + ' )'

    return sql

def get_primary_key_sql(table_name):
    """
        Get primary key of a table
        @return sql:
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME <> 'dtproperties' AND table_name = 'app_comment'
    """
    sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME <> 'dtproperties' AND table_name = '{0}'".format(table_name)

    return sql

class Test():
    pass

def main():
    print(get_primary_key_sql('app_comment'))

if __name__ == '__main__':
    main()
