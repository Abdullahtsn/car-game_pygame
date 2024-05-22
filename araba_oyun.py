import pygame
import random
import sys
import os


pygame.init()

oyunHizi = 8
icKenarRenk = (50,50,50)
disKenarRenk = (180,238,180)
ekranDikeyBoyut = 1100
ekranYatayBoyut = 800

fps = pygame.time.Clock()
oyunYuzeyi = pygame.display.set_mode((ekranYatayBoyut,ekranDikeyBoyut))
pygame.display.set_caption('ARABA YARIŞI')      #pencere başlığı, iconda ekleniyor sonra bak
oyunYuzeyi.fill((0,0,0))                #en dış tabakanın siyaha boyanması
pygame.draw.rect(oyunYuzeyi, disKenarRenk ,[25,0,750,1100])    #kenarlık niyetiyle bi dikdötgeni ortaladım. 
pygame.draw.rect(oyunYuzeyi, icKenarRenk ,[125,0,550,1100])    #ağaçların alanını belli etmek için daha küçük bi kutu koydum, bu kutunun dışına ağaçlar koncak.




class SeritOlustur:
    def __init__(self, konumY ):       #dikey olduğu için x sabit, y1 = başlangıç, y2 = bitiş
        self.konumY = konumY
        self.yanSeritMesafe = 137.5
        self.konumX = 262.5
        self.seritUzunluk = 100
        self.seritRenk = (224,255,255)
        self.seritKalinlik = 5

    def seritCiz (self, hiz):
        pygame.draw.line(oyunYuzeyi, self.seritRenk , [self.konumX ,self.konumY], 
                         [self.konumX ,self.konumY + self.seritUzunluk], self.seritKalinlik)      #burası soldan ilk çizgiyi çiziyor, aşağıdaki ikğ satırda oranlı olarak  belli boşluk bırakıp ikinci ve üçüncüyü çiziyor.
        pygame.draw.line(oyunYuzeyi, self.seritRenk , [ (self.konumX + self.yanSeritMesafe) ,self.konumY], 
                         [ (self.konumX + self.yanSeritMesafe) ,self.konumY + self.seritUzunluk], self.seritKalinlik)
        pygame.draw.line(oyunYuzeyi, self.seritRenk , [ (self.konumX + (self.yanSeritMesafe *2)) ,self.konumY], 
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
        oyunYuzeyi.blit(self.agacAyarla,(self.solAgacX, self.solAgacY))
        self.solAgacY += oyunHizi

    def sagKenarAgac (self):
        oyunYuzeyi.blit(self.agacAyarla,(self.sagAgacX, self.sagAgacY))
        self.sagAgacY += oyunHizi
    
    
       
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


def donguselCizimler():
    global solAgacListesi,sagAgacListesi    #bunu yapmayınca liste adı globalmi değilmi anlamayıp hata veriyor o yüzden heryerden erişilebilir olması için global yaptık.
    oyunYuzeyi.fill((0,0,0))
    pygame.draw.rect(oyunYuzeyi, disKenarRenk ,[25,0,750,1100])    
    pygame.draw.rect(oyunYuzeyi, icKenarRenk ,[125,0,550,1100])

    ##########      Agaç Konum Ve Hareket       ##############
    solAgacListesi = [agaclar for agaclar in solAgacListesi if agaclar.solAgacY <= ekranDikeyBoyut]     #liste üreteci deniyor buna. solağaçlistesindeki elemanların y konumlarını ekranın alt bitiş noktasıyla karşılaştırıp koşula uyan yani sadece ekranın içinde olan ağaçları listeye alıyor. ekranın dışına çıkan ağaçları sonsuzluğa varmaması için siliyor.
    for agaclar in solAgacListesi:      
        agaclar.solKenarAgac()

    sagAgacListesi = [agaclar for agaclar in sagAgacListesi if agaclar.sagAgacY <= ekranDikeyBoyut]     
    for agaclar in sagAgacListesi:
        agaclar.sagKenarAgac()
        
        
    
    ##########      Şerit konumları ve hareketleri       ##############
    seritListesi = [ilkSiraSerit, ikinciSiraSerit, ucuncuSiraSerit, dorduncuSiraSerit, besinciSiraSerit, altinciSiraSerit]
    for seritler in seritListesi:
        seritler.seritCiz(oyunHizi)
        if seritler.konumY > ekranDikeyBoyut :  #seritlerin ekranın dışına çıkınca yukardan tekrar inmesi için.
            seritler.konumY = - seritler.seritUzunluk



oyunCalisiyor = True
while oyunCalisiyor:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyunCalisiyor = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT + 1:      #bu ve alttaki if bloğu rasgele zamanlarda obje oluşturup listenin içine atıyor.
            solAgacListesi.append(AgacOlustur())    #objeyi burda direk oluşturursak sürekli sürekli obje oluşturuyor. o yüzden oluşturup listeye atıyoruz.
        if event.type == pygame.USEREVENT + 2:
            sagAgacListesi.append(AgacOlustur())
        
    donguselCizimler()      #yapılıcak tekrarlı çizimkileri bu fonksiyon içine yaz.

    


    pygame.display.flip()       #güncelleme için.
    fps.tick(60)
    '''pygame.display.update()     #bu ekranın tamamının güncellenmesi için
    pygame.display.update(örnek)    #parametre verirsek verilen parametreyi güncelleri
    pygame.display.flip()       #bu değişen kısımların güncellenmesi için'''
    
    
        



