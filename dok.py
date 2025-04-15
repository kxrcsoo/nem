import webbrowser
import pyautogui
import time

# Open the URL in the default browser
url = 'https://kurcsoo.eu/dok.html'
webbrowser.open(url)

# Wait for the page to load (adjust time as necessary for slower connections)
time.sleep(0.5)

# Get the screen width and height
screenWidth, screenHeight = pyautogui.size()

# Calculate the center of the screen
centerX, centerY = screenWidth // 2, screenHeight // 2

# Click on the center of the screen
pyautogui.click(centerX, centerY)

# Simulate pressing the F11 key to toggle fullscreen in most browsers
pyautogui.press('o')
time.sleep(0.1)
pyautogui.press('f11')

# Wait a bit for fullscreen to take effect



