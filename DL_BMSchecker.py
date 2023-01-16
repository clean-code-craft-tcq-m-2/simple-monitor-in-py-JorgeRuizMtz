from DL_Battery_Tests import battery_test
from DL_Battery_Validations import AllBad_battery_validation, Onefalse_battery_validation, Onetrue_battery_validation, AllGood_battery_validation, MiddleFMiddleT_battery_validation

def battery_validation(Measure):
    AllBad_battery_validation(Measure)
    Onefalse_battery_validation(Measure)
    MiddleFMiddleT_battery_validation(Measure)
    Onetrue_battery_validation(Measure)
    AllGood_battery_validation(Measure)
        
if __name__ == '__main__':
    
    battery_validation(battery_test(15, 30, 0.5))
    battery_validation(battery_test(80, 85, 0.7))
    battery_validation(battery_test(50, 110, 0.7))
    battery_validation(battery_test(50, 85, 0.9))
    battery_validation(battery_test(80, 110, 0.7))
    battery_validation(battery_test(50, 110, 0.9))
    battery_validation(battery_test(80, 85, 0.9))
    battery_validation(battery_test(80, 110, 0.9))    
    assert(battery_test(25, 70, 0.7)) == (True, True, True) 
    ##assert(battery_test(50, 85, 0)) == (True, True, True)
    
