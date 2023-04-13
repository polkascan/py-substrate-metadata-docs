
# Attestation

---------
## Calls

---------
### add
Create a new attestation.

The attester can optionally provide a reference to an existing
delegation that will be saved along with the attestation itself in
the form of an attested delegation.

The referenced CType hash must already be present on chain.

If an optional delegation id is provided, the dispatch origin must
be the owner of the delegation. Otherwise, it could be any
`DelegationEntityId`.

Emits `AttestationCreated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Ctype, Attestations
- Reads if delegation id is provided: Delegations, Roots,
  DelegatedAttestations
- Writes: Attestations, (DelegatedAttestations)
\# &lt;/weight&gt;
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
                'subject_node_id': '[u8; 32]',
            },
        },
    ),
    'claim_hash': '[u8; 32]',
    'ctype_hash': '[u8; 32]',
}
)
```

---------
### change_deposit_owner
Changes the deposit owner.

The balance that is reserved by the current deposit owner will be
freed and balance of the new deposit owner will get reserved.

The subject of the call must be the attester who issues the
attestation. The sender of the call will be the new deposit owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'change_deposit_owner', {'claim_hash': '[u8; 32]'}
)
```

---------
### reclaim_deposit
Reclaim a storage deposit by removing an attestation

Emits `DepositReclaimed`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Attestations, DelegatedAttestations
- Writes: Attestations, DelegatedAttestations
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| claim_hash | `ClaimHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'reclaim_deposit', {'claim_hash': '[u8; 32]'}
)
```

---------
### remove
Remove an attestation.

The origin must be either the creator of the attestation or an
entity which is an ancestor of the attester in the delegation tree,
i.e., it was either the delegator of the attester or an ancestor
thereof.

Emits `AttestationRemoved`.

\# &lt;weight&gt;
Weight: O(P) where P is the number of steps required to verify that
the dispatch Origin controls the delegation entitled to revoke the
attestation. It is bounded by `max_parent_checks`.
- Reads: [Origin Account], Attestations, delegation::Roots
- Reads per delegation step P: delegation::Delegations
- Writes: Attestations, DelegatedAttestations
\# &lt;/weight&gt;
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
                'subject_node_id': '[u8; 32]',
            },
        },
    ),
    'claim_hash': '[u8; 32]',
}
)
```

---------
### revoke
Revoke an existing attestation.

The revoker must be either the creator of the attestation being
revoked or an entity that in the delegation tree is an ancestor of
the attester, i.e., it was either the delegator of the attester or
an ancestor thereof.

Emits `AttestationRevoked`.

\# &lt;weight&gt;
Weight: O(P) where P is the number of steps required to verify that
the dispatch Origin controls the delegation entitled to revoke the
attestation. It is bounded by `max_parent_checks`.
- Reads: [Origin Account], Attestations, delegation::Roots
- Reads per delegation step P: delegation::Delegations
- Writes: Attestations, DelegatedAttestations
\# &lt;/weight&gt;
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
                'subject_node_id': '[u8; 32]',
            },
        },
    ),
    'claim_hash': '[u8; 32]',
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
| claim_hash | `ClaimHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Attestation', 'update_deposit', {'claim_hash': '[u8; 32]'}
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
| None | `ClaimHashOf<T>` | ```[u8; 32]```
| None | `CtypeHashOf<T>` | ```[u8; 32]```
| None | `Option<AuthorizationIdOf<T>>` | ```(None, {'Delegation': '[u8; 32]'})```

---------
### AttestationRemoved
An attestation has been removed.
\[account id, claim hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AttesterOf<T>` | ```AccountId```
| None | `ClaimHashOf<T>` | ```[u8; 32]```

---------
### AttestationRevoked
An attestation has been revoked.
\[account id, claim hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AttesterOf<T>` | ```AccountId```
| None | `ClaimHashOf<T>` | ```[u8; 32]```

---------
### DepositReclaimed
The deposit owner reclaimed a deposit by removing an attestation.
\[account id, claim hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ClaimHashOf<T>` | ```[u8; 32]```

---------
## Storage functions

---------
### Attestations
 Attestations stored on chain.

 It maps from a claim hash to the full attestation.

#### Python
```python
result = substrate.query(
    'Attestation', 'Attestations', ['[u8; 32]']
)
```

#### Return value
```python
{
    'attester': 'AccountId',
    'authorization_id': (None, {'Delegation': '[u8; 32]'}),
    'ctype_hash': '[u8; 32]',
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
    'Attestation', 'ExternalAttestations', [{'Delegation': '[u8; 32]'}, '[u8; 32]']
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