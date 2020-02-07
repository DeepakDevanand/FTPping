#### 1. FTP

- FTP: [wikipedia](http://bit.ly/31zaJXM)

  - 20/tcp--ftp-data, 21/tcp--ftp-control
  - stateful session, separate channel for data transfer

- Modes

  - Active -- Client opens a port to which server connects back (Issues with NAT and Firewalls)
  - Passive -- Client connects to the server from a non-privileged port

- Methods of file transfer

  - Binary -- Data as a stream of bytes (preferred)
  - ASCII -- Data as ascii characters (limited only to text format)


#### 2. Coding

- ftplib: [doc](http://bit.ly/378Csje), [python ftp | zetcode](http://bit.ly/3816Mxq)

  - Instantiate FTP object with server IP address, and call the methods on it.

  - ```python 
        # typical
        ftp = ftplib.FTP(host="192.168.13.140", user="ftper", passwd="p@s$")
        ftp.pwd()
        ftp.dir()
        ftp.cwd("/dir")
    ```

  - ```python 
        # download
        with open("local.txt", "wb") as fp:
            ftp.retrbinary("RETR remote.txt", fp.write)

        # upload
        with open("local.txt", "rb") as fp:
            ftp.storbinary("STOR remote.txt", fp)
    ```

  - Context manager is possible "with"

- namedtuple: [dBader](http://bit.ly/2SqeB9h)

  - ```python
    from collections import namedtuple

    myTuple = ("myTuple", "field1 field2 field3")
    myTuple.field1 = value1
    myTuple.field2 = value2

    myTuple._fields
    ```

- ipaddress: [doc](http://bit.ly/2UsbArC)

  - ```python
    import ipaddress

    add = ipaddress.ip_address("192.168.1.10")
    net = ipaddress.ip_network("192.168.1.0/24")

    hosts = [ str(ip) for ip in list(net.hosts())]
    ```

