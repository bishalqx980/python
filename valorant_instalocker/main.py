import time
import json
import pyautogui

JSON_DATA = "data.json"

def log(message):
    print(f"» {message}")

def scan_and_lock(agent_image, agent_name, lockin_image, duration=0.5, confidence=0.8):
    log(f"Scaning screen for agent: {agent_name}")
    while True:
        try:
            agent_location = pyautogui.locateCenterOnScreen(agent_image, confidence=confidence)
            if agent_location:
                pyautogui.click(agent_location, duration=duration)
                log(f"Agent: {agent_name} found.")
                break
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as e:
            log(e)
            break

    time.sleep(1)

    log(f"Locking agent: {agent_name}")
    while True:
        try:
            lock_confirm_location = pyautogui.locateCenterOnScreen(lockin_image, confidence=confidence)
            if lock_confirm_location:
                pyautogui.click(lock_confirm_location, duration=duration)
                log(f"Agent: {agent_name} has been locked in.")
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as e:
            log(e)
            break

        log(f"Valorant Instalock execution done...")
        
        break


def main():
    msg = """
    𝓐 𝓹𝓻𝓸𝓳𝓮𝓬𝓽 𝓸𝓯

    ▄▄▄▄    ██▓  ██████  ██░ ██  ▄▄▄       ██▓    
    ▓█████▄ ▓██▒▒██    ▒ ▓██░ ██▒▒████▄    ▓██▒    
    ▒██▒ ▄██▒██▒░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒██░    
    ▒██░█▀  ░██░  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██░    
    ░▓█  ▀█▓░██░▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██████▒
    ░▒▓███▀▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░
    ▒░▒   ░  ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░
    ░    ░  ▒ ░░  ░  ░   ░  ░░ ░  ░   ▒     ░ ░   
    ░       ░        ░   ░  ░  ░      ░  ░    ░  ░
        ░                                        
                            Valorant instalocker
    """
    print(msg)
    with open(JSON_DATA, "r") as f:
        data = json.load(f)
    
    agents = data.get("agents")
    counter = 0
    agent_names = []
    for agent_name in agents:
        print(f"{counter}. {agent_name}")
        agent_names.append(agent_name)
        counter += 1
    
    while True:
        try:
            user_input = input("\nAgent number » ")
            if user_input == "q":
                break

            if int(user_input) in range(0, counter):
                selected_agent_name = agent_names[int(user_input)]
                image_path = f"{data.get('image_directory')}{selected_agent_name}.png"
                # Calling function
                scan_and_lock(image_path, selected_agent_name, data.get("lockin_image"))
            else:
                print("Wrong input!")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    



if __name__ == "__main__":
    main()
