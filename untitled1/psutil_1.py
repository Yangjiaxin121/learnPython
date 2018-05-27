import psutil

#获取CPU信息
print(psutil.cpu_count()) #CPU路基数量
print(psutil.cpu_count(logical=False)) #CPU物理核心

print(psutil.cpu_times())

#for x in range(10):
#   print(psutil.cpu_percent(interval=1,percpu=True))


#获取内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

#获取磁盘信息
print(psutil.disk_partitions()) #磁盘分区信息
print(psutil.disk_usage('/'))      #磁盘使用情况
print(psutil.disk_io_counters())     #磁盘IO