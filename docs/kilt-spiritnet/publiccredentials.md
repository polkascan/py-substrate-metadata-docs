
# PublicCredentials

---------
## Calls

---------
### add
See [`Pallet::add`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential | `Box<InputCredentialOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'add', {
    'credential': {
        'authorization': (
            None,
            {
                'Delegation': {
                    'max_checks': 'u32',
                    'subject_node_id': 'scale_info::12',
                },
            },
        ),
        'claims': 'Bytes',
        'ctype_hash': 'scale_info::12',
        'subject': 'Bytes',
    },
}
)
```

---------
### change_deposit_owner
See [`Pallet::change_deposit_owner`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'change_deposit_owner', {'credential_id': 'scale_info::12'}
)
```

---------
### reclaim_deposit
See [`Pallet::reclaim_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'reclaim_deposit', {'credential_id': 'scale_info::12'}
)
```

---------
### remove
See [`Pallet::remove`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 
| authorization | `Option<T::AccessControl>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'remove', {
    'authorization': (
        None,
        {
            'Delegation': {
                'max_checks': 'u32',
                'subject_node_id': 'scale_info::12',
            },
        },
    ),
    'credential_id': 'scale_info::12',
}
)
```

---------
### revoke
See [`Pallet::revoke`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 
| authorization | `Option<T::AccessControl>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'revoke', {
    'authorization': (
        None,
        {
            'Delegation': {
                'max_checks': 'u32',
                'subject_node_id': 'scale_info::12',
            },
        },
    ),
    'credential_id': 'scale_info::12',
}
)
```

---------
### unrevoke
See [`Pallet::unrevoke`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 
| authorization | `Option<T::AccessControl>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'unrevoke', {
    'authorization': (
        None,
        {
            'Delegation': {
                'max_checks': 'u32',
                'subject_node_id': 'scale_info::12',
            },
        },
    ),
    'credential_id': 'scale_info::12',
}
)
```

---------
### update_deposit
See [`Pallet::update_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'update_deposit', {'credential_id': 'scale_info::12'}
)
```

---------
## Events

---------
### CredentialRemoved
A public credentials has been removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| subject_id | `T::SubjectId` | ```{'chain_id': {'Eip155': 'u128', 'Bip122': '[u8; 16]', 'Dotsama': '[u8; 16]', 'Solana': 'Bytes', 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes'}}, 'asset_id': {'Slip44': 'scale_info::91', 'Erc20': '[u8; 20]', 'Erc721': ('[u8; 20]', (None, 'Bytes')), 'Erc1155': ('[u8; 20]', (None, 'Bytes')), 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes', 'id': (None, 'Bytes')}}}```
| credential_id | `CredentialIdOf<T>` | ```scale_info::12```

---------
### CredentialRevoked
A public credential has been revoked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| credential_id | `CredentialIdOf<T>` | ```scale_info::12```

---------
### CredentialStored
A new public credential has been issued.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| subject_id | `T::SubjectId` | ```{'chain_id': {'Eip155': 'u128', 'Bip122': '[u8; 16]', 'Dotsama': '[u8; 16]', 'Solana': 'Bytes', 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes'}}, 'asset_id': {'Slip44': 'scale_info::91', 'Erc20': '[u8; 20]', 'Erc721': ('[u8; 20]', (None, 'Bytes')), 'Erc1155': ('[u8; 20]', (None, 'Bytes')), 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes', 'id': (None, 'Bytes')}}}```
| credential_id | `CredentialIdOf<T>` | ```scale_info::12```

---------
### CredentialUnrevoked
A public credential has been unrevoked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| credential_id | `CredentialIdOf<T>` | ```scale_info::12```

---------
## Storage functions

---------
### CredentialSubjects
 A reverse index mapping from credential ID to the subject the credential
 was issued to.

 It it used to perform efficient lookup of credentials given their ID.

#### Python
```python
result = substrate.query(
    'PublicCredentials', 'CredentialSubjects', ['scale_info::12']
)
```

#### Return value
```python
{
    'asset_id': {
        'Erc1155': ('[u8; 20]', (None, 'Bytes')),
        'Erc20': '[u8; 20]',
        'Erc721': ('[u8; 20]', (None, 'Bytes')),
        'Generic': {'id': (None, 'Bytes'), 'namespace': 'Bytes', 'reference': 'Bytes'},
        'Slip44': 'scale_info::91',
    },
    'chain_id': {
        'Bip122': '[u8; 16]',
        'Dotsama': '[u8; 16]',
        'Eip155': 'u128',
        'Generic': {'namespace': 'Bytes', 'reference': 'Bytes'},
        'Solana': 'Bytes',
    },
}
```
---------
### Credentials
 The map of public credentials already attested.
 It maps from a (subject id + credential id) -&gt; the creation
 details of the credential.

#### Python
```python
result = substrate.query(
    'PublicCredentials', 'Credentials', [
    {
        'asset_id': {
            'Erc1155': (
                '[u8; 20]',
                (None, 'Bytes'),
            ),
            'Erc20': '[u8; 20]',
            'Erc721': (
                '[u8; 20]',
                (None, 'Bytes'),
            ),
            'Generic': {
                'id': (None, 'Bytes'),
                'namespace': 'Bytes',
                'reference': 'Bytes',
            },
            'Slip44': 'scale_info::91',
        },
        'chain_id': {
            'Bip122': '[u8; 16]',
            'Dotsama': '[u8; 16]',
            'Eip155': 'u128',
            'Generic': {
                'namespace': 'Bytes',
                'reference': 'Bytes',
            },
            'Solana': 'Bytes',
        },
    },
    'scale_info::12',
]
)
```

#### Return value
```python
{
    'attester': 'AccountId',
    'authorization_id': (None, {'Delegation': 'scale_info::12'}),
    'block_number': 'u64',
    'ctype_hash': 'scale_info::12',
    'deposit': {'amount': 'u128', 'owner': 'AccountId'},
    'revoked': 'bool',
}
```
---------
## Constants

---------
### Deposit
 The amount of tokens to reserve when attesting a public credential.
#### Value
```python
76950000000000
```
#### Python
```python
constant = substrate.get_constant('PublicCredentials', 'Deposit')
```
---------
### MaxEncodedClaimsLength
 The maximum length in bytes of the encoded claims of a credential.
#### Value
```python
100000
```
#### Python
```python
constant = substrate.get_constant('PublicCredentials', 'MaxEncodedClaimsLength')
```
---------
### MaxSubjectIdLength
 The maximum length in bytes of the raw credential subject
 identifier.
#### Value
```python
268
```
#### Python
```python
constant = substrate.get_constant('PublicCredentials', 'MaxSubjectIdLength')
```
---------
## Errors

---------
### AlreadyAttested
A credential with the same root hash has already issued to the
specified subject.

---------
### Internal
Catch-all for any other errors that should not happen, yet it
happened.

---------
### InvalidInput
The credential input is invalid.

---------
### NotAuthorized
The caller is not authorized to performed the operation.

---------
### NotFound
No credential with the specified root hash has been issued to the
specified subject.

---------
### UnableToPayFees
Not enough tokens to pay for the fees or the deposit.

---------