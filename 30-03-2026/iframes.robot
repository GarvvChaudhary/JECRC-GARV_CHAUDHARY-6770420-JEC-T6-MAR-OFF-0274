*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling Single iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Select Frame    id=singleframe
    
    Input Text    xpath=//input[@type="text"]    JINGA
    Sleep    5s
    Unselect Frame

    Close Browser

Handling Nested iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    [Tags]  nested
    Sleep    2s

    Click Element    xpath=//a[text()="Iframe with in an Iframe"]

    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]

    Select Frame    xpath=//iframe[@src="SingleFrame.html"]

    Input Text    xpath=//input[@type="text"]    Jingaaaa

    Sleep    5s

    Close Browser