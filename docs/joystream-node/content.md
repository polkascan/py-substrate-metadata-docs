
# Content

---------
## Calls

---------
### accept_channel_transfer
Accepts channel transfer.
`commitment_params` is required to prevent changing the transfer conditions.

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the number of entries in `commitment_params.new_collaborators` map
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_id | `T::ChannelId` | 
| commitment_params | `TransferCommitmentWitnessOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'accept_channel_transfer', {
    'channel_id': 'u64',
    'commitment_params': {
        'new_collaborators': 'scale_info::132',
        'price': 'u128',
        'transfer_id': 'u64',
    },
}
)
```

---------
### accept_incoming_offer
Accept incoming Nft offer

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| video_id | `T::VideoId` | 
| witness_price | `Option<<T as balances::Config>::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'accept_incoming_offer', {
    'video_id': 'u64',
    'witness_price': (None, 'u128'),
}
)
```

---------
### add_curator_to_group
Add curator to curator group under given `curator_group_id`

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| curator_group_id | `T::CuratorGroupId` | 
| curator_id | `T::CuratorId` | 
| permissions | `ChannelAgentPermissions` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'add_curator_to_group', {
    'curator_group_id': 'u64',
    'curator_id': 'u64',
    'permissions': 'scale_info::104',
}
)
```

---------
### buy_nft
Buy Nft

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| video_id | `T::VideoId` | 
| participant_id | `T::MemberId` | 
| witness_price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'buy_nft', {
    'participant_id': 'u64',
    'video_id': 'u64',
    'witness_price': 'u128',
}
)
```

---------
### cancel_buy_now
Cancel Nft sell order

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
&lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'cancel_buy_now', {
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### cancel_channel_transfer
cancel channel transfer

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_id | `T::ChannelId` | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'cancel_channel_transfer', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
}
)
```

---------
### cancel_english_auction
Cancel video nft english auction
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'cancel_english_auction', {
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### cancel_offer
Cancel Nft offer

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'cancel_offer', {
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### cancel_open_auction
Cancel video nft open auction
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'cancel_open_auction', {
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### cancel_open_auction_bid
Cancel open auction bid
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| participant_id | `T::MemberId` | 
| video_id | `T::VideoId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'cancel_open_auction_bid', {
    'participant_id': 'u64',
    'video_id': 'u64',
}
)
```

---------
### channel_agent_remark
Channel collaborator remark
&lt;weight&gt;

\#\# Weight
`O (B)`
- DB:
   - O(1)
where:
  - B is the byte lenght of `msg`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'channel_agent_remark', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'msg': 'Bytes',
}
)
```

---------
### channel_owner_remark
Channel owner remark
&lt;weight&gt;

\#\# Weight
`O (B)`
- DB:
   - O(1)
where:
- B is the kilobyte lenght of `msg`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_id | `T::ChannelId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'channel_owner_remark', {'channel_id': 'u64', 'msg': 'Bytes'}
)
```

---------
### claim_and_withdraw_channel_reward
Claim and withdraw reward in JOY from channel account

&lt;weight&gt;

\#\# Weight
`O (H)` where:
- `H` is the lenght of the provided merkle `proof`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| proof | `Vec<ProofElement<T>>` | 
| item | `PullPayment<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'claim_and_withdraw_channel_reward', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'item': {
        'channel_id': 'u64',
        'cumulative_reward_earned': 'u128',
        'reason': '[u8; 32]',
    },
    'proof': [
        {
            'hash': '[u8; 32]',
            'side': ('Left', 'Right'),
        },
    ],
}
)
```

---------
### claim_channel_reward
Claim reward in JOY from channel account

&lt;weight&gt;

\#\# Weight
`O (H)` where:
- `H` is the lenght of the provided merkle `proof`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| proof | `Vec<ProofElement<T>>` | 
| item | `PullPayment<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'claim_channel_reward', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'item': {
        'channel_id': 'u64',
        'cumulative_reward_earned': 'u128',
        'reason': '[u8; 32]',
    },
    'proof': [
        {
            'hash': '[u8; 32]',
            'side': ('Left', 'Right'),
        },
    ],
}
)
```

---------
### claim_creator_token_patronage_credit
Claim channel&\#x27;s creator token patronage credit

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'claim_creator_token_patronage_credit', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
}
)
```

---------
### create_channel
&lt;weight&gt;

\#\# Weight
`O (A + B + C + D + E)` where:
- `A` is the number of entries in `params.collaborators`
- `B` is the number of items in `params.storage_buckets`
- `C` is the number of items in `params.distribution_buckets`
- `D` is the number of items in `params.assets.object_creation_list`
- `E` is the size of  `params.meta` in kilobytes
- DB:
   - `O(A + B + C + D)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_owner | `ChannelOwner<T::MemberId, T::CuratorGroupId>` | 
| params | `ChannelCreationParameters<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'create_channel', {
    'channel_owner': {
        'CuratorGroup': 'u64',
        'Member': 'u64',
    },
    'params': {
        'assets': (
            None,
            {
                'expected_data_size_fee': 'u128',
                'object_creation_list': [
                    {
                        'ipfs_content_id': 'Bytes',
                        'size': 'u64',
                    },
                ],
            },
        ),
        'collaborators': 'scale_info::132',
        'distribution_buckets': 'scale_info::135',
        'expected_channel_state_bloat_bond': 'u128',
        'expected_data_object_state_bloat_bond': 'u128',
        'meta': (None, 'Bytes'),
        'storage_buckets': 'scale_info::83',
    },
}
)
```

---------
### create_curator_group
Add new curator group to runtime storage

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the number of entries in `permissions_by_level` map
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| is_active | `bool` | 
| permissions_by_level | `ModerationPermissionsByLevel<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'create_curator_group', {
    'is_active': 'bool',
    'permissions_by_level': 'scale_info::142',
}
)
```

---------
### create_video
&lt;weight&gt;

\#\# Weight
`O (A + B + C + D)` where:
- `A` is the number of items in `params.assets.object_creation_list`
- `B` is `params.storage_buckets_num_witness`
- `C` is the length of open auction / english auction whitelist (if provided)
- `D` is the size of `params.meta` in kilobytes (if provided)
- DB:
   - `O(A + B + C)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| params | `VideoCreationParameters<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'create_video', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'params': {
        'assets': (
            None,
            {
                'expected_data_size_fee': 'u128',
                'object_creation_list': [
                    {
                        'ipfs_content_id': 'Bytes',
                        'size': 'u64',
                    },
                ],
            },
        ),
        'auto_issue_nft': (
            None,
            {
                'init_transactional_status': {
                    'BuyNow': 'u128',
                    'EnglishAuction': {
                        'buy_now_price': (
                            None,
                            'u128',
                        ),
                        'duration': 'u32',
                        'extension_period': 'u32',
                        'min_bid_step': 'u128',
                        'starting_price': 'u128',
                        'starts_at': (
                            None,
                            'u32',
                        ),
                        'whitelist': 'scale_info::83',
                    },
                    'Idle': None,
                    'InitiatedOfferToMember': (
                        'u64',
                        (None, 'u128'),
                    ),
                    'OpenAuction': {
                        'bid_lock_duration': 'u32',
                        'buy_now_price': (
                            None,
                            'u128',
                        ),
                        'starting_price': 'u128',
                        'starts_at': (
                            None,
                            'u32',
                        ),
                        'whitelist': 'scale_info::83',
                    },
                },
                'nft_metadata': 'Bytes',
                'non_channel_owner': (
                    None,
                    'u64',
                ),
                'royalty': (
                    None,
                    'u32',
                ),
            },
        ),
        'expected_data_object_state_bloat_bond': 'u128',
        'expected_video_state_bloat_bond': 'u128',
        'meta': (None, 'Bytes'),
        'storage_buckets_num_witness': 'u32',
    },
}
)
```

---------
### creator_token_issuer_transfer
Perform transfer of tokens as creator token issuer

&lt;weight&gt;

\#\# Weight
`O (A + B)` where:
- `A` is the number of entries in `outputs`
- `B` is the size of the `metadata` in kilobytes
- DB:
   - `O(A)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| outputs | `TransfersWithVestingOf<T>` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'creator_token_issuer_transfer', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'metadata': 'Bytes',
    'outputs': 'scale_info::393',
}
)
```

---------
### deissue_creator_token
Deissue channel&\#x27;s creator token

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'deissue_creator_token', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
}
)
```

---------
### delete_channel
&lt;weight&gt;

\#\# Weight
`O (A + B + C)` where:
- `A` is `num_objects_to_delete`
- `B` is `channel_bag_witness.storage_buckets_num`
- `C` is `channel_bag_witness.distribution_buckets_num`
- DB:
   - `O(A + B + C)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| channel_bag_witness | `ChannelBagWitness` | 
| num_objects_to_delete | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'delete_channel', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_bag_witness': {
        'distribution_buckets_num': 'u32',
        'storage_buckets_num': 'u32',
    },
    'channel_id': 'u64',
    'num_objects_to_delete': 'u64',
}
)
```

---------
### delete_channel_as_moderator
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| channel_bag_witness | `ChannelBagWitness` | 
| num_objects_to_delete | `u64` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'delete_channel_as_moderator', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_bag_witness': {
        'distribution_buckets_num': 'u32',
        'storage_buckets_num': 'u32',
    },
    'channel_id': 'u64',
    'num_objects_to_delete': 'u64',
    'rationale': 'Bytes',
}
)
```

---------
### delete_channel_assets_as_moderator
&lt;weight&gt;

\#\# Weight
`O (A + B + C)` where:
- `A` is the length of `assets_to_remove`
- `B` is the value of `storage_buckets_num_witness`
- `C` is the size of `rationale` in kilobytes
- DB:
   - `O(A + B)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| assets_to_remove | `BTreeSet<DataObjectId<T>>` | 
| storage_buckets_num_witness | `u32` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'delete_channel_assets_as_moderator', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'assets_to_remove': 'scale_info::83',
    'channel_id': 'u64',
    'rationale': 'Bytes',
    'storage_buckets_num_witness': 'u32',
}
)
```

---------
### delete_video
&lt;weight&gt;

\#\# Weight
`O (A + B)` where:
- `A` is num_objects_to_delete
- `B` is `params.storage_buckets_num_witness` (if provided)
- DB:
   - `O(A + B)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| num_objects_to_delete | `u64` | 
| storage_buckets_num_witness | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'delete_video', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'num_objects_to_delete': 'u64',
    'storage_buckets_num_witness': (
        None,
        'u32',
    ),
    'video_id': 'u64',
}
)
```

---------
### delete_video_as_moderator
&lt;weight&gt;

\#\# Weight
`O (A + B + C)` where:
- `A` is the value of `num_objects_to_delete`
- `B` is the value of `storage_buckets_num_witness`
- `C` is the size of `rationale` in kilobytes
- DB:
   - `O(A + B)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| storage_buckets_num_witness | `Option<u32>` | 
| num_objects_to_delete | `u64` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'delete_video_as_moderator', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'num_objects_to_delete': 'u64',
    'rationale': 'Bytes',
    'storage_buckets_num_witness': (
        None,
        'u32',
    ),
    'video_id': 'u64',
}
)
```

---------
### delete_video_assets_as_moderator
&lt;weight&gt;

\#\# Weight
`O (A + B + C)` where:
- `A` is the length of `assets_to_remove`
- `B` is the value of `storage_buckets_num_witness`
- `C` is the size of `rationale` in kilobytes
- DB:
   - `O(A + B)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| storage_buckets_num_witness | `u32` | 
| assets_to_remove | `BTreeSet<DataObjectId<T>>` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'delete_video_assets_as_moderator', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'assets_to_remove': 'scale_info::83',
    'rationale': 'Bytes',
    'storage_buckets_num_witness': 'u32',
    'video_id': 'u64',
}
)
```

---------
### destroy_nft
Destroy NFT

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'destroy_nft', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### finalize_creator_token_sale
Finalize an ended creator token sale

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'finalize_creator_token_sale', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
}
)
```

---------
### finalize_revenue_split
Finalize an ended revenue split

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'finalize_revenue_split', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
}
)
```

---------
### init_creator_token_sale
Initialize creator token sale

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the size of `params.metadata` in kilobytes (or 0 if not provided)
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| params | `TokenSaleParamsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'init_creator_token_sale', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'params': {
        'cap_per_member': (
            None,
            'u128',
        ),
        'duration': 'u32',
        'metadata': (None, 'Bytes'),
        'starts_at': (None, 'u32'),
        'unit_price': 'u128',
        'upper_bound_quantity': 'u128',
        'vesting_schedule_params': (
            None,
            {
                'blocks_before_cliff': 'u32',
                'cliff_amount_percentage': 'u32',
                'linear_vesting_duration': 'u32',
            },
        ),
    },
}
)
```

---------
### initialize_channel_transfer
Start a channel transfer with specified characteristics

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the number of entries in `transfer_params.new_collaborators` map
- DB:
   - O(A) - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_id | `T::ChannelId` | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| transfer_params | `InitTransferParametersOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'initialize_channel_transfer', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'transfer_params': {
        'new_collaborators': 'scale_info::132',
        'new_owner': {
            'CuratorGroup': 'u64',
            'Member': 'u64',
        },
        'price': 'u128',
    },
}
)
```

---------
### issue_creator_token
Issue creator token

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the number of entries in `params.initial_allocation` map
- DB:
   - `O(A)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| params | `TokenIssuanceParametersOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'issue_creator_token', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'params': {
        'initial_allocation': 'scale_info::180',
        'patronage_rate': 'u32',
        'revenue_split_rate': 'u32',
        'symbol': '[u8; 32]',
        'transfer_policy': {
            'Permissioned': {
                'commitment': '[u8; 32]',
                'payload': (
                    None,
                    {
                        'expected_data_object_state_bloat_bond': 'u128',
                        'expected_data_size_fee': 'u128',
                        'object_creation_params': {
                            'ipfs_content_id': 'Bytes',
                            'size': 'u64',
                        },
                    },
                ),
            },
            'Permissionless': None,
        },
    },
}
)
```

---------
### issue_nft
Issue NFT

&lt;weight&gt;

\#\# Weight
`O (W + B)`
- DB:
   - O(W)
where:
   - W : member whitelist length in case nft initial status is auction
   - B : size of metadata parameter in kilobytes
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| params | `NftIssuanceParameters<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'issue_nft', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'params': {
        'init_transactional_status': {
            'BuyNow': 'u128',
            'EnglishAuction': {
                'buy_now_price': (
                    None,
                    'u128',
                ),
                'duration': 'u32',
                'extension_period': 'u32',
                'min_bid_step': 'u128',
                'starting_price': 'u128',
                'starts_at': (
                    None,
                    'u32',
                ),
                'whitelist': 'scale_info::83',
            },
            'Idle': None,
            'InitiatedOfferToMember': (
                'u64',
                (None, 'u128'),
            ),
            'OpenAuction': {
                'bid_lock_duration': 'u32',
                'buy_now_price': (
                    None,
                    'u128',
                ),
                'starting_price': 'u128',
                'starts_at': (
                    None,
                    'u32',
                ),
                'whitelist': 'scale_info::83',
            },
        },
        'nft_metadata': 'Bytes',
        'non_channel_owner': (
            None,
            'u64',
        ),
        'royalty': (None, 'u32'),
    },
    'video_id': 'u64',
}
)
```

---------
### issue_revenue_split
Issue revenue split for a channel

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| start | `Option<T::BlockNumber>` | 
| duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'issue_revenue_split', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'duration': 'u32',
    'start': (None, 'u32'),
}
)
```

---------
### make_creator_token_permissionless
Make channel&\#x27;s creator token permissionless

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'make_creator_token_permissionless', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
}
)
```

---------
### make_english_auction_bid
Make english auction bid
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| participant_id | `T::MemberId` | 
| video_id | `T::VideoId` | 
| bid_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'make_english_auction_bid', {
    'bid_amount': 'u128',
    'participant_id': 'u64',
    'video_id': 'u64',
}
)
```

---------
### make_open_auction_bid
Make auction bid
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| participant_id | `T::MemberId` | 
| video_id | `T::VideoId` | 
| bid_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'make_open_auction_bid', {
    'bid_amount': 'u128',
    'participant_id': 'u64',
    'video_id': 'u64',
}
)
```

---------
### nft_owner_remark
NFT owner remark
&lt;weight&gt;

\#\# Weight
`O (B)`
- DB:
  - O(1)
where:
  - B is the byte lenght of `msg`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'nft_owner_remark', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'msg': 'Bytes',
    'video_id': 'u64',
}
)
```

---------
### offer_nft
Offer Nft

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| video_id | `T::VideoId` | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| to | `T::MemberId` | 
| price | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'offer_nft', {
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'price': (None, 'u128'),
    'to': 'u64',
    'video_id': 'u64',
}
)
```

---------
### pick_open_auction_winner
Accept open auction bid
Should only be called by auctioneer
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| winner_id | `T::MemberId` | 
| commit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'pick_open_auction_winner', {
    'commit': 'u128',
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
    'winner_id': 'u64',
}
)
```

---------
### reduce_creator_token_patronage_rate_to
Reduce channel&\#x27;s creator token patronage rate to given value

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| target_rate | `YearlyRate` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'reduce_creator_token_patronage_rate_to', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'target_rate': 'u32',
}
)
```

---------
### remove_curator_from_group
Remove curator from a given curator group

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| curator_group_id | `T::CuratorGroupId` | 
| curator_id | `T::CuratorId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'remove_curator_from_group', {
    'curator_group_id': 'u64',
    'curator_id': 'u64',
}
)
```

---------
### sell_nft
Sell Nft
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| video_id | `T::VideoId` | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'sell_nft', {
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'price': 'u128',
    'video_id': 'u64',
}
)
```

---------
### set_channel_paused_features_as_moderator
Extrinsic for pausing/re-enabling channel features

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the size of `rationale` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| new_paused_features | `BTreeSet<PausableChannelFeature>` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'set_channel_paused_features_as_moderator', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'new_paused_features': 'scale_info::111',
    'rationale': 'Bytes',
}
)
```

---------
### set_channel_visibility_as_moderator
Extrinsic for setting channel visibility status (hidden/visible) by moderator

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the size of `rationale` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| is_hidden | `bool` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'set_channel_visibility_as_moderator', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'is_hidden': 'bool',
    'rationale': 'Bytes',
}
)
```

---------
### set_curator_group_status
Set `is_active` status for curator group under given `curator_group_id`

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| curator_group_id | `T::CuratorGroupId` | 
| is_active | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'set_curator_group_status', {
    'curator_group_id': 'u64',
    'is_active': 'bool',
}
)
```

---------
### set_video_visibility_as_moderator
Extrinsic for video visibility status (hidden/visible) setting by moderator

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the size of `rationale` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| is_hidden | `bool` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'set_video_visibility_as_moderator', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'is_hidden': 'bool',
    'rationale': 'Bytes',
    'video_id': 'u64',
}
)
```

---------
### settle_english_auction
Claim won english auction
Can be called by anyone
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| video_id | `T::VideoId` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'settle_english_auction', {'video_id': 'u64'}
)
```

---------
### sling_nft_back
Return Nft back to the original artist at no cost

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| video_id | `T::VideoId` | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'sling_nft_back', {
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### start_english_auction
Start video nft english auction
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- W : whitelist member list length
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| auction_params | `EnglishAuctionParams<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'start_english_auction', {
    'auction_params': {
        'buy_now_price': (
            None,
            'u128',
        ),
        'duration': 'u32',
        'extension_period': 'u32',
        'min_bid_step': 'u128',
        'starting_price': 'u128',
        'starts_at': (None, 'u32'),
        'whitelist': 'scale_info::83',
    },
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### start_open_auction
Start video nft open auction
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- W : member whitelist length
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| auction_params | `OpenAuctionParams<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'start_open_auction', {
    'auction_params': {
        'bid_lock_duration': 'u32',
        'buy_now_price': (
            None,
            'u128',
        ),
        'starting_price': 'u128',
        'starts_at': (None, 'u32'),
        'whitelist': 'scale_info::83',
    },
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### toggle_nft_limits
Only Council can toggle nft issuance limits constraints
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'toggle_nft_limits', {'enabled': 'bool'}
)
```

---------
### update_buy_now_price
Update Buy now nft price

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| new_price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_buy_now_price', {
    'new_price': 'u128',
    'owner_id': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'video_id': 'u64',
}
)
```

---------
### update_channel
&lt;weight&gt;

\#\# Weight
`O (A + B + C + D + E)` where:
- `A` is the number of entries in `params.collaborators`
- `B` is the number of items in `params.assets_to_upload.object_creation_list` (if provided)
- `C` is the number of items in `params.assets_to_remove`
- `D` is the size of `params.new_meta` in kilobytes
- `E` is `params.storage_buckets_num_witness` (if provided)
- DB:
   - `O(A + B + C + E)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| params | `ChannelUpdateParameters<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_channel', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'params': {
        'assets_to_remove': 'scale_info::83',
        'assets_to_upload': (
            None,
            {
                'expected_data_size_fee': 'u128',
                'object_creation_list': [
                    {
                        'ipfs_content_id': 'Bytes',
                        'size': 'u64',
                    },
                ],
            },
        ),
        'collaborators': (
            None,
            'scale_info::132',
        ),
        'expected_data_object_state_bloat_bond': 'u128',
        'new_meta': (None, 'Bytes'),
        'storage_buckets_num_witness': (
            None,
            'u32',
        ),
    },
}
)
```

---------
### update_channel_nft_limit
Updates channel&\#x27;s NFT limit.
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| nft_limit_period | `NftLimitPeriod` | 
| channel_id | `T::ChannelId` | 
| limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_channel_nft_limit', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'limit': 'u64',
    'nft_limit_period': (
        'Daily',
        'Weekly',
    ),
}
)
```

---------
### update_channel_payouts
Update channel payouts

&lt;weight&gt;

\#\# Weight
`O (1)` where:
- DB:
- O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `UpdateChannelPayoutsParameters<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_channel_payouts', {
    'params': {
        'channel_cashouts_enabled': (
            None,
            'bool',
        ),
        'commitment': (
            None,
            '[u8; 32]',
        ),
        'max_cashout_allowed': (
            None,
            'u128',
        ),
        'min_cashout_allowed': (
            None,
            'u128',
        ),
        'payload': (
            None,
            {
                'expected_data_object_state_bloat_bond': 'u128',
                'expected_data_size_fee': 'u128',
                'object_creation_params': {
                    'ipfs_content_id': 'Bytes',
                    'size': 'u64',
                },
                'uploader_account': 'AccountId',
            },
        ),
    },
}
)
```

---------
### update_channel_privilege_level
Extrinsic for updating channel privilege level (requires lead access)

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_id | `T::ChannelId` | 
| new_privilege_level | `T::ChannelPrivilegeLevel` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_channel_privilege_level', {
    'channel_id': 'u64',
    'new_privilege_level': 'u8',
}
)
```

---------
### update_channel_state_bloat_bond
Updates channel state bloat bond value.
Only lead can upload this value

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_channel_state_bloat_bond | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_channel_state_bloat_bond', {
    'new_channel_state_bloat_bond': 'u128',
}
)
```

---------
### update_curator_group_permissions
Update existing curator group&\#x27;s permissions

&lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the number of entries in `permissions_by_level` map
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| curator_group_id | `T::CuratorGroupId` | 
| permissions_by_level | `ModerationPermissionsByLevel<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_curator_group_permissions', {
    'curator_group_id': 'u64',
    'permissions_by_level': 'scale_info::142',
}
)
```

---------
### update_global_nft_limit
Updates global NFT limit
&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| nft_limit_period | `NftLimitPeriod` | 
| limit | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_global_nft_limit', {
    'limit': 'u64',
    'nft_limit_period': (
        'Daily',
        'Weekly',
    ),
}
)
```

---------
### update_upcoming_creator_token_sale
Update upcoming creator token sale

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| new_start_block | `Option<T::BlockNumber>` | 
| new_duration | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_upcoming_creator_token_sale', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'channel_id': 'u64',
    'new_duration': (None, 'u32'),
    'new_start_block': (None, 'u32'),
}
)
```

---------
### update_video
&lt;weight&gt;

\#\# Weight
`O (A + B + C + D + E)` where:
- `A` is params.assets_to_upload.object_creation_list.len() (if provided)
- `B` is params.assets_to_remove.len()
- `C` is `params.storage_buckets_num_witness` (if provided)
- `D` is the length of open auction / english auction whitelist (if provided)
- `E` is the size of `params.new_meta` in kilobytes (if provided)
- DB:
   - `O(A + B + C + D)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| video_id | `T::VideoId` | 
| params | `VideoUpdateParameters<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_video', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'params': {
        'assets_to_remove': 'scale_info::83',
        'assets_to_upload': (
            None,
            {
                'expected_data_size_fee': 'u128',
                'object_creation_list': [
                    {
                        'ipfs_content_id': 'Bytes',
                        'size': 'u64',
                    },
                ],
            },
        ),
        'auto_issue_nft': (
            None,
            {
                'init_transactional_status': {
                    'BuyNow': 'u128',
                    'EnglishAuction': {
                        'buy_now_price': (
                            None,
                            'u128',
                        ),
                        'duration': 'u32',
                        'extension_period': 'u32',
                        'min_bid_step': 'u128',
                        'starting_price': 'u128',
                        'starts_at': (
                            None,
                            'u32',
                        ),
                        'whitelist': 'scale_info::83',
                    },
                    'Idle': None,
                    'InitiatedOfferToMember': (
                        'u64',
                        (None, 'u128'),
                    ),
                    'OpenAuction': {
                        'bid_lock_duration': 'u32',
                        'buy_now_price': (
                            None,
                            'u128',
                        ),
                        'starting_price': 'u128',
                        'starts_at': (
                            None,
                            'u32',
                        ),
                        'whitelist': 'scale_info::83',
                    },
                },
                'nft_metadata': 'Bytes',
                'non_channel_owner': (
                    None,
                    'u64',
                ),
                'royalty': (
                    None,
                    'u32',
                ),
            },
        ),
        'expected_data_object_state_bloat_bond': 'u128',
        'new_meta': (None, 'Bytes'),
        'storage_buckets_num_witness': (
            None,
            'u32',
        ),
    },
    'video_id': 'u64',
}
)
```

---------
### update_video_state_bloat_bond
Updates video state bloat bond value.
Only lead can upload this value

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_video_state_bloat_bond | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'update_video_state_bloat_bond', {'new_video_state_bloat_bond': 'u128'}
)
```

---------
### withdraw_from_channel_balance
Withdraw JOY from channel account

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `ContentActor<T::CuratorGroupId, T::CuratorId, T::MemberId>` | 
| channel_id | `T::ChannelId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Content', 'withdraw_from_channel_balance', {
    'actor': {
        'Curator': ('u64', 'u64'),
        'Lead': None,
        'Member': 'u64',
    },
    'amount': 'u128',
    'channel_id': 'u64',
}
)
```

---------
## Events

---------
### AuctionBidCanceled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `VideoId` | ```u64```

---------
### AuctionBidMade
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `VideoId` | ```u64```
| None | `Balance` | ```u128```
| None | `Option<MemberId>` | ```(None, 'u64')```

---------
### AuctionCanceled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```

---------
### BidMadeCompletingAuction
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `VideoId` | ```u64```
| None | `Option<MemberId>` | ```(None, 'u64')```

---------
### BuyNowCanceled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```

---------
### BuyNowPriceUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `Balance` | ```u128```

---------
### CancelChannelTransfer
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChannelId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```

---------
### ChannelAgentRemarked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### ChannelAssetsDeletedByModerator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `BTreeSet<DataObjectId>` | ```scale_info::83```
| None | `Vec<u8>` | ```Bytes```

---------
### ChannelAssetsRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `BTreeSet<DataObjectId>` | ```scale_info::83```
| None | `Channel` | ```{'owner': {'Member': 'u64', 'CuratorGroup': 'u64'}, 'num_videos': 'u64', 'collaborators': 'scale_info::106', 'cumulative_reward_claimed': 'u128', 'privilege_level': 'u8', 'paused_features': 'scale_info::111', 'transfer_status': {'NoActiveTransfer': None, 'PendingTransfer': {'new_owner': {'Member': 'u64', 'CuratorGroup': 'u64'}, 'transfer_params': {'new_collaborators': 'scale_info::106', 'price': 'u128', 'transfer_id': 'u64'}}}, 'data_objects': 'scale_info::83', 'daily_nft_limit': {'limit': 'u64', 'block_number_period': 'u32'}, 'weekly_nft_limit': {'limit': 'u64', 'block_number_period': 'u32'}, 'daily_nft_counter': {'counter': 'u64', 'last_updated': 'u32'}, 'weekly_nft_counter': {'counter': 'u64', 'last_updated': 'u32'}, 'creator_token_id': (None, 'u64'), 'channel_state_bloat_bond': {'repayment_restricted_to': (None, 'AccountId'), 'amount': 'u128'}}```

---------
### ChannelCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChannelId` | ```u64```
| None | `Channel` | ```{'owner': {'Member': 'u64', 'CuratorGroup': 'u64'}, 'num_videos': 'u64', 'collaborators': 'scale_info::106', 'cumulative_reward_claimed': 'u128', 'privilege_level': 'u8', 'paused_features': 'scale_info::111', 'transfer_status': {'NoActiveTransfer': None, 'PendingTransfer': {'new_owner': {'Member': 'u64', 'CuratorGroup': 'u64'}, 'transfer_params': {'new_collaborators': 'scale_info::106', 'price': 'u128', 'transfer_id': 'u64'}}}, 'data_objects': 'scale_info::83', 'daily_nft_limit': {'limit': 'u64', 'block_number_period': 'u32'}, 'weekly_nft_limit': {'limit': 'u64', 'block_number_period': 'u32'}, 'daily_nft_counter': {'counter': 'u64', 'last_updated': 'u32'}, 'weekly_nft_counter': {'counter': 'u64', 'last_updated': 'u32'}, 'creator_token_id': (None, 'u64'), 'channel_state_bloat_bond': {'repayment_restricted_to': (None, 'AccountId'), 'amount': 'u128'}}```
| None | `ChannelCreationParameters` | ```{'assets': (None, {'object_creation_list': [{'size': 'u64', 'ipfs_content_id': 'Bytes'}], 'expected_data_size_fee': 'u128'}), 'meta': (None, 'Bytes'), 'collaborators': 'scale_info::132', 'storage_buckets': 'scale_info::83', 'distribution_buckets': 'scale_info::135', 'expected_channel_state_bloat_bond': 'u128', 'expected_data_object_state_bloat_bond': 'u128'}```
| None | `AccountId` | ```AccountId```

---------
### ChannelDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```

---------
### ChannelDeletedByModerator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### ChannelFundsWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `Balance` | ```u128```
| None | `ChannelFundsDestination` | ```{'AccountId': 'AccountId', 'CouncilBudget': None}```

---------
### ChannelNftLimitUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `NftLimitPeriod` | ```('Daily', 'Weekly')```
| None | `ChannelId` | ```u64```
| None | `u64` | ```u64```

---------
### ChannelOwnerRemarked
Metaprotocols related event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChannelId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### ChannelPausedFeaturesUpdatedByModerator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `BTreeSet<PausableChannelFeature>` | ```scale_info::111```
| None | `Vec<u8>` | ```Bytes```

---------
### ChannelPayoutsUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `UpdateChannelPayoutsParameters` | ```{'commitment': (None, '[u8; 32]'), 'payload': (None, {'uploader_account': 'AccountId', 'object_creation_params': {'size': 'u64', 'ipfs_content_id': 'Bytes'}, 'expected_data_size_fee': 'u128', 'expected_data_object_state_bloat_bond': 'u128'}), 'min_cashout_allowed': (None, 'u128'), 'max_cashout_allowed': (None, 'u128'), 'channel_cashouts_enabled': (None, 'bool')}```
| None | `Option<DataObjectId>` | ```(None, 'u64')```

---------
### ChannelPrivilegeLevelUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChannelId` | ```u64```
| None | `ChannelPrivilegeLevel` | ```u8```

---------
### ChannelRewardClaimedAndWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `Balance` | ```u128```
| None | `ChannelFundsDestination` | ```{'AccountId': 'AccountId', 'CouncilBudget': None}```

---------
### ChannelRewardUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```
| None | `ChannelId` | ```u64```

---------
### ChannelStateBloatBondValueUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### ChannelTransferAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChannelId` | ```u64```
| None | `TransferCommitmentWitness` | ```{'new_collaborators': 'scale_info::132', 'price': 'u128', 'transfer_id': 'u64'}```

---------
### ChannelUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `ChannelUpdateParameters` | ```{'assets_to_upload': (None, {'object_creation_list': [{'size': 'u64', 'ipfs_content_id': 'Bytes'}], 'expected_data_size_fee': 'u128'}), 'new_meta': (None, 'Bytes'), 'assets_to_remove': 'scale_info::83', 'collaborators': (None, 'scale_info::132'), 'expected_data_object_state_bloat_bond': 'u128', 'storage_buckets_num_witness': (None, 'u32')}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::83```

---------
### ChannelVisibilitySetByModerator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `bool` | ```bool```
| None | `Vec<u8>` | ```Bytes```

---------
### CouncilRewardClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChannelId` | ```u64```
| None | `Balance` | ```u128```

---------
### CreatorTokenIssued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `TokenId` | ```u64```

---------
### CuratorAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CuratorGroupId` | ```u64```
| None | `CuratorId` | ```u64```
| None | `ChannelAgentPermissions` | ```scale_info::104```

---------
### CuratorGroupCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CuratorGroupId` | ```u64```

---------
### CuratorGroupPermissionsUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CuratorGroupId` | ```u64```
| None | `ModerationPermissionsByLevel` | ```scale_info::142```

---------
### CuratorGroupStatusSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CuratorGroupId` | ```u64```
| None | `bool` | ```bool```

---------
### CuratorRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CuratorGroupId` | ```u64```
| None | `CuratorId` | ```u64```

---------
### EnglishAuctionSettled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `VideoId` | ```u64```

---------
### EnglishAuctionStarted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `EnglishAuctionParams` | ```{'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'whitelist': 'scale_info::83', 'starts_at': (None, 'u32'), 'duration': 'u32', 'extension_period': 'u32', 'min_bid_step': 'u128'}```

---------
### GlobalNftLimitUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `NftLimitPeriod` | ```('Daily', 'Weekly')```
| None | `u64` | ```u64```

---------
### InitializedChannelTransfer
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChannelId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `PendingTransfer` | ```{'new_owner': {'Member': 'u64', 'CuratorGroup': 'u64'}, 'transfer_params': {'new_collaborators': 'scale_info::106', 'price': 'u128', 'transfer_id': 'u64'}}```

---------
### NftBought
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```
| None | `MemberId` | ```u64```

---------
### NftDestroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```

---------
### NftIssued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `NftIssuanceParameters` | ```{'royalty': (None, 'u32'), 'nft_metadata': 'Bytes', 'non_channel_owner': (None, 'u64'), 'init_transactional_status': {'Idle': None, 'BuyNow': 'u128', 'InitiatedOfferToMember': ('u64', (None, 'u128')), 'EnglishAuction': {'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'whitelist': 'scale_info::83', 'starts_at': (None, 'u32'), 'duration': 'u32', 'extension_period': 'u32', 'min_bid_step': 'u128'}, 'OpenAuction': {'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'starts_at': (None, 'u32'), 'whitelist': 'scale_info::83', 'bid_lock_duration': 'u32'}}}```

---------
### NftOwnerRemarked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### NftSellOrderMade
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `Balance` | ```u128```

---------
### NftSlingedBackToTheOriginalArtist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```

---------
### OfferAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```

---------
### OfferCanceled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```

---------
### OfferStarted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `VideoId` | ```u64```
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `MemberId` | ```u64```
| None | `Option<Balance>` | ```(None, 'u128')```

---------
### OpenAuctionBidAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```

---------
### OpenAuctionStarted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `OpenAuctionParams` | ```{'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'starts_at': (None, 'u32'), 'whitelist': 'scale_info::83', 'bid_lock_duration': 'u32'}```
| None | `OpenAuctionId` | ```u64```

---------
### ToggledNftLimits
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### VideoAssetsDeletedByModerator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `BTreeSet<DataObjectId>` | ```scale_info::83```
| None | `bool` | ```bool```
| None | `Vec<u8>` | ```Bytes```

---------
### VideoCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `ChannelId` | ```u64```
| None | `VideoId` | ```u64```
| None | `VideoCreationParameters` | ```{'assets': (None, {'object_creation_list': [{'size': 'u64', 'ipfs_content_id': 'Bytes'}], 'expected_data_size_fee': 'u128'}), 'meta': (None, 'Bytes'), 'auto_issue_nft': (None, {'royalty': (None, 'u32'), 'nft_metadata': 'Bytes', 'non_channel_owner': (None, 'u64'), 'init_transactional_status': {'Idle': None, 'BuyNow': 'u128', 'InitiatedOfferToMember': ('u64', (None, 'u128')), 'EnglishAuction': {'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'whitelist': 'scale_info::83', 'starts_at': (None, 'u32'), 'duration': 'u32', 'extension_period': 'u32', 'min_bid_step': 'u128'}, 'OpenAuction': {'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'starts_at': (None, 'u32'), 'whitelist': 'scale_info::83', 'bid_lock_duration': 'u32'}}}), 'expected_video_state_bloat_bond': 'u128', 'expected_data_object_state_bloat_bond': 'u128', 'storage_buckets_num_witness': 'u32'}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::83```

---------
### VideoDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```

---------
### VideoDeletedByModerator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### VideoStateBloatBondValueUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### VideoUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `VideoUpdateParameters` | ```{'assets_to_upload': (None, {'object_creation_list': [{'size': 'u64', 'ipfs_content_id': 'Bytes'}], 'expected_data_size_fee': 'u128'}), 'new_meta': (None, 'Bytes'), 'assets_to_remove': 'scale_info::83', 'auto_issue_nft': (None, {'royalty': (None, 'u32'), 'nft_metadata': 'Bytes', 'non_channel_owner': (None, 'u64'), 'init_transactional_status': {'Idle': None, 'BuyNow': 'u128', 'InitiatedOfferToMember': ('u64', (None, 'u128')), 'EnglishAuction': {'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'whitelist': 'scale_info::83', 'starts_at': (None, 'u32'), 'duration': 'u32', 'extension_period': 'u32', 'min_bid_step': 'u128'}, 'OpenAuction': {'starting_price': 'u128', 'buy_now_price': (None, 'u128'), 'starts_at': (None, 'u32'), 'whitelist': 'scale_info::83', 'bid_lock_duration': 'u32'}}}), 'expected_data_object_state_bloat_bond': 'u128', 'storage_buckets_num_witness': (None, 'u32')}```
| None | `BTreeSet<DataObjectId>` | ```scale_info::83```

---------
### VideoVisibilitySetByModerator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ContentActor` | ```{'Curator': ('u64', 'u64'), 'Member': 'u64', 'Lead': None}```
| None | `VideoId` | ```u64```
| None | `bool` | ```bool```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### AuctionStartsAtMaxDelta
 Max delta between current block and starts at

#### Python
```python
result = substrate.query(
    'Content', 'AuctionStartsAtMaxDelta', []
)
```

#### Return value
```python
'u32'
```
---------
### ChannelById

#### Python
```python
result = substrate.query(
    'Content', 'ChannelById', ['u64']
)
```

#### Return value
```python
{
    'channel_state_bloat_bond': {
        'amount': 'u128',
        'repayment_restricted_to': (None, 'AccountId'),
    },
    'collaborators': 'scale_info::106',
    'creator_token_id': (None, 'u64'),
    'cumulative_reward_claimed': 'u128',
    'daily_nft_counter': {'counter': 'u64', 'last_updated': 'u32'},
    'daily_nft_limit': {'block_number_period': 'u32', 'limit': 'u64'},
    'data_objects': 'scale_info::83',
    'num_videos': 'u64',
    'owner': {'CuratorGroup': 'u64', 'Member': 'u64'},
    'paused_features': 'scale_info::111',
    'privilege_level': 'u8',
    'transfer_status': {
        'NoActiveTransfer': None,
        'PendingTransfer': {
            'new_owner': {'CuratorGroup': 'u64', 'Member': 'u64'},
            'transfer_params': {
                'new_collaborators': 'scale_info::106',
                'price': 'u128',
                'transfer_id': 'u64',
            },
        },
    },
    'weekly_nft_counter': {'counter': 'u64', 'last_updated': 'u32'},
    'weekly_nft_limit': {'block_number_period': 'u32', 'limit': 'u64'},
}
```
---------
### ChannelCashoutsEnabled

#### Python
```python
result = substrate.query(
    'Content', 'ChannelCashoutsEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
### ChannelStateBloatBondValue
 The state bloat bond for the channel (helps preventing the state bloat).

#### Python
```python
result = substrate.query(
    'Content', 'ChannelStateBloatBondValue', []
)
```

#### Return value
```python
'u128'
```
---------
### Commitment

#### Python
```python
result = substrate.query(
    'Content', 'Commitment', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### CuratorGroupById

#### Python
```python
result = substrate.query(
    'Content', 'CuratorGroupById', ['u64']
)
```

#### Return value
```python
{
    'active': 'bool',
    'curators': 'scale_info::106',
    'permissions_by_level': 'scale_info::570',
}
```
---------
### GlobalDailyNftCounter
 Global daily NFT counter.

#### Python
```python
result = substrate.query(
    'Content', 'GlobalDailyNftCounter', []
)
```

#### Return value
```python
{'counter': 'u64', 'last_updated': 'u32'}
```
---------
### GlobalDailyNftLimit
 Global daily NFT limit.

#### Python
```python
result = substrate.query(
    'Content', 'GlobalDailyNftLimit', []
)
```

#### Return value
```python
{'block_number_period': 'u32', 'limit': 'u64'}
```
---------
### GlobalWeeklyNftCounter
 Global weekly NFT counter.

#### Python
```python
result = substrate.query(
    'Content', 'GlobalWeeklyNftCounter', []
)
```

#### Return value
```python
{'counter': 'u64', 'last_updated': 'u32'}
```
---------
### GlobalWeeklyNftLimit
 Global weekly NFT limit.

#### Python
```python
result = substrate.query(
    'Content', 'GlobalWeeklyNftLimit', []
)
```

#### Return value
```python
{'block_number_period': 'u32', 'limit': 'u64'}
```
---------
### MaxAuctionDuration
 Max auction duration

#### Python
```python
result = substrate.query(
    'Content', 'MaxAuctionDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxAuctionExtensionPeriod
 Max auction extension period

#### Python
```python
result = substrate.query(
    'Content', 'MaxAuctionExtensionPeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxBidLockDuration
 Max bid lock duration

#### Python
```python
result = substrate.query(
    'Content', 'MaxBidLockDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxBidStep
 Max auction bid step

#### Python
```python
result = substrate.query(
    'Content', 'MaxBidStep', []
)
```

#### Return value
```python
'u128'
```
---------
### MaxCashoutAllowed

#### Python
```python
result = substrate.query(
    'Content', 'MaxCashoutAllowed', []
)
```

#### Return value
```python
'u128'
```
---------
### MaxCreatorRoyalty
 Max creator royalty percentage

#### Python
```python
result = substrate.query(
    'Content', 'MaxCreatorRoyalty', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxStartingPrice
 Max auction staring price

#### Python
```python
result = substrate.query(
    'Content', 'MaxStartingPrice', []
)
```

#### Return value
```python
'u128'
```
---------
### MinAuctionDuration
 Min auction duration

#### Python
```python
result = substrate.query(
    'Content', 'MinAuctionDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### MinAuctionExtensionPeriod
 Min auction extension period

#### Python
```python
result = substrate.query(
    'Content', 'MinAuctionExtensionPeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### MinBidLockDuration
 Min bid lock duration

#### Python
```python
result = substrate.query(
    'Content', 'MinBidLockDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### MinBidStep
 Min auction bid step

#### Python
```python
result = substrate.query(
    'Content', 'MinBidStep', []
)
```

#### Return value
```python
'u128'
```
---------
### MinCashoutAllowed

#### Python
```python
result = substrate.query(
    'Content', 'MinCashoutAllowed', []
)
```

#### Return value
```python
'u128'
```
---------
### MinCreatorRoyalty
 Min creator royalty percentage

#### Python
```python
result = substrate.query(
    'Content', 'MinCreatorRoyalty', []
)
```

#### Return value
```python
'u32'
```
---------
### MinStartingPrice
 Min auction staring price

#### Python
```python
result = substrate.query(
    'Content', 'MinStartingPrice', []
)
```

#### Return value
```python
'u128'
```
---------
### NextChannelId

#### Python
```python
result = substrate.query(
    'Content', 'NextChannelId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextCuratorGroupId

#### Python
```python
result = substrate.query(
    'Content', 'NextCuratorGroupId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextTransferId

#### Python
```python
result = substrate.query(
    'Content', 'NextTransferId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextVideoId

#### Python
```python
result = substrate.query(
    'Content', 'NextVideoId', []
)
```

#### Return value
```python
'u64'
```
---------
### NftLimitsEnabled
 NFT limits enabled or not
 Can be updated in flight by the Council

#### Python
```python
result = substrate.query(
    'Content', 'NftLimitsEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
### OpenAuctionBidByVideoAndMember
 Bids for open auctions

#### Python
```python
result = substrate.query(
    'Content', 'OpenAuctionBidByVideoAndMember', ['u64', 'u64']
)
```

#### Return value
```python
{'amount': 'u128', 'auction_id': 'u64', 'made_at_block': 'u32'}
```
---------
### PlatfromFeePercentage
 Platform fee percentage

#### Python
```python
result = substrate.query(
    'Content', 'PlatfromFeePercentage', []
)
```

#### Return value
```python
'u32'
```
---------
### VideoById

#### Python
```python
result = substrate.query(
    'Content', 'VideoById', ['u64']
)
```

#### Return value
```python
{
    'data_objects': 'scale_info::83',
    'in_channel': 'u64',
    'nft_status': (
        None,
        {
            'creator_royalty': (None, 'u32'),
            'open_auctions_nonce': 'u64',
            'owner': {'ChannelOwner': None, 'Member': 'u64'},
            'transactional_status': {
                'BuyNow': 'u128',
                'EnglishAuction': {
                    'buy_now_price': (None, 'u128'),
                    'end': 'u32',
                    'extension_period': 'u32',
                    'min_bid_step': 'u128',
                    'start': 'u32',
                    'starting_price': 'u128',
                    'top_bid': (None, 'scale_info::561'),
                    'whitelist': 'scale_info::83',
                },
                'Idle': None,
                'InitiatedOfferToMember': ('u64', (None, 'u128')),
                'OpenAuction': {
                    'auction_id': 'u64',
                    'bid_lock_duration': 'u32',
                    'buy_now_price': (None, 'u128'),
                    'start': 'u32',
                    'starting_price': 'u128',
                    'whitelist': 'scale_info::83',
                },
            },
        },
    ),
    'video_state_bloat_bond': {
        'amount': 'u128',
        'repayment_restricted_to': (None, 'AccountId'),
    },
}
```
---------
### VideoStateBloatBondValue
The state bloat bond for the video (helps preventing the state bloat).

#### Python
```python
result = substrate.query(
    'Content', 'VideoStateBloatBondValue', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### DefaultChannelDailyNftLimit
 Exports const - default channel daily NFT limit.
#### Value
```python
{'block_number_period': 14400, 'limit': 100}
```
#### Python
```python
constant = substrate.get_constant('Content', 'DefaultChannelDailyNftLimit')
```
---------
### DefaultChannelWeeklyNftLimit
 Exports const - default channel weekly NFT limit.
#### Value
```python
{'block_number_period': 14400, 'limit': 100}
```
#### Python
```python
constant = substrate.get_constant('Content', 'DefaultChannelWeeklyNftLimit')
```
---------
### DefaultGlobalDailyNftLimit
 Exports const - default global daily NFT limit.
#### Value
```python
{'block_number_period': 14400, 'limit': 100}
```
#### Python
```python
constant = substrate.get_constant('Content', 'DefaultGlobalDailyNftLimit')
```
---------
### DefaultGlobalWeeklyNftLimit
 Exports const - default global weekly NFT limit.
#### Value
```python
{'block_number_period': 14400, 'limit': 100}
```
#### Python
```python
constant = substrate.get_constant('Content', 'DefaultGlobalWeeklyNftLimit')
```
---------
### MaxKeysPerCuratorGroupPermissionsByLevelMap
 Exports const - max number of keys per curator_group.permissions_by_level map instance
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('Content', 'MaxKeysPerCuratorGroupPermissionsByLevelMap')
```
---------
### MaxNftAuctionWhitelistLength
 Exports const - max nft auction whitelist length
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Content', 'MaxNftAuctionWhitelistLength')
```
---------
### MaxNumberOfCuratorsPerGroup
 Exports const - max number of curators per group
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Content', 'MaxNumberOfCuratorsPerGroup')
```
---------
## Errors

---------
### ActionHasBidsAlready
Already active auction cannot be cancelled

---------
### ActorCannotBeLead
Actor cannot authorize as lead for given extrinsic

---------
### ActorCannotOwnChannel
Actor cannot Own channel

---------
### ActorIsNotBidder
Actor is not a last bidder

---------
### ActorNotAMember
Actor is not A Member

---------
### ActorNotAuthorized
Operation cannot be perfomed with this Actor

---------
### AssetsToRemoveBeyondEntityAssetsSet
List of assets to remove provided for update_channel / update_video contains assets that don&\#x27;t belong to the specified entity

---------
### AuctionBidStepLowerBoundExceeded
Auction bid step lower bound exceeded

---------
### AuctionBidStepUpperBoundExceeded
Auction bid step upper bound exceeded

---------
### AuctionCannotBeCompleted
Auction cannot be completed

---------
### AuctionDidNotStart
Auction did not started

---------
### AuctionDurationLowerBoundExceeded
Auction duration lower bound exceeded

---------
### AuctionDurationUpperBoundExceeded
Auction duration upper bound exceeded

---------
### BadOrigin
Expected root or signed origin

---------
### BidDoesNotExist
Auction does not have bids

---------
### BidIsForPastAuction
Selected Bid is for past open auction

---------
### BidLockDurationIsNotExpired
Bid lock duration is not expired

---------
### BidLockDurationLowerBoundExceeded
Bid lock duration lower bound exceeded

---------
### BidLockDurationUpperBoundExceeded
Bid lock duration upper bound exceeded

---------
### BidStepConstraintViolated
Minimal auction bid step constraint violated.

---------
### BuyNowMustBeGreaterThanStartingPrice
Auction buy now is less then starting price

---------
### CannotWithdrawFromChannelWithCreatorTokenIssued
Cannot directly withdraw funds from a channel account when the channel has
a creator token issued

---------
### CashoutAmountBelowMinimumAmount
Channel cashout amount is too low to be claimed

---------
### CashoutAmountExceedsMaximumAmount
Channel cashout amount is too high to be claimed

---------
### CategoryDoesNotExist
A Channel or Video Category does not exist.

---------
### ChannelAgentInsufficientPermissions

---------
### ChannelBagMissing
Unexpected runtime state: missing channel bag during delete_channel attempt

---------
### ChannelCashoutsDisabled
Channel cashouts are currently disabled

---------
### ChannelContainsAssets
Channel Contains Assets

---------
### ChannelContainsVideos
Channel Contains Video

---------
### ChannelDoesNotExist
Channel does not exist

---------
### ChannelFeaturePaused
Operation cannot be executed, because this channel feature has been paused by a curator

---------
### ChannelNftDailyLimitExceeded

---------
### ChannelNftWeeklyLimitExceeded

---------
### ChannelOwnerCuratorGroupDoesNotExist
Provided channel owner (curator group) does not exist

---------
### ChannelOwnerMemberDoesNotExist
Provided channel owner (member) does not exist

---------
### ChannelStateBloatBondBelowExistentialDeposit
Channel state bloat bond cannot be lower than existential deposit,
because it must secure the channel module account against dusting

---------
### ChannelStateBloatBondChanged
Invalid extrinsic call: Channel state bloat bond changed.

---------
### ChannelTransfersBlockedDuringRevenueSplits
Channel Transfers are blocked during revenue splits

---------
### ChannelTransfersBlockedDuringTokenSales
Channel Transfers are blocked during token sales

---------
### CreatorTokenAlreadyIssued
Creator token was already issued for this channel

---------
### CreatorTokenNotIssued
Creator token wasn&\#x27;t issued for this channel

---------
### CuratorAuthFailed
Curator authentication failed

---------
### CuratorGroupDoesNotExist
Given curator group does not exist

---------
### CuratorGroupIsNotActive
Curator group is not active

---------
### CuratorGroupMaxPermissionsByLevelMapSizeExceeded
Curator group&\#x27;s permissions by level map exceeded the maximum allowed size

---------
### CuratorIdInvalid
Curator id is not a worker id in content working group

---------
### CuratorIsAlreadyAMemberOfGivenCuratorGroup
Curator under provided curator id is already a member of curaror group under given id

---------
### CuratorIsNotAMemberOfGivenCuratorGroup
Curator under provided curator id is not a member of curaror group under given id

---------
### CuratorModerationActionNotAllowed
Curator does not have permissions to perform given moderation action

---------
### CuratorsPerGroupLimitReached
Max number of curators per group limit reached

---------
### DoesNotOwnNft
Given origin does not own nft

---------
### ExtensionPeriodIsGreaterThenAuctionDuration
Extension period is greater then auction duration

---------
### ExtensionPeriodLowerBoundExceeded
Auction extension period lower bound exceeded

---------
### ExtensionPeriodUpperBoundExceeded
Auction extension period upper bound exceeded

---------
### GlobalNftDailyLimitExceeded

---------
### GlobalNftWeeklyLimitExceeded

---------
### InsufficientBalance
Insufficient balance

---------
### InsufficientBalanceForChannelCreation
Cannot create the channel: channel creator has insufficient balance
(budget for channel state bloat bond + channel data objs state bloat bonds + data objs storage fees + existential deposit)

---------
### InsufficientBalanceForTransfer
Cannot transfer the channel: channel owner has insufficient balance (budget for WGs)

---------
### InsufficientBalanceForVideoCreation
Cannot create the video: video creator has insufficient balance
(budget for video state bloat bond + video data objs state bloat bonds + data objs storage fees + existential deposit)

---------
### InsufficientCouncilBudget

---------
### InsufficientTreasuryBalance
Insufficient treasury balance

---------
### InvalidAssetsProvided
Channel assets feasibility

---------
### InvalidBagSizeSpecified
Bag Size specified is not valid

---------
### InvalidBidAmountSpecified
Commit verification for bid amount

---------
### InvalidBuyNowWitnessPriceProvided
`witness_price` provided to `buy_now` extrinsic does not match the current sell price

---------
### InvalidChannelBagWitnessProvided
Channel bag witness parameters don&\#x27;t match the current runtime state

---------
### InvalidChannelOwner
Incorrect channel owner for an operation.

---------
### InvalidChannelTransferAcceptor
Incorrect actor tries to accept the channel transfer.

---------
### InvalidChannelTransferCommitmentParams
Cannot accept the channel transfer: provided commitment parameters doesn&\#x27;t match with
channel pending transfer parameters.

---------
### InvalidChannelTransferStatus
Invalid channel transfer status for operations.

---------
### InvalidMemberProvided
Invalid member id  specified

---------
### InvalidNftOfferWitnessPriceProvided
Current nft offer price does not match the provided `witness_price`

---------
### InvalidStorageBucketsNumWitnessProvided
Storage buckets number witness parameter does not match the current runtime state

---------
### InvalidVideoDataObjectsCountProvided
Invalid number of objects to delete provided for delete_video

---------
### IsNotEnglishAuctionType
Auction type is not `English`

---------
### IsNotOpenAuctionType
Auction type is not `Open`

---------
### LeadAuthFailed
Lead authentication failed

---------
### MaxAuctionWhiteListLengthUpperBoundExceeded
Max auction whitelist length upper bound exceeded

---------
### MaxCashoutValueTooHigh
Attempt to set minimum cashout allowed above the limit

---------
### MaxCuratorPermissionsPerLevelExceeded
Maximum number of curator permissions per given channel privilege level exceeded

---------
### MaxNumberOfChannelAgentPermissionsExceeded
Maximum number of channel agent permissions for channel agent exceeded

---------
### MaxNumberOfChannelAssetsExceeded
Number of channel assets exceeds MaxNumberOfAssetsPerChannel

---------
### MaxNumberOfChannelCollaboratorsExceeded
Number of channel collaborators exceeds MaxNumberOfCollaboratorsPerChannel

---------
### MaxNumberOfPausedFeaturesPerChannelExceeded
Maximum number of paused features per channel exceeded

---------
### MaxNumberOfVideoAssetsExceeded
Number of video assets exceeds MaxMaxNumberOfAssetsPerVideo

---------
### MemberAuthFailed
Member authentication failed

---------
### MemberIdCouldNotBeDerivedFromActor
Member id could not be derived from the provided ContentActor context

---------
### MemberIsNotAllowedToParticipate
Member is not allowed to participate in auction

---------
### MemberProfileNotFound
Member profile not found

---------
### MigrationNotFinished
Migration not done yet

---------
### MinCashoutAllowedExceedsMaxCashoutAllowed
New values for min_cashout_allowed/max_cashout_allowed are invalid
min_cashout_allowed cannot exceed max_cashout_allowed

---------
### MinCashoutValueTooLow
Attempt to set minimum cashout allowed below the limit

---------
### MissingStorageBucketsNumWitness
Storage buckets number witness parameter must be provided when channel/video assets
are being updated.

---------
### NftAlreadyExists
Nft for given video id already exists

---------
### NftAlreadyOwnedByChannel
Attempt to sling back a channel owned nft

---------
### NftAuctionIsAlreadyExpired
Nft auction is already expired

---------
### NftDoesNotExist
Nft for given video id does not exist

---------
### NftIsNotIdle
Can not create auction for Nft, if auction have been already started or nft is locked for the transfer

---------
### NftNonChannelOwnerDoesNotExist
Non-channel owner specified during nft issuance does not exist

---------
### NftNotInBuyNowState
Given video nft is not in buy now state

---------
### NoAssetsSpecified
No assets to be removed have been specified

---------
### NotInAuctionState
Nft is not in auction state

---------
### NumberOfAssetsToRemoveIsZero
Delete channel and assets and delete video assets must have a number of assets to remove greater than zero

---------
### OverflowOrUnderflowHappened
Overflow or underflow error happened

---------
### PatronageCanOnlyBeClaimedForMemberOwnedChannels
Patronage can only be claimed if channel is owned by a member

---------
### PaymentProofVerificationFailed
Payment Proof verification failed

---------
### PendingOfferDoesNotExist
No pending offers for given Nft

---------
### ReplyDoesNotExist
Partecipant is not a member

---------
### RewardAccountIsNotSet
Creator royalty requires reward account to be set.

---------
### RoyaltyLowerBoundExceeded
Royalty Lower Bound Exceeded

---------
### RoyaltyUpperBoundExceeded
Royalty Upper Bound Exceeded

---------
### StartingPriceConstraintViolated
Auction starting price constraint violated.

---------
### StartingPriceLowerBoundExceeded
Starting price lower bound exceeded

---------
### StartingPriceUpperBoundExceeded
Starting price upper bound exceeded

---------
### StartsAtLowerBoundExceeded
Auction starts at lower bound exceeded

---------
### StartsAtUpperBoundExceeded
Auction starts at upper bound exceeded

---------
### TargetMemberDoesNotExist
Nft offer target member does not exist

---------
### UnsufficientBalance
Insufficient balance

---------
### VideoDoesNotExist
Video does not exist

---------
### VideoInSeason
Vfdeo in season can`t be removed (because order is important)

---------
### VideoStateBloatBondChanged
Invalid extrinsic call: video state bloat bond changed.

---------
### WhitelistHasOnlyOneMember
Auction whitelist has only one member

---------
### WhitelistedMemberDoesNotExist
At least one of the whitelisted members does not exist

---------
### WithdrawFromChannelAmountIsZero
An attempt to withdraw funds from channel account failed, because the specified amount
is zero

---------
### WithdrawalAmountExceedsChannelAccountWithdrawableBalance
An attempt to withdraw funds from channel account failed, because the specified amount
exceeds the withdrawable amount (channel account balance minus channel bloat bond)

---------
### ZeroReward
Cannot claim zero reward.

---------