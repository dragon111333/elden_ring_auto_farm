import keyboard
import time
import threading

class control:
    def __init__(self):
        self.updateTime = 0.5
        print("press [M] to start")
        keyboard.wait("m")

        while(True):
            getUp = threading.Thread(target=self.getUp)
            walkForward = threading.Thread(target=self.walk, args=(True,))
            walkBack = threading.Thread(target=self.walk, args=(False,))
            attack = threading.Thread(target=self.attack)
            sit = threading.Thread(target=self.sit)

            self.call(getUp)
            self.call(walkForward)
            self.call(attack)
            self.call(walkBack)
            self.call(sit)

            time.sleep(5)
        pass

    def call(self,th):
        th.start()
        th.join()

    def walk(self,forward) :
        print("walking....")
        limit = 5
        key = "w" if (forward) else "s"
        sumTime = 0
        con = True
        while (con):
            keyboard.press(key)
            time.sleep(self.updateTime)
            sumTime=sumTime+self.updateTime
            if(sumTime >= limit) :
                con = False
                keyboard.release(key)
                time.sleep(0.5)
                return

    def attack(self):
        keyboard.press("ctrl")
        time.sleep(0.2)
        keyboard.release("ctrl")
        time.sleep(3)
        print("attack")
        return

    def sit(self):
        keyboard.press("e")
        time.sleep(0.2)
        keyboard.release("e")
        return

    def getUp(self):
        keyboard.press("q")
        time.sleep(0.2)
        keyboard.release("q")
        time.sleep(1)
        return

if __name__ == "__main__" :
    control()


