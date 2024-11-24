        
import time

def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            print(f"\rLoading... {char}", end="")
            time.sleep(0.1)  # Adjust the delay as needed
    print("\nLoading complete!\n")