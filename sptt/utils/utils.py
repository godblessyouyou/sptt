import telnetlib
import paramiko

class WindowsConnect(object):

    def __init__(self, host, timeout=30):
        # Host type is dict
        self.ip = host['ip']
        self.username = host['username']
        self.password = host['password']
        self.connect = telnetlib.Telnet(host['ip'], port=23, timeout=timeout)
        self.connect.set_debuglevel(2)
        self.connect.read_until('login: ')
        self.connect.write(host['username'] + '\n')
        self.connect.read_until('password: ')
        self.connect.write(host['password'] + '\n')
        self.connect.read


    def exe_command(self, commands):
        # commands type is dict
        for command in commands:
            self.connect.writ
        

