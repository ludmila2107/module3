data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
count_ = 0
def calculate_structure_sum(*args):
    global count_
    for i in args:
        for j in i:
            if isinstance(j, int):
                count_+= j
            elif isinstance(j, dict):
                for v in j.values():
                    if type(v)==int:
                        count_+=v
                    elif type(v)==str:
                        count_ += len(v)
                for k in j.keys():
                    if type(k)==int:
                        count_+=k
                    elif type(k)==str:
                        count_ += len(k)
            elif isinstance(j, str):
                count_ += len(j)
            else:
                calculate_structure_sum(j)

    return count_




print(calculate_structure_sum(data_structure))
