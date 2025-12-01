# Dead-by-Daylight-Region-Changer
## Overview
Region Changer is a lightweight, easy-to-use tool for players of Dead by Daylight to manually select specific regions. This is especially useful for players with slower internet connections or those who want to bypass automatic server selection without relying on a VPN.

## How It Works
Dead by Daylight uses AWS GameLift servers to host its multiplayer sessions. These servers are distributed across multiple regions worldwide, such as North America, Europe, Asia, and others. The game usually determines the best region automatically based on latency and availability.

Region Changer works by modifying your system's hosts file to block specific AWS GameLift servers from responding. By selectively blocking access to unwanted regions, the game is forced to connect to the allowed region, giving you more control over your matchmaking experience.

## Features
- Lightweight: Minimalist design and low resource usage.
- Custom Region Selection: Choose your preferred server region with ease.
- No VPN Required: Avoid the hassle, cost, and higher ping of a VPN connection.

## Setup
### 1. Install Python
If you don't have Python installed:
- Go to (https://www.python.org/downloads/) and download the latest version for your operating system.
- Install Python

### 2. Download the script
https://github.com/snoggles/Dead-by-Daylight-Region-Changer/releases/latest/download/RegionChanger.py

### 3. Create a Shortcut
1. Right click > New Shortcut > `python.exe "C:\path\to\RegionChanger.py"` > Finish
2. Right click shortcut > Properties > Shortcut > Advanced > Run as administrator > OK > OK
3. Rename shortcut to something like `Region Changer`
4. Move shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs` to make it available on the start menu

## How to Use
1. Run the [RegionChanger.py](https://github.com/snoggles/Dead-by-Daylight-Region-Changer/releases/latest/download/RegionChanger.py) shortcut (it asks to run as administrator to modify the hosts file).
2. Select the region you want from the list.
3. The tool will automatically block other regions, forcing Dead by Daylight to connect to your selected region.
4. If you wish to reset to the default settings, use the Cleanup option to unblock all regions.

---

## Limitations
- This tool modifies the hosts file. While this is safe, antivirus software may flag it as suspicious — this is a false positive.
- You must run the tool as an administrator for it to work correctly.

## Disclaimer
- This software is not affiliated with or endorsed by Dead by Daylight or AWS.
- Use at your own risk. Ensure you understand how modifying your hosts file affects your system.

## Building an exe (not recommended)
There are instructions to [build an exe](developing.md), but most virus scanners will automatically delete it, so this is not recommended.

## Support
If you have feedback, questions, or encounter issues, feel free to reach out!

Happy gaming! 🎮
