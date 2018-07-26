

# """Q1 精简版蜘蛛
#
#  
#  3  ----          ----  1
#    | 12 |        | 04 |
#     ---- -------- ----
#         | 14  06 |
#         |        |
#         | 08  00 |
#     ---- -------- ----
#    | 10 |        | 02 |
#  4  ----          ----  2
#  
#
#
# """






#These are PSX button constants
PSB_SELECT      = const(0x0001)
PSB_L3          = const(0x0002)
PSB_R3          = const(0x0004)
PSB_START       = const(0x0008)
PSB_PAD_UP      = const(0x0010)
PSB_PAD_RIGHT   = const(0x0020)
PSB_PAD_DOWN    = const(0x0040)
PSB_PAD_LEFT    = const(0x0080)
PSB_L2          = const(0x0100)
PSB_R2          = const(0x0200)
PSB_L1          = const(0x0400)
PSB_R1          = const(0x0800)
PSB_GREEN       = const(0x1000)
PSB_RED         = const(0x2000)
PSB_BLUE        = const(0x4000)
PSB_PINK        = const(0x8000)
PSB_TRIANGLE    = const(0x1000)
PSB_CIRCLE      = const(0x2000)
PSB_CROSS       = const(0x4000)
PSB_SQUARE      = const(0x8000)
PSB_ALLKEY      = const(0xFFFF)

















# standBy 待机
#Servo_Prg_1_Step = 2;
Servo_Prg_1 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    90,   90,   90,   90,   90,   90,   90,   90,  500  ), # servo center point
  (    70,   90,   90,  110,  110,   90,   90,   70,  500  ), # standby
];
#Servo_List_Run(Servo_Prg_1);#测试


# Forward 前行
#Servo_Prg_2_Step = 11;
Servo_Prg_2 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    90,   90,   90,  110,  110,   90,   45,   90,  200  ), # leg1,4 up; leg4 fw
  (    70,   90,   90,  110,  110,   90,   45,   70,  200  ), # leg1,4 dn
  (    70,   90,   90,   90,   90,   90,   45,   70,  200  ), # leg2,3 up
  (    70,   45,  135,   90,   90,   90,   90,   70,  200  ), # leg1,4 bk; leg2 fw
  (    70,   45,  135,  110,  110,   90,   90,   70,  200  ), # leg2,3 dn
  (    90,   90,  135,  110,  110,   90,   90,   90,  200  ), # leg1,4 up; leg1 fw
  (    90,   90,   90,  110,  110,  135,   90,   90,  200  ), # leg2,3 bk
  (    70,   90,   90,  110,  110,  135,   90,   70,  200  ), # leg1,4 dn
  (    70,   90,   90,  110,   90,  135,   90,   70,  200  ), # leg3 up
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # leg3 fw dn
];
#Servo_List_Run(Servo_Prg_2);#测试


# Backward 退後
#Servo_Prg_3_Step = 11;
Servo_Prg_3 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    90,   45,   90,  110,  110,   90,   90,   90,  200  ), # leg4,1 up; leg1 fw
  (    70,   45,   90,  110,  110,   90,   90,   70,  200  ), # leg4,1 dn
  (    70,   45,   90,   90,   90,   90,   90,   70,  200  ), # leg3,2 up
  (    70,   90,   90,   90,   90,  135,   45,   70,  200  ), # leg4,1 bk; leg3 fw
  (    70,   90,   90,  110,  110,  135,   45,   70,  200  ), # leg3,2 dn
  (    90,   90,   90,  110,  110,  135,   90,   90,  200  ), # leg4,1 up; leg4 fw
  (    90,   90,  135,  110,  110,   90,   90,   90,  200  ), # leg3,1 bk
  (    70,   90,  135,  110,  110,   90,   90,   70,  200  ), # leg4,1 dn
  (    70,   90,  135,   90,  110,   90,   90,   70,  200  ), # leg2 up
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # leg2 fw dn
];
#Servo_List_Run(Servo_Prg_3);#测试


# Left shift 左移
#Servo_Prg_4_Step = 11;
Servo_Prg_4 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    70,   90,   45,   90,   90,   90,   90,   70,  200  ), # leg3,2 up; leg2 fw
  (    70,   90,   45,  110,  110,   90,   90,   70,  200  ), # leg3,2 dn
  (    90,   90,   45,  110,  110,   90,   90,   90,  200  ), # leg1,4 up
  (    90,  135,   90,  110,  110,   45,   90,   90,  200  ), # leg3,2 bk; leg1 fw
  (    70,  135,   90,  110,  110,   45,   90,   70,  200  ), # leg1,4 dn
  (    70,  135,   90,   90,   90,   90,   90,   70,  200  ), # leg3,2 up; leg3 fw
  (    70,   90,   90,   90,   90,   90,  135,   70,  200  ), # leg1,4 bk
  (    70,   90,   90,  110,  110,   90,  135,   70,  200  ), # leg3,2 dn
  (    70,   90,   90,  110,  110,   90,  135,   90,  200  ), # leg4 up
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # leg4 fw dn
];
#Servo_List_Run(Servo_Prg_4);#测试


# Right shift 右移
#Servo_Prg_5_Step = 11;
Servo_Prg_5 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    70,   90,   90,   90,   90,   45,   90,   70,  200  ), # leg2,3 up; leg3 fw
  (    70,   90,   90,  110,  110,   45,   90,   70,  200  ), # leg2,3 dn
  (    90,   90,   90,  110,  110,   45,   90,   90,  200  ), # leg4,1 up
  (    90,   90,   45,  110,  110,   90,  135,   90,  200  ), # leg2,3 bk; leg4 fw
  (    70,   90,   45,  110,  110,   90,  135,   70,  200  ), # leg4,1 dn
  (    70,   90,   90,   90,   90,   90,  135,   70,  200  ), # leg2,3 up; leg2 fw
  (    70,  135,   90,   90,   90,   90,   90,   70,  200  ), # leg4,1 bk
  (    70,  135,   90,  110,  110,   90,   90,   70,  200  ), # leg2,3 dn
  (    90,  135,   90,  110,  110,   90,   90,   70,  200  ), # leg1 up
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # leg1 fw dn
];
#Servo_List_Run(Servo_Prg_5);#测试


# Turn left 左轉leg
#Servo_Prg_6_Step = 8;
Servo_Prg_6 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    90,   90,   90,  110,  110,   90,   90,   90,  200  ), # leg1,4 up
  (    90,  135,   90,  110,  110,   90,  135,   90,  200  ), # leg1,4 turn
  (    70,  135,   90,  110,  110,   90,  135,   70,  200  ), # leg1,4 dn
  (    70,  135,   90,   90,   90,   90,  135,   70,  200  ), # leg2,3 up
  (    70,  135,  135,   90,   90,  135,  135,   70,  200  ), # leg2,3 turn
  (    70,  135,  135,  110,  110,  135,  135,   70,  200  ), # leg2,3 dn
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # leg1,2,3,4 turn
];
#Servo_List_Run(Servo_Prg_6);#测试


# Turn right 右轉
#Servo_Prg_7_Step = 8;
Servo_Prg_7 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    70,   90,   90,   90,   90,   90,   90,   70,  200  ), # leg2,3 up
  (    70,   90,   45,   90,   90,   45,   90,   70,  200  ), # leg2,3 turn
  (    70,   90,   45,  110,  110,   45,   90,   70,  200  ), # leg2,3 dn
  (    90,   90,   45,  110,  110,   45,   90,   90,  200  ), # leg1,4 up
  (    90,   45,   45,  110,  110,   45,   45,   90,  200  ), # leg1,4 turn
  (    70,   45,   45,  110,  110,   45,   45,   70,  200  ), # leg1,4 dn
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # leg1,2,3,4 turn
];
#Servo_List_Run(Servo_Prg_7);#测试


# Lie 趴地
#Servo_Prg_8_Step = 1;
Servo_Prg_8 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (   110,   90,   90,   70,   70,   90,   90,  110,  500  ), # leg1,4 up
];
#Servo_List_Run(Servo_Prg_8);#测试


# Say Hi 打招呼
#Servo_Prg_9_Step = 7;
Servo_Prg_9 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg2,3,4 dn
  (   170,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg1 up
  (   170,  130,   90,   90,   90,   90,   90,   90,  400  ), # leg1 left
  (   170,   50,   90,   90,   90,   90,   90,   90,  400  ), # leg1 right
  (   170,  130,   90,   90,   90,   90,   90,   90,  400  ), # leg1 left
  (   170,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg1 right
  (    70,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg1 dn
];
#Servo_List_Run(Servo_Prg_9);#测试


# Fighting 戰鬥姿態
#Servo_Prg_10_Step = 11;
Servo_Prg_10 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (   120,   90,   90,  110,   60,   90,   90,   70,  500  ), # leg1, 2 down
  (   120,   70,   70,  110,   60,   70,   70,   70,  500  ), # body turn left
  (   120,  110,  110,  110,   60,  110,  110,   70,  500  ), # body turn right
  (   120,   70,   70,  110,   60,   70,   70,   70,  500  ), # body turn left
  (   120,  110,  110,  110,   60,  110,  110,   70,  500  ), # body turn right
  (    70,   90,   90,   70,  110,   90,   90,  110,  500  ), # leg1, 2 up ; leg3, 4 down
  (    70,   70,   70,   70,  110,   70,   70,  110,  500  ), # body turn left
  (    70,  110,  110,   70,  110,  110,  110,  110,  500  ), # body turn right
  (    70,   70,   70,   70,  110,   70,   70,  110,  500  ), # body turn left
  (    70,  110,  110,   70,  110,  110,  110,  110,  500  ), # body turn right
  (    70,   90,   90,   70,  110,   90,   90,  110,  500  )  # leg1, 2 up ; leg3, 4 down
];
#Servo_List_Run(Servo_Prg_10);#测试


# Push up 掌上壓
#Servo_Prg_11_Step = 11;
Servo_Prg_11 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  500  ), # start
  (   100,   90,   90,   80,   80,   90,   90,  100,  600  ), # down
  (    70,   90,   90,  110,  110,   90,   90,   70,  700  ), # up
  (   100,   90,   90,   80,   80,   90,   90,  100,  800  ), # down
  (    70,   90,   90,  110,  110,   90,   90,   70,  900  ), # up
  (   100,   90,   90,   80,   80,   90,   90,  100, 1500  ), # down
  (    70,   90,   90,  110,  110,   90,   90,   70, 2000  ), # up
  (   135,   90,   90,   45,   45,   90,   90,  135,  200  ), # fast down
  (    70,   90,   90,   45,   60,   90,   90,  135,  800  ), # leg1 up
  (    70,   90,   90,   45,  110,   90,   90,  135,  800  ), # leg2 up
  (    70,   90,   90,  110,  110,   90,   90,   70,  800  )  # leg3, leg4 up
];
#Servo_List_Run(Servo_Prg_11);#测试



# Sleep 睡眠姿勢
# Servo_Prg_12_Step = 2;
Servo_Prg_12 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    30,   90,   90,  150,  150,   90,   90,   30,  500  ), # leg1,4 dn
  (    30,   45,  135,  150,  150,  135,   45,   30,  500  ), # protect myself
];



# 舞步 1
#Servo_Prg_13_Step = 10;
Servo_Prg_13 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    90,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg1,2,3,4 up
  (    50,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg1 dn
  (    90,   90,   90,  130,   90,   90,   90,   90,  400  ), # leg1 up; leg2 dn
  (    90,   90,   90,   90,   90,   90,   90,   50,  400  ), # leg2 up; leg4 dn
  (    90,   90,   90,   90,  130,   90,   90,   90,  400  ), # leg4 up; leg3 dn
  (    50,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg3 up; leg1 dn
  (    90,   90,   90,  130,   90,   90,   90,   90,  400  ), # leg1 up; leg2 dn
  (    90,   90,   90,   90,   90,   90,   90,   50,  400  ), # leg2 up; leg4 dn
  (    90,   90,   90,   90,  130,   90,   90,   90,  400  ), # leg4 up; leg3 dn
  (    90,   90,   90,   90,   90,   90,   90,   90,  400  ), # leg3 up
];
#Servo_List_Run(Servo_Prg_13);#测试


# 舞步 2
#Servo_Prg_14_Step = 10;
Servo_Prg_14 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   45,  135,  110,  110,  135,   45,   70,  400  ), # leg1,2,3,4 two sides
  (   115,   45,  135,   65,  110,  135,   45,   70,  400  ), # leg1,2 up
  (    70,   45,  135,  110,   65,  135,   45,  115,  400  ), # leg1,2 dn; leg3,4 up
  (   115,   45,  135,   65,  110,  135,   45,   70,  400  ), # leg3,4 dn; leg1,2 up
  (    70,   45,  135,  110,   65,  135,   45,  115,  400  ), # leg1,2 dn; leg3,4 up
  (   115,   45,  135,   65,  110,  135,   45,   70,  400  ), # leg3,4 dn; leg1,2 up
  (    70,   45,  135,  110,   65,  135,   45,  115,  400  ), # leg1,2 dn; leg3,4 up
  (   115,   45,  135,   65,  110,  135,   45,   70,  400  ), # leg3,4 dn; leg1,2 up
  (    75,   45,  135,  105,  110,  135,   45,   70,  400  ), # leg1,2 dn
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
];
#Servo_List_Run(Servo_Prg_14);#测试


# 舞步 3
#Servo_Prg_15_Step = 10;
Servo_Prg_15 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   45,   45,  110,  110,  135,  135,   70,  400  ), # leg1,2,3,4 bk
  (   110,   45,   45,   60,   70,  135,  135,   70,  400  ), # leg1,2,3 up
  (    70,   45,   45,  110,  110,  135,  135,   70,  400  ), # leg1,2,3 dn
  (   110,   45,   45,  110,   70,  135,  135,  120,  400  ), # leg1,3,4 up
  (    70,   45,   45,  110,  110,  135,  135,   70,  400  ), # leg1,3,4 dn
  (   110,   45,   45,   60,   70,  135,  135,   70,  400  ), # leg1,2,3 up
  (    70,   45,   45,  110,  110,  135,  135,   70,  400  ), # leg1,2,3 dn
  (   110,   45,   45,  110,   70,  135,  135,  120,  400  ), # leg1,3,4 up
  (    70,   45,   45,  110,  110,  135,  135,   70,  400  ), # leg1,3,4 dn
  (    70,   90,   90,  110,  110,   90,   90,   70,  400  ), # standby
];
#Servo_List_Run(Servo_Prg_15);#测试


# Turn left 左拧身
#Servo_Prg_6_Step = 2;
Servo_Prg_16 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    70,  135,  135,  110,  110,  135,  135,   70,  200  ), # turn left
];
#Servo_List_Run(Servo_Prg_16);#测试


# Turn right 右拧身
#Servo_Prg_7_Step = 2;
Servo_Prg_17 = [
  #  Ch04, Ch06, Ch00, Ch02, Ch12, Ch14, Ch08, Ch10,  ms
  (    70,   90,   90,  110,  110,   90,   90,   70,  200  ), # standby
  (    70,   45,   45,  110,  110,   45,   45,   70,  200  ), # turn right
];
#Servo_List_Run(Servo_Prg_17);#测试













import micropython
import utime
from QSpider_v1 import QSpider







#Servo通道顺序：
ch_list = [4, 6, 0, 2, 12, 14, 8, 10];


#servo校准表
#每项：通道号, 最小值, 最大值, 中间值
my_cl = [
	(0, 180, 580, 380),
	(2, 140, 550, 345),
	(4, 140, 550, 345),
	(6, 140, 550, 330),
	(8, 140, 540, 320),
	(10, 140, 550, 330),
	(12, 140, 540, 320),
	(14, 160, 540, 300)
];






#程序起始

ST_RESET     = const(0)
ST_TO_RUN    = const(1)
ST_TO_RESET  = const(2)
ST_RUNNING   = const(3)
ST_SLEEP     = const(4)
ST_TO_SRR    = const(5)
ST_SRRUN     = const(6)

#超声波障碍物躲避距离，小于此距离要转向
MIN_DISTANCE = const(15)#最小障碍距离cm




#主初始化
q1 = QSpider(i2c=2);
q1.setCalibration(my_cl);
q1.resetLeg();

utime.sleep_ms(1000);
status = ST_RESET;

while True:
	if (status == ST_RESET):
		q1.ps2.scanGamepad();
		if (q1.ps2.isKeyPressed() == True):
			if ((q1.ps2.getKey() & PSB_START) == 0):
				q1.standBy();
				status = ST_TO_RUN;
			elif ((q1.ps2.getKey() & PSB_TRIANGLE) == 0):#超声波自走
				q1.standBy();
				status = ST_TO_SRR;
			else:
				pass;
		utime.sleep_ms(100);
	elif (status == ST_TO_RUN):
		q1.ps2.scanGamepad();
		if (q1.ps2.isKeyPressed() == False):
			status = ST_RUNNING;
		utime.sleep_ms(100);
	elif (status == ST_RUNNING):
		q1.ps2.scanGamepad();
		if (q1.ps2.isKeyPressed() == True):
			if ((q1.ps2.getKey() & PSB_START) == 0):
				q1.initLeg();
				status = ST_TO_RESET;
				continue;
			elif ((q1.ps2.getKey() & PSB_PAD_UP) == 0):
				q1.walkForward();#前进
			elif ((q1.ps2.getKey() & PSB_PAD_DOWN) == 0):
				q1.walkBackward();#后退
			elif ((q1.ps2.getKey() & PSB_PAD_LEFT) == 0):
				q1.turnLeft();#左转
			elif ((q1.ps2.getKey() & PSB_PAD_RIGHT) == 0):
				q1.turnRight();#右转
			elif ((q1.ps2.getKey() & PSB_L1) == 0):
				q1.walkLeft();#左移
			elif ((q1.ps2.getKey() & PSB_R1) == 0):
				q1.walkRight();#右移
			elif ((q1.ps2.getKey() & PSB_L2) == 0):
				q1.Servo_List_Run(Servo_Prg_8);#趴地
				status = ST_TO_RUN;
				continue;
			elif ((q1.ps2.getKey() & PSB_SQUARE) == 0):
				q1.Servo_List_Run(Servo_Prg_9);#打招呼
				status = ST_TO_RUN;
				continue;
			elif ((q1.ps2.getKey() & PSB_R2) == 0):
				q1.Servo_List_Run(Servo_Prg_10);#战斗姿态
				status = ST_TO_RUN;
				continue;
			elif ((q1.ps2.getKey() & PSB_CROSS) == 0):
				q1.Servo_List_Run(Servo_Prg_13);#舞步1
				status = ST_TO_RUN;
				continue;
			elif ((q1.ps2.getKey() & PSB_CIRCLE) == 0):
				q1.Servo_List_Run(Servo_Prg_14);#舞步2
				status = ST_TO_RUN;
				continue;
			elif ((q1.ps2.getKey() & PSB_TRIANGLE) == 0):
				q1.Servo_List_Run(Servo_Prg_15);#舞步3
				status = ST_TO_RUN;
				continue;
			elif ((q1.ps2.getKey() & PSB_SELECT) == 0):
				q1.standBy();
				status = ST_TO_RUN;
				continue;
			else:
				status = ST_TO_RUN;
		utime.sleep_ms(100);
	elif (status == ST_TO_RESET):
		q1.ps2.scanGamepad();
		if (q1.ps2.isKeyPressed() == False):
			status = ST_RESET;
		utime.sleep_ms(100);
	elif (status == ST_TO_SRR):
		q1.ps2.scanGamepad();
		if (q1.ps2.isKeyPressed() == False):
			status = ST_SRRUN;
		utime.sleep_ms(100);
	elif (status == ST_SRRUN):
		q1.ps2.scanGamepad();
		if ((q1.ps2.isKeyPressed() == True) and ((q1.ps2.getKey() & PSB_START) == 0)):
			q1.initLeg();
			status = ST_TO_RESET;
			continue;
		else:
			ds = q1.lookForward();
			#print("ds=%dcm" %(ds));
			if (ds > MIN_DISTANCE):
				#print('--> forward.');
				q1.walkForward();#前进
			else:
				q1.walkBackward();#后退
				ds = q1.lookForward();
				dsl = q1.lookLeft();
				dsr = q1.lookRight();
				#print("dl=%dcm, dr=%dcm." %(dsl,dsr));
				if ((dsl > ds) and (dsr > ds)):
					if (dsl >= dsr):
						#print('Turn left.');
						q1.turnLeft();#左转
						q1.turnLeft();#左转
						q1.turnLeft();#左转
					else:
						#print('Turn right.');
						q1.turnRight();#右转
						q1.turnRight();#右转
						q1.turnRight();#右转
				elif (dsl > ds):
					#print('Turn left.');
					q1.turnLeft();#左转
					q1.turnLeft();#左转
					q1.turnLeft();#左转
				elif (dsr > ds):
					#print('Turn right.');
					q1.turnRight();#右转
					q1.turnRight();#右转
					q1.turnRight();#右转
				else:
					#print('<-- backward.');
					q1.walkBackward();#后退
					if (dsl >= dsr):
						#print('Turn left.');
						q1.turnLeft();#左转
						q1.turnLeft();#左转
						q1.turnLeft();#左转
					else:
						#print('Turn right.');
						q1.turnRight();#右转
						q1.turnRight();#右转
						q1.turnRight();#右转
	else:
		q1.initLeg();
		status = ST_RESET;







