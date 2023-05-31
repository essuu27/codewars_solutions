# https://www.codewars.com/kata/55d410c492e6ed767000004f

string = "90's c7rnh11l13 A16st19n, p24ckl28d b32tch36r yr m43ss46ng49r b53g g57str61p63b n67xt l72v74l l78gg81ngs l87st90cl93 m96d98t100t102103n try-h111rd V116c118. T122x124d126rmy g132str136p138b g142ntr146fy, m152h f156p 159rg162n164c 167nn170171 f174ng177rst181ch184 p187ckl191d v195g197n. S202203t205n s209st212213n215bl218 PBR&B c227rnh231l233 VHS. J241242n sh247rts 252ct255256lly b262tt265rs 269gh bl275g Int281ll284g286nts290291. Art297s299n K303ckst308rt311r DIY, f320x322323 cl327ch330 s333lv336337 l340-f343 f346347r l351k353. PBR&B Odd F367t369r371 373gh f378ng381rst385ch388 cr392y W396s And402rs405n ch410411 typ416wr419t421r 424Ph427n429 b432sp435k437 f440441r l445k447, Int453ll456g458nts462463 ph467t469 b472473th d478r480ct tr486d488. A492sth496t498c T502mblr P509rtl513nd XOXO sq524525d, synth v536r538l l542st545cl548 sk552t554b556557rd f562563r d567ll570r t574575st c580rnh584l586 Bl590591 B594ttl598 s601m603604t606cs."
outstr = ''

for i,j in enumerate(string):
    if j.lower() in ('a','e','i','o','u'):
        outstr += str(i+1)
    else:
        outstr += j

print(outstr)
