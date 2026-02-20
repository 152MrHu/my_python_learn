"""
服务器端客户端
1, 创建客户端socket对象
2，连接服务器端，指定服务器ip和端口号
3，接收服务器端的信息并打印
4，给服务器端发送消息

5，释放资源


"""

import  socket

# 1, 创建客户端socket对象  ipv4   tcp
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2，连接服务器端，指定服务器ip和端口号
client_socket.connect(("127.0.0.1", 10086))
# 3，接收服务器端的信息并打印
data = client_socket.recv(1024).decode("utf-8")
print(f"客户端收到: {data}")
# 4，给服务器端发送消息
client_socket.send("hello我的世界".encode("utf-8"))
#
# 5，释放资源
client_socket.close()

