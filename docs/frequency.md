# frequency
---------
| Properties |  |
| -------- | -------- |
| Spec name     | frequency     |
| Implementation name     | frequency     |
| Spec version     | 11     |
| SS58 Format     | 90     |
| Token symbol      | FRQCY     |
| Token decimals      | 8     |

## Aura
---------
### Storage functions
---------
#### Authorities

##### Python
```python
result = substrate.query(
    'Aura', 'Authorities', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------
#### CurrentSlot

##### Python
```python
result = substrate.query(
    'Aura', 'CurrentSlot', []
)
```

##### Return value
```python
'u64'
```
---------

## AuraExt
---------
### Storage functions
---------
#### Authorities

##### Python
```python
result = substrate.query(
    'AuraExt', 'Authorities', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------

## Authorship
---------
### Calls
---------
#### set_uncles
##### Attributes
| Name | Type |
| -------- | -------- | 
| new_uncles | `Vec<T::Header>` | 

##### Python
```python
call = substrate.compose_call(
    'Authorship', 'set_uncles', {
    'new_uncles': [
        {
            'digest': {
                'logs': [
                    {
                        None: None,
                        'Consensus': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                        'Other': 'Bytes',
                        'PreRuntime': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                        'RuntimeEnvironmentUpdated': None,
                        'Seal': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                    },
                ],
            },
            'extrinsics_root': '[u8; 32]',
            'number': 'u32',
            'parent_hash': '[u8; 32]',
            'state_root': '[u8; 32]',
        },
    ],
}
)
```

---------
### Storage functions
---------
#### Author

##### Python
```python
result = substrate.query(
    'Authorship', 'Author', []
)
```

##### Return value
```python
'AccountId'
```
---------
#### DidSetUncles

##### Python
```python
result = substrate.query(
    'Authorship', 'DidSetUncles', []
)
```

##### Return value
```python
'bool'
```
---------
#### Uncles

##### Python
```python
result = substrate.query(
    'Authorship', 'Uncles', []
)
```

##### Return value
```python
[{'InclusionHeight': 'u32', 'Uncle': ('[u8; 32]', (None, 'AccountId'))}]
```
---------
### Constants
---------
#### UncleGenerations
##### Value
```python
0
```
##### Python
```python
constant = substrate.get_constant('Authorship', 'UncleGenerations')
```
---------
### Errors
---------
#### GenesisUncle

---------
#### InvalidUncleParent

---------
#### OldUncle

---------
#### TooHighUncle

---------
#### TooManyUncles

---------
#### UncleAlreadyIncluded

---------
#### UnclesAlreadySet

---------

## Balances
---------
### Calls
---------
#### force_transfer
##### Attributes
| Name | Type |
| -------- | -------- | 
| source | `AccountIdLookupOf<T>` | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'force_transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
#### force_unreserve
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'force_unreserve', {
    'amount': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### set_balance
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| new_free | `T::Balance` | 
| new_reserved | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'set_balance', {
    'new_free': 'u128',
    'new_reserved': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### transfer
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
#### transfer_all
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| keep_alive | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer_all', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
#### transfer_keep_alive
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer_keep_alive', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
### Events
---------
#### BalanceSet
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
#### Deposit
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### DustLost
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Endowed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| free_balance | `T::Balance` | ```u128```

---------
#### ReserveRepatriated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| destination_status | `Status` | ```('Free', 'Reserved')```

---------
#### Reserved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Slashed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Transfer
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Unreserved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Withdraw
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Storage functions
---------
#### Account

##### Python
```python
result = substrate.query(
    'Balances', 'Account', ['AccountId']
)
```

##### Return value
```python
{
    'fee_frozen': 'u128',
    'free': 'u128',
    'misc_frozen': 'u128',
    'reserved': 'u128',
}
```
---------
#### InactiveIssuance

##### Python
```python
result = substrate.query(
    'Balances', 'InactiveIssuance', []
)
```

##### Return value
```python
'u128'
```
---------
#### Locks

##### Python
```python
result = substrate.query(
    'Balances', 'Locks', ['AccountId']
)
```

##### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]', 'reasons': ('Fee', 'Misc', 'All')}]
```
---------
#### Reserves

##### Python
```python
result = substrate.query(
    'Balances', 'Reserves', ['AccountId']
)
```

##### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
#### TotalIssuance

##### Python
```python
result = substrate.query(
    'Balances', 'TotalIssuance', []
)
```

##### Return value
```python
'u128'
```
---------
### Constants
---------
#### ExistentialDeposit
##### Value
```python
1000000
```
##### Python
```python
constant = substrate.get_constant('Balances', 'ExistentialDeposit')
```
---------
#### MaxLocks
##### Value
```python
50
```
##### Python
```python
constant = substrate.get_constant('Balances', 'MaxLocks')
```
---------
#### MaxReserves
##### Value
```python
50
```
##### Python
```python
constant = substrate.get_constant('Balances', 'MaxReserves')
```
---------
### Errors
---------
#### DeadAccount

---------
#### ExistentialDeposit

---------
#### ExistingVestingSchedule

---------
#### InsufficientBalance

---------
#### KeepAlive

---------
#### LiquidityRestrictions

---------
#### TooManyReserves

---------
#### VestingBalance

---------

## CollatorSelection
---------
### Calls
---------
#### leave_intent
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'leave_intent', {}
)
```

---------
#### register_as_candidate
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'register_as_candidate', {}
)
```

---------
#### set_candidacy_bond
##### Attributes
| Name | Type |
| -------- | -------- | 
| bond | `BalanceOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_candidacy_bond', {'bond': 'u128'}
)
```

---------
#### set_desired_candidates
##### Attributes
| Name | Type |
| -------- | -------- | 
| max | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_desired_candidates', {'max': 'u32'}
)
```

---------
#### set_invulnerables
##### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Vec<T::AccountId>` | 

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_invulnerables', {'new': ['AccountId']}
)
```

---------
### Events
---------
#### CandidateAdded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### CandidateRemoved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
#### NewCandidacyBond
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bond_amount | `BalanceOf<T>` | ```u128```

---------
#### NewDesiredCandidates
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| desired_candidates | `u32` | ```u32```

---------
#### NewInvulnerables
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| invulnerables | `Vec<T::AccountId>` | ```['AccountId']```

---------
### Storage functions
---------
#### CandidacyBond

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'CandidacyBond', []
)
```

##### Return value
```python
'u128'
```
---------
#### Candidates

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'Candidates', []
)
```

##### Return value
```python
[{'deposit': 'u128', 'who': 'AccountId'}]
```
---------
#### DesiredCandidates

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'DesiredCandidates', []
)
```

##### Return value
```python
'u32'
```
---------
#### Invulnerables

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'Invulnerables', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### LastAuthoredBlock

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'LastAuthoredBlock', ['AccountId']
)
```

##### Return value
```python
'u32'
```
---------
### Errors
---------
#### AlreadyCandidate

---------
#### AlreadyInvulnerable

---------
#### NoAssociatedValidatorId

---------
#### NotCandidate

---------
#### Permission

---------
#### TooFewCandidates

---------
#### TooManyCandidates

---------
#### TooManyInvulnerables

---------
#### Unknown

---------
#### ValidatorNotRegistered

---------

## Council
---------
### Calls
---------
#### close
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `Weight` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Council', 'close', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
#### close_old_weight
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `OldWeight` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Council', 'close_old_weight', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': 'u64',
}
)
```

---------
#### disapprove_proposal
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Council', 'disapprove_proposal', {'proposal_hash': '[u8; 32]'}
)
```

---------
#### execute
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Council', 'execute', {
    'length_bound': 'u32',
    'proposal': 'Call',
}
)
```

---------
#### propose
##### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `MemberCount` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Council', 'propose', {
    'length_bound': 'u32',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
#### set_members
##### Attributes
| Name | Type |
| -------- | -------- | 
| new_members | `Vec<T::AccountId>` | 
| prime | `Option<T::AccountId>` | 
| old_count | `MemberCount` | 

##### Python
```python
call = substrate.compose_call(
    'Council', 'set_members', {
    'new_members': ['AccountId'],
    'old_count': 'u32',
    'prime': (None, 'AccountId'),
}
)
```

---------
#### vote
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'Council', 'vote', {
    'approve': 'bool',
    'index': 'u32',
    'proposal': '[u8; 32]',
}
)
```

---------
### Events
---------
#### Approved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Closed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
#### Disapproved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Executed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### MemberExecuted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### Proposed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| threshold | `MemberCount` | ```u32```

---------
#### Voted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| voted | `bool` | ```bool```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Storage functions
---------
#### Members

##### Python
```python
result = substrate.query(
    'Council', 'Members', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### Prime

##### Python
```python
result = substrate.query(
    'Council', 'Prime', []
)
```

##### Return value
```python
'AccountId'
```
---------
#### ProposalCount

##### Python
```python
result = substrate.query(
    'Council', 'ProposalCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### ProposalOf

##### Python
```python
result = substrate.query(
    'Council', 'ProposalOf', ['[u8; 32]']
)
```

##### Return value
```python
'Call'
```
---------
#### Proposals

##### Python
```python
result = substrate.query(
    'Council', 'Proposals', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------
#### Voting

##### Python
```python
result = substrate.query(
    'Council', 'Voting', ['[u8; 32]']
)
```

##### Return value
```python
{'ayes': ['AccountId'], 'end': 'u32', 'index': 'u32', 'nays': ['AccountId'], 'threshold': 'u32'}
```
---------
### Errors
---------
#### AlreadyInitialized

---------
#### DuplicateProposal

---------
#### DuplicateVote

---------
#### NotMember

---------
#### ProposalMissing

---------
#### TooEarly

---------
#### TooManyProposals

---------
#### WrongIndex

---------
#### WrongProposalLength

---------
#### WrongProposalWeight

---------

## Democracy
---------
### Calls
---------
#### blacklist
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `H256` | 
| maybe_ref_index | `Option<ReferendumIndex>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'blacklist', {
    'maybe_ref_index': (None, 'u32'),
    'proposal_hash': '[u8; 32]',
}
)
```

---------
#### cancel_proposal
##### Attributes
| Name | Type |
| -------- | -------- | 
| prop_index | `PropIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_proposal', {'prop_index': 'u32'}
)
```

---------
#### cancel_referendum
##### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_referendum', {'ref_index': 'u32'}
)
```

---------
#### clear_public_proposals
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'clear_public_proposals', {}
)
```

---------
#### delegate
##### Attributes
| Name | Type |
| -------- | -------- | 
| to | `AccountIdLookupOf<T>` | 
| conviction | `Conviction` | 
| balance | `BalanceOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'delegate', {
    'balance': 'u128',
    'conviction': (
        'None',
        'Locked1x',
        'Locked2x',
        'Locked3x',
        'Locked4x',
        'Locked5x',
        'Locked6x',
    ),
    'to': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### emergency_cancel
##### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'emergency_cancel', {'ref_index': 'u32'}
)
```

---------
#### external_propose
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose', {
    'proposal': {
        'Inline': 'Bytes',
        'Legacy': {'hash': '[u8; 32]'},
        'Lookup': {
            'hash': '[u8; 32]',
            'len': 'u32',
        },
    },
}
)
```

---------
#### external_propose_default
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose_default', {
    'proposal': {
        'Inline': 'Bytes',
        'Legacy': {'hash': '[u8; 32]'},
        'Lookup': {
            'hash': '[u8; 32]',
            'len': 'u32',
        },
    },
}
)
```

---------
#### external_propose_majority
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose_majority', {
    'proposal': {
        'Inline': 'Bytes',
        'Legacy': {'hash': '[u8; 32]'},
        'Lookup': {
            'hash': '[u8; 32]',
            'len': 'u32',
        },
    },
}
)
```

---------
#### fast_track
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `H256` | 
| voting_period | `T::BlockNumber` | 
| delay | `T::BlockNumber` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'fast_track', {
    'delay': 'u32',
    'proposal_hash': '[u8; 32]',
    'voting_period': 'u32',
}
)
```

---------
#### propose
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `BoundedCallOf<T>` | 
| value | `BalanceOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'propose', {
    'proposal': {
        'Inline': 'Bytes',
        'Legacy': {'hash': '[u8; 32]'},
        'Lookup': {
            'hash': '[u8; 32]',
            'len': 'u32',
        },
    },
    'value': 'u128',
}
)
```

---------
#### remove_other_vote
##### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 
| index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'remove_other_vote', {
    'index': 'u32',
    'target': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### remove_vote
##### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'remove_vote', {'index': 'u32'}
)
```

---------
#### second
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `PropIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'second', {'proposal': 'u32'}
)
```

---------
#### undelegate
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'undelegate', {}
)
```

---------
#### unlock
##### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'unlock', {
    'target': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### veto_external
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `H256` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'veto_external', {'proposal_hash': '[u8; 32]'}
)
```

---------
#### vote
##### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 
| vote | `AccountVote<BalanceOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'vote', {
    'ref_index': 'u32',
    'vote': {
        'Split': {
            'aye': 'u128',
            'nay': 'u128',
        },
        'Standard': {
            'balance': 'u128',
            'vote': {
                'aye': 'bool',
                'conviction': (
                    'None',
                    'Locked1x',
                    'Locked2x',
                    'Locked3x',
                    'Locked4x',
                    'Locked5x',
                    'Locked6x',
                ),
            },
        },
    },
}
)
```

---------
### Events
---------
#### Blacklisted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `H256` | ```[u8; 32]```

---------
#### Cancelled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### Delegated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| target | `T::AccountId` | ```AccountId```

---------
#### ExternalTabled
##### Attributes
No attributes

---------
#### NotPassed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### Passed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### ProposalCanceled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| prop_index | `PropIndex` | ```u32```

---------
#### Proposed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### Seconded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| seconder | `T::AccountId` | ```AccountId```
| prop_index | `PropIndex` | ```u32```

---------
#### Started
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```
| threshold | `VoteThreshold` | ```('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority')```

---------
#### Tabled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### Undelegated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### Vetoed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| proposal_hash | `H256` | ```[u8; 32]```
| until | `T::BlockNumber` | ```u32```

---------
#### Voted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| voter | `T::AccountId` | ```AccountId```
| ref_index | `ReferendumIndex` | ```u32```
| vote | `AccountVote<BalanceOf<T>>` | ```{'Standard': {'vote': {'aye': 'bool', 'conviction': ('None', 'Locked1x', 'Locked2x', 'Locked3x', 'Locked4x', 'Locked5x', 'Locked6x')}, 'balance': 'u128'}, 'Split': {'aye': 'u128', 'nay': 'u128'}}```

---------
### Storage functions
---------
#### Blacklist

##### Python
```python
result = substrate.query(
    'Democracy', 'Blacklist', ['[u8; 32]']
)
```

##### Return value
```python
('u32', ['AccountId'])
```
---------
#### Cancellations

##### Python
```python
result = substrate.query(
    'Democracy', 'Cancellations', ['[u8; 32]']
)
```

##### Return value
```python
'bool'
```
---------
#### DepositOf

##### Python
```python
result = substrate.query(
    'Democracy', 'DepositOf', ['u32']
)
```

##### Return value
```python
(['AccountId'], 'u128')
```
---------
#### LastTabledWasExternal

##### Python
```python
result = substrate.query(
    'Democracy', 'LastTabledWasExternal', []
)
```

##### Return value
```python
'bool'
```
---------
#### LowestUnbaked

##### Python
```python
result = substrate.query(
    'Democracy', 'LowestUnbaked', []
)
```

##### Return value
```python
'u32'
```
---------
#### NextExternal

##### Python
```python
result = substrate.query(
    'Democracy', 'NextExternal', []
)
```

##### Return value
```python
(
    {
        'Inline': 'Bytes',
        'Legacy': {'hash': '[u8; 32]'},
        'Lookup': {'hash': '[u8; 32]', 'len': 'u32'},
    },
    ('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority'),
)
```
---------
#### PublicPropCount

##### Python
```python
result = substrate.query(
    'Democracy', 'PublicPropCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### PublicProps

##### Python
```python
result = substrate.query(
    'Democracy', 'PublicProps', []
)
```

##### Return value
```python
[
    (
        'u32',
        {
            'Inline': 'Bytes',
            'Legacy': {'hash': '[u8; 32]'},
            'Lookup': {'hash': '[u8; 32]', 'len': 'u32'},
        },
        'AccountId',
    ),
]
```
---------
#### ReferendumCount

##### Python
```python
result = substrate.query(
    'Democracy', 'ReferendumCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### ReferendumInfoOf

##### Python
```python
result = substrate.query(
    'Democracy', 'ReferendumInfoOf', ['u32']
)
```

##### Return value
```python
{
    'Finished': {'approved': 'bool', 'end': 'u32'},
    'Ongoing': {
        'delay': 'u32',
        'end': 'u32',
        'proposal': {
            'Inline': 'Bytes',
            'Legacy': {'hash': '[u8; 32]'},
            'Lookup': {'hash': '[u8; 32]', 'len': 'u32'},
        },
        'tally': {'ayes': 'u128', 'nays': 'u128', 'turnout': 'u128'},
        'threshold': (
            'SuperMajorityApprove',
            'SuperMajorityAgainst',
            'SimpleMajority',
        ),
    },
}
```
---------
#### VotingOf

##### Python
```python
result = substrate.query(
    'Democracy', 'VotingOf', ['AccountId']
)
```

##### Return value
```python
{
    'Delegating': {
        'balance': 'u128',
        'conviction': (
            'None',
            'Locked1x',
            'Locked2x',
            'Locked3x',
            'Locked4x',
            'Locked5x',
            'Locked6x',
        ),
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'target': 'AccountId',
    },
    'Direct': {
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'votes': [('u32', {'Split': 'InnerStruct', 'Standard': 'InnerStruct'})],
    },
}
```
---------
### Constants
---------
#### CooloffPeriod
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'CooloffPeriod')
```
---------
#### EnactmentPeriod
##### Value
```python
57600
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'EnactmentPeriod')
```
---------
#### FastTrackVotingPeriod
##### Value
```python
900
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'FastTrackVotingPeriod')
```
---------
#### InstantAllowed
##### Value
```python
True
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'InstantAllowed')
```
---------
#### LaunchPeriod
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'LaunchPeriod')
```
---------
#### MaxBlacklisted
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MaxBlacklisted')
```
---------
#### MaxDeposits
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MaxDeposits')
```
---------
#### MaxProposals
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MaxProposals')
```
---------
#### MaxVotes
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MaxVotes')
```
---------
#### MinimumDeposit
##### Value
```python
10000000000
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MinimumDeposit')
```
---------
#### VoteLockingPeriod
##### Value
```python
57600
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'VoteLockingPeriod')
```
---------
#### VotingPeriod
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'VotingPeriod')
```
---------
### Errors
---------
#### AlreadyCanceled

---------
#### AlreadyDelegating

---------
#### AlreadyVetoed

---------
#### DuplicateProposal

---------
#### InstantNotAllowed

---------
#### InsufficientFunds

---------
#### InvalidHash

---------
#### MaxVotesReached

---------
#### NoPermission

---------
#### NoProposal

---------
#### NoneWaiting

---------
#### Nonsense

---------
#### NotDelegating

---------
#### NotSimpleMajority

---------
#### NotVoter

---------
#### ProposalBlacklisted

---------
#### ProposalMissing

---------
#### ReferendumInvalid

---------
#### TooMany

---------
#### ValueLow

---------
#### VotesExist

---------
#### VotingPeriodLow

---------
#### WrongUpperBound

---------

## Messages
---------
### Calls
---------
#### add_ipfs_message
##### Attributes
| Name | Type |
| -------- | -------- | 
| schema_id | `SchemaId` | 
| cid | `Vec<u8>` | 
| payload_length | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Messages', 'add_ipfs_message', {
    'cid': 'Bytes',
    'payload_length': 'u32',
    'schema_id': 'u16',
}
)
```

---------
#### add_onchain_message
##### Attributes
| Name | Type |
| -------- | -------- | 
| on_behalf_of | `Option<MessageSourceId>` | 
| schema_id | `SchemaId` | 
| payload | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Messages', 'add_onchain_message', {
    'on_behalf_of': (None, 'u64'),
    'payload': 'Bytes',
    'schema_id': 'u16',
}
)
```

---------
### Events
---------
#### MessagesStored
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| schema_id | `SchemaId` | ```u16```
| block_number | `T::BlockNumber` | ```u32```
| count | `u16` | ```u16```

---------
### Storage functions
---------
#### BlockMessageIndex

##### Python
```python
result = substrate.query(
    'Messages', 'BlockMessageIndex', []
)
```

##### Return value
```python
'u16'
```
---------
#### Messages

##### Python
```python
result = substrate.query(
    'Messages', 'Messages', ['u32', 'u16']
)
```

##### Return value
```python
[
    {
        'index': 'u16',
        'msa_id': (None, 'u64'),
        'payload': 'Bytes',
        'provider_msa_id': 'u64',
    },
]
```
---------
### Constants
---------
#### MaxMessagePayloadSizeBytes
##### Value
```python
51200
```
##### Python
```python
constant = substrate.get_constant('Messages', 'MaxMessagePayloadSizeBytes')
```
---------
#### MaxMessagesPerBlock
##### Value
```python
7000
```
##### Python
```python
constant = substrate.get_constant('Messages', 'MaxMessagesPerBlock')
```
---------
### Errors
---------
#### ExceedsMaxMessagePayloadSizeBytes

---------
#### InvalidCid

---------
#### InvalidMessageSourceAccount

---------
#### InvalidPayloadLocation

---------
#### InvalidSchemaId

---------
#### TooManyMessagesInBlock

---------
#### TypeConversionOverflow

---------
#### UnAuthorizedDelegate

---------
#### UnsupportedCidVersion

---------

## Msa
---------
### Calls
---------
#### add_public_key_to_msa
##### Attributes
| Name | Type |
| -------- | -------- | 
| msa_owner_public_key | `T::AccountId` | 
| msa_owner_proof | `MultiSignature` | 
| new_key_owner_proof | `MultiSignature` | 
| add_key_payload | `AddKeyData<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'add_public_key_to_msa', {
    'add_key_payload': {
        'expiration': 'u32',
        'msa_id': 'u64',
        'new_public_key': 'AccountId',
    },
    'msa_owner_proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'msa_owner_public_key': 'AccountId',
    'new_key_owner_proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
#### create
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Msa', 'create', {}
)
```

---------
#### create_provider
##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_name | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'create_provider', {'provider_name': 'Bytes'}
)
```

---------
#### create_sponsored_account_with_delegation
##### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| add_provider_payload | `AddProvider` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'create_sponsored_account_with_delegation', {
    'add_provider_payload': {
        'authorized_msa_id': 'u64',
        'expiration': 'u32',
        'schema_ids': ['u16'],
    },
    'delegator_key': 'AccountId',
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
#### delete_msa_public_key
##### Attributes
| Name | Type |
| -------- | -------- | 
| public_key_to_delete | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'delete_msa_public_key', {'public_key_to_delete': 'AccountId'}
)
```

---------
#### grant_delegation
##### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| add_provider_payload | `AddProvider` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'grant_delegation', {
    'add_provider_payload': {
        'authorized_msa_id': 'u64',
        'expiration': 'u32',
        'schema_ids': ['u16'],
    },
    'delegator_key': 'AccountId',
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
#### grant_schema_permissions
##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 
| schema_ids | `Vec<SchemaId>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'grant_schema_permissions', {
    'provider_msa_id': 'u64',
    'schema_ids': ['u16'],
}
)
```

---------
#### retire_msa
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Msa', 'retire_msa', {}
)
```

---------
#### revoke_delegation_by_delegator
##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_delegation_by_delegator', {'provider_msa_id': 'u64'}
)
```

---------
#### revoke_delegation_by_provider
##### Attributes
| Name | Type |
| -------- | -------- | 
| delegator | `MessageSourceId` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_delegation_by_provider', {'delegator': 'u64'}
)
```

---------
#### revoke_schema_permissions
##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 
| schema_ids | `Vec<SchemaId>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_schema_permissions', {
    'provider_msa_id': 'u64',
    'schema_ids': ['u16'],
}
)
```

---------
### Events
---------
#### DelegationGranted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
#### DelegationRevoked
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
#### DelegationUpdated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
#### MsaCreated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
#### MsaRetired
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```

---------
#### ProviderCreated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```

---------
#### PublicKeyAdded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
#### PublicKeyDeleted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key | `T::AccountId` | ```AccountId```

---------
### Storage functions
---------
#### CurrentMsaIdentifierMaximum

##### Python
```python
result = substrate.query(
    'Msa', 'CurrentMsaIdentifierMaximum', []
)
```

##### Return value
```python
'u64'
```
---------
#### DelegatorAndProviderToDelegation

##### Python
```python
result = substrate.query(
    'Msa', 'DelegatorAndProviderToDelegation', ['u64', 'u64']
)
```

##### Return value
```python
{'revoked_at': 'u32', 'schema_permissions': 'scale_info::239'}
```
---------
#### PayloadSignatureBucketCount

##### Python
```python
result = substrate.query(
    'Msa', 'PayloadSignatureBucketCount', ['u32']
)
```

##### Return value
```python
'u32'
```
---------
#### PayloadSignatureRegistry

##### Python
```python
result = substrate.query(
    'Msa', 'PayloadSignatureRegistry', [
    'u32',
    {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
]
)
```

##### Return value
```python
'u32'
```
---------
#### ProviderToRegistryEntry

##### Python
```python
result = substrate.query(
    'Msa', 'ProviderToRegistryEntry', ['u64']
)
```

##### Return value
```python
{'provider_name': 'Bytes'}
```
---------
#### PublicKeyCountForMsaId

##### Python
```python
result = substrate.query(
    'Msa', 'PublicKeyCountForMsaId', ['u64']
)
```

##### Return value
```python
'u8'
```
---------
#### PublicKeyToMsaId

##### Python
```python
result = substrate.query(
    'Msa', 'PublicKeyToMsaId', ['AccountId']
)
```

##### Return value
```python
'u64'
```
---------
### Constants
---------
#### MaxProviderNameSize
##### Value
```python
16
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxProviderNameSize')
```
---------
#### MaxPublicKeysPerMsa
##### Value
```python
25
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxPublicKeysPerMsa')
```
---------
#### MaxSchemaGrantsPerDelegation
##### Value
```python
30
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxSchemaGrantsPerDelegation')
```
---------
#### MaxSignaturesPerBucket
##### Value
```python
50000
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxSignaturesPerBucket')
```
---------
#### MaxSignaturesStored
##### Value
```python
100000
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxSignaturesStored')
```
---------
#### MortalityWindowSize
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MortalityWindowSize')
```
---------
#### NumberOfBuckets
##### Value
```python
2
```
##### Python
```python
constant = substrate.get_constant('Msa', 'NumberOfBuckets')
```
---------
### Errors
---------
#### AddProviderSignatureVerificationFailed

---------
#### CannotPredictValidityPastCurrentBlock

---------
#### DelegationNotFound

---------
#### DelegationRevoked

---------
#### DuplicateProvider

---------
#### DuplicateProviderRegistryEntry

---------
#### ExceedsMaxProviderNameSize

---------
#### ExceedsMaxSchemaGrantsPerDelegation

---------
#### InvalidSchemaId

---------
#### InvalidSelfProvider

---------
#### InvalidSelfRemoval

---------
#### InvalidSignature

---------
#### KeyAlreadyRegistered

---------
#### KeyLimitExceeded

---------
#### MsaIdOverflow

---------
#### MsaOwnershipInvalidSignature

---------
#### NewKeyOwnershipInvalidSignature

---------
#### NoKeyExists

---------
#### NotKeyOwner

---------
#### NotMsaOwner

---------
#### ProofHasExpired

---------
#### ProofNotYetValid

---------
#### ProviderNotRegistered

---------
#### SchemaNotGranted

---------
#### SignatureAlreadySubmitted

---------
#### SignatureRegistryLimitExceeded

---------
#### UnauthorizedDelegator

---------
#### UnauthorizedProvider

---------

## ParachainInfo
---------
### Storage functions
---------
#### ParachainId

##### Python
```python
result = substrate.query(
    'ParachainInfo', 'ParachainId', []
)
```

##### Return value
```python
'u32'
```
---------

## ParachainSystem
---------
### Calls
---------
#### authorize_upgrade
##### Attributes
| Name | Type |
| -------- | -------- | 
| code_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'authorize_upgrade', {'code_hash': '[u8; 32]'}
)
```

---------
#### enact_authorized_upgrade
##### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'enact_authorized_upgrade', {'code': 'Bytes'}
)
```

---------
#### set_validation_data
##### Attributes
| Name | Type |
| -------- | -------- | 
| data | `ParachainInherentData` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'set_validation_data', {
    'data': {
        'downward_messages': [
            {
                'msg': 'Bytes',
                'sent_at': 'u32',
            },
        ],
        'horizontal_messages': 'scale_info::106',
        'relay_chain_state': {
            'trie_nodes': 'scale_info::88',
        },
        'validation_data': {
            'max_pov_size': 'u32',
            'parent_head': 'Bytes',
            'relay_parent_number': 'u32',
            'relay_parent_storage_root': '[u8; 32]',
        },
    },
}
)
```

---------
#### sudo_send_upward_message
##### Attributes
| Name | Type |
| -------- | -------- | 
| message | `UpwardMessage` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'sudo_send_upward_message', {'message': 'Bytes'}
)
```

---------
### Events
---------
#### DownwardMessagesProcessed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| weight_used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| dmq_head | `relay_chain::Hash` | ```[u8; 32]```

---------
#### DownwardMessagesReceived
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| count | `u32` | ```u32```

---------
#### UpgradeAuthorized
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```[u8; 32]```

---------
#### ValidationFunctionApplied
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| relay_chain_block_num | `RelayChainBlockNumber` | ```u32```

---------
#### ValidationFunctionDiscarded
##### Attributes
No attributes

---------
#### ValidationFunctionStored
##### Attributes
No attributes

---------
### Storage functions
---------
#### AnnouncedHrmpMessagesPerCandidate

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'AnnouncedHrmpMessagesPerCandidate', []
)
```

##### Return value
```python
'u32'
```
---------
#### AuthorizedUpgrade

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'AuthorizedUpgrade', []
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### CustomValidationHeadData

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'CustomValidationHeadData', []
)
```

##### Return value
```python
'Bytes'
```
---------
#### DidSetValidationCode

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'DidSetValidationCode', []
)
```

##### Return value
```python
'bool'
```
---------
#### HostConfiguration

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'HostConfiguration', []
)
```

##### Return value
```python
{
    'hrmp_max_message_num_per_candidate': 'u32',
    'max_code_size': 'u32',
    'max_head_data_size': 'u32',
    'max_upward_message_num_per_candidate': 'u32',
    'max_upward_message_size': 'u32',
    'max_upward_queue_count': 'u32',
    'max_upward_queue_size': 'u32',
    'validation_upgrade_cooldown': 'u32',
    'validation_upgrade_delay': 'u32',
}
```
---------
#### HrmpOutboundMessages

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'HrmpOutboundMessages', []
)
```

##### Return value
```python
[{'data': 'Bytes', 'recipient': 'u32'}]
```
---------
#### HrmpWatermark

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'HrmpWatermark', []
)
```

##### Return value
```python
'u32'
```
---------
#### LastDmqMqcHead

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'LastDmqMqcHead', []
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### LastHrmpMqcHeads

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'LastHrmpMqcHeads', []
)
```

##### Return value
```python
'scale_info::97'
```
---------
#### LastRelayChainBlockNumber

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'LastRelayChainBlockNumber', []
)
```

##### Return value
```python
'u32'
```
---------
#### NewValidationCode

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'NewValidationCode', []
)
```

##### Return value
```python
'Bytes'
```
---------
#### PendingUpwardMessages

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'PendingUpwardMessages', []
)
```

##### Return value
```python
['Bytes']
```
---------
#### PendingValidationCode

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'PendingValidationCode', []
)
```

##### Return value
```python
'Bytes'
```
---------
#### ProcessedDownwardMessages

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'ProcessedDownwardMessages', []
)
```

##### Return value
```python
'u32'
```
---------
#### RelayStateProof

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'RelayStateProof', []
)
```

##### Return value
```python
{'trie_nodes': 'scale_info::88'}
```
---------
#### RelevantMessagingState

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'RelevantMessagingState', []
)
```

##### Return value
```python
{
    'dmq_mqc_head': '[u8; 32]',
    'egress_channels': [
        (
            'u32',
            {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'max_total_size': 'u32',
                'mqc_head': (None, '[u8; 32]'),
                'msg_count': 'u32',
                'total_size': 'u32',
            },
        ),
    ],
    'ingress_channels': [
        (
            'u32',
            {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'max_total_size': 'u32',
                'mqc_head': (None, '[u8; 32]'),
                'msg_count': 'u32',
                'total_size': 'u32',
            },
        ),
    ],
    'relay_dispatch_queue_size': ('u32', 'u32'),
}
```
---------
#### ReservedDmpWeightOverride

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'ReservedDmpWeightOverride', []
)
```

##### Return value
```python
{'proof_size': 'u64', 'ref_time': 'u64'}
```
---------
#### ReservedXcmpWeightOverride

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'ReservedXcmpWeightOverride', []
)
```

##### Return value
```python
{'proof_size': 'u64', 'ref_time': 'u64'}
```
---------
#### UpgradeRestrictionSignal

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'UpgradeRestrictionSignal', []
)
```

##### Return value
```python
(None, ('Present', ))
```
---------
#### UpwardMessages

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'UpwardMessages', []
)
```

##### Return value
```python
['Bytes']
```
---------
#### ValidationData

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'ValidationData', []
)
```

##### Return value
```python
{
    'max_pov_size': 'u32',
    'parent_head': 'Bytes',
    'relay_parent_number': 'u32',
    'relay_parent_storage_root': '[u8; 32]',
}
```
---------
### Errors
---------
#### HostConfigurationNotAvailable

---------
#### NotScheduled

---------
#### NothingAuthorized

---------
#### OverlappingUpgrades

---------
#### ProhibitedByPolkadot

---------
#### TooBig

---------
#### Unauthorized

---------
#### ValidationDataNotAvailable

---------

## Preimage
---------
### Calls
---------
#### note_preimage
##### Attributes
| Name | Type |
| -------- | -------- | 
| bytes | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'note_preimage', {'bytes': 'Bytes'}
)
```

---------
#### request_preimage
##### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'request_preimage', {'hash': '[u8; 32]'}
)
```

---------
#### unnote_preimage
##### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'unnote_preimage', {'hash': '[u8; 32]'}
)
```

---------
#### unrequest_preimage
##### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'unrequest_preimage', {'hash': '[u8; 32]'}
)
```

---------
### Events
---------
#### Cleared
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
#### Noted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
#### Requested
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### PreimageFor

##### Python
```python
result = substrate.query(
    'Preimage', 'PreimageFor', [('[u8; 32]', 'u32')]
)
```

##### Return value
```python
'Bytes'
```
---------
#### StatusFor

##### Python
```python
result = substrate.query(
    'Preimage', 'StatusFor', ['[u8; 32]']
)
```

##### Return value
```python
{
    'Requested': {
        'count': 'u32',
        'deposit': (None, ('AccountId', 'u128')),
        'len': (None, 'u32'),
    },
    'Unrequested': {'deposit': ('AccountId', 'u128'), 'len': 'u32'},
}
```
---------
### Errors
---------
#### AlreadyNoted

---------
#### NotAuthorized

---------
#### NotNoted

---------
#### NotRequested

---------
#### Requested

---------
#### TooBig

---------

## Scheduler
---------
### Calls
---------
#### cancel
##### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| index | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel', {'index': 'u32', 'when': 'u32'}
)
```

---------
#### cancel_named
##### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel_named', {'id': '[u8; 32]'}
)
```

---------
#### schedule
##### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule', {
    'call': 'Call',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
    'when': 'u32',
}
)
```

---------
#### schedule_after
##### Attributes
| Name | Type |
| -------- | -------- | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_after', {
    'after': 'u32',
    'call': 'Call',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
}
)
```

---------
#### schedule_named
##### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named', {
    'call': 'Call',
    'id': '[u8; 32]',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
    'when': 'u32',
}
)
```

---------
#### schedule_named_after
##### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named_after', {
    'after': 'u32',
    'call': 'Call',
    'id': '[u8; 32]',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
}
)
```

---------
### Events
---------
#### CallUnavailable
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
#### Canceled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
#### Dispatched
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### PeriodicFailed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
#### PermanentlyOverweight
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
#### Scheduled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
### Storage functions
---------
#### Agenda

##### Python
```python
result = substrate.query(
    'Scheduler', 'Agenda', ['u32']
)
```

##### Return value
```python
[
    (
        None,
        {
            'call': {
                'Inline': 'Bytes',
                'Legacy': {'hash': '[u8; 32]'},
                'Lookup': {'hash': '[u8; 32]', 'len': 'u32'},
            },
            'maybe_id': (None, '[u8; 32]'),
            'maybe_periodic': (None, ('u32', 'u32')),
            'origin': {
                'Council': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'Void': (),
                None: None,
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
            },
            'priority': 'u8',
        },
    ),
]
```
---------
#### IncompleteSince

##### Python
```python
result = substrate.query(
    'Scheduler', 'IncompleteSince', []
)
```

##### Return value
```python
'u32'
```
---------
#### Lookup

##### Python
```python
result = substrate.query(
    'Scheduler', 'Lookup', ['[u8; 32]']
)
```

##### Return value
```python
('u32', 'u32')
```
---------
### Constants
---------
#### MaxScheduledPerBlock
##### Value
```python
50
```
##### Python
```python
constant = substrate.get_constant('Scheduler', 'MaxScheduledPerBlock')
```
---------
#### MaximumWeight
##### Value
```python
{'proof_size': 524288, 'ref_time': 50000000000}
```
##### Python
```python
constant = substrate.get_constant('Scheduler', 'MaximumWeight')
```
---------
### Errors
---------
#### FailedToSchedule

---------
#### Named

---------
#### NotFound

---------
#### RescheduleNoChange

---------
#### TargetBlockNumberInPast

---------

## Schemas
---------
### Calls
---------
#### create_schema
##### Attributes
| Name | Type |
| -------- | -------- | 
| model | `BoundedVec<u8, T::SchemaModelMaxBytesBoundedVecLimit>` | 
| model_type | `ModelType` | 
| payload_location | `PayloadLocation` | 

##### Python
```python
call = substrate.compose_call(
    'Schemas', 'create_schema', {
    'model': 'Bytes',
    'model_type': (
        'AvroBinary',
        'Parquet',
    ),
    'payload_location': (
        'OnChain',
        'IPFS',
    ),
}
)
```

---------
#### set_max_schema_model_bytes
##### Attributes
| Name | Type |
| -------- | -------- | 
| max_size | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Schemas', 'set_max_schema_model_bytes', {'max_size': 'u32'}
)
```

---------
### Events
---------
#### SchemaCreated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key | `T::AccountId` | ```AccountId```
| schema_id | `SchemaId` | ```u16```

---------
#### SchemaMaxSizeChanged
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| max_size | `u32` | ```u32```

---------
### Storage functions
---------
#### CurrentSchemaIdentifierMaximum

##### Python
```python
result = substrate.query(
    'Schemas', 'CurrentSchemaIdentifierMaximum', []
)
```

##### Return value
```python
'u16'
```
---------
#### GovernanceSchemaModelMaxBytes

##### Python
```python
result = substrate.query(
    'Schemas', 'GovernanceSchemaModelMaxBytes', []
)
```

##### Return value
```python
'u32'
```
---------
#### Schemas

##### Python
```python
result = substrate.query(
    'Schemas', 'Schemas', ['u16']
)
```

##### Return value
```python
{
    'model': 'Bytes',
    'model_type': ('AvroBinary', 'Parquet'),
    'payload_location': ('OnChain', 'IPFS'),
}
```
---------
### Constants
---------
#### MaxSchemaRegistrations
##### Value
```python
65000
```
##### Python
```python
constant = substrate.get_constant('Schemas', 'MaxSchemaRegistrations')
```
---------
#### MinSchemaModelSizeBytes
##### Value
```python
8
```
##### Python
```python
constant = substrate.get_constant('Schemas', 'MinSchemaModelSizeBytes')
```
---------
#### SchemaModelMaxBytesBoundedVecLimit
##### Value
```python
65500
```
##### Python
```python
constant = substrate.get_constant('Schemas', 'SchemaModelMaxBytesBoundedVecLimit')
```
---------
### Errors
---------
#### ExceedsMaxSchemaModelBytes

---------
#### InvalidSchema

---------
#### LessThanMinSchemaModelBytes

---------
#### SchemaCountOverflow

---------

## Session
---------
### Calls
---------
#### purge_keys
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Session', 'purge_keys', {}
)
```

---------
#### set_keys
##### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `T::Keys` | 
| proof | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Session', 'set_keys', {'keys': {'aura': '[u8; 32]'}, 'proof': 'Bytes'}
)
```

---------
### Events
---------
#### NewSession
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session_index | `SessionIndex` | ```u32```

---------
### Storage functions
---------
#### CurrentIndex

##### Python
```python
result = substrate.query(
    'Session', 'CurrentIndex', []
)
```

##### Return value
```python
'u32'
```
---------
#### DisabledValidators

##### Python
```python
result = substrate.query(
    'Session', 'DisabledValidators', []
)
```

##### Return value
```python
['u32']
```
---------
#### KeyOwner

##### Python
```python
result = substrate.query(
    'Session', 'KeyOwner', [('[u8; 4]', 'Bytes')]
)
```

##### Return value
```python
'AccountId'
```
---------
#### NextKeys

##### Python
```python
result = substrate.query(
    'Session', 'NextKeys', ['AccountId']
)
```

##### Return value
```python
{'aura': '[u8; 32]'}
```
---------
#### QueuedChanged

##### Python
```python
result = substrate.query(
    'Session', 'QueuedChanged', []
)
```

##### Return value
```python
'bool'
```
---------
#### QueuedKeys

##### Python
```python
result = substrate.query(
    'Session', 'QueuedKeys', []
)
```

##### Return value
```python
[('AccountId', {'aura': '[u8; 32]'})]
```
---------
#### Validators

##### Python
```python
result = substrate.query(
    'Session', 'Validators', []
)
```

##### Return value
```python
['AccountId']
```
---------
### Errors
---------
#### DuplicatedKey

---------
#### InvalidProof

---------
#### NoAccount

---------
#### NoAssociatedValidatorId

---------
#### NoKeys

---------

## System
---------
### Calls
---------
#### kill_prefix
##### Attributes
| Name | Type |
| -------- | -------- | 
| prefix | `Key` | 
| subkeys | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'kill_prefix', {'prefix': 'Bytes', 'subkeys': 'u32'}
)
```

---------
#### kill_storage
##### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<Key>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'kill_storage', {'keys': ['Bytes']}
)
```

---------
#### remark
##### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'remark', {'remark': 'Bytes'}
)
```

---------
#### remark_with_event
##### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'remark_with_event', {'remark': 'Bytes'}
)
```

---------
#### set_code
##### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_code', {'code': 'Bytes'}
)
```

---------
#### set_code_without_checks
##### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_code_without_checks', {'code': 'Bytes'}
)
```

---------
#### set_heap_pages
##### Attributes
| Name | Type |
| -------- | -------- | 
| pages | `u64` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_heap_pages', {'pages': 'u64'}
)
```

---------
#### set_storage
##### Attributes
| Name | Type |
| -------- | -------- | 
| items | `Vec<KeyValue>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_storage', {'items': [('Bytes', 'Bytes')]}
)
```

---------
### Events
---------
#### CodeUpdated
##### Attributes
No attributes

---------
#### ExtrinsicFailed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### ExtrinsicSuccess
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### KilledAccount
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### NewAccount
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### Remarked
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| hash | `T::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### Account

##### Python
```python
result = substrate.query(
    'System', 'Account', ['AccountId']
)
```

##### Return value
```python
{
    'consumers': 'u32',
    'data': {
        'fee_frozen': 'u128',
        'free': 'u128',
        'misc_frozen': 'u128',
        'reserved': 'u128',
    },
    'nonce': 'u32',
    'providers': 'u32',
    'sufficients': 'u32',
}
```
---------
#### AllExtrinsicsLen

##### Python
```python
result = substrate.query(
    'System', 'AllExtrinsicsLen', []
)
```

##### Return value
```python
'u32'
```
---------
#### BlockHash

##### Python
```python
result = substrate.query(
    'System', 'BlockHash', ['u32']
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### BlockWeight

##### Python
```python
result = substrate.query(
    'System', 'BlockWeight', []
)
```

##### Return value
```python
{
    'mandatory': {'proof_size': 'u64', 'ref_time': 'u64'},
    'normal': {'proof_size': 'u64', 'ref_time': 'u64'},
    'operational': {'proof_size': 'u64', 'ref_time': 'u64'},
}
```
---------
#### Digest

##### Python
```python
result = substrate.query(
    'System', 'Digest', []
)
```

##### Return value
```python
{
    'logs': [
        {
            'Other': 'Bytes',
            None: None,
            'Consensus': ('[u8; 4]', 'Bytes'),
            'PreRuntime': ('[u8; 4]', 'Bytes'),
            'RuntimeEnvironmentUpdated': None,
            'Seal': ('[u8; 4]', 'Bytes'),
        },
    ],
}
```
---------
#### EventCount

##### Python
```python
result = substrate.query(
    'System', 'EventCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### EventTopics

##### Python
```python
result = substrate.query(
    'System', 'EventTopics', ['[u8; 32]']
)
```

##### Return value
```python
[('u32', 'u32')]
```
---------
#### Events

##### Python
```python
result = substrate.query(
    'System', 'Events', []
)
```

##### Return value
```python
[
    {
        'event': {
            'Balances': {
                'BalanceSet': {
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u128'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::42',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {'amount': 'u128', 'who': 'AccountId'},
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'CollatorSelection': {
                'CandidateAdded': {
                    'account_id': 'AccountId',
                    'deposit': 'u128',
                },
                'CandidateRemoved': {'account_id': 'AccountId'},
                'NewCandidacyBond': {'bond_amount': 'u128'},
                'NewDesiredCandidates': {'desired_candidates': 'u32'},
                'NewInvulnerables': {'invulnerables': ['AccountId']},
            },
            'Council': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::38',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::38',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'ExternalTabled': None,
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::32'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::33',
                    'voter': 'AccountId',
                },
            },
            'Messages': {
                'MessagesStored': {
                    'block_number': 'u32',
                    'count': 'u16',
                    'schema_id': 'u16',
                },
            },
            'Msa': {
                'DelegationGranted': {
                    'delegator_id': 'u64',
                    'provider_id': 'u64',
                },
                'DelegationRevoked': {
                    'delegator_id': 'u64',
                    'provider_id': 'u64',
                },
                'DelegationUpdated': {
                    'delegator_id': 'u64',
                    'provider_id': 'u64',
                },
                'MsaCreated': {'key': 'AccountId', 'msa_id': 'u64'},
                'MsaRetired': {'msa_id': 'u64'},
                'ProviderCreated': {'provider_id': 'u64'},
                'PublicKeyAdded': {'key': 'AccountId', 'msa_id': 'u64'},
                'PublicKeyDeleted': {'key': 'AccountId'},
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'scale_info::8',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
            'Schemas': {
                'SchemaCreated': {'key': 'AccountId', 'schema_id': 'u16'},
                'SchemaMaxSizeChanged': {'max_size': 'u32'},
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::24',
                    'dispatch_info': 'scale_info::21',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::21'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
            None: None,
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::38',
                    'task': ('u32', 'u32'),
                },
                'PeriodicFailed': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'PermanentlyOverweight': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Scheduled': {'index': 'u32', 'when': 'u32'},
            },
            'TechnicalCommittee': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::38',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::38',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': 'AccountId',
                },
            },
            'Treasury': {
                'Awarded': {
                    'account': 'AccountId',
                    'award': 'u128',
                    'proposal_index': 'u32',
                },
                'Burnt': {'burnt_funds': 'u128'},
                'Deposit': {'value': 'u128'},
                'Proposed': {'proposal_index': 'u32'},
                'Rejected': {'proposal_index': 'u32', 'slashed': 'u128'},
                'Rollover': {'rollover_balance': 'u128'},
                'SpendApproved': {
                    'amount': 'u128',
                    'beneficiary': 'AccountId',
                    'proposal_index': 'u32',
                },
                'Spending': {'budget_remaining': 'u128'},
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::38'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::52',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
            },
        },
        'phase': {
            'ApplyExtrinsic': 'u32',
            'Finalization': None,
            'Initialization': None,
        },
        'topics': ['[u8; 32]'],
    },
]
```
---------
#### ExecutionPhase

##### Python
```python
result = substrate.query(
    'System', 'ExecutionPhase', []
)
```

##### Return value
```python
{'ApplyExtrinsic': 'u32', 'Finalization': None, 'Initialization': None}
```
---------
#### ExtrinsicCount

##### Python
```python
result = substrate.query(
    'System', 'ExtrinsicCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### ExtrinsicData

##### Python
```python
result = substrate.query(
    'System', 'ExtrinsicData', ['u32']
)
```

##### Return value
```python
'Bytes'
```
---------
#### LastRuntimeUpgrade

##### Python
```python
result = substrate.query(
    'System', 'LastRuntimeUpgrade', []
)
```

##### Return value
```python
{'spec_name': 'Str', 'spec_version': 'u32'}
```
---------
#### Number

##### Python
```python
result = substrate.query(
    'System', 'Number', []
)
```

##### Return value
```python
'u32'
```
---------
#### ParentHash

##### Python
```python
result = substrate.query(
    'System', 'ParentHash', []
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### UpgradedToTripleRefCount

##### Python
```python
result = substrate.query(
    'System', 'UpgradedToTripleRefCount', []
)
```

##### Return value
```python
'bool'
```
---------
#### UpgradedToU32RefCount

##### Python
```python
result = substrate.query(
    'System', 'UpgradedToU32RefCount', []
)
```

##### Return value
```python
'bool'
```
---------
### Constants
---------
#### BlockHashCount
##### Value
```python
4096
```
##### Python
```python
constant = substrate.get_constant('System', 'BlockHashCount')
```
---------
#### BlockLength
##### Value
```python
{'max': {'mandatory': 5242880, 'normal': 3932160, 'operational': 5242880}}
```
##### Python
```python
constant = substrate.get_constant('System', 'BlockLength')
```
---------
#### BlockWeights
##### Value
```python
{
    'base_block': {'proof_size': 0, 'ref_time': 5000000000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 125000000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 125000000},
            'max_extrinsic': {'proof_size': 3670016, 'ref_time': 349875000000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 125000000},
            'max_extrinsic': {'proof_size': 4980736, 'ref_time': 474875000000},
            'max_total': {'proof_size': 5242880, 'ref_time': 500000000000},
            'reserved': {'proof_size': 1310720, 'ref_time': 125000000000},
        },
    },
}
```
##### Python
```python
constant = substrate.get_constant('System', 'BlockWeights')
```
---------
#### DbWeight
##### Value
```python
{'read': 25000000, 'write': 100000000}
```
##### Python
```python
constant = substrate.get_constant('System', 'DbWeight')
```
---------
#### SS58Prefix
##### Value
```python
90
```
##### Python
```python
constant = substrate.get_constant('System', 'SS58Prefix')
```
---------
#### Version
##### Value
```python
{
    'apis': [
        ('0xdd718d5cc53262d4', 1),
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 2),
        ('0xea93e3f16f3d6962', 2),
        ('0x54bef602b989d121', 1),
        ('0x02fadd88517cc081', 1),
        ('0x24d062f93a859f6f', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'frequency',
    'impl_version': 0,
    'spec_name': 'frequency',
    'spec_version': 11,
    'state_version': 1,
    'transaction_version': 1,
}
```
##### Python
```python
constant = substrate.get_constant('System', 'Version')
```
---------
### Errors
---------
#### CallFiltered

---------
#### FailedToExtractRuntimeVersion

---------
#### InvalidSpecName

---------
#### NonDefaultComposite

---------
#### NonZeroRefCount

---------
#### SpecVersionNeedsToIncrease

---------

## TechnicalCommittee
---------
### Calls
---------
#### close
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `Weight` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'close', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
#### close_old_weight
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `OldWeight` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'close_old_weight', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': 'u64',
}
)
```

---------
#### disapprove_proposal
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'disapprove_proposal', {'proposal_hash': '[u8; 32]'}
)
```

---------
#### execute
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'execute', {
    'length_bound': 'u32',
    'proposal': 'Call',
}
)
```

---------
#### propose
##### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `MemberCount` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'propose', {
    'length_bound': 'u32',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
#### set_members
##### Attributes
| Name | Type |
| -------- | -------- | 
| new_members | `Vec<T::AccountId>` | 
| prime | `Option<T::AccountId>` | 
| old_count | `MemberCount` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'set_members', {
    'new_members': ['AccountId'],
    'old_count': 'u32',
    'prime': (None, 'AccountId'),
}
)
```

---------
#### vote
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'vote', {
    'approve': 'bool',
    'index': 'u32',
    'proposal': '[u8; 32]',
}
)
```

---------
### Events
---------
#### Approved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Closed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
#### Disapproved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Executed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### MemberExecuted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### Proposed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| threshold | `MemberCount` | ```u32```

---------
#### Voted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| voted | `bool` | ```bool```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Storage functions
---------
#### Members

##### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'Members', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### Prime

##### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'Prime', []
)
```

##### Return value
```python
'AccountId'
```
---------
#### ProposalCount

##### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'ProposalCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### ProposalOf

##### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'ProposalOf', ['[u8; 32]']
)
```

##### Return value
```python
'Call'
```
---------
#### Proposals

##### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'Proposals', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------
#### Voting

##### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'Voting', ['[u8; 32]']
)
```

##### Return value
```python
{'ayes': ['AccountId'], 'end': 'u32', 'index': 'u32', 'nays': ['AccountId'], 'threshold': 'u32'}
```
---------
### Errors
---------
#### AlreadyInitialized

---------
#### DuplicateProposal

---------
#### DuplicateVote

---------
#### NotMember

---------
#### ProposalMissing

---------
#### TooEarly

---------
#### TooManyProposals

---------
#### WrongIndex

---------
#### WrongProposalLength

---------
#### WrongProposalWeight

---------

## Timestamp
---------
### Calls
---------
#### set
##### Attributes
| Name | Type |
| -------- | -------- | 
| now | `T::Moment` | 

##### Python
```python
call = substrate.compose_call(
    'Timestamp', 'set', {'now': 'u64'}
)
```

---------
### Storage functions
---------
#### DidUpdate

##### Python
```python
result = substrate.query(
    'Timestamp', 'DidUpdate', []
)
```

##### Return value
```python
'bool'
```
---------
#### Now

##### Python
```python
result = substrate.query(
    'Timestamp', 'Now', []
)
```

##### Return value
```python
'u64'
```
---------
### Constants
---------
#### MinimumPeriod
##### Value
```python
6000
```
##### Python
```python
constant = substrate.get_constant('Timestamp', 'MinimumPeriod')
```
---------

## TransactionPayment
---------
### Events
---------
#### TransactionFeePaid
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| actual_fee | `BalanceOf<T>` | ```u128```
| tip | `BalanceOf<T>` | ```u128```

---------
### Storage functions
---------
#### NextFeeMultiplier

##### Python
```python
result = substrate.query(
    'TransactionPayment', 'NextFeeMultiplier', []
)
```

##### Return value
```python
'u128'
```
---------
#### StorageVersion

##### Python
```python
result = substrate.query(
    'TransactionPayment', 'StorageVersion', []
)
```

##### Return value
```python
('V1Ancient', 'V2')
```
---------
### Constants
---------
#### OperationalFeeMultiplier
##### Value
```python
5
```
##### Python
```python
constant = substrate.get_constant('TransactionPayment', 'OperationalFeeMultiplier')
```
---------

## Treasury
---------
### Calls
---------
#### approve_proposal
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'approve_proposal', {'proposal_id': 'u32'}
)
```

---------
#### propose_spend
##### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T, I>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'propose_spend', {
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
#### reject_proposal
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'reject_proposal', {'proposal_id': 'u32'}
)
```

---------
#### remove_approval
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'remove_approval', {'proposal_id': 'u32'}
)
```

---------
#### spend
##### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'spend', {
    'amount': 'u128',
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### Events
---------
#### Awarded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| award | `BalanceOf<T, I>` | ```u128```
| account | `T::AccountId` | ```AccountId```

---------
#### Burnt
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| burnt_funds | `BalanceOf<T, I>` | ```u128```

---------
#### Deposit
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| value | `BalanceOf<T, I>` | ```u128```

---------
#### Proposed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```

---------
#### Rejected
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| slashed | `BalanceOf<T, I>` | ```u128```

---------
#### Rollover
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rollover_balance | `BalanceOf<T, I>` | ```u128```

---------
#### SpendApproved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| amount | `BalanceOf<T, I>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
#### Spending
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| budget_remaining | `BalanceOf<T, I>` | ```u128```

---------
### Storage functions
---------
#### Approvals

##### Python
```python
result = substrate.query(
    'Treasury', 'Approvals', []
)
```

##### Return value
```python
['u32']
```
---------
#### Inactive

##### Python
```python
result = substrate.query(
    'Treasury', 'Inactive', []
)
```

##### Return value
```python
'u128'
```
---------
#### ProposalCount

##### Python
```python
result = substrate.query(
    'Treasury', 'ProposalCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### Proposals

##### Python
```python
result = substrate.query(
    'Treasury', 'Proposals', ['u32']
)
```

##### Return value
```python
{
    'beneficiary': 'AccountId',
    'bond': 'u128',
    'proposer': 'AccountId',
    'value': 'u128',
}
```
---------
### Constants
---------
#### Burn
##### Value
```python
0
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'Burn')
```
---------
#### MaxApprovals
##### Value
```python
64
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'MaxApprovals')
```
---------
#### PalletId
##### Value
```python
'0x70792f7472737279'
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'PalletId')
```
---------
#### ProposalBond
##### Value
```python
50000
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBond')
```
---------
#### ProposalBondMaximum
##### Value
```python
100000000000
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMaximum')
```
---------
#### ProposalBondMinimum
##### Value
```python
10000000000
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMinimum')
```
---------
#### SpendPeriod
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'SpendPeriod')
```
---------
### Errors
---------
#### InsufficientPermission

---------
#### InsufficientProposersBalance

---------
#### InvalidIndex

---------
#### ProposalNotApproved

---------
#### TooManyApprovals

---------

## Utility
---------
### Calls
---------
#### as_derivative
##### Attributes
| Name | Type |
| -------- | -------- | 
| index | `u16` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'as_derivative', {'call': 'Call', 'index': 'u16'}
)
```

---------
#### batch
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'batch', {'calls': ['Call']}
)
```

---------
#### batch_all
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_all', {'calls': ['Call']}
)
```

---------
#### dispatch_as
##### Attributes
| Name | Type |
| -------- | -------- | 
| as_origin | `Box<T::PalletsOrigin>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'dispatch_as', {
    'as_origin': {
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
        None: None,
        'Council': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'TechnicalCommittee': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
    },
    'call': 'Call',
}
)
```

---------
#### force_batch
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'force_batch', {'calls': ['Call']}
)
```

---------
#### with_weight
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| weight | `Weight` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'with_weight', {
    'call': 'Call',
    'weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### Events
---------
#### BatchCompleted
##### Attributes
No attributes

---------
#### BatchCompletedWithErrors
##### Attributes
No attributes

---------
#### BatchInterrupted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `u32` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
#### DispatchedAs
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### ItemCompleted
##### Attributes
No attributes

---------
#### ItemFailed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### Constants
---------
#### batched_calls_limit
##### Value
```python
10922
```
##### Python
```python
constant = substrate.get_constant('Utility', 'batched_calls_limit')
```
---------
### Errors
---------
#### TooManyCalls

---------

## Vesting
---------
### Calls
---------
#### claim
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim', {}
)
```

---------
#### claim_for
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim_for', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### update_vesting_schedules
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| vesting_schedules | `Vec<VestingScheduleOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'update_vesting_schedules', {
    'vesting_schedules': [
        {
            'per_period': 'u128',
            'period': 'u32',
            'period_count': 'u32',
            'start': 'u32',
        },
    ],
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### vested_transfer
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `VestingScheduleOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'vested_transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'schedule': {
        'per_period': 'u128',
        'period': 'u32',
        'period_count': 'u32',
        'start': 'u32',
    },
}
)
```

---------
### Events
---------
#### Claimed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
#### VestingScheduleAdded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| vesting_schedule | `VestingScheduleOf<T>` | ```{'start': 'u32', 'period': 'u32', 'period_count': 'u32', 'per_period': 'u128'}```

---------
#### VestingSchedulesUpdated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### Storage functions
---------
#### VestingSchedules

##### Python
```python
result = substrate.query(
    'Vesting', 'VestingSchedules', ['AccountId']
)
```

##### Return value
```python
[
    {
        'per_period': 'u128',
        'period': 'u32',
        'period_count': 'u32',
        'start': 'u32',
    },
]
```
---------
### Constants
---------
#### MinVestedTransfer
##### Value
```python
0
```
##### Python
```python
constant = substrate.get_constant('Vesting', 'MinVestedTransfer')
```
---------
### Errors
---------
#### AmountLow

---------
#### InsufficientBalanceToLock

---------
#### MaxVestingSchedulesExceeded

---------
#### TooManyVestingSchedules

---------
#### ZeroVestingPeriod

---------
#### ZeroVestingPeriodCount

---------