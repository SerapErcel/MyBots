from githubUserInfo import username, password
from selenium import webdriver
import time
class Github:
    def __init__(self, username, password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.followers=[]

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]").click()

    def loadFolllowers(self):
        items=self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text)
                
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        self.loadFolllowers()

        while True:
            links=self.browser.find_element_by_class_name("paginate-container").find_elements_by_tag_name("a")
            if len(links)==0:
                self.loadFolllowers()
                break

            elif len(links)==1:
                if links[0].text=="Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFolllowers()

                else:
                    break

            elif len(links)==2:
                for link in links:

                    if link.text=="Next":
                        link.click()
                        time.sleep(1)
                        self.loadFolllowers()
                    
                    else:
                        continue


github =Github(username, password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)
