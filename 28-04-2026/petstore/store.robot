*** Settings ***

Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Pet Inventories
    [Documentation]    Get pet inventories by status
    Create Session    petapi    ${BASE_URL}  verify=True

    ${response}=    GET On Session    petapi    /store/inventory

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}

    Log To Console    ${body}
    Log To Console    ${response.status_code}

Place Order
    [Documentation]    Place an order for a pet
    Create Session    petapi    ${BASE_URL}  verify=True

    ${payload}=  Create Dictionary
    ...    id=12345
    ...    petId=54321
    ...    quantity=1
    ...    shipDate=2026-04-28T06:59:40.934Z
    ...    status=placed
    ...    complete=true

    ${response}=    POST On Session    petapi    /store/order    json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}

    Should Be Equal As Integers    ${body}[id]    12345
    Should Be Equal As Strings    ${body}[status]    placed

    Log To Console    ${body}
    Log To Console    ${response.status_code}

    Set Suite Variable    ${ORDER_ID}   ${body}[id]

Find Order By Id
    [Documentation]    Find order by ID
    Create Session    petapi    ${BASE_URL}  verify=True

    ${response}=    GET On Session    petapi    /store/order/${ORDER_ID}

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}

    Should Be Equal As Integers    ${body}[id]    12345

    Log To Console    ${body}
    Log To Console    ${response.status_code}

E2E
    Create Session    e2eapi    ${BASE_URL}  verify=True
    ${payload}=  Create Dictionary
    ...    id=18
    ...    petId=54
    ...    quantity=1
    ...    shipDate=2026-04-28T06:59:40.934Z
    ...    status=placed
    ...    complete=true

    ${res1}=    POST On Session    e2eapi    /store/order    json=${payload}

    Should Be Equal As Integers    ${res1.status_code}    200

    ${body}=    Set Variable    ${res1.json()}
    Set Suite Variable    ${ORDER_ID}    ${body}[id]

    Log To Console    Created an order

    ${res2}=    GET On Session    e2eapi    /store/order/${ORDER_ID}

    Should Be Equal As Integers    ${res2.status_code}    200

    Log To Console    Got the order by ID

    ${res3}=    DELETE On Session    e2eapi    /store/order/${ORDER_ID}

    Should Be Equal As Integers    ${res3.status_code}    200

    Log To Console    e2e successful
