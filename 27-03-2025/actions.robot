*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***

Handling Drag and Drop
    Open Browser  ${url}  chrome
    [Tags]  drop
    Maximize Browser Window
    Sleep    3s
    
    Click Element    xpath=//a[text()="Drag and Drop"]
    Sleep    5s
    
    Drag And Drop    id=column-a    id=column-b
    Sleep    5s

    Close Browser

Handling mouse hover
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    
    Click Element    xpath=//a[text()="Hovers"]
    Sleep    2s

    Mouse Over    xpath=(//div[@class="figure"])[2]
    Sleep    3s

Scroll to element
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Scroll Element Into View    xpath=//a[text()="Typos"]
    Sleep    3s

    Close Browser