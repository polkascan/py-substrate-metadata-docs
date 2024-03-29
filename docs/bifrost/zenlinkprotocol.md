
# ZenlinkProtocol

---------
## Calls

---------
### add_liquidity
See [`Pallet::add_liquidity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| amount_0_desired | `AssetBalance` | 
| amount_1_desired | `AssetBalance` | 
| amount_0_min | `AssetBalance` | 
| amount_1_min | `AssetBalance` | 
| deadline | `BlockNumberFor<T>` | 

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
See [`Pallet::bootstrap_charge_reward`].
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
See [`Pallet::bootstrap_claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| deadline | `BlockNumberFor<T>` | 

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
See [`Pallet::bootstrap_contribute`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| amount_0_contribute | `AssetBalance` | 
| amount_1_contribute | `AssetBalance` | 
| deadline | `BlockNumberFor<T>` | 

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
See [`Pallet::bootstrap_create`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| target_supply_0 | `AssetBalance` | 
| target_supply_1 | `AssetBalance` | 
| capacity_supply_0 | `AssetBalance` | 
| capacity_supply_1 | `AssetBalance` | 
| end | `BlockNumberFor<T>` | 
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
See [`Pallet::bootstrap_end`].
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
See [`Pallet::bootstrap_refund`].
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
See [`Pallet::bootstrap_update`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| target_supply_0 | `AssetBalance` | 
| target_supply_1 | `AssetBalance` | 
| capacity_supply_0 | `AssetBalance` | 
| capacity_supply_1 | `AssetBalance` | 
| end | `BlockNumberFor<T>` | 
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
See [`Pallet::bootstrap_withdraw_reward`].
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
See [`Pallet::create_pair`].
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
See [`Pallet::remove_liquidity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| liquidity | `AssetBalance` | 
| amount_0_min | `AssetBalance` | 
| amount_1_min | `AssetBalance` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `BlockNumberFor<T>` | 

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
See [`Pallet::set_fee_point`].
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
See [`Pallet::set_fee_receiver`].
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
See [`Pallet::swap_assets_for_exact_assets`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_out | `AssetBalance` | 
| amount_in_max | `AssetBalance` | 
| path | `Vec<T::AssetId>` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `BlockNumberFor<T>` | 

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
See [`Pallet::swap_exact_assets_for_assets`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_in | `AssetBalance` | 
| amount_out_min | `AssetBalance` | 
| path | `Vec<T::AssetId>` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `BlockNumberFor<T>` | 

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
See [`Pallet::transfer`].
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
| None | `BlockNumberFor<T>` | ```u32```

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
| None | `BlockNumberFor<T>` | ```u32```

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
'scale_info::747'
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
'scale_info::747'
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
'scale_info::739'
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