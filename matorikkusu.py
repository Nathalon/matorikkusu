import random
import pygame

pygame.init()
pygame.mixer.init()

characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              'ァ', 'ア', 'ィ', 'イ', 'ゥ', 'ウ', 'ェ', 'エ', 'ォ',
              'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ', 'ケ', 'ゲ',
              'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ',
              'ゼ', 'ソ', 'ゾ', 'タ', 'ダ', 'チ', 'ヂ', 'ッ', 'ツ',
              'ヅ', 'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ',
              'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ', 'フ', 'ブ',
              'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'ボ', 'ポ', 'マ', 'ミ',
              'ム', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ', 'ョ', 'ヨ',
              'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヮ', 'ワ', 'ヰ', 'ヱ',
              'ヲ', 'ン', 'ヴ', 'ヵ', 'ヶ', 'ヷ', 'ヸ', 'ヹ', 'ヺ',
              '・', 'ー', 'ヽ', 'ヾ']

font = pygame.font.Font('font/MS Mincho.ttf', 35)
color = (0, 255, 0)

chars = []

for char in characters:
    item = font.render(char, True, (color))
    chars.append(item)

caption = pygame.display.set_caption('(Matorikkusu)')

screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
display = pygame.Surface((1920, 1080))
display.set_alpha(random.randrange(30, 40, 5))

pygame.display.set_icon(pygame.image.load('icons/programIcon.png'))

pygame.mixer.music.load('audio/audio.wav')
pygame.mixer.music.play(loops=-1)


class Matorikkusu:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        value = random.choice(chars)
        if self.y < 1080:
            self.y = self.y + 30
        else:
            self.y = -40 * random.randrange(1, 5)
        screen.blit(value, (self.x, self.y))


symbols = []

for i in range(0, 1920, 15 * 2):
    symbols.append(Matorikkusu(i, random.randrange(-1020, 0)))

blue = (0, 0, 255)
cyan = (0, 255, 255)
dallas = (110, 75, 38)
emberiea = (255, 121, 77)
french_rose = (246, 74, 138)
green = (0, 255, 0)
heliotrope = (223, 115, 255)
red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
olive = (128, 128, 0)
teal = (0, 128, 128)

run = True
delay = 50

while run:
    screen.blit(display, (0, 0))
    display.fill(pygame.Color('black'))

    for symbol in symbols:
        symbol.draw()

    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_LEFT:
                if delay > 0:
                    delay -= 15
            if event.key == pygame.K_RIGHT:
                if delay < 150:
                    delay += 15
            if event.key == pygame.K_b:
                color = blue
            if event.key == pygame.K_c:
                color = cyan
            if event.key == pygame.K_d:
                color = dallas
            if event.key == pygame.K_e:
                color = emberiea
            if event.key == pygame.K_f:
                color = french_rose
            if event.key == pygame.K_g:
                color = green
            if event.key == pygame.K_h:
                color = heliotrope
            if event.key == pygame.K_r:
                color = red
            if event.key == pygame.K_w:
                color = white
            if event.key == pygame.K_y:
                color = yellow
            if event.key == pygame.K_m:
                color = magenta
            if event.key == pygame.K_o:
                color = olive
            if event.key == pygame.K_t:
                color = teal
            if event.key == pygame.K_p:
                pygame.mixer.music.pause()
            if event.key == pygame.K_u:
                pygame.mixer.music.unpause()

            chars = []
            for char in characters:
                item = font.render(char, True, (color))
                chars.append(item)
