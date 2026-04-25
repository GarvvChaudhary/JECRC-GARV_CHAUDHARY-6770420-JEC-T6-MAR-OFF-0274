*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
Handling Window
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/windows/new"]
    
    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}
    
    Switch Window  NEW
    
    Page Should Contain    New Window
    Page Should Contain Element    xpath=//h3[text()="New Window"]

    Switch Window  ${windows}[0]

    Close Window