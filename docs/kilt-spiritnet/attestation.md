
# Attestation

---------
## Calls

---------
### add
See [`Pallet::add`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 
| ctype_hash | `CtypeHashOf<T>` | 
| authorization | `Option<T::AccessControl>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'add', {
    'authorization': (
        None,
        {
            'Delegation': {
                'max_checks': 'u32',
                'subject_node_id': 'scale_info::12',
            },
        },
    ),
    'claim_hash': 'scale_info::12',
    'ctype_hash': 'scale_info::12',
}
)
```

---------
### change_deposit_owner
See [`Pallet::change_deposit_owner`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'change_deposit_owner', {'claim_hash': 'scale_info::12'}
)
```

---------
### reclaim_deposit
See [`Pallet::reclaim_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'reclaim_deposit', {'claim_hash': 'scale_info::12'}
)
```

---------
### remove
See [`Pallet::remove`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 
| authorization | `Option<T::AccessControl>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'remove', {
    'authorization': (
        None,
        {
            'Delegation': {
                'max_checks': 'u32',
                'subject_node_id': 'scale_info::12',
            },
        },
    ),
    'claim_hash': 'scale_info::12',
}
)
```

---------
### revoke
See [`Pallet::revoke`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 
| authorization | `Option<T::AccessControl>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'revoke', {
    'authorization': (
        None,
        {
            'Delegation': {
                'max_checks': 'u32',
                'subject_node_id': 'scale_info::12',
            },
        },
    ),
    'claim_hash': 'scale_info::12',
}
)
```

---------
### update_deposit
See [`Pallet::update_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'update_deposit', {'claim_hash': 'scale_info::12'}
)
```

---------
## Events

---------
### AttestationCreated
A new attestation has been created.
\[attester ID, claim hash, CType hash, (optional) delegation ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AttesterOf<T>` | ```AccountId```
| None | `ClaimHashOf<T>` | ```scale_info::12```
| None | `CtypeHashOf<T>` | ```scale_info::12```
| None | `Option<AuthorizationIdOf<T>>` | ```(None, {'Delegation': 'scale_info::12'})```

---------
### AttestationRemoved
An attestation has been removed.
\[account id, claim hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AttesterOf<T>` | ```AccountId```
| None | `ClaimHashOf<T>` | ```scale_info::12```

---------
### AttestationRevoked
An attestation has been revoked.
\[account id, claim hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AttesterOf<T>` | ```AccountId```
| None | `ClaimHashOf<T>` | ```scale_info::12```

---------
### DepositReclaimed
The deposit owner reclaimed a deposit by removing an attestation.
\[account id, claim hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ClaimHashOf<T>` | ```scale_info::12```

---------
## Storage functions

---------
### Attestations
 Attestations stored on chain.

 It maps from a claim hash to the full attestation.

#### Python
```python
result = substrate.query(
    'Attestation', 'Attestations', ['scale_info::12']
)
```

#### Return value
```python
{
    'attester': 'AccountId',
    'authorization_id': (None, {'Delegation': 'scale_info::12'}),
    'ctype_hash': 'scale_info::12',
    'deposit': {'amount': 'u128', 'owner': 'AccountId'},
    'revoked': 'bool',
}
```
---------
### ExternalAttestations
 Delegated attestations stored on chain.

 It maps from a delegation ID to a vector of claim hashes.

#### Python
```python
result = substrate.query(
    'Attestation', 'ExternalAttestations', [{'Delegation': 'scale_info::12'}, 'scale_info::12']
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### Deposit
 The deposit that is required for storing an attestation.
#### Value
```python
120950000000000
```
#### Python
```python
constant = substrate.get_constant('Attestation', 'Deposit')
```
---------
### MaxDelegatedAttestations
 The maximum number of delegated attestations which can be made by
 the same delegation.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Attestation', 'MaxDelegatedAttestations')
```
---------
## Errors

---------
### AlreadyAttested
There is already an attestation with the same claim hash stored on
chain.

---------
### AlreadyRevoked
The attestation has already been revoked.

---------
### CTypeMismatch
The attestation CType does not match the CType specified in the
delegation hierarchy root.

---------
### MaxDelegatedAttestationsExceeded
The maximum number of delegated attestations has already been
reached for the corresponding delegation id such that another one
cannot be added.

---------
### NotAuthorized
The call origin is not authorized to change the attestation.

---------
### NotFound
No attestation on chain matching the claim hash.

---------