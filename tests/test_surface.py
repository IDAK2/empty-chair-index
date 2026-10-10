from pathlib import Path
HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text(encoding='utf-8')

def test_complete_wallet_lifecycle():
 for token in ('CONVENE A CHAMBER','OFFER TESTIMONY','SEAL THE RECORD','FINALIZED','convene','offer_testimony','seal_hearing','get_hearing'):
  assert token in HTML

def test_chamber_identity_is_not_dashboard_template():
 for token in ('amphitheatre','chair-ring','podium','minutes-ribbon'):
  assert token in HTML
 assert '<table' not in HTML and '<pre' not in HTML

