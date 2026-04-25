'''
Implicit wait- global; used once; wait for the element; before giving the error
Explicit wait- element specific;
'''

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Set Selenium Implicit Wait    5s

    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    Close Browser

#Get selenium implicit wait = Returns you the time of implicit wait
#Set selenium implicit wait = this keyword lets you set implicit wait, usually in seconds is recommended
#Set Browser Implicit Wait = this keyword lets you set implicit wait for one browser instance,
#                            if there are multiple browsers then it will e confined to that browser

