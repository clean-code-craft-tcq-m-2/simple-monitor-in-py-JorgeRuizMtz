from DL_FunctionChecker import temp_is_ok, soc_is_ok, change_rate_is_ok, space

def battery_test(temperature, soc, charge_rate):
    print('')
    print('|','/'.center(space,'/'),'|','/'.center(space,'/'),'|')
    print('|',''.center(space),'|',''.center(space),'|')
    print('|','ENGLISH:'.center(space),'|', 'SPANISH:'.center(space),'|')
    print('|',' BATTERY STATUS REPORT: '.center(space,'.'),'|', ' REPORTE DE ESTADO DE LA BATERIA: '.center(space,'.'),'|')
    
    return (
        temp_is_ok(temperature), 
        soc_is_ok(soc), 
        change_rate_is_ok(charge_rate)
    )
   