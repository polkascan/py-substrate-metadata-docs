
# Bounties

---------
## Calls

---------
### accept_curator
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'accept_curator', {'bounty_id': 'u32'}
)
```

---------
### approve_bounty
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'approve_bounty', {'bounty_id': 'u32'}
)
```

---------
### award_bounty
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'award_bounty', {
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'bounty_id': 'u32',
}
)
```

---------
### claim_bounty
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'claim_bounty', {'bounty_id': 'u32'}
)
```

---------
### close_bounty
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'close_bounty', {'bounty_id': 'u32'}
)
```

---------
### extend_bounty_expiry
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'extend_bounty_expiry', {
    'bounty_id': 'u32',
    'remark': 'Bytes',
}
)
```

---------
### propose_bounty
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T, I>` | 
| description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'propose_bounty', {
    'description': 'Bytes',
    'value': 'u128',
}
)
```

---------
### propose_curator
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 
| curator | `AccountIdLookupOf<T>` | 
| fee | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'propose_curator', {
    'bounty_id': 'u32',
    'curator': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'fee': 'u128',
}
)
```

---------
### unassign_curator
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'unassign_curator', {'bounty_id': 'u32'}
)
```

---------
## Events

---------
### BountyAwarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### BountyBecameActive
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyCanceled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| payout | `BalanceOf<T, I>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### BountyExtended
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyProposed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyRejected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| bond | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Bounties

#### Python
```python
result = substrate.query(
    'Bounties', 'Bounties', ['u32']
)
```

#### Return value
```python
{
    'bond': 'u128',
    'curator_deposit': 'u128',
    'fee': 'u128',
    'proposer': 'AccountId',
    'status': {
        'Active': {'curator': 'AccountId', 'update_due': 'u32'},
        'Approved': None,
        'CuratorProposed': {'curator': 'AccountId'},
        'Funded': None,
        'PendingPayout': {
            'beneficiary': 'AccountId',
            'curator': 'AccountId',
            'unlock_at': 'u32',
        },
        'Proposed': None,
    },
    'value': 'u128',
}
```
---------
### BountyApprovals

#### Python
```python
result = substrate.query(
    'Bounties', 'BountyApprovals', []
)
```

#### Return value
```python
['u32']
```
---------
### BountyCount

#### Python
```python
result = substrate.query(
    'Bounties', 'BountyCount', []
)
```

#### Return value
```python
'u32'
```
---------
### BountyDescriptions

#### Python
```python
result = substrate.query(
    'Bounties', 'BountyDescriptions', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
## Constants

---------
### BountyDepositBase
#### Value
```python
2000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyDepositBase')
```
---------
### BountyDepositPayoutDelay
#### Value
```python
28800
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyDepositPayoutDelay')
```
---------
### BountyUpdatePeriod
#### Value
```python
252000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyUpdatePeriod')
```
---------
### BountyValueMinimum
#### Value
```python
5000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyValueMinimum')
```
---------
### CuratorDepositMax
#### Value
```python
100000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'CuratorDepositMax')
```
---------
### CuratorDepositMin
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'CuratorDepositMin')
```
---------
### CuratorDepositMultiplier
#### Value
```python
500000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'CuratorDepositMultiplier')
```
---------
### DataDepositPerByte
#### Value
```python
300000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'DataDepositPerByte')
```
---------
### MaximumReasonLength
#### Value
```python
8192
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'MaximumReasonLength')
```
---------
## Errors

---------
### HasActiveChildBounty

---------
### InsufficientProposersBalance

---------
### InvalidFee

---------
### InvalidIndex

---------
### InvalidValue

---------
### PendingPayout

---------
### Premature

---------
### ReasonTooBig

---------
### RequireCurator

---------
### TooManyQueued

---------
### UnexpectedStatus

---------