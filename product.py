import os  #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename,'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格'in line:
                continue # 跳過下面 直接到下一回
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':   # q=quit
           break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name,  price])
    print(products)
    return products

    # p = []
        # p.append(name)
        # p.append(price)
        # products.append(p)

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '價格是', p[1], '元')
#txt檔案
# with open('product.txt', 'w', encoding = ' utf-8') as f:
#     for p in products:
#         f.write(p[0]+','+ str(p[1]) + '\n')

#csv檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = ' utf-8') as f:
        for p in products:
            f.write(p[0]+','+ str(p[1]) + '\n')



#此為主要執行function之執行碼 可以簡潔為一個function
def main():
    filename = 'products.csv'
    products = []
    if os.path.isfile(filename): #檢查答案在不在 有在繼續read_file
        print('yeah, 找到檔案囉')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)  
    print_products(products)
    write_file('products.csv', products) 

main()