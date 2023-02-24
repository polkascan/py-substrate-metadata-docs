
# Nft

---------
## Calls

---------
### active
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(T::ClassId, T::TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'active', {'token': ('u32', 'u32')}
)
```

---------
### burn
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(T::ClassId, T::TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'burn', {'token': ('u32', 'u32')}
)
```

---------
### buy_token
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(T::ClassId, T::TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'buy_token', {'token': ('u32', 'u32')}
)
```

---------
### claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(T::ClassId, T::TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'claim', {'token': ('u32', 'u32')}
)
```

---------
### create_class
#### Attributes
| Name | Type |
| -------- | -------- | 
| metadata | `Vec<u8>` | 
| data | `ClassDataOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'create_class', {
    'data': {
        'claim_payment': 'u128',
        'images_hash': (None, 'Bytes'),
        'level': {
            'Angle': None,
            'GrandMaster': None,
            'Mafia': None,
            'Other': 'Bytes',
            'Rookie': None,
            'UnicornHunter': None,
            'WallStreetElite': None,
        },
        'maximum_quantity': 'u32',
        'power_threshold': 'u128',
    },
    'metadata': 'Bytes',
}
)
```

---------
### inactive
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(T::ClassId, T::TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'inactive', {'token': ('u32', 'u32')}
)
```

---------
### mint
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `T::ClassId` | 
| metadata | `Vec<u8>` | 
| attribute | `Vec<u8>` | 
| image_hash | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'mint', {
    'attribute': 'Bytes',
    'class_id': 'u32',
    'image_hash': 'Bytes',
    'metadata': 'Bytes',
}
)
```

---------
### offer_token_for_sale
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(T::ClassId, T::TokenId)` | 
| price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'offer_token_for_sale', {
    'price': 'u128',
    'token': ('u32', 'u32'),
}
)
```

---------
### transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| token | `(T::ClassId, T::TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'transfer', {
    'to': 'AccountId',
    'token': ('u32', 'u32'),
}
)
```

---------
### withdraw_sale
#### Attributes
| Name | Type |
| -------- | -------- | 
| token | `(T::ClassId, T::TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'withdraw_sale', {'token': ('u32', 'u32')}
)
```

---------
## Events

---------
### Active
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `(T::ClassId, T::TokenId)` | ```('u32', 'u32')```

---------
### Burn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::ClassId` | ```u32```
| None | `T::TokenId` | ```u32```

---------
### BuyToken
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::ClassId` | ```u32```
| None | `T::TokenId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### Claim
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::ClassId` | ```u32```
| None | `T::TokenId` | ```u32```

---------
### CreateClass
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::ClassId` | ```u32```

---------
### DestroyClass
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::ClassId` | ```u32```

---------
### Inactive
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `(T::ClassId, T::TokenId)` | ```('u32', 'u32')```

---------
### Mint
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::ClassId` | ```u32```
| None | `T::TokenId` | ```u32```

---------
### OfferTokenForSale
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::ClassId` | ```u32```
| None | `T::TokenId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### Transfer
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `(T::ClassId, T::TokenId)` | ```('u32', 'u32')```

---------
### WithdrawSale
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::ClassId` | ```u32```
| None | `T::TokenId` | ```u32```

---------
## Storage functions

---------
### AllTokensHash

#### Python
```python
result = substrate.query(
    'Nft', 'AllTokensHash', []
)
```

#### Return value
```python
'scale_info::225'
```
---------
### Classes
 Store class info.

 Returns `None` if class info not set or removed.

#### Python
```python
result = substrate.query(
    'Nft', 'Classes', ['u32']
)
```

#### Return value
```python
{
    'data': {
        'claim_payment': 'u128',
        'images_hash': (None, 'Bytes'),
        'level': {
            'Angle': None,
            'GrandMaster': None,
            'Mafia': None,
            'Other': 'Bytes',
            'Rookie': None,
            'UnicornHunter': None,
            'WallStreetElite': None,
        },
        'maximum_quantity': 'u32',
        'power_threshold': 'u128',
    },
    'issuer': 'AccountId',
    'metadata': 'Bytes',
    'total_issuance': 'u32',
}
```
---------
### Daos

#### Python
```python
result = substrate.query(
    'Nft', 'Daos', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### InSaleTokens

#### Python
```python
result = substrate.query(
    'Nft', 'InSaleTokens', ['u32']
)
```

#### Return value
```python
[
    {
        'price': 'u128',
        'seller': 'AccountId',
        'start_block': 'u32',
        'token_id': 'u32',
    },
]
```
---------
### IssuerOf

#### Python
```python
result = substrate.query(
    'Nft', 'IssuerOf', [
    {
        'Angle': None,
        'GrandMaster': None,
        'Mafia': None,
        'Other': 'Bytes',
        'Rookie': None,
        'UnicornHunter': None,
        'WallStreetElite': None,
    },
]
)
```

#### Return value
```python
('AccountId', 'u32')
```
---------
### Locks

#### Python
```python
result = substrate.query(
    'Nft', 'Locks', []
)
```

#### Return value
```python
'scale_info::522'
```
---------
### NextClassId
 Next available class ID.

#### Python
```python
result = substrate.query(
    'Nft', 'NextClassId', []
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
    'Nft', 'NextTokenId', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### NoOwnerTokensOf

#### Python
```python
result = substrate.query(
    'Nft', 'NoOwnerTokensOf', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
### Tokens
 Store token info.

 Returns `None` if token info not set or removed.

#### Python
```python
result = substrate.query(
    'Nft', 'Tokens', ['u32', 'u32']
)
```

#### Return value
```python
{
    'data': {
        'attribute': 'Bytes',
        'claim_payment': 'u128',
        'class_id': 'u32',
        'hash': '[u8; 32]',
        'image_hash': 'Bytes',
        'power_threshold': 'u128',
        'sell_records': [('AccountId', 'u128')],
        'status': {
            'is_active_image': 'bool',
            'is_claimed': 'bool',
            'is_in_sale': 'bool',
        },
    },
    'metadata': 'Bytes',
    'owner': (None, 'AccountId'),
}
```
---------
### TokensOf
 the user&#x27;s all tokens

#### Python
```python
result = substrate.query(
    'Nft', 'TokensOf', ['AccountId']
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
## Errors

---------
### ActiveNft

---------
### CannotDestroyClass
Can not destroy class
Total issuance is not 0

---------
### ClassNotFound
Class not found

---------
### DaoExists

---------
### FeeErr

---------
### InSale


---------
### InUse

---------
### Inactive

---------
### LevelInUse


---------
### Locked

---------
### MaxAttributeExceeded

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
### NoLocked

---------
### NoPermission
The operator is not the owner of the token and has no permission

---------
### NoPermissionNFTLevel

---------
### NotClaim

---------
### NotInSale

---------
### NotIssuer

---------
### NotOwner

---------
### OwnerIsExists

---------
### OwnerNotExists

---------
### PowerTooLow

---------
### TokenAlreadyExists

---------
### TokenNotFound
Token(ClassId, TokenId) not found

---------