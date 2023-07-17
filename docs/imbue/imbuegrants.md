
# ImbueGrants

---------
## Calls

---------
### create_and_convert
Instead of iterating, create a project from the parameters of a grant.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposed_milestones | `BoundedPMilestones<T>` | 
| assigned_approvers | `BoundedApprovers<T>` | 
| currency_id | `CurrencyId` | 
| amount_requested | `BalanceOf<T>` | 
| treasury_origin | `TreasuryOrigin` | 
| grant_id | `GrantId` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueGrants', 'create_and_convert', {
    'amount_requested': 'u128',
    'assigned_approvers': [
        'AccountId',
    ],
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'grant_id': '[u8; 32]',
    'proposed_milestones': [
        {'percentage_to_unlock': 'u8'},
    ],
    'treasury_origin': (
        'Kusama',
        'Imbue',
        'Karura',
    ),
}
)
```

---------
## Events

---------
### GrantSubmitted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| submitter | `AccountIdOf<T>` | ```AccountId```
| grant_id | `GrantId` | ```[u8; 32]```

---------
## Storage functions

---------
### GrantCount

#### Python
```python
result = substrate.query(
    'ImbueGrants', 'GrantCount', []
)
```

#### Return value
```python
'u32'
```
---------
### GrantsSubmitted
 Used to check wether a grant_id has already been submitted.

#### Python
```python
result = substrate.query(
    'ImbueGrants', 'GrantsSubmitted', ['[u8; 32]']
)
```

#### Return value
```python
()
```
---------
### GrantsSubmittedBy
 Stores all the grants a user has submitted.
 Key 1: AccountId
 Key 2: GrantId
 Value: ()

#### Python
```python
result = substrate.query(
    'ImbueGrants', 'GrantsSubmittedBy', ['AccountId', '[u8; 32]']
)
```

#### Return value
```python
()
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'ImbueGrants', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1', 'V2')
```
---------
## Errors

---------
### GrantAlreadyExists
The grant already exists.

---------
### GrantNotFound
The GrantId specified cannot be found.

---------
### MustSumTo100
Milestones must sum to 100

---------
### TooManyMilestones
There are too many milestones.

---------