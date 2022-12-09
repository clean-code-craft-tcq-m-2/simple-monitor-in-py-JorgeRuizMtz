from DL_DataStructure import temp_data_Structurte, soc_data_Structurte, ChargeRate_data_Structurte,  space

def temp_is_ok(temperature):
    
    temp_data_Structurte(temperature)
    
    if temperature < -20 or temperature > 50:
        print('|','-'.center(space,'-'),'|','-'.center(space,'-'),'|')
        print('|',' Temperature is out of range! '.center(space,'*'), '|',' La Temperatura esta fuera del Rango! '.center(space,'*'),'|')
        print('|','-'.center(space,'-'),'|','-'.center(space,'-'),'|')
        
        return False
    else:
        return True

def soc_is_ok(soc):
    
    soc_data_Structurte(soc)
    
    if soc < 20 or soc > 80:
        print('|','-'.center(space,'-'),'|','-'.center(space,'-'),'|')
        print('|',' State of Charge is out of range! '.center(space,'*'), '|',' El estado de Carga esta fuera del Rango! '.center(space,'*'),'|')
        print('|','-'.center(space,'-'),'|','-'.center(space,'-'),'|')
        
        return False
    else:
        return True

def change_rate_is_ok(charge_rate):
    
    ChargeRate_data_Structurte(charge_rate)
    
    if charge_rate <= 0 or charge_rate > 0.8:
        print('|','-'.center(space,'-'),'|','-'.center(space,'-'),'|')
        print('|',' Charge rate is out of range! '.center(space,'*'), '|',' La Tasa de Carga esta fuera del Rango! '.center(space,'*'),'|')
        print('|','-'.center(space,'-'),'|','-'.center(space,'-'),'|')

        return False
    else:
        return True
    