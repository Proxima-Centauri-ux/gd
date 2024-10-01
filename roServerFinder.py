import requests
from selenium import webdriver
import asyncio
import time
import aiohttp

# Enter your roblox cookie here
robloxCookie = " "

# Enter desired city and region here
targetCity = "miami"
targetRegion = "florida"
targetCountryCode = "US"

print("Roblox Server Finder by Exilon (Exilon24 on GitHub).")
placeId = int(input("PlaceID: "))
print("Looking for game...")

# Get game server details from Roblox API
uri = f"https://games.roblox.com/v1/games/{str(placeId)}/servers/Public?excludeFullGames=true&limit=100"
response = requests.get(url=uri)
servers = response.json()["data"]

gameUniverseID = requests.get(f"https://apis.roblox.com/universes/v1/places/{str(placeId)}/universe").json()["universeId"]
gameInfo = requests.get(f"https://games.roblox.com/v1/games?universeIds={str(gameUniverseID)}").json()["data"][0]

print("--------------------------------------------------------")
print(f"Now joining: {gameInfo['name']} by {gameInfo['creator']['name']}.\nThere are {gameInfo['playing']} players currently online.")
print("--------------------------------------------------------")
print("Attempting to find server information...")

authCookies = {
    ".ROBLOSECURITY": robloxCookie,
}
authHeaders = {
    "Referer": f"https://www.roblox.com/games/{placeId}/",
    "Origin": "https://roblox.com",
    "User-Agent": "Roblox/WinInet",
}

taskList = []
global driver
driver = webdriver.Chrome()

async def getServerInfo(server):
    async with aiohttp.ClientSession(cookies=authCookies) as session:
        serverId = server["id"]
        res = await session.post("https://gamejoin.roblox.com/v1/join-game-instance",
                     data={
                     "placeId": placeId,
                     "isTeleport": False,
                     "gameId": serverId,
                     "gameJoinAttemptId": serverId
                     },
                     headers=authHeaders)
        ip = await res.json()
        ip = ip["joinScript"]

        if ip == None:
            return False

        try:
            ip = ip["UdmuxEndpoints"][0]["Address"]
        except:
            print("Error with roblox server joins...")
            return False

        # Geolocation request for the IP address
        geolocation = await session.get(f"http://ip-api.com/json/{ip}")
        geolocation = await geolocation.json()

        if geolocation["status"] != "success":
            return False

        # Print out the geolocation details
        print(f"Server found at ({geolocation['countryCode']}) --> {geolocation['region']}, {geolocation['city']}")

        # Check if the server is located in Miami, Florida
        if geolocation["countryCode"] == targetCountryCode and geolocation["city"].lower() == targetCity and geolocation["regionName"].lower() == targetRegion:
            driver.get(f"https://www.roblox.com/games/{str(placeId)}/")
            driver.add_cookie({
                "name": ".ROBLOSECURITY",
                "value": robloxCookie,
                "path": "/",
                "domain": ".roblox.com"
            })
            driver.refresh()
            driver.execute_script(f"Roblox.GameLauncher.joinGameInstance({placeId}, \"{serverId}\")")
            for t in taskList:
                t.cancel()
            return True
        return False

# Main async loop to find servers
async def main():
    for server in servers:
        taskList.append(asyncio.create_task(getServerInfo(server)))

    try:
        await asyncio.gather(*taskList)
    except:
        print("Done...")  # Ignore the cancelled exception.

asyncio.run(main())
time.sleep(20)  # Keep the webdriver open to ensure Roblox loads
