
# PoolRegistry

---------
## Calls

---------
### execute_update
Executed a scheduled update to the pool.

This checks if the scheduled time is in the past
and, if required, if there are no outstanding
redeem orders. If both apply, then the scheduled
changes are applied.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'PoolRegistry', 'execute_update', {'pool_id': 'u64'}
)
```

---------
### register
Create a new pool

Initialise a new pool with the given ID and tranche
configuration. Tranche 0 is the equity tranche, and must
have zero interest and a zero risk buffer.

The minimum epoch length, and maximum NAV age will be
set to chain-wide defaults. They can be updated
with a call to `update`.

The caller will be given the `PoolAdmin` role for
the created pool. Additional administrators can be
added with the Permissions pallet.

Returns an error if the requested pool ID is already in
use, or if the tranche configuration cannot be used.
#### Attributes
| Name | Type |
| -------- | -------- | 
| admin | `T::AccountId` | 
| pool_id | `T::PoolId` | 
| tranche_inputs | `Vec<TrancheInputOf<T>>` | 
| currency | `T::CurrencyId` | 
| max_reserve | `T::Balance` | 
| metadata | `Option<Vec<u8>>` | 
| write_off_policy | `PolicyOf<T>` | 
| pool_fees | `Vec<PoolFeeInputOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'PoolRegistry', 'register', {
    'admin': 'AccountId',
    'currency': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        None: None,
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'max_reserve': 'u128',
    'metadata': (None, 'Bytes'),
    'pool_fees': [
        (
            ('Top', ),
            {
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
        ),
    ],
    'pool_id': 'u64',
    'tranche_inputs': [
        {
            'metadata': {
                'token_name': 'Bytes',
                'token_symbol': 'Bytes',
            },
            'seniority': (None, 'u32'),
            'tranche_type': {
                'NonResidual': {
                    'interest_rate_per_sec': 'u128',
                    'min_risk_buffer': 'u64',
                },
                'Residual': None,
            },
        },
    ],
    'write_off_policy': [
        {
            'status': {
                'penalty': 'u128',
                'percentage': 'u128',
            },
            'triggers': 'scale_info::129',
        },
    ],
}
)
```

---------
### set_metadata
Sets the IPFS hash for the pool metadata information.

The caller must have the `PoolAdmin` role in order to
invoke this extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PoolRegistry', 'set_metadata', {
    'metadata': 'Bytes',
    'pool_id': 'u64',
}
)
```

---------
### update
Update per-pool configuration settings.

This updates the tranches of the pool,
sets the minimum epoch length, and maximum NAV age.

If no delay is required for updates and redemptions
don&\#x27;t have to be fulfilled, then this is executed
immediately. Otherwise, the update is scheduled
to be executed later.

The caller must have the `PoolAdmin` role in order to
invoke this extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| changes | `PoolChangesOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PoolRegistry', 'update', {
    'changes': {
        'max_nav_age': {
            'NewValue': 'u64',
            'NoChange': None,
        },
        'min_epoch_time': {
            'NewValue': 'u64',
            'NoChange': None,
        },
        'tranche_metadata': {
            'NewValue': [
                {
                    'token_name': 'Bytes',
                    'token_symbol': 'Bytes',
                },
            ],
            'NoChange': None,
        },
        'tranches': {
            'NewValue': [
                {
                    'seniority': (
                        None,
                        'u32',
                    ),
                    'tranche_type': {
                        'NonResidual': 'InnerStruct',
                        'Residual': None,
                    },
                },
            ],
            'NoChange': None,
        },
    },
    'pool_id': 'u64',
}
)
```

---------
## Events

---------
### MetadataSet
Pool metadata was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| metadata | `BoundedVec<u8, T::MaxSizeMetadata>` | ```Bytes```

---------
### Registered
A pool was registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```

---------
### UpdateExecuted
A pool update was executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```

---------
### UpdateRegistered
A pool update was registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```

---------
### UpdateStored
A pool update was stored for later execution.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```

---------
## Storage functions

---------
### PoolMetadata

#### Python
```python
result = substrate.query(
    'PoolRegistry', 'PoolMetadata', ['u64']
)
```

#### Return value
```python
{'metadata': 'Bytes'}
```
---------
### Pools

#### Python
```python
result = substrate.query(
    'PoolRegistry', 'Pools', ['u64']
)
```

#### Return value
```python
('Registered', 'Unregistered')
```
---------
## Constants

---------
### MaxSizeMetadata
 Max size of Metadata
#### Value
```python
46
```
#### Python
```python
constant = substrate.get_constant('PoolRegistry', 'MaxSizeMetadata')
```
---------
### MaxTokenNameLength
 Max length for a tranche token name
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('PoolRegistry', 'MaxTokenNameLength')
```
---------
### MaxTokenSymbolLength
 Max length for a tranche token symbol
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('PoolRegistry', 'MaxTokenSymbolLength')
```
---------
### MaxTranches
 Max number of Tranches
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('PoolRegistry', 'MaxTranches')
```
---------
## Errors

---------
### BadMetadata
Invalid metadata passed

---------
### InvalidTrancheUpdate
Pre-requirements for a TrancheUpdate are not met
for example: Tranche changed but not its metadata or vice versa

---------
### MetadataForCurrencyNotFound
No metadata for the given currency found

---------
### NoSuchPoolMetadata
No Metadata found for the given PoolId

---------
### PoolAlreadyRegistered
A Pool with the given ID was already registered in the past

---------
### TrancheSymbolNameTooLong
The given tranche symbol name exceeds the length limit

---------
### TrancheTokenNameTooLong
The given tranche token name exceeds the length limit

---------