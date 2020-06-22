*** Settings ***
Resource          Common.robot
Suite Setup       Clear Database    ${SERVER}
Suite Teardown    Clear Database    ${SERVER}

*** Test Cases ***
Top Level Test Case 1
    Test Gql Query    test01.gql

