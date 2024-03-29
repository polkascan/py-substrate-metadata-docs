
# OraclePriceCollection

---------
## Calls

---------
### apply_update_collection_info
Apply an change previously proposed by
[`Pallet::propose_update_collection_info`] if the conditions to get
it ready are fullfilled.

This call is permissionless.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| change_id | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'OraclePriceCollection', 'apply_update_collection_info', {
    'change_id': 'scale_info::12',
    'collection_id': 'u64',
}
)
```

---------
### propose_update_collection_info
Propose an update of feeders associated to a specific collection.
The collection will only be modified once
[`Pallet::apply_update_collection_info`] is called.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| info | `types::CollectionInfo<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OraclePriceCollection', 'propose_update_collection_info', {
    'collection_id': 'u64',
    'info': {
        'feeders': 'scale_info::162',
        'min_feeders': 'u32',
        'value_lifetime': (
            None,
            'u64',
        ),
    },
}
)
```

---------
### update_collection
Update the collection, doing the aggregation for each key in the
process.

This call is permissionless.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'OraclePriceCollection', 'update_collection', {'collection_id': 'u64'}
)
```

---------
## Events

---------
### AddedKey
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u64```
| key | `T::OracleKey` | ```{'Isin': '[u8; 12]', 'ConversionRatio': ({'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'})}```

---------
### RemovedKey
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u64```
| key | `T::OracleKey` | ```{'Isin': '[u8; 12]', 'ConversionRatio': ({'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'})}```

---------
### UpdatedCollection
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u64```
| keys_updated | `u32` | ```u32```

---------
### UpdatedCollectionInfo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u64```
| collection_info | `types::CollectionInfo<T>` | ```{'value_lifetime': (None, 'u64'), 'min_feeders': 'u32', 'feeders': 'scale_info::162'}```

---------
## Storage functions

---------
### Collection
 Store all oracle values indexed by feeder

#### Python
```python
result = substrate.query(
    'OraclePriceCollection', 'Collection', ['u64']
)
```

#### Return value
```python
{
    'content': 'scale_info::784',
    'last_updated': 'u64',
    'older_value_timestamp': 'u64',
}
```
---------
### CollectionInfo
 Store all oracle values indexed by feeder

#### Python
```python
result = substrate.query(
    'OraclePriceCollection', 'CollectionInfo', ['u64']
)
```

#### Return value
```python
{
    'feeders': 'scale_info::162',
    'min_feeders': 'u32',
    'value_lifetime': (None, 'u64'),
}
```
---------
### CollectionKeyCount
 Store all oracle values indexed by feeder

#### Python
```python
result = substrate.query(
    'OraclePriceCollection', 'CollectionKeyCount', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### Keys
 Store the keys that are registed for this collection
 Only keys registered in this store can be used to create the collection

#### Python
```python
result = substrate.query(
    'OraclePriceCollection', 'Keys', [
    'u64',
    {
        'ConversionRatio': (
            {
                'Native': None,
                'Tranche': (
                    'u64',
                    '[u8; 16]',
                ),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'LocalAsset': 'u32',
                'Staking': (
                    'BlockRewards',
                ),
            },
            {
                'Native': None,
                'Tranche': (
                    'u64',
                    '[u8; 16]',
                ),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'LocalAsset': 'u32',
                'Staking': (
                    'BlockRewards',
                ),
            },
        ),
        'Isin': '[u8; 12]',
    },
]
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### MaxCollectionSize
 Max size of a data collection
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('OraclePriceCollection', 'MaxCollectionSize')
```
---------
### MaxFeedersPerKey
 Max number of collections
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('OraclePriceCollection', 'MaxFeedersPerKey')
```
---------
## Errors

---------
### IsNotAdmin
The account who trigger the action is not a collection admin.

---------
### KeyNotInCollection
The key is not in the collection.

---------
### KeyNotRegistered
The key is not registered

---------
### MaxCollectionSize
Collection size reached

---------
### NoOracleCollectionChangeId
The change id does not correspond to an oracle collection change

---------
### NotEnoughFeeders
The amount of feeders for a key is not enough

---------
### OracleValueOutdated
The oracle value has passed the collection max age.

---------