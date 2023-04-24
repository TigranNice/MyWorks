import requests
import time

headers = {'Client-Id': '', 'Api-Key': ''}

with open('products.csv', 'r') as file:
    next(file)
    product_id = []
    for row in file:
        row = row.split(';')
        product = int(row[1][1:-1])
        product_id.append(product)

with open('ост2007.csv', 'r', encoding='windows-1251') as file:
    next(file)
    next(file)
    next(file)
    next(file)
    next(file)
    next(file)
    next(file)
    next(file)
    next(file)
    one_c = []
    one_c_id = []
    for row in file:
        row = row[:-14]
        row = row.split(';')
        one_c.append((row[0], row[-1]))
        one_c_id.append(row[0])

response = requests.post('https://api-seller.ozon.ru/v2/product/info/list', headers=headers,
                         json={"offer_id": [],
                               "product_id": product_id,
                               "sku": []
                               })
items = response.json()['result']['items']
sorted(items, key=lambda x: x['offer_id'])
number = int(input('Введите кол-во товара для презентации на сайте: '))
old_ost = []
false_position = []
for i in range(len(items)):
    try:
        if items[i]['stocks']['present'] < number:
            ind = one_c_id.index(items[i]['offer_id'])
            if int(one_c[ind][1]) >= 3 * number:
                old_ost.append((items[i]['offer_id'], items[i]['id'], items[i]['stocks']['present'], number))
                items[i]['stocks']['present'] = number
            elif items[i]['stocks']['present'] <= int(one_c[ind][1]) // 3:
                old_ost.append(
                    (items[i]['offer_id'], items[i]['id'], items[i]['stocks']['present'], int(one_c[ind][1]) // 3))
                items[i]['stocks']['present'] = int(one_c[ind][1]) // 3
            elif items[i]['stocks']['present'] > int(one_c[ind][1]) // 3:
                old_ost.append(
                    (items[i]['offer_id'], items[i]['id'], items[i]['stocks']['present'], int(one_c[ind][1]) // 3))
                items[i]['stocks']['present'] = int(one_c[ind][1]) // 3
    except:
        false_position.append(items[i]['offer_id'])

all_ost = []
ost = {
    "stocks": []
}
count = 1
for prod in old_ost:
    if count % 100 != 0:
        ost['stocks'].append(
            {'offer_id': prod[0], 'product_id': prod[1], 'stock': prod[3]})
        count += 1
    else:
        all_ost.append(ost)
        ost = {
            "stocks": []
        }
        ost['stocks'].append(
            {'offer_id': prod[0], 'product_id': prod[1], 'stock': prod[3]})
        count += 1

print(len(old_ost))
for i in old_ost:
    print(i)

for row in all_ost:
    response = requests.post('https://api-seller.ozon.ru/v1/product/import/stocks', headers=headers, json=row)
    print(response)

print('Поздравляю! Ваши остатки обновлены. Как говорится, сделал дело, гуляй смело))')
time.sleep(600)
