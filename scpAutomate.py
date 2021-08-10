from paramiko import SSHClient
from scp import SCPClient


serverIP = ['255.255.255.255']

serverPass = {
    '255.255.255.255': 'zero',
    # '': '',
    # '': '',
    # '': '',
    # '': '',
    # '': '',
    # '': ''
}


def connectHost(host):
    usrname = 'zero'
    passwd = serverPass[host]
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=host, 
                # port = 'port',
                username=usrname,
                password=passwd)
                # pkey='load_key_if_relevant')
    # SCPCLient takes a paramiko transport as its only argument
    scp = SCPClient(ssh.get_transport())
    scp.put('file.txt', recursive=True, remote_path='~/Desktop')
    scp.close()


def loop():
    for _ in serverIP:
        connectHost(_)


loop()