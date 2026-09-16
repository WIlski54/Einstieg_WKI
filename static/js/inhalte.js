// Inhalte des interaktiven Arbeitsblatts „Der Erste Weltkrieg (1914–1918)“
// Geschichte · Klasse 9 · Gesamtschule Meiderich (Sek I, Klassenunterricht)
// Sprache: kurze Sätze, einfache Wörter, Fakten unverändert.
// Aufgabennummern müssen zu ABSCHNITTE in config.py passen.

window.INHALTE = {
  titel: "Der Erste Weltkrieg (1914–1918)",

  // ─── Kartendaten (Längengrad/Breitengrad) ─────────────────────────────
  karten: {
    europa1914: {
      titel: "Europa 1914 – zwei Blöcke",
      legende: [["mm", "Mittelmächte / Dreibund"], ["en", "Entente"], ["neutral", "neutral"]],
      linien: [],   // Blöcke nur über Farbe der Punkte und Namen – Linien quer über die Karte waren verwirrend
      punkte: [
        { id: "berlin", lon: 13.4, lat: 52.5, label: "Deutsches Reich", bloc: "mm", icon: "🦅", titel: "Deutsches Reich (Berlin)", text: "Kaiserreich seit 1871. Wirtschaftlich stark, aber spät dran bei den Kolonien. Kaiser Wilhelm II. will einen „Platz an der Sonne“ und baut eine große Flotte. Verbündet mit Österreich-Ungarn (1879) und Italien (1882)." },
        { id: "wien", lon: 16.4, lat: 48.2, label: "Österreich-Ungarn", bloc: "mm", icon: "👑", titel: "Österreich-Ungarn (Wien)", text: "Ein Staat mit vielen Völkern. Serbische Nationalisten bedrohen den Zusammenhalt. 1908 nimmt sich Österreich-Ungarn Bosnien – mit der Hauptstadt Sarajevo." },
        { id: "rom", lon: 12.5, lat: 41.9, label: "Italien", bloc: "mm", icon: "🏛️", titel: "Italien (Rom)", text: "Gehört zum Dreibund, bleibt 1914 aber neutral. Der Dreibund war nur zur Verteidigung gedacht. 1915 kämpft Italien auf der Seite der Entente." },
        { id: "paris", lon: 2.35, lat: 48.85, label: "Frankreich", bloc: "en", icon: "🗼", titel: "Frankreich (Paris)", text: "Will Elsass-Lothringen zurück, das es 1871 verloren hat. Verbündet mit Russland (1894) und Großbritannien (1904). Große Kolonien in Afrika und Asien." },
        { id: "london", lon: -0.1, lat: 51.5, label: "Großbritannien", bloc: "en", icon: "⚓", titel: "Großbritannien (London)", text: "Größte See- und Kolonialmacht der Welt. Die neue deutsche Flotte gilt als Bedrohung. 1904 Bündnis mit Frankreich, 1907 mit Russland – das ist die Triple Entente." },
        { id: "petersburg", lon: 30.3, lat: 59.9, label: "Russland", bloc: "en", icon: "🐻", titel: "Russisches Reich (St. Petersburg)", text: "Riesiges Zarenreich mit vielen Bauern. Sieht sich als Beschützer aller Slawen und hilft deshalb Serbien. Seit 1894 mit Frankreich verbündet." },
        { id: "belgrad", lon: 20.5, lat: 44.8, label: "Serbien", bloc: "en", icon: "🔥", titel: "Serbien (Belgrad)", text: "Kleines Königreich, nach den Balkankriegen 1912/13 größer geworden. Serbische Nationalisten wollen alle Südslawen in einem Staat vereinen. Russland ist Serbiens Schutzmacht." },
        { id: "konstantinopel", lon: 29.0, lat: 41.0, label: "Osmanisches Reich", bloc: "mm", icon: "🌙", titel: "Osmanisches Reich (Konstantinopel)", text: "Verliert seit Jahrzehnten Gebiete auf dem Balkan. So wird der Balkan zum „Pulverfass“. Im November 1914 tritt das Reich auf der Seite der Mittelmächte ein." },
        { id: "bruessel", lon: 4.35, lat: 50.85, label: "Belgien", bloc: "neutral", icon: "🕊️", titel: "Belgien (Brüssel)", text: "Neutraler Staat, seit 1839 von den Großmächten geschützt. Der deutsche Kriegsplan führt durch Belgien nach Frankreich. Deshalb tritt Großbritannien 1914 in den Krieg ein." },
      ],
    },

    julikrise: {
      titel: "Die Julikrise 1914 – Orte der Entscheidung",
      legende: [["mm", "Mittelmächte"], ["en", "Entente"], ["neutral", "neutral"]],
      linien: [],
      punkte: [
        { id: "sarajevo", lon: 18.4, lat: 43.85, label: "1 Sarajevo", bloc: "mm", icon: "🎯", titel: "28. Juni 1914 – Sarajevo", text: "Gavrilo Princip erschießt den Thronfolger Franz Ferdinand und seine Frau Sophie. Sarajevo gehört seit 1908 zu Österreich-Ungarn." },
        { id: "berlin", lon: 13.4, lat: 52.5, label: "2 Berlin", bloc: "mm", icon: "📜", titel: "5./6. Juli 1914 – Berlin", text: "Kaiser Wilhelm II. verspricht Österreich-Ungarn volle Unterstützung – der „Blankoscheck“. Am 1. August erklärt Berlin Russland den Krieg, am 3. August Frankreich." },
        { id: "wien", lon: 16.4, lat: 48.2, label: "3 Wien", bloc: "mm", icon: "⏳", titel: "23. und 28. Juli 1914 – Wien", text: "Österreich-Ungarn stellt Serbien ein Ultimatum: 48 Stunden Zeit für harte Forderungen. Am 28. Juli erklärt es Serbien den Krieg – die erste Kriegserklärung." },
        { id: "belgrad", lon: 20.5, lat: 44.8, label: "4 Belgrad", bloc: "en", icon: "✉️", titel: "25. Juli 1914 – Belgrad", text: "Serbien nimmt fast alle Forderungen an. Nur österreichische Beamte im eigenen Land lehnt es ab. Wien bricht die Beziehungen ab." },
        { id: "petersburg", lon: 30.3, lat: 59.9, label: "5 St. Petersburg", bloc: "en", icon: "🪖", titel: "30. Juli 1914 – St. Petersburg", text: "Zar Nikolaus II. macht seine ganze Armee mobil, um Serbien zu helfen. Für Deutschland ist das der Grund, den Schlieffen-Plan zu starten." },
        { id: "paris", lon: 2.35, lat: 48.85, label: "6 Paris", bloc: "en", icon: "🇫🇷", titel: "1.–3. August 1914 – Paris", text: "Frankreich macht am 1. August mobil. Am 3. August erklärt Deutschland Frankreich den Krieg." },
        { id: "bruessel", lon: 4.35, lat: 50.85, label: "7 Brüssel", bloc: "neutral", icon: "🚧", titel: "4. August 1914 – Brüssel", text: "Deutsche Truppen marschieren in das neutrale Belgien ein. So wollen sie Frankreich von Norden angreifen. Belgien wehrt sich." },
        { id: "london", lon: -0.1, lat: 51.5, label: "8 London", bloc: "en", icon: "🇬🇧", titel: "4. August 1914 – London", text: "Wegen des Einmarschs in Belgien erklärt Großbritannien Deutschland den Krieg. Aus dem Streit auf dem Balkan ist ein Krieg in ganz Europa geworden." },
      ],
    },

    fronten: {
      titel: "Die Fronten 1914–1918",
      legende: [["mm", "Mittelmächte"], ["en", "Entente"], ["front", "Frontlinie"]],
      linien: [],
      fronten: [
        { name: "Westfront", punkte: [[2.7, 51.1], [2.9, 50.85], [2.8, 50.3], [3.0, 49.6], [4.0, 49.25], [5.4, 49.2], [5.6, 48.9], [6.6, 48.7], [7.5, 47.6]] },
        { name: "Ostfront", punkte: [[24.1, 57.2], [26.4, 55.8], [26.0, 53.8], [25.8, 52.0], [25.4, 50.5], [25.6, 49.2], [26.2, 48.2]] },
        { name: "Alpenfront", punkte: [[10.5, 46.5], [12.0, 46.6], [13.6, 46.2], [13.5, 45.8]] },
        { name: "Salonikifront", punkte: [[20.8, 41.0], [22.4, 41.2], [24.0, 41.3]] },
      ],
      punkte: [
        { id: "westfront", lon: 5.4, lat: 49.2, label: "Westfront", bloc: "front", icon: "🪖", titel: "Westfront – der Stellungskrieg", text: "Nach der Marneschlacht (September 1914) bewegt sich die Front kaum noch. Vier Jahre Schützengräben von der Nordsee bis zur Schweiz. Ypern 1915: Giftgas. Verdun und Somme 1916: riesige Verluste, erste Panzer." },
        { id: "ostfront", lon: 22.0, lat: 54.0, label: "Ostfront", bloc: "front", icon: "❄️", titel: "Ostfront – Bewegung im Osten", text: "Die Front ist viel länger und dünner besetzt. Deshalb bleibt sie beweglich. 1914 Sieg bei Tannenberg. Nach der Revolution 1917 steigt Russland aus: Frieden von Brest-Litowsk im März 1918." },
        { id: "alpen", lon: 13.6, lat: 46.0, label: "Alpen-/Isonzofront", bloc: "front", icon: "🏔️", titel: "Alpen- und Isonzofront", text: "Seit Mai 1915 kämpft Italien gegen Österreich-Ungarn – im Hochgebirge. Zwölf Schlachten am Fluss Isonzo. 1917 brechen die Mittelmächte bei Caporetto durch." },
        { id: "balkan", lon: 21.5, lat: 43.0, label: "Balkanfront", bloc: "front", icon: "⛰️", titel: "Balkanfront", text: "Serbien hält 1914 stand, wird aber Ende 1915 besetzt. Die Entente landet in Saloniki. Im September 1918 bricht die Front zusammen. Bulgarien gibt als Erster auf." },
        { id: "gallipoli", lon: 26.4, lat: 40.4, label: "Gallipoli", bloc: "front", icon: "🚢", titel: "Gallipoli / Dardanellen 1915", text: "1915 wollen Briten, Franzosen, Australier und Neuseeländer die Meerenge zum Schwarzen Meer öffnen. Das Osmanische Reich wehrt die Landung ab." },
        { id: "skagerrak", lon: 5.7, lat: 56.7, label: "Skagerrak", bloc: "front", icon: "⚓", titel: "Seekrieg – Skagerrakschlacht 1916", text: "Die einzige große Seeschlacht (31. Mai/1. Juni 1916) hat keinen Sieger. Die britische Blockade lässt Deutschland hungern: Steckrübenwinter 1916/17." },
        { id: "atlantik", lon: -7.5, lat: 48.5, label: "U-Boot-Krieg", bloc: "front", icon: "🌊", titel: "Uneingeschränkter U-Boot-Krieg", text: "Ab Februar 1917 versenken deutsche U-Boote ohne Warnung auch neutrale Schiffe. Darum treten die USA im April 1917 in den Krieg ein." },
      ],
    },

    kriegsende: {
      titel: "Orte des Kriegsendes 1918",
      legende: [["mm", "Mittelmächte"], ["en", "Entente"], ["ort", "Ereignisort"]],
      linien: [],
      punkte: [
        { id: "amiens", lon: 2.3, lat: 49.9, label: "Amiens", bloc: "ort", icon: "💥", titel: "8. August 1918 – Amiens", text: "Die Alliierten durchbrechen mit Panzern die deutschen Linien. General Ludendorff nennt es den „schwarzen Tag des deutschen Heeres“." },
        { id: "spa", lon: 5.9, lat: 50.5, label: "Spa", bloc: "ort", icon: "🏰", titel: "September–November 1918 – Spa", text: "Im Hauptquartier verlangen Hindenburg und Ludendorff am 29. September einen Waffenstillstand. Von hier flieht Kaiser Wilhelm II. am 10. November in die Niederlande." },
        { id: "kiel", lon: 10.1, lat: 54.3, label: "Kiel", bloc: "ort", icon: "⚓", titel: "3./4. November 1918 – Kiel", text: "Matrosen weigern sich, noch einmal gegen die Briten auszulaufen. Arbeiter und Soldaten übernehmen die Stadt. Die Novemberrevolution beginnt." },
        { id: "berlin", lon: 13.4, lat: 52.5, label: "Berlin", bloc: "ort", icon: "🏛️", titel: "9. November 1918 – Berlin", text: "Der Kaiser dankt ab. Philipp Scheidemann ruft die Republik aus. Friedrich Ebert übernimmt die Regierung." },
        { id: "compiegne", lon: 2.8, lat: 49.4, label: "Compiègne", bloc: "ort", icon: "🚂", titel: "11. November 1918 – Compiègne", text: "In einem Eisenbahnwagen unterschreibt Matthias Erzberger den Waffenstillstand. Um 11 Uhr schweigen die Waffen." },
        { id: "brest", lon: 23.7, lat: 52.1, label: "Brest-Litowsk", bloc: "ort", icon: "📜", titel: "3. März 1918 – Brest-Litowsk", text: "Sowjetrussland schließt einen harten Frieden und verliert große Gebiete. Deutschland kann nun Truppen nach Westen schicken." },
        { id: "wien", lon: 16.4, lat: 48.2, label: "Wien", bloc: "ort", icon: "🧩", titel: "Oktober/November 1918 – Wien", text: "Die Völker erklären sich unabhängig, Österreich-Ungarn zerfällt. Am 3. November Waffenstillstand, am 11. November gibt Kaiser Karl I. die Macht ab." },
      ],
    },

    europa1920: {
      titel: "Europa nach den Friedensverträgen",
      legende: [["neu", "neuer Staat"], ["verlust", "Verlust Deutschlands"], ["rest", "Rest eines alten Reiches"]],
      linien: [],
      punkte: [
        { id: "warschau", lon: 21.0, lat: 52.2, label: "Polen", bloc: "neu", icon: "🆕", titel: "Polen", text: "Nach 123 Jahren Teilung wieder ein eigener Staat. Bekommt Posen und Westpreußen: den „Polnischen Korridor“ zur Ostsee. Ostpreußen ist nun vom Reich getrennt." },
        { id: "prag", lon: 14.4, lat: 50.1, label: "Tschechoslowakei", bloc: "neu", icon: "🆕", titel: "Tschechoslowakei", text: "Neuer Staat aus Böhmen, Mähren und der Slowakei. Viele Menschen dort sprechen Deutsch (Sudetenland)." },
        { id: "belgrad", lon: 20.5, lat: 44.8, label: "Jugoslawien", bloc: "neu", icon: "🆕", titel: "Königreich der Serben, Kroaten und Slowenen", text: "Ab 1929 „Jugoslawien“. Vereint Serbien mit südslawischen Gebieten aus Österreich-Ungarn – das Ziel der serbischen Nationalisten von 1914." },
        { id: "wien", lon: 16.4, lat: 48.2, label: "Österreich", bloc: "rest", icon: "🧩", titel: "Österreich", text: "Kleiner Rest der alten Monarchie (Vertrag von Saint-Germain 1919). Ein Anschluss an Deutschland ist verboten." },
        { id: "budapest", lon: 19.0, lat: 47.5, label: "Ungarn", bloc: "rest", icon: "🧩", titel: "Ungarn", text: "Verliert im Vertrag von Trianon (1920) rund zwei Drittel seines Gebiets." },
        { id: "riga", lon: 24.1, lat: 56.95, label: "Baltische Staaten", bloc: "neu", icon: "🆕", titel: "Estland, Lettland, Litauen", text: "Die drei Staaten lösen sich von Russland und werden 1918 unabhängig." },
        { id: "helsinki", lon: 24.9, lat: 60.2, label: "Finnland", bloc: "neu", icon: "🆕", titel: "Finnland", text: "Erklärt sich im Dezember 1917 unabhängig von Russland." },
        { id: "strassburg", lon: 7.75, lat: 48.6, label: "Elsass-Lothringen", bloc: "verlust", icon: "↩️", titel: "Elsass-Lothringen", text: "Geht zurück an Frankreich. Deutschland verliert damit viel Eisenerz." },
        { id: "danzig", lon: 18.65, lat: 54.35, label: "Danzig", bloc: "verlust", icon: "↩️", titel: "Freie Stadt Danzig", text: "Wird vom Völkerbund verwaltet, damit Polen einen Hafen hat. Das Memelland kommt 1923 zu Litauen." },
        { id: "saar", lon: 7.0, lat: 49.2, label: "Saargebiet", bloc: "verlust", icon: "↩️", titel: "Saargebiet", text: "15 Jahre vom Völkerbund verwaltet, die Kohle geht an Frankreich. 1935 stimmt die Bevölkerung für Deutschland." },
        { id: "moskau", lon: 37.6, lat: 55.75, label: "Sowjetrussland", bloc: "rest", icon: "☭", titel: "Sowjetrussland / Sowjetunion", text: "Nach der Oktoberrevolution 1917 regieren die Bolschewiki. Bis 1921 Bürgerkrieg. 1922 Gründung der Sowjetunion." },
        { id: "ankara", lon: 32.9, lat: 39.9, label: "Türkei", bloc: "rest", icon: "🌙", titel: "Türkei", text: "Aus dem Osmanischen Reich wird 1923 die Republik Türkei. Die arabischen Gebiete verwalten nun Großbritannien und Frankreich." },
      ],
    },
  },

  // ─── Reiter mit Aufgaben ──────────────────────────────────────────────
  tabs: [
    // ════════════════════════════════ URSACHEN ═════════════════════════
    {
      key: "ursachen", label: "Ursachen", icon: "🧭", kurz: "U",
      intro: {
        eyebrow: "Lesestrecke M1", titel: "Warum war Europa 1914 ein „Pulverfass“?",
        begriffe: ["Imperialismus", "Nationalismus", "Militarismus", "Wettrüsten", "Bündnissystem", "Dreibund", "Triple Entente", "Schlieffen-Plan", "Pulverfass Balkan"],
      },
      aufgaben: [
        {
          nr: 1, typ: "mc", eyebrow: "Grundwissen", titel: "Ursachen erkennen",
          niveaus: {
            A: { frage: "Was war eine Ursache des Ersten Weltkriegs?", optionen: [
              { t: "Das Wettrüsten der Großmächte", ok: true },
              { t: "Die Erfindung des Autos", ok: false },
              { t: "Die Gründung der Vereinten Nationen", ok: false },
            ] },
            B: { frage: "Was bedeutet „Bündnissystem“ im Jahr 1914?", optionen: [
              { t: "Europa war in zwei Blöcke geteilt, die sich Hilfe versprochen hatten", ok: true },
              { t: "Alle Staaten Europas hatten einen gemeinsamen Vertrag", ok: false },
              { t: "Deutschland hatte 1914 keine Verbündeten", ok: false },
              { t: "Die Bündnisse verhinderten den Krieg", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen über den Imperialismus stimmen?", optionen: [
              { t: "Der Streit um Kolonien führte zu Krisen, zum Beispiel in Marokko 1905 und 1911", ok: true },
              { t: "Deutschland kam spät und wollte auch Kolonien – Streit mit Großbritannien und Frankreich", ok: true },
              { t: "Die Kolonien wurden 1914 friedlich verteilt", ok: false },
              { t: "Der Imperialismus betraf nur Staaten außerhalb Europas", ok: false },
            ] },
          },
        },
        {
          nr: 2, typ: "luecke", eyebrow: "Fachbegriffe", titel: "Vier Ursachen – vier Begriffe",
          niveaus: {
            A: { modus: "chips", ablenker: ["Frieden", "Demokratie"], text: "Der Wettlauf um Kolonien heißt [Imperialismus]. Wer das eigene Volk für besser hält, ist ein Anhänger des [Nationalismus]. Das hohe Ansehen des Militärs nennt man [Militarismus]. Feste [Bündnisse] machten aus einem Streit einen Krieg zwischen zwei Blöcken." },
            B: { modus: "input", text: "Frankreich wollte das Gebiet [Elsass-Lothringen|Elsaß-Lothringen] zurück. Deutschland und Großbritannien lieferten sich ein [Flottenwettrüsten|Wettrüsten]. Der Balkan galt als [Pulverfass] Europas. Der [Schlieffen-Plan|Schlieffenplan] sah vor: erst Frankreich schnell besiegen, dann Russland." },
            C: { modus: "input", text: "Österreich-Ungarn war ein [Vielvölkerstaat]. Der serbische [Nationalismus] bedrohte seinen Zusammenhalt. Russland half Serbien als Schutzmacht der [Slawen|slawischen Völker|Südslawen]. Deutschland hatte Österreich-Ungarn im [Zweibund|Dreibund] Hilfe versprochen. Frankreich und Russland waren seit [1894|1892] verbündet. 1907 kam Großbritannien dazu: die [Triple Entente|Entente]. So konnte ein Streit auf dem Balkan ganz Europa in den Krieg ziehen." },
          },
        },
        {
          nr: 3, typ: "zuordnung", eyebrow: "Begriff und Beispiel", titel: "Welches Beispiel passt?",
          niveaus: {
            A: { links: "Ursache", rechts: "Beispiel", paare: [
              ["Imperialismus", "Streit um Kolonien in Marokko"],
              ["Militarismus", "Flottenwettrüsten zwischen Deutschland und Großbritannien"],
              ["Nationalismus", "Frankreich will Elsass-Lothringen zurück"],
            ] },
            B: { links: "Ursache", rechts: "Beispiel", paare: [
              ["Imperialismus", "Streit um Kolonien in Marokko"],
              ["Militarismus", "Flottenwettrüsten zwischen Deutschland und Großbritannien"],
              ["Nationalismus", "Frankreich will Elsass-Lothringen zurück"],
              ["Bündnissystem", "Dreibund gegen Triple Entente"],
            ] },
            C: { links: "Begriff", rechts: "Erklärung", paare: [
              ["Imperialismus", "Wettlauf der Großmächte um Kolonien und Macht in der Welt"],
              ["Militarismus", "Das Militär hat hohes Ansehen, Krieg gilt als normal"],
              ["Nationalismus", "Das eigene Volk gilt als besser als andere"],
              ["Bündnissystem", "Zwei Blöcke versprechen sich Hilfe – jeder Streit wird gefährlich"],
              ["Schlieffen-Plan", "Deutscher Kriegsplan: erst Frankreich, dann Russland"],
            ] },
          },
        },
        {
          nr: 4, typ: "sortierung", eyebrow: "Zeitliche Ordnung", titel: "So entstanden die Bündnisse",
          niveaus: {
            A: { hinweis: "Bringe die Bündnisse in die richtige Reihenfolge. Die Jahreszahlen helfen dir.", items: [
              "1879 · Zweibund: Deutschland und Österreich-Ungarn",
              "1882 · Dreibund: Italien kommt dazu",
              "1907 · Triple Entente: Frankreich, Russland und Großbritannien",
            ] },
            B: { hinweis: "Ordne ohne Jahreszahlen. Was kam zuerst?", items: [
              "Zweibund: Deutschland und Österreich-Ungarn",
              "Dreibund: Italien kommt dazu",
              "Bündnis Frankreich–Russland",
              "Bündnis Großbritannien–Frankreich (Entente cordiale)",
              "Triple Entente: Großbritannien und Russland einigen sich",
            ] },
            C: { hinweis: "Sieben Schritte bis zu den zwei Blöcken – ohne Jahreszahlen.", items: [
              "Deutsche Reichsgründung, Frankreich verliert Elsass-Lothringen",
              "Zweibund: Deutschland und Österreich-Ungarn",
              "Dreibund: Italien kommt dazu",
              "Deutschland verlängert den Vertrag mit Russland nicht",
              "Bündnis Frankreich–Russland",
              "Bündnis Großbritannien–Frankreich (Entente cordiale)",
              "Triple Entente: Großbritannien und Russland einigen sich",
            ] },
          },
        },
        {
          nr: 5, typ: "diagramm", eyebrow: "Diagramm lesen", titel: "Wettrüsten in Zahlen",
          chart: {
            typ: "bar", einheit: "Mio. £", yTitel: "Ausgaben für das Militär in Millionen Pfund",
            quelle: "Gerundete Werte nach P. Kennedy (1987). Tippe auf einen Balken.",
            labels: ["Deutsches Reich", "Großbritannien", "Frankreich", "Russland", "Österreich-Ungarn"],
            datasets: [
              { label: "1890", data: [29, 31, 37, 29, 13], farbe: "#9fb8cc" },
              { label: "1910", data: [64, 68, 52, 63, 17], farbe: "#4d8fc2" },
              { label: "1914", data: [111, 77, 57, 88, 36], farbe: "#AD007C" },
            ],
          },
          niveaus: {
            A: { frage: "Welches Land gab 1914 am meisten Geld für das Militär aus?", optionen: [
              { t: "Das Deutsche Reich", ok: true }, { t: "Frankreich", ok: false }, { t: "Österreich-Ungarn", ok: false },
            ] },
            B: { frage: "Wie veränderten sich die deutschen Ausgaben von 1890 bis 1914?", optionen: [
              { t: "Sie wurden fast viermal so hoch", ok: true }, { t: "Sie wurden etwa doppelt so hoch", ok: false },
              { t: "Sie blieben gleich", ok: false }, { t: "Sie wurden halbiert", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Schlüsse erlaubt das Diagramm?", optionen: [
              { t: "Alle fünf Großmächte gaben 1914 deutlich mehr aus als 1910 – ein Zeichen für das Wettrüsten", ok: true },
              { t: "Deutschland steigerte am stärksten und lag 1914 vorn", ok: true },
              { t: "Großbritannien rüstete nach 1910 ab", ok: false },
              { t: "Das Diagramm beweist, dass nur Deutschland Krieg wollte", ok: false },
            ] },
          },
        },
        {
          nr: 6, typ: "karte", eyebrow: "Karte erkunden", titel: "Europa 1914 – die Blöcke", karte: "europa1914",
          benoetigt: { A: 3, B: 6, C: 9 },
          niveaus: {
            A: { frage: "Welche Staaten bildeten die Triple Entente?", optionen: [
              { t: "Frankreich, Russland und Großbritannien", ok: true }, { t: "Deutschland, Österreich-Ungarn und Italien", ok: false }, { t: "Serbien, Belgien und Italien", ok: false },
            ] },
            B: { frage: "Warum blieb Italien 1914 neutral?", optionen: [
              { t: "Der Dreibund galt nur zur Verteidigung – und Italien hatte eigene Ziele", ok: true },
              { t: "Italien war nie im Dreibund", ok: false },
              { t: "Italien hatte keine Armee", ok: false },
              { t: "Großbritannien hatte Italien den Krieg erklärt", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zur Lage Deutschlands stimmen?", optionen: [
              { t: "Deutschland lag zwischen Frankreich und Russland – Angst vor einem Krieg an zwei Fronten", ok: true },
              { t: "Der Schlieffen-Plan war die Antwort: erst schnell im Westen siegen, dann im Osten", ok: true },
              { t: "Deutschland hatte mehr Verbündete als die Entente", ok: false },
              { t: "Großbritannien war 1914 mit Deutschland verbündet", ok: false },
            ] },
          },
        },
        {
          nr: 7, typ: "freitext", eyebrow: "Erklären", titel: "Pulverfass Europa",
          kontext: "Klasse 9 Geschichte, Abschnitt Ursachen. Begriffe: Imperialismus, Nationalismus, Militarismus, Wettrüsten, Bündnissystem, Balkan.",
          niveaus: {
            A: { aufgabe: "Erkläre in 3 Sätzen: Warum nennt man Europa 1914 ein „Pulverfass“?", starter: ["Ein Grund für den Krieg war …", "Außerdem …", "Die Bündnisse führten dazu, dass …"], begriffe: ["Nationalismus", "Wettrüsten", "Bündnisse"], min: 60 },
            B: { aufgabe: "Erkläre: Warum konnte ein Streit auf dem Balkan zu einem Krieg in ganz Europa werden?", begriffe: ["Bündnissystem", "Nationalismus", "Großmacht", "Schutzmacht"], min: 100 },
            C: { aufgabe: "Welche Ursache war deiner Meinung nach die wichtigste? Begründe mit Beispielen. Vergleiche mindestens zwei Ursachen.", begriffe: ["Imperialismus", "Nationalismus", "Militarismus", "Bündnissystem", "Marokkokrise", "Elsass-Lothringen"], min: 150 },
          },
        },
        {
          nr: 8, typ: "notizen", eyebrow: "Recherche", titel: "Meine Stichpunkte: Ursachen", abschnitt: "ursachen",
          hinweis: "Schreibe die wichtigsten Ursachen als Stichpunkte auf. Nutze die Lesestrecke und eine eigene Quelle.",
          kiFrage: "Prüfe diese Stichpunkte zu den Ursachen des Ersten Weltkriegs: Stimmen sie? Fehlt etwas Wichtiges (Imperialismus, Nationalismus, Militarismus, Bündnissystem)?",
        },
        {
          nr: 9, typ: "zeichnen", eyebrow: "Zeichnen", titel: "Das Bündnissystem als Skizze", geraet: "buendnis",
          niveaus: {
            A: { aufgabe: "Zeichne zwei große Kästen: einen für den Dreibund, einen für die Triple Entente. Schreibe die Länder hinein (Textwerkzeug). Verbinde die Verbündeten mit Linien.", elemente: ["Kasten Dreibund mit Deutschland, Österreich-Ungarn, Italien", "Kasten Triple Entente mit Frankreich, Russland, Großbritannien", "Linien zwischen den Verbündeten", "Beschriftungen"], hinweis: "Tipp: Erst die zwei Kästen, dann die sechs Namen, zum Schluss die Linien." },
            B: { aufgabe: "Zeichne das Bündnissystem von 1914 als Netz: Länder als Kästen, Bündnisse als Linien. Setze Serbien und Belgien an den Rand. Markiere mit einem Pfeil, wo die Julikrise begann.", elemente: ["sechs Großmächte als Kästen", "Bündnislinien für Dreibund und Entente", "Serbien und Belgien", "Pfeil bei Sarajevo/Österreich-Ungarn"], hinweis: "Nutze zwei Farben für die zwei Blöcke." },
            C: { aufgabe: "Zeichne die Kettenreaktion vom Attentat bis zur Kriegserklärung Großbritanniens: Länder als Kästen, jede Reaktion als Pfeil mit Datum. Ergänze den Schlieffen-Plan als Pfeil durch Belgien.", elemente: ["Kästen für Serbien, Österreich-Ungarn, Deutschland, Russland, Frankreich, Belgien, Großbritannien", "nummerierte Pfeile in der Reihenfolge der Julikrise", "Blankoscheck als Pfeil Berlin → Wien", "Schlieffen-Plan als Pfeil durch Belgien"], hinweis: "Die Reihenfolge der Pfeile ist das Wichtigste." },
          },
        },
      ],
    },

    // ════════════════════════════════ AUSLÖSER ═════════════════════════
    {
      key: "ausloeser", label: "Auslöser", icon: "🎯", kurz: "A",
      intro: {
        eyebrow: "Lesestrecke M2", titel: "Das Attentat von Sarajevo und die Julikrise",
        begriffe: ["Attentat von Sarajevo", "Gavrilo Princip", "Franz Ferdinand", "Blankoscheck", "Ultimatum", "Julikrise", "Mobilmachung", "Neutralität Belgiens", "Auslöser und Ursache"],
      },
      aufgaben: [
        {
          nr: 10, typ: "sortierung", eyebrow: "Kettenreaktion", titel: "Die Julikrise in der richtigen Reihenfolge",
          niveaus: {
            A: { hinweis: "Drei Schritte – die Daten helfen dir.", items: [
              "28. Juni · Attentat von Sarajevo",
              "28. Juli · Österreich-Ungarn erklärt Serbien den Krieg",
              "1. August · Deutschland erklärt Russland den Krieg",
            ] },
            B: { hinweis: "Fünf Schritte ohne Datum.", items: [
              "Attentat von Sarajevo",
              "Deutschland gibt Österreich-Ungarn den „Blankoscheck“",
              "Österreich-Ungarn stellt Serbien ein Ultimatum",
              "Österreich-Ungarn erklärt Serbien den Krieg",
              "Deutschland erklärt Russland den Krieg",
            ] },
            C: { hinweis: "Sieben Schritte ohne Datum – vom Attentat bis zum Weltkrieg.", items: [
              "Attentat von Sarajevo",
              "Deutschland gibt Österreich-Ungarn den „Blankoscheck“",
              "Österreich-Ungarn stellt Serbien ein Ultimatum",
              "Österreich-Ungarn erklärt Serbien den Krieg",
              "Russland macht seine Armee mobil",
              "Deutschland erklärt Russland den Krieg",
              "Deutschland erklärt Frankreich den Krieg und marschiert in Belgien ein – Großbritannien tritt ein",
            ] },
          },
        },
        {
          nr: 11, typ: "mc", eyebrow: "Grundwissen", titel: "Das Attentat von Sarajevo",
          niveaus: {
            A: { frage: "Wer wurde am 28. Juni 1914 in Sarajevo erschossen?", optionen: [
              { t: "Der Thronfolger Franz Ferdinand und seine Frau Sophie", ok: true },
              { t: "Kaiser Wilhelm II.", ok: false },
              { t: "Der König von Serbien", ok: false },
            ] },
            B: { frage: "Warum gab Österreich-Ungarn Serbien die Schuld?", optionen: [
              { t: "Der Täter Gavrilo Princip war serbischer Nationalist und hatte Helfer aus Serbien", ok: true },
              { t: "Serbien hatte vorher den Krieg erklärt", ok: false },
              { t: "Der König von Serbien hatte das Attentat öffentlich befohlen", ok: false },
              { t: "Serbische Truppen besetzten Sarajevo", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zum „Blankoscheck“ stimmen?", optionen: [
              { t: "Deutschland versprach Österreich-Ungarn volle Unterstützung – egal, wie es gegen Serbien vorging", ok: true },
              { t: "Das Versprechen machte Österreich-Ungarn mutiger und den Krieg wahrscheinlicher", ok: true },
              { t: "Der Blankoscheck war Geld für Serbien", ok: false },
              { t: "Großbritannien gab Serbien den Blankoscheck", ok: false },
            ] },
          },
        },
        {
          nr: 12, typ: "luecke", eyebrow: "Fachbegriffe", titel: "Vom Attentat zum Krieg",
          niveaus: {
            A: { modus: "chips", ablenker: ["Paris", "Frieden"], text: "Am 28. Juni 1914 wurde Franz Ferdinand in [Sarajevo] ermordet. Österreich-Ungarn gab [Serbien] die Schuld und stellte ein [Ultimatum]. Wegen der [Bündnisse] wurde aus dem Streit schnell ein Krieg in Europa." },
            B: { modus: "input", text: "Der Täter hieß Gavrilo [Princip]. Deutschland gab Österreich-Ungarn den [Blankoscheck]. Am [28]. Juli 1914 erklärte Österreich-Ungarn Serbien den Krieg. Russland antwortete mit der [Mobilmachung|Generalmobilmachung]. Der Einmarsch in [Belgien] brachte Großbritannien in den Krieg." },
            C: { modus: "input", text: "Das Attentat war der [Auslöser], nicht die [Ursache] des Krieges. Die Wochen vom 28. Juni bis 4. August 1914 heißen [Julikrise]. Russland sah sich als [Schutzmacht] Serbiens. Wegen des [Schlieffen-Plans|Schlieffenplans|Schlieffen-Plan|Schlieffenplan] griff Deutschland zuerst Frankreich an. Der Bruch der belgischen [Neutralität] war für Großbritannien der Kriegsgrund." },
          },
        },
        {
          nr: 13, typ: "zuordnung", eyebrow: "Wer tat was?", titel: "Die Akteure der Julikrise",
          niveaus: {
            A: { links: "Wer", rechts: "Was", paare: [
              ["Gavrilo Princip", "Erschießt den Thronfolger in Sarajevo"],
              ["Österreich-Ungarn", "Stellt Serbien ein Ultimatum"],
              ["Deutschland", "Erklärt Russland und Frankreich den Krieg"],
            ] },
            B: { links: "Wer", rechts: "Was", paare: [
              ["Gavrilo Princip", "Erschießt den Thronfolger in Sarajevo"],
              ["Österreich-Ungarn", "Stellt Serbien ein Ultimatum"],
              ["Russland", "Macht seine Armee mobil"],
              ["Deutschland", "Erklärt Russland und Frankreich den Krieg"],
            ] },
            C: { links: "Wer", rechts: "Was", paare: [
              ["Deutschland", "Gibt den Blankoscheck, erklärt später Russland und Frankreich den Krieg"],
              ["Österreich-Ungarn", "Stellt das Ultimatum und erklärt Serbien den Krieg"],
              ["Serbien", "Nimmt fast alles an, lehnt aber einen Punkt ab"],
              ["Russland", "Macht als Schutzmacht Serbiens mobil"],
              ["Großbritannien", "Erklärt Deutschland nach dem Einmarsch in Belgien den Krieg"],
            ] },
          },
        },
        {
          nr: 14, typ: "diagramm", eyebrow: "Diagramm lesen", titel: "Das Tempo der Krise",
          chart: {
            typ: "bar", horizontal: true, einheit: "Tage", yTitel: "Tage nach dem Attentat (28. Juni 1914)",
            quelle: "Abstand der Ereignisse zum Attentat. Tippe auf einen Balken.",
            labels: ["Blankoscheck (5. Juli)", "Ultimatum an Serbien (23. Juli)", "Antwort Serbiens (25. Juli)", "Kriegserklärung an Serbien (28. Juli)", "Russland macht mobil (30. Juli)", "Kriegserklärung an Russland (1. Aug.)", "Kriegserklärung an Frankreich (3. Aug.)", "Einmarsch in Belgien, GB tritt ein (4. Aug.)"],
            datasets: [{ label: "Tage nach dem Attentat", data: [7, 25, 27, 30, 32, 34, 36, 37], farbe: "#006AB3" }],
          },
          niveaus: {
            A: { frage: "Wie viele Tage lagen zwischen dem Attentat und der Kriegserklärung an Serbien?", optionen: [
              { t: "Etwa 30 Tage", ok: true }, { t: "Etwa 7 Tage", ok: false }, { t: "Etwa 100 Tage", ok: false },
            ] },
            B: { frage: "Was zeigt das Diagramm über das Tempo?", optionen: [
              { t: "Fast vier Wochen passierte wenig, dann ging in einer Woche alles ganz schnell", ok: true },
              { t: "Alles lief gleichmäßig ab", ok: false },
              { t: "Das meiste passierte in der ersten Woche", ok: false },
              { t: "Bis zum Krieg vergingen mehrere Monate", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Deutungen passen?", optionen: [
              { t: "Nach dem Ultimatum blieb kaum Zeit für Verhandlungen – Mobilmachung und Bündnisse gaben das Tempo vor", ok: true },
              { t: "Die lange Pause bis zum 23. Juli zeigt: Der Krieg war nicht sofort unvermeidbar", ok: true },
              { t: "Das Diagramm beweist, dass Serbien den Krieg begonnen hat", ok: false },
              { t: "Das Diagramm zeigt die Zahl der Soldaten", ok: false },
            ] },
          },
        },
        {
          nr: 15, typ: "karte", eyebrow: "Karte erkunden", titel: "Julikrise – die Orte", karte: "julikrise",
          benoetigt: { A: 3, B: 6, C: 8 },
          niveaus: {
            A: { frage: "In welcher Stadt war das Attentat?", optionen: [
              { t: "Sarajevo", ok: true }, { t: "Wien", ok: false }, { t: "Belgrad", ok: false },
            ] },
            B: { frage: "Warum sah Österreich-Ungarn das Attentat als Angriff auf sich selbst?", optionen: [
              { t: "Sarajevo lag in Bosnien, das seit 1908 zu Österreich-Ungarn gehörte", ok: true },
              { t: "Sarajevo war die Hauptstadt Serbiens", ok: false },
              { t: "Sarajevo gehörte zu Deutschland", ok: false },
              { t: "Das Attentat war in Wien", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zeigen die Kettenreaktion?", optionen: [
              { t: "Jede Entscheidung in einer Hauptstadt löste die nächste aus: Wien → Belgrad → St. Petersburg → Berlin → Paris → London", ok: true },
              { t: "Deutschland griff wegen des Schlieffen-Plans Frankreich und Belgien an, obwohl der Streit auf dem Balkan begann", ok: true },
              { t: "Alle Hauptstädte entschieden gleichzeitig", ok: false },
              { t: "Großbritannien erklärte als erstes Land den Krieg", ok: false },
            ] },
          },
        },
        {
          nr: 16, typ: "freitext", eyebrow: "Erklären", titel: "Funke oder Pulverfass?",
          kontext: "Klasse 9 Geschichte, Abschnitt Auslöser. Begriffe: Auslöser, Ursache, Attentat von Sarajevo, Julikrise, Blankoscheck, Bündnissystem, Kettenreaktion.",
          niveaus: {
            A: { aufgabe: "Erkläre mit eigenen Worten: Was ist der Unterschied zwischen Auslöser und Ursache? Nutze das Bild vom Funken und vom Pulverfass.", starter: ["Der Auslöser war …", "Die Ursachen dagegen …", "Man kann sagen: …"], begriffe: ["Auslöser", "Ursache", "Attentat", "Bündnisse"], min: 60 },
            B: { aufgabe: "Erkläre: Warum war das Attentat von Sarajevo nur der Auslöser und nicht die Ursache des Krieges?", begriffe: ["Julikrise", "Bündnissystem", "Kettenreaktion", "Blankoscheck"], min: 100 },
            C: { aufgabe: "Hätte man den Krieg im Juli 1914 noch verhindern können? Nenne zwei Momente, in denen Politiker anders hätten entscheiden können. Beurteile, wie wichtig diese Momente waren.", begriffe: ["Blankoscheck", "Ultimatum", "Mobilmachung", "Schlieffen-Plan"], min: 150 },
          },
        },
        {
          nr: 17, typ: "notizen", eyebrow: "Recherche", titel: "Meine Stichpunkte: Auslöser", abschnitt: "ausloeser",
          hinweis: "Schreibe die Schritte der Julikrise mit Datum auf – in der richtigen Reihenfolge. Vergiss die Quelle nicht.",
          kiFrage: "Prüfe diese Stichpunkte zum Auslöser des Ersten Weltkriegs (Attentat von Sarajevo, Julikrise): Stimmen Daten und Reihenfolge?",
        },
      ],
    },

    // ════════════════════════════════ VERLAUF ══════════════════════════
    {
      key: "verlauf", label: "Verlauf", icon: "🪖", kurz: "V",
      intro: {
        eyebrow: "Lesestrecke M3", titel: "Vom Bewegungskrieg zum Stellungskrieg",
        begriffe: ["Schlieffen-Plan", "Marneschlacht", "Stellungskrieg", "Zweifrontenkrieg", "Materialschlacht", "Verdun", "Somme", "Giftgas", "U-Boot-Krieg", "Kriegseintritt der USA", "totaler Krieg", "Heimatfront"],
      },
      aufgaben: [
        {
          nr: 18, typ: "mc", eyebrow: "Grundwissen", titel: "Bewegungskrieg und Stellungskrieg",
          niveaus: {
            A: { frage: "Was ist ein Stellungskrieg?", optionen: [
              { t: "Die Front bewegt sich kaum. Die Soldaten liegen monatelang in Schützengräben", ok: true },
              { t: "Ein Krieg nur auf See", ok: false },
              { t: "Ein Krieg, bei dem sich die Armeen schnell bewegen", ok: false },
            ] },
            B: { frage: "Warum scheiterte der Schlieffen-Plan 1914?", optionen: [
              { t: "In der Marneschlacht wurde der deutsche Angriff vor Paris gestoppt", ok: true },
              { t: "Russland griff Deutschland nicht an", ok: false },
              { t: "Frankreich gab sofort auf", ok: false },
              { t: "Der Plan sah keinen Angriff auf Frankreich vor", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zur „Materialschlacht“ stimmen?", optionen: [
              { t: "Bei Verdun und an der Somme starben 1916 Hunderttausende – die Front bewegte sich kaum", ok: true },
              { t: "Riesige Mengen an Geschützen, Maschinengewehren und Munition sollten den Gegner zermürben", ok: true },
              { t: "Die Materialschlachten brachten 1916 den Durchbruch im Westen", ok: false },
              { t: "„Materialschlacht“ heißt: Es ging nur Material kaputt, keine Menschen starben", ok: false },
            ] },
          },
        },
        {
          nr: 19, typ: "luecke", eyebrow: "Fachbegriffe", titel: "Der Krieg in Stichworten",
          niveaus: {
            A: { modus: "chips", ablenker: ["Rom", "Fahrräder"], text: "1914 stoppten die Franzosen den deutschen Angriff an der [Marne]. Danach lagen die Soldaten in [Schützengräben]. 1916 tobte die Schlacht um [Verdun]. 1917 traten die [USA] in den Krieg ein." },
            B: { modus: "input", text: "Der deutsche Kriegsplan hieß [Schlieffen-Plan|Schlieffenplan]. Im Osten besiegte Deutschland 1914 die Russen bei [Tannenberg]. 1915 setzte Deutschland bei Ypern zum ersten Mal [Giftgas|Gas|Chlorgas] ein. Der uneingeschränkte [U-Boot-Krieg|U-Bootkrieg|Ubootkrieg|U-Boot Krieg] brachte 1917 die USA in den Krieg. Nach der Revolution stieg [Russland] aus dem Krieg aus." },
            C: { modus: "input", text: "Deutschland führte einen [Zweifrontenkrieg] gegen Frankreich und Russland. Der Krieg wurde zum [totalen|totaler] Krieg, weil auch die Menschen zu Hause an der [Heimatfront] betroffen waren. Im [Steckrübenwinter|Hungerwinter|Kohlrübenwinter] 1916/17 hungerte Deutschland. Der Frieden von [Brest-Litowsk|Brest Litowsk|Brest-Litovsk] beendete im März 1918 den Krieg im Osten. Die deutsche [Frühjahrsoffensive] 1918 scheiterte. Ab dem 8. August drängten die Alliierten die Deutschen zurück." },
          },
        },
        {
          nr: 20, typ: "zuordnung", eyebrow: "Jahr und Ereignis", titel: "Was geschah wann?",
          niveaus: {
            A: { links: "Jahr", rechts: "Ereignis", paare: [
              ["1914", "Marneschlacht – der Stellungskrieg beginnt"],
              ["1916", "Schlacht um Verdun"],
              ["1917", "Die USA treten in den Krieg ein"],
            ] },
            B: { links: "Jahr", rechts: "Ereignis", paare: [
              ["1914", "Marneschlacht – der Stellungskrieg beginnt"],
              ["1915", "Erstes Giftgas bei Ypern"],
              ["1916", "Schlacht um Verdun"],
              ["1917", "Die USA treten in den Krieg ein"],
            ] },
            C: { links: "Jahr", rechts: "Ereignisse", paare: [
              ["1914", "Marneschlacht und Tannenberg – Krieg an zwei Fronten"],
              ["1915", "Giftgas bei Ypern, Italien kämpft gegen Österreich-Ungarn"],
              ["1916", "Verdun, Somme und Skagerrakschlacht"],
              ["1917", "USA treten ein, Russland steigt nach der Revolution aus"],
              ["1918", "Frühjahrsoffensive scheitert, Alliierte drängen zurück"],
            ] },
          },
        },
        {
          nr: 21, typ: "sortierung", eyebrow: "Zeitliche Ordnung", titel: "Der Krieg 1914–1918",
          niveaus: {
            A: { hinweis: "Drei Wendepunkte – mit Jahreszahl.", items: [
              "1914 · Marneschlacht: Der Schlieffen-Plan scheitert",
              "1916 · Schlacht um Verdun",
              "1917 · Die USA treten in den Krieg ein",
            ] },
            B: { hinweis: "Fünf Ereignisse ohne Jahreszahl.", items: [
              "Marneschlacht: Der Schlieffen-Plan scheitert",
              "Erstes Giftgas bei Ypern",
              "Schlachten um Verdun und an der Somme",
              "Die USA treten in den Krieg ein",
              "Frieden von Brest-Litowsk mit Russland",
            ] },
            C: { hinweis: "Sieben Ereignisse ohne Jahreszahl.", items: [
              "Marneschlacht: Der Schlieffen-Plan scheitert",
              "Italien tritt gegen Österreich-Ungarn in den Krieg ein",
              "Beginn der Schlacht um Verdun",
              "Somme-Schlacht mit den ersten Panzern",
              "Beginn des uneingeschränkten U-Boot-Krieges",
              "Die USA treten in den Krieg ein",
              "Frieden von Brest-Litowsk mit Russland",
            ] },
          },
        },
        {
          nr: 22, typ: "diagramm", eyebrow: "Diagramm lesen", titel: "Der Preis des Krieges",
          chart: {
            typ: "bar", einheit: "Mio.", yTitel: "Gefallene Soldaten in Millionen (gerundet)",
            quelle: "Gerundete Schätzungen – andere Quellen nennen andere Zahlen. Tippe auf einen Balken.",
            labels: ["Deutsches Reich", "Russland", "Frankreich", "Österreich-Ungarn", "Großbritannien (mit Empire)", "Osmanisches Reich", "Italien", "USA"],
            datasets: [{ label: "Gefallene Soldaten (Mio.)", data: [2.0, 1.8, 1.4, 1.1, 0.9, 0.8, 0.65, 0.12], farben: ["#8b1e2d", "#006AB3", "#006AB3", "#8b1e2d", "#006AB3", "#8b1e2d", "#006AB3", "#006AB3"] }],
            legendeExtra: "rot = Mittelmächte, blau = Entente",
          },
          niveaus: {
            A: { frage: "Welches Land hatte die meisten gefallenen Soldaten?", optionen: [
              { t: "Das Deutsche Reich", ok: true }, { t: "Die USA", ok: false }, { t: "Italien", ok: false },
            ] },
            B: { frage: "Warum hatten die USA so wenige Gefallene?", optionen: [
              { t: "Sie kamen erst 1917 dazu und kämpften erst 1918 in großer Zahl", ok: true },
              { t: "Ihre Waffen waren besser als alle anderen", ok: false },
              { t: "Sie kämpften nur auf See", ok: false },
              { t: "Sie waren mit Deutschland verbündet", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zu diesem Diagramm stimmen?", optionen: [
              { t: "Die Zahlen sind Schätzungen – man muss immer die Quelle prüfen", ok: true },
              { t: "Beide Seiten verloren Millionen Soldaten – es gab keinen „billigen“ Sieg", ok: true },
              { t: "Das Diagramm zeigt auch die toten Zivilisten und die Opfer der Grippe", ok: false },
              { t: "Die Zahlen beweisen, dass Deutschland gewonnen hat", ok: false },
            ] },
          },
        },
        {
          nr: 23, typ: "karte", eyebrow: "Karte erkunden", titel: "Die Fronten des Krieges", karte: "fronten",
          benoetigt: { A: 3, B: 5, C: 7 },
          niveaus: {
            A: { frage: "An welcher Front kämpften Deutschland und Frankreich gegeneinander?", optionen: [
              { t: "An der Westfront", ok: true }, { t: "An der Ostfront", ok: false }, { t: "An der Alpenfront", ok: false },
            ] },
            B: { frage: "Warum blieb die Ostfront beweglicher als die Westfront?", optionen: [
              { t: "Sie war viel länger und dünner besetzt – Durchbrüche blieben möglich", ok: true },
              { t: "Im Osten gab es keine Maschinengewehre", ok: false },
              { t: "Russland hatte keine Armee", ok: false },
              { t: "Die Ostfront lag am Meer", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zum Seekrieg stimmen?", optionen: [
              { t: "Die britische Blockade ließ kaum noch Waren nach Deutschland – die Menschen hungerten", ok: true },
              { t: "Der U-Boot-Krieg brachte 1917 die USA in den Krieg – ein großer Fehler Deutschlands", ok: true },
              { t: "Die Skagerrakschlacht 1916 zerstörte die britische Flotte", ok: false },
              { t: "Deutschland beherrschte den Atlantik bis Kriegsende", ok: false },
            ] },
          },
        },
        {
          nr: 24, typ: "freitext", eyebrow: "Erklären", titel: "Warum blieb die Front stehen?",
          kontext: "Klasse 9 Geschichte, Abschnitt Verlauf. Begriffe: Marneschlacht, Schützengraben, Maschinengewehr, Artillerie, Stellungskrieg, Materialschlacht, totaler Krieg, Heimatfront.",
          niveaus: {
            A: { aufgabe: "Erkläre in 3 Sätzen: Warum wurde aus dem schnellen Krieg 1914 ein Stellungskrieg?", starter: ["Zuerst …", "Aber dann …", "Deshalb …"], begriffe: ["Marne", "Schützengraben", "Maschinengewehr"], min: 60 },
            B: { aufgabe: "Erkläre: Warum machten neue Waffen (Maschinengewehr, Artillerie, Giftgas) den Stellungskrieg so blutig? Warum wurde trotzdem kaum Land gewonnen?", begriffe: ["Stellungskrieg", "Materialschlacht", "Verdun", "Verteidigung"], min: 100 },
            C: { aufgabe: "Erkläre den Begriff „totaler Krieg“ am Beispiel des Ersten Weltkriegs. Gehe auf Heimatfront, Wirtschaft, Propaganda und Zivilbevölkerung ein. Beurteile: Wie wichtig war der Kriegseintritt der USA?", begriffe: ["totaler Krieg", "Heimatfront", "Seeblockade", "Propaganda", "USA"], min: 150 },
          },
        },
        {
          nr: 25, typ: "notizen", eyebrow: "Recherche", titel: "Meine Stichpunkte: Verlauf", abschnitt: "verlauf",
          hinweis: "Ordne deine Stichpunkte nach Jahren (1914, 1915, 1916, 1917, 1918). Ein Stichpunkt pro Ereignis.",
          kiFrage: "Prüfe diese Stichpunkte zum Verlauf des Ersten Weltkriegs (1914–1918): Stimmen Jahreszahlen und Reihenfolge?",
        },
        {
          nr: 26, typ: "zeichnen", eyebrow: "Zeichnen", titel: "Der Schützengraben", geraet: "schuetzengraben",
          niveaus: {
            A: { aufgabe: "Zeichne einen Schützengraben von der Seite: Graben, Sandsäcke, Stacheldraht davor und das Niemandsland. Beschrifte drei Teile.", elemente: ["Graben", "Sandsäcke", "Stacheldraht", "Niemandsland", "mindestens drei Beschriftungen"], hinweis: "Von der Seite heißt: wie ein aufgeschnittener Kuchen." },
            B: { aufgabe: "Zeichne zwei Gräben, die sich gegenüberliegen, mit Niemandsland dazwischen. Ergänze ein Maschinengewehr, Stacheldraht und einen Unterstand. Beschrifte alles.", elemente: ["zwei Gräben gegenüber", "Niemandsland", "Maschinengewehr", "Stacheldraht", "Unterstand", "Beschriftungen"], hinweis: "Das Niemandsland war oft nur 50 bis 300 Meter breit." },
            C: { aufgabe: "Zeichne, warum ein Angriff im Stellungskrieg scheiterte: Angreifer im Niemandsland, Maschinengewehre mit Schussfeld (Pfeile), Artillerie, Stacheldraht. Markiere die entscheidende Stelle und erkläre sie kurz.", elemente: ["Angreifer im offenen Niemandsland", "Maschinengewehre mit Pfeilen für das Schussfeld", "Artillerie", "Stacheldraht", "Markierung und kurze Erklärung"], hinweis: "Die Zeichnung soll etwas erklären – kein Schlachtenbild." },
          },
        },
      ],
    },

    // ════════════════════════════════ KRIEGSENDE ═══════════════════════
    {
      key: "kriegsende", label: "Kriegsende", icon: "🕊️", kurz: "K",
      intro: {
        eyebrow: "Lesestrecke M4", titel: "Niederlage, Revolution, Waffenstillstand",
        begriffe: ["Oberste Heeresleitung", "Hindenburg", "Ludendorff", "14 Punkte Wilsons", "Oktoberreformen", "Matrosenaufstand", "Novemberrevolution", "Ausrufung der Republik", "Waffenstillstand von Compiègne", "Dolchstoßlegende"],
      },
      aufgaben: [
        {
          nr: 27, typ: "mc", eyebrow: "Grundwissen", titel: "Warum verlor Deutschland?",
          niveaus: {
            A: { frage: "Wann begann der Waffenstillstand?", optionen: [
              { t: "Am 11. November 1918", ok: true }, { t: "Am 28. Juni 1914", ok: false }, { t: "Am 8. Mai 1945", ok: false },
            ] },
            B: { frage: "Was bewirkte der Kriegseintritt der USA 1917?", optionen: [
              { t: "Frische Soldaten, Waffen und Lebensmittel – die Alliierten wurden dauerhaft stärker", ok: true },
              { t: "Die USA kämpften für Deutschland", ok: false },
              { t: "Die USA blieben bis zum Ende neutral", ok: false },
              { t: "Die USA schickten nur Geld", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zur Dolchstoßlegende stimmen?", optionen: [
              { t: "Die Legende behauptete: Das Heer war unbesiegt und wurde von der Heimat „von hinten erdolcht“", ok: true },
              { t: "In Wahrheit hatte die Heeresleitung selbst Ende September 1918 den Waffenstillstand verlangt", ok: true },
              { t: "Die Legende wurde 1919 von den Alliierten erfunden", ok: false },
              { t: "Die Legende beschreibt 1918 richtig", ok: false },
            ] },
          },
        },
        {
          nr: 28, typ: "luecke", eyebrow: "Fachbegriffe", titel: "Die letzten Monate",
          niveaus: {
            A: { modus: "chips", ablenker: ["Sieg", "Paris"], text: "In [Kiel] weigerten sich Matrosen im November 1918, noch einmal auszulaufen. Am 9. November wurde in Berlin die [Republik] ausgerufen. Am 11. November 1918 begann der [Waffenstillstand]. Der Kriegseintritt der [USA] hatte alles verändert." },
            B: { modus: "input", text: "Ende September 1918 verlangte die Heeresleitung um Hindenburg und [Ludendorff] einen Waffenstillstand. Der Matrosenaufstand in [Kiel] löste die [Novemberrevolution] aus. Kaiser [Wilhelm II.|Wilhelm II|Wilhelm] dankte ab und floh in die Niederlande. Philipp [Scheidemann] rief am 9. November die Republik aus. Der Waffenstillstand wurde in [Compiègne|Compiegne] unterschrieben." },
            C: { modus: "input", text: "Grundlage der Verhandlungen waren die [14 Punkte|vierzehn Punkte|14-Punkte] des US-Präsidenten Wilson. Mit den [Oktoberreformen] bekam der Reichstag mehr Macht. Prinz Max von [Baden] wurde Reichskanzler. Nacheinander gaben Bulgarien, das [Osmanische Reich|Osmanische] und Österreich-Ungarn auf. Friedrich [Ebert] übernahm am 9. November die Regierung. Die [Dolchstoßlegende|Dolchstosslegende] gab der Heimat die Schuld an der Niederlage – nicht den Generälen." },
          },
        },
        {
          nr: 29, typ: "sortierung", eyebrow: "Zeitliche Ordnung", titel: "Vom Sommer 1918 zum Waffenstillstand",
          niveaus: {
            A: { hinweis: "Drei Daten aus dem Jahr 1918.", items: [
              "8. August 1918 · „Schwarzer Tag des deutschen Heeres“",
              "9. November 1918 · Die Republik wird ausgerufen",
              "11. November 1918 · Waffenstillstand von Compiègne",
            ] },
            B: { hinweis: "Fünf Schritte ohne Datum.", items: [
              "Die deutsche Frühjahrsoffensive scheitert",
              "Alliierter Gegenangriff: „Schwarzer Tag des deutschen Heeres“",
              "Die Heeresleitung verlangt einen Waffenstillstand",
              "Matrosenaufstand in Kiel",
              "Waffenstillstand von Compiègne",
            ] },
            C: { hinweis: "Sieben Schritte ohne Datum.", items: [
              "Die deutsche Frühjahrsoffensive scheitert",
              "Alliierter Gegenangriff: „Schwarzer Tag des deutschen Heeres“",
              "Die Heeresleitung verlangt einen Waffenstillstand",
              "Oktoberreformen: Prinz Max von Baden wird Reichskanzler",
              "Matrosenaufstand in Kiel",
              "Die Republik wird in Berlin ausgerufen",
              "Waffenstillstand von Compiègne",
            ] },
          },
        },
        {
          nr: 30, typ: "zuordnung", eyebrow: "Begriffe", titel: "Begriffe des Kriegsendes",
          niveaus: {
            A: { links: "Begriff", rechts: "Erklärung", paare: [
              ["Waffenstillstand", "Die Kämpfe hören auf – ein Friedensvertrag kommt später"],
              ["Novemberrevolution", "Matrosen, Soldaten und Arbeiter stürzen die Monarchie"],
              ["14 Punkte", "Friedensplan des US-Präsidenten Wilson"],
            ] },
            B: { links: "Begriff", rechts: "Erklärung", paare: [
              ["Waffenstillstand", "Die Kämpfe hören auf – ein Friedensvertrag kommt später"],
              ["Novemberrevolution", "Matrosen, Soldaten und Arbeiter stürzen die Monarchie"],
              ["14 Punkte", "Friedensplan des US-Präsidenten Wilson"],
              ["Dolchstoßlegende", "Falsche Behauptung: Die Heimat habe das Heer verraten"],
            ] },
            C: { links: "Begriff", rechts: "Erklärung", paare: [
              ["Waffenstillstand", "Die Kämpfe hören auf – ein Friedensvertrag kommt später"],
              ["Novemberrevolution", "Matrosen, Soldaten und Arbeiter stürzen die Monarchie"],
              ["14 Punkte", "Wilsons Friedensplan: Selbstbestimmung der Völker, Völkerbund"],
              ["Dolchstoßlegende", "Falsche Behauptung: Die Heimat habe das Heer verraten"],
              ["Oktoberreformen", "1918: Der Reichskanzler braucht die Mehrheit des Reichstags"],
            ] },
          },
        },
        {
          nr: 31, typ: "diagramm", eyebrow: "Diagramm lesen", titel: "Die Amerikaner kommen",
          chart: {
            typ: "line", einheit: "Tsd.", yTitel: "US-Soldaten in Frankreich (in Tausend)",
            quelle: "Gerundete Werte zum Monatsende. Tippe auf einen Punkt.",
            labels: ["Dez 1917", "Feb 1918", "Apr 1918", "Jun 1918", "Aug 1918", "Okt 1918", "Nov 1918"],
            datasets: [{ label: "US-Soldaten in Frankreich (Tsd.)", data: [175, 250, 430, 900, 1470, 1870, 2000], farbe: "#006AB3" }],
          },
          niveaus: {
            A: { frage: "Wie viele US-Soldaten waren im November 1918 in Frankreich?", optionen: [
              { t: "Rund 2 Millionen", ok: true }, { t: "Rund 20.000", ok: false }, { t: "Rund 200", ok: false },
            ] },
            B: { frage: "Was bedeutete das für die deutsche Führung?", optionen: [
              { t: "Sie versuchte im Frühjahr 1918 einen letzten Angriff, bevor die US-Truppen zu stark wurden", ok: true },
              { t: "Sie zog alle Truppen aus Frankreich ab", ok: false },
              { t: "Sie schloss 1917 Frieden mit den USA", ok: false },
              { t: "Sie schickte selbst Soldaten in die USA", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Schlüsse stimmen?", optionen: [
              { t: "Die Kurve erklärt, warum die deutsche Frühjahrsoffensive unter Zeitdruck stand", ok: true },
              { t: "Ab Sommer 1918 waren die Alliierten dauerhaft stärker", ok: true },
              { t: "US-Truppen kämpften schon 1914 in großer Zahl", ok: false },
              { t: "Die Kurve zeigt die deutschen Verluste", ok: false },
            ] },
          },
        },
        {
          nr: 32, typ: "karte", eyebrow: "Karte erkunden", titel: "Orte des Kriegsendes", karte: "kriegsende",
          benoetigt: { A: 3, B: 5, C: 7 },
          niveaus: {
            A: { frage: "Wo begann die Novemberrevolution?", optionen: [
              { t: "In Kiel", ok: true }, { t: "In Compiègne", ok: false }, { t: "In Wien", ok: false },
            ] },
            B: { frage: "Wo wurde der Waffenstillstand unterschrieben?", optionen: [
              { t: "In einem Eisenbahnwagen bei Compiègne", ok: true },
              { t: "Im Schloss von Versailles", ok: false },
              { t: "Im Hauptquartier in Spa", ok: false },
              { t: "Im Reichstag in Berlin", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Zusammenhänge zeigt die Karte?", optionen: [
              { t: "Der Frieden von Brest-Litowsk im Osten machte die Frühjahrsoffensive im Westen möglich – trotzdem reichte es nicht", ok: true },
              { t: "Erst kam die Niederlage an der Front (Amiens, Spa), dann die Revolution zu Hause (Kiel, Berlin)", ok: true },
              { t: "Die Revolution in Kiel zwang eine siegreiche Armee zur Aufgabe", ok: false },
              { t: "Der Waffenstillstand wurde in Berlin unterschrieben", ok: false },
            ] },
          },
        },
        {
          nr: 33, typ: "freitext", eyebrow: "Erklären", titel: "Warum endete der Krieg 1918?",
          kontext: "Klasse 9 Geschichte, Abschnitt Kriegsende. Begriffe: Kriegseintritt der USA, Erschöpfung, Hunger, Seeblockade, Bündnispartner, Oberste Heeresleitung, Novemberrevolution, Waffenstillstand, Dolchstoßlegende.",
          niveaus: {
            A: { aufgabe: "Erkläre in 3 Sätzen: Warum verlor Deutschland den Krieg 1918?", starter: ["Ein wichtiger Grund war …", "Außerdem …", "Am Ende …"], begriffe: ["USA", "Hunger", "Revolution"], min: 60 },
            B: { aufgabe: "Erkläre: Warum verlor Deutschland den Krieg? Nenne drei Gründe: einen militärischen, einen wirtschaftlichen und einen politischen.", begriffe: ["Frühjahrsoffensive", "USA", "Seeblockade", "Bündnispartner", "Novemberrevolution"], min: 100 },
            C: { aufgabe: "Beurteile die Dolchstoßlegende: Warum war sie falsch? Warum war sie trotzdem so gefährlich für die junge Republik?", begriffe: ["Oberste Heeresleitung", "29. September 1918", "Novemberrevolution", "Weimarer Republik", "Propaganda"], min: 150 },
          },
        },
        {
          nr: 34, typ: "notizen", eyebrow: "Recherche", titel: "Meine Stichpunkte: Kriegsende", abschnitt: "kriegsende",
          hinweis: "Schreibe die Schritte von der Niederlage bis zum Waffenstillstand auf – mit Daten.",
          kiFrage: "Prüfe diese Stichpunkte zum Kriegsende 1918 (Heeresleitung, Novemberrevolution, Waffenstillstand): Stimmen Daten und Reihenfolge?",
        },
      ],
    },

    // ════════════════════════════════ FOLGEN ═══════════════════════════
    {
      key: "folgen", label: "Folgen", icon: "🧩", kurz: "F",
      intro: {
        eyebrow: "Lesestrecke M5", titel: "Ein neues Europa und die „Urkatastrophe“",
        begriffe: ["Versailler Vertrag", "Artikel 231", "Reparationen", "Gebietsverluste", "Völkerbund", "Weimarer Republik", "neue Staaten", "Frauenwahlrecht", "Urkatastrophe"],
      },
      aufgaben: [
        {
          nr: 35, typ: "mc", eyebrow: "Grundwissen", titel: "Der Versailler Vertrag",
          niveaus: {
            A: { frage: "Was stand im Versailler Vertrag von 1919?", optionen: [
              { t: "Deutschland musste Gebiete abgeben, Geld zahlen und sein Heer verkleinern", ok: true },
              { t: "Deutschland bekam neue Kolonien in Afrika", ok: false },
              { t: "Deutschland und Frankreich wurden Verbündete", ok: false },
            ] },
            B: { frage: "Was sagte Artikel 231 des Vertrags?", optionen: [
              { t: "Deutschland und seine Verbündeten sind schuld am Krieg (Kriegsschuldartikel)", ok: true },
              { t: "Deutschland darf sofort in den Völkerbund", ok: false },
              { t: "Elsass-Lothringen bleibt deutsch", ok: false },
              { t: "Der Kaiser darf zurückkommen", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen erklären, warum der Vertrag die Weimarer Republik belastete?", optionen: [
              { t: "Viele Deutsche nannten ihn „Diktat“, weil Deutschland nicht mitverhandeln durfte", ok: true },
              { t: "Die Politiker, die ihn unterschreiben mussten, wurden von Rechtsextremen als Verräter beschimpft", ok: true },
              { t: "Der Vertrag erlaubte Deutschland eine Armee von fünf Millionen Mann", ok: false },
              { t: "Fast alle Deutschen begrüßten den Vertrag", ok: false },
            ] },
          },
        },
        {
          nr: 36, typ: "luecke", eyebrow: "Fachbegriffe", titel: "Ein neues Europa",
          niveaus: {
            A: { modus: "chips", ablenker: ["Monarchie", "Sieger"], text: "1919 musste Deutschland den Vertrag von [Versailles] unterschreiben. Es musste [Reparationen] an die Sieger zahlen. Aus dem Kaiserreich wurde eine [Republik]. Damit es keinen neuen Krieg gibt, wurde der [Völkerbund] gegründet." },
            B: { modus: "input", text: "Deutschland verlor [Elsass-Lothringen|Elsaß-Lothringen] an Frankreich und Gebiete im Osten an das neue [Polen]. Das Heer durfte nur noch [100.000|100000|100 000] Mann haben. Artikel [231] legte die Kriegsschuld fest. Die großen Reiche [Österreich-Ungarn|Österreich Ungarn] und das Osmanische Reich zerfielen." },
            C: { modus: "input", text: "Im Krieg starben rund [9|10|neun|zehn] Millionen Soldaten. Neue Staaten wie die [Tschechoslowakei], Polen und Jugoslawien entstanden. Vier Herrscherhäuser endeten: Hohenzollern, Habsburger, [Romanow|Romanows|Romanov] und Osmanen. In Deutschland führten Schulden und Reparationen 1923 zur [Hyperinflation|Inflation]. Die USA traten dem [Völkerbund] nicht bei. Der Historiker George F. Kennan nannte den Krieg die [Urkatastrophe] des 20. Jahrhunderts." },
          },
        },
        {
          nr: 37, typ: "zuordnung", eyebrow: "Folgen ordnen", titel: "Welche Folge gehört wohin?",
          niveaus: {
            A: { links: "Folge", rechts: "Bereich", paare: [
              ["Ende der Monarchie, Weimarer Republik", "Politik"],
              ["Reparationen und Inflation", "Wirtschaft"],
              ["Millionen Tote und Verletzte", "Gesellschaft"],
            ] },
            B: { links: "Folge", rechts: "Bereich", paare: [
              ["Ende der Monarchie, Weimarer Republik", "Politik"],
              ["Reparationen und Inflation", "Wirtschaft"],
              ["Millionen Tote und Verletzte", "Gesellschaft"],
              ["Verlust von Elsass-Lothringen und der Kolonien", "Gebiete"],
            ] },
            C: { links: "Folge", rechts: "Bereich", paare: [
              ["Vier Monarchien enden, neue Republiken entstehen", "Politik"],
              ["Reparationen, Schulden und Hyperinflation 1923", "Wirtschaft"],
              ["Kriegsversehrte, Frauenwahlrecht, „verlorene Generation“", "Gesellschaft"],
              ["Deutschland verliert Gebiete, neue Staaten im Osten", "Gebiete"],
              ["Völkerbund gegründet, USA werden Weltmacht", "Internationale Politik"],
            ] },
          },
        },
        {
          nr: 38, typ: "diagramm", eyebrow: "Diagramm lesen", titel: "Was Deutschland verlor",
          chart: {
            typ: "bar", horizontal: true, einheit: "%", yTitel: "Verlust in Prozent (Vergleich mit 1914)",
            quelle: "Gerundete Werte zum Versailler Vertrag. Tippe auf einen Balken.",
            labels: ["Staatsgebiet", "Bevölkerung", "Steinkohle", "Eisenerz", "Kolonien"],
            datasets: [{ label: "Verlust in %", data: [13, 10, 26, 75, 100], farbe: "#AD007C" }],
          },
          niveaus: {
            A: { frage: "Wie viel Prozent seiner Fläche verlor Deutschland?", optionen: [
              { t: "Etwa 13 Prozent", ok: true }, { t: "Etwa 75 Prozent", ok: false }, { t: "Gar nichts", ok: false },
            ] },
            B: { frage: "Was bedeutete der Verlust von 75 Prozent des Eisenerzes?", optionen: [
              { t: "Die Stahl- und Rüstungsindustrie wurde schwächer, Deutschland musste Erz kaufen", ok: true },
              { t: "Deutschland hatte danach mehr Eisen als vorher", ok: false },
              { t: "Die Landwirtschaft brach zusammen", ok: false },
              { t: "Es hatte keine Folgen", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen stimmen?", optionen: [
              { t: "Deutschland blieb ein großer Staat – 87 Prozent des Gebiets und 90 Prozent der Menschen blieben", ok: true },
              { t: "Die Rohstoffverluste wogen schwerer als der Flächenverlust – das erklärt einen Teil der Wut", ok: true },
              { t: "Deutschland verlor über die Hälfte seiner Bevölkerung", ok: false },
              { t: "Das Diagramm zeigt die Verluste Frankreichs", ok: false },
            ] },
          },
        },
        {
          nr: 39, typ: "sortierung", eyebrow: "Zeitliche Ordnung", titel: "Nach dem Krieg",
          niveaus: {
            A: { hinweis: "Drei Daten nach dem Krieg.", items: [
              "11. November 1918 · Waffenstillstand",
              "28. Juni 1919 · Versailler Vertrag wird unterschrieben",
              "Januar 1920 · Der Völkerbund beginnt seine Arbeit",
            ] },
            B: { hinweis: "Fünf Schritte ohne Datum.", items: [
              "Waffenstillstand von Compiègne",
              "Beginn der Friedenskonferenz in Paris",
              "Versailler Vertrag wird unterschrieben",
              "Die Weimarer Verfassung gilt",
              "Der Völkerbund beginnt seine Arbeit",
            ] },
            C: { hinweis: "Sieben Schritte ohne Datum – bis zur Krise 1923.", items: [
              "Waffenstillstand von Compiègne",
              "Wahl zur Nationalversammlung",
              "Versailler Vertrag wird unterschrieben",
              "Die Weimarer Verfassung gilt",
              "Der Völkerbund beginnt seine Arbeit",
              "Reparationen werden auf 132 Milliarden Goldmark festgelegt",
              "Ruhrbesetzung und Hyperinflation",
            ] },
          },
        },
        {
          nr: 40, typ: "karte", eyebrow: "Karte erkunden", titel: "Europa nach 1919", karte: "europa1920",
          benoetigt: { A: 3, B: 6, C: 10 },
          niveaus: {
            A: { frage: "Welcher Staat entstand 1918 neu aus Teilen von Österreich-Ungarn?", optionen: [
              { t: "Die Tschechoslowakei", ok: true }, { t: "Frankreich", ok: false }, { t: "Das Osmanische Reich", ok: false },
            ] },
            B: { frage: "Was war der „Polnische Korridor“?", optionen: [
              { t: "Ein Gebiet, das Polen den Zugang zur Ostsee gab und Ostpreußen vom Reich trennte", ok: true },
              { t: "Eine Eisenbahn von Berlin nach Warschau", ok: false },
              { t: "Ein Grenzstreifen zwischen Polen und Russland", ok: false },
              { t: "Ein Fluss in Schlesien", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Probleme der neuen Grenzen zeigt die Karte?", optionen: [
              { t: "In den neuen Staaten lebten große Minderheiten, zum Beispiel Deutsche in der Tschechoslowakei", ok: true },
              { t: "Verluste wie Danzig und der Korridor wurden in Deutschland als Unrecht gesehen – die Nationalsozialisten nutzten das später aus", ok: true },
              { t: "Österreich-Ungarn wurde 1919 größer", ok: false },
              { t: "Russland gewann das Baltikum und Finnland dazu", ok: false },
            ] },
          },
        },
        {
          nr: 41, typ: "freitext", eyebrow: "Beurteilen", titel: "Gerechter Frieden oder „Diktat“?",
          kontext: "Klasse 9 Geschichte, Abschnitt Folgen. Begriffe: Versailler Vertrag, Artikel 231, Reparationen, Gebietsverluste, Völkerbund, Weimarer Republik, Sicherheit Frankreichs.",
          niveaus: {
            A: { aufgabe: "Nenne drei Folgen des Ersten Weltkriegs. Erkläre eine davon genauer.", starter: ["Eine Folge war …", "Das bedeutete, dass …", "Eine weitere Folge …"], begriffe: ["Versailler Vertrag", "Republik", "Tote"], min: 60 },
            B: { aufgabe: "Erkläre: Warum fanden viele Deutsche den Versailler Vertrag ungerecht? Und was wollten die Sieger mit dem Vertrag erreichen?", begriffe: ["Artikel 231", "Reparationen", "Gebietsverluste", "Sicherheit", "Diktat"], min: 100 },
            C: { aufgabe: "Beurteile: War der Versailler Vertrag zu hart, zu mild oder angemessen? Nenne Argumente beider Seiten (zum Beispiel: Frankreichs Wunsch nach Sicherheit, die Zerstörungen in Nordfrankreich, der harte Frieden von Brest-Litowsk). Denke auch an die Folgen für später.", begriffe: ["Versailler Vertrag", "Brest-Litowsk", "Reparationen", "Weimarer Republik"], min: 150 },
          },
        },
        {
          nr: 42, typ: "notizen", eyebrow: "Recherche", titel: "Meine Stichpunkte: Folgen", abschnitt: "folgen",
          hinweis: "Ordne deine Stichpunkte nach Bereichen (Politik, Gebiete, Wirtschaft, Gesellschaft) oder nach Zeit.",
          kiFrage: "Prüfe diese Stichpunkte zu den Folgen des Ersten Weltkriegs (Versailler Vertrag, neue Staaten, Weimarer Republik, Völkerbund): Stimmen sie? Fehlt etwas Wichtiges?",
        },
        {
          nr: 43, typ: "zeichnen", eyebrow: "Zeichnen", titel: "Plakat oder Karikatur zu Versailles", geraet: "plakat",
          niveaus: {
            A: { aufgabe: "Gestalte ein Plakat mit dem Titel „Versailles 1919“. Zeichne Deutschland als Kasten und drei Pfeile nach außen: Gebiete, Kolonien, Heer. Beschrifte die Pfeile.", elemente: ["Titel Versailles 1919", "Kasten Deutschland", "drei beschriftete Pfeile: Gebiete, Kolonien, Heer"], hinweis: "Das Textwerkzeug hilft bei Titel und Beschriftungen." },
            B: { aufgabe: "Zeichne eine Karikatur, wie sie 1919 in einer deutschen ODER einer französischen Zeitung stehen könnte. Nutze Symbole (Waage, Ketten, Geldsack, Taube) und schreibe einen Satz darunter.", elemente: ["klare Sichtweise (deutsch oder französisch)", "mindestens zwei Symbole", "Satz unter dem Bild"], hinweis: "Eine Karikatur darf übertreiben." },
            C: { aufgabe: "Zeichne zwei Karikaturen nebeneinander: eine aus deutscher Sicht („Diktat“) und eine aus französischer Sicht („Sicherheit“). Zeige dieselbe Szene aus zwei Blickwinkeln und beschrifte beide.", elemente: ["zwei Bildhälften", "deutsche Sicht mit Beschriftung", "französische Sicht mit Beschriftung", "gleiche Szene aus zwei Blickwinkeln"], hinweis: "Zwei Sichtweisen nebeneinander – das ist deine Beurteilung als Bild." },
          },
        },
      ],
    },

    // ════════════════════════════════ ABSCHLUSS ════════════════════════
    {
      key: "abschluss", label: "Zeitstrahl & Quellen", icon: "📚", kurz: "Z",
      intro: {
        eyebrow: "Abschluss", titel: "Alles in der richtigen Reihenfolge – und mit guten Quellen",
        begriffe: ["Zeitstrahl", "Quellenkritik", "verlässliche Quelle", "Beleg", "Urkatastrophe"],
      },
      aufgaben: [
        {
          nr: 44, typ: "sortierung", eyebrow: "Überblick", titel: "Der große Zeitstrahl 1914–1919",
          niveaus: {
            A: { hinweis: "Vier Ereignisse mit Datum.", items: [
              "Juni 1914 · Attentat von Sarajevo",
              "September 1914 · Marneschlacht",
              "April 1917 · Die USA treten in den Krieg ein",
              "November 1918 · Waffenstillstand",
            ] },
            B: { hinweis: "Sechs Ereignisse ohne Datum.", items: [
              "Attentat von Sarajevo",
              "Marneschlacht – der Stellungskrieg beginnt",
              "Schlacht um Verdun",
              "Die USA treten in den Krieg ein",
              "Novemberrevolution und Waffenstillstand",
              "Versailler Vertrag",
            ] },
            C: { hinweis: "Neun Ereignisse ohne Datum – vom Attentat bis Versailles.", items: [
              "Attentat von Sarajevo",
              "Österreich-Ungarn erklärt Serbien den Krieg",
              "Marneschlacht – der Stellungskrieg beginnt",
              "Erstes Giftgas bei Ypern",
              "Schlacht um Verdun",
              "Die USA treten in den Krieg ein",
              "Frieden von Brest-Litowsk",
              "Waffenstillstand von Compiègne",
              "Versailler Vertrag wird unterschrieben",
            ] },
          },
        },
        {
          nr: 45, typ: "mc", eyebrow: "Quellenkritik", titel: "Gute Quellen erkennen",
          niveaus: {
            A: { frage: "Welche Quelle ist am verlässlichsten?", optionen: [
              { t: "Die Seite der Bundeszentrale für politische Bildung (bpb.de)", ok: true },
              { t: "Ein anonymer Kommentar unter einem Video", ok: false },
              { t: "Ein Bild mit einem Zitat ohne Herkunft", ok: false },
            ] },
            B: { frage: "Woran erkennst du eine verlässliche Internetseite?", optionen: [
              { t: "Autor oder Institution sind bekannt, die Angaben sind belegt, ein Datum steht dabei", ok: true },
              { t: "Sie hat viele Likes", ok: false },
              { t: "Sie steht ganz oben bei Google", ok: false },
              { t: "Sie sieht modern aus", ok: false },
            ] },
            C: { multi: 2, frage: "Welche ZWEI Aussagen zu Wikipedia und KI-Chatbots stimmen?", optionen: [
              { t: "Wikipedia ist gut zum Einstieg – wichtige Angaben prüft man über die Belege oder eine zweite Quelle", ok: true },
              { t: "KI-Chatbots können Fakten und Quellen erfinden – immer nachprüfen", ok: true },
              { t: "Was ein KI-Chatbot sagt, ist immer richtig", ok: false },
              { t: "Wikipedia darf man in der Schule nie benutzen", ok: false },
            ] },
          },
        },
        {
          nr: 46, typ: "blitz", eyebrow: "Blitzfragen", titel: "Blitzrunde",
          hinweis: "Jede Frage kommt nur einmal. Die Antworten werden jedes Mal neu gemischt.",
          niveaus: {
            A: { ziel: 6, stufen: [1], hinweis: "Sechs leichte Fragen richtig beantworten." },
            B: { ziel: 8, stufen: [1, 2], hinweis: "Acht Fragen, leicht und mittel." },
            C: { ziel: 10, stufen: [1, 2, 3], hinweis: "Zehn Fragen – auch die schweren." },
          },
          pool: [
            { id: "b01", stufe: 1, frage: "In welchem Jahr begann der Erste Weltkrieg?", optionen: ["1914", "1918", "1939"], ok: 0 },
            { id: "b02", stufe: 1, frage: "Wo wurde Franz Ferdinand ermordet?", optionen: ["Sarajevo", "Wien", "Belgrad"], ok: 0 },
            { id: "b03", stufe: 1, frage: "Wie hieß der Attentäter von Sarajevo?", optionen: ["Gavrilo Princip", "Philipp Scheidemann", "Erich Ludendorff"], ok: 0 },
            { id: "b04", stufe: 1, frage: "Welche drei Staaten bildeten den Dreibund?", optionen: ["Deutschland, Österreich-Ungarn, Italien", "Frankreich, Russland, Großbritannien", "Serbien, Belgien, Bulgarien"], ok: 0 },
            { id: "b05", stufe: 1, frage: "Wann begann der Waffenstillstand?", optionen: ["11. November 1918", "28. Juni 1919", "9. November 1918"], ok: 0 },
            { id: "b06", stufe: 1, frage: "Welches Land trat 1917 in den Krieg ein?", optionen: ["Die USA", "Italien", "Japan"], ok: 0 },
            { id: "b07", stufe: 1, frage: "Wie heißt ein Krieg in Schützengräben, bei dem sich die Front kaum bewegt?", optionen: ["Stellungskrieg", "Bewegungskrieg", "Seekrieg"], ok: 0 },
            { id: "b08", stufe: 1, frage: "Wo begann die Novemberrevolution?", optionen: ["Kiel", "München", "Berlin"], ok: 0 },
            { id: "b09", stufe: 1, frage: "Wie hieß der Friedensvertrag mit Deutschland 1919?", optionen: ["Versailler Vertrag", "Vertrag von Trianon", "Frieden von Brest-Litowsk"], ok: 0 },
            { id: "b10", stufe: 1, frage: "Welches Gebiet ging 1919 an Frankreich zurück?", optionen: ["Elsass-Lothringen", "Belgien", "Das Saarland für immer"], ok: 0 },
            { id: "b11", stufe: 2, frage: "Was ist der „Blankoscheck“?", optionen: ["Deutschlands Versprechen an Österreich-Ungarn: volle Unterstützung", "Serbiens Antwort auf das Ultimatum", "Die Reparationen"], ok: 0 },
            { id: "b12", stufe: 2, frage: "In welcher Schlacht scheiterte der Schlieffen-Plan?", optionen: ["Marneschlacht 1914", "Verdun 1916", "Tannenberg 1914"], ok: 0 },
            { id: "b13", stufe: 2, frage: "Warum traten die USA in den Krieg ein?", optionen: ["Wegen des uneingeschränkten U-Boot-Kriegs", "Wegen des Einmarschs in Belgien", "Wegen der Revolution in Russland"], ok: 0 },
            { id: "b14", stufe: 2, frage: "Welcher Frieden beendete 1918 den Krieg im Osten?", optionen: ["Brest-Litowsk", "Compiègne", "Saint-Germain"], ok: 0 },
            { id: "b15", stufe: 2, frage: "Was stand in Artikel 231 des Versailler Vertrags?", optionen: ["Deutschland ist schuld am Krieg", "Deutschland darf 100.000 Soldaten haben", "Das Saargebiet geht an den Völkerbund"], ok: 0 },
            { id: "b16", stufe: 2, frage: "Wer rief am 9. November 1918 die Republik aus?", optionen: ["Philipp Scheidemann", "Friedrich Ebert", "Max von Baden"], ok: 0 },
            { id: "b17", stufe: 2, frage: "Was war der „Steckrübenwinter“?", optionen: ["Der Hungerwinter 1916/17 wegen der britischen Blockade", "Die erste Schlacht mit Panzern", "Der Winter der Novemberrevolution"], ok: 0 },
            { id: "b18", stufe: 2, frage: "Welche Waffe wurde 1915 bei Ypern zum ersten Mal eingesetzt?", optionen: ["Giftgas", "Panzer", "U-Boot"], ok: 0 },
            { id: "b19", stufe: 3, frage: "Warum blieb Italien 1914 neutral?", optionen: ["Der Dreibund galt nur zur Verteidigung und Italien hatte eigene Ziele", "Italien hatte keine Armee", "Großbritannien hatte Italien besetzt"], ok: 0 },
            { id: "b20", stufe: 3, frage: "Was war an der Dolchstoßlegende falsch?", optionen: ["Die Heeresleitung selbst hatte den Waffenstillstand verlangt", "Es gab keine Revolution in Deutschland", "Der Krieg war 1918 noch nicht verloren"], ok: 0 },
            { id: "b21", stufe: 3, frage: "Welche zwei Ereignisse folgten in der Julikrise direkt aufeinander?", optionen: ["Russlands Mobilmachung und Deutschlands Kriegserklärung an Russland", "Marneschlacht und Tannenberg", "Kriegseintritt der USA und Brest-Litowsk"], ok: 0 },
            { id: "b22", stufe: 3, frage: "Was bedeutete der „Polnische Korridor“ für Deutschland?", optionen: ["Ostpreußen war vom Rest des Reiches getrennt", "Deutschland verlor das Rheinland", "Polen bekam Berlin"], ok: 0 },
            { id: "b23", stufe: 3, frage: "Warum stand die deutsche Frühjahrsoffensive 1918 unter Zeitdruck?", optionen: ["Immer mehr US-Soldaten kamen nach Frankreich", "Russland griff wieder an", "Giftgas war verboten worden"], ok: 0 },
            { id: "b24", stufe: 3, frage: "Was meinte George F. Kennan mit „Urkatastrophe des 20. Jahrhunderts“?", optionen: ["Der Erste Weltkrieg bereitete den Boden für Faschismus und Zweiten Weltkrieg", "Der Erste Weltkrieg war der erste Krieg mit Flugzeugen", "Die Spanische Grippe tötete mehr Menschen als der Krieg"], ok: 0 },
          ],
        },
        {
          nr: 47, typ: "domino", eyebrow: "Spiel", titel: "Begriffs-Domino",
          hinweis: "Jeder Stein hat links eine Erklärung und rechts einen Begriff. Lege den Stein an, dessen Erklärung zum offenen Begriff passt.",
          niveaus: {
            A: { steine: 6, hinweis: "Sechs Steine – die Grundbegriffe." },
            B: { steine: 9, hinweis: "Neun Steine." },
            C: { steine: 12, hinweis: "Alle zwölf Steine – die Kette schließt sich." },
          },
          paare: [
            { id: "d01", begriff: "Imperialismus", definition: "Wettlauf der Großmächte um Kolonien und Macht" },
            { id: "d02", begriff: "Nationalismus", definition: "Das eigene Volk gilt als besser als andere" },
            { id: "d03", begriff: "Militarismus", definition: "Das Militär hat hohes Ansehen, Krieg gilt als normal" },
            { id: "d04", begriff: "Blankoscheck", definition: "Volle Unterstützung: Deutschlands Versprechen an Wien" },
            { id: "d05", begriff: "Ultimatum", definition: "Forderung mit Frist – sonst gibt es Folgen" },
            { id: "d06", begriff: "Stellungskrieg", definition: "Krieg in Schützengräben, die Front bewegt sich kaum" },
            { id: "d07", begriff: "Materialschlacht", definition: "Riesige Mengen Munition und Geschütze, riesige Verluste" },
            { id: "d08", begriff: "Heimatfront", definition: "Die Menschen zu Hause arbeiten für den Krieg und hungern" },
            { id: "d09", begriff: "Novemberrevolution", definition: "Aufstand von Matrosen, Soldaten und Arbeitern 1918" },
            { id: "d10", begriff: "Waffenstillstand", definition: "Die Kämpfe hören auf, aber noch kein Friedensvertrag" },
            { id: "d11", begriff: "Reparationen", definition: "Geld, das Deutschland für die Kriegsschäden zahlen muss" },
            { id: "d12", begriff: "Völkerbund", definition: "Bund der Staaten, der neue Kriege verhindern soll" },
          ],
        },
        {
          nr: 48, typ: "quellen", eyebrow: "Quellenverzeichnis", titel: "Meine Quellen",
          hinweis: "Trage mindestens zwei verlässliche Quellen ein, die du benutzt hast. Schreibe kurz, warum du sie für verlässlich hältst.",
          min: 2,
        },
        {
          nr: "T", typ: "transfer", eyebrow: "Transfer · Beurteilen", titel: "Urkatastrophe des 20. Jahrhunderts?",
          kontext: "Klasse 9 Geschichte, Transferaufgabe zum ganzen Arbeitsblatt. Begriffe: Ursachen, Auslöser, Verlauf, Kriegsende, Folgen, Versailler Vertrag, Weimarer Republik, Zweiter Weltkrieg, George F. Kennan.",
          aufgabe: "Der Historiker George F. Kennan nannte den Ersten Weltkrieg die „Urkatastrophe des 20. Jahrhunderts“. Erkläre, was er damit meinen könnte. Beurteile: Stimmst du ihm zu? Nutze Ursachen, Verlauf und Folgen – in der richtigen zeitlichen Reihenfolge.",
          begriffe: ["Ursachen", "Verlauf", "Folgen", "Versailler Vertrag", "Weimarer Republik", "Zweiter Weltkrieg"],
          min: 200,
        },
      ],
    },
  ],
};
