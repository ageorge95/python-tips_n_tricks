from subprocess import Popen,\
    CREATE_NEW_CONSOLE,\
    STARTUPINFO,\
    STARTF_USESHOWWINDOW

info = STARTUPINFO()
info.dwFlags = STARTF_USESHOWWINDOW
info.wShowWindow = 6 # 0-HIDDEN, 6-MINIMSED

cmd = 'calc & echo Command executed & pause'
Popen(f"cmd /c {cmd}",
      creationflags=CREATE_NEW_CONSOLE,
      startupinfo=info).wait()