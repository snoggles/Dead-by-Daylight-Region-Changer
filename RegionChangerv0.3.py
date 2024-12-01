# ---------------------------------------------
# Dead by Daylight Region Changer
# Developed by DAMERTON
# GitHub: https://github.com/DAMERTON/Dead-by-Daylight-Region-Changer
# ---------------------------------------------



import os
import ctypes
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def add_to_hosts(ip, domains):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

    if is_admin():
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
    else:
        print("This script requires administrator privileges. Please run as administrator.")


def remove_from_hosts(domains):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

    if is_admin():
        with open(hosts_path, 'r') as hosts_file:
            lines = hosts_file.readlines()

        # Filter out lines containing domains to remove
        filtered_lines = [
            line for line in lines if not any(domain in line for domain in domains)
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

    else:
        print("This script requires administrator privileges. Please run as administrator.")

def get_current_region(regions):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts_path, 'r') as hosts_file:
        content = hosts_file.read()

    blocked_domains = [domain for _, domain in regions.values() if domain]
    unblocked_domains = [domain for domain in blocked_domains if domain not in content]

    if len(unblocked_domains) == 1:
        for key, (region_name, domain) in regions.items():
            if domain == unblocked_domains[0]:
                return region_name
    elif len(unblocked_domains) == len(blocked_domains):
        return "Default (No region locked)"
    else:
        return "Multiple regions unblocked"

def get_user_region_choice():
    regions = {
        "1": ("N. Virginia (us-east-1)", "gamelift-ping.us-east-1.api.aws"),
        "2": ("Ohio (us-east-2)", "gamelift-ping.us-east-2.api.aws"),
        "3": ("N. California (us-west-1)", "gamelift-ping.us-west-1.api.aws"),
        "4": ("Oregon (us-west-2)", "gamelift-ping.us-west-2.api.aws"),
        "5": ("Frankfurt (eu-central-1)", "gamelift-ping.eu-central-1.api.aws"),
        "6": ("Ireland (eu-west-1)", "gamelift-ping.eu-west-1.api.aws"),
        "7": ("London (eu-west-2)", "gamelift-ping.eu-west-2.api.aws"),
        "8": ("South America (sa-east-1)", "gamelift-ping.sa-east-1.api.aws"),
        "9": ("Asia Pacific (Mumbai) (ap-south-1)", "gamelift-ping.ap-south-1.api.aws"),
        "10": ("Asia Pacific (Seoul) (ap-northeast-2)", "gamelift-ping.ap-northeast-2.api.aws"),
        "11": ("Asia Pacific (Singapore) (ap-southeast-1)", "gamelift-ping.ap-southeast-1.api.aws"),
        "12": ("Asia Pacific (Sydney) (ap-southeast-2)", "gamelift-ping.ap-southeast-2.api.aws"),
        "13": ("Asia Pacific (Tokyo) (ap-northeast-1)", "gamelift-ping.ap-northeast-1.api.aws"),
        "14": ("Canada (ca-central-1)", "gamelift-ping.ca-central-1.api.aws"),
        "15": ("Set Default", None),
        "16": ("Exit", None)
    }

    print("GitHub: https://github.com/DAMERTON/Dead-by-Daylight-Region-Changer")
    print("-------------------------------------------------------------------")
    print("\nWelcome to the Bloodpoint Farming Region Changer!")
    print("Please select a region from the following options:\n")

    for key, (region_name, _) in regions.items():
        print(f"{key}. {region_name}")
        if key == "14":  # Add an empty line between options 14 and 15
            print()

    current_region = get_current_region(regions)
    print("\n---------------------------------------------------------")
    print(f"Current region: {current_region}")
    print("---------------------------------------------------------")
    
    while True:
        choice = input("\nEnter the number of your chosen option: ")
        if choice in regions:
            chosen_domain = regions[choice][1]
            domains_to_block = [region[1] for key, region in regions.items() if key not in ["15", "16"] and region[1] != chosen_domain]
            return choice, chosen_domain, domains_to_block, regions
        else:
            print("Invalid choice. Please try again.")



def clear_console():
    """Clear the console screen on Windows."""
    os.system('cls')
    
def clear_console():
    """Clear the console screen on Windows."""
    os.system('cls')
if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrator privileges. Please run as administrator.")
        input("Press Enter to exit...")
        exit()

    all_domains = []
    first_run = True

    while True:
        if not first_run:
            clear_console()
        first_run = False
        choice, chosen_domain, domains_to_block, regions = get_user_region_choice()

        if not all_domains:
            all_domains = [region[1] for key, region in regions.items() if key not in ["15", "16"]]
        if choice == "16":  # Exit option
            print("Exiting the script. Goodbye!")
            break
        elif choice == "15":  # Set Default option
            print("\nPerforming cleanup...")
            remove_from_hosts(all_domains)
        else:
            # Clean up all previously added domains before adding new ones
            print("\nCleaning up previous entries...")
            remove_from_hosts(all_domains)

            ip_address = "0.0.0.0"  # IP address used to block the domains
            print(f"\nSelected region: {regions[choice][0]}")
            add_to_hosts(ip_address, domains_to_block)
            print(f"\nDone!")

        time.sleep(1)  # Wait for 1 seconds before the next iteration
