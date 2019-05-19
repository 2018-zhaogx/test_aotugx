#！/usr/bin/python
#-*- coding:utf-8 -*-



# 购物车

# 功能要求：

# 用户登陆成功后要求用户输入总资产，例如：20000

# 显示商品列表，让用户根据序号选择商品，加入购物车购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。

# 附加：可充值、某商品移除购物车

goods = [
    {"name": "努比亚手机", "price": 1499},
    {"name": "小米笔记本电脑", "price": 4999},
    {"name": "Iphone X", "price": 7999},
    {"name": "手机壳", "price": 10},
    {"name": "笔记本外壳", "price": 99},
    {"name": "苹果笔记本电脑", "price": 11000},
]


user = 'knight'
pwd = 'dk123'
j = 1 # 将序列从1开始
b = [] # 用于添加序列，用户的购物车
p = {} # 存放序列和价格
n = {} # 存放序列和商品名
tag = True
while tag:
    username = input('Please enter the username:').strip()
    password = input('Please enter the password:')
    if username == user and password == pwd:
        print('Login successfully!')
        while True:
            user_money = input('Please enter your funds:').strip()
            if user_money.isdigit():
                user_money = int(user_money)
                break
            else:
                print('Please try again.')
        print('********Product List********')
        for i in goods:
            # print(i) # 得到每件商品的字典形式
            print(j,i['name'],i['price'])   # 打印序列，打印每件商品的商品名,打印每件商品的价格
            p[str(j)] = i['price']          # 为字典p添加商品的价格，key为序列，value为商品的价格
            n[str(j)] = i['name']           # 为字典n添加商品的名称，key为序列，value为商品名
            j += 1

        # print(p)
        # # 此时打印p字典得到{'1': 1499, '2': 4999, '3': 7999, '4': 10, '5': 99, '6': 11000}

        # print(n)
        # # 此时打印n字典得到
        # # {'1': '努比亚手机', '2': '小米笔记本电脑', '3': 'Iphone X', '4': '手机壳', '5': '笔记本外壳', '6': '苹果笔记本电脑'}
        print('Please select the product code added to your shopping cart(One at a time, press "7" to complete the selection)')

        while tag:
            user_select = input('Please enter the product code:').strip()
            if not user_select in ['1','2','3','4','5','6','7']:
                print('Please enter the correct product code')
                continue
            elif int(user_select) >= 0 and int(user_select) <=6:
                b.append(user_select)
                continue
            elif len(b) == 0:
                print('The shopping cart is empty')
                continue
            elif user_select == '7':
                while tag:
                    print('This is your shopping list:')
                    if b.count('1') != 0:
                        print('name:%s   number:%s   price:%s'%(n['1'],b.count('1'),b.count('1')*p['1']))
                    if b.count('2') != 0:
                        print('name:%s   number:%s   price:%s'%(n['2'],b.count('2'),b.count('2')*p['2']))
                    if b.count('3') != 0:
                        print('name:%s   number:%s   price:%s'%(n['3'],b.count('3'),b.count('3')*p['3']))
                    if b.count('4') != 0:
                        print('name:%s   number:%s   price:%s'%(n['4'],b.count('4'),b.count('4')*p['4']))
                    if b.count('5') != 0:
                        print('name:%s   number:%s   price:%s'%(n['5'],b.count('5'),b.count('5')*p['5']))
                    if b.count('6') != 0:
                        print('name:%s   number:%s   price:%s'%(n['6'],b.count('6'),b.count('6')*p['6']))


                    s = 0
                    for i in b:
                        s = s + p[i] # 此时的s为购买商品后的总价格
                    if s > user_money:
                        print('Sorry, your balance is not enough,still need ￥%s RMB,please select again.'%(s-int(user_money)))
                        while tag:
                            print('Press "a" to increase the money')
                            print('Press "d" to delete the product')
                            print('Press "q" to quit')
                            print('Press "r" to resubmit')
                            user_select2 = input('Please select:').strip()
                            if not user_select2 in ['a','d','q','r']:
                                print('Please enter again.')
                                continue

                            # 用户充值功能
                            if user_select2 == 'a':
                                while True:
                                    top_up = input('Please top-up:')
                                    if not top_up.isdigit():
                                        print('Try again')
                                        continue
                                    top_up = int(top_up)
                                    break

                                user_money = user_money + top_up
                                break

                            # 删除商品功能
                            if user_select2 == 'd':
                                while True:
                                    print('Your shopping list:')
                                    if b.count('1') != 0 :
                                        print('Number:1   Name:%s   Quantity:%s   Price:%s' % (n['1'], b.count('1'), b.count('1') * p['1']))
                                    if b.count('2') != 0 :
                                        print('Number:1   Name:%s   Quantity:%s   Price:%s' % (n['2'], b.count('2'), b.count('2') * p['2']))
                                    if b.count('3') != 0 :
                                        print('Number:1   Name:%s   Quantity:%s   Price:%s' % (n['3'], b.count('3'), b.count('3') * p['3']))
                                    if b.count('4') != 0 :
                                        print('Number:1   Name:%s   Quantity:%s   Price:%s' % (n['4'], b.count('4'), b.count('4') * p['4']))
                                    if b.count('5') != 0 :
                                        print('Number:1   Name:%s   Quantity:%s   Price:%s' % (n['5'], b.count('5'), b.count('5') * p['5']))
                                    if b.count('6') != 0 :
                                        print('Number:1   Name:%s   Quantity:%s   Price:%s' % (n['6'], b.count('6'), b.count('6') * p['6']))

                                    # 用户输入的钱减去购买商品后的钱。
                                    res1 = int(b.count('1') * p['1'])
                                    res2 = int(b.count('2') * p['2'])
                                    res3 = int(b.count('3') * p['3'])
                                    res4 = int(b.count('4') * p['4'])
                                    res5 = int(b.count('5') * p['5'])
                                    res6 = int(b.count('6') * p['6'])
                                    print('Your balance is ￥%s'%(user_money - res1 -res2 -res3 -res4 -res5 -res6))

                                    while True:
                                        goods_del = input('Please enter the code of the product you intend to delete,(Press "7" to end):').strip()
                                        if not goods_del.isdigit():
                                            print('Try again')
                                            continue
                                        goods_del = int(goods_del)
                                        break
                                    if goods_del == '7':
                                        print('End delete operation')
                                        break
                                    elif not goods_del in ['1','2','3','4','5','6','7'] or not user_money in b:
                                        print('Your shopping cart has no corresponding product!')
                                        continue
                                    elif goods_del >= 0 and goods_del <= 6:
                                        b.remove(goods_del)
                                        continue

                            # 重新提交功能
                            if user_select2 == 'r':
                                break

                            # 退出功能
                            if user_money == 'q':
                                tag = False
                            tag = False
                            print('Exit the purchase,Your balance is ￥%s'%user_money)
                    else:
                        print('The product was successfully added to the shopping cart,Your balance is ￥%s,'%(user_money - s))
                        while tag:
                            user_select3 = input('Press "y" to complete the purchase, continue to buy press "n",y/n:').strip()
                            if not user_select3 in ['y','n']:
                                print('Try again!')
                                continue
                            if user_select3 == 'y':
                                tag = False
                                print('End shopping')
                            if user_select3 == 'n':
                                break
                        tag = False

    else:
        print('Sorry,the username or password you entered is incorrect,please try again!')