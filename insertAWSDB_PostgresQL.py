import insertUtil as ut
import psycopg2


#Tạo kết nối với RDS PostgreSQL và thêm dữ liệu vào
conn = psycopg2.connect(database='covid_postgres', user='postgres', password='20092001', host='database-postgre.c8nxb47naeqa.us-east-1.rds.amazonaws.com', port='5432')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')
