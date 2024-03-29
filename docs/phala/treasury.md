
# Treasury

---------
## Calls

---------
### approve_proposal
See [`Pallet::approve_proposal`].
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
See [`Pallet::propose_spend`].
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
See [`Pallet::reject_proposal`].
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
See [`Pallet::remove_approval`].
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
See [`Pallet::spend`].
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
Some funds have been allocated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| award | `BalanceOf<T, I>` | ```u128```
| account | `T::AccountId` | ```AccountId```

---------
### Burnt
Some of our funds have been burnt.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| burnt_funds | `BalanceOf<T, I>` | ```u128```

---------
### Deposit
Some funds have been deposited.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| value | `BalanceOf<T, I>` | ```u128```

---------
### Proposed
New proposal.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```

---------
### Rejected
A proposal was rejected; funds were slashed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| slashed | `BalanceOf<T, I>` | ```u128```

---------
### Rollover
Spending has finished; this is the amount that rolls over until next spend.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rollover_balance | `BalanceOf<T, I>` | ```u128```

---------
### SpendApproved
A new spend proposal has been approved.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| amount | `BalanceOf<T, I>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### Spending
We have ended a spend period and will now allocate funds.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| budget_remaining | `BalanceOf<T, I>` | ```u128```

---------
### UpdatedInactive
The inactive funds of the pallet have been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reactivated | `BalanceOf<T, I>` | ```u128```
| deactivated | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Approvals
 Proposal indices that have been approved but not yet awarded.

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
### Deactivated
 The amount which has been reported as inactive to Currency.

#### Python
```python
result = substrate.query(
    'Treasury', 'Deactivated', []
)
```

#### Return value
```python
'u128'
```
---------
### ProposalCount
 Number of proposals that have been made.

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
 Proposals that have been made.

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
 Percentage of spare funds (if any) that are burnt per spend period.
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
 The maximum number of approvals that can wait in the spending queue.

 NOTE: This parameter is also used within the Bounties Pallet extension if enabled.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'MaxApprovals')
```
---------
### PalletId
 The treasury&#x27;s pallet id, used for deriving its sovereign account ID.
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
 Fraction of a proposal&#x27;s value that should be bonded in order to place the proposal.
 An accepted proposal gets these back. A rejected proposal does not.
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
 Maximum amount of funds that should be placed in a deposit for making a proposal.
#### Value
```python
None
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMaximum')
```
---------
### ProposalBondMinimum
 Minimum amount of funds that should be placed in a deposit for making a proposal.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMinimum')
```
---------
### SpendPeriod
 Period between successive spends.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'SpendPeriod')
```
---------
## Errors

---------
### InsufficientPermission
The spend origin is valid but the amount it is allowed to spend is lower than the
amount to be spent.

---------
### InsufficientProposersBalance
Proposer&\#x27;s balance is too low.

---------
### InvalidIndex
No proposal or bounty at that index.

---------
### ProposalNotApproved
Proposal has not been approved.

---------
### TooManyApprovals
Too many approvals in the queue.

---------