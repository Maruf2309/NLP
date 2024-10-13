from selenium import webdriver
import os
driver_path = os.path.join(os.getcwd(),'chromedriver-win64')
exe_path = os.path.join(driver_path, 'chromedriver-win64.exe' )
print(exe_path)

#drive = webdriver.Chrome(exe_path)
drive = webdriver.Chrome()  # running successully

drive.get("https://innovativeskillsbd.com/")
#drive.get("   ")
#print (os.getcwd())
#print(selenium.__version__)


'''
from selenium import webdriver

# Define the path to the ChromeDriver executable
exe_path = 'E:\\M60\\nlp_batch3\\chromedriver-win64\\chromedriver.exe'

# Define the desired capabilities
capabilities = {
    'browserName': 'chrome',
    'version': '',
    'platform': 'ANY',
    'chromeOptions': {
        'args': ['--start-maximized']
    }
}

# Initialize the Chrome WebDriver with the executable path and capabilities
driver = webdriver.Chrome(executable_path=exe_path, desired_capabilities=capabilities)
'''
