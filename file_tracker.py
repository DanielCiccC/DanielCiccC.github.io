import win32gui
import win32process
import win32api
import win32con
import time
import pyautogui
import datetime

def get_active_window_path():
    hwnd = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(hwnd)
    process_handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid[1])
    executable_path = win32process.GetModuleFileNameEx(process_handle, 0)
    return executable_path

# def main():
#     try:
#         while True:
#             file_path = get_active_window_path()
#             current_tab = pyautogui.getActiveWindow().title
#             click_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
#             print(f"Tab Name: {current_tab}")
#             print(f"Click Time: {click_time}")
#             print(f"File Path: {file_path}")
#             print("-" * 30)

#             time.sleep(1)  # Wait for 1 second

#     except KeyboardInterrupt:
#         print("Script terminated.")

def factors(n):             # generator that computes factors
    for k in range(1,n+1):
        if n % k == 0:      # divides evenly, thus k is a factor
            yield k         # yield this factor as next result

if __name__ == "__main__":
    print(factors(60))