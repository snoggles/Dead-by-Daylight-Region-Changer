# Developing

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
