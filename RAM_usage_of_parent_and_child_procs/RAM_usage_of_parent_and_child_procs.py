# NOTE: This works for 1 level deep: parent -> child

from psutil import process_iter, \
    Process

id = None

for proc in process_iter():
    try:
        # go through all the running processes to find our process
        cmdline = proc.cmdline()
        print(f"Detected running process: {cmdline}")

        # EXAMPLE: search for the chrome.exe daemon
        if len(cmdline) == 1 and cmdline[0].endswith('chrome.exe'):
            id = proc.pid
            break

    except:
        id = None

if id:
    current_process = Process(id)
    print(f"Parent process ID {id}, using {current_process.memory_info().vms / 1024 ** 2} MB")

    children = current_process.children(recursive=True)
    for child in children:
        print(f"Child pid is {child.pid}, using {child.memory_info().vms / 1024 ** 2} MB")

else:
    print('Could not find your process !')