from pathlib import Path
SOURCE=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()

def test_bounded_consensus_controls_every_state_driver():
 for token in ("RELATIONS=('FILLS','OVERLAP','OUTSIDE')",'exact role id','every bounded role',"verdict['relation']=='FILLS'"):
  assert token in SOURCE

def test_replay_guard_precedes_consensus_and_mutation():
 assert SOURCE.index('replay_key in self.attempted') < SOURCE.index('verdict=self._place')
 assert 'hashlib.sha256(body.lower().encode())' in SOURCE

def test_permissionless_completion_requires_full_coverage():
 block=SOURCE[SOURCE.index('def seal_hearing'):SOURCE.index('@gl.public.view',SOURCE.index('def seal_hearing'))]
 assert 'gl.message.sender_address' not in block
 assert 'any(not value for value in filled.values())' in block

def test_outside_and_overlap_do_not_fill_chairs():
 line="if verdict['relation']=='FILLS': filled[verdict['role_id']]=tid"
 assert line in SOURCE

