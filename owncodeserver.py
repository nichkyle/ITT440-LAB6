import socket
import sys
import time
import errno
import math         #for calculation
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("\t\t\tWelcome to My First Python Calculator \n\n\t\t\t\t HOW TO USE:\n\n\t\t First step(Write the operation): log/sqrt/exp \n\n\t\t Second Step(Put the number): <number>\n\n\t\t Example: log 10\n\n\t\t\t***Type 'quit' to close***"))
    while True:
        data = s_sock.recv(2048)                        #input that server received from client
        data = data.decode("utf-8")

        #calculation part
        try:
            operation, value = data.split()
            op = str(operation)
            num = int(value)
        
            if op[0] == 'l':
                op = 'Log'
                answer = math.log10(num)
            elif op[0] == 's':
                op = 'Square root'
                answer = math.sqrt(num)
            elif op[0] == 'e':
                op = 'Exponential'
                answer = math.exp(num)
            else:
                answer = ('SYNTAX ERROR')
        
            sendAnswer = (str(op) + '(' + str(num) + ') = ' + str(answer))
            print ('Congratulations, Calculation successful!')
        except:
            print ('Invalid input')
            sendAnswer = ('Invalid input')
    
        #s_sock.send(str.encode(sendAnswer))
        
        if not data:
            break
            
        s_sock.send(str.encode(sendAnswer))
        #s_sock.sendall(str.encode(ok_message))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("\n\t\t=====listening...from...client=====")
    s.listen(22)                                         

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

            except Exception as e:        
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
