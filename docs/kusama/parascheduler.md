
# ParaScheduler

---------
## Storage functions

---------
### AvailabilityCores
 One entry for each availability core. Entries are `None` if the core is not currently
 occupied. Can be temporarily `Some` if scheduled but not occupied.
 The i&#x27;th parachain belongs to the i&#x27;th core, with the remaining cores all being
 parathread-multiplexers.

 Bounded by the maximum of either of these two values:
   * The number of parachains and parathread multiplexers
   * The number of validators divided by `configuration.max_validators_per_core`.

#### Python
```python
result = substrate.query(
    'ParaScheduler', 'AvailabilityCores', []
)
```

#### Return value
```python
[
    {
        'Free': None,
        'Paras': {
            'assignment': {'para_id': 'u32'},
            'availability_timeouts': 'u32',
            'ttl': 'u32',
        },
    },
]
```
---------
### ClaimQueue
 One entry for each availability core. The `VecDeque` represents the assignments to be
 scheduled on that core. `None` is used to signal to not schedule the next para of the core
 as there is one currently being scheduled. Not using `None` here would overwrite the
 `CoreState` in the runtime API. The value contained here will not be valid after the end of
 a block. Runtime APIs should be used to determine scheduled cores/ for the upcoming block.

#### Python
```python
result = substrate.query(
    'ParaScheduler', 'ClaimQueue', []
)
```

#### Return value
```python
'scale_info::803'
```
---------
### SessionStartBlock
 The block number where the session start occurred. Used to track how many group rotations
 have occurred.

 Note that in the context of parachains modules the session change is signaled during
 the block and enacted at the end of the block (at the finalization stage, to be exact).
 Thus for all intents and purposes the effect of the session change is observed at the
 block following the session change, block number of which we save in this storage value.

#### Python
```python
result = substrate.query(
    'ParaScheduler', 'SessionStartBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### ValidatorGroups
 All the validator groups. One for each core. Indices are into `ActiveValidators` - not the
 broader set of Polkadot validators, but instead just the subset used for parachains during
 this session.

 Bound: The number of cores is the sum of the numbers of parachains and parathread
 multiplexers. Reasonably, 100-1000. The dominant factor is the number of validators: safe
 upper bound at 10k.

#### Python
```python
result = substrate.query(
    'ParaScheduler', 'ValidatorGroups', []
)
```

#### Return value
```python
[['u32']]
```
---------