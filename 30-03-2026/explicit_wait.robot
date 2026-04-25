*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://practicetestautomation.com/practice-test-login/

*** Test Cases ***
Handling explicit wait
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Wait Until Element Is Visible    id=username
    Input Text    id=username    student
    Sleep    2s

    Wait Until Element Is Visible    id=password
    Input Text    id=password    Password123
    Sleep    2s

    Wait Until Element Is Enabled    id=submit
    Click Element    id=submit

    Wait Until Location Contains    logged-in-successfully
    Sleep    2s

    Close Browser