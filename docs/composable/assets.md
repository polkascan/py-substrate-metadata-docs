
# Assets

---------
## Calls

---------
### burn_from
Burns `amount` of `asset_id` into the `dest` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'burn_from', {
    'amount': 'u128',
    'asset_id': 'u128',
    'dest': {
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
### force_transfer
Transfer `amount` of the `asset` from `origin` to `dest`. This requires root.

\# Errors
 - When `origin` is not root.
 - If the account has insufficient free balance to make the transfer, or if `keep_alive`
   cannot be respected.
 - If the `dest` cannot be looked up.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `T::AssetId` | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `T::Balance` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_transfer', {
    'asset': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
    'source': {
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
### force_transfer_native
Transfer `amount` of the the native asset from `origin` to `dest`. This requires root.

\# Errors
 - When `origin` is not root.
 - If the account has insufficient free balance to make the transfer, or if `keep_alive`
   cannot be respected.
 - If the `dest` cannot be looked up.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `T::Balance` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_transfer_native', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
    'source': {
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
### mint_initialize
Creates a new asset, minting `amount` of funds into the `dest` account. Intended to be
used for creating wrapped assets, not associated with any project.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `T::Balance` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'mint_initialize', {
    'amount': 'u128',
    'dest': {
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
### mint_initialize_with_governance
Creates a new asset, minting `amount` of funds into the `dest` account. The `dest`
account can use the democracy pallet to mint further assets, or if the governance_origin
is set to an owned account, using signed transactions. In general the
`governance_origin` should be generated from the pallet id.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `T::Balance` | 
| governance_origin | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'mint_initialize_with_governance', {
    'amount': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'governance_origin': {
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
### mint_into
Mints `amount` of `asset_id` into the `dest` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'mint_into', {
    'amount': 'u128',
    'asset_id': 'u128',
    'dest': {
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
### transfer
Transfer `amount` of `asset` from `origin` to `dest`.

\# Errors
 - When `origin` is not signed.
 - If the account has insufficient free balance to make the transfer, or if `keep_alive`
   cannot be respected.
 - If the `dest` cannot be looked up.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `T::AssetId` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| amount | `T::Balance` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer', {
    'amount': 'u128',
    'asset': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
### transfer_all
Transfer all free balance of the `asset` from `origin` to `dest`.

\# Errors
 - When `origin` is not signed.
 - If the `dest` cannot be looked up.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `T::AssetId` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_all', {
    'asset': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
### transfer_all_native
Transfer all free balance of the native asset from `origin` to `dest`.

\# Errors
 - When `origin` is not signed.
 - If the `dest` cannot be looked up.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_all_native', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
### transfer_native
Transfer `amount` of the native asset from `origin` to `dest`. This is slightly
cheaper to call, as it avoids an asset lookup.

\# Errors
 - When `origin` is not signed.
 - If the account has insufficient free balance to make the transfer, or if `keep_alive`
   cannot be respected.
 - If the `dest` cannot be looked up.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `T::Balance` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_native', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
    'value': 'u128',
}
)
```

---------
## Constants

---------
### NativeAssetId
#### Value
```python
79228162514264337593543950338
```
#### Python
```python
constant = substrate.get_constant('Assets', 'NativeAssetId')
```
---------
## Errors

---------
### CannotSetNewCurrencyToRegistry

---------
### InvalidCurrency

---------