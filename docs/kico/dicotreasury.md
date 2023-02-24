
# DicoTreasury

---------
## Calls

---------
### approve_proposal
The council approve the proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DicoTreasury', 'approve_proposal', {'proposal_id': 'u32'}
)
```

---------
### propose_spend
The user makes a proposal about funding
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| value | `BalanceOf<T>` | 
| beneficiary | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'DicoTreasury', 'propose_spend', {
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'currency_id': 'u32',
    'value': 'u128',
}
)
```

---------
### reject_proposal
The council rejected the proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DicoTreasury', 'reject_proposal', {'proposal_id': 'u32'}
)
```

---------
### spend_fund
Users get their fund.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DicoTreasury', 'spend_fund', {}
)
```

---------
## Events

---------
### Approved
A proposal was approved;
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalIndex` | ```u32```

---------
### Awarded
Some funds have been allocated. \[proposal_index, award, beneficiary\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalIndex` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```

---------
### Burnt
Some of our funds have been burnt. \[burn\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### Deposit
Some funds have been deposited. \[deposit\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### Proposed
New proposal. \[proposal_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalIndex` | ```u32```

---------
### Rejected
A proposal was rejected; funds were slashed. \[proposal_index, slashed\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalIndex` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### Rollover
Spending has finished; this is the amount that rolls over until next spend.
\[budget_remaining\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### SpendFund
#### Attributes
No attributes

---------
### Spending
We have ended a spend period and will now allocate funds. \[budget_remaining\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Approvals

#### Python
```python
result = substrate.query(
    'DicoTreasury', 'Approvals', []
)
```

#### Return value
```python
['u32']
```
---------
### ProposalCount

#### Python
```python
result = substrate.query(
    'DicoTreasury', 'ProposalCount', []
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
    'DicoTreasury', 'Proposals', ['u32']
)
```

#### Return value
```python
{
    'beneficiary': 'AccountId',
    'bond': 'u128',
    'currency_id': 'u32',
    'proposer': 'AccountId',
    'start_spend_time': (None, 'u32'),
    'value': 'u128',
}
```
---------
## Constants

---------
### GetNativeCurrencyId
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('DicoTreasury', 'GetNativeCurrencyId')
```
---------
### PalletId
#### Value
```python
'0x70792f7472737279'
```
#### Python
```python
constant = substrate.get_constant('DicoTreasury', 'PalletId')
```
---------
### ProposalBond
 Minimum amount of funds that should be placed in a deposit for making a
 proposal.
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('DicoTreasury', 'ProposalBond')
```
---------
## Errors

---------
### ApprovalsIsempty

---------
### InsufficientProposersBalance
Proposer&\#x27;s balance is too low.

---------
### InvalidIndex
No proposal or bounty at that index.

---------