import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

class DiscordAccountCreator:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()
        
    def create_account(self):
        self.driver.get("https://discord.com/register")
        time.sleep(2)
        
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys(self.username)
        
        email_input = self.driver.find_element_by_name("email")
        email_input.send_keys(self.email)
        
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(self.password)
        
        password_input.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        # Simulate email verification
        verification_link = self.get_verification_link(self.email)
        
        if verification_link:
            response = requests.get(verification_link)
            if response.status_code == 200:
                print("Account created successfully!")
            else:
                print("Failed to verify email.")
        else:
            print("Failed to get verification link.")
        
        self.driver.quit()
        
    def get_verification_link(self, email):
        # Simulate getting verification link from email inbox
        # This is a placeholder function, actual implementation depends on email provider
        
        # For the sake of this example, we will return a dummy verification link
        return "https://dummy_verification_link.com"
        
# Example of creating an account
username = "test_user"
email = "test@example.com"
password = "strongpassword123"

account_creator = DiscordAccountCreator(username, email, password)
account_creator.create_account()