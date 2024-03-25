# Testcase

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class ATG(unittest.TestCase):

    def setUp(self):
        options = AppiumOptions()
        options.load_capabilities({
        "platformName": "android",
        "appium.appActivity": "com.atg.world.activity.SplashActivity",
        "appium.appWaitDuration": "5000",
        "appium.appExecTimeout": "50000",
        "appium:automationName": "UiAutomator2",
        "appium.uiautomator2ServerLaunchTimeout": "50000",
        "appium.uiautomator2ServerInstallTimeout": "50000",
        "appium.appPackage": "com.ATG.World",
        "appium.deviceName": "emulator-5554",
        "appium.driver": "http://localhost:4723/wd/hub"})
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    
    def tearDown(self):
        self.driver.quit()

    def test_LoginWithRightCredential(self):
       getstarted = self.driver.find_element(By.ID, "com.ATG.World:id/getStartedTv")
       getstarted.click()
       loginemail = self.driver.find_element(By.ID, "com.ATG.World:id/login_email")
       loginemail.click()
       email = self.driver.find_element(By.ID, 'com.ATG.World:id:id/email')
       email.send_keys('wiz_saurabh@rediffmail.com')
       password = self.driver.find_element(By.ID, 'com.ATG.World:id/password')
       password.send_keys('Pass@123')
       signin = self.driver.find_element(By.ID, 'com.ATG.World:id/email_sign_in_button')
       signin.click()
       print("test_LoginWithRightCredential passed")
       sleep(10)
    
    def test_PostImage(self):
        fab = self.driver.find_element(By.ID, "com.ATG.World:id/fab")
        fab.click()
        image = self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Image"]')
        image.click()
        take_picture = self.driver.find_element(By.ID, "android:id/button1")
        take_picture.click()
        flipcam = self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/flipCamera")
        flipcam.click()
        click_img_button = self.driver.find_element(By.ID, "com.ATG.World:id/img_clicked_btn")
        click_img_button.click()
        next = self.driver.find_element(By.ID, "com.ATG.World:id/toolbar_post_action")
        next.click()
        caption = self.driver.find_element(By.ID, "com.ATG.World:id/caption_edit_text")
        caption.send_keys('test')
        post = self.driver.find_element(By.ID, "//android.widget.TextView[@resource-id=\"com.ATG.World:id/toolbar_post_action\" and @text=\"Post\"]")
        post.click()
        print("test_PostImage passed")
        sleep(10)


        #################### Test Case Recorded from Appium ################################
        # el49 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/fab")
        # el49.click()
        # el50 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Image\"]")
        # el50.click()
        # el51 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        # el51.click()
        # el52 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/flipCamera")
        # el52.click()
        # el53 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/img_clicked_btn")
        # el53.click()
        # el54 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/toolbar_post_action")
        # el54.click()
        # el55 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/caption_edit_text")
        # el55.send_keys("test")
        # el56 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.ATG.World:id/toolbar_post_action\" and @text=\"Post\"]")
        # el56.click()
        ######################################################################################



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ATG)
    unittest.TextTestRunner(verbosity=2).run(suite)
