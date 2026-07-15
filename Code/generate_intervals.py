from fractions import Fraction
from pathlib import Path

OUT = Path('/mnt/data/metriq_second_jones_paper/cantorval_intervals.tex')

def digits(n):
    return [0, 4*n+18, 8*n+17, 12*n+35]

def tail(n):
    return Fraction(4*n+17, 4**n)

def partial_sums(N):
    sums = {Fraction(0)}
    for n in range(1, N+1):
        vals = [Fraction(d, 4**n) for d in digits(n)]
        sums = {s+v for s in sums for v in vals}
    return sorted(sums)

def merge(intervals):
    out=[]
    for a,b in sorted(intervals):
        if not out or a > out[-1][1]:
            out.append([a,b])
        elif b > out[-1][1]:
            out[-1][1]=b
    return out

levels = {}
for N in range(1,6):
    r=tail(N)
    levels[N]=merge([(s,s+r) for s in partial_sums(N)])

colors={1:'MetriqMint',2:'MetriqSignal',3:'MetriqEmerald',4:'MetriqTealLight',5:'MetriqBlue'}
lines=[]
lines.append('% Auto-generated exact outer approximations U_N for the constructed achievement set.')
lines.append('% Coordinates are normalized by the total sum 17.')
lines.append('\\newcommand{\\DrawCantorvalLevelsCover}{%')
lines.append('  \\begin{scope}[x=17.0cm,y=0.78cm]')
for N in range(1,6):
    y=6-N
    lines.append(f'    \\draw[white,opacity=0.10,line width=0.35pt] (0,{y}) -- (1,{y});')
    lines.append(f'    \\node[anchor=east,font=\\sffamily\\fontsize{{7.3}}{{8.4}}\\selectfont,white,opacity=0.55] at (-0.018,{y}) {{$U_{N}$}};')
    for a,b in levels[N]:
        x1=float(a/Fraction(17)); x2=float(b/Fraction(17))
        lines.append(f'    \\draw[{colors[N]},line width=4.7pt,line cap=round,opacity=0.96] ({x1:.7f},{y}) -- ({x2:.7f},{y});')
lines.append('    \\node[anchor=west,font=\\sffamily\\fontsize{6.6}{7.6}\\selectfont,white,opacity=0.42] at (0,-0.18) {$0$};')
lines.append('    \\node[anchor=east,font=\\sffamily\\fontsize{6.6}{7.6}\\selectfont,white,opacity=0.42] at (1,-0.18) {$17$};')
lines.append('  \\end{scope}%')
lines.append('}')
lines.append('')
lines.append('\\newcommand{\\DrawCantorvalLevelsBody}{%')
lines.append('  \\begin{scope}[x=14.8cm,y=0.57cm]')
for N in range(1,6):
    y=6-N
    lines.append(f'    \\draw[MetriqCharcoal,opacity=0.12,line width=0.35pt] (0,{y}) -- (1,{y});')
    lines.append(f'    \\node[anchor=east,font=\\sffamily\\scriptsize,MetriqMuted] at (-0.018,{y}) {{$U_{N}$}};')
    for a,b in levels[N]:
        x1=float(a/Fraction(17)); x2=float(b/Fraction(17))
        lines.append(f'    \\draw[{colors[N]},line width=3.2pt,line cap=round,opacity=0.94] ({x1:.7f},{y}) -- ({x2:.7f},{y});')
lines.append('    \\node[anchor=west,font=\\sffamily\\scriptsize,MetriqMuted] at (0,-0.28) {$0$};')
lines.append('    \\node[anchor=east,font=\\sffamily\\scriptsize,MetriqMuted] at (1,-0.28) {$17$};')
lines.append('  \\end{scope}%')
lines.append('}')
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote {OUT} with interval counts: ' + ', '.join(f'U_{n}={len(levels[n])}' for n in levels))
