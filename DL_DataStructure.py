from Data_limits import critical_temp, warning_temp, nominal_temp, critical_soc, warning_soc, nominal_soc, critical_chargerate, warning_chargerate, nominal_chargerate, space

def temp_data_Structurte(temp):
    
    critical_temp(temp)
    warning_temp(temp)
    nominal_temp(temp)
    
def soc_data_Structurte(Datasoc):
    
    critical_soc(Datasoc)
    warning_soc(Datasoc)
    nominal_soc(Datasoc)
   
def ChargeRate_data_Structurte(charge_rate):
    
    critical_chargerate(charge_rate)
    warning_chargerate(charge_rate)
    nominal_chargerate(charge_rate)
    