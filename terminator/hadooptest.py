###########################################################################################
# Program to SSH using Paramiko                                                           #
# Reference Link: https://www.kite.com/python/answers/how-to-ssh-using-paramiko-in-python #
########################################################################################### 

import paramiko
import sys
import os
import getpass


def rcmd(host,passwd,cmd,port,name):
    #create a new SSHClient
    ssh=paramiko.SSHClient()
    
    # Allow the Python script to SSH to a remote server with unknown SSH keys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect the client to the server host:port with the credentials username and password
    ssh.connect(host, port, name, passwd)

    # Execute the command on the remote server and return a 3-tuple containing the stdin, stdout, and stderr from the server
    stdin, stdout, stderr = ssh.exec_command(cmd)

    # Return the output from the command
    lines = stdout.readlines()

    # Print the output
    print(lines)

if __name__ == __main__:
    host = "test.rebex.net"
    port = 22
    name = "demo"
    passwd = "password"
    cmd = "ls"

    rcmd(host,passwd,cmd,port,name)
