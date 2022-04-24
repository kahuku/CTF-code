import sys
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((sys.argv[1], int(sys.argv[2])))

def getFirstInput(socket):
    data = socket.recv(1024).decode("utf-8")
    data = ''.join(data)
    data = data.split("!")[1].strip()
    return data

def getInput(socket):
    data = socket.recv(1024).decode("utf-8")
    data = ''.join(data)
    data = data.split("!")[1].strip()
    return data

def encodeResponse(response):
    response += "\n"
    return bytes(response, 'utf-8')

def getAnswer(num1, op, num2):
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "*":
        answer = num1 * num2
    elif op == "//":
        answer = num1 // num2
    return str(answer)

def main():
    data = getFirstInput(clientSocket)

    maths = data.split()
    num1, op, num2 = int(maths[0]), maths[1], int(maths[2])
    
    response = getAnswer(num1, op, num2)
    print("0:", response)

    clientSocket.send(encodeResponse(response))

    for i in range(1, 1000):
        data = getInput(clientSocket)
        try:
            maths = data.split()
            print(maths)
            num1, op, num2 = int(maths[0]), maths[1], int(maths[2])
            
            response = getAnswer(num1, op, num2)
            print(str(i) + ":", response)

            clientSocket.send(encodeResponse(response))
        except Exception as e:
            print(e)
            print(data)
            break

    data = clientSocket.recv(1024).decode("utf-8")
    print(data)

if __name__ == "__main__":
    main()
