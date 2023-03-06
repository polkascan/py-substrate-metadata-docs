
# SubtensorModule

---------
## Calls

---------
### add_stake
--- Adds stake to a neuron account. The call is made from the
coldkey account linked in the neurons&\#x27;s NeuronMetadata.
Only the associated coldkey is allowed to make staking and
unstaking requests. This protects the neuron against
attacks on its hotkey running in production code.

\# Args:
	* &\#x27;origin&\#x27;: (&lt;T as frame_system::Config&gt;Origin):
		- The caller, a coldkey signature associated with the hotkey account.

	* &\#x27;hotkey&\#x27; (T::AccountId):
		- The hotkey account to add stake to.

	* &\#x27;ammount_staked&\#x27; (u64):
		- The ammount to transfer from the balances account of the cold key
		into the staking account of the hotkey.

\# Event:
	* &\#x27;StakeAdded&\#x27;:
		- On the successful staking of funds.

\# Raises:
	* &\#x27;NotRegistered&\#x27;:
		- If the hotkey account is not active (has not subscribed)

	* &\#x27;NonAssociatedColdKey&\#x27;:
		- When the calling coldkey is not associated with the hotkey account.

	* &\#x27;InsufficientBalance&\#x27;:
		- When the amount to stake exceeds the amount of balance in the
		associated colkey account.

#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 
| ammount_staked | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'add_stake', {
    'ammount_staked': 'u64',
    'hotkey': 'AccountId',
}
)
```

---------
### register
---- Registers a new neuron to the graph. 

\# Args:
	* &\#x27;origin&\#x27;: (&lt;T as frame_system::Config&gt;Origin):
		- The caller, registration key as found in RegistrationKey::get(0);

	* &\#x27;block_number&\#x27; (u64):
		- Block number of hash to attempt.

	* &\#x27;nonce&\#x27; (u64):
		- Hashing nonce as a u64.

	* &\#x27;work&\#x27; (Vec&lt;u8&gt;):
		- Work hash as list of bytes.

	* &\#x27;hotkey&\#x27; (T::AccountId,):
		- Hotkey to register.

	* &\#x27;coldkey&\#x27; (T::AccountId,):
		- Coldkey to register.

\# Event:
	* &\#x27;NeuronRegistered&\#x27;:
		- On subscription of a new neuron to the active set.

#### Attributes
| Name | Type |
| -------- | -------- | 
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
    'nonce': 'u64',
    'work': 'Bytes',
}
)
```

---------
### remove_stake
---- Remove stake from the staking account. The call must be made
from the coldkey account attached to the neuron metadata. Only this key
has permission to make staking and unstaking requests.

\# Args:
	* &\#x27;origin&\#x27;: (&lt;T as frame_system::Config&gt;Origin):
		- The caller, a coldkey signature associated with the hotkey account.

	* &\#x27;hotkey&\#x27; (T::AccountId):
		- The hotkey account to withdraw stake from.

	* &\#x27;ammount_unstaked&\#x27; (u64):
		- The ammount to transfer from the staking account into the balance
		of the coldkey.

\# Event:
	* &\#x27;StakeRemoved&\#x27;:
		- On successful withdrawl.

\# Raises:
	* &\#x27;NonAssociatedColdKey&\#x27;:
		- When the calling coldkey is not associated with the hotkey account.

	* &\#x27;NotEnoughStaketoWithdraw&\#x27;:
		- When the amount to unstake exceeds the quantity staked in the
		associated hotkey staking account.

#### Attributes
| Name | Type |
| -------- | -------- | 
| hotkey | `T::AccountId` | 
| ammount_unstaked | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'remove_stake', {
    'ammount_unstaked': 'u64',
    'hotkey': 'AccountId',
}
)
```

---------
### serve_axon
---- Serves or updates axon information for the neuron associated with the caller. If the caller
already registered the metadata is updated. If the caller is not registered this call throws NotRegsitered.

\# Args:
	* &\#x27;origin&\#x27;: (&lt;T as frame_system::Config&gt;Origin):
		- The caller, a hotkey associated of the registered neuron.

	* &\#x27;ip&\#x27; (u128):
		- The u64 encoded IP address of type 6 or 4.

	* &\#x27;port&\#x27; (u16):
		- The port number where this neuron receives RPC requests.

	* &\#x27;ip_type&\#x27; (u8):
		- The ip type one of (4,6).

	* &\#x27;modality&\#x27; (u8):
		- The neuron modality type.

\# Event:
	* &\#x27;AxonServed&\#x27;:
		- On subscription of a new neuron to the active set.

#### Attributes
| Name | Type |
| -------- | -------- | 
| version | `u32` | 
| ip | `u128` | 
| port | `u16` | 
| ip_type | `u8` | 
| modality | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'serve_axon', {
    'ip': 'u128',
    'ip_type': 'u8',
    'modality': 'u8',
    'port': 'u16',
    'version': 'u32',
}
)
```

---------
### set_weights
--- Sets the caller weights for the incentive mechanism. The call can be
made from the hotkey account so is potentially insecure, however, the damage
of changing weights is minimal if caught early. This function includes all the
checks that the passed weights meet the requirements. Stored as u32s they represent
rational values in the range [0,1] which sum to 1 and can be interpreted as
probabilities. The specific weights determine how inflation propagates outward
from this peer. 

Note: The 32 bit integers weights should represent 1.0 as the max u32.
However, the function normalizes all integers to u32_max anyway. This means that if the sum of all
elements is larger or smaller than the amount of elements * u32_max, all elements
will be corrected for this deviation. 

\# Args:
	* `origin`: (&lt;T as frame_system::Config&gt;Origin):
		- The caller, a hotkey who wishes to set their weights.

	* `uids` (Vec&lt;u32&gt;):
		- The edge endpoint for the weight, i.e. j for w_ij.

	* &\#x27;weights&\#x27; (Vec&lt;u32&gt;):
		- The u32 integer encoded weights. Interpreted as rational
		values in the range [0,1]. They must sum to in32::MAX.

\# Event:
	* WeightsSet;
		- On successfully setting the weights on chain.

\# Raises:
	* &\#x27;WeightVecNotEqualSize&\#x27;:
		- If the passed weights and uids have unequal size.

	* &\#x27;WeightSumToLarge&\#x27;:
		- When the calling coldkey is not associated with the hotkey account.

	* &\#x27;InsufficientBalance&\#x27;:
		- When the amount to stake exceeds the amount of balance in the
		associated colkey account.

#### Attributes
| Name | Type |
| -------- | -------- | 
| dests | `Vec<u32>` | 
| weights | `Vec<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'set_weights', {'dests': ['u32'], 'weights': ['u32']}
)
```

---------
### sudo_reset_bonds
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_reset_bonds', {}
)
```

---------
### sudo_set_activity_cutoff
#### Attributes
| Name | Type |
| -------- | -------- | 
| activity_cutoff | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_activity_cutoff', {'activity_cutoff': 'u64'}
)
```

---------
### sudo_set_adjustment_interval
#### Attributes
| Name | Type |
| -------- | -------- | 
| adjustment_interval | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_adjustment_interval', {'adjustment_interval': 'u64'}
)
```

---------
### sudo_set_blocks_per_step
---- SUDO ONLY FUNCTIONS

\# Args:
	* &\#x27;origin&\#x27;: (&lt;T as frame_system::Config&gt;Origin):
		- The caller, must be sudo.

ONE OF:
	* &\#x27;adjustment_interval&\#x27; (u64):
	* &\#x27;activity_cutoff&\#x27; (u64):
	* &\#x27;difficulty&\#x27; (u64):

\# Events:
		* &\#x27;DifficultySet&\#x27;
	* &\#x27;AdjustmentIntervalSet&\#x27;
		* &\#x27;ActivityCuttoffSet&\#x27;
		* &\#x27;TargetRegistrationsPerIntervalSet&\#x27;


#### Attributes
| Name | Type |
| -------- | -------- | 
| blocks_per_step | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_blocks_per_step', {'blocks_per_step': 'u64'}
)
```

---------
### sudo_set_bonds_moving_average
#### Attributes
| Name | Type |
| -------- | -------- | 
| bonds_moving_average | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_bonds_moving_average', {'bonds_moving_average': 'u64'}
)
```

---------
### sudo_set_difficulty
#### Attributes
| Name | Type |
| -------- | -------- | 
| difficulty | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_difficulty', {'difficulty': 'u64'}
)
```

---------
### sudo_set_immunity_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| immunity_period | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_immunity_period', {'immunity_period': 'u64'}
)
```

---------
### sudo_set_incentive_pruning_denominator
#### Attributes
| Name | Type |
| -------- | -------- | 
| incentive_pruning_denominator | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_incentive_pruning_denominator', {
    'incentive_pruning_denominator': 'u64',
}
)
```

---------
### sudo_set_kappa
#### Attributes
| Name | Type |
| -------- | -------- | 
| kappa | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_kappa', {'kappa': 'u64'}
)
```

---------
### sudo_set_max_allowed_max_min_ratio
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_allowed_max_min_ratio | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_max_allowed_max_min_ratio', {'max_allowed_max_min_ratio': 'u64'}
)
```

---------
### sudo_set_max_allowed_uids
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_allowed_uids | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_max_allowed_uids', {'max_allowed_uids': 'u64'}
)
```

---------
### sudo_set_max_weight_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_weight_limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_max_weight_limit', {'max_weight_limit': 'u32'}
)
```

---------
### sudo_set_min_allowed_weights
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_allowed_weights | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_min_allowed_weights', {'min_allowed_weights': 'u64'}
)
```

---------
### sudo_set_rho
#### Attributes
| Name | Type |
| -------- | -------- | 
| rho | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_rho', {'rho': 'u64'}
)
```

---------
### sudo_set_scaling_law_power
#### Attributes
| Name | Type |
| -------- | -------- | 
| scaling_law_power | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_scaling_law_power', {'scaling_law_power': 'u8'}
)
```

---------
### sudo_set_stake_pruning_denominator
#### Attributes
| Name | Type |
| -------- | -------- | 
| stake_pruning_denominator | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_stake_pruning_denominator', {'stake_pruning_denominator': 'u64'}
)
```

---------
### sudo_set_stake_pruning_min
#### Attributes
| Name | Type |
| -------- | -------- | 
| stake_pruning_min | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_stake_pruning_min', {'stake_pruning_min': 'u64'}
)
```

---------
### sudo_set_synergy_scaling_law_power
#### Attributes
| Name | Type |
| -------- | -------- | 
| synergy_scaling_law_power | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_synergy_scaling_law_power', {'synergy_scaling_law_power': 'u8'}
)
```

---------
### sudo_set_validator_batch_size
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_batch_size | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_validator_batch_size', {'validator_batch_size': 'u64'}
)
```

---------
### sudo_set_validator_epoch_len
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_epoch_len | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_validator_epoch_len', {'validator_epoch_len': 'u64'}
)
```

---------
### sudo_set_validator_epochs_per_reset
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_epochs_per_reset | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_validator_epochs_per_reset', {'validator_epochs_per_reset': 'u64'}
)
```

---------
### sudo_set_validator_exclude_quantile
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_exclude_quantile | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_validator_exclude_quantile', {'validator_exclude_quantile': 'u8'}
)
```

---------
### sudo_set_validator_logits_divergence
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_logits_divergence | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_validator_logits_divergence', {'validator_logits_divergence': 'u64'}
)
```

---------
### sudo_set_validator_prune_len
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_prune_len | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_validator_prune_len', {'validator_prune_len': 'u64'}
)
```

---------
### sudo_set_validator_sequence_length
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_sequence_length | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_set_validator_sequence_length', {'validator_sequence_length': 'u64'}
)
```

---------
### sudo_target_registrations_per_interval
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_registrations_per_interval | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'SubtensorModule', 'sudo_target_registrations_per_interval', {
    'target_registrations_per_interval': 'u64',
}
)
```

---------
## Events

---------
### ActivityCuttoffSet
--- Event created when the activity cuttoff has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### AdjustmentIntervalSet
--- Event created when the difficulty adjustment interval has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### AxonServed
--- Event created when the axon server information is added to the network.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### BlocksPerStepSet
--- Event created when default blocks per step has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### BondsMovingAverageSet
--- Event created when bonds moving average set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### DifficultySet
--- Event created when the difficulty has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### FoundationAccountSet
--- Event created when the foundation account has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### FoundationDistributionSet
--- Event created when the foundation distribution has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ImmunityPeriodSet
--- Event created when the immunity period has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### IncentivePruningDenominatorSet
--- Event created when the incentive pruning denominator has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### KappaSet
--- Event created when mechanism kappa has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### MaxAllowedMaxMinRatioSet
--- Event created when the max allowed max min ration has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### MaxAllowedUidsSet
--- Event created when max allowed uids has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### MaxWeightLimitSet
--- Event created when the max weight limit has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### MinAllowedWeightsSet
--- Event created when min allowed weights has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### NeuronRegistered
--- Event created when a new neuron account has been registered to 
the chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### ResetBonds
--- Event thrown when bonds have been reset.
#### Attributes
No attributes

---------
### RhoSet
--- Event created when mechanism rho has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ScalingLawPowerSet
--- Event created when the scaling law power has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```

---------
### SomethingStored
Event documentation should end with an array that provides descriptive names for event
parameters. [something, who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
### StakeAdded
--- Event created during when stake has been transfered from 
the coldkey onto the hotkey staking account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### StakePruningDenominatorSet
--- Event created when the stake pruning denominator has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### StakePruningMinSet
--- Event created when the stake pruning min has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### StakeRemoved
--- Event created when stake has been removed from 
the staking account into the coldkey account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### SynergyScalingLawPowerSet
--- Event created when the synergy scaling law power has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```

---------
### TargetRegistrationsPerIntervalSet
--- Event created when the target registrations per interval has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ValidatorBatchSizeSet
--- Event created when the batch size has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ValidatorEpochLenSet
--- Event created when the validator default epoch length has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ValidatorEpochsPerResetSet
--- Event created when the validator default epoch per reset has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ValidatorExcludeQuantileSet
--- Event created when the validator exclude quantile has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```

---------
### ValidatorLogitsDivergenceSet
--- Event created when the validator logits divergence value has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ValidatorPruneLenSet
--- Event created when the validator pruning length has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ValidatorSequenceLengthSet
--- Event created when the sequence length has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### WeightsSet
---- Event created when a caller successfully set&\#x27;s their weights
on the chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ActivityCutoff

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ActivityCutoff', []
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
    'SubtensorModule', 'AdjustmentInterval', []
)
```

#### Return value
```python
'u64'
```
---------
### BlockAtRegistration

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BlockAtRegistration', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### BlocksPerStep

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BlocksPerStep', []
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
    'SubtensorModule', 'BlocksSinceLastStep', []
)
```

#### Return value
```python
'u64'
```
---------
### BondsMovingAverage

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'BondsMovingAverage', []
)
```

#### Return value
```python
'u64'
```
---------
### Difficulty

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Difficulty', []
)
```

#### Return value
```python
'u64'
```
---------
### FoundationAccount
 \#[pallet::type_value] 
 pub fn DefaultFoundationAccount&lt;T: Config&gt;() -&gt; u64 { T::InitialFoundationAccount::get() }

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'FoundationAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### FoundationDistribution

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'FoundationDistribution', []
)
```

#### Return value
```python
'u64'
```
---------
### Hotkeys
 ---- Maps from hotkey to uid.

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Hotkeys', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### ImmunityPeriod

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ImmunityPeriod', []
)
```

#### Return value
```python
'u64'
```
---------
### IncentivePruningDenominator

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'IncentivePruningDenominator', []
)
```

#### Return value
```python
'u64'
```
---------
### Kappa

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Kappa', []
)
```

#### Return value
```python
'u64'
```
---------
### LastDifficultyAdjustmentBlock

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'LastDifficultyAdjustmentBlock', []
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
    'SubtensorModule', 'LastMechansimStepBlock', []
)
```

#### Return value
```python
'u64'
```
---------
### MaxAllowedMaxMinRatio

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxAllowedMaxMinRatio', []
)
```

#### Return value
```python
'u64'
```
---------
### MaxAllowedUids

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxAllowedUids', []
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
    'SubtensorModule', 'MaxRegistrationsPerBlock', []
)
```

#### Return value
```python
'u64'
```
---------
### MaxWeightLimit

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MaxWeightLimit', []
)
```

#### Return value
```python
'u32'
```
---------
### MinAllowedWeights

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'MinAllowedWeights', []
)
```

#### Return value
```python
'u64'
```
---------
### N
 ************************************************************
	*---- Storage Objects
 ************************************************************

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'N', []
)
```

#### Return value
```python
'u32'
```
---------
### Neurons
 ---- Maps from uid to neuron.

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Neurons', ['u32']
)
```

#### Return value
```python
{
    'active': 'u32',
    'bonds': [('u32', 'u64')],
    'coldkey': 'AccountId',
    'consensus': 'u64',
    'dividends': 'u64',
    'emission': 'u64',
    'hotkey': 'AccountId',
    'incentive': 'u64',
    'ip': 'u128',
    'ip_type': 'u8',
    'last_update': 'u64',
    'modality': 'u8',
    'port': 'u16',
    'priority': 'u64',
    'rank': 'u64',
    'stake': 'u64',
    'trust': 'u64',
    'uid': 'u32',
    'version': 'u32',
    'weights': [('u32', 'u32')],
}
```
---------
### NeuronsToPruneAtNextEpoch
 ---- Maps from uid to uid as a set which we use to record uids to prune at next epoch.

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'NeuronsToPruneAtNextEpoch', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### RegistrationsThisBlock

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'RegistrationsThisBlock', []
)
```

#### Return value
```python
'u64'
```
---------
### RegistrationsThisInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'RegistrationsThisInterval', []
)
```

#### Return value
```python
'u64'
```
---------
### Rho

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'Rho', []
)
```

#### Return value
```python
'u64'
```
---------
### ScalingLawPower

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ScalingLawPower', []
)
```

#### Return value
```python
'u8'
```
---------
### StakePruningDenominator

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'StakePruningDenominator', []
)
```

#### Return value
```python
'u64'
```
---------
### StakePruningMin

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'StakePruningMin', []
)
```

#### Return value
```python
'u64'
```
---------
### SynergyScalingLawPower

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'SynergyScalingLawPower', []
)
```

#### Return value
```python
'u8'
```
---------
### TargetRegistrationsPerInterval

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TargetRegistrationsPerInterval', []
)
```

#### Return value
```python
'u64'
```
---------
### TotalBondsPurchased

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TotalBondsPurchased', []
)
```

#### Return value
```python
'u64'
```
---------
### TotalEmission

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'TotalEmission', []
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
### ValidatorBatchSize

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorBatchSize', []
)
```

#### Return value
```python
'u64'
```
---------
### ValidatorEpochLen

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorEpochLen', []
)
```

#### Return value
```python
'u64'
```
---------
### ValidatorEpochsPerReset

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorEpochsPerReset', []
)
```

#### Return value
```python
'u64'
```
---------
### ValidatorExcludeQuantile

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorExcludeQuantile', []
)
```

#### Return value
```python
'u8'
```
---------
### ValidatorLogitsDivergence

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorLogitsDivergence', []
)
```

#### Return value
```python
'u64'
```
---------
### ValidatorPruneLen

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorPruneLen', []
)
```

#### Return value
```python
'u64'
```
---------
### ValidatorSequenceLength

#### Python
```python
result = substrate.query(
    'SubtensorModule', 'ValidatorSequenceLength', []
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
 Activity constant
#### Value
```python
5000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialActivityCutoff')
```
---------
### InitialAdjustmentInterval
 Initial adjustment interval.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialAdjustmentInterval')
```
---------
### InitialBlocksPerStep
 Blocks per step.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialBlocksPerStep')
```
---------
### InitialBondsMovingAverage
 Blocks per era.
#### Value
```python
900000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialBondsMovingAverage')
```
---------
### InitialDifficulty
 Initial registration difficulty.
#### Value
```python
10000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialDifficulty')
```
---------
### InitialFoundationDistribution
 Initial foundation distribution
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialFoundationDistribution')
```
---------
### InitialImmunityPeriod
 Immunity Period Constant.
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialImmunityPeriod')
```
---------
### InitialIncentivePruningDenominator
 Initial incentive pruning denominator
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialIncentivePruningDenominator')
```
---------
### InitialIssuance
 Initial registration difficulty.
#### Value
```python
548833985028256
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialIssuance')
```
---------
### InitialKappa
 Kappa constant
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialKappa')
```
---------
### InitialMaxAllowedMaxMinRatio
 Initial allowed max min weight ratio
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxAllowedMaxMinRatio')
```
---------
### InitialMaxAllowedUids
 Max UID constant.
#### Value
```python
2000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxAllowedUids')
```
---------
### InitialMaxRegistrationsPerBlock
 Initial max registrations per block.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxRegistrationsPerBlock')
```
---------
### InitialMaxWeightLimit
 Initial max weight limit.
#### Value
```python
4294967295
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMaxWeightLimit')
```
---------
### InitialMinAllowedWeights
 Initial min allowed weights.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialMinAllowedWeights')
```
---------
### InitialRho
 Rho constant
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
 Initial scaling law power.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialScalingLawPower')
```
---------
### InitialStakePruningDenominator
 Initial stake pruning denominator
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialStakePruningDenominator')
```
---------
### InitialStakePruningMin
 Initial stake pruning min
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialStakePruningMin')
```
---------
### InitialSynergyScalingLawPower
 Initial synergy scaling law power.
#### Value
```python
60
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialSynergyScalingLawPower')
```
---------
### InitialTargetRegistrationsPerInterval
 Initial target registrations per interval.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialTargetRegistrationsPerInterval')
```
---------
### InitialValidatorBatchSize
 Default Batch size.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorBatchSize')
```
---------
### InitialValidatorEpochLen
 Default Epoch length.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorEpochLen')
```
---------
### InitialValidatorEpochsPerReset
 Default Reset length.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorEpochsPerReset')
```
---------
### InitialValidatorExcludeQuantile
 Initial validator exclude quantile.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorExcludeQuantile')
```
---------
### InitialValidatorLogitsDivergence
 Initial validator logits divergence penalty/threshold.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorLogitsDivergence')
```
---------
### InitialValidatorPruneLen
 Initial validator context pruning length.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorPruneLen')
```
---------
### InitialValidatorSequenceLen
 Default Batch size.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'InitialValidatorSequenceLen')
```
---------
### MaximumDifficulty
 Maximum registration difficulty
#### Value
```python
4611686018427387903
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'MaximumDifficulty')
```
---------
### MinimumDifficulty
 Minimum registration difficulty
#### Value
```python
10000000
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'MinimumDifficulty')
```
---------
### SDebug
 Debug is on
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'SDebug')
```
---------
### SelfOwnership
 SelfOwnership constant
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('SubtensorModule', 'SelfOwnership')
```
---------
## Errors

---------
### AlreadyRegistered
---- Thrown when the caller requests registering a neuron which 
already exists in the active set.

---------
### BalanceWithdrawalError
---- Thrown when the caller tries to add stake, but for some reason the requested
amount could not be withdrawn from the coldkey account

---------
### CouldNotConvertToBalance
---- Thrown when the dispatch attempts to convert between a u64 and T::balance 
but the call fails.

---------
### DuplicateUids
---- Thrown when the caller attempts to set weights with duplicate uids
in the weight matrix.

---------
### InvalidDifficulty
---- Thrown if the supplied pow hash block does not meet the network difficulty.

---------
### InvalidIpAddress
--- Thrown when an invalid IP address is passed to the serve function.

---------
### InvalidIpType
---- Thrown when the user tries to serve an axon which is not of type
4 (IPv4) or 6 (IPv6).

---------
### InvalidModality
--- Thrown when an invalid modality attempted on serve.
Currently the chain only accepts modality TEXT = 0.

---------
### InvalidSeal
---- Thrown if the supplied pow hash seal does not match the supplied work.

---------
### InvalidUid
---- Thrown when a caller attempts to set weight to at least one uid that
does not exist in the metagraph.

---------
### InvalidWorkBlock
---- Thrown if the supplied pow hash block is in the future or negative

---------
### MaxAllowedMaxMinRatioExceeded
---- Thrown when the dispatch attempts to set weights on chain with where the normalized
max value is more than MaxAllowedMaxMinRatio.

---------
### MaxWeightExceeded
---- Thrown when the dispatch attempts to set weights on chain with where any normalized
weight is more than MaxWeightLimit.

---------
### NonAssociatedColdKey
---- Thrown when a stake, unstake or subscribe request is made by a coldkey
which is not associated with the hotkey account. 
See: fn add_stake and fn remove_stake.

---------
### NoneValue
Error names should be descriptive.

---------
### NotEnoughBalanceToStake
 ---- Thrown when the caller requests adding more stake than there exists
in the cold key account. See: fn add_stake

---------
### NotEnoughStaketoWithdraw
---- Thrown when the caller requests removing more stake then there exists 
in the staking account. See: fn remove_stake.

---------
### NotRegistered
---- Thrown when the caller requests setting or removing data from
a neuron which does not exist in the active set.

---------
### NotSettingEnoughWeights
---- Thrown when the dispatch attempts to set weights on chain with fewer elements 
than are allowed.

---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------
### StorageValueOutOfRange
---- Thrown when the caller attempts to set a storage value outside of its allowed range.

---------
### ToManyRegistrationsThisBlock
---- Thrown when registrations this block exceeds allowed number.

---------
### WeightVecNotEqualSize
---- Thrown when the caller attempts to set the weight keys
and values but these vectors have different size.

---------
### WorkRepeated
---- Thrown when the caller attempts to use a repeated work.

---------