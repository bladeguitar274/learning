""" 
Materials
    tbf = 2" x 4" x 8' Framing pine studs
    ply = 1/2" x 4' x 8' Plywood sheet
    mdf = 1/2" x 4' x 8' MDF Sheet
Stores
    hd = Home Depot
    l = Lowes
    m = menards 
Costs
    h
        tbf=7.50
        ply=50
        mdf=48
    l
        tbf=7.50
        ply=60
        mdf=50
    m
        tbf=8
        ply=44
        mdf=48
"""
'''
End goal
take inputs
calulate out totals per store and print total pricing per store
maybe breakout per item but meh
'''


tbf_amount = int(input("How many 2 x 4 x 8's do you need? "))
ply_amount = int(input('How many full sheets of 1/2" plywood do you need? '))
mdf_amount = int(input('How many full sheets of 1/2" MDF do you need? '))


#dict
Costs = {
    'h' : {
        'tbf':7.50,
        'ply':50,
        'mdf':48
    },
    'l' : {
        'tbf':7.50,
        'ply':60,
        'mdf':50
    },
    'm' : {
        'tbf':8,
        'ply':44,
        'mdf':48
    }
}
Costsh = (
    (Costs['h']['tbf'] * tbf_amount) + (Costs['h']['ply'] * ply_amount) + (Costs['h']['mdf'] * mdf_amount)
)
Costsl = (
    (Costs['l']['tbf'] * tbf_amount) + (Costs['l']['ply'] * ply_amount) + (Costs['l']['mdf'] * mdf_amount)
)
Costsm = (
    (Costs['m']['tbf'] * tbf_amount) + (Costs['m']['ply'] * ply_amount) + (Costs['m']['mdf'] * mdf_amount)
)
print('Total at Home Depot $' + str(Costsh))
#print(Costs['h']['tbf'] * tbf_amount)
#print(Costs['h']['ply'] * ply_amount)
#print(Costs['h']['mdf'] * mdf_amount)
print('Total at Lowes $' + str(Costsl)) 
print('Total at Menards $' + str(Costsm))
