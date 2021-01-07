from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import csv

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('window-size=1920x1080')



lines = open('output.txt').read().splitlines()
myline =random.choice(lines)

email_name = f"{myline}" "+" + str(random.randint(0,1000))+"@gmail.com"


print(email_name)


class ExpressVPN:

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/zacnicholson/Desktop/ExpressVPN/chromedriver') #, options=chrome_options

    def new_account(self):
        self.driver.get('Put Referal Link Here')
        sleep(2)
        order = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/a/span[1]').click()
        sleep(1)
        select_type = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div[2]/div[1]').click()
        sleep(1)
        email = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[2]/div/div[2]/div/input')
        email.send_keys(email_name)
        sleep(1)

        credit_card = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[1]/a').click()
        first_name = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/input').send_keys(myline)
        last_name = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/input').send_keys(myline)
        credit_card_number = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/input[2]').send_keys("###")
        month = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div/div/div[1]/div/select/option[5]').click()
        year = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div/div/div[2]/div/select/option[8]').click()
        csv = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[2]/div/input').send_keys("###")
        join = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div[4]/div[1]/div/div/div[1]/div[2]/div/p[1]/input').click()
        sleep(15)
        self.driver.get('https://www.expressvpn.com/subscriptions')
        turn_off_renewal = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/a').click()
        sleep(2)
        turn_off_renewal_2 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/a').click()
        turn_off_renewal_3 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/a[3]').click()
        turn_off_renewal_4 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[7]/a').click()
        sleep(2)
        final_cancel = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/a').click()
        

        # sleep(10)
        # self.driver.close()

    sleep(2)


bot = ExpressVPN()
bot.new_account()