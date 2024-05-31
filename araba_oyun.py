import pygame
import random
import sys
import os


pygame.init()

class Pencere:
    def __init__(self) :
        self.oyunCalisiyor = True
        self.menu = True
        self.oyunAktif = False
        self.options = False
        self.communication = False
        self.modernTema = True
        self.sesAcik = True
        self.duraklat = True
        self.pencereAktif = False
        self.ozelCubukAcik = False
        self.seviye = 1
        self.oyunHizi = 8
        self.menuButonlarıBosluk = 175
        self.icKenarRenk = (50,50,50)
        self.disKenarRenk = (180,238,180)
        self.ekranDikeyBoyut = 1100
        self.ekranYatayBoyut = 800
        self.fps = pygame.time.Clock()
        self.oyunYuzeyi = pygame.display.set_mode((self.ekranYatayBoyut,self.ekranDikeyBoyut), pygame.NOFRAME) #pygame.noframe       #noframe windosun penceresini kapatıyor.
        pygame.display.set_caption('RACE CAR')      #pencere başlığı, iconda ekleniyor sonra bak
        self.menuArkaPlan = pygame.transform.scale(pygame.image.load(os.path.join('resim','1.jpg')),(self.ekranYatayBoyut,self.ekranDikeyBoyut))
        self.communicationArkaPlan = pygame.transform.scale(pygame.image.load(os.path.join('resim','2.jpg')),(self.ekranYatayBoyut,self.ekranDikeyBoyut))
        self.communicationYaziAyar = pygame.font.Font(os.path.join('font','5.TTF'),40)
        self.optionsArkaPlan = pygame.image.load(os.path.join('resim','3.jpg'))             #burda optionsda görünecek resmi yükleyip,
        self.optionsArkaPlan = pygame.transform.rotate(self.optionsArkaPlan,90)             #resmin normal görünüşü yataya uygun olduğu için dikey boyutlanınca iyi görünmüyor o yüzden 90 derece döndürüp
        self.optionsArkaPlan = pygame.transform.scale(self.optionsArkaPlan,(self.ekranYatayBoyut,self.ekranDikeyBoyut))     #ekrana göre ölçeklemesini yapıyoruz. hepsini aynı değişkene atıp ona işlem yaptıkki farklı farklı değişkenler oluşmasın. eldeki değişkeni güncelledik sürekli
        
        
   
pencereOzellik = Pencere()


class SeritOlustur:
    def __init__(self, konumY ):       #dikey olduğu için x sabit, y1 = başlangıç, y2 = bitiş
        self.konumY = konumY
        self.yanSeritMesafe = 137.5
        self.konumX = 262.5
        self.seritUzunluk = 100
        self.seritRenk = (224,255,255)
        self.seritKalinlik = 5

    def seritCiz (self, hiz):
        pygame.draw.line(pencereOzellik.oyunYuzeyi, self.seritRenk , [self.konumX ,self.konumY], 
                         [self.konumX ,self.konumY + self.seritUzunluk], self.seritKalinlik)      #burası soldan ilk çizgiyi çiziyor, aşağıdaki ikğ satırda oranlı olarak  belli boşluk bırakıp ikinci ve üçüncüyü çiziyor.
        pygame.draw.line(pencereOzellik.oyunYuzeyi, self.seritRenk , [ (self.konumX + self.yanSeritMesafe) ,self.konumY], 
                         [ (self.konumX + self.yanSeritMesafe) ,self.konumY + self.seritUzunluk], self.seritKalinlik)
        pygame.draw.line(pencereOzellik.oyunYuzeyi, self.seritRenk , [ (self.konumX + (self.yanSeritMesafe *2)) ,self.konumY], 
                         [ (self.konumX + (self.yanSeritMesafe *2)) ,self.konumY + self.seritUzunluk], self.seritKalinlik)
        self.konumY += hiz


class AgacOlustur:
    def __init__(self):
        self.agacGenislik = 94
        self.agacYukseklik = 94
        self.solAgacX = 25
        self.solAgacY = -94     #ekranın üst kısımdan başlayarak inmesi için
        self.sagAgacX = 675
        self.sagAgacY = -94
        self.secilenAgacGorseli = random.randint(1,7)      #agac klasöründeki agac isimlerinin rasgele çekilerek belirlenmesi için.
        agacDosyaAdi = os.path.join('agac',f'{self.secilenAgacGorseli}.png')    #diğer işletim sistemlerindede dosyayı bulabilmesi için
        self.agac = pygame.image.load(agacDosyaAdi).convert_alpha()     #convert_alpha() resmin arka planını saydam yapıyor. resmin arka planının görünmesini istersen convert() yöntemini kullan.
        self.agacAyarla = pygame.transform.scale(self.agac,(self.agacGenislik, self.agacYukseklik))     #seçilen ağacı boyutlandırma
        
    def solKenarAgac (self):
        pencereOzellik.oyunYuzeyi.blit(self.agacAyarla,(self.solAgacX, self.solAgacY))
        self.solAgacY += pencereOzellik.oyunHizi

    def sagKenarAgac (self):
        pencereOzellik.oyunYuzeyi.blit(self.agacAyarla,(self.sagAgacX, self.sagAgacY))
        self.sagAgacY += pencereOzellik.oyunHizi
    
ilkSiraSerit = SeritOlustur(100)
ikinciSiraSerit = SeritOlustur(300)
ucuncuSiraSerit = SeritOlustur(500)
dorduncuSiraSerit = SeritOlustur(700)
besinciSiraSerit = SeritOlustur(900)
altinciSiraSerit = SeritOlustur(1100)
     

pygame.time.set_timer(pygame.USEREVENT + 1, random.randint(800, 2700))      #oyun döngüsünde zamanlayıcı ile işlem yapmak için oluşturulan satır. 
pygame.time.set_timer(pygame.USEREVENT + 2 , random.randint(800, 2700))     #userevent +1, +2 gibi şeylerle kimlik veriyoruz gibi bişey.
solAgacListesi = []         #sürekli obje oluşturmasın diye döngüde oluşturulan objeleri buraya ve aşağıya atıyoruz.
sagAgacListesi = [] 


class MenuButonOlustur:
    def __init__(self, metin, boyut, konumY , netlik=True) :
        self.butonEfektAktif = False
        fontIsım = '12.ttf'
        fontOzellik = pygame.font.Font( os.path.join('font',fontIsım) , boyut )
        fontOzellik.set_bold(False) 
        self.yaziPasifRenk = (0,0,0)
        self.yaziAktifRenk = (240,230,140)
        self.cercevePasifRenk = (240,230,140)
        self.cerceveAktifRenk = (0,0,0)
        self.kenarlikRenk = (0,0,0)
        self.metinYazi = metin
        self.metinPasif = fontOzellik.render( self.metinYazi, netlik , self.yaziPasifRenk)          #burdaki antialias metnü pürüzsüzleştirmeyle alakalı, true yaparsan metnin kenarları daha yumuşak oluyor.
        self.metinAktif = fontOzellik.render( self.metinYazi, netlik , self.yaziAktifRenk) 
        self.metinOlcu = self.metinPasif.get_rect()      #oluşturulan yazının  kenar kısımlarının genişlik uzunluk ölçülerini veriyor.
        self.konumY = konumY
        self.metinBaslamaNoktası = (pencereOzellik.ekranYatayBoyut / 2 ) - (self.metinOlcu.width / 2)    #metinölçü.width yerine metinölçü[2] de yazabiliriz aynı sonuç.
        self.kutuIcınBaslamaNoktasıX = 200                                           #soldan 200 piksel ilerden başlaması için
        self.kutuIcınBitisNoktasıX = pencereOzellik.ekranYatayBoyut + (-200 *2)      #200 piksel ileride başladığı için ekran boyutundan 2 kere iki yüz çıkararak hem baştan hem sondan 200 piksellik ortalı bi kutu oluşturduk
        self.kutuIcınBaslamaNoktasıY = self.konumY - 20                              #kutunun ilk başlangıç dikey konumu. -20 ise kutu çiziminin yazının birazcık daha üstünden başlaması için
        self.kutuIcınBitisNoktasıY = self.metinOlcu.height + 40                      #yazının dikey ölçüsü ile yukarda yazı ile arasında fazla boşluk olması için bıraktığımız -20 değerinin alt kısımdada geçerli olması için 2 ile çarpıp artı değere dönüştürme
        self.cerceve = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.cercevePasifRenk, (self.kutuIcınBaslamaNoktasıX, self.kutuIcınBaslamaNoktasıY, self.kutuIcınBitisNoktasıX, self.kutuIcınBitisNoktasıY))
        
    def menuButonEfekt(self, yuzey):        #metnin yatay olarak kapladığı alanı hesaplayıp yatay konumda ortalı yazdırma.
        if self.butonEfektAktif is True :
            if self.kutuIcınBaslamaNoktasıX >= 15 :     #ekranın dışında sonsuza dek gitmesin diye köşelere az kala durması için
                self.kutuIcınBaslamaNoktasıX -= 3       #sola doğru genişlemesi için
                self.kutuIcınBitisNoktasıX += 6         #sağa doğru soldakiyle aynı orantıda genişlemesi için
                self.butonCizYaziYaz()
            else:
                self.butonCizYaziYaz()
        elif self.butonEfektAktif is False:
            self.kutuIcınBaslamaNoktasıX = 200                                           #ilk 4 özellik inittede tanımlı ama kutuların başlangıç konumlarından tekrar büyüyerek gitmesi için burda tekrar ilk değerlerine eşitliyoruz
            self.kutuIcınBitisNoktasıX = pencereOzellik.ekranYatayBoyut + (-200 *2)      
            self.kutuIcınBaslamaNoktasıY = self.konumY - 20                              
            self.kutuIcınBitisNoktasıY = self.metinOlcu.height + 40
            self.butonCizYaziYaz()                                                       #çerçeve özelliklerini ayarlamak ve ekranda değişiklikleri göstermek için blitinde olduğu fonksiyona gönderiyoruz
              
    def butonCizYaziYaz(self):
        if self.butonEfektAktif is True:
            self.cerceve = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.cerceveAktifRenk, (self.kutuIcınBaslamaNoktasıX, self.kutuIcınBaslamaNoktasıY, self.kutuIcınBitisNoktasıX, self.kutuIcınBitisNoktasıY),border_top_left_radius=30, border_bottom_right_radius=30)     #sırasıyla(ilk değer 0 sa içi dolu diğer pozitif değerler içi boş ve arttıkça kenar kalınlığı, ikinci değer tüm kenarları yuvarlatma, diğer 4 değer ayrı ayrı kenarları yuvarlatma)
            pencereOzellik.oyunYuzeyi.blit(self.metinAktif,(self.metinBaslamaNoktası,self.konumY)) 
            
        elif self.butonEfektAktif is False:
            self.cerceve = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.cercevePasifRenk, (self.kutuIcınBaslamaNoktasıX, self.kutuIcınBaslamaNoktasıY, self.kutuIcınBitisNoktasıX, self.kutuIcınBitisNoktasıY),border_top_left_radius=30, border_bottom_right_radius=30)
            pencereOzellik.oyunYuzeyi.blit(self.metinPasif,(self.metinBaslamaNoktası,self.konumY)) 

    def butonTiklamaEfekt(self):    #fare tuşuna basınca butonların kenarında kenarlık oluşturma
        ciz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.kenarlikRenk, (self.cerceve.x -10, self.cerceve.y -10, self.cerceve.width +20, self.cerceve.height +20),3,border_top_left_radius=35, border_bottom_right_radius=35)
        pygame.display.update(ciz)         #buton arka planının tıklanınca etrafında çerçeve olması
        pygame.time.delay(250)        #bu oyun döngüsünü duraklatmıyor
        #pygame.time.wait(5000)       #bu döngüyü duraklatıyor
        
        

    def butonGorev(self):
        if self.metinYazi == 'PLAY - RESUME':
            pencereOzellik.menu = False
            pencereOzellik.oyunAktif = True
            pencereOzellik.duraklat = False
            pencereOzellik.options = False
            print('flgdşlfgkşl')
        elif self.metinYazi == 'RESTART':
            pencereOzellik.seviye = 1
            pencereOzellik.options = False
        elif self.metinYazi == 'OPTIONS':
            pencereOzellik.oyunAktif = False
            pencereOzellik.menu = False
            pencereOzellik.options = True
            
        elif self.metinYazi == 'COMMUNICATION':
            pencereOzellik.oyunAktif = False
            pencereOzellik.menu = False
            pencereOzellik.communication = True
            pencereOzellik.options = False
        else:
            pass



class PencereCubuk:
    def __init__(self) :
        
        self.simgeBoyut = 50
        self.cubukKoordinat = (0,0,pencereOzellik.oyunYuzeyi.get_width(),50)
        self.mCubukRenk = (0,0,0)
        self.rcubukRenk = (240,230,140)
        self.gorevCubuguCiz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.mCubukRenk, self.cubukKoordinat)
        self.gizleyiciKoordinat = (((self.gorevCubuguCiz.w/2) - (self.simgeBoyut/2)), 0, self.simgeBoyut , self.simgeBoyut )
        self.katsayi = 75
        self.pauseFont = pygame.font.Font(os.path.join('font','1.ttf'),135)
        self.pauseFontCiz = self.pauseFont.render('PAUSED',True,(204, 190, 159))
        self.pauseFontCerceveOlcu = self.pauseFontCiz.get_rect()
        
        self.mmenu = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','menu.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mplay = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','play.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mpause = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','pause.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.msound = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','sound.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.msound2 = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','sound2.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mclose = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','close.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mback = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','back.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mnext = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','next.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mthema = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','thema.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mconsol = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','consol.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mdown = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','down.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.mup = pygame.transform.scale(pygame.image.load(os.path.join('icon','modern','up.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))

        self.rmenu = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','menu.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rplay = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','play.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rpause = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','pause.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rsound = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','sound.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rsound2 = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','sound2.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rclose = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','close.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rback = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','back.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rnext = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','next.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rthema = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','thema.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))       
        self.rconsol = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','consol.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rdown = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','down.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))
        self.rup = pygame.transform.scale(pygame.image.load(os.path.join('icon','retro','up.png')).convert_alpha() , (self.simgeBoyut, self.simgeBoyut))


    def ciz(self):  
        if pencereOzellik.ozelCubukAcik is True:
            if pencereOzellik.modernTema is True:
                self.gorevCubuguCiz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.mCubukRenk, self.cubukKoordinat, border_bottom_left_radius= 10, border_bottom_right_radius= 10)
                self.menuKonum = pencereOzellik.oyunYuzeyi.blit(self.mmenu, (10 , 0))
                self.gizleyiciBolgesiCiz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.mCubukRenk, self.gizleyiciKoordinat,border_bottom_left_radius= 10, border_bottom_right_radius= 10)
                if pencereOzellik.sesAcik is True:
                    self.soundKonum = pencereOzellik.oyunYuzeyi.blit(self.msound, (10 + self.katsayi *1, 0))
                elif pencereOzellik.sesAcik is False:
                    self.soundKonum = pencereOzellik.oyunYuzeyi.blit(self.msound2, (10 + self.katsayi *1, 0))
                if pencereOzellik.duraklat is True:
                    self.playPauseKonum = pencereOzellik.oyunYuzeyi.blit(self.mplay, (10 + self.katsayi *2, 0))
                elif pencereOzellik.duraklat is False:
                    self.playPauseKonum =  pencereOzellik.oyunYuzeyi.blit(self.mpause, (10 + self.katsayi *2, 0))
                self.arrowKonum = pencereOzellik.oyunYuzeyi.blit(self.mup, (((self.gorevCubuguCiz.w /2) - (self.simgeBoyut/2)) , 0))
                self.themaKonum = pencereOzellik.oyunYuzeyi.blit(self.mthema, (self.gorevCubuguCiz.width - self.katsayi *3,0))
                self.consolKonum = pencereOzellik.oyunYuzeyi.blit(self.mconsol, (self.gorevCubuguCiz.width - self.katsayi *2,0))
                self.closeKonum =  pencereOzellik.oyunYuzeyi.blit(self.mclose, (self.gorevCubuguCiz.width - self.katsayi,0))

            elif pencereOzellik.modernTema is False:
                self.gorevCubuguCiz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.rcubukRenk, self.cubukKoordinat, border_bottom_left_radius= 10, border_bottom_right_radius= 10)
                self.menuKonum = pencereOzellik.oyunYuzeyi.blit(self.rmenu, (10 , 0))
                self.gizleyiciBolgesiCiz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.rcubukRenk, self.gizleyiciKoordinat,border_bottom_left_radius= 10, border_bottom_right_radius= 10)
                if pencereOzellik.sesAcik is True:
                    self.soundKonum = pencereOzellik.oyunYuzeyi.blit(self.rsound, (10 + self.katsayi *1, 0))
                elif pencereOzellik.sesAcik is False:
                    self.soundKonum = pencereOzellik.oyunYuzeyi.blit(self.rsound2, (10 + self.katsayi *1, 0))
                if pencereOzellik.duraklat is True:
                    self.playPauseKonum = pencereOzellik.oyunYuzeyi.blit(self.rplay, (10 + self.katsayi *2, 0))
                elif pencereOzellik.duraklat is False:
                    self.playPauseKonum =  pencereOzellik.oyunYuzeyi.blit(self.rpause, (10 + self.katsayi *2, 0))
                self.arrowKonum = pencereOzellik.oyunYuzeyi.blit(self.rup, (((self.gorevCubuguCiz.w /2) - (self.simgeBoyut/2)) , 0))
                self.themaKonum = pencereOzellik.oyunYuzeyi.blit(self.rthema, (self.gorevCubuguCiz.width - self.katsayi *3,0))
                self.consolKonum = pencereOzellik.oyunYuzeyi.blit(self.rconsol, (self.gorevCubuguCiz.width - self.katsayi *2,0))
                self.closeKonum =  pencereOzellik.oyunYuzeyi.blit(self.rclose, (self.gorevCubuguCiz.width - self.katsayi,0))

        elif pencereOzellik.ozelCubukAcik is False:
            if pencereOzellik.modernTema is True:
                self.gizleyiciBolgesiCiz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.mCubukRenk, ( self.gizleyiciKoordinat ) ,border_bottom_left_radius= 15, border_bottom_right_radius= 15)
                self.arrowKonum = pencereOzellik.oyunYuzeyi.blit(self.mdown, (((self.gorevCubuguCiz.w /2) - (self.simgeBoyut/2)) , 0))
            elif pencereOzellik.modernTema is False:
                self.gizleyiciBolgesiCiz = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.rcubukRenk, ( self.gizleyiciKoordinat ) ,border_bottom_left_radius= 15, border_bottom_right_radius= 15)
                self.arrowKonum = pencereOzellik.oyunYuzeyi.blit(self.rdown, (((self.gorevCubuguCiz.w /2) - (self.simgeBoyut/2)) , 0))
            

    def gorevCubuguTiklamaOlaylari(self):
        fare_X, fare_Y = pygame.mouse.get_pos()
        if pencereOzellik.ozelCubukAcik is True:
            if self.menuKonum.collidepoint(fare_X, fare_Y):
                if pencereOzellik.duraklat is False:
                    pencereOzellik.duraklat = True
                pencereOzellik.menu = True
                pencereOzellik.options = False
                pencereOzellik.oyunAktif = False
            elif self.soundKonum.collidepoint(fare_X, fare_Y): #oyun sesi kısma eklenicek buraya unutma.
                if pencereOzellik.sesAcik is True:
                    pencereOzellik.sesAcik = False
                elif pencereOzellik.sesAcik is False:
                    pencereOzellik.sesAcik = True
            elif self.playPauseKonum.collidepoint(fare_X, fare_Y):
                if pencereOzellik.duraklat is True:
                    pencereOzellik.duraklat = False
                    pencereOzellik.oyunAktif = True
                    pencereOzellik.menu = False
                elif pencereOzellik.duraklat is False:
                    pencereOzellik.options = False
                    pencereOzellik.duraklat = True
                    pencereOzellik.oyunAktif = False
                    pencereOzellik.oyunYuzeyi.blit(self.pauseFontCiz,((pencereOzellik.oyunYuzeyi.get_width()/2) - (self.pauseFontCerceveOlcu.w/2), (pencereOzellik.oyunYuzeyi.get_height()/2) -self.pauseFontCerceveOlcu.h/2))      #oyun durunca pauseyi çizdirdiğimiz kod. .

            elif self.arrowKonum.collidepoint(fare_X, fare_Y):
                pencereOzellik.ozelCubukAcik = False
            elif self.themaKonum.collidepoint(fare_X, fare_Y):
                if pencereOzellik.modernTema is True:
                    pencereOzellik.modernTema = False
                elif pencereOzellik.modernTema is False:
                    pencereOzellik.modernTema = True
            elif self.consolKonum.collidepoint(fare_X, fare_Y):   #pencere taşınması için görev çubuğunun kapanıp açılması.
                if pencereOzellik.pencereAktif is True:
                    self.oyunYuzeyi = pygame.display.set_mode((pencereOzellik.ekranYatayBoyut,pencereOzellik.ekranDikeyBoyut), pygame.NOFRAME)
                    pencereOzellik.pencereAktif = False
                elif pencereOzellik.pencereAktif is False:
                    self.oyunYuzeyi = pygame.display.set_mode((pencereOzellik.ekranYatayBoyut,pencereOzellik.ekranDikeyBoyut))
                    pencereOzellik.pencereAktif = True
            elif self.closeKonum.collidepoint(fare_X, fare_Y):
                pencereOzellik.oyunCalisiyor = False
                pygame.quit()
                sys.exit()
            else :
                pass
        elif pencereOzellik.ozelCubukAcik is False:
            if self.arrowKonum.collidepoint(fare_X, fare_Y):
                pencereOzellik.ozelCubukAcik = True

            
GorevCubugu = PencereCubuk() 

menuButonSayisi = 4
play = MenuButonOlustur('PLAY - RESUME', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *0)))      #yazı tipleri bilgisayarda kayıtlı olanları alıyor. stilini değiştirmek  istersne kayıtlı olanların yolu C > Windows > Fonts
restart = MenuButonOlustur('RESTART', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *1)))      #bu yazı tipleri olmayan bilgisayarlarda sorun çıkmasın diye uygulama için kopyalayıp onların yolunu verdim.
options = MenuButonOlustur('OPTIONS', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *2)))         #yatay düzlemde ortaladığımız için sınıf oluştururken x almıyoruz. otomatik hesaplıyoruz x i.
communication = MenuButonOlustur('COMMUNICATION', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *3)))              #mümkün olduğunca sistemli ve ortalı olması için belirli formülle dikey düzlemlerine göre çizdirdim.
menuButonListesi = [play, restart, options, communication]      #menu için buton  oluşturursan listeye dahil et aşağıda döngüyle işlem yapılıyor.




class DAraba:
    def __init__(self):
        self.arabaDusman1 = pygame.image.load(os.path.join('araba','d1.png')).convert_alpha()
        self.arabaDusman2 = pygame.image.load(os.path.join('araba','d2.png')).convert_alpha()
        self.arabaDusman3 = pygame.image.load(os.path.join('araba','d3.png')).convert_alpha()
        self.arabaDusman4 = pygame.image.load(os.path.join('araba','d4.png')).convert_alpha()
        self.arabaDusman5 = pygame.image.load(os.path.join('araba','d5.png')).convert_alpha()
        self.arabaDusman6 = pygame.image.load(os.path.join('araba','d6.png')).convert_alpha()
        self.arabaDusman7 = pygame.image.load(os.path.join('araba','d7.png')).convert_alpha()
    


class Options:
    def __init__(self):
        self.arabaOlcu = (136,200)
        self.okAOlcu = (72,72)
        self.okVSOlcu = (50,50)
        self.secimIndex = 7    
        self.secilenAraba = None
        self.volume = 50
        self.kutularArkaPlan = (240, 246, 213)
        self.yatayOrta = pencereOzellik.oyunYuzeyi.get_width() /2
        self.dikeyOrta = pencereOzellik.oyunYuzeyi.get_height() /2
        self.Font = pygame.font.Font(os.path.join('font','12.ttf'),40)
        self.SagOkA = pygame.transform.scale(pygame.image.load(os.path.join('icon','nextbutton.png')).convert_alpha(),self.okAOlcu)
        self.SolOkA = pygame.transform.scale(pygame.image.load(os.path.join('icon','backbutton.png')).convert_alpha(),self.okAOlcu)
        self.SesSimge = pygame.transform.scale(pygame.image.load(os.path.join('icon','volume.png')).convert_alpha(),self.okVSOlcu)
        self.SagOkV = pygame.transform.scale(pygame.image.load(os.path.join('icon','nextarrow.png')).convert_alpha(),self.okVSOlcu)
        self.SolOkV = pygame.transform.scale(pygame.image.load(os.path.join('icon','backarrow.png')).convert_alpha(),self.okVSOlcu)
        self.arabaSecim1 = pygame.transform.scale(pygame.image.load(os.path.join('araba','1.png')).convert_alpha(),self.arabaOlcu)
        self.arabaSecim2 = pygame.transform.scale(pygame.image.load(os.path.join('araba','2.png')).convert_alpha(),self.arabaOlcu)
        self.arabaSecim3 = pygame.transform.scale(pygame.image.load(os.path.join('araba','3.png')).convert_alpha(),self.arabaOlcu)
        self.arabaSecim4 = pygame.transform.scale(pygame.image.load(os.path.join('araba','4.png')).convert_alpha(),self.arabaOlcu)
        self.arabaSecim5 = pygame.transform.scale(pygame.image.load(os.path.join('araba','5.png')).convert_alpha(),self.arabaOlcu)
        self.arabaSecim6 = pygame.transform.scale(pygame.image.load(os.path.join('araba','6.png')).convert_alpha(),self.arabaOlcu)
        self.arabaSecim7 = pygame.transform.scale(pygame.image.load(os.path.join('araba','7.png')).convert_alpha(),self.arabaOlcu)
        self.arabaKutuOlcu = ((self.yatayOrta) -120 , (self.dikeyOrta) -250 , 240 , 300)       
        self.SagOkAOlcu = (self.yatayOrta +150 , (self.dikeyOrta- self.okAOlcu[1]/2) -100) 
        self.SolOkAOlcu = (self.yatayOrta - (150 +(self.okAOlcu[0])), (self.dikeyOrta - self.okAOlcu[1]/2 ) -100)
        self.sesSimgeolcu = ((self.yatayOrta) - self.okVSOlcu[0]/2 , (self.dikeyOrta) +115)
        self.sesKutuOlcu = (self.yatayOrta -50, self.dikeyOrta +180, 100, 60)
        self.solOkVOlcu = (self.yatayOrta -(80 +self.okVSOlcu[0]), (self.dikeyOrta - self.okVSOlcu[1]/2 )+210)
        self.sagOkVOlcu = (self.yatayOrta + 80, (self.dikeyOrta - self.okVSOlcu[1]/2 )+210)
        
        self.sagOkARect = pygame.Rect(self.SagOkAOlcu[0],self.SagOkAOlcu[1],self.okAOlcu[0],self.okAOlcu[1])        #tıklamalarla işlem görmesi için optionsdaki butonların rect nesnelerinin konumlarını oluşturdum güncel ölçülü halleriyle.
        self.solOkARect = pygame.Rect(self.SolOkAOlcu[0],self.SolOkAOlcu[1],self.okAOlcu[0],self.okAOlcu[1])
        self.sagOkVRect = pygame.Rect(self.sagOkVOlcu[0],self.sagOkVOlcu[1],self.okVSOlcu[0],self.okVSOlcu[1])
        self.solOkVRect = pygame.Rect(self.solOkVOlcu[0],self.solOkVOlcu[1],self.okVSOlcu[0],self.okVSOlcu[1])
        print(self.sagOkARect,self.solOkARect,self.solOkVRect,self.sagOkVRect)
    


        
    def arabaGoster(self):
        if self.secimIndex == 1:
            self.secilenAraba = pencereOzellik.oyunYuzeyi.blit(self.arabaSecim1,(pencereOzellik.oyunYuzeyi.get_width()/2 - self.arabaSecim1.get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.arabaSecim1.get_height()/2 -100))
        elif self.secimIndex == 2:
            self.secilenAraba = pencereOzellik.oyunYuzeyi.blit(self.arabaSecim2,(pencereOzellik.oyunYuzeyi.get_width()/2 - self.arabaSecim2.get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.arabaSecim2.get_height()/2 -100))
        elif self.secimIndex == 3:
            self.secilenAraba = pencereOzellik.oyunYuzeyi.blit(self.arabaSecim3,(pencereOzellik.oyunYuzeyi.get_width()/2 - self.arabaSecim3.get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.arabaSecim3.get_height()/2 -100))
        elif self.secimIndex == 4:
            self.secilenAraba = pencereOzellik.oyunYuzeyi.blit(self.arabaSecim4,(pencereOzellik.oyunYuzeyi.get_width()/2 - self.arabaSecim4.get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.arabaSecim4.get_height()/2 -100))
        elif self.secimIndex == 5:
            self.secilenAraba = pencereOzellik.oyunYuzeyi.blit(self.arabaSecim5,(pencereOzellik.oyunYuzeyi.get_width()/2 - self.arabaSecim5.get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.arabaSecim5.get_height()/2 -100))
        elif self.secimIndex == 6:
            self.secilenAraba = pencereOzellik.oyunYuzeyi.blit(self.arabaSecim6,(pencereOzellik.oyunYuzeyi.get_width()/2 - self.arabaSecim6.get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.arabaSecim6.get_height()/2 -100))
        elif self.secimIndex == 7:
            self.secilenAraba = pencereOzellik.oyunYuzeyi.blit(self.arabaSecim7,(pencereOzellik.oyunYuzeyi.get_width()/2 - self.arabaSecim7.get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.arabaSecim7.get_height()/2 -100))
        else:
            pass
    
    

    def optionsCizimler(self):
        pencereOzellik.oyunYuzeyi.blit(pencereOzellik.optionsArkaPlan,(0,0))
        arabaKutu = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.kutularArkaPlan, self.arabaKutuOlcu , border_radius=30)
        pencereOzellik.oyunYuzeyi.blit(self.SagOkA, self.SagOkAOlcu)
        pencereOzellik.oyunYuzeyi.blit(self.SolOkA, self.SolOkAOlcu)
        pencereOzellik.oyunYuzeyi.blit(self.SesSimge, self.sesSimgeolcu)
        sesKutu = pygame.draw.rect(pencereOzellik.oyunYuzeyi, self.kutularArkaPlan, self.sesKutuOlcu , border_radius=10)
        sesSeviyesi = self.Font.render(f'{self.volume}',True,(0,0,0))
        sesSeviyesOlcu = sesSeviyesi.get_rect()
        pencereOzellik.oyunYuzeyi.blit(sesSeviyesi,(sesKutu.centerx - sesSeviyesOlcu.w/2, sesKutu.centery - sesSeviyesOlcu.h/2))
        pencereOzellik.oyunYuzeyi.blit(self.SolOkV, self.solOkVOlcu)
        pencereOzellik.oyunYuzeyi.blit(self.SagOkV, self.sagOkVOlcu)
        self.arabaGoster()

        '''pencereOzellik.oyunYuzeyi.blit(pencereOzellik.optionsArkaPlan,(0,0))    #options genel arka plan
        arabaKutu = pygame.draw.rect(pencereOzellik.oyunYuzeyi,self.ArabaArkaPlanAraba, [(pencereOzellik.oyunYuzeyi.get_width() /2) -120 , (pencereOzellik.oyunYuzeyi.get_height()/2) -150 , 240 , 300],border_radius= 30)     #secilen arabanın belli olması için araba arkasının planı.
        pencereOzellik.oyunYuzeyi.blit(self.SagOkA,(arabaKutu.midright[0] +25, arabaKutu.midright[1]-(self.SagButtonA.h/2)))    #araba değişim sağ ok konumlama
        pencereOzellik.oyunYuzeyi.blit(self.SolOkA,(arabaKutu.midleft[0] - (self.SolButtonA.w + 25), arabaKutu.midright[1]-(self.SolButtonA.h/2)))     #araba değişim sol ok konumlama, ok sol üst kenarından yerleştirilmeye başlandığı için sol kısma yerleştirirken genişliğinide alıyoruz.
        sesKutu = pygame.draw.rect(pencereOzellik.oyunYuzeyi,self.ArabaArkaPlanAraba, [arabaKutu.x +80 , arabaKutu.y -100, arabaKutu.w -160 , 50],border_radius=15)
        pencereOzellik.oyunYuzeyi.blit(self.SagOkV,(sesKutu.midright[0] +15, sesKutu.midright[1]-(self.SagButtonV.h/2)))      #sesin sag oku
        pencereOzellik.oyunYuzeyi.blit(self.SolOkV,(sesKutu.midleft[0] - (self.SolButtonV.w +15), sesKutu.midleft[1]-(self.SolButtonV.h/2)))       #sesin sol oku
        pencereOzellik.oyunYuzeyi.blit(self.Ses,(sesKutu.midleft[0] -150, sesKutu.midleft[1] -self.SagButtonV.h/2))   #ses simgesi
        sesSeviyesi = self.Font.render(f'{self.volume}',True,(0,0,0))
        sesSeviyesiOlculeri = sesSeviyesi.get_rect()
        pencereOzellik.oyunYuzeyi.blit(sesSeviyesi,(sesKutu.centerx - sesSeviyesiOlculeri.w/2, sesKutu.centery - sesSeviyesiOlculeri.h/2))
        self.arabaGoster()'''
    
    def butonGorevler(self):
        fareX, fareY = pygame.mouse.get_pos()
        if self.solOkARect.collidepoint(fareX, fareY):
            if self.secimIndex > 1:
                self.secimIndex -= 1
            elif self.secimIndex == 1:
                self.secimIndex = 7
        elif self.sagOkARect.collidepoint(fareX,fareY):
            if self.secimIndex < 7:
                self.secimIndex += 1
            elif self.secimIndex == 7:
                self.secimIndex = 1
        elif self.solOkVRect.collidepoint(fareX,fareY):
            if self.volume >= 5 :
                self.volume -= 5
        elif self.sagOkVRect.collidepoint(fareX,fareY):
            if self.volume <= 95:
                self.volume += 5
        else:
            pass




optionsObj = Options()

      

def oyunaGec():
    
    ##########      Genel Çizimler          ##############
    pencereOzellik.oyunYuzeyi.fill((0,0,0))
    pygame.draw.rect(pencereOzellik.oyunYuzeyi, pencereOzellik.disKenarRenk ,[25,0,750,1100])    
    pygame.draw.rect(pencereOzellik.oyunYuzeyi, pencereOzellik.icKenarRenk ,[125,0,550,1100])

    ##########      Agaç Konum Ve Hareketleri       ##############
    ''' global solAgacListesi,sagAgacListesi    #bunu yapmayınca liste adı globalmi değilmi anlamayıp hata veriyor o yüzden heryerden erişilebilir olması için global yaptık.
    solAgacListesi = [agaclar for agaclar in solAgacListesi if agaclar.solAgacY <= pencereOzellik.ekranDikeyBoyut]     #liste üreteci deniyor buna. solağaçlistesindeki elemanların y konumlarını ekranın alt bitiş noktasıyla karşılaştırıp koşula uyan yani sadece ekranın içinde olan ağaçları listeye alıyor. ekranın dışına çıkan ağaçları sonsuzluğa varmaması için siliyor.
    for agaclar in solAgacListesi:      
        agaclar.solKenarAgac()
    sagAgacListesi = [agaclar for agaclar in sagAgacListesi if agaclar.sagAgacY <= pencereOzellik.ekranDikeyBoyut]     
    for agaclar in sagAgacListesi:
        agaclar.sagKenarAgac()
        '''
    ##########      Şerit konumları ve hareketleri       ##############
    seritListesi = [ilkSiraSerit, ikinciSiraSerit, ucuncuSiraSerit, dorduncuSiraSerit, besinciSiraSerit, altinciSiraSerit]
    for seritler in seritListesi:
        seritler.seritCiz(pencereOzellik.oyunHizi)
        if seritler.konumY > pencereOzellik.ekranDikeyBoyut :  #seritlerin ekranın dışına çıkınca yukardan tekrar inmesi için.
            seritler.konumY = - seritler.seritUzunluk



def menuyeGec():
    pencereOzellik.oyunYuzeyi.blit(pencereOzellik.menuArkaPlan,(0,0))   #her defasında resmi tekrar tekrar yüklemesin diye pencere ilk oluştururken yüklenen resmi kullanıyoruz.
    play.menuButonEfekt(pencereOzellik.oyunYuzeyi)
    restart.menuButonEfekt(pencereOzellik.oyunYuzeyi)
    options.menuButonEfekt(pencereOzellik.oyunYuzeyi)
    communication.menuButonEfekt(pencereOzellik.oyunYuzeyi)
    pygame.display.update()


def communicationGec():
    pencereOzellik.oyunYuzeyi.blit(pencereOzellik.communicationArkaPlan,(0,0))
    mail = pencereOzellik.communicationYaziAyar.render('abdullah.tosun.9696@gmail.com',True,(0,0,0))
    github = pencereOzellik.communicationYaziAyar.render('https://github.com/Abdullahtsn',True,(20,20,20))
    pencereOzellik.oyunYuzeyi.blit(mail,((pencereOzellik.oyunYuzeyi.get_width()/2 - mail.get_width()/2), (pencereOzellik.oyunYuzeyi.get_height()/2 - mail.get_height()/2)-70 ))
    pencereOzellik.oyunYuzeyi.blit(github,((pencereOzellik.oyunYuzeyi.get_width()/2 - github.get_width()/2), (pencereOzellik.oyunYuzeyi.get_height()/2 - github.get_height()/2) +30))
    


    
    
        
    


def oyunCalistir():
    while pencereOzellik.oyunCalisiyor: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pencereOzellik.oyunCalisiyor = False
                pygame.quit()
                sys.exit()
            

            if event.type == pygame.MOUSEBUTTONUP:        #down ile upu ayırmayınca kafası karışıyor olayları karıştırıyor. görev çubuğu işlemlerini tuşu bırakıncaya atadım.
                GorevCubugu.gorevCubuguTiklamaOlaylari()
                
                            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pencereOzellik.menu is True:
                    for buton in menuButonListesi:
                        if buton.cerceve.x <= fareX  <= buton.cerceve.x + buton.cerceve.width and buton.cerceve.y <= fareY <= buton.cerceve.y + buton.cerceve.height:
                            buton.butonTiklamaEfekt()
                            buton.butonGorev()
                elif pencereOzellik.options is True:
                    optionsObj.butonGorevler()

                
                

        if pencereOzellik.menu is True:     #menü çizimi ve efektler.
            pencereOzellik.oyunAktif = False
            menuyeGec()
            fareX, fareY = pygame.mouse.get_pos()
            for buton in menuButonListesi:
                if buton.cerceve.x <= fareX  <= buton.cerceve.x + buton.cerceve.width and buton.cerceve.y <= fareY <= buton.cerceve.y + buton.cerceve.height:
                    buton.butonEfektAktif = True
                else:
                    buton.butonEfektAktif = False
                buton.menuButonEfekt(pencereOzellik.oyunYuzeyi)
        
        elif  pencereOzellik.menu is False and pencereOzellik.oyunAktif is True and pencereOzellik.duraklat is False:         #oyun şemaları çizimi
            oyunaGec()      #yapılıcak tekrarlı çizimkileri bu fonksiyon içine yaz.

        elif pencereOzellik.menu is False and pencereOzellik.oyunAktif is False and pencereOzellik.communication is True:
            communicationGec()
            pencereOzellik.communication = False    #böyle yapmamızın sebebi sadece bir defa çizip durması, sabit bişeyi defalarca çizmemesi için
        
        elif pencereOzellik.menu is False and pencereOzellik.oyunAktif is False and pencereOzellik.options is True :
            optionsObj.optionsCizimler()
            
            

        GorevCubugu.ciz()       #bunun en altta olmasının sebebi en son çizilip en üstte görünmesi görev çubuğunun
        
        pygame.display.flip()       #güncelleme için.
        pencereOzellik.fps.tick(50)
        

if __name__ == '__main__':      #bu bloğun anlamı: sadece bu py dosyası doğrudan çalıştırılıyorsa oyun menü sınıfı oluşturulup işlemler gerçekleştiricek demek,
    oyunCalistir()                  #eğer bu py dosyası import edilirse o zaman bu blok çalıştırılmıycak demektir.
    
        



