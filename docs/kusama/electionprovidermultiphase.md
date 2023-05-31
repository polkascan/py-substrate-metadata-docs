
# ElectionProviderMultiPhase

---------
## Calls

---------
### governance_fallback
Trigger the governance fallback.

This can only be called when [`Phase::Emergency`] is enabled, as an alternative to
calling [`Call::set_emergency_election_result`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_max_voters | `Option<u32>` | 
| maybe_max_targets | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'ElectionProviderMultiPhase', 'governance_fallback', {
    'maybe_max_targets': (None, 'u32'),
    'maybe_max_voters': (None, 'u32'),
}
)
```

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
        {
            'minimal_stake': 'u128',
            'sum_stake': 'u128',
            'sum_stake_squared': 'u128',
        },
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| raw_solution | `Box<RawSolution<SolutionOf<T::MinerConfig>>>` | 

#### Python
```python
call = substrate.compose_call(
    'ElectionProviderMultiPhase', 'submit', {
    'raw_solution': {
        'round': 'u32',
        'score': {
            'minimal_stake': 'u128',
            'sum_stake': 'u128',
            'sum_stake_squared': 'u128',
        },
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
            'votes17': [
                (
                    'u32',
                    "[('u16', 'u16'); 16]",
                    'u16',
                ),
            ],
            'votes18': [
                (
                    'u32',
                    "[('u16', 'u16'); 17]",
                    'u16',
                ),
            ],
            'votes19': [
                (
                    'u32',
                    "[('u16', 'u16'); 18]",
                    'u16',
                ),
            ],
            'votes2': [
                ('u32', ('u16', 'u16'), 'u16'),
            ],
            'votes20': [
                (
                    'u32',
                    "[('u16', 'u16'); 19]",
                    'u16',
                ),
            ],
            'votes21': [
                (
                    'u32',
                    "[('u16', 'u16'); 20]",
                    'u16',
                ),
            ],
            'votes22': [
                (
                    'u32',
                    "[('u16', 'u16'); 21]",
                    'u16',
                ),
            ],
            'votes23': [
                (
                    'u32',
                    "[('u16', 'u16'); 22]",
                    'u16',
                ),
            ],
            'votes24': [
                (
                    'u32',
                    "[('u16', 'u16'); 23]",
                    'u16',
                ),
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
| raw_solution | `Box<RawSolution<SolutionOf<T::MinerConfig>>>` | 
| witness | `SolutionOrSnapshotSize` | 

#### Python
```python
call = substrate.compose_call(
    'ElectionProviderMultiPhase', 'submit_unsigned', {
    'raw_solution': {
        'round': 'u32',
        'score': {
            'minimal_stake': 'u128',
            'sum_stake': 'u128',
            'sum_stake_squared': 'u128',
        },
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
            'votes17': [
                (
                    'u32',
                    "[('u16', 'u16'); 16]",
                    'u16',
                ),
            ],
            'votes18': [
                (
                    'u32',
                    "[('u16', 'u16'); 17]",
                    'u16',
                ),
            ],
            'votes19': [
                (
                    'u32',
                    "[('u16', 'u16'); 18]",
                    'u16',
                ),
            ],
            'votes2': [
                ('u32', ('u16', 'u16'), 'u16'),
            ],
            'votes20': [
                (
                    'u32',
                    "[('u16', 'u16'); 19]",
                    'u16',
                ),
            ],
            'votes21': [
                (
                    'u32',
                    "[('u16', 'u16'); 20]",
                    'u16',
                ),
            ],
            'votes22': [
                (
                    'u32',
                    "[('u16', 'u16'); 21]",
                    'u16',
                ),
            ],
            'votes23': [
                (
                    'u32',
                    "[('u16', 'u16'); 22]",
                    'u16',
                ),
            ],
            'votes24': [
                (
                    'u32',
                    "[('u16', 'u16'); 23]",
                    'u16',
                ),
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
### ElectionFailed
An election failed.

Not much can be said about which computes failed in the process.
#### Attributes
No attributes

---------
### ElectionFinalized
The election has been finalized, with the given computation and score.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| compute | `ElectionCompute` | ```('OnChain', 'Signed', 'Unsigned', 'Fallback', 'Emergency')```
| score | `ElectionScore` | ```{'minimal_stake': 'u128', 'sum_stake': 'u128', 'sum_stake_squared': 'u128'}```

---------
### PhaseTransitioned
There was a phase transition in a given round.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `Phase<T::BlockNumber>` | ```{'Off': None, 'Signed': None, 'Unsigned': ('bool', 'u32'), 'Emergency': None}```
| to | `Phase<T::BlockNumber>` | ```{'Off': None, 'Signed': None, 'Unsigned': ('bool', 'u32'), 'Emergency': None}```
| round | `u32` | ```u32```

---------
### Rewarded
An account has been rewarded for their signed submission being finalized.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `<T as frame_system::Config>::AccountId` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```

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

The `origin` indicates the origin of the solution. If `origin` is `Some(AccountId)`,
the stored solution was submited in the signed phase by a miner with the `AccountId`.
Otherwise, the solution was stored either during the unsigned phase or by
`T::ForceOrigin`. The `bool` is `true` when a previous solution was ejected to make
room for this one.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| compute | `ElectionCompute` | ```('OnChain', 'Signed', 'Unsigned', 'Fallback', 'Emergency')```
| origin | `Option<T::AccountId>` | ```(None, 'AccountId')```
| prev_ejected | `bool` | ```bool```

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
{'minimal_stake': 'u128', 'sum_stake': 'u128', 'sum_stake_squared': 'u128'}
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
    'score': {
        'minimal_stake': 'u128',
        'sum_stake': 'u128',
        'sum_stake_squared': 'u128',
    },
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
 A sorted, bounded vector of `(score, block_number, index)`, where each `index` points to a
 value in `SignedSubmissions`.

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
[
    (
        {
            'minimal_stake': 'u128',
            'sum_stake': 'u128',
            'sum_stake_squared': 'u128',
        },
        'u32',
        'u32',
    ),
]
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
    'call_fee': 'u128',
    'deposit': 'u128',
    'raw_solution': {
        'round': 'u32',
        'score': {
            'minimal_stake': 'u128',
            'sum_stake': 'u128',
            'sum_stake_squared': 'u128',
        },
        'solution': {
            'votes1': [('u32', 'u16')],
            'votes10': [('u32', "[('u16', 'u16'); 9]", 'u16')],
            'votes11': [('u32', "[('u16', 'u16'); 10]", 'u16')],
            'votes12': [('u32', "[('u16', 'u16'); 11]", 'u16')],
            'votes13': [('u32', "[('u16', 'u16'); 12]", 'u16')],
            'votes14': [('u32', "[('u16', 'u16'); 13]", 'u16')],
            'votes15': [('u32', "[('u16', 'u16'); 14]", 'u16')],
            'votes16': [('u32', "[('u16', 'u16'); 15]", 'u16')],
            'votes17': [('u32', "[('u16', 'u16'); 16]", 'u16')],
            'votes18': [('u32', "[('u16', 'u16'); 17]", 'u16')],
            'votes19': [('u32', "[('u16', 'u16'); 18]", 'u16')],
            'votes2': [('u32', ('u16', 'u16'), 'u16')],
            'votes20': [('u32', "[('u16', 'u16'); 19]", 'u16')],
            'votes21': [('u32', "[('u16', 'u16'); 20]", 'u16')],
            'votes22': [('u32', "[('u16', 'u16'); 21]", 'u16')],
            'votes23': [('u32', "[('u16', 'u16'); 22]", 'u16')],
            'votes24': [('u32', "[('u16', 'u16'); 23]", 'u16')],
            'votes3': [('u32', "[('u16', 'u16'); 2]", 'u16')],
            'votes4': [('u32', "[('u16', 'u16'); 3]", 'u16')],
            'votes5': [('u32', "[('u16', 'u16'); 4]", 'u16')],
            'votes6': [('u32', "[('u16', 'u16'); 5]", 'u16')],
            'votes7': [('u32', "[('u16', 'u16'); 6]", 'u16')],
            'votes8': [('u32', "[('u16', 'u16'); 7]", 'u16')],
            'votes9': [('u32', "[('u16', 'u16'); 8]", 'u16')],
        },
    },
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
### BetterSignedThreshold
 The minimum amount of improvement to the solution score that defines a solution as
 &quot;better&quot; in the Signed phase.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'BetterSignedThreshold')
```
---------
### BetterUnsignedThreshold
 The minimum amount of improvement to the solution score that defines a solution as
 &quot;better&quot; in the Unsigned phase.
#### Value
```python
500000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'BetterUnsignedThreshold')
```
---------
### MaxElectableTargets
 The maximum number of electable targets to put in the snapshot.
#### Value
```python
65535
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MaxElectableTargets')
```
---------
### MaxElectingVoters
 The maximum number of electing voters to put in the snapshot. At the moment, snapshots
 are only over a single block, but once multi-block elections are introduced they will
 take place over multiple blocks.
#### Value
```python
12500
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MaxElectingVoters')
```
---------
### MaxWinners
 The maximum number of winners that can be elected by this `ElectionProvider`
 implementation.

 Note: This must always be greater or equal to `T::DataProvider::desired_targets()`.
#### Value
```python
2000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MaxWinners')
```
---------
### MinerMaxLength
#### Value
```python
3538944
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MinerMaxLength')
```
---------
### MinerMaxVotesPerVoter
#### Value
```python
24
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MinerMaxVotesPerVoter')
```
---------
### MinerMaxWeight
#### Value
```python
{'proof_size': 13650590614545068195, 'ref_time': 1476422011000}
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MinerMaxWeight')
```
---------
### MinerMaxWinners
#### Value
```python
2000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'MinerMaxWinners')
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
18
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
1333333332000
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
325520
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
### SignedMaxRefunds
 The maximum amount of unchecked solutions to refund the call fee for.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedMaxRefunds')
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
16
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedMaxSubmissions')
```
---------
### SignedMaxWeight
 Maximum weight of a signed solution.

 If [`Config::MinerConfig`] is being implemented to submit signed solutions (outside of
 this pallet), then [`MinerConfig::solution_weight`] is used to compare against
 this value.
#### Value
```python
{'proof_size': 13650590614545068195, 'ref_time': 1476422011000}
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
150
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
100000000000
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'SignedRewardBase')
```
---------
### UnsignedPhase
 Duration of the unsigned phase.
#### Value
```python
150
```
#### Python
```python
constant = substrate.get_constant('ElectionProviderMultiPhase', 'UnsignedPhase')
```
---------
## Errors

---------
### BoundNotMet
Some bound not met

---------
### CallNotAllowed
The call is not allowed at this point.

---------
### FallbackFailed
The fallback failed

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
### TooManyWinners
Submitted solution has too many winners

---------