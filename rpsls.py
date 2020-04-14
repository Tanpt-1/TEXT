#coding:gbk
"""
功能：石头剪刀布蜥蜴史波克游戏
作者：谭娉婷
日期：2020.3.30
"""

import random
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
	"""
    将游戏对象对应到不同的整数
    """
	n=name
	if n=="石头":
	   i=0
	elif n=="史波克":
	     i=1
	elif n=="纸":
	     i=2
	elif n=="蜥蜴":
	     i=3
	elif n=="剪刀":
	     i=4
	else:
	     print("Error: No Correct Name")
	     return i#返回数字
	
	
def number_to_name(number):#将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	p=number
	if p==0:
	   q="石头"
	elif p==1:
		 q="史波克"
	elif p==2:
		 q="纸"
	elif p==3:
		 q="蜥蜴"
	elif p==4:
		 q="剪刀"
	else:
		print("Error: No Correct Name")
	return q#返回文字


def rpsls(player_choice):
	choice=player_choice
	return choice


print("欢迎使用RPSLS游戏")
print("----------------")
choice=input("请输入您的选择:")
print("----------------")
import name_to_number#引用函数name_to_number
i=name_to_number.name_to_number(choice)
print("您的选择为:"+str(choice))
j=int(random.randint(0,4))
import number_to_name#引用函数number_to_name
q=number_to_name.number_to_name(j)
print("机器的选择为:"+str(q))


if j-i==4 or i-j==1 or j-i==3 or i-j==2:##j=4,i=0#i=1,j=0.i=2,j=1.i=3,j=2.i=4,j=3#j=3,i=0.j=4,i=1#i=2,j=0.i=3,j=1.i=4,j=2
   print("您赢了")
elif j-i==2 or i-j==3 or i-j==4or j-i==1:##j=2,i=0.j=3,i=1.j=4,i=2#i=3,j=0.i=4,j=1#i=4,j=0#j=1,i=0.j=2,i=1,j=3,i=2,j=4,i=3
	 print("机器赢了")
   
	
