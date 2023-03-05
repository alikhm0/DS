input_line_number = int(input())

products = {}
for i in range(input_line_number):
    line = {}
    input_line = input().split()
    # print(input_line)
    line['type'] = input_line[0]
    line['color'] = input_line[1]
    line['price'] = int(input_line[2])
    line['model'] = input_line[3]
    products[i] = line
# print(products)

pirahan,kapshen,shalvar,joorab=0,0,0,0
for i in range(input_line_number):
    if products[i]['type'] == 'pirahan':
        if products[i]['price'] >= 200000 and products[i]['price'] <= 700000 :
            if products[i]['model'] == 'sadeh':
                pirahan = pirahan +1
    if products[i]['type'] == 'kapshen':
        if products[i]['color'] == 'meshki':
            if products[i]['price']  <= 2000000 :
                if products[i]['model'] == 'charm':
                    kapshen = kapshen +1
    if products[i]['type'] == 'shalvar':
        if products[i]['color'] == 'sabz' or products[i]['color'] == 'khakestari':
            if products[i]['price'] >= 400000 and products[i]['price'] <= 1000000 :
                if products[i]['model'] == 'katan' or products[i]['model'] == 'jean':
                    shalvar = shalvar +1
    if products[i]['type'] == 'joorab':
        if products[i]['color'] == 'sefid':
            if products[i]['model'] == 'nakhi':
                joorab = joorab +1

print(pirahan)
print(kapshen)
print(shalvar)
print(joorab)