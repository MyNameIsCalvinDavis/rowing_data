import sys

"""
Utilization 2(U2 50% 2K Watts) O2 Continuous 30 – 60 min, 18 - 20 spm
Utilization 1 (U1 60% 2K Watts) O2 LA Continuous work or Long interval 10 – 30 min, 20 - 24 spm
Anaerobic Threshold (AT 70% 2K Watts) LA O2 Long interval 5 – 20 min, 24 - 28 spm
Transportation(TN 105% 2K Watts) ATP-PC LA O2 Moderate interval 90 sec - 5 min, 28 - 32 spm
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

# https://www.c2forum.com/viewtopic.php?t=11429
cats = ["UT2", "UT1", "AT", "TR"]
wo_l = ["30-60m", "10-30m", "5-20m", "1.5-5m"]
SR = ["18-20", "20-24", "24-28", "28-32"]
paces_s = [22, 18, 99, 99] # 2K-X
paces_p = [0.55, 0.65, 0.75, 1.05] # 2K*X

s = "{:5} {:^5} | {:^10}     {:^10}     {:^6}\n".format("CAT", "SR", "2K-X", "%2KW", "WL")
s += "======================================================\n"
for i,_ in enumerate(cats):
    s += "{:5} {:5} | {:10} ... {:10} ... {:6}\n".format(cats[i], SR[i],
        "({}) ".format(paces_s[i]) + s_to_fm(m_to_s(P) + paces_s[i]),
        "({:3}%) ".format(int(paces_p[i]*100)) + watts_to_pace(W * paces_p[i]),
        wo_l[i]
    )

print(s)
