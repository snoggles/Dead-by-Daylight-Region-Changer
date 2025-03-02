# ---------------------------------------------
# Dead by Daylight Region Changer
# Developed by DAMERTON
# Maintained by snoggles
# GitHub: https://github.com/snoggles/Dead-by-Daylight-Region-Changer
# ---------------------------------------------
import os
import ctypes
import re
import time
import sys

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
regions = {
    "0": ("Set Default", None),
    "1": ("N. Virginia", "us-east-1"),
    "2": ("Ohio", "us-east-2"),
    "3": ("N. California", "us-west-1"),
    "4": ("Oregon", "us-west-2"),
    "5": ("Frankfurt", "eu-central-1"),
    "6": ("Ireland", "eu-west-1"),
    "7": ("London", "eu-west-2"),
    "8": ("South America", "sa-east-1"),
    "9": ("Asia Pacific (Mumbai)", "ap-south-1"),
    "10": ("Asia Pacific (Seoul)", "ap-northeast-2"),
    "11": ("Asia Pacific (Singapore)", "ap-southeast-1"),
    "12": ("Asia Pacific (Sydney)", "ap-southeast-2"),
    "13": ("Asia Pacific (Tokyo)", "ap-northeast-1"),
    "14": ("Asia Pacific (Hong Kong)", "ap-east-1"),
    "15": ("Canada", "ca-central-1"),
}
all_domains = [region[1] for key, region in regions.items() if key not in ["0"]]


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def add_to_hosts(ip, domains):
    with open(hosts_path, 'r') as hosts_file:
        lines = hosts_file.readlines()

    with open(hosts_path, 'a') as hosts_file:
        for domain in domains:
            line_to_add = f"{ip} {domain}"
            if line_to_add not in lines:
                # Ensure a blank line before adding the new block, if needed
                if lines and not lines[-1].endswith("\n"):
                    hosts_file.write("\n")  # Add a blank line if the last line is not empty
                hosts_file.write(line_to_add + "\n")
                # print(f"Added '{line_to_add}' to the hosts file.")

    # Ensure exactly one blank line at the end of the file
    with open(hosts_path, 'r') as hosts_file:
        lines = hosts_file.readlines()

    with open(hosts_path, 'w') as hosts_file:
        hosts_file.writelines([line.rstrip() + "\n" for line in lines])
        if not lines[-1].strip():  # Check if last line is blank
            hosts_file.write("\n")  # Add a blank line if the last line is blank


def remove_all_overrides():
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

    print("\nCleanup completed: Removed domains from the hosts file.")


def get_current_region():
    with open(hosts_path, 'r') as hosts_file:
        content = hosts_file.read()

    blocked_domains = [domain for _, domain in regions.values() if domain]
    unblocked_domains = [domain for domain in blocked_domains if domain not in content]

    if len(unblocked_domains) == 1:
        for key, (region_name, domain) in regions.items():
            if domain == unblocked_domains[0]:
                return region_name
    elif len(unblocked_domains) == len(blocked_domains):
        return "Default (Not region locked)"
    else:
        return "Error in analysis"


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
            chosen_domain = regions[choice][1]
            regions_to_block = [region[1] for key, region in regions.items() if key not in ["0"] and region[1] != chosen_domain]
            domains_to_block = [f"gamelift.{region}.amazonaws.com" for region in regions_to_block] + \
                               [f"gamelift-ping.{region}.api.aws" for region in regions_to_block]

            return choice, chosen_domain, domains_to_block
        else:
            print("Invalid choice. Please try again.")


def clear_console():
    """Clear the console screen on Windows."""
    os.system('cls')


if __name__ == "__main__":
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    while True:
        choice, chosen_domain, domains_to_block = get_user_region_choice()

        if choice == "0":  # Set Default option
            print("\nPerforming cleanup...")
            remove_all_overrides()
        else:
            # Clean up all previously added domains before adding new ones
            print("\nCleaning up previous entries...")
            remove_all_overrides()

            ip_address = "0.0.0.0"  # IP address used to block the domains
            print(f"\nSelected region: {regions[choice][0]}")
            add_to_hosts(ip_address, domains_to_block)
            print(f"\nDone!")

        time.sleep(1)  # Wait for 1 second before the next iteration
        clear_console()
