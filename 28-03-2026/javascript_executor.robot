*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
Handling JavaScript
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Execute Javascript  window.scrollTo(0,document.body.scrollHeight)
    Sleep    2s

    Execute Javascript  window.scrollTo(0,0)
    Sleep    2s
    Execute Javascript  window.scrollBy(0,500)
    Sleep    2S
    Execute Javascript  window.scrollBy(0,-300)
    Sleep    2S

    Close Browser