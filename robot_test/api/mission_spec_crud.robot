*** Settings ***
Resource          ../Common.robot
Suite Setup       Clear Database    ${SERVER}
Suite Teardown    Clear Database    ${SERVER}

*** Test Cases ***
Create mission specs
    Test Gql Query    ${CURDIR}/ms_create01.gql

