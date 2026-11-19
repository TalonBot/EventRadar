# Načrt razvoja in razdelitev odgovornosti

Projekt razvijava Tilen Gabor (@TalonBot) in Jan Vid Gorenjak (@janvidgo). Razdelitev sva potrdila 19. novembra 2026. Odgovorni član vodi izvedbo, drugi član spremembo pregleda in sodeluje pri povezovanju.

## Odgovornosti

| Področje | Odgovorni član | Pregled |
| --- | --- | --- |
| Flutter, zasloni in navigacija | Tilen | Jan Vid |
| Seznam, iskanje, filtri in zemljevid | Tilen | Jan Vid |
| Supabase, model, migracije in RLS | Jan Vid | Tilen |
| Python uvoznik in podatkovni viri | Jan Vid | Tilen |
| Povezava prijave in priljubljenih v aplikaciji | Tilen | Jan Vid |
| CI in preverjanje podatkovne plasti | Jan Vid | Tilen |
| Dokumentacija in preverjanje oddaje | Tilen | Jan Vid |

Pri dokumentaciji, CI, pregledu sprememb in integraciji sodelujeva oba.

## Razvojne faze

| Faza | Rezultat in merilo zaključka | Odvisnost |
| --- | --- | --- |
| 1. Trenutni mejnik | Objavljena dokumentacija in struktura; dodeljeni Issues; člana in asistent z dostopom; uspešen CI do 20. 11. 2026 ob 08.00 | Potrditev računa asistenta in objava sprememb |
| 2. Osnova aplikacije | Flutter projekt, delujoča navigacija in prikaz testnih dogodkov | Faza 1 |
| 3. Podatkovna plast | Migracije, testni podatki, Auth in preverjena pravila RLS | Faza 1; povezava z aplikacijo po fazi 2 |
| 4. Prvi vir | Preverjeno dovoljenje in ponovljiv uvoz brez podvajanja testnega dogodka | Faza 3 in izbor vira |
| 5. Osnovne funkcionalnosti | Iskanje, filtri, podrobnosti, zemljevid in priljubljeni delujejo skupaj | Fazi 2 in 3; resnični podatki po fazi 4 |
| 6. Stabilizacija | Skupaj preveriva scenarije, napake, prazne rezultate in dokumentacijo; pripraviva demonstracijo | Faza 5 |

Datume naslednjih faz uskladiva z naslednjimi roki predmeta. Prednostno zaključiva osnovno pot od iskanja do shranjenega dogodka. Komentarje, vloge organizatorjev in ročno dodajanje dogodkov načrtujeva kot razširitev; pred implementacijo dopolniva model in pravila dostopa.

## Tehnološke odločitve

Ohranjava Flutter/Dart, Supabase/PostgreSQL/Auth, Python ter OpenStreetMap iz obstoječe zasnove. Za trenutni CI izbereva Python 3.12 in standardno knjižnico, zato preverjanje dokumentacije ne potrebuje dodatnih paketov ali skrivnosti.

Pred implementacijo skupaj potrdiva:

- ciljni platformi mobilne aplikacije in različico Flutter SDK;
- prvi dovoljeni podatkovni vir in način uporabe opisov ter slik;
- knjižnico za zemljevid in ponudnika ploščic z ustreznim pripisom;
- ponudnika približne IP-lokacije; ročna izbira mesta mora delovati tudi ob njegovi nedostopnosti.

## Organizacija dela

Prioritete označujeva kot **P0** (blokira trenutni mejnik), **P1** (osnova naslednje razvojne faze) in **P2** (nadaljnje funkcionalnosti). Vsaka začetna naloga ima enega odgovornega člana in merila zaključka v [seznamu nalog](zacetne-naloge.md).

Za razvoj uporabljava vsebinske veje in Pull Requests. V opis spremembe vključiva povezano nalogo in način preverjanja; drugi član pregleda spremembo pred združitvijo. Nalogo zaključiva, ko doseže merila in so spremembe vključene v repozitorij. Uspešen CI preveri tehnično celovitost datotek; vsebino in uporabniške scenarije pregledava tudi ročno.
