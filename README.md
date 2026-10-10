# Empty Chair Index

Most deliberation tools count voices. Empty Chair Index asks a different question: **which necessary perspective has not yet been represented?**

A convener freezes one bounded question and three to six named roles. Each testimony is compared by GenLayer validators against every role and the chairs already filled. Consensus returns one exact, closed result: `FILLS`, `OVERLAP`, or `OUTSIDE`. Only `FILLS` changes the chamber. The hearing can be sealed by anyone once no chair remains empty.

## Why the contract matters

The semantic judgment cannot be replaced with a keyword rule: a statement may express the resident perspective without saying “resident,” or repeat an operator concern using different words. Validators resolve that meaning; the contract constrains the result and performs every state mutation deterministically.

Replay protection hashes normalized testimony before consensus, including attempts from a different wallet. Unchecked model prose never enters storage. There is no owner-only escape hatch that can strand a complete hearing.

## Lifecycle

1. `convene` freezes the question and role vocabulary.
2. `offer_testimony` obtains the exact semantic relation and role.
3. A `FILLS` verdict occupies one chair; other verdicts preserve the chamber.
4. `seal_hearing` closes a fully represented chamber.
5. `get_hearing` and `get_testimony` expose the complete attributable record.

## Review map

- Contract: `contracts/contract.py`
- Browser dApp: `docs/index.html`
- Contract invariants: `tests/test_contract.py`
- UI/lifecycle checks: `tests/test_surface.py`
- Deployment and source verification: `scripts/`
- Live lifecycle proof: `evidence/live-run.json`

The bundled fixture is explicitly operator-controlled and exists to demonstrate chair filling, overlap handling, cross-wallet replay rejection, finality, and sealing. It is not represented as independent public testimony.
