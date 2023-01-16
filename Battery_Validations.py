from Battery_Tests import battery_test

test = battery_test


def battery_validation(test):

    if test== (True, True, True):
        print('Battery is working fine! \nAll is good.\n')

    elif test == (False, False, False):
        print('Check Temperature, State of Charge & Charge Rate. Note: Battery might be compromised and should be replaced. \n')
        
