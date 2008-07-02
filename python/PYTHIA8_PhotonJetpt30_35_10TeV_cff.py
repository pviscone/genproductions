import FWCore.ParameterSet.Config as cms

source = cms.Source("Pythia8Source",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.59),
    comEnergy = cms.untracked.double(10000.0),
    crossSection = cms.untracked.double(13000.),
    PythiaParameters = cms.PSet(
    processParameters = cms.vstring('Main:timesAllowErrors    = 10000',
                                    'ParticleDecays:limitTau0 = on',              # Decay those unstable particles
                                    'ParticleDecays:tau0Max   = 10.',             # for which _nominal_ proper lifetime < 10 mm
                                    'PromptPhoton:all         = on',
                                    'PhaseSpace:pTHatMin      = 30.',
                                    'PhaseSpace:pTHatMax      = 35.'),
    # This is a vector of ParameterSet names to be read, in this order
    parameterSets = cms.vstring('processParameters')
    )
                    )

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA8_PhotonJetpt30_35_10TeV_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA8 Photon + Jet for 30 < pT < 35 at 10TeV')
    )

photonfilter = cms.EDFilter("MCSingleParticleFilter",
                          MaxEta = cms.untracked.vdouble(2.4),
                          MinEta = cms.untracked.vdouble(-2.4),
                          MinPt = cms.untracked.vdouble(15.0),
                          ParticleID = cms.untracked.vint32(22)
                          )
ProductionFilterSequence = cms.Sequence( photonfilter )
