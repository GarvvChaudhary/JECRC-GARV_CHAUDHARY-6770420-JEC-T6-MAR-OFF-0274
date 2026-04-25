*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handling Alerts
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Click Button    xpath=//button[@onclick="jsAlert()"]
    Sleep    2s

    Handle Alert
    Sleep    2s

    Close Browser

Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsConfirm()"]
    Sleep    2s

    Handle Alert  action=DISMISS
    Sleep    2s
    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsPrompt()"]
    Sleep    2s
    Input Text Into Alert    Jingaaaaaa  action=DISMISS
    Sleep    2s

    Close Browser