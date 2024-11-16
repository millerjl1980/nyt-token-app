from playwright.sync_api import sync_playwright

indypl_nyt_url = 'https://pr.indypl.org/nyt/nytTokenSignIn.php?section=digital'
lib_card_num = ''
email_addr = ''
nyt_token = ''

def solve_drag_puzzle(page):
    draggable = page.locator(".slider")
    drop_target = page.locator(".sliderTarget")
    draggable.drag_to(drop_target)


with sync_playwright() as p:
    chrome = p.chromium.launch(headless=False, slow_mo=500)
    page = chrome.new_page()
    # Step 1: Enter library card number and submit
    page.goto(indypl_nyt_url)
    page.fill('input#cNum', lib_card_num)
    page.click('input[type=submit]')
    # Step 2: Wait for the modal and click "Continue"
    page.wait_for_selector('.css-t0f7tz')
    page.click('button[type=button]')
    # Step 3: Wait for the "Submit" button underneath to become interactable
    page.wait_for_selector(".css-1aisqmo ", state="visible")
    page.click('button[type=submit]')
    # Step 4: Wait for the login page to open for the NYT
    if page.frame_locator('iframe#captcha-container').locator('#captcha-container').is_visible():
        solve_drag_puzzle(page)
    page.wait_for_selector('#email', state='visible')
    page.fill('input#email', email_addr)

    body > iframe