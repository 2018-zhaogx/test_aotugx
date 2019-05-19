#！/usr/bin/python
#-*- coding:utf-8 -*-
while True:
    import socket
    #创建套接字
    sock=socket.socket()
    #注：：客户端不需要绑定ip，直接建立连接
    #服务器的ip和端口号
    sock.connect(('192.168.1.6',80))
    #发送请求
    msg=input('>>>')
    #msg='你吃饭了吗？'
    sock.send(msg.encode('utf-8'))
    #接收
    reg=sock.recv(1024)
    print(reg.decode('utf-8'))
    #sock.close()
    if msg=='close':
        sock.close()
        break




import socket
while True:
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #使用udp不需要建立连接
    host= ('192.168.1.6',8806)
    msg=input('close关闭，>>>')
    #msg='你吃饭了吗？'
    s.sendto(msg.encode('utf-8'),host)
    reg=s.recv(1024)
    print(reg.decode('utf-8'))
    s.close()
    if msg=='close':
       s.close()
       break