import pyautogui
import pydirectinput
import keyboard
import threading


run = True
class AfkGameBot():
    
    def __init__(self):
        self.start_game()

    def start_game(self):
        global run

        button_ok = self.find('collections/OK.png')
        if button_ok:
            pyautogui.moveTo(button_ok)
            pyautogui.doubleClick()


        # ------------------------------------------------ #
        # Кнопка играть
        while True:
          if run == False:
              return False
          answer = self.click('collections/but_Play.png')
          if answer == True:
              break

        # ------------------------------------------------ #
        # Выбор режима с ботами
        for index in range(3):
          answer = self.click('collections/but_Bots.png')
          if answer == True:
              break
        else:
          print('[INFO] Возможно режим уже выбран')

        # ------------------------------------------------ #
        # Выбор режима совместная
        for index in range(3):
          answer = self.click('collections/but_Players.png')
          if answer == True:
              break
        else:
          print('[INFO] Select human')


        # ------------------------------------------------ #
        # Начать поиск
        while True:
          if run == False:
              return False
          answer = self.click('collections/but_Start.png')
          if answer == True:
              break

        # ------------------------------------------------ #
        # Принять игру
        while True:
            if run == False:
                return False
            self.click('collections/accept.png')


            # Ждем прогрузку
            answer = self.click('collections/but_Legion.png')
            if answer == True:
                break

        # Выбрать персонажа
        while True:
            if run == False:
                return False
            answer = self.click('collections/but_TakeHero.png', 'doubleClick')
            answer = self.click('collections/but_TakeHero.png', 'doubleClick')
            if answer == True:
                break


        # Начало игры
        while True:
            if run == False:
                return False

            pydirectinput.press('esc')
            pydirectinput.press('tab')
            pydirectinput.press('f1')

            answer = self.click('collections/but_Inventory.png', 'doubleClick')
            if answer == True:
                break

        # ЗАКРЕПИТЬ ПРЕДМЕТЫ В ЛАВКЕ #
        pydirectinput.write('aaa')
        pyautogui.sleep(1)

        for word in ['quel', 'power', 'vl', 'desol', 'sange and yasha']:
            pydirectinput.press('f6')
            pydirectinput.write(word)
            pyautogui.sleep(1)
            pydirectinput.keyDown('ctrl')
            pydirectinput.keyDown('shift')
            pydirectinput.keyDown('enter')

            pydirectinput.keyUp('ctrl')
            pydirectinput.keyUp('shift')
            pydirectinput.keyUp('enter')

            pydirectinput.press('escape')
            pydirectinput.press('4')



        # ========================== #
        # Реклама
        pydirectinput.keyDown('shift')
        pydirectinput.press('enter')

        pydirectinput.keyUp('shift')
        pydirectinput.write("good game")
        pydirectinput.press('enter')

        pydirectinput.press('4')
        pydirectinput.press('4')
        pydirectinput.press('4')

        # ========================== #

        pyautogui.sleep(60)
        pyautogui.moveTo(10, 10)
        while True:
            finish = self.check_finish()
            if finish == True:
                print('[INFO] End game.')
                break
            stop = self.farm_jungle()
            if stop == False:
                print('[INFO] Stop bot.')
                break
            else:

                while True:
                    finish = self.check_finish()
                    if finish == True:
                        print('[INFO] End game.')
                        break
                    if not self.find('collections/oche.png'):
                        break

                    pyautogui.sleep(5)

        return


    def check_finish(self):
        if run == False:
            return False

        answer = self.find('collections/finish.png')
        self.click('collections/finish.png')
        if answer:
            return True

        answer = self.find('collections/end_dire.png')
        self.click('collections/end_dire.png')
        if answer:
            return True

        else:
            return False


    def farm_jungle(self):
        if run == False:
            return False

        pydirectinput.press('tab')

        # FARM JUNGLE #
        answer = self.click('collections/find_map.png', 'doubleClick')
        self.skillpoint()

        for index in [[85, 61], [97, 58], [133, 60], [119, 35], [153, 57]]:
            _answer = self.find('collections/find_map.png')
            if _answer:
                pyautogui.moveTo([int(_answer[0]) - index[0], int(_answer[1]) + index[1]])
                self.history_click()
        
        self.skillpoint()
        self.click('collections/find_map.png', 'doubleClick')
        self.click('collections/find_map.png', 'doubleClick')
        return 

    def history_click(self):
        if run == False:
            return False

        pyautogui.click()
        pydirectinput.keyDown('shift')
        pydirectinput.keyDown('a')

        pydirectinput.keyUp('shift')
        pydirectinput.keyUp('a')
        return

    def skillpoint(self):
        if run == False:
            return False

        pydirectinput.press('4')
        pydirectinput.press('f3')

        answer = self.find('collections/but_find_aghn.png')

        if answer == False:
            return False
        else:
            left_answer = int(answer[0]) - 65
            top_answer = int(answer[1]) - 20
            
            answer = []
            answer.append(left_answer)
            answer.append(top_answer)

            pyautogui.moveTo(answer)
            pyautogui.doubleClick(answer)
            return True


    def find(self, image):
        if run == False:
            return False

        but = pyautogui.locateOnScreen(image, confidence=0.8)   
        if but != None:
            print(f'[INFO] Find accept {image.split(".")[0]}')
            return but

        elif but == None:
            return False



    def click(self, image, doubleClick = None):
        if run == False:
            return False

        but = pyautogui.locateOnScreen(image, confidence=0.8)   
        if but != None:
            pyautogui.moveTo(but)
            print('[INFO] Click completed.')
            if doubleClick:
                pyautogui.doubleClick(but)
            else:
                pyautogui.click(but)
            return True

        elif but == None:
            return False




def check_leave():
    global run
    while True:
        leave = pyautogui.locateOnScreen('collections/leave.png', confidence = 0.7)
        if leave:
            run = False

            pyautogui.moveTo(10, 500)
            pyautogui.sleep(1)
            while True:
                if pyautogui.locateOnScreen('collections/back_menu.png', confidence = 0.7):
                    print('good')
                    pyautogui.sleep(3)
                    break

            back = pyautogui.locateOnScreen('collections/back_menu.png', confidence = 0.7)
            pyautogui.moveTo(back)
            pyautogui.click()

            while True:
                if pyautogui.locateOnScreen('collections/discon.png', confidence = 0.8):
                    pyautogui.sleep(3)
                    break
            
            pyautogui.moveTo(10, 10)
            pyautogui.sleep(1)
            discon = pyautogui.locateOnScreen('collections/discon.png', confidence = 0.8)
            pyautogui.moveTo(discon)
            pyautogui.click()


            while True:
                if pyautogui.locateOnScreen('collections/leave_me.png', confidence = 0.7):
                    pyautogui.sleep(3)
                    break

            pyautogui.moveTo(10, 10)
            pyautogui.sleep(1)
            leave_me = pyautogui.locateOnScreen('collections/leave_me.png', confidence = 0.7)
            pyautogui.moveTo(leave_me)
            pyautogui.click()

            while True:
                if pyautogui.locateOnScreen('collections/yes_leave.png', confidence = 0.7):
                    pyautogui.sleep(3)
                    break

            pyautogui.moveTo(10, 10)
            pyautogui.sleep(1)
            yes_leave = pyautogui.locateOnScreen('collections/yes_leave.png', confidence = 0.7)
            pyautogui.moveTo(yes_leave)
            pyautogui.click()
            
            pyautogui.sleep(5)
            run = True
            pyautogui.sleep(100)

        pyautogui.sleep(3)


def press_key():
    global run
    while True:
        if keyboard.read_key() == 'home':
            if run == True:
                run = False
                print('[SERVICE] Bot stop.')
                pyautogui.sleep(5)
                break
            elif run == False:
                run = True
                print('[SERVICE] Bot ready.')
                pyautogui.sleep(5)
                break

    return press_key()


threading.Thread(target = press_key).start()
threading.Thread(target = check_leave).start()
while True:
    bot = AfkGameBot()
