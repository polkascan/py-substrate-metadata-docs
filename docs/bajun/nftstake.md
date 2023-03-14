
# NftStake

---------
## Calls

---------
### fund_treasury
#### Attributes
| Name | Type |
| -------- | -------- | 
| fund_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NftStake', 'fund_treasury', {'fund_amount': 'u128'}
)
```

---------
### redeem_staking_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `ContractItemIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NftStake', 'redeem_staking_contract', {'contract_id': 'u128'}
)
```

---------
### set_locked_state
#### Attributes
| Name | Type |
| -------- | -------- | 
| locked_state | `PalletLockedState` | 

#### Python
```python
call = substrate.compose_call(
    'NftStake', 'set_locked_state', {
    'locked_state': (
        'Unlocked',
        'Locked',
    ),
}
)
```

---------
### set_organizer
#### Attributes
| Name | Type |
| -------- | -------- | 
| organizer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'NftStake', 'set_organizer', {'organizer': 'AccountId'}
)
```

---------
### submit_staking_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| staking_contract | `StakingContractOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NftStake', 'submit_staking_contract', {
    'staking_contract': {
        'contract_block_duration': 'u32',
        'contract_clauses': [
            {
                'HasAttribute': (
                    {
                        'Account': 'AccountId',
                        'CollectionOwner': None,
                        'ItemOwner': None,
                        'Pallet': None,
                    },
                    'u32',
                ),
                'HasAttributeWithValue': (
                    {
                        'Account': 'AccountId',
                        'CollectionOwner': None,
                        'ItemOwner': None,
                        'Pallet': None,
                    },
                    'u32',
                    'u64',
                ),
            },
        ],
        'staking_reward': {
            'Nft': ('u32', 'u128'),
            'Tokens': 'u128',
        },
    },
}
)
```

---------
### take_staking_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `ContractItemIdOf<T>` | 
| staked_assets | `StakedAssetsVecOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NftStake', 'take_staking_contract', {
    'contract_id': 'u128',
    'staked_assets': [('u32', 'u128')],
}
)
```

---------
## Events

---------
### LockedStateSet
The pallet&\#x27;s lock status has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| locked_state | `PalletLockedState` | ```('Unlocked', 'Locked')```

---------
### OrganizerSet
An organizer has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| organizer | `T::AccountId` | ```AccountId```

---------
### StakingContractCreated
A new staking contract has been successfully created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| creator | `AccountIdOf<T>` | ```AccountId```
| contract | `ContractItemIdOf<T>` | ```u128```

---------
### StakingContractRedeemed
A new staking contract has been successfully created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemed_by | `AccountIdOf<T>` | ```AccountId```
| contract | `ContractItemIdOf<T>` | ```u128```
| reward | `StakingRewardOf<T>` | ```{'Tokens': 'u128', 'Nft': ('u32', 'u128')}```

---------
### StakingContractTaken
A new staking contract has been successfully created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| taken_by | `AccountIdOf<T>` | ```AccountId```
| contract | `ContractItemIdOf<T>` | ```u128```

---------
### TreasuryFunded
The treasury has received additional funds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| funding_account | `AccountIdOf<T>` | ```AccountId```
| funds | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ActiveContracts

#### Python
```python
result = substrate.query(
    'NftStake', 'ActiveContracts', ['u128']
)
```

#### Return value
```python
{
    'contract_block_duration': 'u32',
    'contract_clauses': [
        {
            'HasAttribute': (
                {
                    'Account': 'AccountId',
                    'CollectionOwner': None,
                    'ItemOwner': None,
                    'Pallet': None,
                },
                'u32',
            ),
            'HasAttributeWithValue': (
                {
                    'Account': 'AccountId',
                    'CollectionOwner': None,
                    'ItemOwner': None,
                    'Pallet': None,
                },
                'u32',
                'u64',
            ),
        },
    ],
    'staking_reward': {'Nft': ('u32', 'u128'), 'Tokens': 'u128'},
}
```
---------
### ContractCollectionId

#### Python
```python
result = substrate.query(
    'NftStake', 'ContractCollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
### ContractDurations

#### Python
```python
result = substrate.query(
    'NftStake', 'ContractDurations', ['u128']
)
```

#### Return value
```python
'u32'
```
---------
### ContractOwners

#### Python
```python
result = substrate.query(
    'NftStake', 'ContractOwners', ['u128']
)
```

#### Return value
```python
'AccountId'
```
---------
### ContractStakedAssets

#### Python
```python
result = substrate.query(
    'NftStake', 'ContractStakedAssets', ['u128']
)
```

#### Return value
```python
[('u32', 'u128')]
```
---------
### LockedState

#### Python
```python
result = substrate.query(
    'NftStake', 'LockedState', []
)
```

#### Return value
```python
('Unlocked', 'Locked')
```
---------
### NextContractId

#### Python
```python
result = substrate.query(
    'NftStake', 'NextContractId', []
)
```

#### Return value
```python
'u128'
```
---------
### Organizer

#### Python
```python
result = substrate.query(
    'NftStake', 'Organizer', []
)
```

#### Return value
```python
'AccountId'
```
---------
### TreasuryAccount

#### Python
```python
result = substrate.query(
    'NftStake', 'TreasuryAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### ContractCollectionConfig
 The configuration for the contract Nft collection
#### Value
```python
{
    'max_supply': None,
    'mint_settings': {
        'default_item_settings': 0,
        'end_block': None,
        'mint_type': 'Issuer',
        'price': None,
        'start_block': None,
    },
    'settings': 0,
}
```
#### Python
```python
constant = substrate.get_constant('NftStake', 'ContractCollectionConfig')
```
---------
### ContractCollectionItemConfig
 The configuration for the contract Nft collection
#### Value
```python
{'settings': 0}
```
#### Python
```python
constant = substrate.get_constant('NftStake', 'ContractCollectionItemConfig')
```
---------
### MinimumStakingTokenReward
 The minimal amount of tokens that can be rewarded in a staking contract.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('NftStake', 'MinimumStakingTokenReward')
```
---------
### TreasuryPalletId
 The treasury&#x27;s pallet id, used for deriving its sovereign account identifier.
#### Value
```python
'0x616a2f6e66747374'
```
#### Python
```python
constant = substrate.get_constant('NftStake', 'TreasuryPalletId')
```
---------
## Errors

---------
### AccountLacksFunds
Account doesn&\#x27;t have enough the minimum amount of funds necessary to contribute.

---------
### ContractAlreadyTaken
The contract has been already taken by the account

---------
### ContractConditionsNotFulfilled
The account that tried to take a staking contract failed to fulfill its conditions.

---------
### ContractNotFound
The contract to be redeemed cannot be found

---------
### ContractNotOwned
The account that tried to redeemed a contract didn&\#x27;t own it

---------
### ContractRewardNotOwned
The account that tried to create a contract didn&\#x27;t actually own it&\#x27;s reward.

---------
### ContractStillActive
The contract is still active, so it cannot be redeemed

---------
### ContractTakenByOther
The contract has been already taken by another account

---------
### InvalidContractReward
The contract reward is not valid. Either an invalid Nft or not enough tokens.

---------
### OrganizerNotSet
There is no account set as the organizer

---------
### PalletLocked
The pallet is currently locked and cannot be interacted with.

---------
### StakedAssetNotOwned
The account that tried to take a staking contract didn&\#x27;t own one or more of the
staked assets.

---------
### TreasuryLacksFunds
The treasury doesn&\#x27;t have enough funds to pay the contract rewards.

---------