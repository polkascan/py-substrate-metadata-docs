
# StatefulStorage

---------
## Calls

---------
### apply_item_actions
#### Attributes
| Name | Type |
| -------- | -------- | 
| state_owner_msa_id | `MessageSourceId` | 
| schema_id | `SchemaId` | 
| target_hash | `PageHash` | 
| actions | `BoundedVec<ItemAction<T::MaxItemizedBlobSizeBytes>, T::
MaxItemizedActionsCount,>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'apply_item_actions', {
    'actions': [
        {
            'Add': {'data': 'Bytes'},
            'Delete': {'index': 'u16'},
        },
    ],
    'schema_id': 'u16',
    'state_owner_msa_id': 'u64',
    'target_hash': 'u32',
}
)
```

---------
### apply_item_actions_with_signature
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `ItemizedSignaturePayload<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'apply_item_actions_with_signature', {
    'delegator_key': 'AccountId',
    'payload': {
        'actions': [
            {
                'Add': {
                    'data': 'Bytes',
                },
                'Delete': {
                    'index': 'u16',
                },
            },
        ],
        'expiration': 'u32',
        'msa_id': 'u64',
        'schema_id': 'u16',
        'target_hash': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### apply_item_actions_with_signature_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `ItemizedSignaturePayloadV2<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'apply_item_actions_with_signature_v2', {
    'delegator_key': 'AccountId',
    'payload': {
        'actions': [
            {
                'Add': {
                    'data': 'Bytes',
                },
                'Delete': {
                    'index': 'u16',
                },
            },
        ],
        'expiration': 'u32',
        'schema_id': 'u16',
        'target_hash': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### delete_page
#### Attributes
| Name | Type |
| -------- | -------- | 
| state_owner_msa_id | `MessageSourceId` | 
| schema_id | `SchemaId` | 
| page_id | `PageId` | 
| target_hash | `PageHash` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'delete_page', {
    'page_id': 'u16',
    'schema_id': 'u16',
    'state_owner_msa_id': 'u64',
    'target_hash': 'u32',
}
)
```

---------
### delete_page_with_signature
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `PaginatedDeleteSignaturePayload<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'delete_page_with_signature', {
    'delegator_key': 'AccountId',
    'payload': {
        'expiration': 'u32',
        'msa_id': 'u64',
        'page_id': 'u16',
        'schema_id': 'u16',
        'target_hash': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### delete_page_with_signature_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `PaginatedDeleteSignaturePayloadV2<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'delete_page_with_signature_v2', {
    'delegator_key': 'AccountId',
    'payload': {
        'expiration': 'u32',
        'page_id': 'u16',
        'schema_id': 'u16',
        'target_hash': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### upsert_page
#### Attributes
| Name | Type |
| -------- | -------- | 
| state_owner_msa_id | `MessageSourceId` | 
| schema_id | `SchemaId` | 
| page_id | `PageId` | 
| target_hash | `PageHash` | 
| payload | `BoundedVec<u8,<T>::MaxPaginatedPageSizeBytes>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'upsert_page', {
    'page_id': 'u16',
    'payload': 'Bytes',
    'schema_id': 'u16',
    'state_owner_msa_id': 'u64',
    'target_hash': 'u32',
}
)
```

---------
### upsert_page_with_signature
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `PaginatedUpsertSignaturePayload<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'upsert_page_with_signature', {
    'delegator_key': 'AccountId',
    'payload': {
        'expiration': 'u32',
        'msa_id': 'u64',
        'page_id': 'u16',
        'payload': 'Bytes',
        'schema_id': 'u16',
        'target_hash': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### upsert_page_with_signature_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| payload | `PaginatedUpsertSignaturePayloadV2<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StatefulStorage', 'upsert_page_with_signature_v2', {
    'delegator_key': 'AccountId',
    'payload': {
        'expiration': 'u32',
        'page_id': 'u16',
        'payload': 'Bytes',
        'schema_id': 'u16',
        'target_hash': 'u32',
    },
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
## Events

---------
### ItemizedPageDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| schema_id | `SchemaId` | ```u16```
| prev_content_hash | `PageHash` | ```u32```

---------
### ItemizedPageUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| schema_id | `SchemaId` | ```u16```
| prev_content_hash | `PageHash` | ```u32```
| curr_content_hash | `PageHash` | ```u32```

---------
### PaginatedPageDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| schema_id | `SchemaId` | ```u16```
| page_id | `PageId` | ```u16```
| prev_content_hash | `PageHash` | ```u32```

---------
### PaginatedPageUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| schema_id | `SchemaId` | ```u16```
| page_id | `PageId` | ```u16```
| prev_content_hash | `PageHash` | ```u32```
| curr_content_hash | `PageHash` | ```u32```

---------
## Constants

---------
### MaxItemizedActionsCount
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('StatefulStorage', 'MaxItemizedActionsCount')
```
---------
### MaxItemizedBlobSizeBytes
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('StatefulStorage', 'MaxItemizedBlobSizeBytes')
```
---------
### MaxItemizedPageSizeBytes
#### Value
```python
65536
```
#### Python
```python
constant = substrate.get_constant('StatefulStorage', 'MaxItemizedPageSizeBytes')
```
---------
### MaxPaginatedPageId
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('StatefulStorage', 'MaxPaginatedPageId')
```
---------
### MaxPaginatedPageSizeBytes
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('StatefulStorage', 'MaxPaginatedPageSizeBytes')
```
---------
### MortalityWindowSize
#### Value
```python
14400
```
#### Python
```python
constant = substrate.get_constant('StatefulStorage', 'MortalityWindowSize')
```
---------
## Errors

---------
### CorruptedState

---------
### InvalidItemAction

---------
### InvalidMessageSourceAccount

---------
### InvalidSchemaId

---------
### InvalidSignature

---------
### PageExceedsMaxPageSizeBytes

---------
### PageIdExceedsMaxAllowed

---------
### ProofHasExpired

---------
### ProofNotYetValid

---------
### SchemaPayloadLocationMismatch

---------
### StalePageState

---------
### UnauthorizedDelegate

---------
### UnsupportedOperationForSchema

---------