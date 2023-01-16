from FunctionChecker import temp_is_ok, soc_is_ok, change_rate_is_ok


def battery_test(temperature, soc, charge_rate):
    return (
        temp_is_ok(temperature), 
        soc_is_ok(soc), 
        change_rate_is_ok(charge_rate)
    )
    
