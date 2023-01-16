from Data_limitsTemp import critical_temp, LOWwarning_temp, HIGHwarning_temp, nominal_temp, space
from Data_limitsSOC import critical_soc, LOWwarning_soc, HIGHwarning_soc, nominal_soc
from Data_limitsRate import critical_chargerate, LOWwarning_chargerate, HIGHwarning_chargerate, nominal_chargerate

def temp_data_Structurte(temp):
   
   critical_temp(temp)
   LOWwarning_temp(temp)
   HIGHwarning_temp(temp)
   nominal_temp(temp)
   
def soc_data_Structurte(Datasoc):
    critical_soc(Datasoc)
    LOWwarning_soc(Datasoc)
    HIGHwarning_soc(Datasoc)
    nominal_soc(Datasoc)

def ChargeRate_data_Structurte(charge_rate):
    critical_chargerate(charge_rate)
    LOWwarning_chargerate(charge_rate)
    HIGHwarning_chargerate(charge_rate)
    nominal_chargerate(charge_rate)