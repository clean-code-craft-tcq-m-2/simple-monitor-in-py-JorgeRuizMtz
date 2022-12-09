from Battery_Tests import battery_test

test = battery_test


def battery_validation(test):

    if test== (True, True, True):
        print('Battery is working fine! \nAll is good.\n')
    
    elif test == (False, True, True):
        print('Check battery temperature\n')
    
    elif test == (True, False, True):
        print('Check State of charge\n')
        
    elif test == (True, True, False):
        print('Check Charge Rate\n')
        
    elif test == (False, False, True):
        print('Check Temperature & State of Charge. Note: Battery might be compromised\n')
    
    elif test == (True, False, False):
        print('Check State of Charge & Charge Rate. Note: Battery might be compromised\n')
        
    elif test == (False, True, False):
        print('Check Temperature & Charge Rate. Note: Battery might be compromised\n')
    
    elif test == (False, False, False):
        print('Check Temperature, State of Charge & Charge Rate. Note: Battery might be compromised and should be replaced. \n')
        
