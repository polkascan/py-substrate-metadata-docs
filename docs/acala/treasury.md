
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
### check_status
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `SpendIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'check_status', {'index': 'u32'}
)
```

---------
### payout
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `SpendIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'payout', {'index': 'u32'}
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
        'Index': 'u32',
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
| asset_kind | `Box<T::AssetKind>` | 
| amount | `AssetBalanceOf<T, I>` | 
| beneficiary | `Box<BeneficiaryLookupOf<T, I>>` | 
| valid_from | `Option<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'spend', {
    'amount': 'u128',
    'asset_kind': (),
    'beneficiary': 'AccountId',
    'valid_from': (None, 'u32'),
}
)
```

---------
### spend_local
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'spend_local', {
    'amount': 'u128',
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### void_spend
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `SpendIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'void_spend', {'index': 'u32'}
)
```

---------
## Events

---------
### AssetSpendApproved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `SpendIndex` | ```u32```
| asset_kind | `T::AssetKind` | ```()```
| amount | `AssetBalanceOf<T, I>` | ```u128```
| beneficiary | `T::Beneficiary` | ```AccountId```
| valid_from | `BlockNumberFor<T>` | ```u32```
| expire_at | `BlockNumberFor<T>` | ```u32```

---------
### AssetSpendVoided
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `SpendIndex` | ```u32```

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
### Paid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `SpendIndex` | ```u32```
| payment_id | `<T::Paymaster as Pay>::Id` | ```()```

---------
### PaymentFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `SpendIndex` | ```u32```
| payment_id | `<T::Paymaster as Pay>::Id` | ```()```

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
### SpendProcessed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `SpendIndex` | ```u32```

---------
### Spending
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| budget_remaining | `BalanceOf<T, I>` | ```u128```

---------
### UpdatedInactive
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reactivated | `BalanceOf<T, I>` | ```u128```
| deactivated | `BalanceOf<T, I>` | ```u128```

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
### Deactivated

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
### SpendCount

#### Python
```python
result = substrate.query(
    'Treasury', 'SpendCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Spends

#### Python
```python
result = substrate.query(
    'Treasury', 'Spends', ['u32']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'asset_kind': (),
    'beneficiary': 'AccountId',
    'expire_at': 'u32',
    'status': {'Attempted': {'id': ()}, 'Failed': None, 'Pending': None},
    'valid_from': 'u32',
}
```
---------
## Constants

---------
### Burn
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'Burn')
```
---------
### MaxApprovals
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'MaxApprovals')
```
---------
### PalletId
#### Value
```python
'0x6163612f74727379'
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'PalletId')
```
---------
### PayoutPeriod
#### Value
```python
216000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'PayoutPeriod')
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
50000000000000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMaximum')
```
---------
### ProposalBondMinimum
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMinimum')
```
---------
### SpendPeriod
#### Value
```python
216000
```
#### Python
```python
constant = substrate.get_constant('Treasury', 'SpendPeriod')
```
---------
## Errors

---------
### AlreadyAttempted

---------
### EarlyPayout

---------
### FailedToConvertBalance

---------
### Inconclusive

---------
### InsufficientPermission

---------
### InsufficientProposersBalance

---------
### InvalidIndex

---------
### NotAttempted

---------
### PayoutError

---------
### ProposalNotApproved

---------
### SpendExpired

---------
### TooManyApprovals

---------