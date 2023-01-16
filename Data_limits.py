space = 120

def critical_temp(tempdata):
    
    if tempdata < -20:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: LOW temperature limit has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de BAJA Temperatura!'.center(space),'|')
    
    elif tempdata > 50:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: HIGH Temperarute has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de ALTA Temperatura!'.center(space),'|')
        
def warning_temp(tempdata):
    
    if tempdata >= -20 and tempdata <= -17.5:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Temperature is getting LOW'.center(space),'|', '¡ADVERTENCIA!: La temperatura está BAJANDO'.center(space),'|')
    
    elif tempdata >= 47.5 and tempdata <= 50:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Temperature is getting HIGH'.center(space),'|', '¡ADVERTENCIA!: La temperatura está AUMENTANDO'.center(space),'|')

def nominal_temp(tempdata):
    
    if tempdata > -17.5 and tempdata < 47.5:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Temperature is Nominal'.center(space),'|', 'La Temperatura es Nominal'.center(space),'|')
    
    
def critical_soc(socinfo):
    
     if socinfo < 20:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: LOW State of Charge has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de BAJO Estado de Carga!'.center(space),'|')
        
     elif socinfo > 80:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: HIGH State of Charge has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de ALTO Estado de Carga!'.center(space),'|')
        
def warning_soc(socinfo):
    
     if socinfo >= 20 and socinfo <= 24:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: State of Charge is getting LOW'.center(space),'|', '¡ADVERTENCIA!: El estado de Carga está BAJANDO'.center(space),'|')
        
     elif socinfo >= 75 and socinfo <= 80:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: State of Charge is getting HIGH'.center(space),'|', '¡ADVERTENCIA!: El Estado de Carga está AUMENTANDO'.center(space),'|')
        
def nominal_soc(socinfo):
     
     if socinfo > 24 and socinfo < 75:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','State of Charge is Nominal'.center(space),'|', 'El Estado de Carga es Nominal'.center(space),'|')
        