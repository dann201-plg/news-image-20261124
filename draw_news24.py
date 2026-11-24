"""Draw the 24 November 2026 world-news image (1024x1024 PNG).

Fresh build for the news-image-20261124 bounty. All 50 stories were verified
as happening or first reported on Tuesday 24 November 2026.
Layout: header date band, one main story, four featured stories, then
45 one-line stories in three columns, plus a footer date-check line.
Run:  python3 draw_news24.py   (writes entry.png beside this file)
"""

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (255, 255, 255)
NAVY = (13, 27, 62)
NAVY2 = (24, 48, 105)
GOLD = (201, 162, 39)
INK = (17, 24, 39)
MUTED = (90, 98, 115)
RULE = (214, 219, 228)
RED = (176, 32, 32)

def font(bold, size):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p, size)

F_DATE = font(True, 44)
F_SUB = font(False, 18)
F_BADGE = font(True, 17)
F_MAIN = font(True, 29)
F_MAIN_SUB = font(False, 17)
F_FEAT = font(True, 17)
F_FEAT_SUB = font(False, 14)
F_ONE = font(False, 12)
F_ONE_B = font(True, 12)
F_FOOT = font(False, 12)
F_FOOT_B = font(True, 12)

MAIN = ("Asian stocks soar as Nvidia relief lifts chip shares",
        "Nikkei +5%, KOSPI +7.4%, Taiwan +9% in the biggest regional rally of the day.")

FEATURED = [
    ("Poland scrambles jets as Russian drone enters airspace",
     "Warsaw activates air defences after a drone briefly crosses in during a Russian attack on Ukraine."),
    ("Israeli strike kills 3 at Gaza police post in Khan Younis",
     "An airstrike kills at least three Palestinians near a police post in southern Gaza."),
    ("Russian attack kills 2, wounds 22 in Zaporizhzhia",
     "An overnight Russian attack on the Ukrainian city kills two people and wounds 22."),
    ("South Korea on alert as Russian jets enter its ADIZ",
     "Seoul issues an air-raid alert after Russian aircraft enter its air defence zone."),
]

ONE_LINERS = [
    ("UKRAINE", "Port attacks threaten food security"),
    ("EUROPE", "Greece builds Ukraine-EU freight route"),
    ("GAZA", "ICRC: shelter curbs leave displaced cold"),
    ("CONGO", "Fighting disrupts Ebola response"),
    ("USA", "State Dept may axe whole embassies"),
    ("USA", "Trump approval hits 45%, term low"),
    ("USA", "Biden gives first speech since office"),
    ("CONGO", "Tshisekedi: process minerals at home"),
    ("GHANA", "Backs 2-year BECE ban for early pupils"),
    ("KENYA", "Bribes eat riders' daily pay"),
    ("NIGERIA", "Tinubu: power cuts hit me too"),
    ("NIGERIA", "Moves to end jail for suicide tries"),
    ("NIGERIA", "Boat tragedy toll rises to 29"),
    ("BURUNDI", "Cholera alert in two provinces"),
    ("BRAZIL", "Stocks fall as Petrobras payout weighs"),
    ("NVIDIA", "Huang faces US federal, state probes"),
    ("GERMANY", "Ifo business climate index released"),
    ("AI", "MemTensor launches 554B AI model"),
    ("CRYPTO", "Ethereum Foundation doubles security"),
    ("CHINA", "SANY unveils 240-ton e-mining truck"),
    ("AUTO", "Pirelli launches Cyber Tyre in US"),
    ("TECH", "Toshiba launches isolation amplifiers"),
    ("AI", "Ant Group open-sources medical AI"),
    ("WEB", "WP Engine extends agentic-web hosting"),
    ("TECH", "Lenovo named Leader in IDC study"),
    ("GHANA", "Tullow cuts forecast after $387m deal"),
    ("TECH", "Vuzix, Friends With Holograms AR deal"),
    ("SCIENCE", "NOAA maps chemistry of 140 rivers"),
    ("CLIMATE", "CO2 jumps in one of largest rises"),
    ("CLIMATE", "Saildrone aids hurricane forecasts"),
    ("CLIMATE", "MJO shifts warm conveyor belts"),
    ("SCIENCE", "AI tracks Atlantic Oscillation"),
    ("HEALTH", "Doctors trained on climate and health"),
    ("CRICKET", "India-NZ Wellington Test ends in draw"),
    ("CHESS", "Gukesh begins world title defence"),
    ("HOCKEY", "India win New Zealand series 1-0"),
    ("CRICKET", "Gill urges ICC to rethink saliva ban"),
    ("CRICKET", "Babar Azam hits 86 on ILT20 debut"),
    ("CRICKET", "Tickner ruled out of 2nd Test vs India"),
    ("BASKETBALL", "Ole Miss beats Clemson 82-62"),
    ("TV", "'Ted Lasso' renewed for Season 5"),
    ("FILM", "'The Odyssey' leads AARP Movies noms"),
    ("FILM", "BAFTA loses longtime sponsor EE"),
    ("MUSIC", "Ariana Grande teases tour concert film"),
    ("FILM", "Charlie Cox: 'too old' for Bond audition"),
]

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- header band ----
d.rectangle([0, 0, W, 112], fill=NAVY)
d.text((28, 14), "TUESDAY 24 NOVEMBER 2026", font=F_DATE, fill=(255, 255, 255))
d.text((28, 68), "World news in one image  ·  Every story from 24 November 2026", font=F_SUB, fill=(196, 205, 225))
badge = "50 STORIES"
bw = d.textlength(badge, font=F_BADGE) + 28
d.rounded_rectangle([W - bw - 28, 32, W - 28, 72], radius=20, fill=GOLD)
d.text((W - bw - 14, 41), badge, font=F_BADGE, fill=NAVY)

y = 112
# ---- main story ----
d.rectangle([0, y, W, y + 7], fill=GOLD)
y += 7
d.text((28, y + 10), "THE DAY IN ONE LINE", font=F_BADGE, fill=RED)
main_lines = textwrap.wrap(MAIN[0], width=44)
yy = y + 36
for ln in main_lines:
    d.text((28, yy), ln, font=F_MAIN, fill=INK)
    yy += 34
d.text((28, yy + 2), MAIN[1], font=F_MAIN_SUB, fill=MUTED)
y = yy + 38
d.line([28, y, W - 28, y], fill=RULE, width=2)

# ---- featured 2x2 ----
y += 14
d.text((28, y), "FEATURED", font=F_BADGE, fill=RED)
y += 28
col_w = (W - 56 - 24) // 2
row_h = 108
for i, (h, s) in enumerate(FEATURED):
    cx = 28 + (i % 2) * (col_w + 24)
    cy = y + (i // 2) * row_h
    d.rectangle([cx, cy, cx + 6, cy + 78], fill=NAVY2)
    hl = textwrap.wrap(h, width=36)
    ty = cy
    for ln in hl:
        d.text((cx + 16, ty), ln, font=F_FEAT, fill=INK)
        ty += 21
    sl = textwrap.wrap(s, width=46)
    for ln in sl[:2]:
        d.text((cx + 16, ty + 2), ln, font=F_FEAT_SUB, fill=MUTED)
        ty += 18
y += row_h * 2 + 4
d.line([28, y, W - 28, y], fill=RULE, width=2)

# ---- one-liners, 3 columns x 15 rows ----
y += 12
d.text((28, y), "THE REST OF THE DAY", font=F_BADGE, fill=RED)
y += 26
cols = 3
rows = 15
cw = (W - 56 - 2 * 20) // cols
rh = 23
for idx, (tag, txt) in enumerate(ONE_LINERS):
    c = idx // rows
    r = idx % rows
    x = 28 + c * (cw + 20)
    yy = y + r * rh
    d.text((x, yy), tag, font=F_ONE_B, fill=NAVY2)
    tw = d.textlength(tag, font=F_ONE_B)
    avail = cw - tw - 8
    t = txt
    while d.textlength(t, font=F_ONE) > avail and len(t) > 4:
        t = t[:-1]
    if t != txt:
        t = t[:-3] + "..."
    d.text((x + tw + 8, yy), t, font=F_ONE, fill=INK)
y += rows * rh + 8
d.line([28, y, W - 28, y], fill=RULE, width=2)

# ---- footer ----
y += 8
d.text((28, y), "50 STORIES  ·  7 REGIONS  ·  8 FIELDS", font=F_FOOT_B, fill=NAVY)
d.text((W - 28 - d.textlength("24 NOV 2026", font=F_FOOT_B), y), "24 NOV 2026", font=F_FOOT_B, fill=RED)
d.text((28, y + 20), "Date-check: stories first reported 21-23 Nov (COP31, Nvidia CEO return, Indonesia fire) were left out.",
       font=F_FOOT, fill=MUTED)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
import os
print("bytes:", os.path.getsize("entry.png"))
