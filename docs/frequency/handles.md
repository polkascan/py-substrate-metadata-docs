
# Handles

---------
## Calls

---------
### change_handle
#### Attributes
| Name | Type |
| -------- | -------- | 
| msa_owner_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `ClaimHandlePayload<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Handles', 'change_handle', {
    'msa_owner_key': 'AccountId',
    'payload': {
        'base_handle': 'Bytes',
        'expiration': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### claim_handle
#### Attributes
| Name | Type |
| -------- | -------- | 
| msa_owner_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `ClaimHandlePayload<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Handles', 'claim_handle', {
    'msa_owner_key': 'AccountId',
    'payload': {
        'base_handle': 'Bytes',
        'expiration': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### retire_handle
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Handles', 'retire_handle', {}
)
```

---------
## Events

---------
### HandleClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| handle | `Vec<u8>` | ```Bytes```

---------
### HandleRetired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| handle | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### CanonicalBaseHandleAndSuffixToMSAId

#### Python
```python
result = substrate.query(
    'Handles', 'CanonicalBaseHandleAndSuffixToMSAId', ['Bytes', 'u16']
)
```

#### Return value
```python
'u64'
```
---------
### CanonicalBaseHandleToSuffixIndex

#### Python
```python
result = substrate.query(
    'Handles', 'CanonicalBaseHandleToSuffixIndex', ['Bytes']
)
```

#### Return value
```python
('u16', 'u16')
```
---------
### MSAIdToDisplayName

#### Python
```python
result = substrate.query(
    'Handles', 'MSAIdToDisplayName', ['u64']
)
```

#### Return value
```python
('Bytes', 'u32')
```
---------
## Constants

---------
### HandleSuffixMax
#### Value
```python
99
```
#### Python
```python
constant = substrate.get_constant('Handles', 'HandleSuffixMax')
```
---------
### HandleSuffixMin
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Handles', 'HandleSuffixMin')
```
---------
### MortalityWindowSize
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Handles', 'MortalityWindowSize')
```
---------
## Errors

---------
### HandleContainsBlockedCharacters

---------
### HandleDoesNotConsistOfSupportedCharacterSets

---------
### HandleIsNotAllowed

---------
### HandleWithinMortalityPeriod

---------
### InvalidHandle

---------
### InvalidHandleByteLength

---------
### InvalidHandleCharacterLength

---------
### InvalidHandleEncoding

---------
### InvalidMessageSourceAccount

---------
### InvalidSignature

---------
### MSAHandleAlreadyExists

---------
### MSAHandleDoesNotExist

---------
### ProofHasExpired

---------
### ProofNotYetValid

---------
### SuffixesExhausted

---------