import time
import os
import sys
import itertools
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hacker_face():
    face = r"""
  ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ██║ ██╔╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  █████╔╝ ███████║██║     █████╔╝ █████╗  ██████╔╝
  ██╔═██╗ ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔═══╝ 
  ██║  ██╗██║  ██║╚██████╗██║  ██╗███████╗██║     
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     
        [ 100% WORKING HACKING TOOLS v2.0 ]
    """
    print(face)

def count_animation(text="Please wait", count=10, delay=0.5):
    for i in range(1, count + 1):
        sys.stdout.write(f"\r{text}... {i}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_spinner(text="Loading modules", duration=5):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{text}... {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def fake_user_prompt():
    sys.stdout.write("\n🔐 Enter target username: ")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("admin\n")
    time.sleep(1)

    sys.stdout.write("🔑 Enter password: ")
    sys.stdout.flush()
    time.sleep(1.5)
    # Auto fill fake input "i" multiple times as password
    for _ in range(8):
        sys.stdout.write("i")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\n")
    time.sleep(1)

    print("🧪 Verifying credentials with 100% Working tools...")
    time.sleep(2)
    print("✅ Access token successfully retrieved.\n")
    time.sleep(1)

def bypass_progress():
    for i in range(0, 101, 5):
        bar = ('█' * (i // 5)).ljust(20)
        sys.stdout.write(f"\r🚨 Bypassing advanced firewall: [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(random.uniform(0.1, 0.3))
    print("\n")

def garbage_output():
    garbage = [
        "[INFO] Initializing zero-day exploit modules...",
        "[INFO] Exploit launched on target server...",
        "[+] Root access shell obtained successfully.",
        "[DEBUG] Scanning for open ports and vulnerabilities...",
        "[!] Warning: Intrusion Detection System (IDS) bypassed.",
        "[+] Extracting sensitive data archives...",
        "[DATA] Transferring 12.7MB encrypted payload...",
        "[!] Firewall rules overridden with 100% Working tools.",
        "[+] Target system compromised completely!",
    ]
    for line in garbage:
        print(line)
        time.sleep(random.uniform(0.6, 1.3))

def final_message():
    time.sleep(2)
    print("\n🎯 Mission accomplished.")
    time.sleep(1)
    print("📂 Sensitive files located: 15")
    time.sleep(1.2)
    print("🔓 Data decrypted successfully with 100% Working tools!")
    time.sleep(2)
    print("\n" + "😈" * 12)
    print("😈  YOU ARE FOOL! THIS WAS JUST A PRANK 😂  😈")
    print("😈" * 12)
    time.sleep(3)

def main():
    clear()
    hacker_face()
    time.sleep(2)
    count_animation("Please wait")
    loading_spinner("Loading hacking modules", duration=5)
    fake_user_prompt()
    bypass_progress()
    garbage_output()
    final_message()

if __name__ == "__main__":
    main()
