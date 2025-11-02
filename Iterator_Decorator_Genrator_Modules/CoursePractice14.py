import itertools
import operator

expert_List1 = [("Ali","Ahmadi","M",35),("Sima","Sadri","C",39),("Ahmad","Moradi","M",30), 
                ("Ftemeh","Majd","C",29),("Sara","Biglar","IE",27),("Reza","Rahnama","EE",45)]

expert_List2 = [("Mina","Gohari","EE",40),("Iman","Shams","M",26),("Farzad","Yeganeh","M",41),
                ("Ali","Imani","C",33),("Aref","Alameh","M",32),("Narges","Sohrabi","C",35)]

expert_List=[expert_List1,expert_List2]
total_List=list(itertools.chain.from_iterable(expert_List))
print(f'\nThe Result Of Total List:\n\n{total_List}')
print(155*'-')
sorted_List=sorted(total_List,key=operator.itemgetter(2))
print(f'The Result Of Sorted List:\n\n{sorted_List}')
print(155*'-')
math_List=list(itertools.compress(sorted_List,[0,0,0,0,0,0,0,1,1,1,1,1]))
print(f'The Result Of Math List:\n\n{math_List}')
print(155*'-')
com_list=list(itertools.combinations(math_List,3))
print(f'The result Of Combination List:\n\n{com_list}')
