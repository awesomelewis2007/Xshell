#! bin/python39
#Xshell GNU public licence
import os
import sys
import time
BOOT_START = time.time()
class Boot:
    def Fatal_cant_boot(errorno = "Unknown error no",reason = "No reason was given",log = "No log file was found",fix = "No fixes available"):
        print("[X] Fatal Xshell cant boot due to an error in the system")
        print("--------------------------------------------------------")
        print("Error Number:",errorno)
        print("Reason:",reason)
        print("Log:")
        print("--------------------------------------------------------")
        print(log)
        print("--------------------------------------------------------")
        print("Fixes:",fix)
        exit()
    def check_filesystem():
        import os
        from os import path
        import sys
        paths = ["system","system/system64","system/system64/syscore"]
        log = "INFO: Executing sys checkdisk\n"
        for i in paths:
            log = log + "INFO: Checking path '"+i+"\n"
            x = os.path.exists(i)
            if x == True:
                pass
                log = log + "INFO: The path '"+i+"' was found and continuing to next path\n"
                log = log + "\n"
            if x == False:
                log = log + "ERROR: Path not found '"+i+"\n"
                log = log + "Xshell Will Not contine to boot"+"\n"
                log = log + "Printing error message and quitting"
                a = "CHECK DISK: The system cant find the path '"+i+"'"
                Boot.Fatal_cant_boot(errorno="404",reason=a,log=log,fix="Reinstall Xshell or relocate the missing path or file")

    def path_add():
        import sys
        import os
        paths = ["system/temp","system"]
        for p in paths:
            sys.path.append(p)
        cwd = os.getcwd()
        sys.path.append(cwd)
    def check_modules():
        try:
            import js2py
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module js2py",log="none",fix="try to install the module using pip")
        try:
            import platform
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module platform",log="none",fix="try to install the module using pip")  
        try:
            from colr import color
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module colr",log="none",fix="try to install the module using pip") 
        try:
            import requests
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module requests",log="none",fix="try to install the module using pip") 
        try:
            import socket
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module socket",log="none",fix="try to install the module using pip") 
        try:
            import logging
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module logging",log="none",fix="try to install the module using pip")  
        try:
            import psutil
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module psutil",log="none",fix="try to install the module using pip")  
                
Boot.check_modules()  
import logging
logging.basicConfig(format='[%(asctime)s]  [%(filename)s:%(lineno)d] [ %(levelname)s ]  %(message)s',datefmt='%d-%m-%Y:%H:%M:%S',level=logging.DEBUG,filename='system/temp/logs/System_log.log')
global log
log = logging.getLogger()
log.info("==============================BOOT==============================")


#=====================MAIN======================
from system.system64.syscore import REGISTRY
from system.system64.syscore.usr import Login
import js2py
log.info(msg="Imported module:js2py")
import datetime
log.info(msg="Imported module:datetime")
import platform
log.info(msg="Imported module:platform")
from colr import color
log.info(msg="Imported module:color")
import requests
log.info(msg="Imported module:requests")
import socket
log.info(msg="Imported module:socket")

Login.Welcome.message()

global LOG_STATE
log.info(msg="Reading registory log state")
REG_LOG_STATE = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/OS_LOGGING_STATE/REG_LOGGING.data")
x = platform.system()
log.info("SYSTEM OS:    "+str(x))
x = platform.version()
log.info("SYSTEM VER:   "+str(x))
x = platform.processor()
log.info("CPU:          "+str(x))
x = platform.python_build()
log.info("PYTHON BUILD: "+str(x))
if REG_LOG_STATE == "1":
    from system.system64.syscore import REGISTRY
    x = platform.system()
    x = x.upper()
    REGISTRY.write("system/REGISTRY/LOCAL_MACHINE/LOCAL_OS/OS.data",x)
    REGISTRY.write("system/temp/OS",x)
    x = platform.version()
    REGISTRY.write("system/REGISTRY/LOCAL_MACHINE/LOCAL_NAME/NAME.data",x)
    REGISTRY.write("system/temp/OS_NAME",x)
if REG_LOG_STATE == "0":
    pass
Boot.path_add()
Boot.check_filesystem()

BOOT_END = time.time()
log.info("CODE: 100")
boot_time = BOOT_END - BOOT_START
round(boot_time, 3)
print(color("Boot Time: ", fore="blue")+str(boot_time)+"Ms")
print("")
#====History=====
Xshell_running = True
try:
    history_file_read = open("system/temp/history","r")
    history_file_read_x = history_file_read.read()
    log.info(msg="Successfully read history")
except:
    log.warn(msg="Can't find history file, Creating one")
    history_file_read = open("system/temp/history","w")
    log.info(msg="Created File")
    history_file_read.close()
    history_file_read = open("system/temp/history","r")
    history_file_read_x = history_file_read.read()
    log.info(msg="Successfully read history")
#====Welcome====


if REG_LOG_STATE == "0":
    print(color("Xshell has started in no REG logging mode",fore="yellow"))
    log.debug("Running in No Reg logging")
if REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/HISTORY/HISTORY_ON.data") == "0":
    log.info("History is off")
    print(color("History is off use 'history -on' to enable it again",fore="yellow"))
from system.system64 import lang
print(lang.get_welcome_message())
#====SYSTEM IMPORT====
from system.system64 import command
from system.system64.syscore import history

#====SYS LOOP====
while Xshell_running == True:
    cwd = os.getcwd()
    xshell_text = "Xshell@"+socket.gethostname()
    print(color('┌──[', fore='blue')+color(xshell_text, fore='green')+color(']──[', fore='blue')+cwd+color(']', fore='blue'))
    try:
        user_input = input(color('└─>', fore='blue'))
    except KeyboardInterrupt:
        log.info("^c was pressed sending warning")
        print(color('\n[!] Keyboard interrupt press ctrl+c again to exit', fore="yellow"))
        print(color('┌──[', fore='blue')+color(xshell_text, fore='green')+color(']──[', fore='blue')+cwd+color(']', fore='blue'))
        try:
            user_input = input(color('└─>', fore='blue'))
        except KeyboardInterrupt:
            print("\n")
            log.info("^c was pressed closing Xshell")
            log.info("Killing System")
            exit()
    lg = "Running Command:"+user_input
    log.info(msg=lg)
    del lg
    if "exit" in user_input:
        trim_user_input = user_input[:4]
        if trim_user_input == "exit":
            log.info("Killing System")
            exit()
    if "quit" in user_input:
        trim_user_input = user_input[:4]
        if trim_user_input == "quit":
            log.info("Killing System")
            exit()
    command.run(user_input)
    try:
        if REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/HISTORY/HISTORY_ON.data") == "1":
            history.write(user_input)
            
    except:
        log.error("Something is going wrong in the history Xshell Can't Write")