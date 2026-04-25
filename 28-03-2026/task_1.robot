*** Settings ***
Documentation  Handling Multiselect
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
${locator}  id=colors

*** Test Cases ***
Handling Multiselection
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Page Should Contain List    ${locator}
    ${options}=  Get List Items    ${locator}
    Log To Console    ${options}


    Select From List By Label    ${locator}  Blue
    Sleep    1s

    Select From List By Label    ${locator}  Yellow
    Sleep    1s
    
    @{selected_options}=  Get Selected List Labels    ${locator}
    Log To Console    ${selected_options}

    List Selection Should Be    ${locator}  @{selected_options}
    Sleep    3s

    Close Browser
