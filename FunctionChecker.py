def temp_is_ok(temperature):
    if temperature < -20 or temperature > 50:
        print('Temperature is out of range!')
        print('Check battery temperature\n')
        return False
    else:
        return True

def soc_is_ok(soc):
    if soc < 20 or soc > 100:
        print('State of Charge is out of range!')
        print('Check State of charge\n')
        return False
    else:
        return True

def change_rate_is_ok(charge_rate):
    if charge_rate < 0 or charge_rate > 0.8:
        print('Charge rate is out of range!')
        print('Check Charge Rate\n')
        return False
    else:
        return True
    
