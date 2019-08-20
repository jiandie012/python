import paramiko
import sys
import os
import getpass



def rcmd(host,passwd,cmd,port,name):
    ssh=paramiko.SSHClient
    
