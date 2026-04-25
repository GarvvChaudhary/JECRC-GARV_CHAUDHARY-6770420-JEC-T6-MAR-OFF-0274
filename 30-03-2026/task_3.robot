'''
TASK 3

Navigate to amazon
Click on electronic in tab
Check on 'boat' checkbox
click on any product before clicking store the name of product
switch to new window
assert the product name is present in the new window
print the actual price, discounted price and the percentage
scroll to add to cart and click on the button
click on cart icon on top right corner
check if same product has been added
'''

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Amazon
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//div[@id="nav-main"]//descendant::a[text()=" Electronics "]
    Sleep    1s

    Click Element    xpath=(//span[text()="boAt"])[2]
    Sleep    2s

    ${product_name}  Get Text    //div[@cel_widget_id="MAIN-SEARCH_RESULTS-9"]/descendant::h2
    Log To Console    ${product_name}

    Click Element    xpath=//div[@cel_widget_id="MAIN-SEARCH_RESULTS-9"]
    Sleep    2s

    Switch Window  NEW

    Page Should Contain    ${product_name}

    ${actual_price}  Get Text    xpath=//span[@class="aok-relative"]
    Log To Console    ${actual_price}

    ${discounted_price}  Get Text    xpath=(//span[@class="a-price-whole"]//ancestor::span[@aria-hidden="true"])[6]
    Log To Console    Discounted Price: ${discounted_price}

    ${discount}  Get Text    xpath=//span[@class="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage apex-savings-percentage"]
    Log To Console    Discount: ${discount}
    
    Scroll Element Into View    xpath=//input[@id="add-to-cart-button"]

    Click Element    xpath=//input[@id="add-to-cart-button"]

    Click Element    xpath=//a[@id="nav-cart"]
    Sleep    3s

    Page Should Contain    ${product_name}
    Sleep    2s

    Close Browser