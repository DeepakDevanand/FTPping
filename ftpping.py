#!/usr/bin/env python3

'''
#################################################################################################################################################################################
# <<<<<<<<<< FTP service door-knocking on hosts in the network >>>>>>>>>>
#
# @file: ftpping.py
# @input: network address block (eg. 192.168.10.0/24), or a comma-separated list of IP addresses (eg. 192.168.10.23,192.168.10.24 [no space around comma delimiter, for now!!])
#         defaults to ftp-user "Anonymous" if none specified.
# @output: ftp service reply status with rtt (round trip time)
#
#################################################################################################################################################################################
'''



import ftplib 
from argparse import ArgumentParser
from contextlib import closing
from datetime import datetime
from collections import namedtuple
from sys import exc_info
from ipaddress import ip_network


def parse_input():
    ''' Sets the optional arguments for script input, and returns the parsed argument list
        Anonymous option for login is a flag.
    '''

    parser = ArgumentParser()
    parser.add_argument("-t","--host", help="IP address or netblock. No DNS name support yet.")
    parser.add_argument("-a","--anonymous", action="store_true", help="Use anonymous login")
    parser.add_argument("-u","--user", help="Username for ftp login")
    parser.add_argument("-p","--passwd", help="Password for ftp login")
    #parser.add_argument("-o", "--output", help="File to log the output")

    args = parser.parse_args()
    return args



def ftp_connect(HOST, USER, PASSWD):
    ''' Takes IP address, ftp-user and ftp-password as input, initiates ftp session on the IP address, and returns the response status from the target.
        Also in the response round trip time, and error status, if any.  
    '''

    response = namedtuple('response', 'host status latency')
    response.host = HOST 

    try:
        with closing(ftplib.FTP(HOST)) as ftp:

            t1 = datetime.now()
            try:
                response.status = ftp.login(user=USER, passwd=PASSWD)

            except ftplib.all_errors as e:
                response.status = e

            t2 = datetime.now()
            response.latency = (t2-t1)

    except ConnectionRefusedError as e:
        response.status = e

    except OSError as e:
        response.status = "No route to host"

    except:
        response.status = exc_info()[0]


    return response




if __name__ == "__main__":
    ''' Begins execution by parsing the user-supplied input, initiating the ftp session and printing the response status.
    '''

    args = parse_input()
    

    # List of hosts to ftp-connect to
    hosts = []
    if args.host:
        if ('/' in args.host): 
            host_arg = ip_network(args.host)
            hosts = [ str(ip) for ip in list(host_arg.hosts()) ]

        elif (',' in args.host):
            hosts = [ ip for ip in args.host.split(',') ]
        
        else:
            hosts.append(args.host)


    # Default anonymous ftp login if no credentials given
    args.user = 'Anonymous' if (args.anonymous or args.user == None) else args.user
    args.passwd = 'Anonymous' if (args.passwd == None) else args.passwd


    # FTP login on hosts in the list
    for host in hosts:
        response = ftp_connect(host, args.user, args.passwd)

        if response.status == "230 Login successful.":
            print("Reply from {}: ftp-user={} rtt={}".format(host, args.user, response.latency))

        else:
            print("No response from {}: ftp-user={} error={}".format(host, args.user, response.status))
