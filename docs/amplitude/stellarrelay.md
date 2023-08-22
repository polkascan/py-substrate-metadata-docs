
# StellarRelay

---------
## Calls

---------
### update_tier_1_validator_set
This extrinsic is used to update the current sets of validators and
organizations. The current values of validators and organizations are moved to the
OldValidators and OldOrganizations respectively, and the function arguments are stored
as new/current values. The `enactment_block_height` parameter is used by the
`validate_stellar_transaction` function to determine if it should use the &\#x27;old&\#x27; or
updated sets for validation. This makes a seamless transition between old and new
validators possible.

It can only be called by the root origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| validators | `Vec<ValidatorOf<T>>` | 
| organizations | `Vec<OrganizationOf<T>>` | 
| enactment_block_height | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'StellarRelay', 'update_tier_1_validator_set', {
    'enactment_block_height': 'u32',
    'organizations': [
        {
            'id': 'u128',
            'name': 'Bytes',
        },
    ],
    'validators': [
        {
            'name': 'Bytes',
            'organization_id': 'u128',
            'public_key': 'Bytes',
        },
    ],
}
)
```

---------
## Events

---------
### UpdateTier1ValidatorSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_validators_enactment_block_height | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### NewValidatorsEnactmentBlockHeight

#### Python
```python
result = substrate.query(
    'StellarRelay', 'NewValidatorsEnactmentBlockHeight', []
)
```

#### Return value
```python
'u32'
```
---------
### OldOrganizations

#### Python
```python
result = substrate.query(
    'StellarRelay', 'OldOrganizations', []
)
```

#### Return value
```python
[{'id': 'u128', 'name': 'Bytes'}]
```
---------
### OldValidators

#### Python
```python
result = substrate.query(
    'StellarRelay', 'OldValidators', []
)
```

#### Return value
```python
[{'name': 'Bytes', 'organization_id': 'u128', 'public_key': 'Bytes'}]
```
---------
### Organizations

#### Python
```python
result = substrate.query(
    'StellarRelay', 'Organizations', []
)
```

#### Return value
```python
[{'id': 'u128', 'name': 'Bytes'}]
```
---------
### Validators

#### Python
```python
result = substrate.query(
    'StellarRelay', 'Validators', []
)
```

#### Return value
```python
[{'name': 'Bytes', 'organization_id': 'u128', 'public_key': 'Bytes'}]
```
---------
## Constants

---------
### IsPublicNetwork
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('StellarRelay', 'IsPublicNetwork')
```
---------
### OrganizationLimit
#### Value
```python
255
```
#### Python
```python
constant = substrate.get_constant('StellarRelay', 'OrganizationLimit')
```
---------
### ValidatorLimit
#### Value
```python
255
```
#### Python
```python
constant = substrate.get_constant('StellarRelay', 'ValidatorLimit')
```
---------
## Errors

---------
### Base64DecodeError

---------
### BoundedVecCreationFailed

---------
### DuplicateOrganizationId

---------
### DuplicateValidatorPublicKey

---------
### EmptyEnvelopeSet

---------
### EnvelopeSignedByUnknownValidator

---------
### EnvelopeSlotIndexMismatch

---------
### ExternalizedNHMismatch

---------
### ExternalizedValueMismatch

---------
### ExternalizedValueNotFound

---------
### FailedToComputeNonGenericTxSetContentHash

---------
### InvalidEnvelopeSignature

---------
### InvalidQuorumSetNotEnoughOrganizations

---------
### InvalidQuorumSetNotEnoughValidators

---------
### InvalidScpPledge

---------
### InvalidTransactionSet

---------
### InvalidTransactionXDR

---------
### InvalidXDR

---------
### MissingExternalizedMessage

---------
### NoOrganizationsRegistered

---------
### NoOrganizationsRegisteredForNetwork

---------
### NoValidatorsRegistered

---------
### NoValidatorsRegisteredForNetwork

---------
### OrganizationLimitExceeded

---------
### SlotIndexIsNone

---------
### TransactionMemoDoesNotMatch

---------
### TransactionNotInTransactionSet

---------
### TransactionSetHashCreationFailed

---------
### TransactionSetHashMismatch

---------
### ValidatorLimitExceeded

---------