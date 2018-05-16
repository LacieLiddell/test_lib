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

#Check EM Power
#    ${getConfirm} =     Check EM Power Supply
##    Convert to integer   ${getConfirm}
#    Log to console     ${getConfirm}
##    Should be equal      ${68551683}      ${getConfirm}


Check VIP1 Change
    [Setup]     Set Config      ${FK_VIP1F1}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
    ${FK_VIP2F3}    ${FK_VIP1F1}  VIP1PT1

Check VIP2 Change
    [Setup]     Set Config  ${FK_VIP2F3}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
    ${FK_VIP1F1}    ${FK_VIP2F3}    VIP2PT2

Check BFK Change
    : FOR     ${initConfig}   IN RANGE  ${FK_VIP1F1}   ${FK_VIP2F3}
    \   Set Config  ${initConfig}
    \   Block Change to ${FK_BFKSF49} from ${FK_BFKCF48} and check SB1T25

Check BUSTRO Change
    [Setup]     Set Config      ${FK_BSTOF55}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
    ${FK_BSTRF54}    ${FK_BSTOF55}  SB4T28


Check BUSTRR Change
    [Setup]     Set Config      ${FK_BSTRF54}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
     ${FK_BSTOF55}  ${FK_BSTRF54}  SB4T28
#    : FOR     ${initConfig}   IN  ${FK_BSTOF55}   ${FK_BSTRF54}
#    \   Set Config  ${initConfig}
#    \   Run Keyword If  '${initConfig}' == '${FK_BSTOF55}'   Block Change to ${FK_BSTRF54} from ${FK_BSTOF55} and check SB4T28
#    \   Run Keyword If   '${initConfig}' == '${FK_BSTRF54}'   Block Change to ${FK_BSTOF55} from ${FK_BSTRF54} and check SB4T28


Check BUDO Change
    [Setup]     Set Config      ${FK_BUDOF51}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
    ${FK_BUDRF50}  ${FK_BUDOF51}  SB2T26


Check BUDR Change
    [Setup]     Set Config      ${FK_BUDRF50}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
    ${FK_BUDOF51}   ${FK_BUDRF50}  SB2T26


Check BPOPO Change
    [Setup]     Set Config      ${FK_BOPOF53}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
    ${FK_BOPRF52}  ${FK_BOPOF53}  SB3T27

Check BPOPR Change
    [Setup]     Set Config      ${FK_BOPRF52}
    [Template]  Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
    ${FK_BOPOF53}   ${FK_BOPRF52}  SB3T27
#    ${getTMI}   ${getState} =     Check Block Change  ${FK_BOPRF52}     ${FK_BOPOF53}
#    Log to console  ${getTMI}
#    Log to console  ${getState}



Check resources
    ${getConfirm}=      Check Inside Resources
    Log to console      ${getConfirm}
    Convert to number    ${getConfirm}
    Should be equal     ${getConfirm}   ${0.0}


*** Keywords ***
Block Change to ${fkOpposite} from ${fkInit} and check ${tmi}
#    [Arguments]     ${fkOpposite}   ${fkInit}
    ${getTMI}   ${getState} =     Check Block Change  ${fkOpposite}   ${fkInit}   ${tmi}
    Log to console  ${getTMI}
    Convert to number    ${getTMI}
    Log to console  ${getState}
    Convert to number    ${getState}
    Should be equal     ${getState}  ${getTMI}