
# coding: utf-8
# classify green and non green data

import json
from collections import OrderedDict
from pprint import pprint



#########Melbourne
AlbertPark = ([-37.8368354108246,144.96013641357422], [-37.858726947015846, 144.98167991638184])
Alexandragarden= ([-37.81944632616724, 144.96831983327866], [-37.8230736274583, 144.9759306013584])
Batmanpark = ([-37.82150234098555, 144.95543487477778], [-37.822231185253266, 144.9578240524578])
CarltonGardens = ([-37.80102707613663, 144.96889651685365], [-37.80814768646792, 144.97401819496758])
Cricket_AAMIpark = ([-37.816296296320694, 144.9791428524295], [-37.82577352474828, 144.98932854116356])
Fawknerpark = ([-37.83738718745357, 144.97746579449233], [-37.84541929714928, 144.98483516376075])
Fedsquare = ([-37.81728043453767, 144.9675685178089], [-37.81887380381079, 144.9705739330101])
FlagstaffGardens = ([-37.809109639012874, 144.952636660223], [-37.81175422782249, 144.95642796266554])
Royalpark_melzoo = ([-37.77955911022859, 144.9419936685042], [-37.794787242365544, 144.95728628320262])
StVincentGardens = ([-37.8385978913426, 144.9523560088703], [-37.83981799495433, 144.95830917177886])
UniversityOval = ([-37.793643275000754, 144.9604656547308], [-37.79642406344074, 144.96289774775505])
ikon_princesPark = ([-37.7785166660836, 144.95897769927979], [-37.79282936590083,144.9688482284546])
melBotanic = ([-37.82355540285284,144.97067031287975], [-37.83427087542552, 144.98390299105472])

########Sydney
ArtgalleryNSW = ([-33.866502472302294,151.21372474126883 ], [-33.87195433857322,151.2177882879264])
BarangarooReserve= ([-33.85566429952218, 151.20016917547218], [-33.85869354158092, 151.20240814944736])
Bradfieldpark = ([-33.84758980881784, 151.21160857379436], [-33.85083318224948, 151.21376171708107])
BradleysHead = ([-33.84297402663763, 151.23533338308334], [-33.853096342414624, 151.248237490654])
Centennialpark = ([-33.890926452870204, 151.22772801981455], [-33.90275281843705, 151.2438936935473])
Hydepark = ([-33.87034726748204, 151.2100449086529],  [-33.87676090276431, 151.21259166611253])
Jubileepark = ([-33.87219716321645, 151.17468059062958], [-33.8759027976293, 151.18108838796616])
Moorepark = ([-33.88912825507548, 151.21825139590078], [-33.904714052720124, 151.22583552210574])
Queenspark = ([-33.89884564291081, 151.24470233917236], [-33.90386802005763, 151.25309228897095])
Royalbotanicgardens = ([-33.85938761538035, 151.21427858469895],  [-33.86717399296229, 151.22030953166893])
Tumbalongpark = ([-33.87386340897371, 151.200664210284], [-33.87586716729526, 151.20266005396843])
Victoriapark = ([-33.88512379293545, 151.19088337927803], [-33.88822324007781, 151.19463176637635])
WendySecretGarden = ([-33.84345522020612, 151.20745986700058], [-33.84488096301803, 151.20963379740715])
Wentworthpark = ([-33.87468459677023, 151.1902812233542], [-33.87899581893191, 151.19553164750084])


########Brisbane
Gabba= ([-27.4851858153704,153.03701093855352], [-27.48658493401821, 153.03923549565525])
Raymondpark = ([-27.48007907272888, 153.03650446236134], [-27.481601992710456, 153.04099649190903])
RomaParkland = ([-27.461289488702842, 153.01645594156844], [-27.46445006304699, 153.02132012761695])
Victoriapark_golf = ([-27.449722804602114, 153.01794216667463], [-27.457758182969183, 153.0276061657553])
cityBotanicGardens= ([-27.472752425482355, 153.02736282348633], [-27.47960585537521, 153.03199768066406])
kangarooPoint = ([-27.47339971209088, 153.03342126309872] , [-27.479603155916788, 153.0349735915661])
newfarmpark = ([-27.467370480974058, 153.04836291334914], [-27.471102027913197, 153.05401365719126])
suncorp_stadium = ([-27.46396133621852, 153.0087379571953], [-27.465903339539203,153.010526320056])
wickhamPark = ([-27.46506824416126,153.02060934273334], [-27.467002830498537, 153.02465915679932])

########Perth
CharlesPatersonPark = ([-31.961978152107374, 115.88967732746812], [-31.96627435601906,115.89879013259622])
Foreshore_sirJames= ([-31.971158413451914, 115.85584960427275], [-31.976655512422955,115.87204344120016])
GloucesterPark = ([-31.955489433846815, 115.87881660246785], [-31.958752799999154, 115.88479086756706])
GolfClub = ([-31.978267551972746, 115.84773595170054], [-31.98831420216151, 115.85710624889407])
Hydepark = ([-31.936632003818577, 115.85930437659829], [-31.93990969187566, 115.86644307589142])
Kingspark_BotanicGarden = ([-31.95337655414906, 115.81785543704586], [-31.971581134490837, 115.84555192733364])
Langley_OzoneReserve = ([-31.959914567137083, 115.86437730836656], [-31.96373755621299, 115.88054365265157])
RussellSquare = ([-31.94512152624929, 115.85440134184546], [-31.94733735558192, 115.85741758346558])
lakeMonger_BritanniaRoadReserve = ([-31.922624653166398, 115.82120295741265], [-31.935008303745914, 115.8381932427792])
nibStadium = ([-31.944110875075605, 115.8684157655531], [-31.94706055953364, 115.87239281096993])
zoo_windsorpark = ([-31.973625341196524, 115.85124514997005], [-31.978285029714847, 115.85696026682854])


s = '.json'
green = []
ng = []


print s[0]


data = json.load(open(s))

print len(data['rows'])
count = len(data['rows'])



for  i in range(count):
    # a is coordinates
    a = data['rows'][i]['value']['geometry']['coordinates']
    txt = (data['rows'][i]['value']['properties']['text'])
    post = [a, txt]
    
    if s[9] == 'p':
        if ( (CharlesPatersonPark[1][0] <= a[1] <= CharlesPatersonPark[0][0] and CharlesPatersonPark[0][1] <= a[0] <= CharlesPatersonPark[1][1]) or
        (Foreshore_sirJames[1][0] <= a[1] <= Foreshore_sirJames[0][0] and Foreshore_sirJames[0][1] <= a[0] <= Foreshore_sirJames[1][1]) or
        (GloucesterPark[1][0] <= a[1] <= GloucesterPark[0][0] and GloucesterPark[0][1] <= a[0] <= GloucesterPark[1][1]) or
        (GolfClub[1][0] <= a[1] <= GolfClub[0][0] and GolfClub[0][1] <= a[0] <= GolfClub[1][1]) or
        (Hydepark[1][0] <= a[1] <= Hydepark[0][0] and Hydepark[0][1] <= a[0] <= Hydepark[1][1]) or
        (Kingspark_BotanicGarden[1][0] <= a[1] <= Kingspark_BotanicGarden[0][0] and Kingspark_BotanicGarden[0][1] <= a[0] <= Kingspark_BotanicGarden[1][1]) or
        (RussellSquare[1][0] <= a[1] <= RussellSquare[0][0] and RussellSquare[0][1] <= a[0] <= RussellSquare[1][1]) or
        (lakeMonger_BritanniaRoadReserve[1][0] <= a[1] <= lakeMonger_BritanniaRoadReserve[0][0] and lakeMonger_BritanniaRoadReserve[0][1] <= a[0] <= lakeMonger_BritanniaRoadReserve[1][1]) or
        (nibStadium[1][0] <= a[1] <= nibStadium[0][0] and nibStadium[0][1] <= a[0] <= nibStadium[1][1]) or
        (zoo_windsorpark[1][0] <= a[1] <= zoo_windsorpark[0][0] and zoo_windsorpark[0][1] <= a[0] <= zoo_windsorpark[1][1])):
            green.append(post)
        else:
            ng.append(post)
    
    elif s[9] == 'b':
        if ((Gabba[1][0] <= a[1] <= Gabba[0][0] and Gabba[0][1] <= a[0] <= Gabba[1][1]) or
        (Raymondpark[1][0] <= a[1] <= Raymondpark[0][0] and Raymondpark[0][1] <= a[0] <= Raymondpark[1][1]) or
        (RomaParkland[1][0] <= a[1] <= RomaParkland[0][0] and RomaParkland[0][1] <= a[0] <= RomaParkland[1][1]) or
        (Victoriapark_golf[1][0] <= a[1] <= Victoriapark_golf[0][0] and Victoriapark_golf[0][1] <= a[0] <= Victoriapark_golf[1][1]) or
        (cityBotanicGardens[1][0] <= a[1] <= cityBotanicGardens[0][0] and cityBotanicGardens[0][1] <= a[0] <= cityBotanicGardens[1][1]) or
        (kangarooPoint[1][0] <= a[1] <= kangarooPoint[0][0] and kangarooPoint[0][1] <= a[0] <= kangarooPoint[1][1]) or
        (newfarmpark[1][0] <= a[1] <= newfarmpark[0][0] and newfarmpark[0][1] <= a[0] <= newfarmpark[1][1]) or
        (suncorp_stadium[1][0] <= a[1] <= suncorp_stadium[0][0] and suncorp_stadium[0][1] <= a[0] <= suncorp_stadium[1][1]) or
        (wickhamPark[1][0] <= a[1] <= wickhamPark[0][0] and wickhamPark[0][1] <= a[0] <= wickhamPark[1][1])):
            green.append(post)
        else:
            ng.append(post)
    
    elif s[9] == 's':
        if ( (ArtgalleryNSW[1][0] <= a[1] <= ArtgalleryNSW[0][0] and ArtgalleryNSW[0][1] <= a[0] <= ArtgalleryNSW[1][1]) or
        (BarangarooReserve[1][0] <= a[1] <= BarangarooReserve[0][0] and BarangarooReserve[0][1] <= a[0] <= BarangarooReserve[1][1]) or
        (Bradfieldpark[1][0] <= a[1] <= Bradfieldpark[0][0] and Bradfieldpark[0][1] <= a[0] <= Bradfieldpark[1][1]) or
        (BradleysHead[1][0] <= a[1] <= BradleysHead[0][0] and VBradleysHead[0][1] <= a[0] <= BradleysHead[1][1]) or
        (Centennialpark[1][0] <= a[1] <= Centennialpark[0][0] and Centennialpark[0][1] <= a[0] <= Centennialpark[1][1]) or
        (Hydepark[1][0] <= a[1] <= Hydepark[0][0] and Hydepark[0][1] <= a[0] <= Hydepark[1][1]) or
        (Jubileepark[1][0] <= a[1] <= Jubileepark[0][0] and Jubileepark[0][1] <= a[0] <= Jubileepark[1][1]) or
        (Moorepark[1][0] <= a[1] <= Moorepark[0][0] and Moorepark[0][1] <= a[0] <= Moorepark[1][1]) or
        (Queenspark[1][0] <= a[1] <= Queenspark[0][0] and Queenspark[0][1] <= a[0] <= Queenspark[1][1]) or
        (Royalbotanicgardens[1][0] <= a[1] <= Royalbotanicgardens[0][0] and Royalbotanicgardens[0][1] <= a[0] <= Royalbotanicgardens[1][1]) or
        (Tumbalongpark[1][0] <= a[1] <= Tumbalongpark[0][0] and Tumbalongpark[0][1] <= a[0] <= Tumbalongpark[1][1]) or
        (Victoriapark[1][0] <= a[1] <= Victoriapark[0][0] and Victoriapark[0][1] <= a[0] <= Victoriapark[1][1]) or
        (Wentworthpark[1][0] <= a[1] <= Wentworthpark[0][0] and Wentworthpark[0][1] <= a[0] <= Wentworthpark[1][1]) or
        (WendySecretGarden[1][0] <= a[1] <= WendySecretGarden[0][0] and WendySecretGarden[0][1] <= a[0] <= WendySecretGarden[1][1])):
            green.append(post)
        else:
            ng.append(post)
    
    elif s[9] == 'm':
        if ( (AlbertPark[1][0] <= a[1] <= AlbertPark[0][0] and AlbertPark[0][1] <= a[0] <= AlbertPark[1][1]) or
        (Alexandragarden[1][0] <= a[1] <= Alexandragarden[0][0] and Alexandragarden[0][1] <= a[0] <= Alexandragarden[1][1]) or
        (Batmanpark[1][0] <= a[1] <= Batmanpark[0][0] and Batmanpark[0][1] <= a[0] <= Batmanpark[1][1]) or
        (CarltonGardens[1][0] <= a[1] <= CarltonGardens[0][0] and CarltonGardens[0][1] <= a[0] <= CarltonGardens[1][1]) or
        (Cricket_AAMIpark[1][0] <= a[1] <= Cricket_AAMIpark[0][0] and Cricket_AAMIpark[0][1] <= a[0] <= Cricket_AAMIpark[1][1]) or
        (Fawknerpark[1][0] <= a[1] <= Fawknerpark[0][0] and Fawknerpark[0][1] <= a[0] <= Fawknerpark[1][1]) or
        (Fedsquare[1][0] <= a[1] <= Fedsquare[0][0] and Fedsquare[0][1] <= a[0] <= Fedsquare[1][1]) or
        (FlagstaffGardens[1][0] <= a[1] <= FlagstaffGardens[0][0] and FlagstaffGardens[0][1] <= a[0] <= FFlagstaffGardens[1][1]) or
        (Royalpark_melzoo[1][0] <= a[1] <= Royalpark_melzoo[0][0] and Royalpark_melzoo[0][1] <= a[0] <= Royalpark_melzoo[1][1]) or
        (StVincentGardens[1][0] <= a[1] <= StVincentGardens[0][0] and StVincentGardens[0][1] <= a[0] <= StVincentGardens[1][1]) or
        (UniversityOval[1][0] <= a[1] <= UniversityOval[0][0] and UniversityOval[0][1] <= a[0] <= UniversityOval[1][1]) or
        (ikon_princesPark[1][0] <= a[1] <= ikon_princesPark[0][0] and ikon_princesPark[0][1] <= a[0] <= ikon_princesPark[1][1]) or
        (melBotanic[1][0] <= a[1] <= melBotanic[0][0] and melBotanic[0][1] <= a[0] <= melBotanic[1][1])):
            green.append(post)
        else:
            ng.append(post)
    
    i = i + 1

        
        

#for po in per:       
    #print json.dumps(po     
     #  json.dumps(y[1])
        
if s[9] == 'p':
    print 'perth green: ', len(green)
    print 'perth ngree: ', len(ng)
if s[9] == 'b':
    print 'bris green: ',  len(green)
    print 'bris ngree: ', len(ng)
if s[9] == 's':
    print 'syd green: ', len(green)
    print 'syd ngree: ', len(ng)
if s[9] == 'm':
    print 'mel green: ',  len(green)
    print 'mel ngree: ',  len(ng)


f_green = ''
f_ng = ''
if s[9] == 'p':
    f_green = 'per-tweets-green.json'
    f_ng = 'per-tweets-ng.json'
if s[9] == 'b':
    f_green = 'bris-tweets-green.json'
    f_ng = 'bris-tweets-ng.json'
if s[9] == 's':
    f_green = 'syd-tweets-green.json'
    f_ng = 'syd-tweets-ng.json'
if s[9] == 'm':
    f_green = 'mel-tweets-green.json'
    f_ng = 'mel-tweets-ng.json'



with open(f_green, 'w') as nf:
    for po in green:
        nf.write(json.dumps(po[1])) 
        nf.write("\n")

with open(f_ng, 'w') as nf:
    for po in ng:
        nf.write(json.dumps(po[1])) 
        nf.write("\n")
