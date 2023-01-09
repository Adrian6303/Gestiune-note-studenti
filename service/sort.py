def quick_sort(lst, key=None, reversed=False):
    '''
        Complexitate:

        caz favorabil: O(n*log(n)) , elementele sunt deja sortate
        caz nefavorabil: O(n^2) , elementele sunt sortate in ordine inversa
        caz mediu/general: O(n*log(n)), elementele sunt aranjate aleatoriu, complexitate medie
    '''
    if key is None:
        key = lambda x: x
    if len(lst) <= 1:
        return lst
    pivot = key(lst[0])
    left = [x for x in lst[1:] if key(x) < pivot]
    right = [x for x in lst[1:] if key(x) >= pivot]
    if not reversed:
        return quick_sort(left, key=key) + [lst[0]] + quick_sort(right, key=key)
    else:
        return quick_sort(right, key=key, reversed=True) + [lst[0]] + quick_sort(left, key=key, reversed=True)


def gnome_sort(lst, key=None, reversed=False):
    '''
        Complexitate:

        caz favorabil: O(n) , elementele sunt deja sortate
        caz nefavorabil: O(n^2) , elementele sunt sortate in ordine inversa
        caz mediu/general: O(n^2), elementele sunt aranjate aleatoriu, complexitate medie
    '''
    if key is None:
        key = lambda x: x
    i = 0
    while i < len(lst):
        if i == 0 or key(lst[i]) >= key(lst[i-1]):
            i += 1
        else:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
    if reversed:
        lst.reverse()
    return lst

