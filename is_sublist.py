def is_sublist(larger, smaller):
        if smaller == [] or larger == smaller:
              return True
        elif len(smaller) < len(larger):
              lst = []
              for ind in range(len(smaller)):
                    for ind1 in range(len(larger)):
                            if smaller[ind] == larger[ind1]:
                                  lst.append(ind)
                            else:
                                  continue
              if lst == []:
                  return False
              for ind in range(1, len(lst)):
                      if  lst[ind] - lst[ind - 1] != 1:
                            return False
                      else:
                           continue
              return True


print(is_sublist([13, 9, 21], [9]))
