#import nc
import nclib

nc = nclib.Netcat(('2048.challs.olicyber.it', 10007))

print (nc.recv())
stringa = nc.recv()
print (stringa.decode())
splitta = stringa.decode().trim().split(" ")
print("\n"+splitta[0])