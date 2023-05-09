
# DarwiniaFeeMarket

---------
## Calls

---------
### cancel_enrollment
Cancel enrolled relayer(Update market needed)
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DarwiniaFeeMarket', 'cancel_enrollment', {}
)
```

---------
### decrease_locked_collateral
Decrease relayer&\#x27;s locked collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_collateral | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaFeeMarket', 'decrease_locked_collateral', {'new_collateral': 'u128'}
)
```

---------
### enroll_and_lock_collateral
Any accounts can enroll to be a relayer by lock collateral. The relay fee is optional,
the default value is MinimumRelayFee in runtime. (Update market needed)
Note: One account can enroll only once.
#### Attributes
| Name | Type |
| -------- | -------- | 
| lock_collateral | `BalanceOf<T, I>` | 
| relay_fee | `Option<BalanceOf<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaFeeMarket', 'enroll_and_lock_collateral', {
    'lock_collateral': 'u128',
    'relay_fee': (None, 'u128'),
}
)
```

---------
### increase_locked_collateral
Increase relayer&\#x27;s locked collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_collateral | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaFeeMarket', 'increase_locked_collateral', {'new_collateral': 'u128'}
)
```

---------
### set_assigned_relayers_number
#### Attributes
| Name | Type |
| -------- | -------- | 
| number | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaFeeMarket', 'set_assigned_relayers_number', {'number': 'u32'}
)
```

---------
### set_slash_protect
#### Attributes
| Name | Type |
| -------- | -------- | 
| slash_protect | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaFeeMarket', 'set_slash_protect', {'slash_protect': 'u128'}
)
```

---------
### update_relay_fee
Update relay fee for enrolled relayer. (Update market needed)
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_fee | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaFeeMarket', 'update_relay_fee', {'new_fee': 'u128'}
)
```

---------
## Events

---------
### CancelEnrollment
Relayer cancel enrollment. \[account_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```

---------
### Enroll
Relayer enrollment. \[account_id, locked_collateral, relay_fee\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```

---------
### FeeMarketSlash
Slash report
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SlashReport<T::AccountId, T::BlockNumber, BalanceOf<T, I>>` | ```{'lane': '[u8; 4]', 'message': 'u64', 'sent_time': 'u32', 'confirm_time': (None, 'u32'), 'delay_time': (None, 'u32'), 'account_id': '[u8; 20]', 'amount': 'u128'}```

---------
### OrderCreated
Create new order. \[lane_id, message_nonce, order_fee, assigned_relayers,
out_of_slots_time\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LaneId` | ```[u8; 4]```
| None | `MessageNonce` | ```u64```
| None | `BalanceOf<T, I>` | ```u128```
| None | `Vec<T::AccountId>` | ```['[u8; 20]']```
| None | `Option<T::BlockNumber>` | ```(None, 'u32')```

---------
### OrderReward
Reward distribute of the order. \[lane_id, message_nonce, rewards\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LaneId` | ```[u8; 4]```
| None | `MessageNonce` | ```u64```
| None | `RewardItem<T::AccountId, BalanceOf<T, I>>` | ```{'to_assigned_relayers': 'scale_info::172', 'to_treasury': (None, 'u128'), 'to_message_relayer': (None, ('[u8; 20]', 'u128')), 'to_confirm_relayer': (None, ('[u8; 20]', 'u128'))}```

---------
### UpdateAssignedRelayersNumber
Update market assigned relayers numbers. \[new_assigned_relayers_number\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### UpdateCollateralSlashProtect
Update collateral slash protect value. \[slash_protect_value\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T, I>` | ```u128```

---------
### UpdateLockedCollateral
Update relayer locked collateral. \[account_id, new_collateral\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```
| None | `BalanceOf<T, I>` | ```u128```

---------
### UpdateRelayFee
Update relayer fee. \[account_id, new_fee\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```
| None | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### AssignedRelayers

#### Python
```python
result = substrate.query(
    'DarwiniaFeeMarket', 'AssignedRelayers', []
)
```

#### Return value
```python
[{'collateral': 'u128', 'fee': 'u128', 'id': '[u8; 20]'}]
```
---------
### AssignedRelayersNumber

#### Python
```python
result = substrate.query(
    'DarwiniaFeeMarket', 'AssignedRelayersNumber', []
)
```

#### Return value
```python
'u32'
```
---------
### CollateralSlashProtect

#### Python
```python
result = substrate.query(
    'DarwiniaFeeMarket', 'CollateralSlashProtect', []
)
```

#### Return value
```python
'u128'
```
---------
### Orders

#### Python
```python
result = substrate.query(
    'DarwiniaFeeMarket', 'Orders', [('[u8; 4]', 'u64')]
)
```

#### Return value
```python
{
    'assigned_relayers': [
        {
            'fee': 'u128',
            'id': '[u8; 20]',
            'valid_range': {'end': 'u32', 'start': 'u32'},
        },
    ],
    'collateral_per_assigned_relayer': 'u128',
    'confirm_time': (None, 'u32'),
    'lane': '[u8; 4]',
    'message': 'u64',
    'sent_time': 'u32',
}
```
---------
### Relayers

#### Python
```python
result = substrate.query(
    'DarwiniaFeeMarket', 'Relayers', []
)
```

#### Return value
```python
['[u8; 20]']
```
---------
### RelayersMap

#### Python
```python
result = substrate.query(
    'DarwiniaFeeMarket', 'RelayersMap', ['[u8; 20]']
)
```

#### Return value
```python
{'collateral': 'u128', 'fee': 'u128', 'id': '[u8; 20]'}
```
---------
## Constants

---------
### AssignedRelayerSlashRatio
 The slash ratio for assigned relayers.
#### Value
```python
200000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'AssignedRelayerSlashRatio')
```
---------
### CollateralPerOrder
 The collateral relayer need to lock for each order.

 This also represents the maximum slash value for a single delayed order.
 Please note that if this value is set to zero the fee market will be suspended.
#### Value
```python
50000000000000000000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'CollateralPerOrder')
```
---------
### ConfirmRelayersRewardRatio
#### Value
```python
200000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'ConfirmRelayersRewardRatio')
```
---------
### DutyRelayersRewardRatio
 Reward parameters
#### Value
```python
600000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'DutyRelayersRewardRatio')
```
---------
### LockId
#### Value
```python
'0x64612f6665656372'
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'LockId')
```
---------
### MessageRelayersRewardRatio
#### Value
```python
800000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'MessageRelayersRewardRatio')
```
---------
### MinimumRelayFee
 The minimum fee for relaying.
#### Value
```python
15000000000000000000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'MinimumRelayFee')
```
---------
### Slot
 The slot times set
#### Value
```python
600
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'Slot')
```
---------
### TreasuryPalletId
 Some reward goes to Treasury.
#### Value
```python
'0x64612f7472737279'
```
#### Python
```python
constant = substrate.get_constant('DarwiniaFeeMarket', 'TreasuryPalletId')
```
---------
## Errors

---------
### AlreadyEnrolled
The relayer has been enrolled.

---------
### CollateralTooLow
Locked collateral is too low to cover one order.

---------
### InsufficientBalance
Insufficient balance.

---------
### NewCollateralShouldLargerThanBefore
New collateral should large than the original one.

---------
### NewCollateralShouldLessThanBefore
New collateral should less than the original one.

---------
### NotEnrolled
This relayer doesn&\#x27;t enroll ever.

---------
### OccupiedRelayer
The relayer is occupied, and can&\#x27;t cancel enrollment now.

---------
### RelayFeeTooLow
The fee is lower than MinimumRelayFee.

---------
### StillHasOrdersNotConfirmed
Update locked collateral is not allow since some orders are not confirm.

---------