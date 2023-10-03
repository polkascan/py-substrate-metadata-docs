
# Refungible

---------
## Storage functions

---------
### AccountBalance
 Amount of tokens (not pieces) partially owned by an account within a collection.

#### Python
```python
result = substrate.query(
    'Refungible', 'AccountBalance', [
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
'u32'
```
---------
### Allowance
 Allowance set by a token owner for another user to perform one of certain transactions on a number of pieces of a token.

#### Python
```python
result = substrate.query(
    'Refungible', 'Allowance', [
    'u32',
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
 Amount of token pieces owned by account.

#### Python
```python
result = substrate.query(
    'Refungible', 'Balance', [
    'u32',
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
### CollectionAllowance
 Spender set by a wallet owner that could perform certain transactions on all tokens in the wallet.

#### Python
```python
result = substrate.query(
    'Refungible', 'CollectionAllowance', [
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
'bool'
```
---------
### Owned
 Used to enumerate tokens owned by account.

#### Python
```python
result = substrate.query(
    'Refungible', 'Owned', [
    'u32',
    {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'u32',
]
)
```

#### Return value
```python
'bool'
```
---------
### TokenProperties
 Amount of pieces a refungible token is split into.

#### Python
```python
result = substrate.query(
    'Refungible', 'TokenProperties', ['u32', 'u32']
)
```

#### Return value
```python
{'_reserved': 'u32', 'consumed_space': 'u32', 'map': 'scale_info::581'}
```
---------
### TokensBurnt
 Amount of tokens burnt in a collection.

#### Python
```python
result = substrate.query(
    'Refungible', 'TokensBurnt', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### TokensMinted
 Total amount of minted tokens in a collection.

#### Python
```python
result = substrate.query(
    'Refungible', 'TokensMinted', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### TotalSupply
 Total amount of pieces for token

#### Python
```python
result = substrate.query(
    'Refungible', 'TotalSupply', ['u32', 'u32']
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### NotRefungibleDataUsedToMintFungibleCollectionToken
Not Refungible item data used to mint in Refungible collection.

---------
### RefungibleDisallowsNesting
Refungible token can&\#x27;t nest other tokens.

---------
### RepartitionWhileNotOwningAllPieces
Refungible token can&\#x27;t be repartitioned by user who isn&\#x27;t owns all pieces.

---------
### SettingPropertiesNotAllowed
Setting item properties is not allowed.

---------
### WrongRefungiblePieces
Maximum refungibility exceeded.

---------