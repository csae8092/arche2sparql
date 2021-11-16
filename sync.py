import os
from acdh_arche_pyutils.client import ArcheToTripleStore

BGUSER = os.environ.get('BGUSER')
BGPW = os.environ.get('BGPW')

triple_store = "https://arche-sparql.acdh-dev.oeaw.ac.at/sparql"
arche_endpoint = "https://arche.acdh.oeaw.ac.at/api/"
client = ArcheToTripleStore(
    triple_store, arche_endpoint=arche_endpoint,
    user=BGUSER, pw=BGPW 
)
client.delete_triples()
top_cols = client.post_all_resources()
