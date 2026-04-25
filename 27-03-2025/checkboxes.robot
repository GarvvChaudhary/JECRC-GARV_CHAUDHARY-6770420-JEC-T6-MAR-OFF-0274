*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${chk}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkboxes
     [Documentation]  herokuapp checkboxes
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Sleep    1s
     
     Click Element    xpath=//a[text()="Checkboxes"]
     
     Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]

     Select Checkbox    xpath=(//input[@type="checkbox"])[1]
     Sleep    2s

     Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
     Sleep    2s

     Close Browser

Practice Checkboxes
    [Documentation]  practicing checkboxes
    Open Browser  ${chk}  chrome
    [Tags]  check
    Maximize Browser Window
    Sleep    3s
    
    Click Element    xpath=//input[@id="male"]
    
    Page Should Contain Checkbox    xpath=//input[@id="sunday"]
    
    Select Checkbox    xpath=//input[@id="sunday"]
    Sleep    3s
    
    Select Checkbox    xpath=//input[@id="monday"]
    Sleep    3s

    Close Browser