import insertUtil as ut
import MySQLdb


#Tạo kết nối với RDS Aurora MySQL và thêm dữ liệu vào
conn = MySQLdb.connect(host='database-aurora.cluster-cqxpkgslhnca.us-east-1.rds.amazonaws.com', user='admin', passwd='20092001', db='covid_aurora', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')
