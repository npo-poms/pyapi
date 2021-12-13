from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class ChannelEnum(Enum):
    """
    :cvar NED1: NPO 1.
    :cvar NED2: NPO 2.
    :cvar NED3: NPO 3 &amp; Z@pp.
    :cvar NEDE: Nederland-e.
    :cvar RTL4: RTL 4.
    :cvar RTL5: RTL 5.
    :cvar SBS6: SBS 6.
    :cvar RTL7: RTL 7.
    :cvar VERO: Veronica/Jetix.
    :cvar NET5: Net 5.
    :cvar RTL8: RTL 8.
    :cvar REGI: Regional TV combi-channel.
    :cvar OFRY: Omrop Fryslân tv.
    :cvar NOOR: TV Noord.
    :cvar RTVD: RTV Drenthe.
    :cvar OOST: TV Oost.
    :cvar GELD: TV Gelderland.
    :cvar FLEV: TV Flevoland.
    :cvar BRAB: Omroep Brabant.
    :cvar REGU: Regio TV Utrecht.
    :cvar NORH: TV Noord-Holland.
    :cvar WEST: TV West.
    :cvar RIJN: TV Rijnmond.
    :cvar L1_TV: L1 TV.
    :cvar OZEE: Omroep Zeeland.
    :cvar AT5: AT5.
    :cvar RNN7: RNN7.
    :cvar BVNT: BVN.
    :cvar EEN: Eén.
    :cvar KETN: Ketnet &amp; Canvas.
    :cvar VTM: VTM.
    :cvar KA2: 2BE.
    :cvar VT4: VT4.
    :cvar LUNE: La Une (RTBF 1).
    :cvar LDUE: La Deux (RTBF 2).
    :cvar RTBF: RTBF Sat.
    :cvar ARD: ARD.
    :cvar ZDF: ZDF.
    :cvar WDR: WDR Fehrsehen
    :cvar N_3: N3 (NDR).
    :cvar SUDW: SWF Baden-Württemberg.
    :cvar SWF: SWF Rheinland-Pfalz.
    :cvar RTL: RTL Television.
    :cvar SAT1: Sat1.
    :cvar PRO7: Pro7.
    :cvar VALUE_3_SAT: 3 Sat.
    :cvar KABE: Kabel 1.
    :cvar ARTE: ARTE France
    :cvar ART: ARTE Deutschland
    :cvar T5_ME: TV 5 Monde Europe.
    :cvar FRA2: France 2.
    :cvar FRA3: France 3.
    :cvar BBC1: BBC 1.
    :cvar BBC2: BBC 2.
    :cvar BBTH: BBC Three.
    :cvar BBTC: BBC Three / CBBC.
    :cvar BBCF: BBC Four.
    :cvar BBFC: BBC Four / Ceebies.
    :cvar BBCP: BBC Prime.
    :cvar TRTI: TRT International.
    :cvar SHOW: ShowTV.
    :cvar LIGT: LigTV.
    :cvar TURK: Türkmax.
    :cvar ATVT: ATV.
    :cvar FOXT: Fox Türk.
    :cvar HABN: HaberTürk.
    :cvar STTV: Star TV.
    :cvar RRTM: RTM.
    :cvar RMBC: MBC.
    :cvar RART: ART Europe.
    :cvar ARTM: ART Movie.
    :cvar TVBS: TVBS Europe.
    :cvar ASIA: Sony Ent TV MAX.
    :cvar TIVI: A-Tivi.
    :cvar B4_UM: B4U Movies.
    :cvar PCNE: Phoenix CNE.
    :cvar PATN: ATN.
    :cvar ZEET: Zee TV.
    :cvar ZEEC: Zee Cinema.
    :cvar TVE: TVE.
    :cvar RAI: Rai Uno.
    :cvar RAID: Rai Due.
    :cvar RAIT: Rai Tre.
    :cvar TEVE: TeVe Sur.
    :cvar ERTS: ERT Sat.
    :cvar STV: STV.
    :cvar NTV: NTV.
    :cvar TVPO: TV Polonia.
    :cvar NOSJ: NOS Journaal 24.
    :cvar CULT: Cultura.
    :cvar VALUE_101: 101.
    :cvar PO24: Politiek24.
    :cvar HILV: HilversumBest.
    :cvar HOLL: Holland Doc.
    :cvar GESC: /Geschiedenis.
    :cvar VALUE_3_VCN: 3voor12 Central.
    :cvar VALUE_3_VOS: 3voor12 On Stage.
    :cvar STER: Sterren.nl.
    :cvar NCRV: Spirit24.
    :cvar OPVO: Zappelin24/Familie24.
    :cvar CONS: Consumenten TV.
    :cvar HUMO: Humor TV.
    :cvar ENTE: E! Enterntainment.
    :cvar FASH: Fashion TV.
    :cvar COMC: Comedy Central/Nickelodeon.
    :cvar TBN: TBN Europe.
    :cvar DISC: Discovery Channel.
    :cvar ZONE: Zone Reality (UK).
    :cvar ANPL: Animal Planet.
    :cvar CLUB: Zone Club.
    :cvar NAGE: National Geographic/CNBC.
    :cvar TRAC: Trace TV.
    :cvar NGHD: National Geographic HD.
    :cvar WILD: Nat Geo Wild.
    :cvar GARU: Garuda TV.
    :cvar ZAZA: Zazaro TV.
    :cvar FAM7: Family7.
    :cvar DTAL: Discovery Travel &amp; Living.
    :cvar SCIE: Discovery Science.
    :cvar CIVI: Discovery Civilisation.
    :cvar DIHD: Discovery HD.
    :cvar HIST: The History Channel.
    :cvar TRAV: Travel Channel.
    :cvar HETG: Het Gesprek.
    :cvar GOED: GoedTV.
    :cvar BABY: Baby TV (NL).
    :cvar DH1: HD-NL.
    :cvar LITV: Liberty TV.
    :cvar LIVE: Liveshop.
    :cvar STAR: Star!
    :cvar WEER: Weerkanaal.
    :cvar REAL: Zone Reality.
    :cvar SCIF: Sci-Fi Channel.
    :cvar VALUE_13_ST: 13th Street.
    :cvar CARC: Car Channel.
    :cvar NOSN: NostalgieNet.
    :cvar HISH: The History Channel HD.
    :cvar BRHD: Brava HD.
    :cvar FANT: Fan TV.
    :cvar RACW: Raceworld TV.
    :cvar COMF: Comedy Family.
    :cvar DIER: AVRO Dier en Natuur.
    :cvar POKE: Poker Channel.
    :cvar MNET: Misdaadnet.
    :cvar VOOM: Voom HD.
    :cvar ZONH: Zone Horror.
    :cvar KPN1: Eredivisie Live 1.
    :cvar KPN2: Eredivisie Live 2.
    :cvar KPN3: Eredivisie Live 3.
    :cvar KPN4: Eredivisie Live 4.
    :cvar ZIZO: PO Zizone TV.
    :cvar DVIC: Viceland.
    :cvar DVB1: PO DVB-H 1.
    :cvar DVB2: PO DVB-H 2.
    :cvar DVB3: PO DVB-H 3.
    :cvar NICK: Nickelodeon.
    :cvar NIJN: Nick Jr.
    :cvar NIKT: Nick Toons.
    :cvar NIKH: Nick Hits.
    :cvar CART: Cartoon Network.
    :cvar BOOM: Boomerang.
    :cvar CNN: CNN.
    :cvar BBCW: BBC World.
    :cvar EURN: Euronews.
    :cvar SKNE: Sky News.
    :cvar BLOO: Bloomberg TV.
    :cvar CNBC: CNBC Europe.
    :cvar PALJ: Al Jazeera Arabic.
    :cvar ALJA: Al Jazeera.
    :cvar FOXN: Fox News.
    :cvar FXNL: Fox Nederland.
    :cvar MTV: MTV.
    :cvar MTV2: MTV2.
    :cvar HITS: MTV Hits.
    :cvar BASE: MTV Base.
    :cvar MTVB: MTV Brand New.
    :cvar TMF: TMF.
    :cvar TMFN: TMF NL.
    :cvar TMFP: TMF Party.
    :cvar TMFY: TMF Pure.
    :cvar TVOR: TV Oranje.
    :cvar VH1_E: VH-1 (EU).
    :cvar VH1_C: VH-1 Classic.
    :cvar PERC: Performance Channel.
    :cvar MEZZ: Mezzo.
    :cvar EURO: Eurosport.
    :cvar EUR2: Eurosport 2.
    :cvar EXTR: Extreme Sports Channel (EU).
    :cvar MOTO: Motors TV.
    :cvar SAIL: Sailing channel.
    :cvar ESPN: ESPN.
    :cvar NASE: ESPN America.
    :cvar SP11: Sport1.1.
    :cvar SP12: Sport1.2.
    :cvar SP13: Sport1.3.
    :cvar SP14: Sport1.4.
    :cvar SP15: Sport1.5.
    :cvar SP16: Sport1.6.
    :cvar SP17: Sport1.7.
    :cvar SP18: Sport1.8.
    :cvar S1_HD: Sport1 HD.
    :cvar FIL1: Film1.1 pepe.
    :cvar FIL2: Film1.2 pepe.
    :cvar FIL3: Film1.3 pepe.
    :cvar FL11: Film1.1 DI.
    :cvar FL1_P: Film1+1 DI.
    :cvar FL12: Film1.2 DI.
    :cvar FL13: Film1.3 DI.
    :cvar FLHD: Film1 HD DI.
    :cvar MGMM: MGM Movie Channel.
    :cvar TCM: TCM.
    :cvar HALL: Hallmark.
    :cvar ACNW: Action Now!
    :cvar RHUS: Hustler TV.
    :cvar PLAY: Playboy TV.
    :cvar ADUL: Adult Channel.
    :cvar PSPI: Private Spice.
    :cvar HUST: Blue Hustler.
    :cvar OXMO: PO X-MO.
    :cvar XM24: X-MO DI.
    :cvar OU24: PO Out TV.
    :cvar RAD1: NPO Radio 1.
    :cvar RAD2: NPO Radio 2.
    :cvar R2_SJ:
    :cvar RAD3: NPO 3FM.
    :cvar R3_KX:
    :cvar R3_AL:
    :cvar RAD4: NPO Radio 4.
    :cvar R4_CO:
    :cvar RAD5: NPO Radio 5.
    :cvar R5_ST:
    :cvar RAD6: NPO Radio 6.
    :cvar REGR: Regional radio combi-channel.
    :cvar RFRY: Omrop Fryslân radio.
    :cvar DRRD: Radio Drenthe.
    :cvar RNOO: Radio Noord.
    :cvar ROST: Radio Oost.
    :cvar RGEL: Radio Gelderland.
    :cvar RFLE: Radio Flevoland.
    :cvar RBRA: Omroep Brabant.
    :cvar RUTR: Radio M Utrecht.
    :cvar RNOH: Radio Noord-Holland.
    :cvar RWST: 89,3 Radio West.
    :cvar RRIJ: Radio Rijnmond.
    :cvar LRAD: L1 Radio.
    :cvar RZEE: Omroep Zeeland.
    :cvar COMM: Commercial radio combi-channel.
    :cvar RVER: Radio Veronica.
    :cvar SLAM: SLAM! FM.
    :cvar SKYR: Sky Radio.
    :cvar BNRN: BNR Nieuwsradio.
    :cvar KINK: Kink FM.
    :cvar PCAZ: CAZ!.
    :cvar QMUS: Qmusic.
    :cvar R538: Radio 538.
    :cvar GOLD: Radio 10 Gold.
    :cvar ARRO: Arrow Classic Rock.
    :cvar FUNX: FunX.
    :cvar FUNA: FunX Amsterdam.
    :cvar FUNR: FunX Rotterdam.
    :cvar FUNU: FunX Utrecht.
    :cvar FUNG: FunX Den Haag.
    :cvar FUNB: FunX Arab
    :cvar FUND: FunX Dance
    :cvar FUNH: FunX HipHop
    :cvar FUNL: FunX Latin
    :cvar FUNJ: FunX Reggae
    :cvar FUNS: FunX SlowJamz
    :cvar FUNF: FunX Fissa
    :cvar CLAS: Classic FM.
    :cvar BEL1: VRT/Radio 1.
    :cvar BEL2: VRT/Radio 2.
    :cvar KLAR: Klara.
    :cvar BBR1: BBC Radio 1.
    :cvar BBR2: BBC Radio 2.
    :cvar BBR3: BBC Radio 3.
    :cvar BBR4: BBC Radio 4.
    :cvar BBWS: BBC Worldservice.
    :cvar BBCX: BBC 1XTRA.
    :cvar NDR3: NDR3.
    :cvar WDR4: WDR 4.
    :cvar WDR3: WDR3.
    :cvar ONL1: NPO Online 1
    :cvar OMEG: Omega TV
    :cvar D24_K:
    :cvar H1_NL:
    :cvar SYFY:
    :cvar SBS9:
    :cvar DIXD:
    :cvar BRNL:
    :cvar FOXL:
    :cvar TLC:
    :cvar BCFS:
    :cvar AMC:
    :cvar FLM1:
    :cvar ZGS1:
    :cvar BRTZ:
    :cvar RTLF:
    :cvar TVDR:
    :cvar VRTC:
    :cvar VALUE_10_TB: NPO 1 Extra
    :cvar TRT1: TRT 1
    :cvar ALJI: Al Jazeera English
    :cvar SPID: Spike Nederland
    :cvar XXXX: Test channel. This channel only exist for the sake of testing.
    """
    NED1 = "NED1"
    NED2 = "NED2"
    NED3 = "NED3"
    NEDE = "NEDE"
    RTL4 = "RTL4"
    RTL5 = "RTL5"
    SBS6 = "SBS6"
    RTL7 = "RTL7"
    VERO = "VERO"
    NET5 = "NET5"
    RTL8 = "RTL8"
    REGI = "REGI"
    OFRY = "OFRY"
    NOOR = "NOOR"
    RTVD = "RTVD"
    OOST = "OOST"
    GELD = "GELD"
    FLEV = "FLEV"
    BRAB = "BRAB"
    REGU = "REGU"
    NORH = "NORH"
    WEST = "WEST"
    RIJN = "RIJN"
    L1_TV = "L1TV"
    OZEE = "OZEE"
    AT5 = "AT5_"
    RNN7 = "RNN7"
    BVNT = "BVNT"
    EEN = "EEN_"
    KETN = "KETN"
    VTM = "VTM_"
    KA2 = "KA2_"
    VT4 = "VT4_"
    LUNE = "LUNE"
    LDUE = "LDUE"
    RTBF = "RTBF"
    ARD = "ARD_"
    ZDF = "ZDF_"
    WDR = "WDR_"
    N_3 = "N_3_"
    SUDW = "SUDW"
    SWF = "SWF_"
    RTL = "RTL_"
    SAT1 = "SAT1"
    PRO7 = "PRO7"
    VALUE_3_SAT = "3SAT"
    KABE = "KABE"
    ARTE = "ARTE"
    ART = "ART"
    T5_ME = "T5ME"
    FRA2 = "FRA2"
    FRA3 = "FRA3"
    BBC1 = "BBC1"
    BBC2 = "BBC2"
    BBTH = "BBTH"
    BBTC = "BBTC"
    BBCF = "BBCF"
    BBFC = "BBFC"
    BBCP = "BBCP"
    TRTI = "TRTI"
    SHOW = "SHOW"
    LIGT = "LIGT"
    TURK = "TURK"
    ATVT = "ATVT"
    FOXT = "FOXT"
    HABN = "HABN"
    STTV = "STTV"
    RRTM = "RRTM"
    RMBC = "RMBC"
    RART = "RART"
    ARTM = "ARTM"
    TVBS = "TVBS"
    ASIA = "ASIA"
    TIVI = "TIVI"
    B4_UM = "B4UM"
    PCNE = "PCNE"
    PATN = "PATN"
    ZEET = "ZEET"
    ZEEC = "ZEEC"
    TVE = "TVE_"
    RAI = "RAI_"
    RAID = "RAID"
    RAIT = "RAIT"
    TEVE = "TEVE"
    ERTS = "ERTS"
    STV = "STV_"
    NTV = "NTV_"
    TVPO = "TVPO"
    NOSJ = "NOSJ"
    CULT = "CULT"
    VALUE_101 = "101_"
    PO24 = "PO24"
    HILV = "HILV"
    HOLL = "HOLL"
    GESC = "GESC"
    VALUE_3_VCN = "3VCN"
    VALUE_3_VOS = "3VOS"
    STER = "STER"
    NCRV = "NCRV"
    OPVO = "OPVO"
    CONS = "CONS"
    HUMO = "HUMO"
    ENTE = "ENTE"
    FASH = "FASH"
    COMC = "COMC"
    TBN = "TBN_"
    DISC = "DISC"
    ZONE = "ZONE"
    ANPL = "ANPL"
    CLUB = "CLUB"
    NAGE = "NAGE"
    TRAC = "TRAC"
    NGHD = "NGHD"
    WILD = "WILD"
    GARU = "GARU"
    ZAZA = "ZAZA"
    FAM7 = "FAM7"
    DTAL = "DTAL"
    SCIE = "SCIE"
    CIVI = "CIVI"
    DIHD = "DIHD"
    HIST = "HIST"
    TRAV = "TRAV"
    HETG = "HETG"
    GOED = "GOED"
    BABY = "BABY"
    DH1 = "DH1_"
    LITV = "LITV"
    LIVE = "LIVE"
    STAR = "STAR"
    WEER = "WEER"
    REAL = "REAL"
    SCIF = "SCIF"
    VALUE_13_ST = "13ST"
    CARC = "CARC"
    NOSN = "NOSN"
    HISH = "HISH"
    BRHD = "BRHD"
    FANT = "FANT"
    RACW = "RACW"
    COMF = "COMF"
    DIER = "DIER"
    POKE = "POKE"
    MNET = "MNET"
    VOOM = "VOOM"
    ZONH = "ZONH"
    KPN1 = "KPN1"
    KPN2 = "KPN2"
    KPN3 = "KPN3"
    KPN4 = "KPN4"
    ZIZO = "ZIZO"
    DVIC = "DVIC"
    DVB1 = "DVB1"
    DVB2 = "DVB2"
    DVB3 = "DVB3"
    NICK = "NICK"
    NIJN = "NIJN"
    NIKT = "NIKT"
    NIKH = "NIKH"
    CART = "CART"
    BOOM = "BOOM"
    CNN = "CNN_"
    BBCW = "BBCW"
    EURN = "EURN"
    SKNE = "SKNE"
    BLOO = "BLOO"
    CNBC = "CNBC"
    PALJ = "PALJ"
    ALJA = "ALJA"
    FOXN = "FOXN"
    FXNL = "FXNL"
    MTV = "MTV_"
    MTV2 = "MTV2"
    HITS = "HITS"
    BASE = "BASE"
    MTVB = "MTVB"
    TMF = "TMF_"
    TMFN = "TMFN"
    TMFP = "TMFP"
    TMFY = "TMFY"
    TVOR = "TVOR"
    VH1_E = "VH1E"
    VH1_C = "VH1C"
    PERC = "PERC"
    MEZZ = "MEZZ"
    EURO = "EURO"
    EUR2 = "EUR2"
    EXTR = "EXTR"
    MOTO = "MOTO"
    SAIL = "SAIL"
    ESPN = "ESPN"
    NASE = "NASE"
    SP11 = "SP11"
    SP12 = "SP12"
    SP13 = "SP13"
    SP14 = "SP14"
    SP15 = "SP15"
    SP16 = "SP16"
    SP17 = "SP17"
    SP18 = "SP18"
    S1_HD = "S1HD"
    FIL1 = "FIL1"
    FIL2 = "FIL2"
    FIL3 = "FIL3"
    FL11 = "FL11"
    FL1_P = "FL1P"
    FL12 = "FL12"
    FL13 = "FL13"
    FLHD = "FLHD"
    MGMM = "MGMM"
    TCM = "TCM_"
    HALL = "HALL"
    ACNW = "ACNW"
    RHUS = "RHUS"
    PLAY = "PLAY"
    ADUL = "ADUL"
    PSPI = "PSPI"
    HUST = "HUST"
    OXMO = "OXMO"
    XM24 = "XM24"
    OU24 = "OU24"
    RAD1 = "RAD1"
    RAD2 = "RAD2"
    R2_SJ = "R2SJ"
    RAD3 = "RAD3"
    R3_KX = "R3KX"
    R3_AL = "R3AL"
    RAD4 = "RAD4"
    R4_CO = "R4CO"
    RAD5 = "RAD5"
    R5_ST = "R5ST"
    RAD6 = "RAD6"
    REGR = "REGR"
    RFRY = "RFRY"
    DRRD = "DRRD"
    RNOO = "RNOO"
    ROST = "ROST"
    RGEL = "RGEL"
    RFLE = "RFLE"
    RBRA = "RBRA"
    RUTR = "RUTR"
    RNOH = "RNOH"
    RWST = "RWST"
    RRIJ = "RRIJ"
    LRAD = "LRAD"
    RZEE = "RZEE"
    COMM = "COMM"
    RVER = "RVER"
    SLAM = "SLAM"
    SKYR = "SKYR"
    BNRN = "BNRN"
    KINK = "KINK"
    PCAZ = "PCAZ"
    QMUS = "QMUS"
    R538 = "R538"
    GOLD = "GOLD"
    ARRO = "ARRO"
    FUNX = "FUNX"
    FUNA = "FUNA"
    FUNR = "FUNR"
    FUNU = "FUNU"
    FUNG = "FUNG"
    FUNB = "FUNB"
    FUND = "FUND"
    FUNH = "FUNH"
    FUNL = "FUNL"
    FUNJ = "FUNJ"
    FUNS = "FUNS"
    FUNF = "FUNF"
    CLAS = "CLAS"
    BEL1 = "BEL1"
    BEL2 = "BEL2"
    KLAR = "KLAR"
    BBR1 = "BBR1"
    BBR2 = "BBR2"
    BBR3 = "BBR3"
    BBR4 = "BBR4"
    BBWS = "BBWS"
    BBCX = "BBCX"
    NDR3 = "NDR3"
    WDR4 = "WDR4"
    WDR3 = "WDR3"
    ONL1 = "ONL1"
    OMEG = "OMEG"
    D24_K = "D24K"
    H1_NL = "H1NL"
    SYFY = "SYFY"
    SBS9 = "SBS9"
    DIXD = "DIXD"
    BRNL = "BRNL"
    FOXL = "FOXL"
    TLC = "TLC_"
    BCFS = "BCFS"
    AMC = "AMC_"
    FLM1 = "FLM1"
    ZGS1 = "ZGS1"
    BRTZ = "BRTZ"
    RTLF = "RTLF"
    TVDR = "TVDR"
    VRTC = "VRTC"
    VALUE_10_TB = "10TB"
    TRT1 = "TRT1"
    ALJI = "ALJI"
    SPID = "SPID"
    XXXX = "XXXX"
