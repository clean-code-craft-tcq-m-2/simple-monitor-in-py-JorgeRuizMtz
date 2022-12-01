from Battery_Tests import battery_test
from Battery_Validations import battery_validation

        
if __name__ == '__main__':
    

    battery_validation(battery_test(25, 70, 0.7))
    battery_validation(battery_test(80, 85, 0.7))
    battery_validation(battery_test(50, 110, 0.7))
    battery_validation(battery_test(50, 85, 0.9))
    battery_validation(battery_test(80, 110, 0.7))
    battery_validation(battery_test(50, 110, 0.9))
    battery_validation(battery_test(80, 85, 0.9))
    battery_validation(battery_test(80, 110, 0.9))
    
    assert(battery_test(25, 70, 0.7)) == (True, True, True) 
    assert(battery_test(50, 85, 0)) == (True, True, True)
