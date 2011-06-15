#!/usr/bin/env python

import numpy as np
#call spheno with fit on to obtain mu and vd

import commands
#lsout=commands.getoutput('ls')
commands.getoutput('cp LesHouches.in.neutrinofits-ON LesHouches.in')
commands.getoutput('./bin/SPheno')
import pyslha
spc=pyslha.readSLHAFile('SPheno.spc')
eps=spc[0]['RVKAPPA']
eps1=eps.entries[1]
eps2=eps.entries[2]
eps3=eps.entries[3]
veps=np.array( [eps1,eps2,eps3] )
snvev=spc[0]['RVSNVEV']
snvev1=snvev.entries[1]
snvev2=snvev.entries[2]
snvev3=snvev.entries[3]
vsnvev=np.array( [snvev1,snvev2,snvev3] )
sphenorp=spc[0]['SPHENORP']
lamb1=sphenorp.entries[4]
lamb2=sphenorp.entries[5]
lamb3=sphenorp.entries[6]
vd=sphenorp.entries[15]
vu=sphenorp.entries[16]
vlamb=np.array( [lamb1,lamb2,lamb3] )
vmu=(vlamb-vd*veps)/vsnvev
mu=vmu[1]
#To write rp parameters
datos= open('solutions.out','w')
#begin for cycle
for i in range(1,10001):
    if i%100==0:
        print "i=",i
#random generation of epsilon_i and lambda_i
    sgn=(-1)**np.random.random_integers(1,2,3)
    epsi=np.random.uniform(-1,1,3)
    lambi=np.random.uniform(-1,1,3)
    vi=(lambi-epsi*vd)/mu
    salida = open('salida.out', 'w')
    print >> salida, lambi[0], lambi[1], lambi[2], epsi[0], epsi[1], epsi[2]
##to check with original SPheno.spc
#print >> salida, lamb1, lamb2, lamb3, eps1, eps1, eps2 
    salida.close()
    commands.getoutput('./main.sh')
    commands.getoutput('./bin/SPheno')
    nspc=pyslha.readSLHAFile('SPheno.spc')
    nsphenorp=nspc[0]['SPHENORP']
    m2atm=nsphenorp.entries[7]
    m2sol=nsphenorp.entries[8]
    t2atm=nsphenorp.entries[9]
    t2sol=nsphenorp.entries[10]
    s2cho=nsphenorp.entries[11]
    if (m2atm > 2.18e-3 and m2atm < 2.73e-3 and t2atm > 0.6393e0 and t2atm <1.7777e0 and m2sol > 7.09e-5 and m2sol < 8.19e-5 and t2sol > 0.3698e0 and t2sol < 0.5625e0) and s2cho > 0.0e0 and s2cho < 0.035e0:
        print "slt found at i=",i
        print >> datos, m2atm, t2atm, m2sol,t2sol,s2cho, lambi[0], lambi[1], lambi[2], epsi[0], epsi[1], epsi[2]
#
datos.close()
#3E-02 0.6 ! epsilon_1
#1.E-05 1. ! epsilon_2
#1.E-05 1. ! epsilon_3
#1.E-05 6.E-02 ! Lambda_1 = v_d epsilon_1 + mu v_L1
#3.E-02 7E-01 ! Lambda_2 = v_d epsilon_2 + mu v_L2
#3.E-02 7E-01 ! Lambda_3 = v_d epsilon_3 + mu v_L3


#
