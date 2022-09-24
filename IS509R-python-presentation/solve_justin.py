from pwn import *
p = remote('drewwilson.guru', 40001)

while True:
    line = p.recvline().decode()
    print(line)
    try: num1 = int(line.split(" ")[-2])
    except: p.interactive()
    num2 = int(line.split(" ")[-1].strip())
    p.sendline(str(num1+num2).encode())
