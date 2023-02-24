
# ZenlinkProtocol

---------
## Calls

---------
### add_liquidity
Provide liquidity to a pair.

The order of foreign dot effect result.

\# Arguments

- `asset_0`: Asset which make up pair
- `asset_1`: Asset which make up pair
- `amount_0_desired`: Maximum amount of asset_0 added to the pair
- `amount_1_desired`: Maximum amount of asset_1 added to the pair
- `amount_0_min`: Minimum amount of asset_0 added to the pair
- `amount_1_min`: Minimum amount of asset_1 added to the pair
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| amount_0_desired | `AssetBalance` | 
| amount_1_desired | `AssetBalance` | 
| amount_0_min | `AssetBalance` | 
| amount_1_min | `AssetBalance` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'add_liquidity', {
    'amount_0_desired': 'u128',
    'amount_0_min': 'u128',
    'amount_1_desired': 'u128',
    'amount_1_min': 'u128',
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'deadline': 'u32',
}
)
```

---------
### bootstrap_charge_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| charge_rewards | `Vec<(T::AssetId, AssetBalance)>` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_charge_reward', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'charge_rewards': [
        (
            {
                'asset_index': 'u64',
                'asset_type': 'u8',
                'chain_id': 'u32',
            },
            'u128',
        ),
    ],
}
)
```

---------
### bootstrap_claim
Claim lp asset from a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_claim', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'deadline': 'u32',
    'recipient': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### bootstrap_contribute
Contribute some asset to a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `amount_0_contribute`: The amount of asset_0 contribute to this bootstrap pair
- `amount_1_contribute`: The amount of asset_1 contribute to this bootstrap pair
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| amount_0_contribute | `AssetBalance` | 
| amount_1_contribute | `AssetBalance` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_contribute', {
    'amount_0_contribute': 'u128',
    'amount_1_contribute': 'u128',
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'deadline': 'u32',
}
)
```

---------
### bootstrap_create
Create bootstrap pair

The order of asset don&\#x27;t affect result.

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `target_supply_0`: Target amount of asset_0 total contribute
- `target_supply_0`: Target amount of asset_1 total contribute
- `capacity_supply_0`: The max amount of asset_0 total contribute
- `capacity_supply_1`: The max amount of asset_1 total contribute
- `end`: The earliest ending block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| target_supply_0 | `AssetBalance` | 
| target_supply_1 | `AssetBalance` | 
| capacity_supply_0 | `AssetBalance` | 
| capacity_supply_1 | `AssetBalance` | 
| end | `T::BlockNumber` | 
| rewards | `Vec<T::AssetId>` | 
| limits | `Vec<(T::AssetId, AssetBalance)>` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_create', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'capacity_supply_0': 'u128',
    'capacity_supply_1': 'u128',
    'end': 'u32',
    'limits': [
        (
            {
                'asset_index': 'u64',
                'asset_type': 'u8',
                'chain_id': 'u32',
            },
            'u128',
        ),
    ],
    'rewards': [
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ],
    'target_supply_0': 'u128',
    'target_supply_1': 'u128',
}
)
```

---------
### bootstrap_end
End a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_end', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
}
)
```

---------
### bootstrap_refund
Contributor refund from disable bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_refund', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
}
)
```

---------
### bootstrap_update
update a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `min_contribution_0`: The new min amount of asset_0 contribute
- `min_contribution_0`: The new min amount of asset_1 contribute
- `target_supply_0`: The new target amount of asset_0 total contribute
- `target_supply_0`: The new target amount of asset_1 total contribute
- `capacity_supply_0`: The new max amount of asset_0 total contribute
- `capacity_supply_1`: The new max amount of asset_1 total contribute
- `end`: The earliest ending block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| target_supply_0 | `AssetBalance` | 
| target_supply_1 | `AssetBalance` | 
| capacity_supply_0 | `AssetBalance` | 
| capacity_supply_1 | `AssetBalance` | 
| end | `T::BlockNumber` | 
| rewards | `Vec<T::AssetId>` | 
| limits | `Vec<(T::AssetId, AssetBalance)>` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_update', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'capacity_supply_0': 'u128',
    'capacity_supply_1': 'u128',
    'end': 'u32',
    'limits': [
        (
            {
                'asset_index': 'u64',
                'asset_type': 'u8',
                'chain_id': 'u32',
            },
            'u128',
        ),
    ],
    'rewards': [
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ],
    'target_supply_0': 'u128',
    'target_supply_1': 'u128',
}
)
```

---------
### bootstrap_withdraw_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'bootstrap_withdraw_reward', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'recipient': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### create_pair
Create pair by two assets.

The order of foreign dot effect result.

\# Arguments

- `asset_0`: Asset which make up Pair
- `asset_1`: Asset which make up Pair
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'create_pair', {
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
}
)
```

---------
### remove_liquidity
Extract liquidity.

The order of foreign dot effect result.

\# Arguments

- `asset_0`: Asset which make up pair
- `asset_1`: Asset which make up pair
- `amount_asset_0_min`: Minimum amount of asset_0 to exact
- `amount_asset_1_min`: Minimum amount of asset_1 to exact
- `recipient`: Account that accepts withdrawal of assets
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| liquidity | `AssetBalance` | 
| amount_0_min | `AssetBalance` | 
| amount_1_min | `AssetBalance` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'remove_liquidity', {
    'amount_0_min': 'u128',
    'amount_1_min': 'u128',
    'asset_0': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'asset_1': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'deadline': 'u32',
    'liquidity': 'u128',
    'recipient': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_fee_point
Set the protocol fee point.

\# Arguments

- `fee_point`:
The fee_point which integer between [0,30]
0 means no protocol fee.
30 means 0.3% * 100% = 0.0030.
default is 5 and means 0.3% * 1 / 6 = 0.0005.
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee_point | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'set_fee_point', {'fee_point': 'u8'}
)
```

---------
### set_fee_receiver
Set the new receiver of the protocol fee.

\# Arguments

- `send_to`:
(1) Some(receiver): it turn on the protocol fee and the new receiver account.
(2) None: it turn off the protocol fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| send_to | `Option<<T::Lookup as StaticLookup>::Source>` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'set_fee_receiver', {
    'send_to': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': 'u32',
            'Raw': 'Bytes',
        },
    ),
}
)
```

---------
### swap_assets_for_exact_assets
Buy amount of foreign by path.

\# Arguments

- `amount_out`: Amount of the foreign will be bought
- `amount_in_max`: Maximum amount of sold foreign
- `path`: path can convert to pairs.
- `recipient`: Account that receive the target foreign
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_out | `AssetBalance` | 
| amount_in_max | `AssetBalance` | 
| path | `Vec<T::AssetId>` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'swap_assets_for_exact_assets', {
    'amount_in_max': 'u128',
    'amount_out': 'u128',
    'deadline': 'u32',
    'path': [
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ],
    'recipient': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### swap_exact_assets_for_assets
Sell amount of foreign by path.

\# Arguments

- `amount_in`: Amount of the foreign will be sold
- `amount_out_min`: Minimum amount of target foreign
- `path`: path can convert to pairs.
- `recipient`: Account that receive the target foreign
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_in | `AssetBalance` | 
| amount_out_min | `AssetBalance` | 
| path | `Vec<T::AssetId>` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'swap_exact_assets_for_assets', {
    'amount_in': 'u128',
    'amount_out_min': 'u128',
    'deadline': 'u32',
    'path': [
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ],
    'recipient': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### transfer
Move some assets from one holder to another.

\# Arguments

- `asset_id`: The foreign id.
- `target`: The receiver of the foreign.
- `amount`: The amount of the foreign to transfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| amount | `AssetBalance` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'transfer', {
    'amount': 'u128',
    'asset_id': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'recipient': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### transfer_to_parachain
Transfer zenlink assets to a sibling parachain.

Zenlink assets can be either native or foreign to the sending parachain.

\# Arguments

- `asset_id`: Global identifier for a zenlink foreign
- `para_id`: Destination parachain
- `account`: Destination account
- `amount`: Amount to transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| para_id | `ParaId` | 
| recipient | `T::AccountId` | 
| amount | `AssetBalance` | 
| max_weight | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkProtocol', 'transfer_to_parachain', {
    'amount': 'u128',
    'asset_id': {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
    'max_weight': 'u64',
    'para_id': 'u32',
    'recipient': 'AccountId',
}
)
```

---------
## Events

---------
### AssetSwap
Transact in trading \[owner, recipient, swap_path, balances\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Vec<T::AssetId>` | ```[{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}]```
| None | `Vec<AssetBalance>` | ```['u128']```

---------
### BootstrapClaim
Claim a bootstrap pair. \[bootstrap_pair_account, claimer, receiver, asset_0, asset_1,
asset_0_refund, asset_1_refund, lp_amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### BootstrapContribute
Contribute to bootstrap pair. \[who, asset_0, asset_0_contribute, asset_1_contribute\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```

---------
### BootstrapCreated
Create a bootstrap pair. \[bootstrap_pair_account, asset_0, asset_1,
total_supply_0,total_supply_1, capacity_supply_0,capacity_supply_1, end\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `T::BlockNumber` | ```u32```

---------
### BootstrapEnd
A bootstrap pair end. \[asset_0, asset_1, asset_0_amount, asset_1_amount,
total_lp_supply]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### BootstrapRefund
Refund from disable bootstrap pair. \[bootstrap_pair_account, caller, asset_0, asset_1,
asset_0_refund, asset_1_refund\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### BootstrapUpdate
Update a bootstrap pair. \[caller, asset_0, asset_1,
total_supply_0,total_supply_1, capacity_supply_0,capacity_supply_1\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `T::BlockNumber` | ```u32```

---------
### Burned
Some assets were burned. \[asset_id, owner, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `AssetBalance` | ```u128```

---------
### ChargeReward
Charge reward into a bootstrap.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `Vec<(T::AssetId, AssetBalance)>` | ```[({'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}, 'u128')]```

---------
### DistributeReward
Bootstrap distribute some rewards to contributors.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `Vec<(T::AssetId, AssetBalance)>` | ```[({'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}, 'u128')]```

---------
### LiquidityAdded
Add liquidity. \[owner, asset_0, asset_1, add_balance_0, add_balance_1,
mint_balance_lp\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### LiquidityRemoved
Remove liquidity. \[owner, recipient, asset_0, asset_1, rm_balance_0, rm_balance_1,
burn_balance_lp\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### Minted
Some assets were minted. \[asset_id, owner, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `AssetBalance` | ```u128```

---------
### PairCreated
Swap
Create a trading pair. \[asset_0, asset_1\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```

---------
### Transferred
Foreign Asset
Some assets were transferred. \[asset_id, owner, target, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `AssetBalance` | ```u128```

---------
### TransferredToParachain
Transfer by xcm
Transferred to parachain. \[asset_id, src, para_id, dest, amount, used_weight\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `AssetBalance` | ```u128```
| None | `u64` | ```u64```

---------
### WithdrawReward
Withdraw all reward from a bootstrap.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AssetId` | ```{'chain_id': 'u32', 'asset_type': 'u8', 'asset_index': 'u64'}```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### BootstrapEndStatus
 End status of bootstrap

 BootstrapEndStatus: map bootstrap pair =&gt; pairStatus

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'BootstrapEndStatus', [
    (
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ),
]
)
```

#### Return value
```python
{
    'Bootstrap': {
        'accumulated_supply': ('u128', 'u128'),
        'capacity_supply': ('u128', 'u128'),
        'end_block_number': 'u32',
        'pair_account': 'AccountId',
        'target_supply': ('u128', 'u128'),
    },
    'Disable': None,
    'Trading': {'pair_account': 'AccountId', 'total_supply': 'u128'},
}
```
---------
### BootstrapLimits

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'BootstrapLimits', [
    (
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ),
]
)
```

#### Return value
```python
'scale_info::617'
```
---------
### BootstrapPersonalSupply

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'BootstrapPersonalSupply', [
    (
        (
            {
                'asset_index': 'u64',
                'asset_type': 'u8',
                'chain_id': 'u32',
            },
            {
                'asset_index': 'u64',
                'asset_type': 'u8',
                'chain_id': 'u32',
            },
        ),
        'AccountId',
    ),
]
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### BootstrapRewards

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'BootstrapRewards', [
    (
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ),
]
)
```

#### Return value
```python
'scale_info::617'
```
---------
### FeeMeta
 (Option&lt;fee_receiver&gt;, fee_point)

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'FeeMeta', []
)
```

#### Return value
```python
((None, 'AccountId'), 'u8')
```
---------
### ForeignLedger
 Foreign foreign storage
 The number of units of assets held by any given account.

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'ForeignLedger', [
    (
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
        'AccountId',
    ),
]
)
```

#### Return value
```python
'u128'
```
---------
### ForeignList

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'ForeignList', []
)
```

#### Return value
```python
[{'asset_index': 'u64', 'asset_type': 'u8', 'chain_id': 'u32'}]
```
---------
### ForeignMeta
 TWOX-NOTE: `AssetId` is trusted, so this is safe.

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'ForeignMeta', [
    {
        'asset_index': 'u64',
        'asset_type': 'u8',
        'chain_id': 'u32',
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### KLast
 Refer: https://github.com/Uniswap/uniswap-v2-core/blob/master/contracts/UniswapV2Pair.sol\#L88
 Last unliquidated protocol fee;

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'KLast', [
    (
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ),
]
)
```

#### Return value
```python
'[u64; 4]'
```
---------
### LiquidityPairs

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'LiquidityPairs', [
    (
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ),
]
)
```

#### Return value
```python
(None, {'asset_index': 'u64', 'asset_type': 'u8', 'chain_id': 'u32'})
```
---------
### PairStatuses
 (T::AssetId, T::AssetId) -&gt; PairStatus

#### Python
```python
result = substrate.query(
    'ZenlinkProtocol', 'PairStatuses', [
    (
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
        {
            'asset_index': 'u64',
            'asset_type': 'u8',
            'chain_id': 'u32',
        },
    ),
]
)
```

#### Return value
```python
{
    'Bootstrap': {
        'accumulated_supply': ('u128', 'u128'),
        'capacity_supply': ('u128', 'u128'),
        'end_block_number': 'u32',
        'pair_account': 'AccountId',
        'target_supply': ('u128', 'u128'),
    },
    'Disable': None,
    'Trading': {'pair_account': 'AccountId', 'total_supply': 'u128'},
}
```
---------
## Constants

---------
### PalletId
 This pallet id.
#### Value
```python
'0x2f7a656e6c696e6b'
```
#### Python
```python
constant = substrate.get_constant('ZenlinkProtocol', 'PalletId')
```
---------
## Errors

---------
### AccountIdBadLocation
Location given was invalid or unsupported.

---------
### AssetNotExists
Asset does not exist.

---------
### ChargeRewardParamsError
Charge bootstrap extrinsic args has error,

---------
### Deadline
Transaction block number is larger than the end block number.

---------
### DeniedCreatePair
Trading pair can&\#x27;t be created.

---------
### DeniedTransferToSelf
Transfer to self by XCM message.

---------
### DenyRefund
Bootstrap deny refund

---------
### DisableBootstrap
Bootstrap is disable

---------
### ExcessiveSoldAmount
Sold amount is more than exception.

---------
### ExecutionFailed
XCM execution failed.

---------
### ExistRewardsInBootstrap
Exist some reward in bootstrap,

---------
### IncorrectAssetAmountRange
Incorrect foreign amount range.

---------
### InsufficientAssetBalance
Account balance must be greater than or equal to the transfer amount.

---------
### InsufficientLiquidity
Liquidity is not enough.

---------
### InsufficientPairReserve
Trading pair does have enough foreign.

---------
### InsufficientTargetAmount
Get target amount is less than exception.

---------
### InvalidContributionAmount
Amount of contribution is invalid.

---------
### InvalidFeePoint
Invalid fee_point

---------
### InvalidPath
Can&\#x27;t find pair though trading path.

---------
### InvariantCheckFailed
Can&\#x27;t pass the K value check

---------
### NativeBalanceTooLow
Account native currency balance must be greater than ExistentialDeposit.

---------
### NoRewardTokens
Reward of bootstrap is not set.

---------
### NotInBootstrap
Pair is not in bootstrap

---------
### NotQualifiedAccount
Not eligible to contribute

---------
### Overflow
Overflow.

---------
### PairAlreadyExists
Trading pair already exists.

---------
### PairCreateForbidden
Created pair can&\#x27;t create now

---------
### PairNotExists
Trading pair does not exist.

---------
### RequireProtocolAdmin
Require the admin who can reset the admin and receiver of the protocol fee.

---------
### RequireProtocolAdminCandidate
Require the admin candidate who can become new admin after confirm.

---------
### TargetChainNotRegistered
Not in ZenlinkRegistedParaChains.

---------
### UnqualifiedBootstrap
Amount of contribution is invalid.

---------
### UnsupportedAssetType
Unsupported AssetId by this ZenlinkProtocol Version.

---------
### ZeroContribute
Zero contribute in bootstrap

---------