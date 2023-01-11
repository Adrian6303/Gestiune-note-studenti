def cmp(el1, el2, key):
    if key(el1)[0] < key(el2)[0]:
        return True
    elif key(el1)[0] == key(el2)[0]:
        if key(el1)[1] < key(el2)[1]:
            return True
        return False
    return False


def quick_sort(lst, key=None, reversed=False, cmp=None):
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
    pivot = lst[0]

    left = [x for x in lst[1:] if cmp(x, pivot, key)]
    right = [x for x in lst[1:] if cmp(x, pivot, key) == False]
    if not reversed:
        return quick_sort(left, key=key,cmp=cmp) + [lst[0]] + quick_sort(right, key=key, cmp=cmp)
    else:
        return quick_sort(right, key=key, reversed=True,cmp=cmp) + [lst[0]] + quick_sort(left, key=key, reversed=True, cmp=cmp)


def gnome_sort(lst, key=None, reversed=False, cmp=None):
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
        if i == 0 or cmp(lst[i-1], lst[i], key):
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    if reversed:
        lst.reverse()
    return lst
