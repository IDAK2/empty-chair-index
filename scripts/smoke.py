import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions
def calldata_compat(method=None,args=None,kwargs=None):
 out={}
 if method is not None: out['method']=method
 if args: out['args']=args
 if kwargs: out['kwargs']=kwargs
 return out
contract_actions.make_calldata_object=calldata_compat
ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/'accounts.env').read_text(); ADDRESS=json.loads((ROOT/'deployment.json').read_text())['contractAddress']
def owner(): return create_account(account_private_key=re.search(r'^ACCOUNT_7_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip())
def wait(c,tx,expect='SUCCESS'):
 receipt=c.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True); leaders=receipt.get('consensus_data',{}).get('leader_receipt')or[]; leaders=[leaders] if isinstance(leaders,dict) else leaders; executions=[str(x.get('execution_result','')).upper() for x in leaders]; assert receipt.get('result_name')=='MAJORITY_AGREE' and expect in executions; return receipt,executions
def write(c,name,args,expect='SUCCESS'):
 tx=c.write_contract(address=ADDRESS,function_name=name,args=args); print(name+'_tx='+str(tx),flush=True); _,executions=wait(c,tx,expect); return str(tx),executions
convener=create_client(chain=studionet,account=owner()); speakers=[create_client(chain=studionet,account=create_account()) for _ in range(4)]; stamp=str(int(time.time())); hid='CHAMBER-'+stamp; question='How should the public archive redesign evening access without excluding residents, frontline operators, or people who need accessible routes?'; roles=['RESIDENT','OPERATOR','ACCESS']; descriptions=['Residents who can only visit after work and need the archive to remain practically usable in the evening.','Frontline staff responsible for safe closing, manageable workload, and reliable evening procedures.','Visitors who need step-free routes, assistive navigation, and enough time to use the service independently.']; statements=['As a parent leaving work at six, I need at least one late evening each week to consult local records without losing wages.','The closing team needs a visible final-entry time and a two-person lockup procedure so evening access does not create unsafe lone work.','A wheelchair user needs a step-free entrance and enough time to navigate the archive independently before the desk closes.']; tx={}; tx['convene'],_=write(convener,'convene',[hid,question,roles,descriptions]); verdicts=[]
for i,(role,statement) in enumerate(zip(roles,statements)):
 tx[role],_=write(speakers[i],'offer_testimony',[hid,role+'-'+stamp,statement]); verdicts.append(convener.read_contract(address=ADDRESS,function_name='get_testimony',args=[role+'-'+stamp]))
before=convener.read_contract(address=ADDRESS,function_name='get_hearing',args=[hid]); replay=speakers[3].write_contract(address=ADDRESS,function_name='offer_testimony',args=[hid,'REPLAY-'+stamp,'  '+statements[0].lower()+'  ']); tx['replay']=str(replay); replay_receipt,replay_execution=wait(speakers[3],replay,'ERROR'); after=convener.read_contract(address=ADDRESS,function_name='get_hearing',args=[hid]); assert before==after and {x['relation'] for x in verdicts}=={'FILLS'} and {x['role_id'] for x in verdicts}==set(roles); tx['seal'],_=write(speakers[3],'seal_hearing',[hid]); final=convener.read_contract(address=ADDRESS,function_name='get_hearing',args=[hid]); assert final['state']=='SEALED' and all(x['testimony_id'] for x in final['chairs']); proof={'hearingId':hid,'contract':ADDRESS,'transactions':tx,'placements':[{'id':x['id'],'relation':x['relation'],'role':x['role_id']} for x in verdicts],'final':final,'normalizedReplay':{'consensus':replay_receipt.get('result_name'),'execution':replay_execution,'stateUnchanged':before==after},'fixtureDisclosure':'Statements and wallets are operator-controlled fixtures used to prove bounded semantic placement, cross-wallet replay rejection, and permissionless sealing.'}; (ROOT/'evidence').mkdir(exist_ok=True); (ROOT/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n'); print(json.dumps(proof,indent=2))
