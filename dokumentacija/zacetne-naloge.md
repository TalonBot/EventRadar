# Začetne naloge

Spodaj določava opise, odgovornosti, prioritete in merila zaključka za začetne GitHub Issues. P0 označuje trenutni mejnik, P1 razvojno osnovo in P2 nadaljnje funkcionalnosti. Vseh osem nalog je objavljenih in dodeljenih odgovornemu članu.

| GitHub Issue | Odgovorni član | Prioriteta |
| --- | --- | --- |
| [#1 Dostop asistenta in pregled mejnika](https://github.com/TalonBot/EventRadar/issues/1) | Tilen | P0 |
| [#2 Osnova aplikacije Flutter in navigacija](https://github.com/TalonBot/EventRadar/issues/2) | Tilen | P1 |
| [#3 Shema Supabase in zaščita podatkov](https://github.com/TalonBot/EventRadar/issues/3) | Jan Vid | P1 |
| [#4 Dovoljeni podatkovni vir in prvi uvoz](https://github.com/TalonBot/EventRadar/issues/4) | Jan Vid | P1 |
| [#5 Seznam podrobnosti iskanje in filtri](https://github.com/TalonBot/EventRadar/issues/5) | Tilen | P1 |
| [#6 Prijava in priljubljeni](https://github.com/TalonBot/EventRadar/issues/6) | Tilen | P2 |
| [#7 Zemljevid in izbira mesta](https://github.com/TalonBot/EventRadar/issues/7) | Tilen | P2 |
| [#8 Integracijski pregled in razširitev CI](https://github.com/TalonBot/EventRadar/issues/8) | Jan Vid | P2 |

## 1 Dostop asistenta in pregled mejnika

**Odgovorni:** Tilen (@TalonBot). **Prioriteta:** P0. **Pregled:** Jan Vid.

Pred rokom preveriva objavljeno stanje repozitorija in dostop asistenta Tilna Hliša. Njegovega GitHub uporabniškega imena še nimava potrjenega.

Merila zaključka:

- [ ] Potrdiva GitHub račun asistenta in ga dodava; preveriva stanje povabila oziroma dostopa.
- [ ] Oba člana imava dostop za pisanje.
- [ ] Dokumentacija, README in struktura so objavljeni v glavni veji.
- [ ] Začetni Issues imajo opise, dodelitve in prioritete.
- [ ] GitHub Actions uspešno preveri zadnji commit glavne veje.
- [ ] Pregled opraviva do 20. 11. 2026 ob 08.00 (Europe/Ljubljana).

## 2 Osnova aplikacije Flutter in navigacija

**Odgovorni:** Tilen (@TalonBot). **Prioriteta:** P1. **Pregled:** Jan Vid. **Odvisnost:** trenutni mejnik.

V mapi app vzpostaviva Flutter projekt in osnovne zaslone po obstoječem mockupu. Pred začetkom potrdiva ciljni platformi in različico SDK.

Merila zaključka:

- [ ] Aplikacijo lahko zaženeva po navodilih v app/README.md.
- [ ] Delujejo uvodni zaslon, spodnja navigacija in povratek iz podrobnosti.
- [ ] Seznam prikazuje testne dogodke; prikazana sta tudi prazno stanje in napaka.
- [ ] CI vključuje formatiranje, analizo in smiselne teste začetne aplikacije.

## 3 Shema Supabase in zaščita podatkov

**Odgovorni:** Jan Vid (@janvidgo). **Prioriteta:** P1. **Pregled:** Tilen. **Odvisnost:** trenutni mejnik.

Za začetni model pripraviva ponovljive migracije in pravila RLS. Identiteto uporabnika poveževa s Supabase Auth.

Merila zaključka:

- [ ] Obstajajo tabele Event, Venue, Category, Source in Favorite z ustreznimi ključi.
- [ ] Favorite prepreči podvojeno shranjevanje istega dogodka za istega uporabnika.
- [ ] Neprijavljen uporabnik bere dogodke, priljubljene pa bere in spreminja samo njihov lastnik.
- [ ] Z dvema uporabnikoma preveriva, da ne moreta dostopati do priljubljenih drugega.
- [ ] Datumi ohranijo časovni pas; testni podatki in navodila omogočijo ponovitev postavitve.

## 4 Dovoljeni podatkovni vir in prvi uvoz

**Odgovorni:** Jan Vid (@janvidgo). **Prioriteta:** P1. **Pregled:** Tilen. **Odvisnost:** naloga 3 za zapis v bazo.

Izbereva prvi vir dogodkov ter pripraviva Python adapter, normalizacijo in prepoznavanje podvojitev.

Merila zaključka:

- [ ] Dokumentirava vir, pogoje uporabe in dovoljeno uporabo opisov ter slik.
- [ ] Adapter preveri obvezna polja in pravilno obravnava datum, mesto ter manjkajoče koordinate.
- [ ] Ponovljen uvoz istega vzorca ne ustvari podvojenega dogodka.
- [ ] Napako posameznega zapisa zabeleživa; veljavni zapisi se lahko obdelajo.
- [ ] Testi uporabijo lokalni vzorec; navodila opišejo zagon in potrebne okoljske spremenljivke.

## 5 Seznam podrobnosti iskanje in filtri

**Odgovorni:** Tilen (@TalonBot). **Prioriteta:** P1. **Pregled:** Jan Vid. **Odvisnost:** nalogi 2 in 3.

Aplikacijo poveževa s podatki Supabase ter izvedeva scenarij iskanja dogodka v drugem mestu.

Merila zaključka:

- [ ] Seznam prikazuje prihodnje dogodke za ročno izbrano mesto.
- [ ] Delujejo iskanje po nazivu ter filtra kategorije in datuma.
- [ ] Podrobnosti prikažejo datum, prizorišče in razpoložljivo povezavo do vstopnic.
- [ ] Preveriva nalaganje, prazne rezultate in napako povezave.
- [ ] Datum v aplikaciji pravilno upošteva lokalni čas dogodka.

## 6 Prijava in priljubljeni

**Odgovorni:** Tilen (@TalonBot). **Prioriteta:** P2. **Pregled:** Jan Vid. **Odvisnost:** nalogi 3 in 5.

Supabase Auth poveževa s prijavo, odjavo in shranjevanjem dogodkov. Brskanje ostane dostopno brez prijave.

Merila zaključka:

- [ ] Registracija, prijava in odjava imajo razumljiva uspešna in neuspešna stanja.
- [ ] Neprijavljenega uporabnika shranjevanje usmeri na prijavo in nato nazaj k dogodku.
- [ ] Prijavljeni uporabnik doda in odstrani dogodek ter vidi svoje priljubljene.
- [ ] Po odjavi aplikacija ne kaže zasebnih podatkov prejšnjega uporabnika.

## 7 Zemljevid in izbira mesta

**Odgovorni:** Tilen (@TalonBot). **Prioriteta:** P2. **Pregled:** Jan Vid. **Odvisnost:** naloga 5.

Dogodke s koordinatami prikaževa na zemljevidu. Izbereva knjižnico, ponudnika ploščic in način približne IP-lokacije.

Merila zaključka:

- [ ] Dokumentirava izbrano knjižnico, ponudnika in pogoje uporabe.
- [ ] Zemljevid ima zahtevan pripis; izbira oznake odpre pravi dogodek.
- [ ] Dogodek brez koordinat ostane v seznamu in ne povzroči napake zemljevida.
- [ ] Ročna izbira mesta deluje tudi brez IP-lokacije in GPS-dovoljenja.
- [ ] Filter oddaljenosti je na voljo le z veljavnimi koordinatami.

## 8 Integracijski pregled in razširitev CI

**Odgovorni:** Jan Vid (@janvidgo). **Prioriteta:** P2. **Pregled:** Tilen. **Odvisnost:** naloge 4, 5, 6 in 7.

Skupaj preveriva uporabniške scenarije in podatkovni tok ter razširiva CI glede na dejansko implementacijo.

Merila zaključka:

- [ ] Ponoviva scenarije iskanja, shranjevanja in osveževanja iz prototipne dokumentacije.
- [ ] CI preveri Flutter in Python kodo ter smiselne teste brez produkcijskih skrivnosti.
- [ ] Dokumentirava zagon, omejitve in odprte napake.
- [ ] Odpraviva napake, ki blokirajo osnovno pot od iskanja do priljubljenega dogodka.
