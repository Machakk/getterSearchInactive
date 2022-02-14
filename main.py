from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
gettertool = "https://www.gettertools.com/nys.x1.asia.travian.com/42-Search-inactives#result"

driver.get(gettertool)

# Accept cookies
cookies = driver.find_element(By.CSS_SELECTOR, 'body > div > form > div > div > div.consentBoxBottom > '
                                               'div.consentBoxButtons > '
                                               'button.stylebutton.-accept-all.-button-main.-button-highlight')
cookies.click()

# left and right coor from getter site (for inactive players)
left_coord = driver.find_elements(By.CLASS_NAME, 'koordk1 > span')
right_coord = driver.find_elements(By.CLASS_NAME, 'koordk2 > span')

# Izbaciti iz liste sve leve koordinate

koordsLeva = []
koordsDesna = []

# lists with x and y coordinates
for k in left_coord:
    tmp = k.text
    koordsLeva.append([tmp])

for k in right_coord:
    tmp = k.text
    koordsDesna.append([tmp])

cpt1 = 0
cpt2 = 0
newList = []
while cpt1 < len(koordsLeva):
    newList.append(koordsLeva[cpt1] + koordsDesna[cpt2])
    cpt1 = cpt1 + 1
    cpt2 = cpt2 + 1

# change to new url
driver.get("https://nys.x1.asia.travian.com/")

# opening new raid list
create_raid = driver.find_element(By.XPATH, '//*[@id="raidList"]/div[3]/div[1]/a[2]/div/span')
create_raid.click()

# REP This action from here

# add village target
targets = driver.find_element(By.XPATH, '//*[@id="raidList903"]/div[2]/form/table/tfoot/tr[1]/td/a').click()
# left and rigth village coordinate target
left_target = driver.find_element(By.XPATH, '//*[@id="xCoordInput"]')
right_target = driver.find_element(By.XPATH, '//*[@id="yCoordInput"]')

# two dimensional array - coodrinates injection
cpt_injection = 0
for i in newList:
    left_target.send_keys(newList[0][0])