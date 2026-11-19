# EventRadar

EventRadar razvijava kot mobilno aplikacijo za odkrivanje dogodkov v Sloveniji pri predmetu RVIR v študijskem letu 2026/2027. Na enem mestu želiva omogočiti pregled koncertov, zabav, festivalov, športnih in kulturnih dogodkov.

**Člana ekipe:** Tilen Gabor ([@TalonBot](https://github.com/TalonBot)) in Jan Vid Gorenjak ([@janvidgo](https://github.com/janvidgo)).

## Stanje projekta

Trenutno pripravljava zasnovo in prototipno dokumentacijo. Mobilna aplikacija, podatkovna baza in uvoznik še niso implementirani. Rok mejnika je **20. november 2026 ob 08.00 (Europe/Ljubljana)**.

## Načrtovane funkcionalnosti

- Pregled, iskanje in filtriranje dogodkov po mestu, kategoriji in datumu.
- Podrobnosti dogodka, povezava do vstopnic in prikaz na zemljevidu.
- Brskanje brez prijave ter prijava in shranjevanje priljubljenih.
- Uvoz iz dovoljenih virov s preverjanjem in prepoznavanjem podvojitev.

Komentarje in ročni vnos organizatorjev bova obravnavala kot razširitev po osnovni različici. Podrobno zasnovo in obstoječe mockupe ohranjava v [prototipni dokumentaciji](dokumentacija/EventRadar_Prototipna_Dokumentacija.docx).

## Predvidene tehnologije

| Del | Tehnologija |
| --- | --- |
| Mobilna aplikacija | Flutter in Dart |
| Podatki in prijava | Supabase, PostgreSQL, Supabase Auth in RLS |
| Uvoz dogodkov | Python |
| Zemljevid | OpenStreetMap; knjižnico in ponudnika ploščic še izbereva |
| Organizacija in preverjanje | GitHub Issues, Pull Requests in GitHub Actions |

Tehnologije izhajajo iz že pripravljene zasnove. Odprte odločitve spremljava v [načrtu dela](dokumentacija/nacrt-dela.md).

## Struktura repozitorija

```text
.github/workflows/   začetno preverjanje projekta
app/                prostor za mobilno aplikacijo Flutter
importer/           prostor za uvoznik Python
supabase/           prostor za shemo in migracije podatkovne baze
dokumentacija/      obstoječa zasnova, mockup, načrt dela in pregled mejnika
scripts/            lokalna preverjanja, ki jih izvaja tudi CI
```

## Dokumentacija in delo

- [Kazalo dokumentacije in pregled zahtev](dokumentacija/README.md)
- [Načrt razvoja in razdelitev odgovornosti](dokumentacija/nacrt-dela.md)
- [Pripravljene začetne naloge](dokumentacija/zacetne-naloge.md)
- [GitHub Issues](https://github.com/TalonBot/EventRadar/issues)
- [GitHub Actions](https://github.com/TalonBot/EventRadar/actions)

## Lokalno preverjanje

Za trenutno preverjanje potrebujeva Python 3.12 brez dodatnih paketov. Iz korena repozitorija zaženeva:

```sh
python scripts/check_project.py
```

Preveriva zahtevane datoteke, vsebino Wordovega dokumenta, vključeno sliko mockupa in lokalne povezave v Markdownu. Enak ukaz izvaja workflow ob pushu, pull requestu ali ročnem zagonu. Flutter build in preverjanja uvoznika dodava ob njuni implementaciji.

Spremembe pripravljava na vsebinskih vejah, jih poveževa z nalogo ter jih pred združitvijo medsebojno pregledava. Gesel, dostopnih žetonov in ključa Supabase `service_role` ne vključujeva v repozitorij.
