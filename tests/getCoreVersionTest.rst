.. code:: robotframework



    *** Settings ***
	
    Library     OperatingSystem
    Library     C:\\Users\\lacie\\PycharmProjects\\test_lib\\test_lib.py
    Default Tags    smoke
    Test Setup      Log to console      start
                    Connect
    Test Teardown   Log to console      end
    
     #*** Variables ***
    #${libPath}    C:\\Users\\lacie\\PycharmProjects\\test_lib\\test_lib.py
    

    
    
    *** Keywords ***
    Connect
        Connect And Listen Core
        
