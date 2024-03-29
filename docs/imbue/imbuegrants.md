
# ImbueGrants

---------
## Calls

---------
### create_and_convert
See [`Pallet::create_and_convert`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposed_milestones | `BoundedPMilestones<T>` | 
| assigned_approvers | `BoundedApprovers<T>` | 
| currency_id | `CurrencyId` | 
| amount_requested | `BalanceOf<T>` | 
| treasury_origin | `TreasuryOrigin` | 
| grant_id | `GrantId` | 
| external_owned_address | `Option<common_types::ForeignOwnedAccount>` | 

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
        'ForeignAsset': (
            'ETH',
            'USDT',
        ),
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'external_owned_address': (
        None,
        {
            'ETH': '[u8; 20]',
            'TRON': '[u8; 22]',
        },
    ),
    'grant_id': 'scale_info::12',
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
| grant_id | `GrantId` | ```scale_info::12```

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
    'ImbueGrants', 'GrantsSubmitted', ['scale_info::12']
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
    'ImbueGrants', 'GrantsSubmittedBy', ['AccountId', 'scale_info::12']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### CurrencyAccountComboNotSupported
Currency is not supported for this external address.

---------
### EoaRequiredForForeignCurrencies
If youre using a foreign currency then you need an external_owned_address.

---------
### GrantAlreadyExists
The grant already exists.

---------
### GrantNotFound
The GrantId specified cannot be found.

---------
### InvalidTreasuryOrigin
This is an invalid Treasury origin.

---------
### MustSumTo100
Milestones must sum to 100

---------
### TooManyApprovers
Too many approvers

---------
### TooManyMilestones
There are too many milestones.

---------