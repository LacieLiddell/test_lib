.. code:: robotframework

*** Settings ***

Library     OperatingSystem
#Library     C:\\Users\\lacie\\PycharmProjects\\testLib\\
#Library     C:\\Users\\lacie\\PycharmProjects\\testLib\\testLib.py      with name   testlib
Library     ${libPath}
Default Tags    smoke
Test Setup      Log to console      connect
Test Teardown   Log to console      end


*** Variables ***
${getConfirm}
#${coreVersion}     ${1}
${libPath}    .\\library.py
${clientPath}       .\\client.py



*** Test Cases ***
Check core version
    Check


*** Keywords ***
Check
#    [Arguments]         ${coreVersion}
    ${getConfirm} =     Get Sw Version Test
#    Get SW Version Test
    Convert to integer   ${getConfirm}
    Should be equal      ${65553}      ${getConfirm}
    Log to console       ok