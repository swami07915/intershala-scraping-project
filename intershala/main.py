import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# skill=input("which skill,language or field you are intrested in?")
# place=input("select majore tech cites rather than t2 t3 cites if possible.")
# work=input("you are comfertable in which one\nA.work from home\nB.part time\njust type  A or B or both type AB.")

skill="python"
place="mumbai"
work="AB"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver: Chrome=webdriver.Chrome(options=chrome_options)

if work=="A":
    driver.get(f"https://internshala.com/internships/work-from-home-{skill}-internships-in-{place}/")
elif work=="B":
    driver.get(f"https://internshala.com/internships/part-time-python-internships-in-mumbai/")
elif work=="AB":
    driver.get(f"https://internshala.com/internships/work-from-home-{skill}-internships-in-{place}/part-time-true/")


driver.maximize_window()
close=driver.find_element(By.ID,"close_popup")
close.click()


cards=driver.find_elements(By.CSS_SELECTOR,"div[class*='individual_internship']")


# wait = WebDriverWait(driver, 10)
# cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'individual_internship')]")))
# cards = driver.find_elements(By.XPATH, "//div[contains(@class,'individual_internship')]")
print(len(cards))
#
list_of_stipends=[]
for card in cards:
    try:
        time.sleep(1)
        stipend=card.find_element(By.CLASS_NAME,"stipend")
        clean_stipend=stipend.text
        without_symbol=clean_stipend.replace("₹","").replace("/month","")
        max_value=without_symbol.split()
        if len(max_value)==3:
            number=int(max_value[2].replace(",",""))
            print(number)
            list_of_stipends.append(number)
        elif len(max_value)==1:
            try:
                number=int(max_value[0].replace(",",""))
                print(number)
                list_of_stipends.append(number)
            except:
                pass
        time.sleep(1)
    except :
        pass
    # stipend = WebDriverWait(card, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"stipend"))).text
    # print(stipend)



