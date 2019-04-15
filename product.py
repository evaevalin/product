import os  #operating system

#讀取檔案
def red_file(filename):
    products = []
    if os.path.isfile(filename):
        print('yeah, 找到檔案囉')
        with open(filename,'r', encoding = 'utf-8') as f:
            for line in f:
                if '商品,價格'in line:
                    continue # 跳過下面 直接到下一回
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    else:
        print('找不到檔案')
    return products #把products清單所有讀完的資料(name, price)回傳


#讓使用者輸入
def user_input(products):
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
    return(products)

#印出所有購買紀錄
def print_producs(products):
    for p in products:
        print(p[0], '價格是', p[1], '元')
#txt檔案
# with open('product.txt', 'w', encoding = ' utf-8') as f:
#     for p in products:
#         f.write(p[0]+','+ str(p[1]) + '\n')

#cvs檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = ' utf-8') as f:
        for p in products:
            f.write(p[0]+','+ str(p[1]) + '\n')

products = read_file('products.csv')
products =user_inpupt(products)
print_products(products)
products = write_file()