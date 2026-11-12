
import tkinter as tk
import unicodedata

# =====================================
# EKO ASİSTAN - GERİ DÖNÜŞÜM SİSTEMİ
# TURUNCU - YEŞİL - BEYAZ TEMA
# =====================================

# RENKLER
ARKA_PLAN = "#F1F8E9"
KOYU_YESIL = "#1B5E20"
YESIL = "#43A047"
ACIK_YESIL = "#C8E6C9"
TURUNCU = "#F57C00"
ACIK_TURUNCU = "#FFF3E0"
BEYAZ = "#FFFFFF"
YAZI = "#263238"
KIRMIZI = "#C62828"

# ATIK GRUPLARI
ATIK_GRUPLARI = {
    "Plastik": [
        "plastik şişe", "pet şişe", "plastik kap",
        "plastik bardak", "plastik tabak",
        "plastik çatal", "plastik kaşık",
        "plastik ambalaj", "yoğurt kabı",
        "deterjan şişesi", "şampuan şişesi",
        "su şişesi", "plastik kapak",
        "temiz poşet", "streç film",
        "plastik oyuncak", "plastik bidon"
    ],

    "Kağıt": [
        "gazete", "dergi", "kitap",
        "defter", "kağıt", "fotokopi kağıdı",
        "karton", "karton kutu",
        "mukavva", "kağıt torba",
        "broşür", "zarf", "poster",
        "yumurta kolisi", "koli",
        "ambalaj kağıdı"
    ],

    "Cam": [
        "cam şişe", "cam kavanoz",
        "reçel kavanozu", "turşu kavanozu",
        "parfüm şişesi", "cam sos şişesi",
        "cam içecek şişesi"
    ],

    "Metal": [
        "konserve kutusu", "teneke kutu",
        "metal içecek kutusu",
        "alüminyum kutu", "metal kapak",
        "alüminyum folyo", "metal ambalaj",
        "çelik kutu", "metal kavanoz kapağı"
    ],

    "Organik": [
        "muz kabuğu", "elma kabuğu",
        "portakal kabuğu", "mandalina kabuğu",
        "patates kabuğu", "soğan kabuğu",
        "sebze artığı", "meyve artığı",
        "çay posası", "kahve telvesi",
        "yumurta kabuğu", "kuru yaprak",
        "çim artığı", "çiçek artığı",
        "bitki artığı"
    ],

    "Elektronik": [
        "eski telefon", "bozuk telefon",
        "bilgisayar", "klavye", "fare",
        "monitör", "televizyon",
        "yazıcı", "tablet", "kulaklık",
        "şarj cihazı", "usb kablo",
        "elektrik kablosu", "modem",
        "kumanda", "elektronik oyuncak",
        "bozuk radyo", "eski kamera",
        "elektrikli süpürge"
    ],

    "Pil ve Batarya": [
        "kalem pil", "ince pil",
        "düğme pil", "şarjlı pil",
        "telefon bataryası",
        "lityum pil", "powerbank",
        "laptop bataryası", "akü"
    ],

    "Tekstil": [
        "eski tişört", "eski pantolon",
        "eski gömlek", "eski kazak",
        "eski mont", "eski ayakkabı",
        "eski çanta", "eski perde",
        "eski havlu", "eski çarşaf",
        "kumaş parçası", "eski elbise"
    ],

    "Tehlikeli Atık": [
        "boya kutusu", "tiner",
        "solvent", "böcek ilacı",
        "motor yağı", "antifriz",
        "kimyasal temizleyici",
        "floresan lamba",
        "enerji tasarruflu ampul"
    ],

    "İlaç Atığı": [
        "son kullanma tarihi geçmiş ilaç",
        "eski ilaç", "ilaç tableti",
        "şurup", "kullanılmayan ilaç"
    ],

    "Bitkisel Atık Yağ": [
        "kızartma yağı", "atık yemeklik yağ",
        "kullanılmış ayçiçek yağı",
        "kullanılmış zeytinyağı"
    ],

    "Genel Çöp": [
        "kirli peçete", "ıslak mendil",
        "bebek bezi", "kirli sünger",
        "sigara izmariti", "süpürge tozu",
        "kirli kağıt havlu"
    ]
}

# TOPLAMA YERLERİ
YONLENDIRMELER = {
    "Plastik": "Plastik ambalaj toplama kutusu",
    "Kağıt": "Kağıt ve karton toplama kutusu",
    "Cam": "Cam ambalaj toplama kutusu",
    "Metal": "Metal ambalaj toplama kutusu",
    "Organik": "Uygun organik atık / kompost sistemi",
    "Elektronik": "Elektronik atık toplama merkezi",
    "Pil ve Batarya": "Pil / batarya toplama noktası",
    "Tekstil": "Tekstil toplama / yeniden kullanım noktası",
    "Tehlikeli Atık": "Tehlikeli atık toplama noktası",
    "İlaç Atığı": "Atık ilaç toplama noktası",
    "Bitkisel Atık Yağ": "Bitkisel atık yağ toplama noktası",
    "Genel Çöp": "Evsel atık kutusu"
}


def normalleştir(metin):
    metin = metin.casefold().replace("ı", "i")
    metin = unicodedata.normalize("NFKD", metin)

    return "".join(
        harf for harf in metin
        if not unicodedata.combining(harf)
    ).strip()


# ARAMA SÖZLÜĞÜ
ATIKLAR = {}

for kategori, atik_listesi in ATIK_GRUPLARI.items():
    for atik in atik_listesi:
        ATIKLAR[normalleştir(atik)] = (atik, kategori)


def atik_ara(event=None):
    aranan = normalleştir(giris.get())

    eslesenler = [
        bilgi[0]
        for anahtar, bilgi in ATIKLAR.items()
        if aranan in anahtar
    ]

    liste.delete(0, tk.END)

    for atik in sorted(eslesenler):
        liste.insert(tk.END, atik)


def atik_kontrol(event=None):
    aranan = normalleştir(giris.get())

    if aranan not in ATIKLAR:
        sonuc.config(
            text="Atık bulunamadı!\nListeden bir atık seçebilirsin.",
            fg=KIRMIZI,
            bg=ACIK_TURUNCU
        )
        return

    ad, kategori = ATIKLAR[aranan]
    yer = YONLENDIRMELER[kategori]

    sonuc.config(
        text=(
            f"♻ ATIK BİLGİSİ ♻\n\n"
            f"Atık: {ad.title()}\n\n"
            f"Kategori: {kategori}\n\n"
            f"Toplama yeri:\n{yer}"
        ),
        fg=KOYU_YESIL,
        bg=ACIK_YESIL
    )


def listeden_sec(event=None):
    secim = liste.curselection()

    if secim:
        atik = liste.get(secim[0])

        giris.delete(0, tk.END)
        giris.insert(0, atik)

        atik_kontrol()


def temizle():
    giris.delete(0, tk.END)

    sonuc.config(
        text="",
        bg=BEYAZ
    )

    atik_ara()
    giris.focus_set()


# =====================================
# ANA PENCERE
# =====================================

pencere = tk.Tk()
pencere.title("EKO ASİSTAN")
pencere.geometry("680x780")
pencere.minsize(540, 680)
pencere.configure(bg=ARKA_PLAN)

# BAŞLIK ALANI
baslik_cerceve = tk.Frame(
    pencere,
    bg=TURUNCU
)
baslik_cerceve.pack(fill="x")

tk.Label(
    baslik_cerceve,
    text="🌍 EKO ASİSTAN ♻",
    font=("Arial", 26, "bold"),
    bg=TURUNCU,
    fg=BEYAZ
).pack(pady=18)

# ALT BAŞLIK
toplam = sum(
    len(atik_listesi)
    for atik_listesi in ATIK_GRUPLARI.values()
)

tk.Label(
    pencere,
    text=f"♻ {toplam} Atık  |  {len(ATIK_GRUPLARI)} Kategori",
    font=("Arial", 13, "bold"),
    bg=ARKA_PLAN,
    fg=KOYU_YESIL
).pack(pady=14)

tk.Label(
    pencere,
    text="Hangi atığı geri dönüştürmek istiyorsun?",
    font=("Arial", 13, "bold"),
    bg=ARKA_PLAN,
    fg=TURUNCU
).pack(pady=10)

# ARAMA KUTUSU
giris = tk.Entry(
    pencere,
    font=("Arial", 15),
    width=32,
    justify="center",
    bg=BEYAZ,
    fg=KOYU_YESIL,
    insertbackground=TURUNCU,
    relief="solid",
    bd=2,
    highlightthickness=2,
    highlightbackground=ACIK_YESIL,
    highlightcolor=TURUNCU
)
giris.pack(pady=8)

giris.bind("<KeyRelease>", atik_ara)
giris.bind("<Return>", atik_kontrol)

# KONTROL BUTONU
tk.Button(
    pencere,
    text="♻ ATIK KONTROL ET",
    command=atik_kontrol,
    bg=TURUNCU,
    fg=BEYAZ,
    activebackground=YESIL,
    activeforeground=BEYAZ,
    font=("Arial", 13, "bold"),
    padx=25,
    pady=12,
    relief="flat",
    cursor="hand2"
).pack(pady=12)

# LİSTE BAŞLIĞI
tk.Label(
    pencere,
    text="Atık listesinden de seçim yapabilirsin:",
    font=("Arial", 11, "bold"),
    bg=ARKA_PLAN,
    fg=KOYU_YESIL
).pack(pady=8)

# LİSTE ÇERÇEVESİ
liste_cerceve = tk.Frame(
    pencere,
    bg=YESIL,
    padx=3,
    pady=3
)
liste_cerceve.pack(pady=5)

kaydirma = tk.Scrollbar(
    liste_cerceve,
    bg=ACIK_YESIL,
    activebackground=TURUNCU
)
kaydirma.pack(side=tk.RIGHT, fill=tk.Y)

liste = tk.Listbox(
    liste_cerceve,
    width=43,
    height=9,
    font=("Arial", 11),
    bg=BEYAZ,
    fg=KOYU_YESIL,
    selectbackground=TURUNCU,
    selectforeground=BEYAZ,
    yscrollcommand=kaydirma.set,
    relief="flat",
    bd=0
)
liste.pack(side=tk.LEFT)

kaydirma.config(command=liste.yview)
liste.bind("<<ListboxSelect>>", listeden_sec)

# SONUÇ KUTUSU
sonuc = tk.Label(
    pencere,
    text="",
    font=("Arial", 13, "bold"),
    bg=BEYAZ,
    fg=KOYU_YESIL,
    justify="center",
    wraplength=520,
    width=44,
    height=8
)
sonuc.pack(pady=16, padx=15)

# TEMİZLE BUTONU
tk.Button(
    pencere,
    text="TEMİZLE",
    command=temizle,
    bg=YESIL,
    fg=BEYAZ,
    activebackground=TURUNCU,
    activeforeground=BEYAZ,
    font=("Arial", 11, "bold"),
    padx=30,
    pady=8,
    relief="flat",
    cursor="hand2"
).pack(pady=5)

# ALT MESAJ
tk.Label(
    pencere,
    text="🌱 Daha temiz bir dünya bizim elimizde!",
    bg=ARKA_PLAN,
    fg=KOYU_YESIL,
    font=("Arial", 11, "italic")
).pack(pady=12)

# BAŞLAT
atik_ara()
giris.focus_set()

pencere.mainloop()
