# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start_1 = '01-02-2013'    
date_stop_1 = '07-28-2015'   

date_start_obj_1 = datetime.strptime(date_start_1, '%m-%d-%Y')
date_stop_obj_1 = datetime.strptime(date_stop_1, '%m-%d-%Y')
print(date_stop_obj_1 - date_start_obj_1)

####b)  
date_start_2 = '12312013'  
date_stop_2 = '05282015'  

date_start_obj_2 = datetime.strptime(date_start_2, '%m%d%Y')
date_stop_obj_2 = datetime.strptime(date_stop_2, '%m%d%Y')
print(date_stop_obj_2 - date_start_obj_2)

####c)  
date_start_3 = '15-Jan-1994'      
date_stop_3 = '14-Jul-2015'  

date_start_obj_3 = datetime.strptime(date_start_3, '%d-%b-%Y')
date_stop_obj_3 = datetime.strptime(date_stop_3, '%d-%b-%Y')
print(date_stop_obj_3 - date_start_obj_3)