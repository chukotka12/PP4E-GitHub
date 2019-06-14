# аргументы, потоки
import  sys, os
print(os.getcwd())  # in Outputs
print(sys.path[0])

print('[argv]')
for arg in sys.argv:    # from Args
    print(arg)          # in Outputs

print('[interaction]')  # to Outputs
text = input('Enter text:') # from Inputs
rept = sys.stdin.readline() # from Input
sys.stdout.write(text*int(rept)) #to Outputs
