
# Storage

---------
## Calls

---------
### accept_distribution_bucket_invitation
Accept pending invite.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| bucket_id | `DistributionBucketId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'accept_distribution_bucket_invitation', {
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
    'worker_id': 'u64',
}
)
```

---------
### accept_pending_data_objects
A storage provider signals that the data object was successfully uploaded to its storage.
&lt;weight&gt;

\#\# Weight
`O (W )` where:
- `W` is the number of items in `data_objects`
- DB:
   - `O(W)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| storage_bucket_id | `T::StorageBucketId` | 
| bag_id | `BagId<T>` | 
| data_objects | `BTreeSet<T::DataObjectId>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'accept_pending_data_objects', {
    'bag_id': {
        'Dynamic': {
            'Channel': 'u64',
            'Member': 'u64',
        },
        'Static': {
            'Council': None,
            'WorkingGroup': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        },
    },
    'data_objects': 'scale_info::84',
    'storage_bucket_id': 'u64',
    'worker_id': 'u64',
}
)
```

---------
### accept_storage_bucket_invitation
Accept the storage bucket invitation. An invitation must match the worker_id parameter.
It accepts an additional account ID (transactor) for accepting data objects to prevent
transaction nonce collisions.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| storage_bucket_id | `T::StorageBucketId` | 
| transactor_account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'accept_storage_bucket_invitation', {
    'storage_bucket_id': 'u64',
    'transactor_account_id': 'AccountId',
    'worker_id': 'u64',
}
)
```

---------
### cancel_distribution_bucket_operator_invite
Cancel pending invite. Must be pending.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bucket_id | `DistributionBucketId<T>` | 
| operator_worker_id | `WorkerId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'cancel_distribution_bucket_operator_invite', {
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
    'operator_worker_id': 'u64',
}
)
```

---------
### cancel_storage_bucket_operator_invite
Cancel pending storage bucket invite. An invitation must be pending.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| storage_bucket_id | `T::StorageBucketId` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'cancel_storage_bucket_operator_invite', {'storage_bucket_id': 'u64'}
)
```

---------
### create_distribution_bucket
Create a distribution bucket.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| family_id | `T::DistributionBucketFamilyId` | 
| accepting_new_bags | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'create_distribution_bucket', {
    'accepting_new_bags': 'bool',
    'family_id': 'u64',
}
)
```

---------
### create_distribution_bucket_family
Create a distribution bucket family.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Storage', 'create_distribution_bucket_family', {}
)
```

---------
### create_storage_bucket
Create storage bucket.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| invite_worker | `Option<WorkerId<T>>` | 
| accepting_new_bags | `bool` | 
| size_limit | `u64` | 
| objects_limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'create_storage_bucket', {
    'accepting_new_bags': 'bool',
    'invite_worker': (None, 'u64'),
    'objects_limit': 'u64',
    'size_limit': 'u64',
}
)
```

---------
### delete_distribution_bucket
Delete distribution bucket. Must be empty.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bucket_id | `DistributionBucketId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'delete_distribution_bucket', {
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
}
)
```

---------
### delete_distribution_bucket_family
Deletes a distribution bucket family.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| family_id | `T::DistributionBucketFamilyId` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'delete_distribution_bucket_family', {'family_id': 'u64'}
)
```

---------
### delete_storage_bucket
Delete storage bucket. Must be empty. Storage operator must be missing.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| storage_bucket_id | `T::StorageBucketId` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'delete_storage_bucket', {'storage_bucket_id': 'u64'}
)
```

---------
### distribution_operator_remark
Create a dynamic bag. Development mode.
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is size of `message` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| distribution_bucket_id | `DistributionBucketId<T>` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'distribution_operator_remark', {
    'distribution_bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
    'msg': 'Bytes',
    'worker_id': 'u64',
}
)
```

---------
### invite_distribution_bucket_operator
Invite an operator. Must be missing.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bucket_id | `DistributionBucketId<T>` | 
| operator_worker_id | `WorkerId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'invite_distribution_bucket_operator', {
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
    'operator_worker_id': 'u64',
}
)
```

---------
### invite_storage_bucket_operator
Invite storage bucket operator. Must be missing.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| storage_bucket_id | `T::StorageBucketId` | 
| operator_id | `WorkerId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'invite_storage_bucket_operator', {
    'operator_id': 'u64',
    'storage_bucket_id': 'u64',
}
)
```

---------
### remove_distribution_bucket_operator
Removes distribution bucket operator.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bucket_id | `DistributionBucketId<T>` | 
| operator_worker_id | `WorkerId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'remove_distribution_bucket_operator', {
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
    'operator_worker_id': 'u64',
}
)
```

---------
### remove_storage_bucket_operator
Removes storage bucket operator.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| storage_bucket_id | `T::StorageBucketId` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'remove_storage_bucket_operator', {'storage_bucket_id': 'u64'}
)
```

---------
### set_distribution_bucket_family_metadata
Set distribution bucket family metadata.
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is size of `metadata` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| family_id | `T::DistributionBucketFamilyId` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'set_distribution_bucket_family_metadata', {
    'family_id': 'u64',
    'metadata': 'Bytes',
}
)
```

---------
### set_distribution_operator_metadata
Set distribution operator metadata for the distribution bucket.
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is size of `metadata` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| bucket_id | `DistributionBucketId<T>` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'set_distribution_operator_metadata', {
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
    'metadata': 'Bytes',
    'worker_id': 'u64',
}
)
```

---------
### set_storage_bucket_voucher_limits
Sets storage bucket voucher limits.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| storage_bucket_id | `T::StorageBucketId` | 
| new_objects_size_limit | `u64` | 
| new_objects_number_limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'set_storage_bucket_voucher_limits', {
    'new_objects_number_limit': 'u64',
    'new_objects_size_limit': 'u64',
    'storage_bucket_id': 'u64',
}
)
```

---------
### set_storage_operator_metadata
Sets storage operator metadata (eg.: storage node URL).
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is size of `metadata` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| storage_bucket_id | `T::StorageBucketId` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'set_storage_operator_metadata', {
    'metadata': 'Bytes',
    'storage_bucket_id': 'u64',
    'worker_id': 'u64',
}
)
```

---------
### storage_operator_remark
Deposit a StorageOperatorRemarked event
containing a generic message.
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is size of `message` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| storage_bucket_id | `T::StorageBucketId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'storage_operator_remark', {
    'msg': 'Bytes',
    'storage_bucket_id': 'u64',
    'worker_id': 'u64',
}
)
```

---------
### update_blacklist
Add and remove hashes to the current blacklist.
&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the number of items in `remove_hashes`
- `V` is the number of items in `add_hashes`
- DB:
   - `O(W)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| remove_hashes | `BTreeSet<Vec<u8>>` | 
| add_hashes | `BTreeSet<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_blacklist', {
    'add_hashes': 'scale_info::163',
    'remove_hashes': 'scale_info::163',
}
)
```

---------
### update_data_object_state_bloat_bond
Updates data object state bloat bond value.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| state_bloat_bond | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_data_object_state_bloat_bond', {'state_bloat_bond': 'u128'}
)
```

---------
### update_data_size_fee
Updates size-based pricing of new objects uploaded.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_data_size_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_data_size_fee', {'new_data_size_fee': 'u128'}
)
```

---------
### update_distribution_bucket_mode
Updates &\#x27;distributing&\#x27; flag for the distributing flag.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bucket_id | `DistributionBucketId<T>` | 
| distributing | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_distribution_bucket_mode', {
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
    'distributing': 'bool',
}
)
```

---------
### update_distribution_bucket_status
Updates a distribution bucket &\#x27;accepts new bags&\#x27; flag.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bucket_id | `DistributionBucketId<T>` | 
| accepting_new_bags | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_distribution_bucket_status', {
    'accepting_new_bags': 'bool',
    'bucket_id': {
        'distribution_bucket_family_id': 'u64',
        'distribution_bucket_index': 'u64',
    },
}
)
```

---------
### update_distribution_buckets_for_bag
Updates distribution buckets for a bag.
&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the number of items in `add_buckets_indices`
- `V` is the number of items in `remove_buckets_indices`
- DB:
   - `O(V + W)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bag_id | `BagId<T>` | 
| family_id | `T::DistributionBucketFamilyId` | 
| add_buckets_indices | `BTreeSet<T::DistributionBucketIndex>` | 
| remove_buckets_indices | `BTreeSet<T::DistributionBucketIndex>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_distribution_buckets_for_bag', {
    'add_buckets_indices': 'scale_info::84',
    'bag_id': {
        'Dynamic': {
            'Channel': 'u64',
            'Member': 'u64',
        },
        'Static': {
            'Council': None,
            'WorkingGroup': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        },
    },
    'family_id': 'u64',
    'remove_buckets_indices': 'scale_info::84',
}
)
```

---------
### update_distribution_buckets_per_bag_limit
Updates &quot;Distribution buckets per bag&quot; number limit.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_distribution_buckets_per_bag_limit', {'new_limit': 'u32'}
)
```

---------
### update_families_in_dynamic_bag_creation_policy
Update number of distributed buckets used in given dynamic bag creation policy.
Updates distribution buckets for a bag.
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the number of items in `families`
- DB:
   - `O(W)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dynamic_bag_type | `DynamicBagType` | 
| families | `BTreeMap<T::DistributionBucketFamilyId, u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_families_in_dynamic_bag_creation_policy', {
    'dynamic_bag_type': (
        'Member',
        'Channel',
    ),
    'families': 'scale_info::167',
}
)
```

---------
### update_number_of_storage_buckets_in_dynamic_bag_creation_policy
Update number of storage buckets used in given dynamic bag creation policy.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dynamic_bag_type | `DynamicBagType` | 
| number_of_storage_buckets | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_number_of_storage_buckets_in_dynamic_bag_creation_policy', {
    'dynamic_bag_type': (
        'Member',
        'Channel',
    ),
    'number_of_storage_buckets': 'u32',
}
)
```

---------
### update_storage_bucket_status
Update whether new bags are being accepted for storage.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| storage_bucket_id | `T::StorageBucketId` | 
| accepting_new_bags | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_storage_bucket_status', {
    'accepting_new_bags': 'bool',
    'storage_bucket_id': 'u64',
}
)
```

---------
### update_storage_buckets_for_bag
Updates storage buckets for a bag.
&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the number of items in `add_buckets`
- `V` is the number of items in `remove_buckets`
- DB:
   - `O(V + W)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bag_id | `BagId<T>` | 
| add_buckets | `BTreeSet<T::StorageBucketId>` | 
| remove_buckets | `BTreeSet<T::StorageBucketId>` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_storage_buckets_for_bag', {
    'add_buckets': 'scale_info::84',
    'bag_id': {
        'Dynamic': {
            'Channel': 'u64',
            'Member': 'u64',
        },
        'Static': {
            'Council': None,
            'WorkingGroup': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        },
    },
    'remove_buckets': 'scale_info::84',
}
)
```

---------
### update_storage_buckets_per_bag_limit
Updates &quot;Storage buckets per bag&quot; number limit.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_storage_buckets_per_bag_limit', {'new_limit': 'u32'}
)
```

---------
### update_storage_buckets_voucher_max_limits
Updates &quot;Storage buckets voucher max limits&quot;.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_objects_size | `u64` | 
| new_objects_number | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_storage_buckets_voucher_max_limits', {
    'new_objects_number': 'u64',
    'new_objects_size': 'u64',
}
)
```

---------
### update_uploading_blocked_status
Updates global uploading flag.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_status | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Storage', 'update_uploading_blocked_status', {'new_status': 'bool'}
)
```

---------
## Events

---------
### DataObjectPerMegabyteFeeUpdated
Emits on changing the size-based pricing of new objects uploaded.
Params
- new data size fee
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### DataObjectStateBloatBondValueUpdated
Emits on updating the data object state bloat bond.
Params
- state bloat bond value
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### DataObjectsDeleted
Emits on data objects deletion from bags.
Params
- account ID for the state bloat bond
- bag ID
- data object IDs
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `BagId` | ```{'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::84```

---------
### DataObjectsMoved
Emits on moving data objects between bags.
Params
- source bag ID
- destination bag ID
- data object IDs
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BagId` | ```{'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}```
| None | `BagId` | ```{'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::84```

---------
### DataObjectsUpdated
Emits on storage assets being uploaded and deleted at the same time
Params
- UploadParameters
- Ids of the uploaded objects
- Ids of the removed objects
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `UploadParameters` | ```{'bag_id': {'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}, 'object_creation_list': [{'size': 'u64', 'ipfs_content_id': 'Bytes'}], 'state_bloat_bond_source_account_id': 'AccountId', 'expected_data_size_fee': 'u128', 'expected_data_object_state_bloat_bond': 'u128'}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::84```
| None | `BTreeSet<DataObjectId>` | ```scale_info::84```

---------
### DataObjectsUploaded
Emits on uploading data objects.
Params
- data objects IDs
- initial uploading parameters
- state bloat bond for objects
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BTreeSet<DataObjectId>` | ```scale_info::84```
| None | `UploadParameters` | ```{'bag_id': {'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}, 'object_creation_list': [{'size': 'u64', 'ipfs_content_id': 'Bytes'}], 'state_bloat_bond_source_account_id': 'AccountId', 'expected_data_size_fee': 'u128', 'expected_data_object_state_bloat_bond': 'u128'}```
| None | `Balance` | ```u128```

---------
### DistributionBucketCreated
Emits on creating distribution bucket.
Params
- distribution bucket family ID
- accepting new bags
- distribution bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketFamilyId` | ```u64```
| None | `bool` | ```bool```
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```

---------
### DistributionBucketDeleted
Emits on deleting distribution bucket.
Params
- distribution bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```

---------
### DistributionBucketFamilyCreated
Emits on creating distribution bucket family.
Params
- distribution family bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketFamilyId` | ```u64```

---------
### DistributionBucketFamilyDeleted
Emits on deleting distribution bucket family.
Params
- distribution family bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketFamilyId` | ```u64```

---------
### DistributionBucketFamilyMetadataSet
Emits on setting the metadata by a distribution bucket family.
Params
- distribution bucket family ID
- metadata
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketFamilyId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### DistributionBucketInvitationAccepted
Emits on accepting a distribution bucket invitation for the operator.
Params
- worker ID
- distribution bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```

---------
### DistributionBucketInvitationCancelled
Emits on canceling a distribution bucket invitation for the operator.
Params
- distribution bucket ID
- operator worker ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```
| None | `WorkerId` | ```u64```

---------
### DistributionBucketMetadataSet
Emits on setting the metadata by a distribution bucket operator.
Params
- worker ID
- distribution bucket ID
- metadata
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```
| None | `Vec<u8>` | ```Bytes```

---------
### DistributionBucketModeUpdated
Emits on storage bucket mode update (distributing flag).
Params
- distribution bucket ID
- distributing
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```
| None | `bool` | ```bool```

---------
### DistributionBucketOperatorInvited
Emits on creating a distribution bucket invitation for the operator.
Params
- distribution bucket ID
- worker ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```
| None | `WorkerId` | ```u64```

---------
### DistributionBucketOperatorRemoved
Emits on the distribution bucket operator removal.
Params
- distribution bucket ID
- distribution bucket operator ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```
| None | `WorkerId` | ```u64```

---------
### DistributionBucketStatusUpdated
Emits on storage bucket status update (accepting new bags).
Params
- distribution bucket ID
- new status (accepting new bags)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```
| None | `bool` | ```bool```

---------
### DistributionBucketsPerBagLimitUpdated
Emits on changing the &quot;Distribution buckets per bag&quot; number limit.
Params
- new limit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### DistributionBucketsUpdatedForBag
Emits on updating distribution buckets for bag.
Params
- bag ID
- storage buckets to add ID collection
- storage buckets to remove ID collection
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BagId` | ```{'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}```
| None | `DistributionBucketFamilyId` | ```u64```
| None | `BTreeSet<DistributionBucketIndex>` | ```scale_info::84```
| None | `BTreeSet<DistributionBucketIndex>` | ```scale_info::84```

---------
### DistributionOperatorRemarked
Emits on Distribution Operator making a remark
Params
- operator&\#x27;s worker id
- distribution bucket id
- remark message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `DistributionBucketId` | ```{'distribution_bucket_family_id': 'u64', 'distribution_bucket_index': 'u64'}```
| None | `Vec<u8>` | ```Bytes```

---------
### DynamicBagCreated
Emits on creating a dynamic bag.
Params
- dynamic bag creation parameters
- uploaded data objects ids
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DynamicBagCreationParameters` | ```{'bag_id': {'Member': 'u64', 'Channel': 'u64'}, 'object_creation_list': [{'size': 'u64', 'ipfs_content_id': 'Bytes'}], 'state_bloat_bond_source_account_id': 'AccountId', 'expected_data_size_fee': 'u128', 'expected_data_object_state_bloat_bond': 'u128', 'storage_buckets': 'scale_info::84', 'distribution_buckets': 'scale_info::136'}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::84```

---------
### DynamicBagDeleted
Emits on deleting a dynamic bag.
Params
- dynamic bag ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DynamicBagId` | ```{'Member': 'u64', 'Channel': 'u64'}```

---------
### FamiliesInDynamicBagCreationPolicyUpdated
Emits on dynamic bag creation policy update (distribution bucket families).
Params
- dynamic bag type
- families and bucket numbers
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DynamicBagType` | ```('Member', 'Channel')```
| None | `BTreeMap<DistributionBucketFamilyId, u32>` | ```scale_info::167```

---------
### NumberOfStorageBucketsInDynamicBagCreationPolicyUpdated
Emits on updating the number of storage buckets in dynamic bag creation policy.
Params
- dynamic bag type
- new number of storage buckets
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DynamicBagType` | ```('Member', 'Channel')```
| None | `u32` | ```u32```

---------
### PendingDataObjectsAccepted
Emits on accepting pending data objects.
Params
- storage bucket ID
- worker ID (storage provider ID)
- bag ID
- pending data objects
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `WorkerId` | ```u64```
| None | `BagId` | ```{'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::84```

---------
### StorageBucketCreated
Emits on creating the storage bucket.
Params
- storage bucket ID
- invited worker
- flag &quot;accepting_new_bags&quot;
- size limit for voucher,
- objects limit for voucher,
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `Option<WorkerId>` | ```(None, 'u64')```
| None | `bool` | ```bool```
| None | `u64` | ```u64```
| None | `u64` | ```u64```

---------
### StorageBucketDeleted
Emits on storage bucket deleting.
Params
- storage bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```

---------
### StorageBucketInvitationAccepted
Emits on accepting the storage bucket invitation.
Params
- storage bucket ID
- invited worker ID
- transactor account ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `WorkerId` | ```u64```
| None | `AccountId` | ```AccountId```

---------
### StorageBucketInvitationCancelled
Emits on cancelling the storage bucket invitation.
Params
- storage bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```

---------
### StorageBucketOperatorInvited
Emits on the storage bucket operator invitation.
Params
- storage bucket ID
- operator worker ID (storage provider ID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `WorkerId` | ```u64```

---------
### StorageBucketOperatorRemoved
Emits on the storage bucket operator removal.
Params
- storage bucket ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```

---------
### StorageBucketStatusUpdated
Emits on storage bucket status update.
Params
- storage bucket ID
- new status
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `bool` | ```bool```

---------
### StorageBucketVoucherLimitsSet
Emits on setting the storage bucket voucher limits.
Params
- storage bucket ID
- new total objects size limit
- new total objects number limit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `u64` | ```u64```
| None | `u64` | ```u64```

---------
### StorageBucketsPerBagLimitUpdated
Emits on changing the &quot;Storage buckets per bag&quot; number limit.
Params
- new limit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### StorageBucketsUpdatedForBag
Emits on updating storage buckets for bag.
Params
- bag ID
- storage buckets to add ID collection
- storage buckets to remove ID collection
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BagId` | ```{'Static': {'Council': None, 'WorkingGroup': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'Dynamic': {'Member': 'u64', 'Channel': 'u64'}}```
| None | `BTreeSet<StorageBucketId>` | ```scale_info::84```
| None | `BTreeSet<StorageBucketId>` | ```scale_info::84```

---------
### StorageBucketsVoucherMaxLimitsUpdated
Emits on changing the &quot;Storage buckets voucher max limits&quot;.
Params
- new objects size limit
- new objects number limit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```
| None | `u64` | ```u64```

---------
### StorageOperatorMetadataSet
Emits on setting the storage operator metadata.
Params
- storage bucket ID
- invited worker ID
- metadata
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `WorkerId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### StorageOperatorRemarked
Emits on Storage Operator making a remark
Params
- operator&\#x27;s worker id
- storage bucket id
- remark message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `StorageBucketId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### UpdateBlacklist
Emits on updating the blacklist with data hashes.
Params
- hashes to remove from the blacklist
- hashes to add to the blacklist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BTreeSet<Vec<u8>>` | ```scale_info::163```
| None | `BTreeSet<Vec<u8>>` | ```scale_info::163```

---------
### UploadingBlockStatusUpdated
Emits on changing the size-based pricing of new objects uploaded.
Params
- new status
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### VoucherChanged
Emits on changing the voucher for a storage bucket.
Params
- storage bucket ID
- new voucher
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StorageBucketId` | ```u64```
| None | `Voucher` | ```{'size_limit': 'u64', 'objects_limit': 'u64', 'size_used': 'u64', 'objects_used': 'u64'}```

---------
## Storage functions

---------
### Bags
 Bags storage map.

#### Python
```python
result = substrate.query(
    'Storage', 'Bags', [
    {
        'Dynamic': {
            'Channel': 'u64',
            'Member': 'u64',
        },
        'Static': {
            'Council': None,
            'WorkingGroup': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        },
    },
]
)
```

#### Return value
```python
{
    'distributed_by': 'scale_info::136',
    'objects_number': 'u64',
    'objects_total_size': 'u64',
    'stored_by': 'scale_info::84',
}
```
---------
### Blacklist
 Blacklisted data object hashes.

#### Python
```python
result = substrate.query(
    'Storage', 'Blacklist', ['Bytes']
)
```

#### Return value
```python
()
```
---------
### CurrentBlacklistSize
 Blacklist collection counter.

#### Python
```python
result = substrate.query(
    'Storage', 'CurrentBlacklistSize', []
)
```

#### Return value
```python
'u64'
```
---------
### DataObjectPerMegabyteFee
 Size based pricing of new objects uploaded.

#### Python
```python
result = substrate.query(
    'Storage', 'DataObjectPerMegabyteFee', []
)
```

#### Return value
```python
'u128'
```
---------
### DataObjectStateBloatBondValue
 The state bloat bond for the data objects (helps preventing the state bloat).

#### Python
```python
result = substrate.query(
    'Storage', 'DataObjectStateBloatBondValue', []
)
```

#### Return value
```python
'u128'
```
---------
### DataObjectsById
 &#x27;Data objects for bags&#x27; storage double map.

#### Python
```python
result = substrate.query(
    'Storage', 'DataObjectsById', [
    {
        'Dynamic': {
            'Channel': 'u64',
            'Member': 'u64',
        },
        'Static': {
            'Council': None,
            'WorkingGroup': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        },
    },
    'u64',
]
)
```

#### Return value
```python
{
    'accepted': 'bool',
    'ipfs_content_id': 'Bytes',
    'size': 'u64',
    'state_bloat_bond': {
        'amount': 'u128',
        'repayment_restricted_to': (None, 'AccountId'),
    },
}
```
---------
### DistributionBucketByFamilyIdById
 &#x27;Distribution bucket&#x27; storage double map.

#### Python
```python
result = substrate.query(
    'Storage', 'DistributionBucketByFamilyIdById', ['u64', 'u64']
)
```

#### Return value
```python
{
    'accepting_new_bags': 'bool',
    'assigned_bags': 'u64',
    'distributing': 'bool',
    'operators': 'scale_info::84',
    'pending_invitations': 'scale_info::84',
}
```
---------
### DistributionBucketFamilyById
 Distribution bucket families.

#### Python
```python
result = substrate.query(
    'Storage', 'DistributionBucketFamilyById', ['u64']
)
```

#### Return value
```python
{'next_distribution_bucket_index': 'u64'}
```
---------
### DistributionBucketFamilyNumber
 Total number of distribution bucket families in the system.

#### Python
```python
result = substrate.query(
    'Storage', 'DistributionBucketFamilyNumber', []
)
```

#### Return value
```python
'u64'
```
---------
### DistributionBucketsPerBagLimit
 &quot;Distribution buckets per bag&quot; number limit.

#### Python
```python
result = substrate.query(
    'Storage', 'DistributionBucketsPerBagLimit', []
)
```

#### Return value
```python
'u32'
```
---------
### DynamicBagCreationPolicies
 DynamicBagCreationPolicy by bag type storage map.

#### Python
```python
result = substrate.query(
    'Storage', 'DynamicBagCreationPolicies', [('Member', 'Channel')]
)
```

#### Return value
```python
{'families': 'scale_info::167', 'number_of_storage_buckets': 'u32'}
```
---------
### NextDataObjectId
 Data object id counter. Starts at zero.

#### Python
```python
result = substrate.query(
    'Storage', 'NextDataObjectId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextDistributionBucketFamilyId
 Distribution bucket family id counter. Starts at zero.

#### Python
```python
result = substrate.query(
    'Storage', 'NextDistributionBucketFamilyId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextStorageBucketId
 Storage bucket id counter. Starts at zero.

#### Python
```python
result = substrate.query(
    'Storage', 'NextStorageBucketId', []
)
```

#### Return value
```python
'u64'
```
---------
### StorageBucketById
 Storage buckets.

#### Python
```python
result = substrate.query(
    'Storage', 'StorageBucketById', ['u64']
)
```

#### Return value
```python
{
    'accepting_new_bags': 'bool',
    'assigned_bags': 'u64',
    'operator_status': {
        'InvitedStorageWorker': 'u64',
        'Missing': None,
        'StorageWorker': ('u64', 'AccountId'),
    },
    'voucher': {
        'objects_limit': 'u64',
        'objects_used': 'u64',
        'size_limit': 'u64',
        'size_used': 'u64',
    },
}
```
---------
### StorageBucketsPerBagLimit
 &quot;Storage buckets per bag&quot; number limit.

#### Python
```python
result = substrate.query(
    'Storage', 'StorageBucketsPerBagLimit', []
)
```

#### Return value
```python
'u32'
```
---------
### UploadingBlocked
 Defines whether all new uploads blocked

#### Python
```python
result = substrate.query(
    'Storage', 'UploadingBlocked', []
)
```

#### Return value
```python
'bool'
```
---------
### VoucherMaxObjectsNumberLimit
 &quot;Max objects number for a storage  bucket voucher&quot; number limit.

#### Python
```python
result = substrate.query(
    'Storage', 'VoucherMaxObjectsNumberLimit', []
)
```

#### Return value
```python
'u64'
```
---------
### VoucherMaxObjectsSizeLimit
 &quot;Max objects size for a storage bucket voucher&quot; number limit.

#### Python
```python
result = substrate.query(
    'Storage', 'VoucherMaxObjectsSizeLimit', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### BlacklistSizeLimit
 Exports const - maximum size of the &quot;hash blacklist&quot; collection.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Storage', 'BlacklistSizeLimit')
```
---------
### DefaultChannelDynamicBagNumberOfStorageBuckets
 Exports const - the default dynamic bag creation policy for channels (storage bucket
 number).
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Storage', 'DefaultChannelDynamicBagNumberOfStorageBuckets')
```
---------
### DefaultMemberDynamicBagNumberOfStorageBuckets
 Exports const - the default dynamic bag creation policy for members (storage bucket
 number).
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Storage', 'DefaultMemberDynamicBagNumberOfStorageBuckets')
```
---------
### MaxDataObjectSize
 Exports const - max data object size in bytes.
#### Value
```python
64424509440
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MaxDataObjectSize')
```
---------
### MaxDistributionBucketFamilyNumber
 Exports const - max allowed distribution bucket family number.
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MaxDistributionBucketFamilyNumber')
```
---------
### MaxDistributionBucketsPerBag
 Exports const - maximum number of distribution buckets per bag.
#### Value
```python
51
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MaxDistributionBucketsPerBag')
```
---------
### MaxNumberOfOperatorsPerDistributionBucket
 Exports const - max number of operators per distribution bucket.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MaxNumberOfOperatorsPerDistributionBucket')
```
---------
### MaxNumberOfPendingInvitationsPerDistributionBucket
 Exports const - max number of pending invitations per distribution bucket.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MaxNumberOfPendingInvitationsPerDistributionBucket')
```
---------
### MaxStorageBucketsPerBag
 Exports const - maximum number of storage buckets per bag.
#### Value
```python
13
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MaxStorageBucketsPerBag')
```
---------
### MinDistributionBucketsPerBag
 Exports const - minimum number of distribution buckets per bag.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MinDistributionBucketsPerBag')
```
---------
### MinStorageBucketsPerBag
 Exports const - minimum number of storage buckets per bag.
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('Storage', 'MinStorageBucketsPerBag')
```
---------
## Errors

---------
### ArithmeticError
Generic Arithmetic Error due to internal accounting operation

---------
### BlacklistSizeLimitExceeded
Blacklist size limit exceeded.

---------
### CallDisabled
Call Disabled

---------
### CannotDeleteNonEmptyDynamicBag
Cannot delete non empty dynamic bag.

---------
### CannotDeleteNonEmptyStorageBucket
Cannot delete a non-empty storage bucket.

---------
### DataObjectBlacklisted
Data object hash is part of the blacklist.

---------
### DataObjectDoesntExist
Data object doesn&\#x27;t exist.

---------
### DataObjectIdCollectionIsEmpty
Data object id collection is empty.

---------
### DataObjectIdParamsAreEmpty
The `data_object_ids` extrinsic parameter collection is empty.

---------
### DataObjectStateBloatBondChanged
Invalid extrinsic call: data object state bloat bond changed.

---------
### DataSizeFeeChanged
Invalid extrinsic call: data size fee changed.

---------
### DifferentStorageProviderInvited
Invalid operation with invites: another storage provider was invited.

---------
### DistributionBucketDoesntAcceptNewBags
Distribution bucket doesn&\#x27;t accept new bags.

---------
### DistributionBucketDoesntExist
Distribution bucket doesn&\#x27;t exist.

---------
### DistributionBucketFamilyDoesntExist
Distribution bucket family doesn&\#x27;t exist.

---------
### DistributionBucketIdCollectionsAreEmpty
Distribution bucket id collections are empty.

---------
### DistributionBucketIsBoundToBag
Distribution bucket is bound to a bag.

---------
### DistributionBucketIsNotBoundToBag
Distribution bucket is not bound to a bag.

---------
### DistributionBucketsPerBagLimitTooHigh
The new `DistributionBucketsPerBagLimit` number is too high.

---------
### DistributionBucketsPerBagLimitTooLow
The new `DistributionBucketsPerBagLimit` number is too low.

---------
### DistributionBucketsViolatesDynamicBagCreationPolicy
Distribution bucket id collection provided contradicts the existing dynamic bag
creation policy.

---------
### DistributionFamilyBoundToBagCreationPolicy
Distribution family bound to a bag creation policy.

---------
### DistributionProviderOperatorAlreadyInvited
Distribution provider operator already invited.

---------
### DistributionProviderOperatorDoesntExist
Distribution provider operator doesn&\#x27;t exist.

---------
### DistributionProviderOperatorSet
Distribution provider operator already set.

---------
### DynamicBagDoesntExist
Dynamic bag doesn&\#x27;t exist.

---------
### DynamicBagExists
Cannot create the dynamic bag: dynamic bag exists.

---------
### EmptyContentId
Upload data error: empty content ID provided.

---------
### InsufficientBalance
Insufficient balance for an operation.

---------
### InsufficientTreasuryBalance
Insufficient module treasury balance for an operation.

---------
### InvalidCidLength
Invalid CID length (must be 46 bytes)

---------
### InvalidStateBloatBondSourceAccount
Upload data error: invalid state bloat bond source account.

---------
### InvalidStorageProvider
Invalid storage provider for bucket.

---------
### InvalidTransactorAccount
Invalid transactor account ID for this bucket.

---------
### InvitedStorageProvider
Invalid operation with invites: storage provider was already invited.

---------
### MaxDataObjectSizeExceeded
Max data object size exceeded.

---------
### MaxDistributionBucketFamilyNumberLimitExceeded
Max distribution bucket family number limit exceeded.

---------
### MaxDistributionBucketNumberPerBagLimitExceeded
Max distribution bucket number per bag limit exceeded.

---------
### MaxNumberOfOperatorsPerDistributionBucketReached
Max number of operators for a distribution bucket reached.

---------
### MaxNumberOfPendingInvitationsLimitForDistributionBucketReached
Max number of pending invitations limit for a distribution bucket reached.

---------
### MustBeDistributionProviderOperatorForBucket
Invalid operations: must be a distribution provider operator for a bucket.

---------
### NoDistributionBucketInvitation
No distribution bucket invitation.

---------
### NoObjectsOnUpload
Empty &quot;data object creation&quot; collection.

---------
### NoStorageBucketInvitation
Invalid operation with invites: there is no storage bucket invitation.

---------
### NumberOfDistributionBucketsOutsideOfAllowedContraints
Not allowed &\#x27;number of distribution buckets&\#x27;

---------
### NumberOfStorageBucketsOutsideOfAllowedContraints
Not allowed &\#x27;number of storage buckets&\#x27;

---------
### SourceAndDestinationBagsAreEqual
Cannot move objects within the same bag.

---------
### StorageBucketDoesntAcceptNewBags
The storage bucket doesn&\#x27;t accept new bags.

---------
### StorageBucketDoesntExist
The requested storage bucket doesn&\#x27;t exist.

---------
### StorageBucketIdCollectionsAreEmpty
Storage bucket id collections are empty.

---------
### StorageBucketIsBoundToBag
The requested storage bucket is already bound to a bag.

---------
### StorageBucketIsNotBoundToBag
The requested storage bucket is not bound to a bag.

---------
### StorageBucketObjectNumberLimitReached
Object number limit for the storage bucket reached.

---------
### StorageBucketObjectSizeLimitReached
Objects total size limit for the storage bucket reached.

---------
### StorageBucketPerBagLimitExceeded
`StorageBucketsPerBagLimit` was exceeded for a bag.

---------
### StorageBucketsNumberViolatesDynamicBagCreationPolicy
Storage bucket id collection provided contradicts the existing dynamic bag
creation policy.

---------
### StorageBucketsPerBagLimitTooHigh
The new `StorageBucketsPerBagLimit` number is too high.

---------
### StorageBucketsPerBagLimitTooLow
The new `StorageBucketsPerBagLimit` number is too low.

---------
### StorageProviderAlreadySet
Invalid operation with invites: storage provider was already set.

---------
### StorageProviderMustBeSet
Storage provider must be set.

---------
### StorageProviderOperatorDoesntExist
Storage provider operator doesn&\#x27;t exist.

---------
### UploadingBlocked
Uploading of the new object is blocked.

---------
### VoucherMaxObjectNumberLimitExceeded
Max object number limit exceeded for voucher.

---------
### VoucherMaxObjectSizeLimitExceeded
Max object size limit exceeded for voucher.

---------
### ZeroObjectSize
Upload data error: zero object size.

---------