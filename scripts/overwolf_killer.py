import psutil

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == process_name.lower():
            return True
    return False

def kill_process(process_name):
    found = False
    for proc in psutil.process_iter(['name']):
        current_process_name = proc.info['name']
        if current_process_name and current_process_name.lower() == process_name.lower():
            print("Overwolf found")
            found = True
            try:
                proc.terminate()
                print(f"Terminated {process_name} (PID: {proc.pid})")
            except psutil.NoSuchProcess:
                print(f"{process_name} process already terminated.")
            except Exception as e:
                print(f"Failed to terminate {process_name}: {e}")
            break  # Exit the loop after finding and terminating the process

    if not found:
        print(f"{process_name} not found.")


def kill_overwolf():
    # Check if "Curseforge" is running
    if not is_process_running("Curseforge"):
        print("curseforge is not running")
        kill_process("Overwolf.exe")
    else:
        print("Curseforge is running, no action needed.")
