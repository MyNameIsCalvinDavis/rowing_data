import sys
from prettytable import PrettyTable

"""
Utilization 2(U2 50% 2K Watts) O2 Continuous 30 – 60 min, 18 - 20 spm
Utilization 1 (U1 60% 2K Watts) O2 LA Continuous work or Long interval 10 – 30 min, 20 - 24 spm
    2x15' 1x30' 3x15'
Anaerobic Threshold (AT 70% 2K Watts) LA O2 Long interval 5 – 20 min, 24 - 28 spm
    6x2k 3r     4x8' 4r     2x14' 8r
Transportation(TN 105% 2K Watts) ATP-PC LA O2 Moderate interval 90 sec - 5 min, 28 - 32 spm
    4x4'3r    5x1000 3r     6x2:30' 3r   15x3' 1r 
"""


def s_to_fm(s):
    m = int(s / 60)
    s = int(s - (m*60))
    return str(m) + ":" + str(s).zfill(2)

def m_to_s(m):
    time_s = int(m[0]) * 60 + int(m[2:])
    return time_s

def pace_to_watts(p):
    time_s = m_to_s(p)
    pace_s = time_s / 500

    # www.concept2.com/indoor-rowers/training/calculators/watts-calculator
    W = 2.80 / (pace_s**3)
    return round(W, 2)

def watts_to_pace(w):
    P = ((2.80 / w)**0.3333) * 500
    return s_to_fm(P)


W = pace_to_watts(sys.argv[1])
P = sys.argv[1]

x = PrettyTable()

# https://www.c2forum.com/viewtopic.php?t=11429
paces_pl = [0.50, 0.60, 0.70, 0.80, 0.60, 0.65, 0.70, 0.75]
paces_ph = [0.60, 0.70, 0.80, 1.05, 0.65, 0.70, 0.75, 0.80]
paces_a = [watts_to_pace(round((x+y)/2,2)*W) for x,y in zip(paces_pl, paces_ph)]

combo_pace_l = [watts_to_pace(x*W) for x in paces_pl]
combo_pace_h = [watts_to_pace(x*W) for x in paces_ph]
combo_p = []
combo_pace_num = []

# Create X%-Y% strings
for l,h in zip(paces_pl, paces_ph):
    combo_p.append(str(int(l*100)) + "-" + str(int(h*100)))

# Create X:XX-Y:YY strings
for l,h in zip(combo_pace_l, combo_pace_h):
    combo_pace_num.append(l + "-" + h)


x.add_column("CAT", ["UT2", "UT1", "AT", "TR", "MP", "HMP", "10K", "5K"])
x.add_column("%", combo_p)
x.add_column("Pace", combo_pace_num)
x.add_column("Pace Avg", paces_a)

for n, l in enumerate(x.get_string().split('\n')):
    if n == 7:
        print("+-----+--------+-----------+----------+")
    print(l)
