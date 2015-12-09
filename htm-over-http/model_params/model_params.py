MODEL_PARAMS = {
  "inferenceArgs": {
    "predictionSteps": [1],
    "predictedField": "c1",
    "inputPredictedField": "auto"
  },
  "modelConfig": {
    "aggregationInfo": {
      "seconds": 0,
      "fields": [],
      "months": 0,
      "days": 0,
      "years": 0,
      "hours": 0,
      "microseconds": 0,
      "weeks": 0,
      "minutes": 0,
      "milliseconds": 0
    },
    "model": "CLA",
    "version": 1,
    "predictAheadTime": None,
    "modelParams": {
      "sensorParams": {
        "verbosity": 0,
        "encoders": {
          "c0_dayOfWeek": None,
          "c0_timeOfDay": {
            "type": "DateEncoder",
            "timeOfDay": [21, 9.4912233474773693],
            "fieldname": "c0",
            "name": "c0"
          },
          "c1": {
            "name": "c1",
            "fieldname": "c1",
              'resolution': 21,
            #"numBuckets": 114.0,
            "seed": 42,
            "type": "RandomDistributedScalarEncoder"
          },
          "c0_weekend": None
        },
        "sensorAutoReset": None
      },
      "spParams": {
        "spatialImp": "cpp",
        "columnCount": 2048,
        "synPermInactiveDec": 0.0005,
        "inputWidth": 0,
        "spVerbosity": 0,
        "synPermActiveInc": 0.0015,
        "synPermConnected": 0.10000000000000001,
        "numActiveColumnsPerInhArea": 40,
        "seed": 1956,
        "potentialPct": 0.8,
        "globalInhibition": 1,
        "maxBoost": 1.0
      },
      "trainSPNetOnlyIfRequested": False,
      "clParams": {
        "alpha": 0.035828933612157998,
        "regionName": "CLAClassifierRegion",
        "steps": "1",
        "clVerbosity": 0
      },
      "tpParams": {
        "columnCount": 2048,
        "activationThreshold": 13,
        "pamLength": 3,
        "cellsPerColumn": 32,
        "permanenceInc": 0.10000000000000001,
        "minThreshold": 10,
        "verbosity": 0,
        "maxSynapsesPerSegment": 32,
        "outputType": "normal",
        "globalDecay": 0.0,
        "initialPerm": 0.20999999999999999,
        "permanenceDec": 0.10000000000000001,
        "seed": 1960,
        "maxAge": 0,
        "newSynapseCount": 20,
        "maxSegmentsPerCell": 128,
        "temporalImp": "cpp",
        "inputWidth": 2048
      },
      "anomalyParams": {
        "anomalyCacheRecords": None,
        "autoDetectThreshold": None,
        "autoDetectWaitRecords": 5030
      },
      "spEnable": True,
      "inferenceType": "TemporalAnomaly",
      "tpEnable": True,
      "clEnable": False
    }
  }
}
