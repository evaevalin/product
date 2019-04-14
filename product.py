products = []
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


print(products)

for p in products:
    print(p[0], '價格是', p[1], '元')

#txt檔案
# with open('product.txt', 'w', encoding = ' utf-8') as f:
#     for p in products:
#         f.write(p[0]+','+ str(p[1]) + '\n')

#csv檔案 可以用excel開
with open('product.csv', 'w', encoding = ' utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0]+','+ str(p[1]) + '\n')
