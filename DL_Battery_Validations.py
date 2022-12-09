from DL_Battery_Tests import battery_test, space

test = battery_test

def battery_validation(test):

    if test== (True, True, True):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Battery is working fine!: All is good!'.ljust(space), '|','La Bateria esta trabajando bien!: ¡Todo esta correcto!'.ljust(space),'|')
    
    elif test == (False, True, True):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Check battery temperature'.ljust(space), '|','Revisar la temperatura de la Bateria'.ljust(space),'|')
    
    elif test == (True, False, True):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Check State of charge'.ljust(space), '|','Revisar el Estado de Carga'.ljust(space),'|')
        
    elif test == (True, True, False):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Check Charge Rate'.ljust(space), '|','Revisar Tasa de Carga'.ljust(space),'|')
        
    elif test == (False, False, True):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Check Temperature & State of Charge. Note: Battery might be compromised'.ljust(space), '|','Revisar Temperatura & Estado de Carga. Nota: La Bateria podria estar fallando'.ljust(space),'|')
    
    elif test == (True, False, False):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Check State of Charge & Charge Rate. Note: Battery might be compromised'.ljust(space), '|','Revisar Estado de carga & Tasa de Carga. Nota: La Bateria podria estar fallando'.ljust(space),'|')
        
    elif test == (False, True, False):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Check Temperature & Charge Rate. Note: Battery might be compromised'.ljust(space), '|','Revisar Temperatura & Tasa de Carga. Nota: La Bateria podria estar fallando'.ljust(space),'|')
    
    elif test == (False, False, False):
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','SUMMARY:'.ljust(space),'|','RESUMEN:'.ljust(space),'|')
        print('|','Check Temperature, State of Charge & Charge Rate. Note: Battery might be compromised and should be replaced.'.ljust(space), '|','Revisar Temperatura, Estado de Carga & Tasa de Carga. Nota: La Bateria podria estar fallando y debera ser templazada'.ljust(space),'|')
 
