
# Treasury

---------
## Calls

---------
### approve_proposal
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'approve_proposal', {'proposal_id': 'u32'}
)
```

---------
### propose_spend
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T, I>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
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
### reject_proposal
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'reject_proposal', {'proposal_id': 'u32'}
)
```

---------
### remove_approval
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'remove_approval', {'proposal_id': 'u32'}
)
```

---------
### spend
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
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
## Events

---------
### Awarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| award | `BalanceOf<T, I>` | ```u128```
| account | `T::AccountId` | ```AccountId```

---------
### Burnt
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| burnt_funds | `BalanceOf<T, I>` | ```u128```

---------
### Deposit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| value | `BalanceOf<T, I>` | ```u128```

---------
### Proposed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```

---------
### Rejected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| slashed | `BalanceOf<T, I>` | ```u128```

---------
### Rollover
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rollover_balance | `BalanceOf<T, I>` | ```u128```

---------
### SpendApproved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| amount | `BalanceOf<T, I>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### Spending
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| budget_remaining | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Approvals

#### Python
```python
result = substrate.query(
    'Treasury', 'Approvals', []
)
```

#### Return value
```python
['u32']
```
---------
### Inactive

#### Python
```python
result = substrate.query(
    'Treasury', 'Inactive', []
)
```

#### Return value
```python
'u128'
```
---------
### ProposalCount

#### Python
```python
result = substrate.query(
    'Treasury', 'ProposalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Proposals

#### Python
```python
result = substrate.query(
    'Treasury', 'Proposals', ['u32']
)
```

#### Return value
```python
{
    'beneficiary': 'AccountId',
    'bond': 'u128',
    'proposer': 'AccountId',
    'value': 'u128',
}
```
---------
## Constants

---------
### Burn
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'Burn')
```
---------
### MaxApprovals
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'MaxApprovals')
```
---------
### PalletId
#### Value
```python
'0x70792f7472737279'
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'PalletId')
```
---------
### ProposalBond
#### Value
```python
50000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBond')
```
---------
### ProposalBondMaximum
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMaximum')
```
---------
### ProposalBondMinimum
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMinimum')
```
---------
### SpendPeriod
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'SpendPeriod')
```
---------
## Errors

---------
### InsufficientPermission

---------
### InsufficientProposersBalance

---------
### InvalidIndex

---------
### ProposalNotApproved

---------
### TooManyApprovals

---------