*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary

*** Variables ***
#scalar variable
${url}  https://cricheroes.com/

#list variable
@{bikes}  ktm  kawasaki  honda  pulsar

#dictionary variable
&{cars}  nissan=gtr  honda=civic  bmw=m5

*** Test Cases ***
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://cricheroes.com/
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Log    navigated to cricheroes
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.honda}
    Sleep    3s

    Close Browser

Open cricbuzz in edge
     Open Edge Browser

*** Keywords ***
 Open Edge Browser
    [Documentation]  Chrome browser navigating to https://cricheroes.com/
    [Tags]  smoke
    Open Browser  ${url}  edge
    Maximize Browser Window

    Log    navigated to cricheroes
    Log To Console    navigated to cricheroeeees
    Sleep    3s

    Close Browser