import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django #Django yu içe aktardı.

django.setup()

import random
from first_app.models import Topic,Webpage,AccessRecord #oluşturduğumuz modelleri import ettik.
from faker import Faker

fakegen = Faker() #ratgele veriler oluşturmak için Faker metodunu "fakegen" nesnesinin içine attık
topics = ['Search','Social','Marketplace','News','Games'] #websitesi araması içn dizi oluşturduk.

def add_topic(): # 'topic' listesinden rastgele bir konu seçmek için
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] #get_or_create () - o nesnenin bir tuple değerini döndürür
    t.save() #oluşturulan rastgele Tuple t nesnesine kaydedilir.
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic() #add_topic metodundaki verileri top değişkenine at
        # Sahte veri -Fake oluştur
        fake_url = fakegen.url() #fakegen nesnesindeki url bilgisini fake_url değişkenine attık
        fake_date = fakegen.date() #fakegen nesnesindeki tarih bilgisini fake_date değişkenine attık
        fake_name = fakegen.company() #fakegen nesnesindeki company bilgisini fake_name değişkenine attık

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]# yeni web sayfası oluşturmak içn
        #get_or_create () -ile o nesnenin bir tuple değerini döndürür

        accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]# Bu sayfa için Sahte Erişim Kaydı oluştur

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)#20 tane kayıt getirsin.
    print('Populating Complete')
