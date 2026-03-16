# 🤔 Problem Statements

<p align="right"><b>Assigned on:</b> 16-03-2026</p>

---

## Task 1

### OrangeHRM Login

Automate the login flow in OrangeHRM and verify that the user successfully reaches the dashboard:

1. Open the OrangeHRM demo website. `https://opensource-demo.orangehrmlive.com/`
2. Get and print the title of the page.
3. Locate the username input field and use clear() if needed.
4. Enter the username using send_keys().
5. Locate the password input field and enter the password using send_keys().
6. Submit the login form using either: click() on the Login button, or Keys.ENTER
7. After login, print the current URL.
8. Check if dashboard is present in that url using `in`
9. Print 'successful login'

Test Data:

Username: `Admin`
Password: `admin123`

---

## Task 2

### Radio Buttons

Automate interaction with radio buttons `https://demoqa.com/radio-button`

1. Open the radio button page.
2. Print the **title** of the page.
3. Locate the **"Yes" radio button**.
4. Click the radio button using `click()`.
5. Capture and print the **result message** using `.text`.
6. Use `get_attribute()` to fetch attributes like:
   - `class`
   - `id`
7. Print the **current URL**.
---
