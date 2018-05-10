.. code:: robotframework

*** Settings ***

Library     OperatingSystem
Library     ${libPath}
#Library     ${constPath}
Default Tags    smoke
Suite Setup    Connect
Suite Teardown      Disconnect
Test Setup      Log to console      connect
Test Teardown   Log to console      end


*** Variables ***
${obj}
${client}
${libPath}    .\\library.py
#${constPath}       .\\some components\\constants_table.py
${POWER_OFF}    ${0}
${POWER_ON}      ${1}
${FK_TMI1F23}     ${23}
${FK_BFKCF48}     ${48}
${FK_BFKSF49}     ${49}
${FK_VIP1F1}     ${1}
${FK_VIP2F3}     ${3}
${FK_VIP1NF2}     ${2}
${FK_VIP2NF4}     ${4}
${FK_BSTRF54}     ${54}
${FK_BSTOF55}     ${55}
${FK_BUDRF50}     ${50}
${FK_BUDOF51}     ${51}
${FK_BOPRF52}     ${52}
${FK_BOPOF53}     ${53}
${FK_RRF7}     ${7}
${FK_DRF8}     ${8}
${FK_VOF9}    ${9}
${FK_OOF10}     ${10}
${VOF19}     ${19}
${VO2F20}     ${20}



*** Test Cases ***
Check core version
    ${getConfirm} =     Get Sw Version Test
    Convert to integer   ${getConfirm}
    Log to console     ${getConfirm}
    Should be equal      ${65553}      ${getConfirm}


Check be version
    ${getConfirm} =     Get BE Version Test
    Convert to integer   ${getConfirm}
    Log to console     ${getConfirm}
    Should be equal      ${68551683}      ${getConfirm}

Check EM Power
    ${getConfirm} =     Check EM Power Supply
#    Convert to integer   ${getConfirm}
    Log to console     ${getConfirm}
#    Should be equal      ${68551683}      ${getConfirm}


Check VIP Change
    ${getTMI}   ${getState} =     Check Block Change  ${FK_VIP2F3}    ${FK_VIP1F1}
    Log to console  ${getTMI}
    Log to console  ${getState}

Check BFK Change
    [Template]  Block Change to "${fkOpposite}" from "${fkInit}"
    ${FK_BFKSF49} ${FK_BFKCF48}
#    Log to console      ok



#Check resources
#    ${obj}=     Connect
#    ${getConfirm}=      Check Inside Resources     ${obj}
#    Log to console      ${getConfirm}robo


*** Keywords ***
Block Change to "${fkOpposite}" from "${fkInit}"
#    [Arguments]     ${fkOpposite}   ${fkInit}
    ${getTMI}   ${getState} =     Check Block Change  ${fkOpposite}   ${fkInit}
    Log to console  ${getTMI}
    Log to console  ${getState}