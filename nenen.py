from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_credentials():
    with open('email.txt') as f1, open('password.txt') as f2:
        return list(zip([line.strip() for line in f1], [line.strip() for line in f2]))

def create_driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_argument('--load-extension={}'.format(
        r'C:\Users\Administrator\Documents\rekt'))
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--window-size=900,760")
    return webdriver.Chrome(options=options)

def login(driver, email, password):
    driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1eqf2ixEhWTjHF_YVB7n9bFI2MrcyChe-%3Fusp%3Dsharing%26pli%3D1&ec=GAlAqQM&hl=en&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S1796273906%3A1747037422137558")
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email + Keys.ENTER)
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password + Keys.ENTER)
    sleep(5)
    try:
        driver.find_element(By.XPATH, '//*[@id="confirm"]').click()
        sleep(3)
    except:
        pass
    print(f"[{email}] Login sukses")

def handle_batch(account_batch, batch_index):
    driver = create_driver()
    for idx, (email, password) in enumerate(account_batch):
        if idx > 0:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[idx])
        login(driver, email, password)
        with open('result_login.txt', 'a') as f:
            f.write(f"{email} login sukses\n")

if __name__ == "__main__":
    all_accounts = get_credentials()
    batch_size = 10
    batches = [all_accounts[i:i + batch_size] for i in range(0, len(all_accounts), batch_size)]

    for batch_index, batch in enumerate(batches):
        handle_batch(batch, batch_index)
