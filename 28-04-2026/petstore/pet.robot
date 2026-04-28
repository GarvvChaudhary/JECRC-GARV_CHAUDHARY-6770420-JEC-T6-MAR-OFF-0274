*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           JSONLibrary

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/add_pet.json

    ${response}=  POST On Session  petapi  /pet  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Update Pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/update_pet.json

    ${response}=  PUT On Session  petapi  /pet  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Find Pet By Id
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  GET On Session  petapi  /pet/23

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Find Pet By Status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qp}=  Create Dictionary
    ...    status=available

    ${response}=  GET On Session  petapi  /pet/findByStatus  params=${qp}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Upload an Image
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=  Create Dictionary  additionalMetadata=piliya's image
    ${file_data}=  Set Variable  ${CURDIR}/../data/dogesh.jpg
    ${file}=  Evaluate    {'file': open('${file_data}', 'rb')}

    ${response}=  POST On Session  petapi  /pet/23/uploadImage
    ...    data=${form_data}
    ...    files=${file}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Update a pet with form data
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=  Create Dictionary  name=Rex  status=sold

    ${response}=  POST On Session  petapi  /pet/23
    ...    data=${form_data}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Delete a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  DELETE On Session  petapi  /pet/23

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}