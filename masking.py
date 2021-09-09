import config as cf
import structure as st

def predefined_policies():
    query="create or replace masking policy new_policy as (val string) returns string -> case when current_role() in ('{role}') then val else 'MASKED' end".format(role=cf.ROLE)
    st.execute_query(query)     
#masking
#Assuming there are 3 lists(string_list,zipcode_list,number_list)
#--------------string_list------------------------
def string_masking():
    try:
        for i in cf.columns:
            query="alter table if exists {db}.{schema}.{table} modify column {column} set masking policy new_policy".format(db=cf.database.upper(),schema=cf.schema.upper(),table=cf.table.upper(),column=i)
            st.execute_query(query)
        res="Successfully Masked"
        return res
    except Exception as e:
        error="Not Masked"
        return error