
# ProtocolFee

---------
## Calls

---------
### change_base_fee
Changes the a base fee for the root origin.

\# Errors
* `BadOrigin` - Only root allowed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| op | `ProtocolOp` | 
| base_fee | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'ProtocolFee', 'change_base_fee', {
    'base_fee': 'u128',
    'op': (
        'AssetRegisterTicker',
        'AssetIssue',
        'AssetAddDocuments',
        'AssetCreateAsset',
        'CheckpointCreateSchedule',
        'ComplianceManagerAddComplianceRequirement',
        'IdentityCddRegisterDid',
        'IdentityAddClaim',
        'IdentityAddSecondaryKeysWithAuthorization',
        'PipsPropose',
        'ContractsPutCode',
        'CorporateBallotAttachBallot',
        'CapitalDistributionDistribute',
        'NFTCreateCollection',
        'NFTMint',
        'IdentityCreateChildIdentity',
    ),
}
)
```

---------
### change_coefficient
Changes the fee coefficient for the root origin.

\# Errors
* `BadOrigin` - Only root allowed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| coefficient | `PosRatio` | 

#### Python
```python
call = substrate.compose_call(
    'ProtocolFee', 'change_coefficient', {'coefficient': ('u32', 'u32')}
)
```

---------
## Events

---------
### CoefficientSet
The fee coefficient.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PosRatio` | ```('u32', 'u32')```

---------
### FeeCharged
Fee charged.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### FeeSet
The protocol fee of an operation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### BaseFees
 The mapping of operation names to the base fees of those operations.

#### Python
```python
result = substrate.query(
    'ProtocolFee', 'BaseFees', [
    (
        'AssetRegisterTicker',
        'AssetIssue',
        'AssetAddDocuments',
        'AssetCreateAsset',
        'CheckpointCreateSchedule',
        'ComplianceManagerAddComplianceRequirement',
        'IdentityCddRegisterDid',
        'IdentityAddClaim',
        'IdentityAddSecondaryKeysWithAuthorization',
        'PipsPropose',
        'ContractsPutCode',
        'CorporateBallotAttachBallot',
        'CapitalDistributionDistribute',
        'NFTCreateCollection',
        'NFTMint',
        'IdentityCreateChildIdentity',
    ),
]
)
```

#### Return value
```python
'u128'
```
---------
### Coefficient
 The fee coefficient as a positive rational (numerator, denominator).

#### Python
```python
result = substrate.query(
    'ProtocolFee', 'Coefficient', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
## Errors

---------
### InsufficientAccountBalance
Insufficient account balance to pay the fee.

---------
### InsufficientSubsidyBalance
Insufficient subsidy balance to pay the fee.

---------
### UnHandledImbalances
Not able to handled the imbalances

---------