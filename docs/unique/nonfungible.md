
# Nonfungible

---------
## Storage functions

---------
### AccountBalance
 Amount of tokens owned by an account in a collection.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'AccountBalance', [
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
 Allowance set by a token owner for another user to perform one of certain transactions on a token.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'Allowance', ['u32', 'u32']
)
```

#### Return value
```python
{'Ethereum': '[u8; 20]', 'Substrate': 'AccountId'}
```
---------
### CollectionAllowance
 Operator set by a wallet owner that could perform certain transactions on all tokens in the wallet.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'CollectionAllowance', [
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
    'Nonfungible', 'Owned', [
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
### TokenAuxProperties
 Custom data of a token that is serialized to bytes,
 primarily reserved for on-chain operations,
 normally obscured from the external users.

 Auxiliary properties are slightly different from
 usual [`TokenProperties`] due to an unlimited number
 and separately stored and written-to key-value pairs.

 Currently unused.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'TokenAuxProperties', ['u32', 'u32', ('None', 'Rmrk'), 'Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### TokenChildren
 Used to enumerate token&#x27;s children.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'TokenChildren', ['u32', 'u32', ('u32', 'u32')]
)
```

#### Return value
```python
'bool'
```
---------
### TokenData
 Token data, used to partially describe a token.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'TokenData', ['u32', 'u32']
)
```

#### Return value
```python
{'owner': {'Ethereum': '[u8; 20]', 'Substrate': 'AccountId'}}
```
---------
### TokenProperties
 Map of key-value pairs, describing the metadata of a token.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'TokenProperties', ['u32', 'u32']
)
```

#### Return value
```python
{'consumed_space': 'u32', 'map': 'scale_info::352', 'space_limit': 'u32'}
```
---------
### TokensBurnt
 Amount of burnt tokens in a collection.

#### Python
```python
result = substrate.query(
    'Nonfungible', 'TokensBurnt', ['u32']
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
    'Nonfungible', 'TokensMinted', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### CantBurnNftWithChildren
Unable to burn NFT with children

---------
### NonfungibleItemsHaveNoAmount
Used amount &gt; 1 with NFT

---------
### NotNonfungibleDataUsedToMintFungibleCollectionToken
Not Nonfungible item data used to mint in Nonfungible collection.

---------