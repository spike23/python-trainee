import paramiko

host = "10.1.192.100"
port = 22
transport = paramiko.Transport((host, port))

password = "pass"               
username = "user"                
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)


destination = '/home/folder/airflow/1.txt' 
source = r'C:\Users\admin\Downloads\1.txt' 
sftp.put(source, destination)

sftp.close()
transport.close()
print ('Upload done.')
