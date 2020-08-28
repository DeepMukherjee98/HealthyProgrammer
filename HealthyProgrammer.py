from pygame import mixer
import time
from datetime import datetime

def getdate():
    import datetime
    return str(datetime.datetime.now())

def file(x):
    eyes=r'C:\Users\meena\desktop\Shuteyes.mp3'
    exer=r'C:\Users\meena\desktop\doexercise.mp3'
    water=r'C:\Users\meena\desktop\drinkwater.mp3'
    if x=='eyes':
        return eyes
    elif x=='exer':
        return exer
    else:
        return water

def music(x):
    mixer.init()
    mixer.music.load(file(x))
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)

def quit():
    exit()

def timecheck():
    if time.localtime().tm_hour == 17 and time.localtime().tm_min == 00 and time.localtime().tm_sec == 00:
        quit()

def main():
    w=time.time()
    e=time.time()
    exe=time.time()
    while True:
        timecheck()
        if (time.time()-w)>1200:
            music('water')
            while True:
                y=input("Done? y/n : ")
                if y=='y':
                    mixer.music.stop()
                    w=time.time()
                    f=open('water.txt','a')
                    date=getdate()
                    water='['+date+']   '+' Done'
                    f.write(water+'\n')
                    f.close()
                    break
                elif y=='quit':
                    quit()
                else:
                    continue
        timecheck()
        if (time.time()-e)>1800:
            music('eyes')
            while True:
                y=input("Done? y/n : ")
                if y=='y':
                    mixer.music.stop()
                    e=time.time()
                    f=open('eyes.txt','a')
                    date=getdate()
                    eyes='['+date+']   '+' Done'
                    f.write(eyes+'\n')
                    f.close()
                    break
                elif y=='quit':
                    quit()
                else:
                    continue
        timecheck()
        if (time.time()-exe)>2700:
            music('exer')
            while True:
                y=input("Done? y/n : ")
                if y=='y':
                    mixer.music.stop()
                    exe=time.time()
                    f=open('exercise.txt','a')
                    date=getdate()
                    exercise='['+date+']   '+' Done'
                    f.write(exercise+'\n')
                    f.close()
                    break
                elif y=='quit':
                    quit()
                else:
                    continue

if __name__ == '__main__':
    if time.localtime().tm_hour ==9 and time.localtime().tm_min==00 and time.localtime().tm_sec==00 :
        main()
