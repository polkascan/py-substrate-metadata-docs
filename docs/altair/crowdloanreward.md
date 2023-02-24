
# CrowdloanReward

---------
## Calls

---------
### initialize
A on call init. Basically a composition of the setters below
#### Attributes
| Name | Type |
| -------- | -------- | 
| direct_payout_ratio | `Perbill` | 
| vesting_period | `T::BlockNumber` | 
| vesting_start | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanReward', 'initialize', {
    'direct_payout_ratio': 'u32',
    'vesting_period': 'u32',
    'vesting_start': 'u32',
}
)
```

---------
### set_direct_payout_ratio
Modify the ratio between vested and direct payout amount.

This administrative function allows to modify the ratio
between vested and direct payout amount after the pallet
was initialized via a call to the [`initialize`] transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ratio | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanReward', 'set_direct_payout_ratio', {'ratio': 'u32'}
)
```

---------
### set_vesting_period
Set vesting period.

This administrative transaction allows to modify the vesting period
after a previous [`initialize`] transaction was triggered in order
to perform seminal pallet configuration.

\#\# Emits
UpdateVestingPeriod
#### Attributes
| Name | Type |
| -------- | -------- | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanReward', 'set_vesting_period', {'period': 'u32'}
)
```

---------
### set_vesting_start
Set the start of the vesting period.
#### Attributes
| Name | Type |
| -------- | -------- | 
| start | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanReward', 'set_vesting_start', {'start': 'u32'}
)
```

---------
## Events

---------
### DirectPayoutRatioUpdated
Direct payout ratio for contributors has been updated
\[payout_ratio\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Perbill` | ```u32```

---------
### RewardClaimed
Event emitted when a reward claim was processed successfully.
\[who, direct_reward, vested_reward\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### RewardPalletInitialized
Event triggered when the reward module is ready to reward contributors
\[vesting_start, vesting_period, direct_payout_ratio\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `Perbill` | ```u32```

---------
### VestingPeriodUpdated
Vesting period has been updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
### VestingStartUpdated
Start of vesting has been updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### DirectPayoutRatio
 Which ratio of the rewards are payed directly. The rest is transferred via a vesting schedule.

#### Python
```python
result = substrate.query(
    'CrowdloanReward', 'DirectPayoutRatio', []
)
```

#### Return value
```python
'u32'
```
---------
### VestingPeriod
 Over which period are the contributions vested.

#### Python
```python
result = substrate.query(
    'CrowdloanReward', 'VestingPeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### VestingStart
 At which block number does the vesting start.

#### Python
```python
result = substrate.query(
    'CrowdloanReward', 'VestingStart', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### PalletId
 Constant configuration parameter to store the module identifier for the pallet.

 The module identifier may be of the form ```PalletId(*b&quot;cc/rwrd&quot;)```. This
 constant is set when building this config trait for the runtime.

 \# Example
 ```rust,ignore

 // Parameterize crowdloan reward pallet configuration
 parameter_types! {
   pub const CrowdloanRewardPalletId: PalletId = PalletId(*b&quot;cc/rwrd&quot;);
 }

 // Implement crowdloan reward pallet&#x27;s configuration trait for the runtime
 impl pallet_crowdloarn_reward::Config for Runtime {
   type Event = Event;
   type WeightInfo = ();
   type PalletId = CrowdloanRewardPalletId;
 }

 ```
#### Value
```python
'0x63632f7265777264'
```
#### Python
```python
constant = substrate.get_constant('CrowdloanReward', 'PalletId')
```
---------
## Errors

---------
### MustBeAdministrator
Invalid call to an administrative extrinsics

---------
### PalletNotInitialized
Pallet must be initialized first

---------
### RewardInsufficient
The reward is below the existential deposit

---------