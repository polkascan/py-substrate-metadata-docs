
# Schemas

---------
## Calls

---------
### create_schema
#### Attributes
| Name | Type |
| -------- | -------- | 
| model | `BoundedVec<u8, T::SchemaModelMaxBytesBoundedVecLimit>` | 
| model_type | `ModelType` | 
| payload_location | `PayloadLocation` | 

#### Python
```python
call = substrate.compose_call(
    'Schemas', 'create_schema', {
    'model': 'Bytes',
    'model_type': (
        'AvroBinary',
        'Parquet',
    ),
    'payload_location': (
        'OnChain',
        'IPFS',
        'Itemized',
        'Paginated',
    ),
}
)
```

---------
### create_schema_via_governance
#### Attributes
| Name | Type |
| -------- | -------- | 
| creator_key | `T::AccountId` | 
| model | `BoundedVec<u8, T::SchemaModelMaxBytesBoundedVecLimit>` | 
| model_type | `ModelType` | 
| payload_location | `PayloadLocation` | 
| settings | `BoundedVec<SchemaSetting, T::MaxSchemaSettingsPerSchema>` | 

#### Python
```python
call = substrate.compose_call(
    'Schemas', 'create_schema_via_governance', {
    'creator_key': 'AccountId',
    'model': 'Bytes',
    'model_type': (
        'AvroBinary',
        'Parquet',
    ),
    'payload_location': (
        'OnChain',
        'IPFS',
        'Itemized',
        'Paginated',
    ),
    'settings': [
        (
            'AppendOnly',
            'SignatureRequired',
        ),
    ],
}
)
```

---------
### propose_to_create_schema
#### Attributes
| Name | Type |
| -------- | -------- | 
| model | `BoundedVec<u8, T::SchemaModelMaxBytesBoundedVecLimit>` | 
| model_type | `ModelType` | 
| payload_location | `PayloadLocation` | 
| settings | `BoundedVec<SchemaSetting, T::MaxSchemaSettingsPerSchema>` | 

#### Python
```python
call = substrate.compose_call(
    'Schemas', 'propose_to_create_schema', {
    'model': 'Bytes',
    'model_type': (
        'AvroBinary',
        'Parquet',
    ),
    'payload_location': (
        'OnChain',
        'IPFS',
        'Itemized',
        'Paginated',
    ),
    'settings': [
        (
            'AppendOnly',
            'SignatureRequired',
        ),
    ],
}
)
```

---------
### set_max_schema_model_bytes
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_size | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Schemas', 'set_max_schema_model_bytes', {'max_size': 'u32'}
)
```

---------
## Events

---------
### SchemaCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key | `T::AccountId` | ```AccountId```
| schema_id | `SchemaId` | ```u16```

---------
### SchemaMaxSizeChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| max_size | `u32` | ```u32```

---------
## Storage functions

---------
### CurrentSchemaIdentifierMaximum

#### Python
```python
result = substrate.query(
    'Schemas', 'CurrentSchemaIdentifierMaximum', []
)
```

#### Return value
```python
'u16'
```
---------
### GovernanceSchemaModelMaxBytes

#### Python
```python
result = substrate.query(
    'Schemas', 'GovernanceSchemaModelMaxBytes', []
)
```

#### Return value
```python
'u32'
```
---------
### Schemas

#### Python
```python
result = substrate.query(
    'Schemas', 'Schemas', ['u16']
)
```

#### Return value
```python
{
    'model': 'Bytes',
    'model_type': ('AvroBinary', 'Parquet'),
    'payload_location': ('OnChain', 'IPFS', 'Itemized', 'Paginated'),
    'settings': 'u16',
}
```
---------
## Constants

---------
### MaxSchemaRegistrations
#### Value
```python
65000
```
#### Python
```python
constant = substrate.get_constant('Schemas', 'MaxSchemaRegistrations')
```
---------
### MaxSchemaSettingsPerSchema
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Schemas', 'MaxSchemaSettingsPerSchema')
```
---------
### MinSchemaModelSizeBytes
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('Schemas', 'MinSchemaModelSizeBytes')
```
---------
### SchemaModelMaxBytesBoundedVecLimit
#### Value
```python
65500
```
#### Python
```python
constant = substrate.get_constant('Schemas', 'SchemaModelMaxBytesBoundedVecLimit')
```
---------
## Errors

---------
### ExceedsMaxSchemaModelBytes

---------
### InvalidSchema

---------
### InvalidSetting

---------
### LessThanMinSchemaModelBytes

---------
### SchemaCountOverflow

---------