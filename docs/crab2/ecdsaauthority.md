
# EcdsaAuthority

---------
## Calls

---------
### add_authority
Add a authority and trigger `on_authorities_change`.

Not allow to call while authorities is changing.
This will insert new authority into the index 0 of authorities.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EcdsaAuthority', 'add_authority', {'new': '[u8; 20]'}
)
```

---------
### remove_authority
Remove a authority and trigger `on_authorities_change`.

Not allow to call while authorities is changing.
#### Attributes
| Name | Type |
| -------- | -------- | 
| old | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EcdsaAuthority', 'remove_authority', {'old': '[u8; 20]'}
)
```

---------
### submit_authorities_change_signature
Submit the authorities change signature.

Free to submit the first-correct signature.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signature | `Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EcdsaAuthority', 'submit_authorities_change_signature', {'signature': '[u8; 65]'}
)
```

---------
### submit_new_message_root_signature
Submit the new message root signature.

Free to submit the first-correct signature.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signature | `Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EcdsaAuthority', 'submit_new_message_root_signature', {'signature': '[u8; 65]'}
)
```

---------
### swap_authority
Swap the old authority with the new authority and trigger `on_authorities_change`.

Not allow to call while authorities is changing.
#### Attributes
| Name | Type |
| -------- | -------- | 
| old | `T::AccountId` | 
| new | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EcdsaAuthority', 'swap_authority', {'new': '[u8; 20]', 'old': '[u8; 20]'}
)
```

---------
## Events

---------
### CollectedEnoughAuthoritiesChangeSignatures
Collected enough authorities change signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| operation | `Operation<T::AccountId>` | ```{'AddMember': {'new': '[u8; 20]'}, 'RemoveMember': {'pre': '[u8; 20]', 'old': '[u8; 20]'}, 'SwapMembers': {'pre': '[u8; 20]', 'old': '[u8; 20]', 'new': '[u8; 20]'}}```
| threshold | `Option<u32>` | ```(None, 'u32')```
| message | `Hash` | ```[u8; 32]```
| signatures | `Vec<(T::AccountId, Signature)>` | ```[('[u8; 20]', '[u8; 65]')]```

---------
### CollectedEnoughNewMessageRootSignatures
Collected enough new message root signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| commitment | `Commitment` | ```{'block_number': 'u32', 'message_root': '[u8; 32]', 'nonce': 'u32'}```
| message | `Hash` | ```[u8; 32]```
| signatures | `Vec<(T::AccountId, Signature)>` | ```[('[u8; 20]', '[u8; 65]')]```

---------
### CollectingAuthoritiesChangeSignatures
Authorities changed. Collecting authorities change signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message | `Hash` | ```[u8; 32]```

---------
### CollectingNewMessageRootSignatures
New message root found. Collecting new message root signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message | `Hash` | ```[u8; 32]```

---------
## Storage functions

---------
### Authorities
 The current active authorities.

#### Python
```python
result = substrate.query(
    'EcdsaAuthority', 'Authorities', []
)
```

#### Return value
```python
['[u8; 20]']
```
---------
### AuthoritiesChangeToSign
 The authorities change waiting for signing.

#### Python
```python
result = substrate.query(
    'EcdsaAuthority', 'AuthoritiesChangeToSign', []
)
```

#### Return value
```python
{
    'message': '[u8; 32]',
    'operation': {
        'AddMember': {'new': '[u8; 20]'},
        'RemoveMember': {'old': '[u8; 20]', 'pre': '[u8; 20]'},
        'SwapMembers': {
            'new': '[u8; 20]',
            'old': '[u8; 20]',
            'pre': '[u8; 20]',
        },
    },
    'signatures': [('[u8; 20]', '[u8; 65]')],
    'threshold': (None, 'u32'),
}
```
---------
### MessageRootToSign
 The incoming message root waiting for signing.

#### Python
```python
result = substrate.query(
    'EcdsaAuthority', 'MessageRootToSign', []
)
```

#### Return value
```python
{
    'authorized': 'bool',
    'commitment': {
        'block_number': 'u32',
        'message_root': '[u8; 32]',
        'nonce': 'u32',
    },
    'message': '[u8; 32]',
    'signatures': [('[u8; 20]', '[u8; 65]')],
}
```
---------
### NextAuthorities
 The incoming authorities.

#### Python
```python
result = substrate.query(
    'EcdsaAuthority', 'NextAuthorities', []
)
```

#### Return value
```python
['[u8; 20]']
```
---------
### Nonce
 The nonce of the current active authorities. AKA term/session/era.

#### Python
```python
result = substrate.query(
    'EcdsaAuthority', 'Nonce', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### ChainId
 Chain&#x27;s ID, which is using for constructing the message. (follow EIP-712 SPEC)
#### Value
```python
44
```
#### Python
```python
constant = substrate.get_constant('EcdsaAuthority', 'ChainId')
```
---------
### MaxAuthorities
 The maximum number of authorities.
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('EcdsaAuthority', 'MaxAuthorities')
```
---------
### MaxPendingPeriod
 How long should we wait for the message root to be signed.

 If the collecting new message root signatures process takes more than
 `MaxPendingPeriod`, we will drop the root. And update the root with a new one.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('EcdsaAuthority', 'MaxPendingPeriod')
```
---------
### SignThreshold
 The signing threshold.

 Once `signatures_count / authorities_count &gt;= threshold`, we say the message is trusted.
#### Value
```python
600000000
```
#### Python
```python
constant = substrate.get_constant('EcdsaAuthority', 'SignThreshold')
```
---------
### SyncInterval
 The interval of checking the message root.
 This must be shorter than [`Config::MaxPendingPeriod`].
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('EcdsaAuthority', 'SyncInterval')
```
---------
## Errors

---------
### AlreadySubmitted
This authority had already finished his duty.

---------
### AtLeastOneAuthority
Require at least one authority. Not allow to decrease below one.

---------
### AuthorityExisted
The authority is already existed.

---------
### BadSignature
Failed to verify the signature.

---------
### NoAuthoritiesChange
Didn&\#x27;t find any authorities changes to sign.

---------
### NoNewMessageRoot
Didn&\#x27;t find any new message root to sign.

---------
### NotAuthority
This is not an authority.

---------
### OnAuthoritiesChange
Currently, the authorities is changing.

---------
### TooManyAuthorities
Too many authorities.

---------