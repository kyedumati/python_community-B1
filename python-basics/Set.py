ls = [10,2,2,3]
print(ls[0])

set_values = {"java","python",100,20,30}
print(set_values)
# print(set_values[0])   # indexerror
set_values.add(200)
set_values.add(200)
# set_values.clear()
# set_values = set()
# set_values.remove(100)
set_values2 = {100,400}
print("before update ",set_values)
set_values.update(set_values2)
print("after update ",set_values)

