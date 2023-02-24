
# PublicCredentials

---------
## Calls

---------
### add
Register a new public credential on chain.

This function fails if a credential with the same identifier already
exists for the specified subject.

Emits `CredentialStored`.
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
                    'subject_node_id': '[u8; 32]',
                },
            },
        ),
        'claims': 'Bytes',
        'ctype_hash': '[u8; 32]',
        'subject': 'Bytes',
    },
}
)
```

---------
### change_deposit_owner
Changes the deposit owner.

The balance that is reserved by the current deposit owner will be
freed and balance of the new deposit owner will get reserved.

The subject of the call must be the owner of the credential.
The sender of the call will be the new deposit owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'change_deposit_owner', {'credential_id': '[u8; 32]'}
)
```

---------
### reclaim_deposit
Removes the information pertaining a public credential from the
chain and returns the deposit to its payer.

The removal of the credential does not delete it entirely from the
blockchain history, but only its link *from* the blockchain state
*to* the blockchain history is removed.

Clients parsing public credentials should interpret
the lack of such a link as the fact that the credential has been
removed by its attester some time in the past.

This function fails if a credential already exists for the specified
subject.

The dispatch origin must be the owner of the deposit, hence not the
credential&\#x27;s attester.

Emits `CredentialRemoved`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'reclaim_deposit', {'credential_id': '[u8; 32]'}
)
```

---------
### remove
Removes the information pertaining a public credential from the
chain.

The removal of the credential does not delete it entirely from the
blockchain history, but only its link *from* the blockchain state
*to* the blockchain history is removed.

Clients parsing public credentials should interpret
the lack of such a link as the fact that the credential has been
removed by its attester some time in the past.

This function fails if a credential already exists for the specified
subject.

The dispatch origin must be authorized to remove the credential.

Emits `CredentialRemoved`.
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
                'subject_node_id': '[u8; 32]',
            },
        },
    ),
    'credential_id': '[u8; 32]',
}
)
```

---------
### revoke
Revokes a public credential.

If a credential was already revoked, this function does not fail but
simply results in a noop.

The dispatch origin must be authorized to revoke the credential.

Emits `CredentialRevoked`.
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
                'subject_node_id': '[u8; 32]',
            },
        },
    ),
    'credential_id': '[u8; 32]',
}
)
```

---------
### unrevoke
Unrevokes a public credential.

If a credential was not revoked, this function does not fail but
simply results in a noop.

The dispatch origin must be authorized to unrevoke the
credential.

Emits `CredentialUnrevoked`.
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
                'subject_node_id': '[u8; 32]',
            },
        },
    ),
    'credential_id': '[u8; 32]',
}
)
```

---------
### update_deposit
Updates the deposit amount to the current deposit rate.

The sender must be the deposit owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| credential_id | `CredentialIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PublicCredentials', 'update_deposit', {'credential_id': '[u8; 32]'}
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
| subject_id | `T::SubjectId` | ```{'chain_id': {'Eip155': 'u128', 'Bip122': '[u8; 16]', 'Dotsama': '[u8; 16]', 'Solana': 'Bytes', 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes'}}, 'asset_id': {'Slip44': '[u64; 4]', 'Erc20': '[u8; 20]', 'Erc721': ('[u8; 20]', (None, 'Bytes')), 'Erc1155': ('[u8; 20]', (None, 'Bytes')), 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes', 'id': (None, 'Bytes')}}}```
| credential_id | `CredentialIdOf<T>` | ```[u8; 32]```

---------
### CredentialRevoked
A public credential has been revoked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| credential_id | `CredentialIdOf<T>` | ```[u8; 32]```

---------
### CredentialStored
A new public credential has been issued.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| subject_id | `T::SubjectId` | ```{'chain_id': {'Eip155': 'u128', 'Bip122': '[u8; 16]', 'Dotsama': '[u8; 16]', 'Solana': 'Bytes', 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes'}}, 'asset_id': {'Slip44': '[u64; 4]', 'Erc20': '[u8; 20]', 'Erc721': ('[u8; 20]', (None, 'Bytes')), 'Erc1155': ('[u8; 20]', (None, 'Bytes')), 'Generic': {'namespace': 'Bytes', 'reference': 'Bytes', 'id': (None, 'Bytes')}}}```
| credential_id | `CredentialIdOf<T>` | ```[u8; 32]```

---------
### CredentialUnrevoked
A public credential has been unrevoked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| credential_id | `CredentialIdOf<T>` | ```[u8; 32]```

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
    'PublicCredentials', 'CredentialSubjects', ['[u8; 32]']
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
        'Slip44': '[u64; 4]',
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
            'Slip44': '[u64; 4]',
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
    '[u8; 32]',
]
)
```

#### Return value
```python
{
    'attester': 'AccountId',
    'authorization_id': (None, {'Delegation': '[u8; 32]'}),
    'block_number': 'u64',
    'ctype_hash': '[u8; 32]',
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
73750000000000
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
204
```
#### Python
```python
constant = substrate.get_constant('PublicCredentials', 'MaxSubjectIdLength')
```
---------
## Errors

---------
### CredentialAlreadyIssued
A credential with the same root hash has already issued to the
specified subject.

---------
### CredentialNotFound
No credential with the specified root hash has been issued to the
specified subject.

---------
### InternalError
Catch-all for any other errors that should not happen, yet it
happened.

---------
### InvalidInput
The credential input is invalid.

---------
### UnableToPayFees
Not enough tokens to pay for the fees or the deposit.

---------
### Unauthorized
The caller is not authorized to performed the operation.

---------