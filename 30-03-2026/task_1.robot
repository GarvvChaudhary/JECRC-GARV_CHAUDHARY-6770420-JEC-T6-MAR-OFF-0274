'''
TASK 1
1.
'''

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Popup Window
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    
    Scroll Element Into View    xpath=//button[@id="PopUp"]

    Click Element    xpath=//button[@id="PopUp"]

    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}

    Switch Window  NEW
    Sleep    3s

    Switch Window  ${windows}[0]
    
    Page Should Contain Element   xpath=//h3[@class="post-title entry-title"]
    Sleep    2s

    Close Window