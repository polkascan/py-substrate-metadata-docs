
# SubtensorModule

---------
## Calls

---------
### add_stake
#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 
| amount_staked | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'add_stake', {
    'amount_staked': 'u64',
    'hotkey': 'AccountId',
}
)
```

---------
### become_delegate
#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'become_delegate', {'hotkey': 'AccountId'}
)
```

---------
### burned_register
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| hotkey | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'burned_register', {
    'hotkey': 'AccountId',
    'netuid': 'u16',
}
)
```

---------
### dissolve_network
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'dissolve_network', {'netuid': 'u16'}
)
```

---------
### faucet
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_number | `u64` | 
| nonce | `u64` | 
| work | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'faucet', {
    'block_number': 'u64',
    'nonce': 'u64',
    'work': 'Bytes',
}
)
```

---------
### register
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| block_number | `u64` | 
| nonce | `u64` | 
| work | `Vec<u8>` | 
| hotkey | `T::AccountId` | 
| coldkey | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'register', {
    'block_number': 'u64',
    'coldkey': 'AccountId',
    'hotkey': 'AccountId',
    'netuid': 'u16',
    'nonce': 'u64',
    'work': 'Bytes',
}
)
```

---------
### register_network
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'register_network', {}
)
```

---------
### remove_stake
#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 
| amount_unstaked | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'remove_stake', {
    'amount_unstaked': 'u64',
    'hotkey': 'AccountId',
}
)
```

---------
### root_register
#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'root_register', {'hotkey': 'AccountId'}
)
```

---------
### serve_axon
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| version | `u32` | 
| ip | `u128` | 
| port | `u16` | 
| ip_type | `u8` | 
| protocol | `u8` | 
| placeholder1 | `u8` | 
| placeholder2 | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'serve_axon', {
    'ip': 'u128',
    'ip_type': 'u8',
    'netuid': 'u16',
    'placeholder1': 'u8',
    'placeholder2': 'u8',
    'port': 'u16',
    'protocol': 'u8',
    'version': 'u32',
}
)
```

---------
### serve_prometheus
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| version | `u32` | 
| ip | `u128` | 
| port | `u16` | 
| ip_type | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'serve_prometheus', {
    'ip': 'u128',
    'ip_type': 'u8',
    'netuid': 'u16',
    'port': 'u16',
    'version': 'u32',
}
)
```

---------
### set_weights
#### Attributes
| Name | Type |
| -------- | -------- | 
| netuid | `u16` | 
| dests | `Vec<u16>` | 
| weights | `Vec<u16>` | 
| version_key | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'set_weights', {
    'dests': ['u16'],
    'netuid': 'u16',
    'version_key': 'u64',
    'weights': ['u16'],
}
)
```

---------
### sudo
Authenticates a council proposal and dispatches a function call with `Root` origin.

The dispatch origin for this call must be a council majority.

\#\# Complexity
- O(1).
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<T::SudoRuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo', {'call': 'Call'}
)
```

---------
### sudo_unchecked_weight
Authenticates a council proposal and dispatches a function call with `Root` origin.
This function does not check the weight of the call, and instead allows the
user to specify the weight of the call.

The dispatch origin for this call must be a council majority.

\#\# Complexity
- O(1).
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<T::SudoRuntimeCall>` | 
| weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_unchecked_weight', {
    'call': 'Call',
    'weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### swap_hotkey
#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 
| new_hotkey | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'swap_hotkey', {
    'hotkey': 'AccountId',
    'new_hotkey': 'AccountId',
}
)
```

---------
### vote
#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 
| proposal | `T::Hash` | 
| index | `u32` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'vote', {
    'approve': 'bool',
    'hotkey': 'AccountId',
    'index': 'u32',
    'proposal': 'scale_info::10',
}
)
```

---------
## Events

---------
### ActivityCutoffSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### AdjustmentAlphaSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### AdjustmentIntervalSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### AxonServed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `T::AccountId` | ```AccountId```

---------
### BondsMovingAverageSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### BulkBalancesSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### BulkNeuronsRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### BurnSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### DefaultTakeSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```

---------
### DelegateAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `u16` | ```u16```

---------
### DifficultySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### EmissionValuesSet
#### Attributes
No attributes

---------
### Faucet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### HotkeySwapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| coldkey | `T::AccountId` | ```AccountId```
| old_hotkey | `T::AccountId` | ```AccountId```
| new_hotkey | `T::AccountId` | ```AccountId```

---------
### ImmunityPeriodSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### KappaSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### MaxAllowedUidsSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### MaxAllowedValidatorsSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### MaxBurnSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### MaxDifficultySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### MaxRegistrationsPerBlockSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### MaxWeightLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### MinAllowedWeightSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### MinBurnSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### MinDifficultySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### NetworkAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### NetworkImmunityPeriodSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### NetworkLockCostReductionIntervalSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### NetworkMinLockCostSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### NetworkRateLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### NetworkRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```

---------
### NeuronRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```
| None | `T::AccountId` | ```AccountId```

---------
### PowRegistrationAllowed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `bool` | ```bool```

---------
### PrometheusServed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `T::AccountId` | ```AccountId```

---------
### RAORecycledForRegistrationSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### RegistrationAllowed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `bool` | ```bool```

---------
### RegistrationPerIntervalSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### RhoSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### ScalingLawPowerSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### SenateRequiredStakePercentSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ServingRateLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### StakeAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### StakeRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### SubnetLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```

---------
### SubnetOwnerCutSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```

---------
### Sudid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### TempoSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### TxRateLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ValidatorPruneLenSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### WeightsMinStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### WeightsSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u16` | ```u16```

---------
### WeightsSetRateLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
### WeightsVersionKeySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u16` | ```u16```
| None | `u64` | ```u64```

---------
## Storage functions

---------
### Active

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Active', ['u16']
)
```

#### Return value
```python
['bool']
```
---------
### ActivityCutoff

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ActivityCutoff', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### AdjustmentAlpha

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'AdjustmentAlpha', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### AdjustmentInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'AdjustmentInterval', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### Axons

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Axons', ['u16', 'AccountId']
)
```

#### Return value
```python
{
    'block': 'u64',
    'ip': 'u128',
    'ip_type': 'u8',
    'placeholder1': 'u8',
    'placeholder2': 'u8',
    'port': 'u16',
    'protocol': 'u8',
    'version': 'u32',
}
```
---------
### BlockAtRegistration

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BlockAtRegistration', ['u16', 'u16']
)
```

#### Return value
```python
'u64'
```
---------
### BlockEmission

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BlockEmission', []
)
```

#### Return value
```python
'u64'
```
---------
### BlocksSinceLastStep

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BlocksSinceLastStep', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### Bonds

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Bonds', ['u16', 'u16']
)
```

#### Return value
```python
[('u16', 'u16')]
```
---------
### BondsMovingAverage

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BondsMovingAverage', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### Burn

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Burn', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### BurnRegistrationsThisInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BurnRegistrationsThisInterval', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### Consensus

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Consensus', ['u16']
)
```

#### Return value
```python
['u16']
```
---------
### DefaultTake

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'DefaultTake', []
)
```

#### Return value
```python
'u16'
```
---------
### Delegates

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Delegates', ['AccountId']
)
```

#### Return value
```python
'u16'
```
---------
### Difficulty

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Difficulty', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### Dividends

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Dividends', ['u16']
)
```

#### Return value
```python
['u16']
```
---------
### Emission

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Emission', ['u16']
)
```

#### Return value
```python
['u64']
```
---------
### EmissionValues

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'EmissionValues', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### ImmunityPeriod

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ImmunityPeriod', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### Incentive

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Incentive', ['u16']
)
```

#### Return value
```python
['u16']
```
---------
### IsNetworkMember

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'IsNetworkMember', ['AccountId', 'u16']
)
```

#### Return value
```python
'bool'
```
---------
### Kappa

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Kappa', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### Keys

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Keys', ['u16', 'u16']
)
```

#### Return value
```python
'AccountId'
```
---------
### LastAdjustmentBlock

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'LastAdjustmentBlock', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### LastMechansimStepBlock

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'LastMechansimStepBlock', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### LastTxBlock

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'LastTxBlock', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### LastUpdate

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'LastUpdate', ['u16']
)
```

#### Return value
```python
['u64']
```
---------
### LoadedEmission

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'LoadedEmission', ['u16']
)
```

#### Return value
```python
[('AccountId', 'u64', 'u64')]
```
---------
### MaxAllowedUids

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxAllowedUids', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### MaxAllowedValidators

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxAllowedValidators', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### MaxBurn

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxBurn', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### MaxDifficulty

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxDifficulty', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### MaxRegistrationsPerBlock

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxRegistrationsPerBlock', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### MaxWeightsLimit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxWeightsLimit', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### MinAllowedWeights

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MinAllowedWeights', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### MinBurn

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MinBurn', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### MinDifficulty

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MinDifficulty', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### NetworkImmunityPeriod

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkImmunityPeriod', []
)
```

#### Return value
```python
'u64'
```
---------
### NetworkLastLockCost

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkLastLockCost', []
)
```

#### Return value
```python
'u64'
```
---------
### NetworkLastRegistered

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkLastRegistered', []
)
```

#### Return value
```python
'u64'
```
---------
### NetworkLockReductionInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkLockReductionInterval', []
)
```

#### Return value
```python
'u64'
```
---------
### NetworkMinAllowedUids

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkMinAllowedUids', []
)
```

#### Return value
```python
'u16'
```
---------
### NetworkMinLockCost

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkMinLockCost', []
)
```

#### Return value
```python
'u64'
```
---------
### NetworkModality

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkModality', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### NetworkPowRegistrationAllowed

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkPowRegistrationAllowed', ['u16']
)
```

#### Return value
```python
'bool'
```
---------
### NetworkRateLimit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkRateLimit', []
)
```

#### Return value
```python
'u64'
```
---------
### NetworkRegisteredAt

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkRegisteredAt', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### NetworkRegistrationAllowed

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworkRegistrationAllowed', ['u16']
)
```

#### Return value
```python
'bool'
```
---------
### NetworksAdded

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NetworksAdded', ['u16']
)
```

#### Return value
```python
'bool'
```
---------
### NeuronsToPruneAtNextEpoch

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NeuronsToPruneAtNextEpoch', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### Owner

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Owner', ['AccountId']
)
```

#### Return value
```python
'AccountId'
```
---------
### POWRegistrationsThisInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'POWRegistrationsThisInterval', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### PendingEmission

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'PendingEmission', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### Prometheus

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Prometheus', ['u16', 'AccountId']
)
```

#### Return value
```python
{
    'block': 'u64',
    'ip': 'u128',
    'ip_type': 'u8',
    'port': 'u16',
    'version': 'u32',
}
```
---------
### PruningScores

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'PruningScores', ['u16']
)
```

#### Return value
```python
['u16']
```
---------
### RAORecycledForRegistration

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'RAORecycledForRegistration', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### Rank

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Rank', ['u16']
)
```

#### Return value
```python
['u16']
```
---------
### RegistrationsThisBlock

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'RegistrationsThisBlock', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### RegistrationsThisInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'RegistrationsThisInterval', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### Rho

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Rho', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### ScalingLawPower

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ScalingLawPower', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### SenateRequiredStakePercentage

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'SenateRequiredStakePercentage', []
)
```

#### Return value
```python
'u64'
```
---------
### ServingRateLimit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ServingRateLimit', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### Stake

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Stake', ['AccountId', 'AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### SubnetLimit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'SubnetLimit', []
)
```

#### Return value
```python
'u16'
```
---------
### SubnetLocked

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'SubnetLocked', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### SubnetOwner

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'SubnetOwner', ['u16']
)
```

#### Return value
```python
'AccountId'
```
---------
### SubnetOwnerCut

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'SubnetOwnerCut', []
)
```

#### Return value
```python
'u16'
```
---------
### SubnetworkN

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'SubnetworkN', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### TargetRegistrationsPerInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TargetRegistrationsPerInterval', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### Tempo

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Tempo', ['u16']
)
```

#### Return value
```python
'u16'
```
---------
### TotalColdkeyStake

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TotalColdkeyStake', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### TotalHotkeyStake

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TotalHotkeyStake', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### TotalIssuance

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TotalIssuance', []
)
```

#### Return value
```python
'u64'
```
---------
### TotalNetworks

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TotalNetworks', []
)
```

#### Return value
```python
'u16'
```
---------
### TotalStake

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TotalStake', []
)
```

#### Return value
```python
'u64'
```
---------
### Trust

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Trust', ['u16']
)
```

#### Return value
```python
['u16']
```
---------
### TxRateLimit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TxRateLimit', []
)
```

#### Return value
```python
'u64'
```
---------
### Uids

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Uids', ['u16', 'AccountId']
)
```

#### Return value
```python
'u16'
```
---------
### UsedWork

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'UsedWork', ['Bytes']
)
```

#### Return value
```python
'u64'
```
---------
### ValidatorPermit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorPermit', ['u16']
)
```

#### Return value
```python
['bool']
```
---------
### ValidatorPruneLen

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorPruneLen', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### ValidatorTrust

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorTrust', ['u16']
)
```

#### Return value
```python
['u16']
```
---------
### Weights

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Weights', ['u16', 'u16']
)
```

#### Return value
```python
[('u16', 'u16')]
```
---------
### WeightsMinStake

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'WeightsMinStake', []
)
```

#### Return value
```python
'u64'
```
---------
### WeightsSetRateLimit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'WeightsSetRateLimit', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
### WeightsVersionKey

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'WeightsVersionKey', ['u16']
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### InitialActivityCutoff
#### Value
```python
5000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialActivityCutoff')
```
---------
### InitialAdjustmentAlpha
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialAdjustmentAlpha')
```
---------
### InitialAdjustmentInterval
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialAdjustmentInterval')
```
---------
### InitialBondsMovingAverage
#### Value
```python
900000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialBondsMovingAverage')
```
---------
### InitialBurn
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialBurn')
```
---------
### InitialDefaultTake
#### Value
```python
11796
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialDefaultTake')
```
---------
### InitialDifficulty
#### Value
```python
10000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialDifficulty')
```
---------
### InitialEmissionValue
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialEmissionValue')
```
---------
### InitialImmunityPeriod
#### Value
```python
4096
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialImmunityPeriod')
```
---------
### InitialIssuance
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialIssuance')
```
---------
### InitialKappa
#### Value
```python
32767
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialKappa')
```
---------
### InitialMaxAllowedUids
#### Value
```python
4096
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxAllowedUids')
```
---------
### InitialMaxAllowedValidators
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxAllowedValidators')
```
---------
### InitialMaxBurn
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxBurn')
```
---------
### InitialMaxDifficulty
#### Value
```python
4611686018427387903
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxDifficulty')
```
---------
### InitialMaxRegistrationsPerBlock
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxRegistrationsPerBlock')
```
---------
### InitialMaxWeightsLimit
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxWeightsLimit')
```
---------
### InitialMinAllowedWeights
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMinAllowedWeights')
```
---------
### InitialMinBurn
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMinBurn')
```
---------
### InitialMinDifficulty
#### Value
```python
10000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMinDifficulty')
```
---------
### InitialNetworkImmunityPeriod
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialNetworkImmunityPeriod')
```
---------
### InitialNetworkLockReductionInterval
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialNetworkLockReductionInterval')
```
---------
### InitialNetworkMinAllowedUids
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialNetworkMinAllowedUids')
```
---------
### InitialNetworkMinLockCost
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialNetworkMinLockCost')
```
---------
### InitialNetworkRateLimit
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialNetworkRateLimit')
```
---------
### InitialPruningScore
#### Value
```python
65535
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialPruningScore')
```
---------
### InitialRAORecycledForRegistration
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialRAORecycledForRegistration')
```
---------
### InitialRho
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialRho')
```
---------
### InitialScalingLawPower
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialScalingLawPower')
```
---------
### InitialSenateRequiredStakePercentage
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialSenateRequiredStakePercentage')
```
---------
### InitialServingRateLimit
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialServingRateLimit')
```
---------
### InitialSubnetLimit
#### Value
```python
12
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialSubnetLimit')
```
---------
### InitialSubnetOwnerCut
#### Value
```python
11796
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialSubnetOwnerCut')
```
---------
### InitialTargetRegistrationsPerInterval
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialTargetRegistrationsPerInterval')
```
---------
### InitialTempo
#### Value
```python
99
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialTempo')
```
---------
### InitialTxRateLimit
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialTxRateLimit')
```
---------
### InitialValidatorPruneLen
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorPruneLen')
```
---------
### InitialWeightsVersionKey
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialWeightsVersionKey')
```
---------
## Errors

---------
### AllNetworksInImmunity

---------
### AlreadyDelegate

---------
### AlreadyRegistered

---------
### AlreadySenateMember

---------
### BalanceSetError

---------
### BalanceWithdrawalError

---------
### BelowStakeThreshold

---------
### BenchmarkingOnly

---------
### CouldNotConvertToBalance

---------
### DuplicateUids

---------
### EmissionValuesDoesNotMatchNetworks

---------
### FaucetDisabled

---------
### HotkeyOriginMismatch

---------
### IncorrectNetuidsLength

---------
### IncorrectNetworkVersionKey

---------
### InvalidDifficulty

---------
### InvalidEmissionValues

---------
### InvalidIpAddress

---------
### InvalidIpType

---------
### InvalidModality

---------
### InvalidPort

---------
### InvalidSeal

---------
### InvalidTempo

---------
### InvalidUid

---------
### InvalidWorkBlock

---------
### MaxAllowedUIdsNotAllowed

---------
### MaxAllowedUidsExceeded

---------
### MaxWeightExceeded

---------
### NetworkDoesNotExist

---------
### NetworkExist

---------
### NoValidatorPermit

---------
### NonAssociatedColdKey

---------
### NotDelegate

---------
### NotEnoughBalance

---------
### NotEnoughBalanceToStake

---------
### NotEnoughStakeToSetWeights

---------
### NotEnoughStaketoWithdraw

---------
### NotRegistered

---------
### NotSenateMember

---------
### NotSettingEnoughWeights

---------
### NotSubnetOwner

---------
### OperationNotPermittedonRootSubnet

---------
### RegistrationDisabled

---------
### SenateMember

---------
### ServingRateLimitExceeded

---------
### SettingWeightsTooFast

---------
### StakeAlreadyAdded

---------
### StakeTooLowForRoot

---------
### StorageValueOutOfRange

---------
### TempoHasNotSet

---------
### TooManyRegistrationsThisBlock

---------
### TooManyRegistrationsThisInterval

---------
### TooManyUids

---------
### TxRateLimitExceeded

---------
### WeightVecNotEqualSize

---------