import snowflake.connector
import config as cf
entity=cf.entity
conn = snowflake.connector.connect(
                user=cf.USER,
                password=cf.PASSWORD,
                account=cf.ACCOUNT,
                )
#methods to execute the query and return the result
def execute_query(query):
    conn.cursor().execute(query)
def return_result(query):
    cd=conn.cursor().execute(query)
    return cd
#verify connection
def verify_connection():
    try:
        query="select current_version()"
        conn.cursor().execute(query)
        res="Connection Established"
        return res
    except Exception as e:
        error="connection is not established"
        return error  # this is send to hayagreev
#main_code:
def mandatory_codes():
    query="use role {role}".format(role=cf.ROLE)
    execute_query(query)
    query="use warehouse {warehouse}".format(warehouse=cf.WAREHOUSE)
    execute_query(query)
def get_databases():
    query="select DATABASE_NAME from sample_data.information_schema.databases where DATABASE_NAME!='SAMPLE_DATA'"
    res=return_result(query) 
    return res
def get_schema(db_name):
    query="select distinct TABLE_SCHEMA from {db}.INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA !='INFORMATION_SCHEMA' and  COLUMN_NAME like '%{entity}%'".format(db=db_name,entity=entity.upper())
    res=return_result(query)
    return res
def get_tables(db_name,schema_name):
    query="select distinct TABLE_NAME from {db}.INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA !='INFORMATION_SCHEMA' and TABLE_SCHEMA ='{schema}' and COLUMN_NAME like '%{entity}%'".format(db=db_name,schema=schema_name,entity=entity.upper()) 
    res=return_result(query) 
    return res
def get_columns(db_name,schema_name,table_name):
    query="select COLUMN_NAME from {db}.INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA !='INFORMATION_SCHEMA' and TABLE_SCHEMA ='{schema}' and TABLE_NAME='{table}' and COLUMN_NAME like '%{entity}%'".format(db=db_name,schema=schema_name,table=table_name,entity=entity.upper()) 
    res=return_result(query)
    return res

