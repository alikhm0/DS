q, p , x = map(int, input().split())

ice_cream = q // p
r = ice_cream
res = ice_cream
while (r != 0):
    r = ice_cream // x
    i = ice_cream % x
    ice_cream = r + i
    res =res + r

print(res)
    