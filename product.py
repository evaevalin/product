import os  #operating system

products = []
if os.path.isfile('products.csv'):
    print('yeah, 找到檔案囉')
    with open('product.csv', 'w', encoding = ' utf-8') as f:
        f.write('商品,價格\n')
        for p in products:     #每個商品
            f.write(p[0]+','+ str(p[1]) + '\n')
else:
    print('找不到檔案')

#寫入檔案， 可以用excel開



#讀取檔案
with open('product.csv','r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格'in line:
            continue # 跳過下面 直接到下一回
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':   # q=quit
       break
    price = input('請輸入商品價格: ')
    price = int(price)
    # p = []
    # p.append(name)
    # p.append(price)
    # products.append(p)

    products.append([name,  price])

#印出所有購買商品紀錄
print(products)
for p in products:
    print(p[0], '價格是', p[1], '元')

#txt檔案
# with open('product.txt', 'w', encoding = ' utf-8') as f:
#     for p in products:
#         f.write(p[0]+','+ str(p[1]) + '\n')


