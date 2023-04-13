
# OrmlNFT

---------
## Storage functions

---------
### Classes
 Store class info.

 Returns `None` if class info not set or removed.

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'Classes', ['u32']
)
```

#### Return value
```python
{
    'data': {
        'attributes': 'scale_info::276',
        'collection_type': {
            'Collectable': None,
            'Executable': 'Bytes',
            'Wearable': None,
        },
        'deposit': 'u128',
        'is_locked': 'bool',
        'mint_limit': (None, 'u32'),
        'royalty_fee': 'u32',
        'token_type': ('Transferable', 'BoundToAddress'),
        'total_minted_tokens': 'u32',
    },
    'metadata': 'Bytes',
    'owner': 'AccountId',
    'total_issuance': 'u64',
}
```
---------
### NextClassId
 Next available class ID.

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'NextClassId', []
)
```

#### Return value
```python
'u32'
```
---------
### NextTokenId
 Next available token ID.

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'NextTokenId', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### StackableCollection
 Index stackable collections by (class ID, token ID)

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'StackableCollection', [('u32', 'u64')]
)
```

#### Return value
```python
()
```
---------
### StackableCollectionsBalances
 Index stackable collections balances

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'StackableCollectionsBalances', ['u32', 'u64', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### Tokens
 Store token info.

 Returns `None` if token info not set or removed.

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'Tokens', ['u32', 'u64']
)
```

#### Return value
```python
{
    'data': {
        'attributes': 'scale_info::276',
        'deposit': 'u128',
        'is_locked': 'bool',
    },
    'metadata': 'Bytes',
    'owner': 'AccountId',
}
```
---------
### TokensByOwner
 Token existence check by owner and class ID.

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'TokensByOwner', ['AccountId', 'u32', 'u64']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### CannotDestroyClass
Can not destroy class
Total issuance is not 0

---------
### ClassNotFound
Class not found

---------
### InvalidStackableNftAmount
Invalid stackable NFT balance

---------
### InvalidStackableNftTransfer
Invalid stackable NFT transfer (stored value is equal to zero)

---------
### MaxMetadataExceeded
Failed because the Maximum amount of metadata was exceeded

---------
### NoAvailableClassId
No available class ID

---------
### NoAvailableTokenId
No available token ID

---------
### NoPermission
The operator is not the owner of the token and has no permission

---------
### StackableCollectionAlreadyExists
The stackable collection already exists

---------
### TokenAlreadyExist
Token already exists

---------
### TokenIdRequired
This collection is not autoincrement id

---------
### TokenNotFound
Token(ClassId, TokenId) not found

---------