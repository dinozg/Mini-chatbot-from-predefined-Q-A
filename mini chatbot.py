import string
from typing import Dict, Tuple, Optional

rjecnik_osiguranja = {
    "1. Koja je svrha osiguranja?": "Svrha osiguranja je zaštita od financijskih gubitaka ili štete uzrokovane neželjenim događajima.",
    "2. Koji su osnovni tipovi osiguranja?": "Osnovni tipovi osiguranja uključuju životno osiguranje, zdravstveno osiguranje, imovinsko osiguranje i odgovornost.",
    "3. Što je premija u osiguranju?": "Premija je iznos novca koji osiguranik plaća osiguravajućem društvu kako bi bio pokriven osiguranjem.",
    "4. Kako se određuje visina premije?": "Visina premije ovisi o riziku, vrsti osiguranja, dobi osiguranika i drugim faktorima.",
    "5. Što je osigurana suma?": "Osigurana suma je maksimalni iznos koji će osiguravajuće društvo isplatiti u slučaju štete.",
    "6. Kako funkcionira životno osiguranje?": "Životno osiguranje pruža isplatu u slučaju smrti osiguranika ili nakon određenog vremenskog razdoblja.",
    "7. Koja je svrha zdravstvenog osiguranja?": "Zdravstveno osiguranje pruža pokriće za medicinske troškove i liječenje.",
    "8. Što je osiguranje od odgovornosti?": "Osiguranje od odgovornosti štiti osiguranika od financijskih posljedica štete koju može uzrokovati drugima.",
    "9. Kako se odabire osiguravajuće društvo?": "Prilikom odabira osiguravajućeg društva, važno je istražiti reputaciju, pokriće i uvjete police.",
    "10. Što je franšiza u osiguranju?": "Franšiza je iznos koji osiguranik mora platiti prije nego što osiguravajuće društvo počne pokrivati troškove štete.",
    "11. Kako se određuje rizik u osiguranju?": "Rizik u osiguranju određuje se analizom faktora poput povijesti osiguranika, vrste pokrića i drugih čimbenika.",
    "12. Što je osiguranje imovine?": "Osiguranje imovine pruža zaštitu od gubitka ili oštećenja imovine poput kuće, automobila ili poslovnog prostora.",
    "13. Kako se provodi procjena rizika u osiguranju imovine?": "Procjena rizika u osiguranju imovine uključuje ocjenu vrijednosti imovine i identifikaciju potencijalnih opasnosti.",
    "14. Koji su čimbenici koji utječu na cijenu osiguranja automobila?": "Čimbenici poput dobi vozača, vrste automobila, prijeđenih kilometara i vozačke povijesti utječu na cijenu osiguranja automobila.",
    "15. Što je polica osiguranja?": "Polica osiguranja je pravni dokument koji sadrži uvjete i odredbe osiguranja između osiguranika i osiguravajućeg društva.",
    "16. Kako funkcionira osiguranje putovanja?": "Osiguranje putovanja pruža pokriće za neočekivane događaje tijekom putovanja, poput bolesti, gubitka prtljage ili otkaza putovanja.",
    "17. Koja je uloga osigurateljskog posrednika?": "Osigurateljski posrednik pomaže osiguraniku u odabiru odgovarajućeg osiguranja i pregovara s osiguravajućim društvima.",
    "18. Što je dopunsko zdravstveno osiguranje?": "Dopunsko zdravstveno osiguranje pruža dodatno pokriće koje nadopunjuje osnovno zdravstveno osiguranje.",
    "19. Koje vrste pokrića nudi osiguranje od krađe?": "Osiguranje od krađe može pokrivati gubitak ili oštećenje imovine uzrokovano krađom ili provalom.",
    "20. Što je osiguranje od poplava?": "Osiguranje od poplava pruža pokriće za štetu uzrokovanu poplavama, često izvan uobičajenog osiguranja imovine.",
    "21. Kako se odabire pokriće od odgovornosti u poslovanju?": "Pri odabiru pokrića od odgovornosti u poslovanju, poduzeća moraju uzeti u obzir vrstu industrije, veličinu i druge čimbenike.",
    "22. Koja je razlika između osiguranja odgovornosti za profesionalne usluge i opće odgovornosti?": "Osiguranje odgovornosti za profesionalne usluge štiti od grešaka ili propusta u pružanju profesionalnih usluga, dok opća odgovornost pokriva štetu uzrokovanu općim poslovnim aktivnostima.",
    "23. Kako se određuje visina osiguranja za odgovornost u poslovanju?": "Visina osiguranja za odgovornost u poslovanju određuje se na temelju vrste poslovanja, prihoda i drugih faktora.",
    "24. Kako funkcionira osiguranje od odgovornosti vlasnika kućnih ljubimaca?": "Osiguranje od odgovornosti vlasnika kućnih ljubimaca pruža pokriće za štetu koju kućni ljubimci mogu uzrokovati drugima.",
    "25. Što je polica osiguranja odgovornosti u vožnji?": "Polica osiguranja odgovornosti u vožnji potvrđuje da vozač ima odgovarajuće osiguranje kako bi pokrio potencijalne štete drugima tijekom vožnje.",
    "26. Koja je svrha osiguranja od gubitka dohotka?": "Osiguranje od gubitka dohotka pruža financijsku zaštitu osiguraniku u slučaju gubitka prihoda zbog ozljede ili bolesti.",
    "27. Kako se određuje visina naknade u osiguranju od gubitka dohotka?": "Visina naknade u osiguranju od gubitka dohotka ovisi o prihodu osiguranika i uvjetima police.",
    "28. Što je osiguranje od cyber rizika?": "Osiguranje od cyber rizika pruža pokriće za financijske gubitke uzrokovane cyber napadima ili sigurnosnim incidentima.",
    "29. Koja je svrha osiguranja od prirodne katastrofe?": "Osiguranje od prirodne katastrofe pruža pokriće za štetu uzrokovanu prirodnim katastrofama poput potresa, uragana ili poplava.",
    "30. Kako se odabire osiguranje od odgovornosti proizvođača?": "Proizvođači odabiru osiguranje od odgovornosti kako bi bili pokriveni u slučaju štete uzrokovane njihovim proizvodima.",
    "31. Što je osiguranje od terorizma?": "Osiguranje od terorizma pruža pokriće za štetu uzrokovanu terorističkim aktima.",
    "32. Kako se određuje premija u osiguranju od terorizma?": "Premija u osiguranju od terorizma može ovisiti o lokaciji, vrsti objekta i sigurnosnim mjerama.",
    "33. Koja je svrha osiguranja od profesionalne odgovornosti?": "Osiguranje od profesionalne odgovornosti štiti pojedince od odgovornosti za greške ili propuste u obavljanju njihovih profesionalnih dužnosti.",
    "34. Kako se ocjenjuje rizik u osiguranju od profesionalne odgovornosti?": "Rizik u osiguranju od profesionalne odgovornosti ocjenjuje se analizom povijesti rada, stručnosti i vrste usluga.",
    "35. Što je osiguranje od kidnapiranja i otmica?": "Osiguranje od kidnapiranja i otmica pruža pokriće za troškove i otkup u slučaju kidnapiranja.",
    "36. Koja su tipična pokrića u policama osiguranja od kidnapiranja?": "Pokrića u policama osiguranja od kidnapiranja uključuju otkup, troškove pregovaranja i psihološku podršku.",
    "37. Kako se određuje vrijednost umjetničkih predmeta u osiguranju?": "Vrijednost umjetničkih predmeta u osiguranju određuje se procjenom stručnjaka i tržišnom vrijednošću.",
    "38. Što je osiguranje od odgovornosti proizvođača proizvoda?": "Osiguranje od odgovornosti proizvođača proizvoda pruža pokriće za štetu uzrokovanu neispravnim proizvodima.",
    "39. Kako se procjenjuje rizik od odgovornosti proizvođača proizvoda?": "Rizik od odgovornosti proizvođača proizvoda procjenjuje se analizom kvalitete proizvoda, sigurnosnih standarda i povijesti tužbi.",
    "40. Koje su vrste pokrića u osiguranju od odgovornosti poslodavca?": "Osiguranje od odgovornosti poslodavca može uključivati pokriće za radne nesreće, diskriminaciju i druge odgovornosti prema zaposlenicima.",
    "41. Što je osiguranje od odgovornosti vlasnika nekretnina?": "Osiguranje od odgovornosti vlasnika nekretnina pruža pokriće za štetu ili ozljede koje se mogu dogoditi na vlasnikovoj imovini.",
    "42. Kako se određuje premija u osiguranju od odgovornosti vlasnika nekretnina?": "Premija u osiguranju od odgovornosti vlasnika nekretnina može ovisiti o veličini imovine, njezinoj namjeni i sigurnosnim mjerama.",
    "43. Koje su prednosti osiguranja od odgovornosti u ugostiteljstvu?": "Osiguranje od odgovornosti u ugostiteljstvu pruža zaštitu od potencijalnih tužbi povezanih s poslovanjem restorana ili hotela.",
    "44. Što je osiguranje od odgovornosti za proizvode?": "Osiguranje od odgovornosti za proizvode pruža pokriće za štetu koju proizvodi mogu uzrokovati krajnjim korisnicima.",
    "45. Kako se odabire pokriće od odgovornosti u osiguranju hrane i pića?": "Pri odabiru pokrića od odgovornosti u osiguranju hrane i pića, važno je uzeti u obzir higijenske standarde, kvalitetu sastojaka i druge čimbenike.",
    "46. Koje vrste osiguranja nude zaštitu od cyber prijetnji?": "Vrste osiguranja poput cyber odgovornosti i osiguranja od cyber prijetnji pružaju pokriće za financijske gubitke uzrokovane cyber napadima.",
    "47. Kako se određuje visina osiguranja od odgovornosti za profesionalne usluge?": "Visina osiguranja od odgovornosti za profesionalne usluge određuje se na temelju vrste usluga, prihoda i rizika povezanih s djelovanjem.",
    "48. Što je osiguranje od odgovornosti za okoliš?": "Osiguranje od odgovornosti za okoliš pruža pokriće za štetu uzrokovanu štetnim utjecajem poslovanja na okoliš.",
    "49. Koje vrste osiguranja nude zaštitu od prijetnji od terorizma za poslovne subjekte?": "Osiguranje od terorizma za poslovne subjekte može uključivati pokriće za štetu na imovini, prekid poslovanja i odgovornost.",
    "50. Kako se odabire osiguranje od odgovornosti za sportske događaje?": "Pri odabiru osiguranja od odgovornosti za sportske događaje, važno je uzeti u obzir rizike povezane s organizacijom sportskih manifestacija i prisutnost publike."
}
def jaccardova_sličnost(s1:str, s2:str) -> float: 
    """Izračunava jaccardovu sličnost između dva stringa.
       Ulazni parametri:
           s1 (str)
           s2 (str)
       Povratna vrijednost:
           float
    """
    set1 = set(s1.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower().split())
    set2 = set(s2.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower().split())
    presjek = set1 & set2 
    unija = set1 | set2
    return round(len(presjek) / len(unija), 2)

def kosinusova_sličnost(s1:str, s2:str) -> float: 
    """Izračunava kosinusnu sličnost između dva stringa.
       Ulazni parametri:
           s1 (str)
           s2 (str)
       Povratna vrijednost:
           float
    """
    lista1 = s1.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower().split()
    lista2 = s2.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower().split()
    brojač1 = {x:lista1.count(x) for x in lista1}
    brojač2 = {x:lista2.count(x) for x in lista2}
    dot_produkt = sum(brojač1[x] * brojač2.get(x, 0) for x in lista1)
    magnituda1 = sum(x**2 for x in brojač1.values())**0.5
    magnituda2 = sum(x**2 for x in brojač2.values())**0.5
    if magnituda1 * magnituda2 == 0:
        return 0
    else:
        return round(dot_produkt / (magnituda1 * magnituda2), 2)

def bigrami(s1:str, s2:str, n=2) -> float:
    """Izračunava koeficijent sličnosti sukladno broju preklapajućih bigrama.
       Ulazni parametri:
           s1 (str)
           s2 (str)
       Povratna vrijednost:
           float
    """
    s1 = s1.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower()
    s2 = s2.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower()
    parovi1 = [(s1[i:i+n], i) for i in range(len(s1) - 1)]
    parovi2 = [(s2[i:i+n], i) for i in range(len(s2) - 1)]
    presjek = 0
    for par1, i in parovi1:
        for par2, j in parovi2:
            if par1 == par2:
                presjek += 1
                parovi2.remove((par2, j))
                break
    return round(2.0 * presjek / (len(s1) + len(s2)), 2)

def filtracija_rjecnika(unos:str) -> Dict[str, str]:
    """Pretražuje sva pitanja iz rječnika na pojavljivanje ključne riječi.
       Ulazni parametar:
           unos (str) : Unos od strane korisnika
       Povratna vrijednost:
           dict : Filtrirani rječnik u kojem se pojavljuju riječi iz korisnikovog unosa
    """
    unos_set = set(unos.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower().split())
    lista_pitanja = [[x,x.lstrip(string.digits).lstrip(string.punctuation).rstrip(string.punctuation).strip().lower()] for x in list(rjecnik_osiguranja.keys())]
    lista_pitanja = [x + [len(set(x[1].split()) & unos_set)] for x in lista_pitanja]
    lista_pitanja_scored = [x[0] for x in lista_pitanja if x[2] > 0]
    rjecnik_osiguranja_filtrirano = {x:rjecnik_osiguranja[x] for x in rjecnik_osiguranja.keys() if x in lista_pitanja_scored}
    return rjecnik_osiguranja_filtrirano
    
def pronađi_najsličnija_pitanja(unos:str, rjecnik_osiguranja:Dict[str, str]) -> Tuple[str|None, str|None, str|None]: 
    """Izračunava prosjek 3 metrike sličnosti te vraća najsličnija pitanja u obliku n-torke.
       Ulazni parametri:
           unos (str) : Unos od strane korisnika
           rjecnik_osiguranja (dict) : Rječnik osiguranja s pitanjima kao ključevima i odgovorima kao vrijednostima
       Povratna vrijednost:
           tuple : 3 pitanja ili None ako nema dovoljno pitanja
    """
    jaccard_rezultati = {kljuc:jaccardova_sličnost(kljuc, unos) for kljuc in rjecnik_osiguranja.keys()}
    kosinus_rezultati = {kljuc:kosinusova_sličnost(kljuc, unos) for kljuc in rjecnik_osiguranja.keys()}
    bigrami_rezultati = {kljuc:bigrami(kljuc, unos) for kljuc in rjecnik_osiguranja.keys()}
    rezultati_ukupno = {kljuc:round((jaccard_rezultati[kljuc] + kosinus_rezultati[kljuc] + bigrami_rezultati[kljuc]) / 3,2) for kljuc in rjecnik_osiguranja.keys()}
    sortirani_koeficijenti = list(sorted(rezultati_ukupno.values(), reverse=True))[:3]
    rezultati_ukupno_reverzno = {vrijednost:kljuc for kljuc, vrijednost in rezultati_ukupno.items() if vrijednost in sortirani_koeficijenti}
    if len(rezultati_ukupno_reverzno) == 0:
        najsličnije_pitanje = None
        drugo_nasjličnije_pitanje = None
        trece_najsličnije_pitanje = None
    elif len(rezultati_ukupno_reverzno) == 1:
        najsličnije_pitanje = rezultati_ukupno_reverzno[sortirani_koeficijenti[0]]
        drugo_nasjličnije_pitanje = None
        trece_najsličnije_pitanje = None
    elif len(rezultati_ukupno_reverzno) == 2:
        najsličnije_pitanje = rezultati_ukupno_reverzno[sortirani_koeficijenti[0]]
        drugo_nasjličnije_pitanje = rezultati_ukupno_reverzno[sortirani_koeficijenti[1]]
        trece_najsličnije_pitanje = None
    else: 
        najsličnije_pitanje = rezultati_ukupno_reverzno[sortirani_koeficijenti[0]]
        drugo_nasjličnije_pitanje = rezultati_ukupno_reverzno[sortirani_koeficijenti[1]]
        trece_najsličnije_pitanje = rezultati_ukupno_reverzno[sortirani_koeficijenti[2]]
    return najsličnije_pitanje, drugo_nasjličnije_pitanje, trece_najsličnije_pitanje

def glavna_funkcija() -> None:
    izlaz = False
    iteracija = 0
    while not izlaz:
        if iteracija == 0:
            unos_korisnika = input('Dobar dan, što vas danas zanima o našim proizvodima ? ').lower()
        else:
            unos_korisnika = input('Recite što vas dalje zanima o našim proizvodima ? ').lower()
        if unos_korisnika == 'kraj':
            break
        filtrirani_rjecnik = filtracija_rjecnika(unos_korisnika)
        if filtrirani_rjecnik != {}:
            rezultati_iz_rjecnika = pronađi_najsličnija_pitanja(unos_korisnika, filtrirani_rjecnik)
        else:
            rezultati_iz_rjecnika = pronađi_najsličnija_pitanja(unos_korisnika, rjecnik_osiguranja)
        print(f'Pronašao sam najsličnije pitanje vašem u našoj bazi znanja: {rezultati_iz_rjecnika[0]}')
        potvrda_korisnika = input('Molim vas potvrdu je li to pitanje na koje želite odgovor. Upišite da ili ne: ').lower().strip()
        if 'da' in potvrda_korisnika:
            print(f'Odgovor na vaše pitanje je: {rjecnik_osiguranja[rezultati_iz_rjecnika[0]]}')
            iteracija += 1
            continue
        elif 'ne' in potvrda_korisnika:
            print('Trenutak molim.')
            iteracija += 1
            if rezultati_iz_rjecnika[1] is not None:
                print(f'OK, imam još jedno pitanje slično vašem: {rezultati_iz_rjecnika[1]}')
                potvrda_korisnika = input('Molim vas potvrdu je li to pitanje na koje možda želite odgovor. Upišite da ili ne: ').lower().strip()
                iteracija += 1
                if 'da' in potvrda_korisnika:
                    print(f'Odgovor na vaše pitanje je: {rjecnik_osiguranja[rezultati_iz_rjecnika[1]]}')
                    iteracija += 1
                    continue
                elif 'ne' in potvrda_korisnika:
                    print('Samo malo, provjerit ću mogu li pronaći još jedno pitanje.')
                    if rezultati_iz_rjecnika[2] is not None:
                        print(f'Za svaki slučaj preostalo mi je još jedno pitanje slično vašem: {rezultati_iz_rjecnika[2]}')
                        potvrda_korisnika = input('Recite je li to možda pitanje na koje želite odgovor. Upišite samo da ili ne: ').lower().strip()
                        if 'da' in potvrda_korisnika:
                            print(f'Odgovor na vaše pitanje je: {rjecnik_osiguranja[rezultati_iz_rjecnika[2]]}')
                            iteracija += 1
                            continue
                    else:
                        print('Izgleda da nema više sličnih pitanja. Pokušajte opet detaljnije upisati vaše pitanje.')
                        continue
            else:
                print('Izgleda da nema više sličnih pitanja. Pokušajte opet detaljnije upisati vaše pitanje.')
                continue
glavna_funkcija()