
# XAssets

---------
## Calls

---------
### force_transfer
transfer method reserved for root(sudo)
#### Attributes
| Name | Type |
| -------- | -------- | 
| transactor | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| id | `AssetId` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XAssets', 'force_transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'id': 'u32',
    'transactor': {
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
### set_asset_limit
asset restriction method reserved for root
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `AssetId` | 
| restrictions | `AssetRestrictions` | 

#### Python
```python
call = substrate.compose_call(
    'XAssets', 'set_asset_limit', {
    'id': 'u32',
    'restrictions': {'bits': 'u32'},
}
)
```

---------
### set_balance
set free token for an account
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| id | `AssetId` | 
| balances | `BTreeMap<AssetType, BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'XAssets', 'set_balance', {
    'balances': 'scale_info::258',
    'id': 'u32',
    'who': {
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
transfer between two accounts
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| id | `AssetId` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XAssets', 'transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'id': 'u32',
    'value': 'u128',
}
)
```

---------
## Events

---------
### BalanceSet
Set asset balance of an account by root. [asset_id, who, asset_type, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `AssetType` | ```('Usable', 'Locked', 'Reserved', 'ReservedWithdrawal', 'ReservedDexSpot')```
| None | `BalanceOf<T>` | ```u128```

---------
### Destroyed
Some balances of an asset were destoryed. [asset_id, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Issued
New balances of an asset were issued. [asset_id, receiver, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Moved
Some balances of an asset was moved from one to another. [asset_id, from, from_type, to, to_type, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `AssetType` | ```('Usable', 'Locked', 'Reserved', 'ReservedWithdrawal', 'ReservedDexSpot')```
| None | `T::AccountId` | ```AccountId```
| None | `AssetType` | ```('Usable', 'Locked', 'Reserved', 'ReservedWithdrawal', 'ReservedDexSpot')```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AssetBalance
 asset balance for user&amp;asset_id, use btree_map to accept different asset type

#### Python
```python
result = substrate.query(
    'XAssets', 'AssetBalance', ['AccountId', 'u32']
)
```

#### Return value
```python
'scale_info::258'
```
---------
### AssetRestrictionsOf
 asset extend limit properties, set asset &quot;can do&quot;, example, `CanTransfer`, `CanDestroyWithdrawal`
 notice if not set AssetRestriction, default is true for this limit
 if want let limit make sense, must set false for the limit

#### Python
```python
result = substrate.query(
    'XAssets', 'AssetRestrictionsOf', ['u32']
)
```

#### Return value
```python
{'bits': 'u32'}
```
---------
### TotalAssetBalance
 asset balance for an asset_id, use btree_map to accept different asset type

#### Python
```python
result = substrate.query(
    'XAssets', 'TotalAssetBalance', ['u32']
)
```

#### Return value
```python
'scale_info::258'
```
---------
## Errors

---------
### ActionNotAllowed
Action is not allowed.

---------
### AmountIntoBalanceFailed
Cannot convert Amount into Balance type

---------
### DenyNativeAsset
 Not Allow native asset,

---------
### InsufficientBalance
Balance too low to send value

---------
### InvalidAsset
Got and Invalid Asset

---------
### LiquidityRestrictions
Failed because liquidity restrictions due to locking

---------
### NoProvider
Unable to increment the consumer reference counters on the account. Either no provider
reference exists to allow a non-zero balance of a non-self-sufficient asset, or the
maximum number of consumers has been reached.

---------
### Overflow
Got an overflow after adding

---------
### StillHasActiveReserved
Account still has active reserved

---------
### TotalAssetInsufficientBalance
Balance too low to send value

---------
### TotalAssetOverflow
Got an overflow after adding

---------