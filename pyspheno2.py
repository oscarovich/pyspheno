#!/usr/bin/env python

import numpy as np
import commands
import pyslha
import sys

##To write rp parameters and neutrino 
datos= open('solutions.out','w')
for m0 in [200, 500, 700, 1000]:
    print "m0=", m0
    for tanb in [3, 10, 30, 50]:
        print "tanb=", tanb
        LesHouchesFit,decaysFit=pyslha.readSLHAFile('LesHouches_FIT_ON.in')
        LesHouchesFit['MINPAR'].entries[1]=m0 #M0
        LesHouchesFit['MINPAR'].entries[3]=1.0*tanb #tanbeta
        LesHouchesFit2={'AMODSEL':LesHouchesFit['MODSEL'],'BSMINPUTS':LesHouchesFit['SMINPUTS'],'CMINPAR':LesHouchesFit['MINPAR'],'GSPhenoInput':LesHouchesFit['SPHENOINPUT']}
        pyslha.writeSLHAFile('LesHouches.in',LesHouchesFit2,decaysFit)
#        sys.exit(0)
## Run Spheno with lesHouches.in
#    commands.getoutput('cp LesHouches.in.neutrinofits-ON LesHouches.in')
        commands.getoutput('./bin/SPheno')
##Determine mu
        spc,decays=pyslha.readSLHAFile('SPheno.spc')
        veps=np.asarray(spc['RVKAPPA'].entries.values())
        vsnvev=np.asarray(spc['RVSNVEV'].entries.values())
        vlam=np.asarray(spc['SPHENORP'].entries.values()[0:3])
        vd=spc['SPHENORP'].entries[15]
        mu=((vlam-vd*veps)/vsnvev)[0]
##begin the iterations 
        LesHouches,decays=pyslha.readSLHAFile('LesHouches_MASS.in')
        print "begin loop"
        for i in range(1,100):
            if i%10==0:
                print "i=",i
##random generation of epsilon_i and lambda_i
            sgn=(-1)**np.random.random_integers(1,2,3)
            sgn2=(-1)**np.random.random_integers(1,2,3)
            pcnt=np.random.uniform(0.9,1.1,3)
            pcnt2=np.random.uniform(0.9,1.1,3)
            epsi=veps*pcnt
            lambi=vlam*pcnt2
            vi=(lambi-epsi*vd)/mu
##  Reading LesHouches_MASS.in 
            LesHouches['RVKAPPAIN'].entries[1]=epsi[0]
            LesHouches['RVKAPPAIN'].entries[2]=epsi[1]
            LesHouches['RVKAPPAIN'].entries[3]=epsi[2]
            LesHouches['RVSNVEVIN'].entries[1]=vi[0]
            LesHouches['RVSNVEVIN'].entries[2]=vi[1]
            LesHouches['RVSNVEVIN'].entries[3]=vi[2]
            LesHouches['MINPAR'].entries[1]=m0 #M0
            LesHouches['MINPAR'].entries[3]=1.0*tanb #tanbeta
## To write LesHouches.in in the right order.
            LesHouches2={'AMODSEL':LesHouches['MODSEL'],'BSMINPUTS':LesHouches['SMINPUTS'],'CMINPAR':LesHouches['MINPAR'],'DEXTPAR':LesHouches['EXTPAR'],'ERVSNVEVIN':LesHouches['RVSNVEVIN'],'FRVKAPPAIN':LesHouches['RVKAPPAIN'],'GSPhenoInput':LesHouches['SPHENOINPUT']}
            pyslha.writeSLHAFile('LesHouches.in',LesHouches2,decays)
##                sys.exit(0)
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
##  Checking neutrinosbounds at 3 sigma   
            if (Delta2m32 > 2.18e-3 and Delta2m32 < 2.73e-3 and t223 > 0.6393e0 and t223 <1.7777e0 and Delta2m21 > 7.09e-5 and Delta2m21 < 8.19e-5 and t212 > 0.3698e0 and t212 < 0.5625e0) and s213 > 0.0e0 and s213 < 0.035e0:
                print "slt found at i=",i
                print >> datos, Delta2m32, t223, Delta2m21,t212,s213, lambi[0], lambi[1], lambi[2], epsi[0], epsi[1], epsi[2],m0,tanb
#
datos.close()

