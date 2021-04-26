import paramiko


host = 'HOST'
user = "LOGIN"
password = 'PASSWORD'
key = "SSH_KEY"


def ssh_connect(command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password, key_filename=key)
        stdin, stdout, stderr = client.exec_command(str(command))
        data = stdout.read() + stderr.read()
        client.close()
        return data.decode("utf-8")
    except:
        client.close()
        return ("No connection to server")
