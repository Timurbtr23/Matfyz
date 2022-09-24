Otázka Q1
Stručně napište, co pro vás bylo nejnáročnější na předchozím cvičení.
Vaše odpověď: [A1] Asi nic, to jsem vsechno vedel [/A1]

Otázka Q2
Seznam níže obsahuje různé cesty. Vyberte všechny absolutní cesty ze
seznamu (oddělte jednotlivá čísla čárkou nebo mezerou).

/etc/
../intro/
.bashrc
/dev/../etc/os-release
../share/man/man3/lseek64.3.gz

Vaše odpověď: [A2] ... [/A2]

Otázka Q3
Zkraťte následující cestu tak, aby neobsahovala žádné relativní odkazy
(tj. převeďte ji na absolutní cestu bez .. a .).

/home/../usr/./share/./man/../../lib/../../etc/ssh/.././os-release


Vaše odpověď: [A3] ... [/A3]

Otázka Q4
Vyberte z možností níže tu, které nejlépe vystihuje účel
následujího útržku Pythoního programu (komentáře jsme odstranili).
Chceme po vás vybrat nejlepší možnost (tj. nejpřesnější): odpověď
je to Pythoní kód, který něco vytiskne je sice pravdivá, ale neřeší
podstatu otázky

stats = {}
with open('/proc/meminfo', 'r') as f:
    for line in f:
        parts = line.split(":")
        stats[parts[0].strip()] = parts[1].split()[0].strip()
print(float(stats['MemFree'])/float(stats['MemTotal']))



Vytiskne první dva řádky souboru /proc/meminfo.
Vytiskne druhý sloupeček souboru /proc/meminfo, jednotlivé sloupečky
jsou odděleny dvojtečkou (:).
Vytiskne odhad volného množství paměti v procentech.
Zkontroluje, že /proc/meminfo obsahuje platná data.
Přečte /proc/meminfo a ověří, jestli je ve správném formátu.

Vaše odpověď: [A4] ... [/A4]
