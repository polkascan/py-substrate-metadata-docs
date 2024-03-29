
# PoolFees

---------
## Calls

---------
### apply_new_fee
Execute a successful fee append proposal for the given (pool,
bucket) pair.

Origin unrestriced due to pre-check via proposal gate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| change_id | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'PoolFees', 'apply_new_fee', {
    'change_id': 'scale_info::12',
    'pool_id': 'u64',
}
)
```

---------
### charge_fee
Charge a fee.

Origin must be the fee destination.
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee_id | `T::FeeId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'PoolFees', 'charge_fee', {'amount': 'u128', 'fee_id': 'u64'}
)
```

---------
### propose_new_fee
Propose to append a new fee to the given (pool, bucket) pair.

Origin must be by pool admin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| bucket | `PoolFeeBucket` | 
| fee | `PoolFeeInfoOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PoolFees', 'propose_new_fee', {
    'bucket': ('Top', ),
    'fee': {
        'destination': 'AccountId',
        'editor': {
            'Account': 'AccountId',
            'Root': None,
        },
        'fee_type': {
            'ChargedUpTo': {
                'limit': {
                    'AmountPerSecond': 'u128',
                    'ShareOfPortfolioValuation': 'u128',
                },
            },
            'Fixed': {
                'limit': {
                    'AmountPerSecond': 'u128',
                    'ShareOfPortfolioValuation': 'u128',
                },
            },
        },
    },
    'pool_id': 'u64',
}
)
```

---------
### remove_fee
Remove a fee.

Origin must be the fee editor.
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee_id | `T::FeeId` | 

#### Python
```python
call = substrate.compose_call(
    'PoolFees', 'remove_fee', {'fee_id': 'u64'}
)
```

---------
### uncharge_fee
Cancel a charged fee.

Origin must be the fee destination.
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee_id | `T::FeeId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'PoolFees', 'uncharge_fee', {'amount': 'u128', 'fee_id': 'u64'}
)
```

---------
### update_portfolio_valuation
Update the negative portfolio valuation via pending amounts of the
pool&\#x27;s active fees. Also updates the latter if the last update
happened in the past.

NOTE: There can be fee amounts which are dependent on
AssetsUnderManagement. Therefore, we enforce this to have been
updated in the current timestamp. In the future, this coupling will
be handled by an accounting pallet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'PoolFees', 'update_portfolio_valuation', {'pool_id': 'u64'}
)
```

---------
## Events

---------
### Accrued
A fixed pool fee accrued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| fee_id | `T::FeeId` | ```u64```
| pending | `T::Balance` | ```u128```
| disbursement | `T::Balance` | ```u128```

---------
### Added
A previously proposed and approved pool fee was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| bucket | `PoolFeeBucket` | ```('Top',)```
| fee_id | `T::FeeId` | ```u64```
| fee | `PoolFeeInfoOf<T>` | ```{'destination': 'AccountId', 'editor': {'Root': None, 'Account': 'AccountId'}, 'fee_type': {'Fixed': {'limit': {'ShareOfPortfolioValuation': 'u128', 'AmountPerSecond': 'u128'}}, 'ChargedUpTo': {'limit': {'ShareOfPortfolioValuation': 'u128', 'AmountPerSecond': 'u128'}}}}```

---------
### Charged
A pool fee was charged.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| fee_id | `T::FeeId` | ```u64```
| amount | `T::Balance` | ```u128```
| pending | `T::Balance` | ```u128```

---------
### Paid
A pool fee was paid.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| fee_id | `T::FeeId` | ```u64```
| amount | `T::Balance` | ```u128```
| destination | `T::AccountId` | ```AccountId```

---------
### PortfolioValuationUpdated
The portfolio valuation for a pool was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| valuation | `T::Balance` | ```u128```
| update_type | `PortfolioValuationUpdateType` | ```('Exact', 'Inexact')```

---------
### Proposed
A new pool fee was proposed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| fee_id | `T::FeeId` | ```u64```
| bucket | `PoolFeeBucket` | ```('Top',)```
| fee | `PoolFeeInfoOf<T>` | ```{'destination': 'AccountId', 'editor': {'Root': None, 'Account': 'AccountId'}, 'fee_type': {'Fixed': {'limit': {'ShareOfPortfolioValuation': 'u128', 'AmountPerSecond': 'u128'}}, 'ChargedUpTo': {'limit': {'ShareOfPortfolioValuation': 'u128', 'AmountPerSecond': 'u128'}}}}```

---------
### Removed
A pool fee was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| bucket | `PoolFeeBucket` | ```('Top',)```
| fee_id | `T::FeeId` | ```u64```

---------
### Uncharged
A pool fee was uncharged.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| fee_id | `T::FeeId` | ```u64```
| amount | `T::Balance` | ```u128```
| pending | `T::Balance` | ```u128```

---------
## Storage functions

---------
### ActiveFees
 Represents the active fees for a given pool id and fee bucket. For each
 fee, the limit as well as pending, disbursement and payable amounts are
 included.

 Lifetime of a storage entry: Forever, inherited from pool lifetime.

#### Python
```python
result = substrate.query(
    'PoolFees', 'ActiveFees', ['u64', ('Top', )]
)
```

#### Return value
```python
[
    {
        'amounts': {
            'disbursement': 'u128',
            'fee_type': {'ChargedUpTo': 'InnerStruct', 'Fixed': 'InnerStruct'},
            'payable': {'AllPending': None, 'UpTo': 'u128'},
            'pending': 'u128',
        },
        'destination': 'AccountId',
        'editor': {'Account': 'AccountId', 'Root': None},
        'id': 'u64',
    },
]
```
---------
### AssetsUnderManagement
 Stores the (positive) portfolio valuation associated to each pool
 derived from the AUM of the previous epoch.

 Lifetime of a storage entry: Forever, inherited from pool lifetime.

#### Python
```python
result = substrate.query(
    'PoolFees', 'AssetsUnderManagement', ['u64']
)
```

#### Return value
```python
'u128'
```
---------
### FeeIds
 Maps a pool to their corresponding fee ids with [PoolFeeBucket]
 granularity.

 Lifetime of a storage entry: Forever, inherited from pool lifetime.

#### Python
```python
result = substrate.query(
    'PoolFees', 'FeeIds', ['u64', ('Top', )]
)
```

#### Return value
```python
['u64']
```
---------
### FeeIdsToPoolBucket
 Maps a fee identifier to the corresponding pool and [PoolFeeBucket].

 Lifetime of a storage entry: Forever, inherited from pool lifetime.

#### Python
```python
result = substrate.query(
    'PoolFees', 'FeeIdsToPoolBucket', ['u64']
)
```

#### Return value
```python
('u64', ('Top', ))
```
---------
### LastFeeId
 Source of truth for the last created fee identifier.

 Lifetime: Forever.

#### Python
```python
result = substrate.query(
    'PoolFees', 'LastFeeId', []
)
```

#### Return value
```python
'u64'
```
---------
### PortfolioValuation
 Stores the (negative) portfolio valuation associated to each pool
 derived from the pending fee amounts.

 Lifetime of a storage entry: Forever, inherited from pool lifetime.

#### Python
```python
result = substrate.query(
    'PoolFees', 'PortfolioValuation', ['u64']
)
```

#### Return value
```python
{'last_updated': 'u64', 'value': 'u128', 'values': [('u64', 'u128')]}
```
---------
## Constants

---------
### PalletId
 Identifier of this pallet used as an account which temporarily
 stores disbursing fees in between closing and executing an epoch.
#### Value
```python
'0x6366672f706c6673'
```
#### Python
```python
constant = substrate.get_constant('PoolFees', 'PalletId')
```
---------
## Errors

---------
### CannotBeCharged
Attempted to charge a fee of unchargeable type.

---------
### ChangeIdNotPoolFees
The change id does not belong to a pool fees change.

---------
### FeeIdAlreadyExists
Attempted to add a fee id which already exists.

---------
### FeeNotFound
A fee could not be found.

---------
### MaxPoolFeesPerBucket
The pool bucket has reached the maximum fees size.

---------
### NotPoolAdmin
Only the PoolAdmin can execute a given operation.

---------
### NothingCharged
Attempted to charge with zero amount

---------
### NothingUncharged
Attempted to uncharge with zero amount

---------
### PoolNotFound
A pool could not be found.

---------
### UnauthorizedCharge
The fee can only be charged by the destination.

---------
### UnauthorizedEdit
The fee can only be edited or removed by the editor.

---------