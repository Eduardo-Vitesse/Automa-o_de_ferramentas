from pynput.keyboard import Key, Controller
#from pynput.mouse import Button, Controller as Controll
import time
from gtts import gTTS
from playsound import playsound

keyboard = Controller()
#mouse = Controll()

#mouse.move(23, 877)
#mouse.press(Button.left)
#mouse.release(Button.left)

# MENSAGEM DE VOZ DANDO BOAS VINDAS
voice_start = gTTS("Bom dia Luiz, vou abrir suas ferramentas de trabalho",lang='pt', slow=False)
voice_start.save('hello.mp3')
playsound('hello.mp3')

# ABRIR O SLACK
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(3)
keyboard.type('Slack')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(40)

# ABRIR O TERMINAL
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(3)
keyboard.type('Git Bash')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(7)
keyboard.type('cd ../..')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.type('cd GitHub/SchoolWeb/')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.type('clear')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)

# ABRIR O NAVEGADOR NO AZURE
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(3)
keyboard.type('edge')
time.sleep(5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(20)

keyboard.type('https://mail.google.com/mail/u/1/#inbox')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(10)
with keyboard.pressed(Key.ctrl):
    keyboard.press('t')
    keyboard.release('t')
time.sleep(3)

keyboard.type('azure')
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(10)

# ABRIR O VISUAL STUDIO
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(3)
keyboard.type('Visual Studio 2015')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(40)

# MENSAGEM DE VOZ DE ENCERRAMENTO
voice_and = gTTS("Suas ferramentas estão prontas, bom trabalho",lang='pt', slow=False)
voice_and.save('goodbye.mp3')
playsound('goodbye.mp3')



