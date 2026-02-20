"""
服务器端客户端
1, 创建服务器端socket对象
2，绑定ip和端口号
3，设置监听数
4，等待客户端申请建立连接
5，给客户端发送消息
6，接收客户端的信息并打印
7，释放资源


"""
# 服务器端
import socket
# 1, 创建服务器端socket对象  ipv4   字节流
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2，绑定ip和端口号
server_socket.bind(("127.0.0.1", 10086))
# 3，设置监听数
server_socket.listen(5)
while True:
    try:
        # 4，等待客户端申请建立连接

        accept_socket, client_address = server_socket.accept()

        # 5，给客户端发送消息
        accept_socket.send(b'welcom To Socket') #有中文不行

        # 6，接收客户端的信息并打印
        data =  accept_socket.recv(1024).decode("utf-8")
        print(f"服务器端收到来自{client_address}的信息：", data)

        # 7，释放资源
        accept_socket.close()
    except:
        pass

# 设置端口号重用  目的：快速重启服务器，服务器关闭后立即释放端口
#  参1：  当前的套接字对象，   参2：  选项名        ，  参3：设置值
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

