import psutil

def print_cpu_utilization():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Utilization: {cpu_percent}%")

def print_disk_usage():
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage:")
    print(f"  Total: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"  Used: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"  Free: {disk_usage.free / (1024 ** 3):.2f} GB")
    print(f"  Percentage Used: {disk_usage.percent}%")

if __name__ == "__main__":
    print_cpu_utilization()
    print_disk_usage()
  
#this is a test github 