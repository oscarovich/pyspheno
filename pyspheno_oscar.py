#!/usr/bin/env python
'''Parallel Spheno'''
import numpy as np
import commands
import pyslha
## Run Spheno with lesHouches.in
commands.getoutput('cp LesHouches.in.neutrinofits-ON LesHouches.in')
commands.getoutput('./bin/SPheno')
##Determine mu
spc,decays=pyslha.readSLHAFile('SPheno.spc')
veps=np.asarray(spc['RVKAPPA'].entries.values())
vsnvev=np.asarray(spc['RVSNVEV'].entries.values())
vlam=np.asarray(spc['SPHENORP'].entries.values()[0:3])
vd=spc['SPHENORP'].entries[15]
mu=((vlam-vd*veps)/vsnvev)[0]
##To write rp parameters and neutrino 
datos= open('solutions.out','w')
#begin the iterations 
for i in range(1,11):
    if i%100==0:
        print "i=",i
#random generation of epsilon_i and lambda_i
#    sgn=(-1)**np.random.random_integers(1,2,3)
    sgn=np.array([1.0,1.0,-1.0])
#    epsi=np.random.uniform(-1,1,3)
#    epsi=np.array([np.random.uniform(3e-2,0.6),np.random.uniform(1e-5,1),np.random.uniform(1e-5,1)])*(-1)**np.random.random_integers(1,2,3)
    A1=np.log10([8e-2,8e-2,8e-2])    
    B1=np.log10([1e-1,1e-1,1e-1])    
    epsi=10**((B1-A1)*np.random.uniform(0,1,3)+A1)*sgn    
#    lambi=np.random.uniform(-1,1,3)
#    lambi=np.array([np.random.uniform(1e-5,6e-2),np.random.uniform(3e-2,7e-1),np.random.uniform(3e-2,7e-1)])*(-1)**np.random.random_integers(1,2,3)
    A2=np.log10([2e-3,5e-2,5e-2])    
    B2=np.log10([4e-3,7e-2,7e-2])    
    lambi=10**((B2-A2)*np.random.uniform(0,1,3)+A2)    
    vi=(lambi-epsi*vd)/mu
##  Reading LesHouches_MASS.in 
    LesHouches,decays=pyslha.readSLHAFile('LesHouches_MASS.in')
    LesHouches['RVKAPPAIN'].entries[1]=epsi[0]
    LesHouches['RVKAPPAIN'].entries[2]=epsi[1]
    LesHouches['RVKAPPAIN'].entries[3]=epsi[2]
    LesHouches['RVSNVEVIN'].entries[1]=vi[0]
    LesHouches['RVSNVEVIN'].entries[2]=vi[1]
    LesHouches['RVSNVEVIN'].entries[3]=vi[2]
##    To check with original SPheno.spc
#    LesHouches['RVKAPPAIN'].entries[1]=veps[0]
#    LesHouches['RVKAPPAIN'].entries[2]=veps[1]
#    LesHouches['RVKAPPAIN'].entries[3]=veps[2]
#    LesHouches['RVSNVEVIN'].entries[1]=vsnvev[0]
#    LesHouches['RVSNVEVIN'].entries[2]=vsnvev[1]
#    LesHouches['RVSNVEVIN'].entries[3]=vsnvev[2]
## To write LesHouches.in in the right order.
    LesHouches2={'AMODSEL':LesHouches['MODSEL'],'BSMINPUTS':LesHouches['SMINPUTS'],\
     'CMINPAR':LesHouches['MINPAR'],'DEXTPAR':LesHouches['EXTPAR'],\
     'ERVSNVEVIN':LesHouches['RVSNVEVIN'],'FRVKAPPAIN':LesHouches['RVKAPPAIN'],\
     'GSPhenoInput':LesHouches['SPHENOINPUT']}
    pyslha.writeSLHAFile('LesHouches.in',LesHouches2,decays)
    commands.getoutput('./bin/SPheno')
##  Reading the new SPheno.spc
    nspc=pyslha.readSLHAFile('SPheno.spc')
    nsphenorp=nspc[0]['SPHENORP']
##  nuetrino oscilation parameters 
    Delta2m32=nsphenorp.entries[7]
    Delta2m21=nsphenorp.entries[8]
    t223=nsphenorp.entries[9]
    t212=nsphenorp.entries[10]
    s213=nsphenorp.entries[11]
# Checking neutrinosbounds at 3 sigma   
    if (Delta2m32 > 2.18e-3 and Delta2m32 < 2.73e-3 and t223 > 0.6393e0 and t223 <1.7777e0\
     and Delta2m21 > 7.09e-5 and Delta2m21 < 8.19e-5 and t212 > 0.3698e0 and t212 < 0.5625e0)\
     and s213 > 0.0e0 and s213 < 0.056e0:
        print "slt found at i=",i
        print >> datos, Delta2m32, t223, Delta2m21,t212,s213,\
        lambi[0], lambi[1], lambi[2], epsi[0], epsi[1], epsi[2]
#
datos.close()
#3E-02 0.6 ! epsilon_1
#1.E-05 1. ! epsilon_2
#1.E-05 1. ! epsilon_3
#1.E-05 6.E-02 ! Lambda_1 = v_d epsilon_1 + mu v_L1
#3.E-02 7E-01 ! Lambda_2 = v_d epsilon_2 + mu v_L2
#3.E-02 7E-01 ! Lambda_3 = v_d epsilon_3 + mu v_L3


#
