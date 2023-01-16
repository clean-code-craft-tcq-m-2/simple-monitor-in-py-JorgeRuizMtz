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

