from flask import Flask
from user import usr
from biodb import biodb, model as bio_model
from config import config

app = Flask(__name__)
app.register_blueprint(usr, url_prefix = '/usr')
app.register_blueprint(biodb, url_prefix = '/db')

print(
bio_model.Software.add(
    'PSORT',
    ['Open Source', 'Protien', 'FASTA'],
    'http://psort.hgc.jp/',
    'PSORT is a computer program for the prediction of protein localization sites in cells. It receives the information of an amino acid sequence and its source orgin, e.g., Gram-negative bacteria, as inputs. Then, it analyzes the input sequence by applying the stored rules for various sequence features of known protein sorting signals. Finally, it reports the possiblity for the input protein to be localized at each candidate site with additional information.',
    True,
    'N.A.'
    'Prashant'
)
)