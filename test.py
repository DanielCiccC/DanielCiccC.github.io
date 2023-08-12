import pyautogui
import datetime
import time

def main():
    try:
        while True:
            x, y = pyautogui.position()
            current_tab = pyautogui.getActiveWindow().title
            click_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print(f"Tab Name: {current_tab}")
            print(f"Click Time: {click_time}")
            print("-" * 30)

            time.sleep(1)  # Adjust the interval as needed
    except KeyboardInterrupt:
        print("Script terminated.")

if __name__ == "__main__":
    main()