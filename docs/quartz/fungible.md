
# Fungible

---------
## Storage functions

---------
### Allowance
 Storage for assets delegated to a limited extent to other users.

#### Python
```python
result = substrate.query(
    'Fungible', 'Allowance', [
    'u32',
    {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### Balance
 Amount of tokens owned by an account inside a collection.

#### Python
```python
result = substrate.query(
    'Fungible', 'Balance', [
    'u32',
    {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### TotalSupply
 Total amount of fungible tokens inside a collection.

#### Python
```python
result = substrate.query(
    'Fungible', 'TotalSupply', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### FungibleDisallowsNesting
Fungible token does not support nesting.

---------
### FungibleItemsDontHaveData
Tried to set data for fungible item.

---------
### FungibleTokensAreAlwaysValid
Only a fungible collection could be possibly broken; any fungible token is valid.

---------
### NotFungibleDataUsedToMintFungibleCollectionToken
Not Fungible item data used to mint in Fungible collection.

---------
### SettingAllowanceForAllNotAllowed
Setting allowance for all is not allowed.

---------
### SettingPropertiesNotAllowed
Setting item properties is not allowed.

---------