from Data_limitsTemp import space

def critical_soc(socinfo):
    
     if socinfo < 20:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: LOW State of Charge has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de BAJO Estado de Carga!'.center(space),'|')
        
     elif socinfo > 80:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: HIGH State of Charge has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de ALTO Estado de Carga!'.center(space),'|')
        
def LOWwarning_soc(socinfo):
    
     if socinfo >= 20 and socinfo <= 24:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: State of Charge is getting LOW'.center(space),'|', '¡ADVERTENCIA!: El estado de Carga está BAJANDO'.center(space),'|')
        
def HIGHwarning_soc(socinfo):
        
     if socinfo >= 75 and socinfo <= 80:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: State of Charge is getting HIGH'.center(space),'|', '¡ADVERTENCIA!: El Estado de Carga está AUMENTANDO'.center(space),'|')
        
def nominal_soc(socinfo):
     
     if socinfo > 24 and socinfo < 75:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','State of Charge is Nominal'.center(space),'|', 'El Estado de Carga es Nominal'.center(space),'|')