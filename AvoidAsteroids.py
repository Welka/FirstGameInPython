#!/usr/bin/env python
import pygame
import os
from pygame.locals import *
import random
import json

def loadimages(image):
    """Funkcja do wczytywania obrazów z folderu images"""
    fi = os.path.join("images",image)
    im = pygame.image.load(fi)
    return im
def loadsound(sound):
    """Funkcja do wczytywania dźwięków z folderu sounds"""
    fi = os.path.join("sounds",sound)
    so = pygame.mixer.Sound(fi)
    return so


def Menu():
    """Funkcja generująca Main Menu"""
    #wymiary okna
    Window_Width = 800
    Window_Height = 600
    #inicjalizacja modułów
    pygame.init()
    #inicjalizacja okna do wyświetlania
    screen = pygame.display.set_mode((Window_Width,Window_Height))
    #Dodanie nazwy okna
    pygame.display.set_caption("Avoid Asteroids")
    #zmienna uruchamiająca pętlę wyświetlającą menu
    run=True
    #inicjalizacja kursora w Main Menu
    CursorImage=loadimages("cursor.png")
    CursorRect = CursorImage.get_rect(center=(285,150))
    CursorVel=0
    #zmienne określające głośność i trydność gry
    Volume=100
    Dif=0
    def RulesWindow():
        """Funkcją wywołująca okno zasad gry"""
        #czarne tło
        screen.fill((0,0,0))
        #wyświetlanie napisu 'Rules'
        Rul=pygame.font.SysFont("arial",60)
        Rul = Rul.render("Rules",True,(255,160,0))
        RulRect = Rul.get_rect(center=(400,70))
        screen.blit(Rul,RulRect)
        #inicjalizacja grafiki przycisku UP
        kup=loadimages("keyup.png")
        kupRect = kup.get_rect(center=(300,225))
        screen.blit(kup,kupRect)
        #inicjalizacja grafiki przycisku DOWN
        kdown=loadimages("keydown.png")
        kdownRect = kdown.get_rect(center=(300,275))
        screen.blit(kdown,kdownRect)
        #wyświetlanie napisu 'Controls:'
        Controls=pygame.font.SysFont("arial",40)
        Controls = Controls.render("Controls:",True,(255,255,255))
        ControlsRect = Controls.get_rect(center=(200,250))
        screen.blit(Controls,ControlsRect)
        #wyświetlanie napisu 'Avoid the asteroids and collect bitcoins to collect points'
        Points =pygame.font.SysFont("arial",30)
        Points = Points.render("Avoid the asteroids and collect bitcoins to collect points",True,(255,255,255))
        PointsRect = Points.get_rect(center=(400,150))
        screen.blit(Points,PointsRect)
        #wyświetlanie napisu 'Press P to pause the game'
        pressP=pygame.font.SysFont("arial",35)
        pressP = pressP.render("Press P to pause the game",True,(255,255,255))
        pressPRect = pressP.get_rect(center=(300,350))
        screen.blit(pressP,pressPRect)
        #inicjalizacja zmian na ekranie
        pygame.display.flip()
        r=True
        while r:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        r = False
    def OptionsWindow(Volume,Dif):
        """Funkcją wywołująca okno opcji"""
        #lista trudności
        DifList=["Easy","Medium","Hard"]
        #inicjalizacja kursora w opcjach
        CurImage=loadimages("cursor.png")
        CurRect = CurImage.get_rect(center=(50,150))
        CurVel=0
        o=True
        while o:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return Volume , Dif
                    elif event.key == K_LEFT:
                        if CurRect.centery == 150:
                            Volume -= 5
                            if Volume == -5:
                                Volume = 0
                        elif CurRect.centery == 200:
                            Dif -=1
                            if Dif == -1:
                                Dif = 0
                    elif event.key == K_RIGHT:
                        if CurRect.centery == 150:   
                            Volume += 5
                            if Volume == 105:
                                Volume = 100
                        elif CurRect.centery == 200:
                            Dif +=1
                            if Dif == 3:
                                Dif = 2                           
                    elif event.key == K_DOWN:
                        CurVel=50
                    elif event.key == K_UP:
                        CurVel=-50
                    elif event.key == K_ESCAPE:
                        o = False
            #czarne tło
            screen.fill((0,0,0))
            #wyświetlanie napisu 'Options'
            Op=pygame.font.SysFont("arial",60)
            Op = Op.render("Options",True,(255,160,0))
            OpRect = Op.get_rect(center=(400,70))
            screen.blit(Op,OpRect)
            #wyświetlanie napisu 'Volume: (wartość dźwięku)%'
            volume=pygame.font.SysFont("arial",40)
            volume = volume.render("Volume:"+str(Volume)+"%",True,(255,255,255))
            volumeRect = volume.get_rect(center=(200,150))
            screen.blit(volume,volumeRect)
            #wyświetlanie napisu 'Difficulty: (poziom trudności)'
            difficulty=pygame.font.SysFont("arial",40)
            difficulty = difficulty.render("Difficulty:"+DifList[Dif],True,(255,255,255))
            difficultyRect = difficulty.get_rect(center=(200,200))
            screen.blit(difficulty,difficultyRect)
            #Przemieszczanie kursora na ekranie
            CurRect.centery += CurVel
            if CurRect.centery == 250:
                CurRect.centery = 200
            elif CurRect.centery == 100:
                CurRect.centery = 150
            screen.blit(CurImage,CurRect) 
            #inicjalizacja zmian
            pygame.display.update()

    def BestScoresWindow():
        """Funkcją wywołująca okno najlepszych wyników"""
        #czarne tło
        screen.fill((0,0,0))
        #odczytywanie najlepszych wyników z pliku BestScores.json
        data=open("BestScores.json","r")
        Scores=json.loads(data.read())
        #wyświetlanie napisu 'Best Scores'
        BS=pygame.font.SysFont("arial",60)
        BS = BS.render("Best Scores",True,(255,160,0))
        BSRect = BS.get_rect(center=(400,70))
        screen.blit(BS,BSRect)
        #wyświetlanie 10 najlepszych wyników
        for i in range(len(Scores["ScoreList"])):
            BSc=pygame.font.SysFont("arial",30)
            BSc = BSc.render(str(i+1)+". "+str(Scores["ScoreList"][i]),True,(255,255,255))
            BScRect = BSc.get_rect(center=(200,150+30*i))
            screen.blit(BSc,BScRect)
        #inicjalizacja zmian
        pygame.display.flip()
        b=True
        while b:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        b = False

    def CreditsWindow():
        """Funkcją wywołująca okno Credits"""
        #czarne tło
        screen.fill((0,0,0))
        #wyświetlanie napisu 'Credits'
        Cr=pygame.font.SysFont("arial",60)
        Cr = Cr.render("Credits",True,(255,160,0))
        CrRect = Cr.get_rect(center=(400,70))
        screen.blit(Cr,CrRect)       
        #wyświetlanie napisu 'Made by Student' 
        cre =pygame.font.SysFont("arial",30)
        cre = cre.render("Made by Student",True,(255,255,255))
        creRect = cre.get_rect(center=(400,150))
        screen.blit(cre,creRect)
        #inicjalizacja zmian
        pygame.display.flip()
        c=True
        while c:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        c = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    CursorVel = 50
                elif event.key == K_UP:
                    CursorVel = -50
                elif event.key == K_RETURN:
                    if CursorRect.centery == 150:
                        game(Volume,Dif)
                    elif CursorRect.centery == 200:
                        RulesWindow()
                    elif CursorRect.centery == 250:
                        Volume,Dif=OptionsWindow(Volume,Dif)
                    elif CursorRect.centery == 300:
                        BestScoresWindow()
                    elif CursorRect.centery == 350:
                        CreditsWindow()
                    elif CursorRect.centery == 400:
                        pygame.quit()
                        quit()
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    CursorVel = 0
                elif event.key == K_UP:
                    CursorVel = 0
            #inicjalizacja grafiki tła menu
            screen.blit(loadimages("menu.png"),(0,0))
            #wyświetlanie napisu 'Main Menu'
            Menu=pygame.font.SysFont("arial",40)
            Menu = Menu.render("Main Menu",True,(255,160,0))
            MenuRect = Menu.get_rect(center=(400,50))
            screen.blit(Menu,MenuRect)
            #wyświetlanie napisu 'Start'
            Start=pygame.font.SysFont("arial",40)
            Start = Start.render("Start",True,(100,160,0))
            StartRect = Start.get_rect(center=(400,150))
            screen.blit(Start,StartRect)
            #wyświetlanie napisu 'Rules'
            Rules=pygame.font.SysFont("arial",40)
            Rules = Rules.render("Rules",True,(100,160,0))
            RulesRect = Rules.get_rect(center=(400,200))
            screen.blit(Rules,RulesRect)
            #wyświetlanie napisu 'Options'
            Options=pygame.font.SysFont("arial",40)
            Options = Options.render("Options",True,(100,160,0))
            OptionsRect = Options.get_rect(center=(400,250))
            screen.blit(Options,OptionsRect)
            #wyświetlanie napisu 'Best Scores'
            BestScores=pygame.font.SysFont("arial",40)
            BestScores = BestScores.render("Best Scores",True,(100,160,0))
            BestScoresRect = BestScores.get_rect(center=(400,300))
            screen.blit(BestScores,BestScoresRect)           
            #wyświetlanie napisu 'Credits'
            Credits=pygame.font.SysFont("arial",40)
            Credits = Credits.render("Credits",True,(100,160,0))
            CreditsRect = Credits.get_rect(center=(400,350))
            screen.blit(Credits,CreditsRect)  
            #wyświetlanie napisu 'Quit'
            Quit=pygame.font.SysFont("arial",40)
            Quit = Quit.render("Quit",True,(100,160,0))
            QuitRect = Quit.get_rect(center=(400,400))
            screen.blit(Quit,QuitRect) 
            #Przemieszczanie kursora na ekranie
            CursorRect.centery += CursorVel
            if CursorRect.centery == 450:
                CursorRect.centery = 150
            elif CursorRect.centery == 100:
                CursorRect.centery = 400
            screen.blit(CursorImage,CursorRect) 
            #inicjalizacja zmian
            pygame.display.update()



def game(Vol,Dif):
    #wymiary okna
    Window_Width = 800
    Window_Height = 600
    #inicjaliza modułu mixer
    pygame.mixer.init(frequency=22050,size=-16,channels=0,buffer=512)
    #inicjaliza muzyki w tle
    pygame.mixer.music.load(os.path.join("sounds","backsound.mp3"))
    #zapętlenie muzyki w tle
    pygame.mixer.music.play(loops = -1)
    #zmiana głośności muzyki w tle
    pygame.mixer.music.set_volume(Vol/100*0.7)
    #inicjalizacja modułów
    pygame.init()
    def Create(x):
        """Funkcją tworząca obiekty w grze"""
        #generowanie asteroid w zależności od wybranej trudności
        if (x=="Asteroid"):
            if Dif==0:
                NewAsteroid = Aster1Image.get_rect(midtop=(800,random.randrange(400)))
                return NewAsteroid
            elif Dif==1:
                NewAsteroid = Aster2Image.get_rect(midtop=(800,random.randrange(400)))
                return NewAsteroid            
            else:
                NewAsteroid = Aster3Image.get_rect(midtop=(800,random.randrange(400)))
                return NewAsteroid
        #generowanie bitcoinów
        elif (x=="Bitcoin"):
            NewBitcoin = BitcoinImage.get_rect(midtop=(800,random.randrange(400)))
            return NewBitcoin
    def Move(x):
        """Funkcją przemieszczająca obiekty w grze"""
        #przemieszczanie asteroid w zależności od wybranej trudności
        if x == AsteroidList:
            if Dif==0:
                for Asteroid in x:
                    Asteroid.centerx -= 4
                return x
            elif Dif==1:
                for Asteroid in x:
                    Asteroid.centerx -= 6
                return x
            else:
                for Asteroid in x:
                    Asteroid.centerx -= 7
                return x
        #przemieszczanie bitcoinów
        elif x == BitcoinsList:
            for bitcoin in x:
                bitcoin.centerx -= 2
            return x
    def Collisions(list):
        """Funkcją sprawdzająca kolizje obiektów w grze"""
        #sprawdzanie kolizji statku gracza z innymi obiektami
        for x in list:
            if ShipRect.colliderect(x):
                if (list == AsteroidList):
                    pygame.mixer.Channel(1).play(AsterSound)
                    AsteroidList.remove(x)
                    return True
                if (list == BitcoinsList):
                    pygame.mixer.Channel(2).play(BitcoinSound)
                    BitcoinsList.remove(x)
                    return True
    def ScoreCounter():
        """Funkcją wyświetlająca aktualny wynik"""
        #wyświetlanie napisu '(aktualny wynik)'
        Score = pygame.font.SysFont("arial",40).render(str(int(score)),True,(255,255,255))
        ScoreRect = Score.get_rect(center=(50,50))
        screen.blit(Score,ScoreRect)

    def LifeCounter():
        """Funkcją wyświetlająca ilość żyć"""
        #wyświetlanie napisu 'Lifes:(aktualna ilość żyć)'
        Life = pygame.font.SysFont("arial",40).render("Lifes:"+str(int(life)),True,(255,255,255))
        LifeRect = Life.get_rect(center=(50,90))
        screen.blit(Life,LifeRect)
    #inicjalizacja okna do wyświetlania
    screen = pygame.display.set_mode((Window_Width,Window_Height))
    #inicjalizacja gafiki tła w grze
    BackgroundImage = loadimages("back.png")
    #inicjalizacja gafiki podłoża w grze
    FloorImage = loadimages("moon.png")
    Floor_x=0
    #inicjalizacja gafiki statku gracza
    ShipImage = loadimages("ship.png")
    ShipRect = ShipImage.get_rect(center=(50,300))
    ShipVel = 0
    #inicjalizacja gafik asteroid
    Aster1Image = loadimages("asteroid1.png")
    Aster2Image = loadimages("asteroid2.png")
    Aster3Image = loadimages("asteroid3.png")
    #inicjalizacja dźwięku kolizji statku z asteroidą
    AsterSound = loadsound("astercrash.wav")
    #zamiana głoścności dźwięku kolizji statku z asteroidą
    AsterSound.set_volume(Vol/100*0.2)
    #lista zawierająca dane o asteroidach
    AsteroidList=[]
    #częstotliwość generowania obiektów w grze
    Spawn = pygame.USEREVENT
    if Dif == 0:    
        pygame.time.set_timer(Spawn,1000)
    elif Dif == 1:
        pygame.time.set_timer(Spawn,600)
    else:
        pygame.time.set_timer(Spawn,500)
    #inicjalizacja gafiki bitcoina
    BitcoinImage = loadimages("bitcoin.png")
    #lista zawierająca dane o bitcoinach
    BitcoinsList=[]
    #inicjalizacja dźwięku kolizji statku z bitcoinem
    BitcoinSound = loadsound("bitcoin.wav")
    #zamiana głoścności dźwięku kolizji statku z bitcoinem
    BitcoinSound.set_volume(Vol/100*0.2)
    #zmienne pomocnicze
    n=1
    score=0
    life=3
    #czas w grze 
    clock = pygame.time.Clock()
    running = True
    def End():
        """Funkcją wyświetlająca okno GAME OVER"""
        #wyświetlanie napisu 'GAME OVER'
        br=pygame.font.SysFont("arial",40)
        br = br.render("GAME OVER",True,(255,160,0))
        brRect = br.get_rect(center=(400,50))
        screen.blit(br,brRect)
        #inicjalizacja grafiki kursora w oknie GAME OVER
        CursImage=loadimages("cursor.png")
        CursRect = CursImage.get_rect(center=(50,150))
        CursVel=0
        #zapis wyniku do pliku
        data=open("BestScores.json","r")
        Scores=json.loads(data.read())
        if len(Scores["ScoreList"])<10:
            Scores["ScoreList"].append(score)
            Scores["ScoreList"].sort(reverse=True)
        else:
            if score<Scores["ScoreList"][9]:
                pass
            else:
                Scores["ScoreList"].pop()
                Scores["ScoreList"].append(score)
                Scores["ScoreList"].sort(reverse=True)
        NewData = Scores
        file=open("BestScores.json", "w")
        json.dump(NewData,file)
        file.close()

        end = True
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_m:
                        end = False
                    elif event.key == K_DOWN:
                        CursVel=50
                    elif event.key == K_UP:
                        CursVel=-50
                    elif event.key == K_RETURN:
                        if CursRect.centery == 150:
                            end= False
                        elif CursRect.centery == 200:
                            pygame.quit()
                            quit()
            #inicjalizacja gafiki tła w oknie GAME OVER
            screen.blit(loadimages("gameover.png"),(0,0))
            screen.blit(br,brRect)
            #wyświetlanie napisu 'Main Menu'
            Me=pygame.font.SysFont("arial",40)
            Me = Me.render("Main Menu",True,(255,255,255))
            MeRect = Me.get_rect(center=(200,150))
            screen.blit(Me,MeRect)
            #wyświetlanie napisu 'Quit'
            Qu=pygame.font.SysFont("arial",40)
            Qu = Qu.render("Quit",True,(255,255,255))
            QuRect = Qu.get_rect(center=(200,200))
            screen.blit(Qu,QuRect)
            #Przemieszczanie kursora na ekranie                        
            CursRect.centery += CursVel
            if CursRect.centery == 250:
                CursRect.centery = 200
            elif CursRect.centery == 100:
                CursRect.centery = 150
            screen.blit(CursImage,CursRect)
            #inicjalizacja zmian na ekranie
            pygame.display.update() 
                        
    def Paused():
        """Funkcją wyświetlająca okno pauzy"""
        #czarne tło
        screen.fill((0,0,0))
        #wyświetlanie napisu 'Paused'
        Pas=pygame.font.SysFont("arial",40)
        Pas = Pas.render("Paused",True,(255,255,255))
        PasRect = Pas.get_rect(center=(400,50))
        screen.blit(Pas,PasRect)
        #wyświetlanie napisu 'Press:             to unpause.'
        Pa=pygame.font.SysFont("arial",30)
        Pa = Pa.render("Press:             to unpause.",True,(255,255,255))
        PaRect = Pa.get_rect(center=(400,150))
        screen.blit(Pa,PaRect)
        #inicjalizacja grafiki przycisku ESC
        Esc=loadimages("esc.png")
        EscRect = Esc.get_rect(center=(370,150))
        screen.blit(Esc,EscRect)
        #inicjalizacja zmian
        pygame.display.flip()
        pause=True

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    pygame.mixer.music.pause()
                    Paused()
                    pygame.mixer.music.unpause()
                elif event.key == K_UP:
                    ShipVel = -6
                elif event.key == K_DOWN:
                    ShipVel = 6
            elif event.type == KEYUP:
                if event.key == K_UP:
                    ShipVel = 0
                elif event.key == K_DOWN:
                    ShipVel = 0
            elif event.type == Spawn:
                #tworzenie i dodawanie obietków do list
                AsteroidList.append(Create("Asteroid"))
                n += 1
                if n%3==0:
                    BitcoinsList.append(Create("Bitcoin"))
        #tło w grze
        screen.blit(BackgroundImage,(0,0))
        #przemieszczanie statku gracza
        ShipRect.centery += ShipVel
        if ShipRect.top <= 0:
            ShipRect.top = 0
        elif ShipRect.bottom >= 0.83*Window_Height:
            ShipRect.bottom = 0.83*Window_Height
        screen.blit(ShipImage,ShipRect)
        #sprawdzanie kolizji statku z asteroidą
        if Collisions(AsteroidList)==True:
            life -= 1
            if life == 0:    
                pygame.mixer.music.stop()
                End()
                running=False
        #przemieszczanie asteroid
        AsteroidList = Move(AsteroidList)
        for Asteroid in AsteroidList:
            if Dif==0:
                screen.blit(Aster1Image,Asteroid)
            elif Dif==1:
                screen.blit(Aster2Image,Asteroid)
            else:
                screen.blit(Aster3Image,Asteroid)
        #przemieszczanie bitcoinów
        BitcoinsList = Move(BitcoinsList)
        for Bitcoin in BitcoinsList:
            screen.blit(BitcoinImage,Bitcoin)
        #sprawdzanie kolizji statku z bitcoinem
        if Collisions(BitcoinsList)==True:
            score += 1
        #wywoływnanie funkcji wyświetlającej aktualny wynik
        ScoreCounter()
        #wywoływnanie funkcji wyświetlającej aktualny stan żyć
        LifeCounter()
        #przemieszczanie podłoża na ekranie 
        Floor_x -= 1
        screen.blit(FloorImage,(Floor_x,500))
        if Floor_x <= -800:
            Floor_x = 0
        #inicjalizacja zmian
        pygame.display.update()
        #aktualizowanie czasu
        clock.tick(60)
Menu()