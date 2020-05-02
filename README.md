# FTPping

Ping hosts in the network running FTP service


### What?

Ping-esque program with FTP as connection method to discover FTP servers in the network. An `nmap -p 20,21 <target>` kin, but with a very basic functionality.


### Why?

Primarily, for understanding (and to later abusing) the FTP protocol and its implementations (such as vsftpd).


### Installation

```
$ git clone https://github.com/DeepakDevanand/FTPping.git
$ cd FTPping/

$ chmod +x ftpping.py

$ ./ftpping.py --help
usage: ftpping.py [-h] [-t HOST] [-a] [-u USER] [-p PASSWD]

optional arguments:
  -h, --help            show this help message and exit
  -t HOST, --host HOST  IP address or netblock. No DNS name support yet.
  -a, --anonymous       Use anonymous login
  -u USER, --user USER  Username for ftp login
  -p PASSWD, --passwd PASSWD
                        Password for ftp login
```

### Usage

```
$ ftpping.py -t 192.168.13.0/24 --anonymous
Reply from 192.168.13.2: ftp-user=ftper rtt=0:00:04.113046
No response from 192.168.13.3: ftp-user=Anonymous error=No route to host
Reply from 192.168.13.140: ftp-user=ftper rtt=0:00:03.845046
No response from 192.168.13.3: ftp-user=Anonymous error=530 Permission denied.
```

```
$ ftpping.py --host 192.168.13.140 --user ftper --pass p@$s
Reply from 192.168.13.140: ftp-user=ftper rtt=0:00:04.101212
```

```
$ ftpping.py --host 192.168.13.140,192.168.13.2 --user ftper --pass p@$s
Reply from 192.168.13.140: ftp-user=ftper rtt=0:00:04.101212
Reply from 192.168.13.140: ftp-user=ftper rtt=0:00:04.234331
```

### To-do

- [ ] FTPS, SSL/TLS support during connection attempts
- [ ] Performant pinging in a large IP address space (multi-threading)
- [ ] DNS name support for target specification
- [ ] Option to generate a custom log report
- [ ] Option to read from a file having usernames and passwords
