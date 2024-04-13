FEDERAL_TAXATION = {
'FICA': 0.0765,                      # Share of a Gross_salary
'Federal_standard_deduction': 13200,'Federal_tax_brackets': [
(11000, 0.10),
(44725, 0.12),
(95375, 0.22),
(182100, 0.24),
(231250, 0.32),
(578125, 0.35),
(1E12, 0.37)
]}
STATES_TAXATION = {
 'California': {'State_standard_deduction': 4609, 'State_tax_brackets':[
(10412, 0.01),
(24684, 0.02),
(38959, 0.04),
(54081, 0.06),
(68350, 0.08),
(349137, 0.093),
(418961, 0.103),
(698271, 0.113),
(1E12, 0.123),
]},
 'New York': {'State_standard_deduction': 8000, 'State_tax_brackets':[
(8500, 0.04),
(11700, 0.045),
(13900, 0.0525),
(21400, 0.059),
(80650, 0.0645),
(215400, 0.0685),
(1077550, 0.0882),
(5000000, 0.0965),
(25000000, 0.103),
(1E12, 0.109)
]},
'Colorado': {'State_standard_deduction': 0, 'State_tax_brackets':[(1E12, 0.045),]},
'Texas': {'State_standard_deduction': 0, 'State_tax_brackets':[(1E12, 0),]}}
#'Illinois': {'State_standard_deduction': 0, 'State_tax_brackets':[(1E12, 0.0495),]},

CITIES_TAXATION = {
'New York': {'City_standard_deduction': 0, 'City_tax_brackets':[
(12000, 0.03078),
(25000, 0.03762),
(50000, 0.03819),
(1E12, 0.03876)
]},
'Chicago': {'City_standard_deduction': 0, 'City_tax_brackets':[(1E12, 0),]},
'Los Angeles': {'City_standard_deduction': 0, 'City_tax_brackets':[(1E12, 0),]},
'Dallas': {'City_standard_deduction': 0, 'City_tax_brackets':[(1E12, 0),]},
'Atlanta': {'City_standard_deduction': 0, 'City_tax_brackets':[(1E12, 0),]},
}        

import pickle

def usa_taxation_stats(Federal, States, Cities):  
        f = open(r"usa_taxation.txt", "wb")
        obj1 = FEDERAL_TAXATION
        obj2 = STATES_TAXATION
        obj3 = CITIES_TAXATION
        pickle.dump(obj1, f)
        pickle.dump(obj2, f)
        pickle.dump(obj3, f)
        f.close()

usa_taxation_stats(FEDERAL_TAXATION, STATES_TAXATION, CITIES_TAXATION)