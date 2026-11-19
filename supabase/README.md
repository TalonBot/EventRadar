# Podatkovna plast

V tej mapi bova hranila različice sheme in migracije za Supabase PostgreSQL. Začetni model je že opisan v [prototipni dokumentaciji](../dokumentacija/EventRadar_Prototipna_Dokumentacija.docx).

Jan Vid prevzame tabele Event, Venue, Category, Source in Favorite ter povezavo s Supabase Auth. Pred uporabo iz odjemalca pripraviva pravila RLS: javno branje objavljenih dogodkov, dostop do priljubljenih samo njihovemu lastniku. Zapis uvoznika bo potekal v zaupanem strežniškem okolju.

Migracij in produkcijskega okolja v tem mejniku še ne vzpostavljava. Ključa `service_role` ne vključujeva v mobilno aplikacijo ali repozitorij.
