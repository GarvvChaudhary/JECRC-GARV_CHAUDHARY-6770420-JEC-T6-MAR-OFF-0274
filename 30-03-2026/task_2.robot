*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Scroll Element Into View    id=alertBtn

    Click Button    id=alertBtn
    Sleep    2s

    Handle Alert
    Sleep    2s

    Close Browser

Confirm alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    id=confirmBtn

    Click Button    id=confirmBtn
    Sleep    2s

    Handle Alert
    Page Should Contain    You pressed OK!

    ${text}  Get Text    id=demo
    Log To Console    ${text}

    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    id=promptBtn

    Click Button    id=promptBtn
    Sleep    2s

    Input Text Into Alert    JINGA
    Page Should Contain    Hello JINGA! How are you today?

    ${text}  Get Text    id=demo
    Log To Console    ${text}

    Close Browser