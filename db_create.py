# -*- coding: utf-8 -*-

from app import db
from app.models import User, Party

db.drop_all()

db.create_all()
db.session.commit()

admon = User('tomer', 'admon', '123')
tomer = User(u'תומר', u'אדמון', '234')
avihu = User(u'אביהו', u'פינקו', '345')
pinko = User('avihu', 'pinko', '456')
yulia = User(u'יוליה', u'זורין', '567')
zorin = User('yulia', 'zorin', '678')

avoda = Party(u'העבודה', 'https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg')
likud = Party(u'הליכוד', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Likud_Logo.svg/250px-Likud_Logo.svg.png')
lavan = Party(u'פתק לבן', 'https://www.weberthai.com/fileadmin/user_upload/01_training-elements/02.4_others/02.5_color_cards/05_color_mosaic/images/1.jpg')
habait = Party(u'הבית היהודי',
               'https://upload.wikimedia.org/wikipedia/he/thumb/9/92/The-Jewish-Home-logo.svg/416px-The-Jewish-Home-logo.svg.png')
kadima = Party(u'קדימה',
               'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Logo_Kadima.svg/300px-Logo_Kadima.svg.png')
shas = Party(u'שס', 'http://www.nrg.co.il/images/archive/300x225/1/002/608.jpg')
yarok = Party(u'עלה ירוק', 'https://pbs.twimg.com/profile_images/553476099775016960/8Ha40Qym_400x400.jpeg')

db.session.add(kadima)
db.session.add(habait)
db.session.add(avoda)
db.session.add(likud)
db.session.add(yarok)
db.session.add(shas)
db.session.add(lavan)
db.session.add(admon)
db.session.add(tomer)
db.session.add(avihu)
db.session.add(yulia)
db.session.add(pinko)
db.session.add(zorin)
db.session.commit()
users = User.query.all()
print(users)
# for user in users:
#     print (user.voted)
