import numpy as np
import csv

feature_names = ['cons',
                 'son',
                 'syll',
                 'labial',
                 'round',
                 'coronal',
                 'ant',
                 'distrib',
                 'dorsal',
                 'high',
                 'low',
                 'back',
                 'tense',
                 'phrngl',
                 'atr',
                 'voice',
                 's.g.',
                 'c.g.',
                 'cont.',
                 'strident',
                 'lateral',
                 'del rel',
                 'nasal']

# generating the feature vectors
ipa_data = {}
with open('ipa_features.csv', encoding='utf8') as csvfile:
    rows = csv.DictReader(csvfile, delimiter=',', quotechar="'")
    
    ipa_names = []
    ipa_features = []
    for r in rows:      
        # build the feture vector.
        newFeature = np.zeros(len(feature_names))
        for f in range(len(feature_names)):
            newFeature[f] = float(r[feature_names[f]])

        ipa_names.append(r['ipa'])
        ipa_features.append(newFeature)
    
    feature_name_count = len(feature_names)
    ipa_data['names'] = ipa_names
    ipa_data['features'] = np.array(ipa_features)