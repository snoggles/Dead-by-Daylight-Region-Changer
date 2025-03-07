# Dead-by-Daylight-Region-Changer
## Overview  
Region Changer is a lightweight, easy-to-use tool for players of Dead by Daylight to manually select specific regions. This is especially useful for players with slower internet connections or those who want to bypass automatic server selection without relying on a VPN.

## How It Works
Dead by Daylight uses AWS GameLift servers to host its multiplayer sessions. These servers are distributed across multiple regions worldwide, such as North America, Europe, Asia, and others. The game usually determines the best region automatically based on latency and availability.

Region Changer works by modifying your system's hosts file to block specific AWS GameLift servers from responding. By selectively blocking access to unwanted regions, the game is forced to connect to the allowed region, giving you more control over your matchmaking experience.

## Features  
- Lightweight: Minimalist design and low resource usage.  
- Custom Region Selection: Choose your preferred server region with ease.  
- No VPN Required: Avoid the hassle and potential slowdowns of a VPN connection.  
- Quick Setup: One-click functionality to switch regions or reset to default.  

## How to Use
1. Run [RegionChanger.exe](https://github.com/snoggles/Dead-by-Daylight-Region-Changer/releases/latest/download/RegionChanger.exe) (it asks to run as administrator to modify the hosts file).
2. Select the region you want from the list.
3. The tool will automatically block other regions, forcing Dead by Daylight to connect to your selected region.
4. If you wish to reset to the default settings, use the Cleanup option to unblock all regions.

## Limitations  
- This tool modifies the hosts file. While this is safe, antivirus software may flag it as suspicious — this is a false positive.
- You must run the tool as an administrator for it to work correctly.

## Disclaimer  
- This software is not affiliated with or endorsed by Dead by Daylight or AWS.  
- Use at your own risk. Ensure you understand how modifying your hosts file affects your system.

---

## Running from source

Alternatively, instead of [running the .exe](#how-to-use), you can run the [RegionChanger.py](https://github.com/snoggles/Dead-by-Daylight-Region-Changer/releases/latest/download/RegionChanger.py) script directly if you [install python](#1-install-python).

### Benefits
- Faster startup time.
- Antivirus will not interfere with it.
- You can easily see what it's doing and make changes.

### Creating Shortcut
1. Right click > New Shortcut > `python.exe C:\path\to\RegionChanger.py` > Finish
2. Right click shortcut > Properties > Shortcut > Advanced > Run as administrator > OK > OK
3. Rename shortcut to something like `Region Changer`
4. Move shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs` to make it available on the start menu

---

## How to Build Your Own Version

If you want to build your own version of the Region Changer as an executable (.exe), follow these simple steps:

### What You Need:
- **Python** installed on your computer (download it from (https://www.python.org/).

### Step-by-Step Guide

#### 1. Install Python
If you don't have Python installed:
- Go to (https://www.python.org/downloads/) and download the latest version for your operating system.
- Install Python, and make sure to check the box that says "Add Python to PATH" during the installation.

#### 2. Install Requirements
- Open a terminal or command prompt on your computer:
  - **Windows**: Press `Win + R`, type `cmd`, and hit Enter.
  - **Mac/Linux**: Open the Terminal app.

- Type the following command and press Enter:

```bash
pip install -r requirements.txt
```

This command will install the packages used to turn Python scripts into `.exe` files.

#### 3. Prepare Your Files
- Make sure you have the following files in the same folder:
  - `RegionChanger.py` (the script you want to convert).
  - `BPS.ico` (your custom icon for the EXE file).

#### 4. Open the Terminal/Command Prompt in the Script's Folder
- In **Windows**, right-click on the folder containing your files, and select "Open command window here" or "Open PowerShell window here."
- In **Mac/Linux**, navigate to the folder in the terminal using the `cd` command.

#### 5. Run the Command to build the .exe
- In the terminal or command prompt, type the following command:

```bash
build.bat
```

#### 6. Wait for the EXE to build
Building may take a few minutes. Once it's done, you’ll see some new folders created in your script's directory:
- **build**: This is where the EXE file and other temporary files are saved.

#### 7. Find the EXE File
- Navigate to the **build** folder.
- Inside, you’ll find `RegionChanger.exe`. This is your final executable file!

#### 8. Test Your EXE
- Double-click the `RegionChanger.exe` file to make sure it works as expected.
- If everything looks good, you can start using it or share it with others!

And that's it! You've successfully built your own version of the Region Changer EXE.
---

If you have feedback, questions, or encounter issues, feel free to reach out!  

Happy gaming! 🎮
