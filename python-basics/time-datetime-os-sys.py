import time, datetime, os, sys

# time

start = time.perf_counter()
print('time')
print(time.ctime())
print(time.localtime(), '\n')

# datetime

print('datetime')
print(datetime.datetime.today().strftime('%Y %m %d | %H %M %S'))
epoch_start = datetime.datetime(1970, 1, 1)
time_ = datetime.timedelta(seconds=2**31)
the_end = epoch_start + time_
print('This is the end:', the_end, '\n')

# os
print('os')
print(os.name)
print(os.getlogin())
print(os.getcwd())
print(os.getpid(), '\n')
# os. mkdir, remove, rename, rmdir, chmod

# sys
print('sys')
print(sys.platform)
print(sys.executable)
print(sys.getsizeof('hello-world.py'))
print(sys.getsizeof('imports.py'))
print(sys.version)


print('Elapsed time: ', time.perf_counter() - start, 'seconds')