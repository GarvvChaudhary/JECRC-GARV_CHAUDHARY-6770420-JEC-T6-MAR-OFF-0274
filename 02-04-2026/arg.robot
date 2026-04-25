*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Login Success    tunda4munda@gmail.com  #iamironman
    Sleep    5s
*** Keywords ***
Login Success
    [Arguments]  ${email}  ${pwd}=iamironman
    Input Text    id=customer_email    ${email}
    Input Text    id=customer_password    ${pwd}

