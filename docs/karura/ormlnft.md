
# OrmlNFT

---------
## Storage functions

---------
### Classes

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
        'attributes': 'scale_info::337',
        'deposit': 'u128',
        'properties': 'u8',
    },
    'metadata': 'Bytes',
    'owner': 'AccountId',
    'total_issuance': 'u64',
}
```
---------
### NextClassId

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
### Tokens

#### Python
```python
result = substrate.query(
    'OrmlNFT', 'Tokens', ['u32', 'u64']
)
```

#### Return value
```python
{'data': {'attributes': 'scale_info::337', 'deposit': 'u128'}, 'metadata': 'Bytes', 'owner': 'AccountId'}
```
---------
### TokensByOwner

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

---------
### ClassNotFound

---------
### MaxMetadataExceeded

---------
### NoAvailableClassId

---------
### NoAvailableTokenId

---------
### NoPermission

---------
### TokenNotFound

---------