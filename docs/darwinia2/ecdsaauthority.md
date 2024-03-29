
# EcdsaAuthority

---------
## Calls

---------
### add_authority
See [`Pallet::add_authority`].
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
See [`Pallet::remove_authority`].
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
See [`Pallet::submit_authorities_change_signature`].
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
See [`Pallet::submit_new_message_root_signature`].
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
See [`Pallet::swap_authority`].
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
| message | `Hash` | ```scale_info::12```
| signatures | `Vec<(T::AccountId, Signature)>` | ```[('[u8; 20]', '[u8; 65]')]```

---------
### CollectedEnoughNewMessageRootSignatures
Collected enough new message root signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| commitment | `Commitment<BlockNumberFor<T>>` | ```{'block_number': 'u32', 'message_root': 'scale_info::12', 'nonce': 'u32'}```
| message | `Hash` | ```scale_info::12```
| signatures | `Vec<(T::AccountId, Signature)>` | ```[('[u8; 20]', '[u8; 65]')]```

---------
### CollectingAuthoritiesChangeSignatures
Authorities changed. Collecting authorities change signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message | `Hash` | ```scale_info::12```

---------
### CollectingNewMessageRootSignatures
New message root found. Collecting new message root signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message | `Hash` | ```scale_info::12```

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
    'message': 'scale_info::12',
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
        'message_root': 'scale_info::12',
        'nonce': 'u32',
    },
    'message': 'scale_info::12',
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
46
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
7
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