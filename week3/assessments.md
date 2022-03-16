Week 3 Self Assessment

For classifying product names to categories:

- What precision (P@1) were you able to achieve?

Initial data set results:

N 9649

P@1 0.638

R@1 0.638

After level 1:

N 10000

P@1 0.917

R@1 0.917

- What fastText parameters did you use?
    - -epoch 50 -wordNgrams 2 -lr 2
- How did you transform the product names?
    - Lower case, remove punctuations, english stemmer ignoring stopwords
- How did you prune infrequent category labels, and how did that affect your precision?
    - 10 products min
- How did you prune the category tree, and how did that affect your precision?
    - Lowest category, up to 2 level deep

For deriving synonyms from content:

- What 20 tokens did you use for evaluation?
    - Product Types
        - Video Games
        - MP3 Players
        - Netbook
        - Software
        - Video Game Systems
    - Brands
        - Sony
        - Linksys
        - BlackBerry
        - Timbuk2
        - Minolta
    - Models
        - PlayStation
        - Freedom
        - A3X126-14
        - Series 7
        - Pentium
    - Attributes
        - Black
        - 7200 rpm
        - DVD-ROM
        - Megapixels
        - Waterproof
- What fastText parameters did you use?
    - -epoch 50 -wordNgrams 2 -lr 2
- How did you transform the product names?
    - Lower case, remove punctuations, english stemmer ignoring stopwords
- What threshold score did you use?
    - 20
- What synonyms did you obtain for those tokens?

| phrase | synonyms |
| --- | --- |
| video games | game 0.955429xbox 0.954766gamecub 0.950759time 0.941027schedule 0.935253trademark 0.933038360 0.921046adv 0.911705guide 0.906329ps2 0.905788auto 0.964992- 0.961126multimedia 0.954698squad 0.946716d 0.94638personal 0.945802sound 0.943897dj 0.936446disney 0.934535hi 0.929394 |
| mp3 players | playback 0.973037fm 0.959114jvc 0.957676ipod™ 0.950975dock 0.949324xm 0.94781radio 0.947375deck 0.937564tuner 0.928265alarm 0.924365player 0.978422play 0.963041playback 0.959424dvd 0.958018progressive 0.94686scan 0.941361cd 0.928929fm 0.921351mp3 0.916892 hd 0.916726 |
| netbook | duo 0.973653vaio 0.973472notebook 0.972227processor 0.971871atom™ 0.9691151tb 0.964078x2 0.96344320gb 0.963314amd 0.963294 athlon™ 0.961725 |
| software | sandisk 0.954046fire 0.948551b 0.948295my 0.948201mini 0.942064lowepro 0.939808targus 0.936278zildjian 0.933933extreme 0.933437 e 0.932127 |
| video game system | auto 0.964992- 0.961126multimedia 0.954698squad 0.946716d 0.94638personal 0.945802sound 0.943897dj 0.936446disney 0.934535hi 0.929394gamecub 0.964857games 0.955429adv 0.950582xbox 0.946319boy 0.944405time 0.944338of 0.920691guide 0.916368nintendo 0.911128box 0.901079system 0.99771cable 0.910066answering 0.890944expandable 0.869479dect 0.855526cordless 0.853931bridgeable 0.843695panasonic 0.834147wine 0.818342 philips 0.81717 |
| sony | camcorder 0.956025camcord 0.938531handycam 0.934659hd 0.897872recorder 0.894298record 0.887327kodak 0.883001jvc 0.880642green 0.87937855 0.877782 |
| linksys | link 0.980107802 0.975195n 0.964922netgear 0.964775ethernet 0.956373switch 0.954281router 0.94506squad 0.924115port 0.913395 network 0.89075 |
| blackberry | mobile 0.98255no 0.969793unlocked 0.967595nokia 0.966943motorola 0.96582htc 0.963828verizon 0.959326phon 0.958562phone 0.958115phones 0.954775 |
| timbuk2 | time 0.993062gamecub 0.966835box 0.96225xbox 0.960518schedule 0.953731games 0.951435of 0.951424adv 0.95001man 0.946343 watch 0.94547 |
| minolta | minnesota 0.976659logitech 0.973556targus 0.973061optical 0.972159texas 0.968558chicago 0.967414executive 0.966821chrom 0.966056mint 0.958298deluxe 0.956205 |
| playstation | xbox 0.936669nfl 0.93408ps2 0.929818nintendo 0.921699window 0.913535psp 0.912997360 0.909774mad 0.908145world 0.90793 adv 0.906783 |
| freedom | free 0.996934frost 0.990467frigidaire 0.989345freezer 0.986068maytag 0.981108whirlpool 0.976773bisqu 0.976171bottom 0.97503bisque 0.97389 gallery 0.967065 |
| a3x126-14 | 14 0.976569pentax 0.967953k 0.966027secure 0.965981silv 0.94083finepix 0.939311megapixel 0.935971stylus 0.933657olympus 0.930818fujifilm 0.92856 |
| series 7 | drop 0.939895call 0.914269drum 0.90371grill 0.899737metallic 0.890815gibson 0.885895ball 0.88539pedal 0.880876gaming 0.878976convertible 0.8716559 0.959234super 0.9189228 0.917385plus 0.910367dryer 0.9076315 0.899707cycle 0.89426cu 0.882404ft 0.86704 11 0.859834 |
| pentium | i5 0.993168aspire 0.993034i7 0.9911071tb 0.990304x2 0.990247i3 0.98933athlon™ 0.988997processor 0.98443duo 0.983561 320gb 0.983015 |
| black | blackberry 0.884059microphon 0.858242clear 0.853376orang 0.851067phon 0.824443travel 0.821195microphone 0.820211series 0.810985glove 0.80971 cell 0.808234 |
| 7200 rpm | 50 0.89177360 0.884002hdmi 0.875415smart 0.871842entertainment 0.870739choice 0.857345dynex 0.852463sharp 0.85056dynex™ 0.848853100 0.848351ball 0.0810091full 0.0801502size 0.0785739single 0.078477acoustic 0.0752418guitar 0.0711067electric 0.0676694tall 0.066552guitars 0.0638283 string 0.0631635 |
| dvd-rom | g 0.936009hi 0.933106gp 0.924075disc 0.918543recorder 0.913105disney 0.910302zildjian 0.90932record 0.909207party 0.905369 dvd 0.900411 |
| megapixels | megapixel 0.998213fujifilm 0.993442coolpix 0.988186finepix 0.9870132mp 0.983498eos 0.9825531mp 0.98239816 0.981659zoom 0.98101 0mp 0.980375 |
| waterproof | water 0.973162ice 0.963692door 0.959183thru 0.952971french 0.943032by 0.941187side 0.940388counter 0.92895depth 0.925182 refrigerator 0.918266 |

For integrating synonyms with search:

- How did you transform the product names (if different than previously)?
    - same
- What threshold score did you use?
    - .9
- Were you able to find the additional results by matching synonyms?
    - Yes

For classifying reviews:

- What precision (P@1) were you able to achieve?
- What fastText parameters did you use?
- How did you transform the review content?
- What else did you try and learn?