from Data_limitsTemp import space   
    
def critical_chargerate(ratedata):
    
    if ratedata == 0 :
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: LOW Charge rate has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de BAJA Tasa de Carga!'.center(space),'|')
        
    elif ratedata > 0.8:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: HIGH Charge rate has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de ALTa Tasa de Carga!'.center(space),'|')
 
def LOWwarning_chargerate(ratedata):
     if ratedata > 0 and ratedata <= 0.04:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Charge rate is getting LOW'.center(space),'|', '¡ADVERTENCIA!: La Tasa de Carga está BAJANDO'.center(space),'|')

def HIGHwarning_chargerate(ratedata):
     if ratedata >= 0.76 and ratedata <= 0.8:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Charge rate is getting HIGH'.center(space),'|', '¡ADVERTENCIA!: La Tasa de Carga está AUMENTANDO'.center(space),'|')
        
def nominal_chargerate(ratedata):
    
     if ratedata > 0.04 and ratedata <= 0.76:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Charge rate is Nominal'.center(space),'|', 'La Tasa de Carga es Nominal'.center(space),'|')