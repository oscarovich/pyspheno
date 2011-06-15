#!/usr/bin/env bash
echo "
Block MODSEL                 # Select model
 1    1                      # mSUGRA
Block SMINPUTS               # Standard Model inputs
 1   1.279340E+02       # alpha_rm^-1(M_Z), MSbar, SM
 2   1.166390E-05       # G_F, Fermi constant
 3   1.172000E-01       # alpha_s(MZ) SM MSbar
 4   9.118760E+01       # Z-boson pole mass
 5   4.250000E+00       # m_b(mb) SM MSbar
 6   1.727000E+02       # m_top(pole)
 7   1.777000E+00       # m_tau(pole)
Block MINPAR                 # Input parameters
 1   1000                # M0
 2   240                # m_1/2
 3   1.000000E+01       # tanb
 4   1                  # sign(mu)
 5  -1.000000E+02       # A0
Block EXTPAR                 # Gaugino masses
 1   240                # M_1  240
 2   240                # M_2  240 134 270
 3   240                # M_3  240 
Block RVSNVEVIN 		 # sneutrino vevs at Q
         1    $1        # v_L_1
         2    $2        # v_L_2
         3    $3        # v_L_3
Block RVKAPPAIN 		        # bilinear RP parameters at Q
         1     $4       # epsilon_1
         2     $5       # epsilon_2
         3     $6       # epsilon_3
Block SPhenoInput       # SPheno specific input
 1   0                  # error level
 2   0                  # if =1, then SPA conventions are used
11   1                  # calculate branching ratios
12   1.00000000E-06     # write only branching ratios larger than this value
21   0                  # calculate cross section 
22   5.00000000E+02     # cms energy in GeV
23   0.00000000E+00     # polarisation of incoming e- beam
24   0.00000000E+00     # polarisation of incoming e+ beam
25   0                  # if 0 no ISR is calculated, if 1 ISR is caculated
22   2.00000000E+03     # cms energy in GeV
23   0.00000000E+00     # polarisation of incoming e- beam
24   0.00000000E+00     # polarisation of incoming e+ beam
25   0                  # if 0 no ISR is calculated, if 1 ISR is caculated
26   1.00000000E-02     # write only cross sections larger than this value [fb]
31  -1.00000000E+00     # m_GUT, if < 0 than it determined via g_1=g_2
32   0                  # require strict unification g_1=g_2=g_3 if '1' is set
33  -1.00000000E+00     # Q_EWSB, if < 0 than  Q_EWSB=sqrt(m_~t1 m_~t2)
41   2.49520000E+00     # width of the Z-boson
42   2.11800000E+00     # width of the W-boson
51   5.10998900E-04     # electron mass
52   1.05658357E-01     # muon mass
61   2.00000000E+00     # scale where quark masses of first 2 gen. are defined
62   3.00000000E-03     # m_u(Q)
63   1.35000000E+00     # m_c(Q)
64   7.00000000E-03     # m_d(Q)
65   1.20000000E-01     # m_s(Q)
90   1                  # if R-parity is added " > LesHouches.in