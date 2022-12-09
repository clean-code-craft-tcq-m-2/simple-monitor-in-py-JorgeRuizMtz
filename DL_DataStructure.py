space = 120
def temp_data_Structurte(temp):
    
    if temp < -20:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: LOW temperature limit has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de BAJA Temperatura!'.center(space),'|')
        
    elif temp >= -20 and temp <= -17.5:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Temperature is getting LOW'.center(space),'|', '¡ADVERTENCIA!: La temperatura está BAJANDO'.center(space),'|')
        
    elif temp > -17.5 and temp < 47.5:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Temperature is Nominal'.center(space),'|', 'La Temperatura es Nominal'.center(space),'|')
        
    elif temp >= 47.5 and temp <= 50:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Temperature is getting HIGH'.center(space),'|', '¡ADVERTENCIA!: La temperatura está AUMENTANDO'.center(space),'|')
        
    elif temp > 50:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: HIGH Temperarute has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de ALTA Temperatura!'.center(space),'|')
        
    
def soc_data_Structurte(Datasoc):
    
    if Datasoc < 20:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: LOW State of Charge has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de BAJO Estado de Carga!'.center(space),'|')
        
    elif Datasoc >= 20 and Datasoc <= 24:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: State of Charge is getting LOW'.center(space),'|', '¡ADVERTENCIA!: El estado de Carga está BAJANDO'.center(space),'|')
        
    elif Datasoc > 24 and Datasoc < 75:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','State of Charge is Nominal'.center(space),'|', 'El Estado de Carga es Nominal'.center(space),'|')
        
    elif Datasoc >= 75 and Datasoc <= 80:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: State of Charge is getting HIGH'.center(space),'|', '¡ADVERTENCIA!: El Estado de Carga está AUMENTANDO'.center(space),'|')
        
    elif Datasoc > 80:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: HIGH State of Charge has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de ALTO Estado de Carga!'.center(space),'|')
        
        
def ChargeRate_data_Structurte(charge_rate):
    
    if charge_rate == 0 :
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: LOW Charge rate has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de BAJA Tasa de Carga!'.center(space),'|')
        
        
    elif charge_rate > 0 and charge_rate <= 0.04:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Charge rate is getting LOW'.center(space),'|', '¡ADVERTENCIA!: La Tasa de Carga está BAJANDO'.center(space),'|')

        
    elif charge_rate > 0.04 and charge_rate <= 0.76:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Charge rate is Nominal'.center(space),'|', 'La Tasa de Carga es Nominal'.center(space),'|')
        
    elif charge_rate >= 0.76 and charge_rate <= 0.8:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','Warning!: Charge rate is getting HIGH'.center(space),'|', '¡ADVERTENCIA!: La Tasa de Carga está AUMENTANDO'.center(space),'|')
        
    elif charge_rate > 0.8:
        print('|',''.center(space),'|',''.center(space),'|')
        print('|','DANGER!: HIGH Charge rate has been Breach!'.center(space),'|', '¡PELIGRO!: Se ha incumplido el límite de ALTa Tasa de Carga!'.center(space),'|')
        