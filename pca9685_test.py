
from pca9685 import PCA9685
from machine import I2C

i2c = I2C(2, freq=100000)

pca = PCA9685(i2c, 0x40, 50)
pca.setAllPWM(0, 160)



pca.setPWM(0, 0, 160)
pca.setPWM(4, 0, 160)

pca.setServoMin(0, 120)

pca.setServoMax(0, 240)

pca.Servo(0, -90)




#通道4测试
pca.setPWM(4, 0, 140)#min
pca.setPWM(4, 0, 345)#cen
pca.setPWM(4, 0, 550)#max
pca.calibration(4, 140, 550, 345)
pca.Servo(4, 45)
pca.Servo(4, 0)
pca.Servo(4, -45)


#通道5测试
pca.setPWM(5, 0, 140)#min
pca.setPWM(5, 0, 345)#cen
pca.setPWM(5, 0, 550)#max
pca.calibration(5, 140, 550, 345)
pca.Servo(5, 45)
pca.Servo(5, 0)
pca.Servo(5, -45)


#通道6测试
pca.setPWM(6, 0, 140)#min
pca.setPWM(6, 0, 330)#cen
pca.setPWM(6, 0, 550)#max
pca.calibration(6, 140, 550, 330)
pca.Servo(6, 45)
pca.Servo(6, 0)
pca.Servo(6, -45)


#通道7测试
pca.setPWM(7, 0, 140)#min
pca.setPWM(7, 0, 320)#cen
pca.setPWM(7, 0, 540)#max
pca.calibration(7, 140, 540, 320)
pca.Servo(7, 45)
pca.Servo(7, 0)
pca.Servo(7, -45)





