fruitmand = { "appel":3, "banaan":5, "kers":50 }
print( fruitmand.keys() )
# Vul in --> return .keys():dict_keys(['appel', 'banaan', 'kers']) 
print( fruitmand.values() )
# Vul in --> return .values():dict_values([3, 5, 50])
print( fruitmand.items() )
# Vul in --> return .items(): dict_items([('appel', 3), ('banaan', 5), ('kers', 50)])

"""
Wat zijn de gelijkenissen van deze waarden met lijsten? Wat zijn de verschillen?
Hebben beide vierkante haakjes. 
"""

"""
Zijn deze waarden effectief lijsten? Hoe kan je dit testen?
Nee, hebben geen methodes die lijsten hebben.
"""

"""
Indien nee, is het mogelijk om deze waarden naar lijsten om te vormen?
Ja, via de typecasting funcite list().
"""