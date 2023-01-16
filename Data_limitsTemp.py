space = 120

def critical_temp(tempdata):
    
    if tempdata < -20 or tempdata > 50:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: Temperature limit has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de Temperatura!'.center(space),'|')
        return True
        
    elif tempdata > -17.5 and tempdata < 47.5:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Temperature is Nominal'.center(space),'|', 'La Temperatura es Nominal'.center(space),'|')
        return True
        
def warning_temp(tempdata):
    
    if tempdata >= -20 and tempdata <= -17.5 or tempdata >= 47.5 and tempdata <= 50:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Temperature is changing'.center(space),'|', '¡ADVERTENCIA!: La temperatura está CAMBIANDO'.center(space),'|')
        
        
    elif tempdata > -17.5 and tempdata < 47.5:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Temperature is Nominal'.center(space),'|', 'La Temperatura es Nominal'.center(space),'|')
