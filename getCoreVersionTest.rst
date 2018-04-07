.. code:: robotframework



    *** Settings ***
    
    Library     OperatingSystem
    Library     C:\\Users\\lacie\\PycharmProjects\\test_lib\\testLib.py
    Default Tags    smoke
    Test Setup      Log to console      connect
    Test Teardown   Log to console      end
    
    
    *** Variables ***
    ${getConfirm}
    #${libPath}    C:\\Users\\lacie\\PycharmProjects\\test_lib\\test_lib.py
    

    *** Test cases ***
    Check core version
        Check
    
    *** Keywords ***
    Check
        ${getConfirm} =      Connect And Listen Core
		Log to console       ${getConfirm}  