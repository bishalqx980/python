import pyautogui
import time

def scan_and_lock(image_path, lock_confirm_img="assets/lock_confirm.png", confidence=0.8):
    print("Scaning screen...")
    while True:
        try:
            agent_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if agent_location:
                print("Agent location found...")
                pyautogui.click(agent_location)
            
            time.sleep(1)
            
            try:
                lock_confirm_location = pyautogui.locateCenterOnScreen(lock_confirm_img, confidence=confidence)
                if lock_confirm_location:
                    print("LOCK IN button found...")
                    pyautogui.click(lock_confirm_location)
            except pyautogui.ImageNotFoundException:
                pass
            except Exception as e:
                print(e)
                break

            print(f"Agent has been selected successfully...")
            break
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as e:
            print(e)
            break

        time.sleep(1)


if __name__ == "__main__":
    image_location = f"agents/killjoy.png"
    scan_and_lock(image_location)
