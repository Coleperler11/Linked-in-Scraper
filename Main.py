from selenium import webdriver
from time import sleep
import json

def main():
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://www.linkedin.com')

    username, password = get_credentials()

    try:
        username_field = driver.find_element_by_id('session_key')
        username_field.send_keys(username)
        
    except:
        print("Unable to find username field")
        return

    sleep(1)


    try:
        password_field = driver.find_element_by_id('session_password')
        password_field.send_keys(password)
        
    except:
        print("Password field not found")
        return

    sleep(1)

    button = driver.find_element_by_class_name('sign-in-form__submit-button')
    button.click()
    sleep(10)

    sales_navigator = driver.find_element_by_id('ember39')
    button.click()
    sleep(5)
    


def get_credentials():
    username, password = None, None
    try:
        with open("auth.json", 'r') as file:
            data = json.load(file)
            username = data['username']
            password = data['password']

            
    except FileNotFoundError:
        print("No auth file added. ")

    
    if not (username and password):
        print("Missing either username or password, check auth file")
        exit()

    return username, password


if __name__ == "__main__":
    main()
