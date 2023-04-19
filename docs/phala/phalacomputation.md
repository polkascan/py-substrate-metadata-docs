
# PhalaComputation

---------
## Calls

---------
### force_heartbeat
Triggers a force heartbeat request to all workers by sending a MAX pow target

Only for integration test.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'force_heartbeat', {}
)
```

---------
### force_start_computing
Start computing

Only for integration test.
#### Attributes
| Name | Type |
| -------- | -------- | 
| session | `T::AccountId` | 
| stake | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'force_start_computing', {
    'session': 'AccountId',
    'stake': 'u128',
}
)
```

---------
### force_stop_computing
Stop computing

Only for integration test.
#### Attributes
| Name | Type |
| -------- | -------- | 
| session | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'force_stop_computing', {'session': 'AccountId'}
)
```

---------
### set_budget_per_block
#### Attributes
| Name | Type |
| -------- | -------- | 
| nonce | `u64` | 
| block_number | `T::BlockNumber` | 
| budget | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'set_budget_per_block', {
    'block_number': 'u32',
    'budget': 'u128',
    'nonce': 'u64',
}
)
```

---------
### set_cool_down_expiration
Sets the cool down expiration time in seconds.

Can only be called by root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| period | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'set_cool_down_expiration', {'period': 'u64'}
)
```

---------
### set_heartbeat_paused
Pause or resume the heartbeat challenges.

This API is introduced to pause the computing rewards for a period while we upgrading
StakePool v2. Worker&\#x27;s rewards would still be accumulated in GK in the pausing period
but never be paid out until the heartbeat is resumed.

Can only be called by root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| paused | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'set_heartbeat_paused', {'paused': 'bool'}
)
```

---------
### unbind
Unbinds a worker from the given session (or pool sub-account).

It will trigger a force stop of computing if the worker is still in computing state. Anyone
can call it.
#### Attributes
| Name | Type |
| -------- | -------- | 
| session | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'unbind', {'session': 'AccountId'}
)
```

---------
### update_contract_root
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `AccountId32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'update_contract_root', {'account_id': 'AccountId'}
)
```

---------
### update_tokenomic
Updates the tokenomic parameters at the end of this block.

Can only be called by the tokenomic admin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_params | `TokenomicParams` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaComputation', 'update_tokenomic', {
    'new_params': {
        'budget_per_block': 'u128',
        'cost_b': 'u128',
        'cost_k': 'u128',
        'heartbeat_window': 'u32',
        'k': 'u128',
        'kappa': 'u128',
        'pha_rate': 'u128',
        're': 'u128',
        'rho': 'u128',
        'rig_b': 'u128',
        'rig_k': 'u128',
        'slash_rate': 'u128',
        'treasury_ratio': 'u128',
        'v_max': 'u128',
    },
}
)
```

---------
## Events

---------
### BenchmarkUpdated
Benchmark Updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```
| p_instant | `u32` | ```u32```

---------
### BudgetUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nonce | `u64` | ```u64```
| budget | `u128` | ```u128```

---------
### CoolDownExpirationChanged
Cool down expiration changed (in sec).

Indicates a change in [`CoolDownPeriod`].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| period | `u64` | ```u64```

---------
### InternalErrorWorkerSettleFailed
Some internal error happened when settling a worker&\#x27;s ledger.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| worker | `WorkerPublicKey` | ```[u8; 32]```

---------
### InternalErrorWrongHalvingConfigured
Some internal error happened when trying to halve the subsidy
#### Attributes
No attributes

---------
### SessionBound
Worker &amp; session are bounded.

Affected states:
- [`SessionBindings`] for the session account is pointed to the worker
- [`WorkerBindings`] for the worker is pointed to the session account
- the worker info at [`Sessions`] is updated with `Ready` state
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```
| worker | `WorkerPublicKey` | ```[u8; 32]```

---------
### SessionSettled
Worker settled successfully.

It results in the v in [`Sessions`] being updated. It also indicates the downstream
stake pool has received the computing reward (payout), and the treasury has received the
tax.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```
| v_bits | `u128` | ```u128```
| payout_bits | `u128` | ```u128```

---------
### SessionSettlementDropped
A session settlement was dropped because the on-chain version is more up-to-date.

This is a temporary walk-around of the computing staking design. Will be fixed by
StakePool v2.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```
| v | `u128` | ```u128```
| payout | `u128` | ```u128```

---------
### SessionUnbound
Worker &amp; worker are unbound.

Affected states:
- [`SessionBindings`] for the session account is removed
- [`WorkerBindings`] for the worker is removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```
| worker | `WorkerPublicKey` | ```[u8; 32]```

---------
### SubsidyBudgetHalved
Block subsidy halved by 25%.

This event will be followed by a [`TokenomicParametersChanged`](\#variant.TokenomicParametersChanged)
event indicating the change of the block subsidy budget in the parameter.
#### Attributes
No attributes

---------
### TokenomicParametersChanged
Tokenomic parameter changed.

Affected states:
- [`TokenomicParameters`] is updated.
#### Attributes
No attributes

---------
### WorkerEnterUnresponsive
Worker enters unresponsive state.

Affected states:
- the worker info at [`Sessions`] is updated from `WorkerIdle` to `WorkerUnresponsive`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```

---------
### WorkerExitUnresponsive
Worker returns to responsive state.

Affected states:
- the worker info at [`Sessions`] is updated from `WorkerUnresponsive` to `WorkerIdle`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```

---------
### WorkerReclaimed
Worker is reclaimed, with its slash settled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```
| original_stake | `BalanceOf<T>` | ```u128```
| slashed | `BalanceOf<T>` | ```u128```

---------
### WorkerStarted
A worker starts computing.

Affected states:
- the worker info at [`Sessions`] is updated with `WorkerIdle` state
- [`NextSessionId`] for the session is incremented
- [`Stakes`] for the session is updated
- [`OnlineWorkers`] is incremented
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```
| init_v | `u128` | ```u128```
| init_p | `u32` | ```u32```

---------
### WorkerStopped
Worker stops computing.

Affected states:
- the worker info at [`Sessions`] is updated with `WorkerCoolingDown` state
- [`OnlineWorkers`] is decremented
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### BudgetUpdateNonce

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'BudgetUpdateNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### ComputingHalvingInterval
 The interval of halving (75% decay) in block number.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'ComputingHalvingInterval', []
)
```

#### Return value
```python
'u32'
```
---------
### ComputingStartBlock
 The block number when the computing starts. Used to calculate halving.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'ComputingStartBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### ContractAccount

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'ContractAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### CoolDownPeriod
 The cool down period (in sec)

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'CoolDownPeriod', []
)
```

#### Return value
```python
'u64'
```
---------
### ExpectedHeartbeatCount
 The expected heartbeat count at every block (default: 20)

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'ExpectedHeartbeatCount', []
)
```

#### Return value
```python
'u32'
```
---------
### HeartbeatPaused
 Won&#x27;t sent heartbeat challenges to the the worker if enabled.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'HeartbeatPaused', []
)
```

#### Return value
```python
'bool'
```
---------
### LastBugdetUpdateBlock

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'LastBugdetUpdateBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxBudgetLimit

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'MaxBudgetLimit', []
)
```

#### Return value
```python
'u128'
```
---------
### NextSessionId
 The next id to assign to a computing session

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'NextSessionId', []
)
```

#### Return value
```python
'u32'
```
---------
### OnlineWorkers
 Total online workers including WorkerIdle and WorkerUnresponsive workers.

 Increased when a worker is turned to WorkerIdle; decreased when turned to CoolingDown.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'OnlineWorkers', []
)
```

#### Return value
```python
'u32'
```
---------
### ScheduledTokenomicUpdate
 The scheduled new tokenomic params to update at the end of this block.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'ScheduledTokenomicUpdate', []
)
```

#### Return value
```python
{
    'budget_per_block': 'u128',
    'cost_b': 'u128',
    'cost_k': 'u128',
    'heartbeat_window': 'u32',
    'k': 'u128',
    'kappa': 'u128',
    'pha_rate': 'u128',
    're': 'u128',
    'rho': 'u128',
    'rig_b': 'u128',
    'rig_k': 'u128',
    'slash_rate': 'u128',
    'treasury_ratio': 'u128',
    'v_max': 'u128',
}
```
---------
### SessionBindings
 The bound worker for a session account

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'SessionBindings', ['AccountId']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### Sessions
 The miner state.

 The session state is created when a worker is bounded with a session, but it will be kept even
 if the worker is force unbound. A re-bind of a worker will reset the computing state.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'Sessions', ['AccountId']
)
```

#### Return value
```python
{
    'benchmark': {
        'challenge_time_last': 'u64',
        'iterations': 'u64',
        'p_init': 'u32',
        'p_instant': 'u32',
        'working_start_time': 'u64',
    },
    'cool_down_start': 'u64',
    'state': (
        'Ready',
        'WorkerIdle',
        '_Unused',
        'WorkerUnresponsive',
        'WorkerCoolingDown',
    ),
    'stats': {'total_reward': 'u128'},
    'v': 'u128',
    'v_updated_at': 'u64',
    've': 'u128',
}
```
---------
### Stakes
 The stakes of session accounts.

 Only presents for computing and cooling down sessions.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'Stakes', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### TokenomicParameters
 Tokenomic parameters used by Gatekeepers to compute the V promote.

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'TokenomicParameters', []
)
```

#### Return value
```python
{
    'budget_per_block': 'u128',
    'cost_b': 'u128',
    'cost_k': 'u128',
    'heartbeat_window': 'u32',
    'k': 'u128',
    'kappa': 'u128',
    'pha_rate': 'u128',
    're': 'u128',
    'rho': 'u128',
    'rig_b': 'u128',
    'rig_k': 'u128',
    'slash_rate': 'u128',
    'treasury_ratio': 'u128',
    'v_max': 'u128',
}
```
---------
### WorkerBindings
 The bound worker account for a worker

#### Python
```python
result = substrate.query(
    'PhalaComputation', 'WorkerBindings', ['[u8; 32]']
)
```

#### Return value
```python
'AccountId'
```
---------
## Errors

---------
### BadSender
The transaction is sent by an unauthorized sender

---------
### BenchmarkMissing
There&\#x27;s no benchmark result on the blockchain.

---------
### BenchmarkTooLow
Indicating the initial benchmark score is too low to start computing.

---------
### BudgetExceedMaxLimit

---------
### BudgetUpdateBlockInvalid

---------
### CoolDownNotReady
Cannot reclaim the worker because it&\#x27;s still in cooldown period.

---------
### DuplicateBoundSession
Not permitted because the session is already bound with another worker.

---------
### DuplicateBoundWorker
Not permitted because the worker is already bound with another session account.

---------
### InsufficientStake
Cannot start computing because there&\#x27;s too little stake.

---------
### InternalErrorBadTokenomicParameters
Internal error. The tokenomic parameter is not set.

---------
### InternalErrorCannotStartWithExistingStake
Internal error. A worker should never start with existing stake in the storage.

---------
### NonceIndexInvalid

---------
### NotMigrationRoot
Migration root not authorized

---------
### SessionNotBound
Not permitted because the session is not bound with a worker.

---------
### SessionNotFound
session not found.

---------
### TooMuchStake
Cannot start computing because there&\#x27;s too much stake (exceeds Vmax).

---------
### WorkerNotBound
Not permitted because the worker is not bound with a worker account.

---------
### WorkerNotComputing
Worker is not in `Computation` state to stop computing.

---------
### WorkerNotReady
Worker is not in `Ready` state to proceed.

---------
### WorkerNotRegistered
The worker is not registered in the registry.

---------
### _GatekeeperNotRegistered
Deprecated

---------
### _InvalidMessage
Deprecated.

---------