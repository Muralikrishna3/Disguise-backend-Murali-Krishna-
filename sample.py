import snowflake.connector
import config as cf
import pandas as pd
entity='email'
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

def mandatory_codes():
    query="use role {role}".format(role=cf.ROLE)
    execute_query(query)
    query="use warehouse {warehouse}".format(warehouse=cf.WAREHOUSE)
    execute_query(query)
    #query="use database disguise_DB"
    #execute_query(query)
    #query="use schema DISGUISE_DEV"
    #execute_query(query)
mandatory_codes()
def get_schema(db_name):
    query="select  TABLE_SCHEMA from {db}.INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA !='INFORMATION_SCHEMA' and  COLUMN_NAME like '%{entity}%'".format(db=db_name,entity=entity.upper())
    res=return_result(query)
    
    for i in res:
        valid=""
        for j in i:
            if j!='(' and j!=')' and j!="'" and j!=",":
                valid=valid+j
        #sentence="jfidfijf e {i}".format(i=i)
        print(valid)
db_name='DISGUISE_DB'
get_schema(db_name)