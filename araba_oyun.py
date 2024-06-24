import pygame
import random
import sys
import os



if getattr(sys,'frozen', False):        #exe çalışıyorsa dosyaların açılması için onun yolunu alcak. script çalışıyorsa konumu mevcut olan ayarlancak.
    os.chdir(sys._MEIPASS)
else:                       
    os.chdir('.')


pygame.init()
pygame.mixer.init()


class Pencere:
    def __init__(self) :
        self.oyunCalisiyor = True
        self.menu = True
        self.oyunAktif = False
        self.options = False
        self.communication = False
        self.oyunSonu = False
        self.oyunSonuMuzigi = True
        self.oyunMuzikBastanBasla = True
        self.oyunMuzigiDurakladı = False
        self.modernTema = True
        self.sesAcik = True
        self.duraklat = True
        self.muzikDegistir = False
        self.pencereAktif = False
        self.ozelCubukAcik = False
        self.solTusBasili = False
        self.sagTusBasili = False
        self.altTusBasili = False
        self.ustTusBasili= False
        self.seviye = 1
        self.oyunHizi = 8
        self.puan = 0
        self.menuButonlarıBosluk = 175
        self.icKenarRenk = (128,128,128)
        self.disKenarRenk = (180,238,180)
        self.ekranDikeyBoyut = 1100
        self.ekranYatayBoyut = 800
        self.fps = pygame.time.Clock()
        self.oyunYuzeyi = pygame.display.set_mode((self.ekranYatayBoyut,self.ekranDikeyBoyut), pygame.NOFRAME)  #noframe windosun penceresini kapatıyor.  #doublebuf çift tamponlama yapıyor. değişiklikleri başka bi yüzde tutup sonrasında anayüzeye kopyalıyor. resimlerdeki titreme gibi şeyleri engelleyebiliyor ama ek kaynak kullanımı gibi durumları var o yüzden kullanmıyorum. diğer işletim sistemlerindede uyumsuzluğa yol açabiliyor. performans ve kaynak tüketimi artırıyor.
        self.icon = pygame.image.load(os.path.join('icon','simge.ico'))
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption('RACE CAR')      #pencere başlığı, iconda ekleniyor sonra bak
        self.menuArkaPlan = pygame.transform.scale(pygame.image.load(os.path.join('resim','1.jpg')),(self.ekranYatayBoyut,self.ekranDikeyBoyut))
        self.communicationArkaPlan = pygame.transform.scale(pygame.image.load(os.path.join('resim','2.jpg')),(self.ekranYatayBoyut,self.ekranDikeyBoyut))
        self.communicationYaziAyar = pygame.font.Font(os.path.join('font','5.TTF'),40)
        self.optionsArkaPlan = pygame.image.load(os.path.join('resim','3.jpg'))             #burda optionsda görünecek resmi yükleyip,
        self.optionsArkaPlan = pygame.transform.rotate(self.optionsArkaPlan,90)             #resmin normal görünüşü yataya uygun olduğu için dikey boyutlanınca iyi görünmüyor o yüzden 90 derece döndürüp
        self.optionsArkaPlan = pygame.transform.scale(self.optionsArkaPlan,(self.ekranYatayBoyut,self.ekranDikeyBoyut))     #ekrana göre ölçeklemesini yapıyoruz. hepsini aynı değişkene atıp ona işlem yaptıkki farklı farklı değişkenler oluşmasın. eldeki değişkeni güncelledik sürekli
        self.oyunSonuYaziAyar = pygame.font.Font(os.path.join('font','13.ttf'),75)
        self.oyunSonuArkaPlan = pygame.transform.scale(pygame.image.load(os.path.join('resim','7.jpg')),(self.ekranYatayBoyut +50,self.ekranDikeyBoyut))     #score yazısını ay resmine ortalasın diye ekranın biraz soluncan başlatıcaz o yüzden xi biraz büyük alıyoruz.

    def herseyiSifirla(self):
        oyunIciSeviyeAyarlari.sagAgacListesi = []       #değişkenler ve listeler üzerinden yapılan tüm işlemleri sıfırlıyoruz ki en baştan başlasın
        oyunIciSeviyeAyarlari.solAgacListesi = []
        oyunIciSeviyeAyarlari.engelListesi = []
        self.seviye = 1
        self.puan = 0
        self.oyunHizi = 8
        self.oyunAktif = False
        self.options = False
        self.duraklat = True
        self.oyunSonuMuzigi = True
        self.oyunMuzigiDurakladı = False
        self.oyunMuzikBastanBasla = True
        self.tuslariSerbestBirak()
        arabaObj.x = pencereOzellik.oyunYuzeyi.get_width()/2 - arabaObj.genislik/2
        arabaObj.y = pencereOzellik.oyunYuzeyi.get_height() - 215

    def tuslariSerbestBirak(self):          #oyun ekranından  çıkınca eğer bi tuş basılıysa o true olarak kalıp tuşa basılıymış gibi devam ediyor. o yüzden hepsini false olarak ayarlıyoruz
            self.altTusBasili = False
            self.ustTusBasili = False
            self.solTusBasili = False
            self.sagTusBasili = False
            

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
    agacListesi = [pygame.transform.scale(pygame.image.load(os.path.join('agac',f'{i}.png')).convert_alpha(),(70, 70)) for i in range(1,22)]    #initten önce tanımlayıp oluşturulcak olan yüzlerce ağaç için tekrar tekrar yüklenmesinin önüne geçtik sadece bir kere yüklenip sonrakilerde bu yüklenen kullanılcak.
    def __init__(self):
        self.agacGenislik = 70
        self.agacYukseklik = 70
        self.solAgacX = ((0 + oyunIciSeviyeAyarlari.IcKenarOlcu[0]) /2) - (self.agacGenislik/2)
        self.sagAgacX = (oyunIciSeviyeAyarlari.IcKenarOlcu[0] + oyunIciSeviyeAyarlari.IcKenarOlcu[2]) + (( pencereOzellik.oyunYuzeyi.get_width() - oyunIciSeviyeAyarlari.IcKenarOlcu[0] - oyunIciSeviyeAyarlari.IcKenarOlcu[2]) /2 - self.agacGenislik/2)
        self.agacY = -94     #ekranın üst kısımdan başlayarak inmesi için. y koordinatı ikisindede aynı ilerleyişte  olcağı için tek değişken
        self.seviyeResim = None
        self.seviyeyeAyarla()   
        

    def seviyeyeAyarla(self):                                   #amacı ; bulunulan seviyeye göre ayrılan 3 görselden rasgele bir tanesini seçip kullanması için
        if pencereOzellik.seviye == 1:
            self.seviyeResim = AgacOlustur.agacListesi[0:3]
        elif pencereOzellik.seviye == 2:
            self.seviyeResim = AgacOlustur.agacListesi[3:6]
        elif pencereOzellik.seviye == 3:
            self.seviyeResim = AgacOlustur.agacListesi[6:9]
        elif pencereOzellik.seviye == 4:
            self.seviyeResim = AgacOlustur.agacListesi[9:12]
        elif pencereOzellik.seviye == 5:
            self.seviyeResim = AgacOlustur.agacListesi[12:15]
        elif pencereOzellik.seviye == 6:
            self.seviyeResim = AgacOlustur.agacListesi[15:18]
        elif pencereOzellik.seviye == 7:
            self.seviyeResim = AgacOlustur.agacListesi[15:18]
        elif pencereOzellik.seviye == 8:
            self.seviyeResim = AgacOlustur.agacListesi[18:]
        self.secilen = self.seviyeResim[random.randint(0,2)]
    
    def agacCiz(self,bolge):
        if bolge == 'sol':
            pencereOzellik.oyunYuzeyi.blit(self.secilen,(self.solAgacX, self.agacY))
        elif bolge == 'sag':
            pencereOzellik.oyunYuzeyi.blit(self.secilen,(self.sagAgacX, self.agacY))
        self.agacY += pencereOzellik.oyunHizi
    

ilkSiraSerit = SeritOlustur(100)
ikinciSiraSerit = SeritOlustur(300)
ucuncuSiraSerit = SeritOlustur(500)
dorduncuSiraSerit = SeritOlustur(700)
besinciSiraSerit = SeritOlustur(900)
altinciSiraSerit = SeritOlustur(1100)
     
def seritAyarlamalari():
    seritListesi = [ilkSiraSerit, ikinciSiraSerit, ucuncuSiraSerit, dorduncuSiraSerit, besinciSiraSerit, altinciSiraSerit]
    for seritler in seritListesi:
        seritler.seritCiz(pencereOzellik.oyunHizi)
        if seritler.konumY > pencereOzellik.ekranDikeyBoyut :  #seritlerin ekranın dışına çıkınca yukardan tekrar inmesi için.
            seritler.konumY = - seritler.seritUzunluk


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
        self.metinPasif = fontOzellik.render( self.metinYazi, netlik , self.yaziPasifRenk)          #burdaki antialias metni pürüzsüzleştirmeyle alakalı, true yaparsan metnin kenarları daha yumuşak oluyor.
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
        sesler.menuButonSes()         #menüdeki tüm butonlar için tıklanınca kenarlık resmi çizen fonksiyona koyup tüm butonlar için tek satırlık ses komutu koyduk, yoksa aşağıda her buton için ayrı ayrı koycaktık.
        pygame.time.delay(100)        #bu oyun döngüsünü duraklatmıyor
        #pygame.time.wait(5000)       #bu döngüyü duraklatıyor
        

    def butonGorev(self):
        if self.metinYazi == 'PLAY - RESUME':
            pencereOzellik.menu = False
            pencereOzellik.oyunAktif = True
            pencereOzellik.duraklat = False
            pencereOzellik.options = False
        elif self.metinYazi == 'RESTART':
            pencereOzellik.herseyiSifirla()
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
        self.rcubukRenk = (169,122,239)
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
            

    def gorevCubuguTiklamaOlaylari(self):               #görev çubuğundaki tıklamalarda ses oynatması için her butonun collidepointin içine yazdık. fonksiyon en altına yazınca nereye basarsan ses çalıyor.
        fare_X, fare_Y = pygame.mouse.get_pos()         #collidepointte buton konumunun tıklanmasıyla görevler gerçekleştiği için ses çalmalarıda oralara yazdık.
        if pencereOzellik.ozelCubukAcik is True:
            if self.menuKonum.collidepoint(fare_X, fare_Y):
                if pencereOzellik.duraklat is False:
                    pencereOzellik.duraklat = True
                pencereOzellik.menu = True
                pencereOzellik.oyunAktif = False
                pencereOzellik.options = False
                pencereOzellik.oyunAktif = False
                pencereOzellik.communication = False 
                pencereOzellik.oyunSonu = False
                sesler.gorevButonSes() 
            elif self.soundKonum.collidepoint(fare_X, fare_Y): 
                if pencereOzellik.sesAcik is True:
                    pencereOzellik.sesAcik = False
                elif pencereOzellik.sesAcik is False:
                    pencereOzellik.sesAcik = True
                sesler.gorevButonSes()
                sesler.sesSeviyesiAyarla()
            elif self.playPauseKonum.collidepoint(fare_X, fare_Y):
                if pencereOzellik.duraklat is True:
                    pencereOzellik.duraklat = False
                    pencereOzellik.oyunAktif = True
                    pencereOzellik.menu = False
                    pencereOzellik.oyunSonu = False
                elif pencereOzellik.duraklat is False:
                    pencereOzellik.options = False
                    pencereOzellik.duraklat = True
                    pencereOzellik.oyunAktif = False
                    pencereOzellik.communication = False 
                    pencereOzellik.oyunSonu = False
                     
                sesler.gorevButonSes()
            elif self.arrowKonum.collidepoint(fare_X, fare_Y):
                pencereOzellik.ozelCubukAcik = False
                sesler.gorevButonSes()
            elif self.themaKonum.collidepoint(fare_X, fare_Y):
                if pencereOzellik.modernTema is True:
                    pencereOzellik.modernTema = False
                elif pencereOzellik.modernTema is False:
                    pencereOzellik.modernTema = True
                sesler.gorevButonSes()
            elif self.consolKonum.collidepoint(fare_X, fare_Y):   #pencere taşınması için görev çubuğunun kapanıp açılması.
                if pencereOzellik.pencereAktif is True:
                    self.oyunYuzeyi = pygame.display.set_mode((pencereOzellik.ekranYatayBoyut,pencereOzellik.ekranDikeyBoyut), pygame.NOFRAME)
                    pencereOzellik.pencereAktif = False
                elif pencereOzellik.pencereAktif is False:
                    self.oyunYuzeyi = pygame.display.set_mode((pencereOzellik.ekranYatayBoyut,pencereOzellik.ekranDikeyBoyut))
                    pencereOzellik.pencereAktif = True
                sesler.gorevButonSes()
            elif self.closeKonum.collidepoint(fare_X, fare_Y):
                pencereOzellik.oyunCalisiyor = False
                pygame.quit()
                sys.exit()
            else :
                pass
            
        elif pencereOzellik.ozelCubukAcik is False:
            if self.arrowKonum.collidepoint(fare_X, fare_Y):
                pencereOzellik.ozelCubukAcik = True
                sesler.gorevButonSes()

            
GorevCubugu = PencereCubuk() 

menuButonSayisi = 4
play = MenuButonOlustur('PLAY - RESUME', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *0)))      #yazı tipleri bilgisayarda kayıtlı olanları alıyor. stilini değiştirmek  istersne kayıtlı olanların yolu C > Windows > Fonts
restart = MenuButonOlustur('RESTART', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *1)))      #bu yazı tipleri olmayan bilgisayarlarda sorun çıkmasın diye uygulama için kopyalayıp onların yolunu verdim.
options = MenuButonOlustur('OPTIONS', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *2)))         #yatay düzlemde ortaladığımız için sınıf oluştururken x almıyoruz. otomatik hesaplıyoruz x i.
communication = MenuButonOlustur('COMMUNICATION', 40, (((pencereOzellik.oyunYuzeyi.get_height() - GorevCubugu.gorevCubuguCiz.height) / menuButonSayisi) + GorevCubugu.gorevCubuguCiz.height/2 + (pencereOzellik.menuButonlarıBosluk *3)))              #mümkün olduğunca sistemli ve ortalı olması için belirli formülle dikey düzlemlerine göre çizdirdim.
menuButonListesi = [play, restart, options, communication]      #menu için buton  oluşturursan listeye dahil et aşağıda döngüyle işlem yapılıyor.



class Options:
    def __init__(self):
        self.arabaOlcu = (136,200)
        self.okAOlcu = (72,72)
        self.okVSOlcu = (50,50)
        self.secimIndex = 1    
        self.secilenAraba = None
        self.volume = 15
        self.kutularArkaPlan = (240, 246, 213)
        self.yatayOrta = pencereOzellik.oyunYuzeyi.get_width() /2
        self.dikeyOrta = pencereOzellik.oyunYuzeyi.get_height() /2
        self.Font = pygame.font.Font(os.path.join('font','12.ttf'),40)
        self.SagOkA = pygame.transform.scale(pygame.image.load(os.path.join('icon','nextbutton.png')).convert_alpha(),self.okAOlcu)
        self.SolOkA = pygame.transform.scale(pygame.image.load(os.path.join('icon','backbutton.png')).convert_alpha(),self.okAOlcu)
        self.SesSimge = pygame.transform.scale(pygame.image.load(os.path.join('icon','volume.png')).convert_alpha(),self.okVSOlcu)
        self.SagOkV = pygame.transform.scale(pygame.image.load(os.path.join('icon','nextarrow.png')).convert_alpha(),self.okVSOlcu)
        self.SolOkV = pygame.transform.scale(pygame.image.load(os.path.join('icon','backarrow.png')).convert_alpha(),self.okVSOlcu)
        self.arabaResim = [(pygame.image.load(os.path.join('araba',f'{i}.png')).convert_alpha()) for i in range(1,15)]             #bu resimleri transformun içine yazmayıp burda değişken olarak tutmamın sebebi oyun için farklı ölçeklerde kullanmak için. scale kullanıldıktan sonra tekrar boyutlama yapılamıyor
        self.optionsArabaListe = [(pygame.transform.scale(i,self.arabaOlcu)) for i in self.arabaResim]  #bu şekilde bi liste üreteci oluşturarak aşağıdaki şekilde hepsini tek tek yazma ve değişkene atama işleminden kurtulmuş olduk.
                                                                                                                                                #aynı zamanda kod olarak daha az göründüğü için kafa karıştırıcılığıda azaldı. hemde daha düzenli ve performans açısından daha iyi oldu.
        '''self.arabaSecim1 = pygame.transform.scale(self.arabaResim1.convert_alpha(),self.arabaOlcu)
        self.arabaSecim2 = pygame.transform.scale(self.arabaResim2.convert_alpha(),self.arabaOlcu)
        self.arabaSecim3 = pygame.transform.scale(self.arabaResim3.convert_alpha(),self.arabaOlcu)
        self.arabaSecim4 = pygame.transform.scale(self.arabaResim4.convert_alpha(),self.arabaOlcu)
        self.arabaSecim5 = pygame.transform.scale(self.arabaResim5.convert_alpha(),self.arabaOlcu)
        self.arabaSecim6 = pygame.transform.scale(self.arabaResim6.convert_alpha(),self.arabaOlcu)
        self.arabaSecim7 = pygame.transform.scale(self.arabaResim7.convert_alpha(),self.arabaOlcu)'''

        self.arabaKutuOlcu = ((self.yatayOrta) -120 , (self.dikeyOrta) -230 , 240 , 300)       
        self.SagOkAOlcu = (self.yatayOrta +150 , (self.dikeyOrta- self.okAOlcu[1]/2) -80) 
        self.SolOkAOlcu = (self.yatayOrta - (150 +(self.okAOlcu[0])), (self.dikeyOrta - self.okAOlcu[1]/2 ) -80)
        self.sesSimgeolcu = ((self.yatayOrta) - self.okVSOlcu[0]/2 , (self.dikeyOrta) +135)
        self.sesKutuOlcu = (self.yatayOrta -50, self.dikeyOrta +200, 100, 60)
        self.solOkVOlcu = (self.yatayOrta -(80 +self.okVSOlcu[0]), (self.dikeyOrta - self.okVSOlcu[1]/2 )+230)
        self.sagOkVOlcu = (self.yatayOrta + 80, (self.dikeyOrta - self.okVSOlcu[1]/2 )+230)
        
        self.sagOkARect = pygame.Rect(self.SagOkAOlcu[0],self.SagOkAOlcu[1],self.okAOlcu[0],self.okAOlcu[1])        #tıklamalarla işlem görmesi için optionsdaki butonların rect nesnelerinin konumlarını oluşturdum güncel ölçülü halleriyle.
        self.solOkARect = pygame.Rect(self.SolOkAOlcu[0],self.SolOkAOlcu[1],self.okAOlcu[0],self.okAOlcu[1])
        self.sagOkVRect = pygame.Rect(self.sagOkVOlcu[0],self.sagOkVOlcu[1],self.okVSOlcu[0],self.okVSOlcu[1])
        self.solOkVRect = pygame.Rect(self.solOkVOlcu[0],self.solOkVOlcu[1],self.okVSOlcu[0],self.okVSOlcu[1])
        
        
    def arabaGoster(self):
        pencereOzellik.oyunYuzeyi.blit((self.optionsArabaListe[self.secimIndex -1]), (pencereOzellik.oyunYuzeyi.get_width()/2 - self.optionsArabaListe[self.secimIndex -1].get_width()/2  ,pencereOzellik.oyunYuzeyi.get_height()/2 - self.optionsArabaListe[self.secimIndex -1].get_height()/2 -80))
        #yukardaki şekilde yazarak aşağıdaki blokları ifade ettik hem karışıklığı hem gereksiz işlemleri azalttık. bu fonksiyondaki yorum satırlarıyla yukardaki tek satır aynı işlevi görüyor. initteki optionArabaListesindede bu yöntemi kullandım.
        '''if self.secimIndex == 1:
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
            pass'''
    
    
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
        

    def butonGorevler(self):
        fareX, fareY = pygame.mouse.get_pos()
        if self.solOkARect.collidepoint(fareX, fareY):
            if self.secimIndex > 1:
                self.secimIndex -= 1
            elif self.secimIndex == 1:
                self.secimIndex = 14
            sesler.optionsButonSes() 
        elif self.sagOkARect.collidepoint(fareX,fareY):
            if self.secimIndex < 14:
                self.secimIndex += 1
            elif self.secimIndex == 14:
                self.secimIndex = 1
            sesler.optionsButonSes()
        elif self.solOkVRect.collidepoint(fareX,fareY):
            if self.volume >= 5 :
                self.volume -= 5
            sesler.sesSeviyesiAyarla()
            sesler.optionsButonSes()
        elif self.sagOkVRect.collidepoint(fareX,fareY):
            if self.volume <= 95:
                self.volume += 5
            sesler.sesSeviyesiAyarla()
            sesler.optionsButonSes()
        else:
            pass
        arabaObj.secilenArabaOlcuAyarla()           #optionsda herhangi bişeye tıklandıktan sonra oyun ordaki görselin oyun  içinde boyutlanması için


optionsObj = Options()


class Araba(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.genislik = 45
        self.yukseklik = 67

        self.x = pencereOzellik.oyunYuzeyi.get_width()/2 - self.genislik/2
        self.y = pencereOzellik.oyunYuzeyi.get_height() - 215
        self.arabaListe = [optionsObj.arabaResim[i] for i in range(0,14)]
        '''self.arabaListe = [getattr(optionsObj,f'arabaResim{i}') for i in range(1,15)]        #self.arabaListe = [f'optionsObj.arabaResim{i}' for i in range(1,8)] bu şekilde yazınca düz olarak algılayıp hata veriyor listeyi yazdırınca düz yazı olarak kaydettiğini gördüm.
                                                                                            #o yüzden ya listenin tüm elemanlarının adlarını tek tek yazıcam yada döngüyle çalışabilmesi için getattr kullanıcam. getattr sınıfın niteliklerine güncel olarak erişmek istediğinde kullanışlı.
                                                                                            #anlamı ; getattr(x, 'y') x.y'ye eşdeğerdir...getattr() fonksiyonu, bir nesnenin belirli bir özelliğine (attribute) dinamik olarak erişmenizi sağlar. Bu özellik, nesnenin özelliğinin adıyla birlikte fonksiyona iletilir.
        '''
        self.sAraba = pygame.transform.scale(self.arabaListe[optionsObj.secimIndex-1],(self.genislik, self.yukseklik))
        self.secilenArabaOlcuAyarla()                                                       #obje oluşturulurken bir kere çalıştırılması ve none döndürmemesi için.
        self.rect = self.sAraba.get_rect()                                                  #aşağıdaki fonksiyona gönderilip resmin bir kere tanımlanmasından sonra rectini alıyoruz.
        self.mask = pygame.mask.from_surface(self.sAraba)                                   #resimlerin çarpışmasını kare olarak hesaplayıp ona göre yapmak pek doğru gelmiyor. ilk önce rectlerini(karelerini) hesaplıycaz çarpışıyormu diye,
       
        '''self.ArabaSpriteGrubu = pygame.sprite.Group()
        self.ArabaSpriteGrubu.add(self)                                                     #maskesini çizebilmek için sprite grubundan oluşturulan listeye sadece arabayı dahil ediyoruz. engelle için ayrı bi liste yaptık zaten.
        '''
    def secilenArabaOlcuAyarla(self):
        self.sAraba = pygame.transform.scale(self.arabaListe[optionsObj.secimIndex-1],(self.genislik, self.yukseklik))  #burda secim indexi initte eşitleyince sabit kalıyor değişmiyor. güncel olarak değişsin diye böyle atadım.
        
    def secileniCiz(self):
        pencereOzellik.oyunYuzeyi.blit(self.sAraba,(self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y
    
    def tusKontrolleri(self):
        if pencereOzellik.solTusBasili is True:
            if self.x > oyunIciSeviyeAyarlari.IcKenarOlcu[0]:
                self.x -= pencereOzellik.oyunHizi/3*2
            else:
                pass
        if pencereOzellik.sagTusBasili is True:
            if self.x + self.genislik < oyunIciSeviyeAyarlari.IcKenarOlcu[0] + oyunIciSeviyeAyarlari.IcKenarOlcu[2]:
                self.x += pencereOzellik.oyunHizi/3*2
            else:
                pass 
        if pencereOzellik.altTusBasili is True:
            if self.y + self.yukseklik +25 < pencereOzellik.oyunYuzeyi.get_height() - (oyunIciSeviyeAyarlari.bilgiKutuOlcu[3]):
                self.y += pencereOzellik.oyunHizi/3*2
            else:
                pass
        if pencereOzellik.ustTusBasili is True:
            if self.y > pencereOzellik.oyunYuzeyi.get_height() - pencereOzellik.oyunYuzeyi.get_height() /2 - self.yukseklik:
                self.y -= pencereOzellik.oyunHizi/3*2

        self.rect.x = self.x              #eğer rectlerini güncellemezsek ilk iki eleman sürekli 0,0 olarak görülüyor ve sol üst köşedeymiş gibi gösteriyor.
        self.rect.y = self.y              #o yüzden her hareket sonrası rectlerini güncelliyoruz.
        

arabaObj = Araba()



class Engeller(pygame.sprite.Sprite):
    bariyerResimListesi = [pygame.image.load(os.path.join('engeller',f'{i}.png')).convert_alpha() for i in range(1,9)] 
    arabaResimListesi = [pygame.transform.scale(pygame.image.load(os.path.join('engeller',f'{i}.png')).convert_alpha(),(53,77)) for i in range(9,16)]
    sagUcakResimListesi = [pygame.image.load(os.path.join('engeller',f'{i}.png')).convert_alpha() for i in range(16,23)] 
    #sagUcakResimListesi = [pygame.transform.scale(resim,(resim.get_width()/5*4, resim.get_height()/5*3)) for resim in sagUcakResimListesi]
    solUcakResimListesi = [pygame.image.load(os.path.join('engeller',f'{i}.png')).convert_alpha() for i in range(23,30)] 
    #solUcakResimListesi = [pygame.transform.scale(resim,(resim.get_width()/5*4, resim.get_height()/5*3)) for resim in solUcakResimListesi]
    #resimleri initte değilde initten önce tanımlamamın sebebi oluşturulan her obje için tekrar tekrar resim yüklenmesini engellemek, sadece bir defa resim yüklemek için. burdan 100 örnek oluşturulsada resimler sadece bir defa yüklenip, her örnek için rasgele seçilmesini sağlıycak bi yapı oluşturabilirim.
    def __init__(self, tur, x, y) :
        super().__init__()
        self.tur = tur
        self.x = x
        self.y = y
        self.secilenResim = None
        self.arabaHareketlenmesi = random.randint(100, pencereOzellik.oyunYuzeyi.get_height() -450)
        self.tekrar = 0
        self.ucakRasgeleYsecimi = random.randint(1, pencereOzellik.oyunHizi)
        self.ucakRasgeleXsecimi = random.randint(1, pencereOzellik.oyunHizi)

        if self.tur == 'bariyer':
            self.secilenResim = random.choice(Engeller.bariyerResimListesi)
        elif self.tur == 'araba':
            self.secilenResim = random.choice(Engeller.arabaResimListesi)       #choice ile resim listesinden rasgele bir tanesinin seçilmesini sağlıyoruz.
        elif self.tur == 'ucaksol':
            self.secilenResim = random.choice(Engeller.solUcakResimListesi)
        elif self.tur == 'ucaksag':
            self.secilenResim = random.choice(Engeller.sagUcakResimListesi)

        self.rect = self.secilenResim.get_rect()
        self.mask = pygame.mask.from_surface(self.secilenResim)


    def engelCiz(self):    
        if self.tur == 'bariyer':
            self.y += pencereOzellik.oyunHizi

        elif self.tur == 'araba':
            self.y += pencereOzellik.oyunHizi /2
            
            if self.y > self.arabaHareketlenmesi and self.tekrar < 45:
                if self.x < arabaObj.x :
                    self.x += pencereOzellik.oyunHizi /3    
                if self.x > arabaObj.x :
                    self.x -= pencereOzellik.oyunHizi /3
                self.tekrar += 1
        elif self.tur == 'ucaksag':
            self.y += self.ucakRasgeleYsecimi
            self.x += self.ucakRasgeleXsecimi/2
        elif self.tur == 'ucaksol':
            self.y += self.ucakRasgeleYsecimi
            self.x -= self.ucakRasgeleXsecimi/2

        self.rect.x = self.x
        self.rect.y = self.y
        

        pencereOzellik.oyunYuzeyi.blit(self.secilenResim,(self.x, self.y))
    
          

class SeviyeAyarlar:
    def __init__(self):
        self.zamanDegeri = 2000
        self.puanZamanlayicisi = pygame.USEREVENT +1
        pygame.time.set_timer(self.puanZamanlayicisi, self.zamanDegeri)
        self.agacZamanlayicisiSag = pygame.USEREVENT +2    #pygame.settimer  için zamanı aşağıdaki fonksiyonda tanımlayıp her süre dolumunda o fonksiyona gönderdim ki süreki farklı zamanları seçsin
        self.agacZamanlayicisiSol = pygame.USEREVENT +3
        self.agacIcinZamanSec('sag')       
        self.agacIcinZamanSec('sol') 
        self.engelZamanlayicisi = pygame.USEREVENT +4
        self.engellerIcinZamanSec()
        self.bilgiKutuOlcu = [0 ,pencereOzellik.oyunYuzeyi.get_height() -80 , pencereOzellik.oyunYuzeyi.get_width(), 80]
        self.bilgiFont = pygame.font.Font(os.path.join('font','2.ttf'), 30)
        self.fontRenk = (240, 246, 213)
        self.fontOlcu = self.bilgiFont.render(f'Olcu : {pencereOzellik.seviye}', True, self.fontRenk)       #bunu burda yapmamızın sebebi yazının yüksekliğiyle ilgili hesaplamayı initte yapıp fonksiyon her çalıştığında tekrar tekrar hesaplama yapmaması için. metni initte hazırlayabiliyoruz,
                                                                                                            #ama puan ve seviye değişkenlerinin sürekli güncellenmesi gerekiyor. initte bunlar güncellenmiyor sınıf oluşturulurken ki değerleri alıyor sabit kalıyor. oyüzden yazı oluşturma kısmını fonksiyona, 
                                                                                                            #bunların ölçüleri sabit olcağı için ölçüsünüde bi yer tutucuya katardım ki metnin yükseklik olarak ölçüsünü alabileyim
        self.levelBilgiKonum = (150, self.bilgiKutuOlcu[1] + (self.bilgiKutuOlcu[3]/2 - self.fontOlcu.get_height()/2))      #dikey olarak kutuya ortalayabilmek için için font ölçüdeki rasgele oluşturduğum meyni kullanıyorum . dikay olarak boyutları sabit olcak.
        self.scoreBilgiKonum = (pencereOzellik.oyunYuzeyi.get_width()/2 +25, self.bilgiKutuOlcu[1] + (self.bilgiKutuOlcu[3]/2 - self.fontOlcu.get_height()/2))
        self.disKenarOlcu =[0,0,pencereOzellik.oyunYuzeyi.get_width() ,pencereOzellik.oyunYuzeyi.get_height()]
        self.IcKenarOlcu = [125,0,550,1100]
        self.sagAgacListesi = []
        self.solAgacListesi = []
        self.engelListesi = []
        self.engelSpriteGrubu = pygame.sprite.Group()


    def seviyeSecim(self):
        if 0 <= pencereOzellik.puan < 80:
            pencereOzellik.seviye = 1
        elif 80 <= pencereOzellik.puan < 170:
            pencereOzellik.seviye = 2
            pencereOzellik.oyunHizi = 9
        elif 170 <= pencereOzellik.puan < 270:
            pencereOzellik.seviye = 3
            pencereOzellik.oyunHizi = 10
        elif 270 <= pencereOzellik.puan < 380:
            pencereOzellik.seviye = 4
            pencereOzellik.oyunHizi = 11
        elif 380 <= pencereOzellik.puan < 620:
            pencereOzellik.seviye = 5
            pencereOzellik.oyunHizi = 12
        elif 620 <= pencereOzellik.puan < 945:
            pencereOzellik.seviye = 6
            pencereOzellik.oyunHizi = 13
        elif 945 <= pencereOzellik.puan < 1395:
            pencereOzellik.seviye = 7
            pencereOzellik.oyunHizi = 15
        elif 1395 <= pencereOzellik.puan :
            pencereOzellik.seviye = 8
            pencereOzellik.oyunHizi = 18


        pygame.draw.rect(pencereOzellik.oyunYuzeyi, pencereOzellik.disKenarRenk , self.disKenarOlcu)    
        pygame.draw.rect(pencereOzellik.oyunYuzeyi, (pencereOzellik.icKenarRenk) , self.IcKenarOlcu)
        seritAyarlamalari()
        self.agacAyarla()
        self.engelAyarla()
        arabaObj.secileniCiz()

        #eğer seviye seviye çizimleri daha özelleştirmek istersen aşağıdaki şekilde yap.
        '''if 1 <= pencereOzellik.seviye <= 2 :    
            pygame.draw.rect(pencereOzellik.oyunYuzeyi, pencereOzellik.disKenarRenk , self.disKenarOlcu)    
            pygame.draw.rect(pencereOzellik.oyunYuzeyi, (pencereOzellik.icKenarRenk) , self.IcKenarOlcu)
            seritAyarlamalari()
            self.agacAyarla()
            self.engelAyarla()
            arabaObj.secileniCiz()'''
        
    def oyunBilgisi(self):          #oyundayken oyuncuya bilgi amaçlı yazılan seviye ve puan textlerinin çizilmesi
        bilgiKutu = pygame.draw.rect(pencereOzellik.oyunYuzeyi, (0,0,0), self.bilgiKutuOlcu)
        levelBilgi = self.bilgiFont.render(f'LEVEL : {pencereOzellik.seviye}', True, self.fontRenk)
        scoreBilgi = self.bilgiFont.render(f'SCORE : {pencereOzellik.puan}', True, self.fontRenk)
        pencereOzellik.oyunYuzeyi.blit(levelBilgi, self.levelBilgiKonum)
        pencereOzellik.oyunYuzeyi.blit(scoreBilgi, self.scoreBilgiKonum)

    def agacIcinZamanSec(self,bolge):
        if bolge == 'sag':
            pygame.time.set_timer(self.agacZamanlayicisiSag, (random.randint(700, 3000)))
        elif bolge == 'sol':
            pygame.time.set_timer(self.agacZamanlayicisiSol, (random.randint(700, 3000)))
        
    def agacOlustur(self,bolge):
        if bolge == 'sag':
            self.sagAgacListesi.append(AgacOlustur())
        elif bolge == 'sol':
            self.solAgacListesi.append(AgacOlustur())
    
    def agacAyarla(self):
        for i in self.sagAgacListesi:
            i.agacCiz('sag')
        for i in self.solAgacListesi:
            i.agacCiz('sol')
        self.sagAgacListesi = [x for x in self.sagAgacListesi if x.agacY < pencereOzellik.oyunYuzeyi.get_height() ]     #ekran dışına  çıkan ağaçları listeye almıyoruz. sonsuza kadar giden ağaçların objelerini boşa çıkarıp pythonun çöp toplayıcının silmesini sağlıyoruz.
        self.solAgacListesi = [x for x in self.solAgacListesi if x.agacY < pencereOzellik.oyunYuzeyi.get_height() ]


    def engellerIcinZamanSec(self):
        if 1 <= pencereOzellik.seviye <= 3:
            pygame.time.set_timer(self.engelZamanlayicisi, (random.randint(2000,3500)))
        elif 4 <= pencereOzellik.seviye <= 6:
            pygame.time.set_timer(self.engelZamanlayicisi, (random.randint(1700,3000)))
        elif 7 <= pencereOzellik.seviye < 8:
            pygame.time.set_timer(self.engelZamanlayicisi, (random.randint(1400,2200)))
        elif 8 <= pencereOzellik.seviye:
            pygame.time.set_timer(self.engelZamanlayicisi, (random.randint(1000,1700)))

    def engelOlustur(self):# seviyeleri duzenle
        if 1 <= pencereOzellik.seviye <= 2:
            self.engelListesi.append(Engeller('bariyer', random.randint(self.IcKenarOlcu[0],self.IcKenarOlcu[0] + self.IcKenarOlcu[2]-96), -100))
        elif 3 <= pencereOzellik.seviye <= 4:
            self.engelListesi.append(random.choice([Engeller('bariyer', random.randint(self.IcKenarOlcu[0],self.IcKenarOlcu[0] + self.IcKenarOlcu[2]-96), -100),
                                                    Engeller('araba', random.randint(self.IcKenarOlcu[0],self.IcKenarOlcu[0] + self.IcKenarOlcu[2]-96), -100)]))
        elif 5 <= pencereOzellik.seviye <= 6:
            self.engelListesi.append(Engeller('araba', random.randint(self.IcKenarOlcu[0],self.IcKenarOlcu[0] + self.IcKenarOlcu[2]-96), -100))
        elif 7 == pencereOzellik.seviye:
            self.engelListesi.append(random.choice([Engeller('ucaksol', pencereOzellik.oyunYuzeyi.get_width() +100, random.randint(-400, 0)),
                                                    Engeller('ucaksag', -100, random.randint(-400, 0))]))
        elif 8 <= pencereOzellik.seviye:
            self.engelListesi.append(random.choice([Engeller('araba', random.randint(self.IcKenarOlcu[0],self.IcKenarOlcu[0] + self.IcKenarOlcu[2]-96), -100),
                                                    Engeller('ucaksol', pencereOzellik.oyunYuzeyi.get_width() +100, random.randint(-400, 0)),
                                                    Engeller('ucaksag', -100, random.randint(-400, 0))]))

    def engelAyarla(self):
        for i in self.engelListesi:
            i.engelCiz()
        self.engelListesi = [x for x in self.engelListesi if x.y < pencereOzellik.oyunYuzeyi.get_height() and -200 < x.x < pencereOzellik.oyunYuzeyi.get_width() + 100 ]
        
    def engelSpriteGrubuGuncelle(self):
        self.engelSpriteGrubu.empty()       #ekran dışına çıkan çıkan spritelerin temizlenmesi için sprite listesinin temizlenip engel listesinin haliyle güncellenmesi
        self.engelSpriteGrubu.add(self.engelListesi)
 

oyunIciSeviyeAyarlari = SeviyeAyarlar()


class Ses:
    def __init__(self) :
        self.gorevButon = pygame.mixer.Sound(os.path.join('ses','butongorev.wav'))
        self.menuButon = pygame.mixer.Sound(os.path.join('ses','butonmenu.wav'))
        self.optionsButon = pygame.mixer.Sound(os.path.join('ses','butonoptions.wav'))
        self.oyunSonu = pygame.mixer.Sound(os.path.join('ses','son.wav'))
        self.oyunDongusu = pygame.mixer.music.load(os.path.join('ses','oyun.wav'))
        self.sesSeviyesiAyarla()

    def sesSeviyesiAyarla(self):
        if pencereOzellik.sesAcik is True:
            self.gorevButon.set_volume(optionsObj.volume/100)
            self.menuButon.set_volume(optionsObj.volume/100)
            self.optionsButon.set_volume(optionsObj.volume/100)
            self.oyunSonu.set_volume(optionsObj.volume/100)
            pygame.mixer.music.set_volume(optionsObj.volume/100)
        elif pencereOzellik.sesAcik is False:
            self.gorevButon.set_volume(0)
            self.menuButon.set_volume(0)
            self.optionsButon.set_volume(0)
            self.oyunSonu.set_volume(0)
            pygame.mixer.music.set_volume(0)

    def gorevButonSes(self):
        self.gorevButon.play()
    def menuButonSes(self):
        self.menuButon.play()
    def optionsButonSes(self):
        self.optionsButon.play()
    
    
sesler = Ses()


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

def duraklat():
    pencereOzellik.oyunYuzeyi.blit(GorevCubugu.pauseFontCiz,((pencereOzellik.oyunYuzeyi.get_width()/2) - (GorevCubugu.pauseFontCerceveOlcu.w/2), (pencereOzellik.oyunYuzeyi.get_height()/2) -GorevCubugu.pauseFontCerceveOlcu.h/2))      #oyun durunca pauseyi çizdirdiğimiz kod. .

def oyunSonuEkrani(sonpuan):
    pencereOzellik.oyunYuzeyi.blit(pencereOzellik.oyunSonuArkaPlan,(-50,0))
    gameOver = pencereOzellik.oyunSonuYaziAyar.render('GAME OVER',True,(235,235,235))
    puan = pencereOzellik.oyunSonuYaziAyar.render((f'SCORE  {sonpuan}'),True,(20,20,20))
    pencereOzellik.oyunYuzeyi.blit(gameOver,((pencereOzellik.oyunYuzeyi.get_width()/2 - gameOver.get_width()/2), (pencereOzellik.oyunYuzeyi.get_height()/2 - gameOver.get_height()/2) -350))
    pencereOzellik.oyunYuzeyi.blit(puan,((pencereOzellik.oyunYuzeyi.get_width()/2 - puan.get_width()/2), (pencereOzellik.oyunYuzeyi.get_height()/2 - puan.get_height()/2) +50 ))
    
def sesDonguleri():
    muzikCaliyor = pygame.mixer.music.get_busy()
    if pencereOzellik.oyunAktif is True:
        if muzikCaliyor is False:
            if pencereOzellik.oyunMuzikBastanBasla is True:
                pygame.mixer.music.play(-1)
                pencereOzellik.oyunMuzikBastanBasla = False
            elif pencereOzellik.oyunMuzigiDurakladı is True:
                pygame.mixer.music.unpause()
    if pencereOzellik.oyunAktif is False:
        if muzikCaliyor is True:
            pygame.mixer.music.pause()
            pencereOzellik.oyunMuzigiDurakladı = True
    if pencereOzellik.oyunSonu is True:
        if pencereOzellik.oyunSonuMuzigi is True:   
            sesler.oyunSonu.play()
            pencereOzellik.oyunSonuMuzigi = False
    if pencereOzellik.oyunSonu is False:
        if pencereOzellik.oyunSonuMuzigi is False:      #döngüde bu blok sürekli çalıştığı için sürekli sesi stop komutu yapıyordu. o yüzden oyunsonuekranındaki değişkenlerle ters mantık uyguladık.
            sesler.oyunSonu.stop()
            pencereOzellik.oyunSonuMuzigi = True


def oyunCalistir():
    while pencereOzellik.oyunCalisiyor: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pencereOzellik.oyunCalisiyor = False
                pygame.quit()
                sys.exit()
                     
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pencereOzellik.menu is True:
                    for buton in menuButonListesi:
                        if buton.cerceve.x <= fareX  <= buton.cerceve.x + buton.cerceve.width and buton.cerceve.y <= fareY <= buton.cerceve.y + buton.cerceve.height:
                            buton.butonTiklamaEfekt()
                            buton.butonGorev()
                elif pencereOzellik.options is True:
                    optionsObj.butonGorevler()
                GorevCubugu.gorevCubuguTiklamaOlaylari()        #görev çubuğunu sürekli algılanması için en alta yazıp fonksiyona gönderiyoruz.

            if event.type == pygame.KEYDOWN:
                if pencereOzellik.oyunAktif:
                    if event.key == pygame.K_LEFT:
                        pencereOzellik.solTusBasili = True
                    elif event.key == pygame.K_RIGHT:
                        pencereOzellik.sagTusBasili = True
                    elif event.key == pygame.K_UP:
                        pencereOzellik.ustTusBasili = True
                    elif event.key == pygame.K_DOWN:
                        pencereOzellik.altTusBasili = True

            if event.type == pygame.KEYUP:
                if pencereOzellik.oyunAktif:
                    if event.key == pygame.K_LEFT:
                        pencereOzellik.solTusBasili = False
                    elif event.key == pygame.K_RIGHT:
                        pencereOzellik.sagTusBasili = False
                    elif event.key == pygame.K_UP:
                        pencereOzellik.ustTusBasili = False
                    elif event.key == pygame.K_DOWN:
                        pencereOzellik.altTusBasili = False
        
            ############   OLUŞTURULAN ÖZEL EVENTLER   #################
            if event.type == oyunIciSeviyeAyarlari.puanZamanlayicisi:       #sadece oyunaktifken her 2 saniye için oyun hızının puana eklenmesi.
                if pencereOzellik.oyunAktif is True:
                    pencereOzellik.puan += pencereOzellik.oyunHizi

            if event.type == oyunIciSeviyeAyarlari.agacZamanlayicisiSag:       #sadece oyun aktifken ağaç çizimi için rasgele zamanların belirlenlemesi ve ağaç çizimi
                if pencereOzellik.oyunAktif is True:
                    oyunIciSeviyeAyarlari.agacIcinZamanSec('sag')
                    oyunIciSeviyeAyarlari.agacOlustur('sag')
                    
            if event.type == oyunIciSeviyeAyarlari.agacZamanlayicisiSol:       #sadece oyun aktifken ağaç çizimi için rasgele zamanların belirlenlemesi ve ağaç çizimi
                if pencereOzellik.oyunAktif is True:
                    oyunIciSeviyeAyarlari.agacIcinZamanSec('sol') 
                    oyunIciSeviyeAyarlari.agacOlustur('sol')   

            if event.type == oyunIciSeviyeAyarlari.engelZamanlayicisi:         #engel oluşturma zamanlaması
                if pencereOzellik.oyunAktif is True:
                    oyunIciSeviyeAyarlari.engellerIcinZamanSec()
                    oyunIciSeviyeAyarlari.engelOlustur()    


        if pencereOzellik.menu is True:     #menü çizimi ve efektler.
            menuyeGec()
            fareX, fareY = pygame.mouse.get_pos()
            for buton in menuButonListesi:
                if buton.cerceve.x <= fareX  <= buton.cerceve.x + buton.cerceve.width and buton.cerceve.y <= fareY <= buton.cerceve.y + buton.cerceve.height:
                    buton.butonEfektAktif = True
                else:
                    buton.butonEfektAktif = False
                buton.menuButonEfekt(pencereOzellik.oyunYuzeyi)
        
        if  pencereOzellik.oyunAktif is True and pencereOzellik.menu is False and  pencereOzellik.duraklat is False:         #oyun şemaları çizimi
            oyunIciSeviyeAyarlari.seviyeSecim()      #yapılıcak tekrarlı çizimkileri bu fonksiyon içine yaz.
            oyunIciSeviyeAyarlari.oyunBilgisi()
            oyunIciSeviyeAyarlari.engelSpriteGrubuGuncelle()
            arabaObj.tusKontrolleri()  
            
            ####### ÇARPIŞMA KONTROLLERİ ########
            carpismaKontrolleriAlani = pygame.sprite.spritecollide(arabaObj, oyunIciSeviyeAyarlari.engelSpriteGrubu, True)   #ilk önce rectlerin çarpışmasını kontrol ediyoruz bu hem daha az kaynak hem daha az hesaplama gerektiriyor.
            if carpismaKontrolleriAlani:
                for engel in carpismaKontrolleriAlani:          #eğer rect çarğışması varsa maske çarpışmasını kontrol ediyoruz. bu resimlerin karelerinin  yerine direk piksellerini kontrol ediyor. daha detaylı bi kontrol sağlıyor o yüzden rectler gerçekleştikten sonra bunu kontrol ediyoruz ki sürekli pikselleri kontrol ederek gereksiz hesap yükünden kurtuluyoruz.
                    offsett = ( engel.rect.x - arabaObj.rect.x , engel.rect.y - arabaObj.rect.y)
                    carpismaNoktasi = arabaObj.mask.overlap(engel.mask, offsett)
                    if carpismaNoktasi:
                        pencereOzellik.oyunSonu = True
                        sonpuan = str(pencereOzellik.puan)      #aşağıdaki fonksiyonda puanı sıfırlıyor o yüzden puanı burda bideğişkende tutup oyun sonu fonksiyonuna bu değişkeni gönderiyoruz.
                        #pencereOzellik.oyunSonuMuzigi = True    #bayrak kullanmayıp direk sesi açınca döngü olduğu için sürekli sürekli sesi oynatıyor. burdaki bayrak tek bir defa çalması için.
                        pencereOzellik.herseyiSifirla()
            
            
        elif pencereOzellik.communication is True and pencereOzellik.menu is False and pencereOzellik.oyunAktif is False and pencereOzellik.oyunSonu is False:
            communicationGec()
        
        elif pencereOzellik.options is True and pencereOzellik.menu is False and pencereOzellik.oyunAktif is False :
            optionsObj.optionsCizimler()
        
        elif pencereOzellik.duraklat is True and pencereOzellik.menu is False and pencereOzellik.oyunAktif is False and pencereOzellik.oyunSonu is False:
            duraklat()
            
        elif  pencereOzellik.oyunSonu is True and pencereOzellik.menu is False and pencereOzellik.oyunAktif is False :
            oyunSonuEkrani(sonpuan)

        if pencereOzellik.oyunAktif is False and pencereOzellik.menu is True or pencereOzellik.duraklat is True:
            pencereOzellik.tuslariSerbestBirak()
        


        GorevCubugu.ciz()       #bunun en altta olmasının sebebi en son çizilip en üstte görünmesi görev çubuğunun

        sesDonguleri()
        
        pygame.display.flip()       #güncelleme için.
        pencereOzellik.fps.tick(50)
        

if __name__ == '__main__':      #bu bloğun anlamı: sadece bu py dosyası doğrudan çalıştırılıyorsa  işlemler gerçekleştiricek demek,
    oyunCalistir()                  #eğer bu py dosyası import edilirse o zaman bu blok çalıştırılmıycak demektir.
    
        



