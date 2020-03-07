import AppClass
import time

machine = AppClass.AppClass()
f = open('genSTR.txt', 'r')
res = open('resSMC.txt', 'w')
start_time = time.perf_counter()
for line in f.readlines():
    match = machine.CheckString(line)
    if match:
        res.write(line + '\n')
f.close()
print('Res time: ' + str(time.perf_counter() - start_time))
