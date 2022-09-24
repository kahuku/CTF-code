import sys
import socket

def getLine(socket):
    data = socket.recv(1024).decode("utf-8")
    return data.split("\n")

def encodeResponse(response):
    response += "\n"
    return bytes(response, 'utf-8')

def main():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((sys.argv[1], int(sys.argv[2])))

    while(1):
        data = getLine(clientSocket)
        [print(line) for line in data]
        try:
            a, b = int(data[0].split(" ")[1]), int(data[0].split(" ")[2])
            answer = str(a + b)
            print(answer)
            clientSocket.send(encodeResponse(answer))
        except Exception as e:
            exit()

if __name__ == "__main__":
    main()