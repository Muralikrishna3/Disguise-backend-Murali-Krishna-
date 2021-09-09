import structure as st
import parameters as p
import masking as ms
#global variables
masking_policy=p.masking_policy
#Verify Connection
res=st.verify_connection()
print(res)
#mandatory_codes like use warehouse etc, before getting databases,schema....
st.mandatory_codes()
#filter_name function
def filter_name(name):
    valid=""
    for j in name:
        if j!='(' and j!=')' and j!="'" and j!=",":
            valid=valid+j
    return valid
#main_code
databases=st.get_databases()
for i in databases:
    i=filter_name(i)
    schema=st.get_schema(i)
    for j in schema:
        j=filter_name(j)
        tables=st.get_tables(i,j)
        for k in tables:
            k=filter_name(k)
            columns=st.get_columns(i,j,k)
            for p in columns:
                p=filter_name(p)
                query="alter table if exists {db}.{schema}.{table} modify column {column} set masking policy {masking_policy}".format(db=i,schema=j,table=k,column=p,masking_policy=masking_policy)
                st.execute_query(query)
                
print("successfully masked")