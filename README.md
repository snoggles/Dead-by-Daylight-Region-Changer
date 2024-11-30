# Dead-by-Daylight-Region-Changer
## Overview  
Region Changer is a lightweight, easy-to-use tool designed for players of Dead by Daylight who wish to optimize their gaming experience by manually selecting specific regions. This is especially useful for players with slower internet connections or those who want to bypass automatic server selection without relying on a VPN.  

## How It Works  
Dead by Daylight uses AWS GameLift servers to host its multiplayer sessions. These servers are distributed across multiple regions worldwide, such as North America, Europe, Asia, and others. The game usually determines the best region automatically based on latency and availability.  

Region Changer works by modifying your system's hosts file to block specific AWS GameLift servers from responding. By selectively blocking access to unwanted regions, the game is forced to connect to the allowed region, giving you more control over your matchmaking experience.  

## Features  
- Lightweight: Minimalist design and low resource usage.  
- Custom Region Selection: Choose your preferred server region with ease.  
- No VPN Required: Avoid the hassle and potential slowdowns of a VPN connection.  
- Quick Setup: One-click functionality to switch regions or reset to default.  

## How to Use  
1. Run the software as an administrator (required to modify the hosts file).  
2. Select the region you want from the list.  
3. The tool will automatically block other regions, forcing Dead by Daylight to connect to your selected region.  
4. If you wish to reset to the default settings, use the Cleanup option to unblock all regions.  

## Limitations  
- This tool modifies the hosts file. While this is safe, antivirus software may flag it as suspicious—this is a false positive.  
- You must run the tool as an administrator for it to work correctly.  

## Disclaimer  
- This software is not affiliated with or endorsed by Dead by Daylight or AWS.  
- Use at your own risk. Ensure you understand how modifying your hosts file affects your system.  

---

If you have feedback, questions, or encounter issues, feel free to reach out!  

Happy gaming! 🎮
