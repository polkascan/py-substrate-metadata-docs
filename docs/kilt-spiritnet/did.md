
# Did

---------
## Calls

---------
### add_key_agreement_key
Add a single new key agreement key to the DID.

The new key is added to the set of public keys.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidEncryptionKey` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'add_key_agreement_key', {'new_key': {'X25519': '[u8; 32]'}}
)
```

---------
### add_service_endpoint
Add a new service endpoint under the given DID.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did, ServiceEndpoints, DidEndpointsCount
- Writes: Did, ServiceEndpoints, DidEndpointsCount
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| service_endpoint | `DidEndpoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'add_service_endpoint', {
    'service_endpoint': {
        'id': 'Bytes',
        'service_types': ['Bytes'],
        'urls': ['Bytes'],
    },
}
)
```

---------
### change_deposit_owner
Changes the deposit owner.

The balance that is reserved by the current deposit owner will be
freed and balance of the new deposit owner will get reserved.

The subject of the call must be the did owner.
The sender of the call will be the new deposit owner.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Did', 'change_deposit_owner', {}
)
```

---------
### create
Store a new DID on chain, after verifying that the creation
operation has been signed by the KILT account associated with the
identifier of the DID being created and that a DID with the same
identifier has not previously existed on (and then deleted from) the
chain.

There must be no DID information stored on chain under the same DID
identifier.

The new keys added with this operation are stored under the DID
identifier along with the block number in which the operation was
executed.

The dispatch origin can be any KILT account with enough funds to
execute the extrinsic and it does not have to be tied in any way to
the KILT account identifying the DID subject.

Emits `DidCreated`.

\# &lt;weight&gt;
- The transaction&\#x27;s complexity is mainly dependent on the number of
  new key agreement keys and the number of new service endpoints
  included in the operation.
---------
Weight: O(K) + O(N) where K is the number of new key agreement
keys bounded by `MaxNewKeyAgreementKeys`, while N is the number of
new service endpoints bounded by `MaxNumberOfServicesPerDid`.
- Reads: [Origin Account], Did, DidBlacklist
- Writes: Did (with K new key agreement keys), ServiceEndpoints
  (with N new service endpoints), DidEndpointsCount
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| details | `Box<DidCreationDetails<T>>` | 
| signature | `DidSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'create', {
    'details': {
        'did': 'AccountId',
        'new_attestation_key': (
            None,
            {
                'Ecdsa': '[u8; 33]',
                'Ed25519': '[u8; 32]',
                'Sr25519': '[u8; 32]',
            },
        ),
        'new_delegation_key': (
            None,
            {
                'Ecdsa': '[u8; 33]',
                'Ed25519': '[u8; 32]',
                'Sr25519': '[u8; 32]',
            },
        ),
        'new_key_agreement_keys': 'scale_info::273',
        'new_service_details': [
            {
                'id': 'Bytes',
                'service_types': [
                    'Bytes',
                ],
                'urls': ['Bytes'],
            },
        ],
        'submitter': 'AccountId',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### delete
Delete a DID from the chain and all information associated with it,
after verifying that the delete operation has been signed by the DID
subject using the authentication key currently stored on chain.

The referenced DID identifier must be present on chain before the
delete operation is evaluated.

After it is deleted, a DID with the same identifier cannot be
re-created ever again.

As the result of the deletion, all traces of the DID are removed
from the storage, which results in the invalidation of all
attestations issued by the DID subject.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidDeleted`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Kills: Did entry associated to the DID identifier
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| endpoints_to_remove | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'delete', {'endpoints_to_remove': 'u32'}
)
```

---------
### reclaim_deposit
Reclaim a deposit for a DID. This will delete the DID and all
information associated with it, after verifying that the caller is
the owner of the deposit.

The referenced DID identifier must be present on chain before the
delete operation is evaluated.

After it is deleted, a DID with the same identifier cannot be
re-created ever again.

As the result of the deletion, all traces of the DID are removed
from the storage, which results in the invalidation of all
attestations issued by the DID subject.

Emits `DidDeleted`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Kills: Did entry associated to the DID identifier
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| did_subject | `DidIdentifierOf<T>` | 
| endpoints_to_remove | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'reclaim_deposit', {
    'did_subject': 'AccountId',
    'endpoints_to_remove': 'u32',
}
)
```

---------
### remove_attestation_key
Remove the DID attestation key.

The old key is deleted from the set of public keys if
it is not used in any other part of the DID.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_attestation_key', {}
)
```

---------
### remove_delegation_key
Remove the DID delegation key.

The old key is deleted from the set of public keys if
it is not used in any other part of the DID.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_delegation_key', {}
)
```

---------
### remove_key_agreement_key
Remove a DID key agreement key from both its set of key agreement
keys and as well as its public keys.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| key_id | `KeyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_key_agreement_key', {'key_id': '[u8; 32]'}
)
```

---------
### remove_service_endpoint
Remove the service with the provided ID from the DID.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], ServiceEndpoints, DidEndpointsCount
- Writes: Did, ServiceEndpoints, DidEndpointsCount
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| service_id | `ServiceEndpointId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_service_endpoint', {'service_id': 'Bytes'}
)
```

---------
### set_attestation_key
Set or update the DID attestation key.

If an old key existed, it is deleted from the set of public keys if
it is not used in any other part of the DID. The new key is added to
the set of public keys.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidVerificationKey` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'set_attestation_key', {
    'new_key': {
        'Ecdsa': '[u8; 33]',
        'Ed25519': '[u8; 32]',
        'Sr25519': '[u8; 32]',
    },
}
)
```

---------
### set_authentication_key
Update the DID authentication key.

The old key is deleted from the set of public keys if it is
not used in any other part of the DID. The new key is added to the
set of public keys.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidVerificationKey` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'set_authentication_key', {
    'new_key': {
        'Ecdsa': '[u8; 33]',
        'Ed25519': '[u8; 32]',
        'Sr25519': '[u8; 32]',
    },
}
)
```

---------
### set_delegation_key
Set or update the DID delegation key.

If an old key existed, it is deleted from the set of public keys if
it is not used in any other part of the DID. The new key is added to
the set of public keys.

The dispatch origin must be a DID origin proxied via the
`submit_did_call` extrinsic.

Emits `DidUpdated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidVerificationKey` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'set_delegation_key', {
    'new_key': {
        'Ecdsa': '[u8; 33]',
        'Ed25519': '[u8; 32]',
        'Sr25519': '[u8; 32]',
    },
}
)
```

---------
### submit_did_call
Proxy a dispatchable call of another runtime extrinsic that
supports a DID origin.

The referenced DID identifier must be present on chain before the
operation is dispatched.

A call submitted through this extrinsic must be signed with the
right DID key, depending on the call. This information is provided
by the `DidAuthorizedCallOperation` parameter, which specifies the
DID subject acting as the origin of the call, the DID&\#x27;s tx counter
(nonce), the dispatchable to call in case signature verification
succeeds, the type of DID key to use to verify the operation
signature, and the block number the operation was targeting for
inclusion, when it was created and signed.

In case the signature is incorrect, the nonce is not valid, the
required key is not present for the specified DID, or the block
specified is too old the verification fails and the call is not
dispatched. Otherwise, the call is properly dispatched with a
`DidOrigin` origin indicating the DID subject.

A successful dispatch operation results in the tx counter associated
with the given DID to be incremented, to mitigate replay attacks.

The dispatch origin can be any KILT account with enough funds to
execute the extrinsic and it does not have to be tied in any way to
the KILT account identifying the DID subject.

Emits `DidCallDispatched`.

\# &lt;weight&gt;
Weight: O(1) + weight of the dispatched call
- Reads: [Origin Account], Did
- Writes: Did
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| did_call | `Box<DidAuthorizedCallOperation<T>>` | 
| signature | `DidSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'submit_did_call', {
    'did_call': {
        'block_number': 'u64',
        'call': 'Call',
        'did': 'AccountId',
        'submitter': 'AccountId',
        'tx_counter': 'u64',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
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
| did | `DidIdentifierOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'update_deposit', {'did': 'AccountId'}
)
```

---------
## Events

---------
### DidCallDispatched
A DID-authorised call has been executed.
\[DID caller, dispatch result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DidIdentifierOf<T>` | ```AccountId```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### DidCreated
A new DID has been created.
\[transaction signer, DID identifier\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
### DidDeleted
A DID has been deleted.
\[DID identifier\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
### DidUpdated
A DID has been updated.
\[DID identifier\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
## Storage functions

---------
### Did
 DIDs stored on chain.

 It maps from a DID identifier to the DID details.

#### Python
```python
result = substrate.query(
    'Did', 'Did', ['AccountId']
)
```

#### Return value
```python
{
    'attestation_key': (None, '[u8; 32]'),
    'authentication_key': '[u8; 32]',
    'delegation_key': (None, '[u8; 32]'),
    'deposit': {'amount': 'u128', 'owner': 'AccountId'},
    'key_agreement_keys': 'scale_info::405',
    'last_tx_counter': 'u64',
    'public_keys': 'scale_info::414',
}
```
---------
### DidBlacklist
 The set of DIDs that have been deleted and cannot therefore be created
 again for security reasons.

 It maps from a DID identifier to a unit tuple, for the sake of tracking
 DID identifiers.

#### Python
```python
result = substrate.query(
    'Did', 'DidBlacklist', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### DidEndpointsCount
 Counter of service endpoints for each DID.

 It maps from (DID identifier) to a 32-bit counter.

#### Python
```python
result = substrate.query(
    'Did', 'DidEndpointsCount', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### ServiceEndpoints
 Service endpoints associated with DIDs.

 It maps from (DID identifier, service ID) to the service details.

#### Python
```python
result = substrate.query(
    'Did', 'ServiceEndpoints', ['AccountId', 'Bytes']
)
```

#### Return value
```python
{'id': 'Bytes', 'service_types': ['Bytes'], 'urls': ['Bytes']}
```
---------
## Constants

---------
### Deposit
 The amount of balance that will be taken for each DID as a deposit
 to incentivise fair use of the on chain storage. The deposit can be
 reclaimed when the DID is deleted.
#### Value
```python
2007900000000000
```
#### Python
```python
constant = substrate.get_constant('Did', 'Deposit')
```
---------
### Fee
 The amount of balance that will be taken for each DID as a fee to
 incentivise fair use of the on chain storage. The fee will not get
 refunded when the DID is deleted.
#### Value
```python
50000000000000
```
#### Python
```python
constant = substrate.get_constant('Did', 'Fee')
```
---------
### MaxBlocksTxValidity
 The maximum number of blocks a DID-authorized operation is
 considered valid after its creation.
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxBlocksTxValidity')
```
---------
### MaxNewKeyAgreementKeys
 Maximum number of key agreement keys that can be added in a creation
 operation.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNewKeyAgreementKeys')
```
---------
### MaxNumberOfServicesPerDid
 The maximum number of services that can be stored under a DID.
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNumberOfServicesPerDid')
```
---------
### MaxNumberOfTypesPerService
 The maximum number of a types description for a service endpoint.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNumberOfTypesPerService')
```
---------
### MaxNumberOfUrlsPerService
 The maximum number of a URLs for a service endpoint.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNumberOfUrlsPerService')
```
---------
### MaxPublicKeysPerDid
 Maximum number of total public keys which can be stored per DID key
 identifier. This includes the ones currently used for
 authentication, key agreement, attestation, and delegation.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxPublicKeysPerDid')
```
---------
### MaxServiceIdLength
 The maximum length of a service ID.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxServiceIdLength')
```
---------
### MaxServiceTypeLength
 The maximum length of a service type description.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxServiceTypeLength')
```
---------
### MaxServiceUrlLength
 The maximum length of a service URL.
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxServiceUrlLength')
```
---------
### MaxTotalKeyAgreementKeys
 Maximum number of total key agreement keys that can be stored for a
 DID subject.

 Should be greater than `MaxNewKeyAgreementKeys`.
#### Value
```python
19
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxTotalKeyAgreementKeys')
```
---------
## Errors

---------
### BadDidOrigin
The DID call was submitted by the wrong account

---------
### DidAlreadyDeleted
The DID has already been previously deleted.

---------
### DidAlreadyPresent
The DID with the given identifier is already present on chain.

---------
### DidNotPresent
No DID with the given identifier is present on chain.

---------
### InternalError
An error that is not supposed to take place, yet it happened.

---------
### InvalidDidAuthorizationCall
The call had parameters that conflicted with each other
or were invalid.

---------
### InvalidNonce
The DID operation nonce is not equal to the current DID nonce + 1.

---------
### InvalidServiceEncoding
One of the service endpoint details contains non-ASCII characters.

---------
### InvalidSignature
The DID operation signature is invalid for the payload and the
verification key provided.

---------
### InvalidSignatureFormat
The DID operation signature is not in the format the verification
key expects.

---------
### MaxKeyAgreementKeysLimitExceeded
A number of new key agreement keys greater than the maximum allowed
has been provided.

---------
### MaxNumberOfServicesPerDidExceeded
The maximum number of service endpoints for a DID has been exceeded.

---------
### MaxNumberOfTypesPerServiceExceeded
The maximum number of types for a service endpoint has been
exceeded.

---------
### MaxNumberOfUrlsPerServiceExceeded
The maximum number of URLs for a service endpoint has been exceeded.

---------
### MaxPublicKeysPerDidExceeded
The maximum number of public keys for this DID key identifier has
been reached.

---------
### MaxServiceIdLengthExceeded
The service endpoint ID exceeded the maximum allowed length.

---------
### MaxServiceTypeLengthExceeded
One of the service endpoint types exceeded the maximum allowed
length.

---------
### MaxServiceUrlLengthExceeded
One of the service endpoint URLs exceeded the maximum allowed
length.

---------
### MaxTotalKeyAgreementKeysExceeded
The maximum number of key agreements has been reached for the DID
subject.

---------
### NotOwnerOfDeposit
Only the owner of the deposit can reclaim its reserved balance.

---------
### ServiceAlreadyPresent
A service with the provided ID is already present for the given DID.

---------
### ServiceNotPresent
A service with the provided ID is not present under the given DID.

---------
### StoredEndpointsCountTooLarge
The number of service endpoints stored under the DID is larger than
the number of endpoints to delete.

---------
### TransactionExpired
The block number provided in a DID-authorized operation is invalid.

---------
### UnableToPayFees
The origin is unable to reserve the deposit and pay the fee.

---------
### UnsupportedDidAuthorizationCall
The called extrinsic does not support DID authorisation.

---------
### VerificationKeyNotPresent
One or more verification keys referenced are not stored in the set
of verification keys.

---------