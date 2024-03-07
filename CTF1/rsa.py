p = 31203823011584293925292892004768678649007921708143724964523519434907490075137389666516064079173254239505333474794435766970228843102239992137832894131350011905468150917706124386258572937863199733149240701268555972817079969652039795476469278334586085530607952924800664113490486256193938613820292293524853005676568892668889192631598074631721009287826261714432706926381380464605850727048882458896778227356544651551181517341492622399136673570067578290100351866114320782473149388462778330435097901102952490454089237351200568715122143441147203687562565555787033366214196556369451537513348936174435107653633307977057080460859
q = 31263585120264030826786194924675306496663476970794735668075948000546642462448666478763554441698290110927903655145580138144302266361421471506526210439699838348754418012881701055948083201522136266528571708533753034587322238940612874021403244190121742486095163395484548219112865298376840278254276568526051450267753258902258875801737654106647162424443221783794414390974537951667174779196982427359469307529106238459541600520562809805899226171931305322549192758828867959086977570182098276015645907913953195977410139625623559595977680936246252453364081886436040868121244682948825191345645931590608146270578781104255016111481
e = 65537
n = p * q
phi = (p - 1) * (q - 1)
k = 1
while True:
    rem = (k * phi + 1) % e
    if rem == 0:
        d = (k * phi + 1) // e
        # print(k,d)
        break
    k += 1
c = 511581927368108818998040925574090703534124600847860359457106141918794249474941144714074817393736916944656861357853105076501968275693078352340396012538168854570404122473782421363098629398083569559392377806250319686925946870105688167095543803846812626412945737046179798099419024782873329851322884878702467022570625145959757678499276881190060022977632955835997176247382944731895306052629017904365607312090186445877637427551615282094797226954281378717242896367800943259643505147199880394012459810284160419612280511045070981679599112691819037553577470567646322693176534408514822016037648876413486053102729610141578934306779895395806759398186626189066568707724861119713655520626988965901394377099961338026616299109940433438148744213779998680885828919899728585323216845120835282282916927639939823863282573769439604324322014200125470468369556299406024474720793720136575066856411479538175471744345345929941856423440708981226628738822830588095052336300946296749130498643383762081701404365895406271880024708112531000895781178511141715565660803161587961531566303481355642576890144989616635710437490927802938966836540343829068068733171275786768862917206914336925895698488088330266103532594168345236831350273979517949825503480592015021106652469844
m = pow(c, d, n)
print(m)
m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
print(m)