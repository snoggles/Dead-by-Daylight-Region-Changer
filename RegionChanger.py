# ---------------------------------------------
# Dead by Daylight Region Changer
# Developed by DAMERTON
# Maintained by snoggles
# GitHub: https://github.com/Bloodpoint-Farming/Dead-by-Daylight-Region-Changer
# ---------------------------------------------
import os
import ctypes
import re
import time
import sys
import platform

# Detect OS and set hosts_path accordingly
if platform.system() == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    hosts_path = "/etc/hosts"

regions = {
    "0": ("Set Default", None),
    "1": ("N. Virginia", "us-east-1"),
    "2": ("Ohio", "us-east-2"),
    "3": ("N. California", "us-west-1"),
    "4": ("Oregon", "us-west-2"),
    "5": ("Frankfurt", "eu-central-1"),
    "6": ("Ireland", "eu-west-1"),
    "7": ("London", "eu-west-2"),
    "8": ("South America (São Paulo)", "sa-east-1"),
    "9": ("Asia Pacific (Mumbai)", "ap-south-1"),
    "10": ("Asia Pacific (Seoul)", "ap-northeast-2"),
    "11": ("Asia Pacific (Singapore)", "ap-southeast-1"),
    "12": ("Asia Pacific (Sydney)", "ap-southeast-2"),
    "13": ("Asia Pacific (Tokyo)", "ap-northeast-1"),
    "14": ("Asia Pacific (Hong Kong)", "ap-east-1"),
    "15": ("Canada", "ca-central-1"),
}
all_region_ids = [region[1] for key, region in regions.items() if key not in ["0"]]


def ensure_admin():
    if platform.system() == "Windows":
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit(0)
    else:
        if os.geteuid() != 0:
            print("This script requires root privileges. Re-running with sudo...")
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

def append_hosts_entries(choice):
    with open(hosts_path, 'a') as hosts_file:
        hosts_file.write("\n")

        for id, region in regions.items():
            if id == "0":
                continue

            comment_prefix = "#" if id == choice else " "
            domain = f"gamelift-ping.{region[1]}.api.aws"
            line_to_add = f"{comment_prefix} 0.0.0.0 {domain}\n"
            hosts_file.write(line_to_add)

def remove_all_overrides():
    ensure_hosts_file_exists()

    with open(hosts_path, 'r') as hosts_file:
        lines = hosts_file.readlines()

    def is_gamelift_line(line):
        # This the traditional pattern used < 8.4.0
        pattern1 = r".*\sgamelift\.[^.]+\.amazonaws\.com$"
        # The .api.aws hostnames were added briefly in 8.4.0, then reverted.
        # Starting in 8.5.2, the .api.aws seem to be turned on and off intermittently.
        pattern2 = r".*\sgamelift-ping\.[^.]+\.api\.aws$"
        return re.match(pattern1, line) or re.match(pattern2, line)

    # Filter out lines containing domains to remove
    filtered_lines = [
        line for line in lines if not is_gamelift_line(line)
    ]

    # Remove any trailing blank lines
    while filtered_lines and filtered_lines[-1].strip() == "":
        filtered_lines.pop()

    # Ensure exactly one blank line at the end
    if filtered_lines and filtered_lines[-1].strip() != "":
        filtered_lines.append("\n")

    with open(hosts_path, 'w') as hosts_file:
        hosts_file.writelines(filtered_lines)


def get_current_region():
    ensure_hosts_file_exists()

    with open(hosts_path, 'r') as hosts_file:
        content = hosts_file.read()

    # Remove commented out entries
    content = "\n".join([line for line in content.splitlines() if not re.match(r"^\s*#\s*", line)])

    unblocked_region_ids = [region_id for region_id in all_region_ids if region_id not in content]

    if len(unblocked_region_ids) == len(all_region_ids):
        return "Default (Not region locked)"
    else:
        return ", ".join([get_region_name(region_id) for region_id in unblocked_region_ids])

def get_region_name(region_id):
    for region_name, domain in regions.values():
        if domain == region_id:
            return region_name
    return "Unknown Region"


def get_user_region_choice():
    print("GitHub: https://github.com/snoggles/Dead-by-Daylight-Region-Changer")
    print("-------------------------------------------------------------------")
    print("\nWelcome to the Bloodpoint Farming Region Changer!")
    print("Please select a region from the following options:\n")

    for key, (region_name, region_id) in regions.items():
        print(f"{key}. {region_name} ({region_id})")

    current_region = get_current_region()
    print("\n---------------------------------------------------------")
    print(f"Current region: {current_region}")
    print("---------------------------------------------------------")

    while True:
        choice = input("\nEnter the number of your chosen option: ")
        if choice in regions:
            return choice
        else:
            print("Invalid choice. Please try again.")


def clear_console():
    """Clear the console screen on Windows or Linux."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def ensure_hosts_file_exists():
    """Create the hosts file (and parent dir if needed) when it doesn't exist.

    This prevents opens in 'r' mode from failing on a fresh system.
    """
    directory = os.path.dirname(hosts_path)
    if directory and not os.path.isdir(directory):
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception:
            # If we can't create the directory, let the later file open raise.
            pass

    if not os.path.exists(hosts_path):
        # Open in write mode to create an empty file.
        try:
            with open(hosts_path, 'w'):
                pass
        except Exception:
            # If creation fails (permissions, etc.), let the caller handle it.
            pass


if __name__ == "__main__":
    ensure_admin()

    while True:
        choice = get_user_region_choice()
        
        print("\nClearing old overrides...")
        remove_all_overrides()
            
        if choice != "0":  # ignore Default option
            print(f"\nSelected region: {regions[choice][0]}")
            append_hosts_entries(choice)

        print(f"\nDone!")
        time.sleep(1)  # Wait for 1 second before the next iteration
        clear_console()
