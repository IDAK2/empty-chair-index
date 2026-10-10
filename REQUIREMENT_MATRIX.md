# Requirement matrix

| Review requirement | Implementation | Executable evidence |
|---|---|---|
| Meaningful GenLayer use | Full testimony compared with every bounded role | `test_bounded_consensus_controls_every_state_driver` |
| Bounded validator result | Closed relation and exact role only | Contract guards + source-match proof |
| Replay safety | Normalized digest checked before consensus | `test_replay_guard_precedes_consensus_and_mutation` + live replay |
| Complete lifecycle | Convene, fill, inspect, seal | Browser demo + `live-run.json` |
| No stranded completion | Anyone may seal only after full coverage | `test_permissionless_completion_requires_full_coverage` |
| Genuine frontend | Wallet, writes, finalized receipts, reads | `test_complete_wallet_lifecycle` + browser QA |
