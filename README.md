# RobloxServerJoinerMk2
This is a W.I.P script that allows you to go to any roblox server locale of your choosing. Originally made by Exilon24. There are a LOT of issues with the code and any improvements would be greatly accepted

## Installation:
Open your terminal and move to the directory you wish to install this tool and clone this repo: git clone https://github.com/TheConfusedlol/RobloxServerJoinerMk2.git

Then cd into the installed directory and run pip install -r requirements.txt

The program requires some settings to be set. Open up roServerFinder.py in a text editor (notepad, vim, anything really). There are 2 fields you need to set (starting line 7):

# Finding the roblox cookie
Download a cookie editor extension. [I use this one](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en)
Go to roblox
Log into the account you want the cookie for
Open the extension and copy your .ROBLOSECURITY cookie and paste it into the robloxserverfinder python script: image. <br/>
**Do not show this string to anyone, doing so will allow them to log into your account. If you do share it, use the extension to clear your cookies and re-login to your account.**

## Enter desired city and region here (Florida used as an example)
```
targetCity = "miami"
targetRegion = "florida"
targetCountryCode = "US"
```

Make sure to save your changes before running the script.
## List of every known roblox server reigon (as at 29/9/2024)
Format: City Symbol, City
```
Ashburn, Virginia, US
Secaucus, New Jersey US
Dallas, Texas, US
Los Angeles, California, US
Miami, Florida, US
Palo Alto, California, US
San Mateo, California, US
Newark, New Jersey, US
Atlanta, Georgia, US
City of London, England, United Kingdom
Singapore, Singapore
Frankfurt am Main, Hesse, Germany
Amsterdam, North Holland, Netherlands
Paris, Île-de-France, France
Hong Kong, China
Tokyo, Tokyo-to, Japan
Mumbai, India
Sydney, Australia
São Paulo, Brazil
```
## List of every known roblox server country reigon (as at 29/9/2024)
```
US - North/South America (Ashburn, Virginia; Secaucus, NJ; Dallas, TX; Los Angeles, CA; Miami, FL; Palo Alto, California; San Mateo, California; Newark, New Jersey; Atlanta, Georgia)
UK - United Kingdom (City of London, England)
SG - Singapore
DE - Germany (Frankfurt am Main, Hesse)
NL - Netherlands (Amsterdam, North Holland)
FR - France (Paris, Île-de-France)
HK - Hong Kong
JP - Japan (Tokyo, Tokyo-to)
IN - India (Mumbai)
AU - Australia (Sydney)
BR - Brazil (São Paulo)
```
## Addendum: Handling Cities Without States
When specifying a city and region, it's important to note that not all cities are associated with a state or province. For cities like Tokyo or London, which are major urban centers and not part of a state system, you can follow this format:
``` 
Enter desired city and region here
targetCity = "tokyo"          # For cities without a state, use the city name only
targetRegion = ""              # Leave this blank if the city does not have a state
targetCountryCode = "JP"      # Use the appropriate country code (e.g., "JP" for Japan, "UK" for the United Kingdom)
```
# Non-working servers:
Singapore
Portland, Oregon
Tokyo, Japan

## Usage
Then go to the directory roServerFinder.py is in and run python roServerFinder.py and enter the game ID e.g: https://www.roblox.com/games/15069312471/LifeLike-Disasters game ID is 15069312471

This will open a browser window, requesting to join a roblox game. It will prompt you to allow roblox to open. If you decline, roblox will not open. The browser window will automatically close after you join.
# Safety
I understand that it can be concerning to give your Roblox security information to a random piece of code from the internet. I want to assure you that this script will not hack your account. It's designed solely to help you join the servers you want to play on.
# Virus-Total Results
![image](https://github.com/user-attachments/assets/4d1b88c9-0dab-4419-a5ed-43fdf4e68f83)
[link to the report](https://www.virustotal.com/gui/file/46d8780b0d0d991df26ca72c24a1919cbfc1f95c6092fdf843c6621eda12072c?nocache=1)

