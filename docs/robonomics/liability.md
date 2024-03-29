
# Liability

---------
## Calls

---------
### create
Create agreement between two parties.
#### Attributes
| Name | Type |
| -------- | -------- | 
| agreement | `T::Agreement` | 

#### Python
```python
call = substrate.compose_call(
    'Liability', 'create', {
    'agreement': {
        'economics': {'price': 'u128'},
        'promisee': 'AccountId',
        'promisee_signature': {
            'Ecdsa': '[u8; 65]',
            'Ed25519': '[u8; 64]',
            'Sr25519': '[u8; 64]',
        },
        'promisor': 'AccountId',
        'promisor_signature': {
            'Ecdsa': '[u8; 65]',
            'Ed25519': '[u8; 64]',
            'Sr25519': '[u8; 64]',
        },
        'technics': {
            'hash': 'scale_info::9',
        },
    },
}
)
```

---------
### finalize
Publish technical report of complite works.
#### Attributes
| Name | Type |
| -------- | -------- | 
| report | `ReportFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Liability', 'finalize', {
    'report': {
        'index': 'u32',
        'payload': {
            'hash': 'scale_info::9',
        },
        'sender': 'AccountId',
        'signature': {
            'Ecdsa': '[u8; 65]',
            'Ed25519': '[u8; 64]',
            'Sr25519': '[u8; 64]',
        },
    },
}
)
```

---------
## Events

---------
### NewLiability
Yay! New liability created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Index` | ```u32```
| None | `TechnicsFor<T>` | ```{'hash': 'scale_info::9'}```
| None | `EconomicsFor<T>` | ```{'price': 'u128'}```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
### NewReport
Liability report published.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Index` | ```u32```
| None | `ReportFor<T>` | ```{'index': 'u32', 'sender': 'AccountId', 'payload': {'hash': 'scale_info::9'}, 'signature': {'Ed25519': '[u8; 64]', 'Sr25519': '[u8; 64]', 'Ecdsa': '[u8; 65]'}}```

---------
## Storage functions

---------
### AgreementOf
 Technical and economical parameters of liability.

#### Python
```python
result = substrate.query(
    'Liability', 'AgreementOf', ['u32']
)
```

#### Return value
```python
{
    'economics': {'price': 'u128'},
    'promisee': 'AccountId',
    'promisee_signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'promisor': 'AccountId',
    'promisor_signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'technics': {'hash': 'scale_info::9'},
}
```
---------
### LatestIndex
 [DEPRECATED] Latest liability index.
 TODO: remove after mainnet upgrade

#### Python
```python
result = substrate.query(
    'Liability', 'LatestIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### NextIndex
 Next liability index.

#### Python
```python
result = substrate.query(
    'Liability', 'NextIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### ReportOf
 Result of liability execution.

#### Python
```python
result = substrate.query(
    'Liability', 'ReportOf', ['u32']
)
```

#### Return value
```python
{
    'index': 'u32',
    'payload': {'hash': 'scale_info::9'},
    'sender': 'AccountId',
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
```
---------
## Errors

---------
### AgreementNotFound
Unable to load agreement from storage.

---------
### AlreadyFinalized
Liability already finalized.

---------
### BadAgreementProof
Agreement proof verification failed.

---------
### BadReportProof
Report proof verification failed.

---------
### BadReportSender
Wrong report sender account.

---------
### OracleIsNotReady
Real world oracle is not ready for this report.

---------