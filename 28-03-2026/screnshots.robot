*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/../Screenshots
    
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Capture Page Screenshot  fullpage.png
    Sleep    2s
    
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  dhurandhar.png
    Sleep    2s

    Close Browser