"""
网编用来实现不同计算机上运行程序间进行数据交互
网编三要素: IP  端口   协议

"""
import socket as s

# AF_INET是ipv4
# SOCK_STREAM是tcp
socket_obj = s.socket(s.AF_INET, s.SOCK_STREAM)
print(socket_obj)

