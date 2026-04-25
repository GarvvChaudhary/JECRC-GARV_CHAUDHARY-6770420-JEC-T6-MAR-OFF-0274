*** Settings ***
Documentation  Handling dropdowns
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***

Handle dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[text()="Dropdown"]
    
    Page Should Contain List    id=dropdown

    ${options}=  Get List Items    id=dropdown
    Log To Console    ${options}

    Select From List By Label  id=dropdown  Option 1

    ${selected_option}=  Get Selected List Labels    id=dropdown
    Log To Console    ${selected_option}

    List Selection Should Be    id=dropdown  Option 1
    Sleep    3s

    Close Browser

