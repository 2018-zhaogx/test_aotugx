#！/usr/bin/python
#-*- coding:utf-8 -*-
product_list=[('小艾同学',299),('自行车',400),('苹果8',5000),('玩具枪',100)]
print(product_list)
salary=0 #余额
shopping_list=[] #购物车
while True:
    salary=input("请输入您的工资：")
    if(salary.isdigit()):
        salary=int(salary)
        while True:
            choose_id=input("请输入商品ID：,输入’q‘退出并结算")
            if choose_id.isdigit():  #是数字
                choose_id=int(choose_id)
                if(choose_id>=0 and choose_id<len(product_list)):
                    if salary>=product_list[choose_id][1]:
                        shopping_list.append(product_list[choose_id])
                        salary-=product_list[choose_id][1]
                    else:
                        print("您的余额不足！")
                else:
                    print("商品不存在")
            elif choose_id=='q':
                print("您购买的商品有：%s,您的余额为%s"%(shopping_list,salary))
                exit()
            else:
                print("商品ID格式不正确")
        break
    else:
        print("您的工资格式不正确！")
