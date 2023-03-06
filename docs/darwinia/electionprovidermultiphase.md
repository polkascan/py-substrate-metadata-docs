
# ElectionProviderMultiPhase

---------
## Calls

---------
### set_emergency_election_result
Set a solution in the queue, to be handed out to the client of this pallet in the next
call to `ElectionProvider::elect`.

This can only be set by `T::ForceOrigin`, and only when the phase is `Emergency`.

The solution is not checked for any feasibility and is assumed to be trustworthy, as any
feasibility check itself can in principle cause the election process to fail (due to
memory/weight constrains).
#### Attributes
| Name | Type |
| -------- | -------- | 
| supports | `Supports<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'ElectionProviderMultiPhase', 'set_emergency_election_result', {
    'supports': [
        (
            'AccountId',
            {
                'total': 'u128',
                'voters': [
                    (
                        'AccountId',
                        'u128',
                    ),
                ],
            },
        ),
    ],
}
)
```

---------
### set_minimum_untrusted_score
Set a new value for `MinimumUntrustedScore`.

Dispatch origin must be aligned with `T::ForceOrigin`.

This check can be turned off by setting the value to `None`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_next_score | `Option<ElectionScore>` | 

#### Python
```python
call = substrate.compose_call(
    'ElectionProviderMultiPhase', 'set_minimum_untrusted_score', {
    'maybe_next_score': (
        None,
        '[u128; 3]',
    ),
}
)
```

---------
### submit
Submit a solution for the signed phase.

The dispatch origin fo this call must be __signed__.

The solution is potentially queued, based on the claimed score and processed at the end
of the signed phase.

A deposit is reserved and recorded for the solution. Based on the outcome, the solution
might be rewarded, slashed, or get all or a part of the deposit back.

\# &lt;weight&gt;
Queue size must be provided as witness data.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| raw_solution | `Box<RawSolution<SolutionOf<T>>>` | 
| num_signed_submissions | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ElectionProviderMultiPhase', 'submit', {
    'num_signed_submissions': 'u32',
    'raw_solution': {
        'round': 'u32',
        'score': '[u128; 3]',
        'solution': {
            'votes1': [('u32', 'u16')],
            'votes10': [
                (
                    'u32',
                    "[('u16', 'u16'); 9]",
                    'u16',
                ),
            ],
            'votes11': [
                (
                    'u32',
                    "[('u16', 'u16'); 10]",
                    'u16',
                ),
            ],
            'votes12': [
                (
                    'u32',
                    "[('u16', 'u16'); 11]",
                    'u16',
                ),
            ],
            'votes13': [
                (
                    'u32',
                    "[('u16', 'u16'); 12]",
                    'u16',
                ),
            ],
            'votes14': [
                (
                    'u32',
                    "[('u16', 'u16'); 13]",
                    'u16',
                ),
            ],
            'votes15': [
                (
                    'u32',
                    "[('u16', 'u16'); 14]",
                    'u16',
                ),
            ],
            'votes16': [
                (
                    'u32',
                    "[('u16', 'u16'); 15]",
                    'u16',
                ),
            ],
            'votes2': [
                ('u32', ('u16', 'u16'), 'u16'),
            ],
            'votes3': [
                (
                    'u32',
                    "[('u16', 'u16'); 2]",
                    'u16',
                ),
            ],
            'votes4': [
                (
                    'u32',
                    "[('u16', 'u16'); 3]",
                    'u16',
                ),
            ],
            'votes5': [
                (
                    'u32',
                    "[('u16', 'u16'); 4]",
                    'u16',
                ),
            ],
            'votes6': [
                (
                    'u32',
                    "[('u16', 'u16'); 5]",
                    'u16',
                ),
            ],
            'votes7': [
                (
                    'u32',
                    "[('u16', 'u16'); 6]",
                    'u16',
                ),
            ],
            'votes8': [
                (
                    'u32',
                    "[('u16', 'u16'); 7]",
                    'u16',
                ),
            ],
            'votes9': [
                (
                    'u32',
                    "[('u16', 'u16'); 8]",
                    'u16',
                ),
            ],
        },
    },
}
)
```

---------
### submit_unsigned
Submit a solution for the unsigned phase.

The dispatch origin fo this call must be __none__.

This submission is checked on the fly. Moreover, this unsigned solution is only
validated when submitted to the pool from the **local** node. Effectively, this means
that only active validators can submit this transaction when authoring a block (similar
to an inherent).

To prevent any incorrect solution (and thus wasted time/weight), this transaction will
panic if the solution submitted by the validator is invalid in any way, effectively
putting their authoring reward at risk.

No deposit or reward is associated with this submission.
#### Attributes
| Name | Type |
| -------- | -------- | 
| raw_solution | `Box<RawSolution<SolutionOf<T>>>` | 
| witness | `SolutionOrSnapshotSize` | 

#### Python
```python
call = substrate.compose_call(
    'ElectionProviderMultiPhase', 'submit_unsigned', {
    'raw_solution': {
        'round': 'u32',
        'score': '[u128; 3]',
        'solution': {
            'votes1': [('u32', 'u16')],
            'votes10': [
                (
                    'u32',
                    "[('u16', 'u16'); 9]",
                    'u16',
                ),
            ],
            'votes11': [
                (
                    'u32',
                    "[('u16', 'u16'); 10]",
                    'u16',
                ),
            ],
            'votes12': [
                (
                    'u32',
                    "[('u16', 'u16'); 11]",
                    'u16',
                ),
            ],
            'votes13': [
                (
                    'u32',
                    "[('u16', 'u16'); 12]",
                    'u16',
                ),
            ],
            'votes14': [
                (
                    'u32',
                    "[('u16', 'u16'); 13]",
                    'u16',
                ),
            ],
            'votes15': [
                (
                    'u32',
                    "[('u16', 'u16'); 14]",
                    'u16',
                ),
            ],
            'votes16': [
                (
                    'u32',
                    "[('u16', 'u16'); 15]",
                    'u16',
                ),
            ],
            'votes2': [
                ('u32', ('u16', 'u16'), 'u16'),
            ],
            'votes3': [
                (
                    'u32',
                    "[('u16', 'u16'); 2]",
                    'u16',
                ),
            ],
            'votes4': [
                (
                    'u32',
                    "[('u16', 'u16'); 3]",
                    'u16',
                ),
            ],
            'votes5': [
                (
                    'u32',
                    "[('u16', 'u16'); 4]",
                    'u16',
                ),
            ],
            'votes6': [
                (
                    'u32',
                    "[('u16', 'u16'); 5]",
                    'u16',
                ),
            ],
            'votes7': [
                (
                    'u32',
                    "[('u16', 'u16'); 6]",
                    'u16',
                ),
            ],
            'votes8': [
                (
                    'u32',
                    "[('u16', 'u16'); 7]",
                    'u16',
                ),
            ],
            'votes9': [
                (
                    'u32',
                    "[('u16', 'u16'); 8]",
                    'u16',
                ),
            ],
        },
    },
    'witness': {
        'targets': 'u32',
        'voters': 'u32',
    },
}
)
```

---------
## Events

---------
### ElectionFinalized
The election has been finalized, with `Some` of the given computation, or else if the
election failed, `None`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| election_compute | `Option<ElectionCompute>` | ```(None, ('OnChain', 'Signed', 'Unsigned', 'Fallback', 'Emergency'))```

---------
### Rewarded
An account has been rewarded for their signed submission being finalized.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `<T as frame_system::Config>::AccountId` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```

---------
### SignedPhaseStarted
The signed phase of the given round has started.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `u32` | ```u32```

---------
### Slashed
An account has been slashed for submitting an invalid signed submission.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `<T as frame_system::Config>::AccountId` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```

---------
### SolutionStored
A solution was stored with the given compute.

If the solution is signed, this means that it hasn&\#x27;t yet been processed. If the
solution is unsigned, this means that it has also been processed.

The `bool` is `true` when a previous solution was ejected to make room for this one.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| election_compute | `ElectionCompute` | ```('OnChain', 'Signed', 'Unsigned', 'Fallback', 'Emergency')```
| prev_ejected | `bool` | ```bool```

---------
### UnsignedPhaseStarted
The unsigned phase of the given round has started.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `u32` | ```u32```

---------
## Storage functions

---------
### CurrentPhase
 Current phase.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'CurrentPhase', []
)
```

#### Return value
```python
{'Emergency': None, 'Off': None, 'Signed': None, 'Unsigned': ('bool', 'u32')}
```
---------
### DesiredTargets
 Desired number of targets to elect for this round.

 Only exists when [`Snapshot`] is present.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'DesiredTargets', []
)
```

#### Return value
```python
'u32'
```
---------
### MinimumUntrustedScore
 The minimum score that each &#x27;untrusted&#x27; solution must attain in order to be considered
 feasible.

 Can be set via `set_minimum_untrusted_score`.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'MinimumUntrustedScore', []
)
```

#### Return value
```python
'[u128; 3]'
```
---------
### QueuedSolution
 Current best solution, signed or unsigned, queued to be returned upon `elect`.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'QueuedSolution', []
)
```

#### Return value
```python
{
    'compute': ('OnChain', 'Signed', 'Unsigned', 'Fallback', 'Emergency'),
    'score': '[u128; 3]',
    'supports': [
        ('AccountId', {'total': 'u128', 'voters': [('AccountId', 'u128')]}),
    ],
}
```
---------
### Round
 Internal counter for the number of rounds.

 This is useful for de-duplication of transactions submitted to the pool, and general
 diagnostics of the pallet.

 This is merely incremented once per every time that an upstream `elect` is called.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'Round', []
)
```

#### Return value
```python
'u32'
```
---------
### SignedSubmissionIndices
 A sorted, bounded set of `(score, index)`, where each `index` points to a value in
 `SignedSubmissions`.

 We never need to process more than a single signed submission at a time. Signed submissions
 can be quite large, so we&#x27;re willing to pay the cost of multiple database accesses to access
 them one at a time instead of reading and decoding all of them at once.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'SignedSubmissionIndices', []
)
```

#### Return value
```python
'scale_info::205'
```
---------
### SignedSubmissionNextIndex
 The next index to be assigned to an incoming signed submission.

 Every accepted submission is assigned a unique index; that index is bound to that particular
 submission for the duration of the election. On election finalization, the next index is
 reset to 0.

 We can&#x27;t just use `SignedSubmissionIndices.len()`, because that&#x27;s a bounded set; past its
 capacity, it will simply saturate. We can&#x27;t just iterate over `SignedSubmissionsMap`,
 because iteration is slow. Instead, we store the value here.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'SignedSubmissionNextIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### SignedSubmissionsMap
 Unchecked, signed solutions.

 Together with `SubmissionIndices`, this stores a bounded set of `SignedSubmissions` while
 allowing us to keep only a single one in memory at a time.

 Twox note: the key of the map is an auto-incrementing index which users cannot inspect or
 affect; we shouldn&#x27;t need a cryptographically secure hasher.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'SignedSubmissionsMap', ['u32']
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'raw_solution': {
        'round': 'u32',
        'score': '[u128; 3]',
        'solution': {
            'votes1': [('u32', 'u16')],
            'votes10': [('u32', "[('u16', 'u16'); 9]", 'u16')],
            'votes11': [('u32', "[('u16', 'u16'); 10]", 'u16')],
            'votes12': [('u32', "[('u16', 'u16'); 11]", 'u16')],
            'votes13': [('u32', "[('u16', 'u16'); 12]", 'u16')],
            'votes14': [('u32', "[('u16', 'u16'); 13]", 'u16')],
            'votes15': [('u32', "[('u16', 'u16'); 14]", 'u16')],
            'votes16': [('u32', "[('u16', 'u16'); 15]", 'u16')],
            'votes2': [('u32', ('u16', 'u16'), 'u16')],
            'votes3': [('u32', "[('u16', 'u16'); 2]", 'u16')],
            'votes4': [('u32', "[('u16', 'u16'); 3]", 'u16')],
            'votes5': [('u32', "[('u16', 'u16'); 4]", 'u16')],
            'votes6': [('u32', "[('u16', 'u16'); 5]", 'u16')],
            'votes7': [('u32', "[('u16', 'u16'); 6]", 'u16')],
            'votes8': [('u32', "[('u16', 'u16'); 7]", 'u16')],
            'votes9': [('u32', "[('u16', 'u16'); 8]", 'u16')],
        },
    },
    'reward': 'u128',
    'who': 'AccountId',
}
```
---------
### Snapshot
 Snapshot data of the round.

 This is created at the beginning of the signed phase and cleared upon calling `elect`.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'Snapshot', []
)
```

#### Return value
```python
{'targets': ['AccountId'], 'voters': [('AccountId', 'u64', ['AccountId'])]}
```
---------
### SnapshotMetadata
 The metadata of the [`RoundSnapshot`]

 Only exists when [`Snapshot`] is present.

#### Python
```python
result = substrate.query(
    'ElectionProviderMultiPhase', 'SnapshotMetadata', []
)
```

#### Return value
```python
{'targets': 'u32', 'voters': 'u32'}
```
---------
## Constants

---------
### MinerMaxLength
 Maximum length (bytes) that the mined solution should consume.

 The miner will ensure that the total length of the unsigned solution will not exceed
 this value.
#### Value
```python
3538944
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MinerMaxLength')
```
---------
### MinerMaxWeight
 Maximum weight that the miner should consume.

 The miner will ensure that the total weight of the unsigned solution will not exceed
 this value, based on [`WeightInfo::submit_unsigned`].
#### Value
```python
1444875000000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MinerMaxWeight')
```
---------
### MinerTxPriority
 The priority of the unsigned transaction submitted in the unsigned-phase
#### Value
```python
16602069666338596453
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MinerTxPriority')
```
---------
### OffchainRepeat
 The repeat threshold of the offchain worker.

 For example, if it is 5, that means that at least 5 blocks will elapse between attempts
 to submit the worker&#x27;s solution.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'OffchainRepeat')
```
---------
### SignedDepositBase
 Base deposit for a signed solution.
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedDepositBase')
```
---------
### SignedDepositByte
 Per-byte deposit for a signed solution.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedDepositByte')
```
---------
### SignedDepositWeight
 Per-weight deposit for a signed solution.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedDepositWeight')
```
---------
### SignedMaxSubmissions
 Maximum number of signed submissions that can be queued.

 It is best to avoid adjusting this during an election, as it impacts downstream data
 structures. In particular, `SignedSubmissionIndices&lt;T&gt;` is bounded on this value. If you
 update this value during an election, you _must_ ensure that
 `SignedSubmissionIndices.len()` is less than or equal to the new value. Otherwise,
 attempts to submit new solutions may cause a runtime panic.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedMaxSubmissions')
```
---------
### SignedMaxWeight
 Maximum weight of a signed solution.

 This should probably be similar to [`Config::MinerMaxWeight`].
#### Value
```python
1444875000000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedMaxWeight')
```
---------
### SignedPhase
 Duration of the signed phase.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedPhase')
```
---------
### SignedRewardBase
 Base reward for a signed solution
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedRewardBase')
```
---------
### SolutionImprovementThreshold
 The minimum amount of improvement to the solution score that defines a solution as
 &quot;better&quot; (in any phase).
#### Value
```python
500000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SolutionImprovementThreshold')
```
---------
### UnsignedPhase
 Duration of the unsigned phase.
#### Value
```python
600
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'UnsignedPhase')
```
---------
### VoterSnapshotPerBlock
 The maximum number of voters to put in the snapshot. At the moment, snapshots are only
 over a single block, but once multi-block elections are introduced they will take place
 over multiple blocks.

 Also, note the data type: If the voters are represented by a `u32` in `type
 CompactSolution`, the same `u32` is used here to ensure bounds are respected.
#### Value
```python
22500
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'VoterSnapshotPerBlock')
```
---------
## Errors

---------
### CallNotAllowed
The call is not allowed at this point.

---------
### InvalidSubmissionIndex
`Self::insert_submission` returned an invalid index.

---------
### MissingSnapshotMetadata
Snapshot metadata should exist but didn&\#x27;t.

---------
### OcwCallWrongEra
OCW submitted solution for wrong round

---------
### PreDispatchEarlySubmission
Submission was too early.

---------
### PreDispatchWeakSubmission
Submission was too weak, score-wise.

---------
### PreDispatchWrongWinnerCount
Wrong number of winners presented.

---------
### SignedCannotPayDeposit
The origin failed to pay the deposit.

---------
### SignedInvalidWitness
Witness data to dispatchable is invalid.

---------
### SignedQueueFull
The queue was full, and the solution was not better than any of the existing ones.

---------
### SignedTooMuchWeight
The signed submission consumes too much weight

---------