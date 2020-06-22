*** Settings ***
Library           OperatingSystem
Library           lib/GqlLibrary.py

*** Variables ***
${SERVER}               127.0.0.1

*** Keywords ***
Test Gql Query 
    [Arguments]    ${GQLFILE}
    Run Gql Query   ${SERVER}    ${GQLFILE}
    Status Should Be    response matched expected
 
