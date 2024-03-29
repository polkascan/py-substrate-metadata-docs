
# OperationsWorkingGroupAlpha

---------
## Calls

---------
### add_opening
Add a job opening for a regular worker/lead role.
Require signed leader origin or the root (to add opening for the leader position).

\# &lt;weight&gt;

\#\# Weight
`O (D)` where:
- `D` is the size of `description` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| description | `Vec<u8>` | 
| opening_type | `OpeningType` | 
| stake_policy | `StakePolicy<T::BlockNumber, BalanceOf<T>>` | 
| reward_per_block | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'add_opening', {
    'description': 'Bytes',
    'opening_type': (
        'Leader',
        'Regular',
    ),
    'reward_per_block': (None, 'u128'),
    'stake_policy': {
        'leaving_unstaking_period': 'u32',
        'stake_amount': 'u128',
    },
}
)
```

---------
### apply_on_opening
Apply on a worker opening.

\# &lt;weight&gt;

\#\# Weight
`O (D)` where:
- `D` is the size of `p.description` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| p | `ApplyOnOpeningParameters<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'apply_on_opening', {
    'p': {
        'description': 'Bytes',
        'member_id': 'u64',
        'opening_id': 'u64',
        'reward_account_id': 'AccountId',
        'role_account_id': 'AccountId',
        'stake_parameters': {
            'stake': 'u128',
            'staking_account_id': 'AccountId',
        },
    },
}
)
```

---------
### cancel_opening
Cancel an opening for the regular worker/lead position.
Require signed leader origin or the root (to cancel opening for the leader position).

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| opening_id | `OpeningId` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'cancel_opening', {'opening_id': 'u64'}
)
```

---------
### decrease_stake
Decreases the regular worker/lead stake and returns the remainder to the
worker staking_account_id. Can be decreased to zero, no actions on zero stake.
Accepts the stake amount to decrease.
Requires signed leader origin or the root (to decrease the leader stake).

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| stake_balance_delta | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'decrease_stake', {
    'stake_balance_delta': 'u128',
    'worker_id': 'u64',
}
)
```

---------
### fill_opening
Fill opening for the regular/lead position.
Require signed leader origin or the root (to fill opening for the leader position).
\# &lt;weight&gt;

\#\# Weight
`O (A)` where:
- `A` is the length of `successful_application_ids`
- DB:
   - O(A)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| opening_id | `OpeningId` | 
| successful_application_ids | `BTreeSet<ApplicationId>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'fill_opening', {
    'opening_id': 'u64',
    'successful_application_ids': 'scale_info::90',
}
)
```

---------
### fund_working_group_budget
Fund working group budget by a member.
&lt;weight&gt;

\#\# Weight
`O (1)` Doesn&\#x27;t depend on the state or parameters
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `MemberId<T>` | 
| amount | `BalanceOf<T>` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'fund_working_group_budget', {
    'amount': 'u128',
    'member_id': 'u64',
    'rationale': 'Bytes',
}
)
```

---------
### increase_stake
Increases the regular worker/lead stake, demands a worker origin.
Locks tokens from the worker staking_account_id equal to new stake. No limits on the stake.

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| stake_balance_delta | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'increase_stake', {
    'stake_balance_delta': 'u128',
    'worker_id': 'u64',
}
)
```

---------
### lead_remark
Lead remark message

\# &lt;weight&gt;

\#\# Weight
`O (M)` where:
- `M` is the size of `msg` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'lead_remark', {'msg': 'Bytes'}
)
```

---------
### leave_role
Leave the role by the active worker.
\# &lt;weight&gt;

\#\# Weight
`O (R)` where:
- `R` is the size of `rationale` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| rationale | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'leave_role', {'rationale': (None, 'Bytes'), 'worker_id': 'u64'}
)
```

---------
### set_budget
Sets a new budget for the working group.
Requires root origin.

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_budget | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'set_budget', {'new_budget': 'u128'}
)
```

---------
### set_status_text
Sets a new status text for the working group.
Requires root origin.

\# &lt;weight&gt;

\#\# Weight
`O (S)` where:
- `S` is the size of the contents of `status_text` in kilobytes when it is not none

- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| status_text | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'set_status_text', {'status_text': (None, 'Bytes')}
)
```

---------
### slash_stake
Slashes the regular worker stake, demands a leader origin. No limits, no actions on zero stake.
If slashing balance greater than the existing stake - stake is slashed to zero.
Requires signed leader origin or the root (to slash the leader stake).
\# &lt;weight&gt;

\#\# Weight
`O (P)` where:
- `P` is the size of `penality.slashing_text` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| penalty | `BalanceOf<T>` | 
| rationale | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'slash_stake', {
    'penalty': 'u128',
    'rationale': (None, 'Bytes'),
    'worker_id': 'u64',
}
)
```

---------
### spend_from_budget
Transfers specified amount to any account.
Requires leader origin.

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| rationale | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'spend_from_budget', {
    'account_id': 'AccountId',
    'amount': 'u128',
    'rationale': (None, 'Bytes'),
}
)
```

---------
### terminate_role
Terminate the active worker by the lead.
Requires signed leader origin or the root (to terminate the leader role).
\# &lt;weight&gt;

\#\# Weight
`O (P)` where:
- `P` is the size `penalty.slashing_text` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| penalty | `Option<BalanceOf<T>>` | 
| rationale | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'terminate_role', {
    'penalty': (None, 'u128'),
    'rationale': (None, 'Bytes'),
    'worker_id': 'u64',
}
)
```

---------
### update_reward_account
Update the reward account associated with a set reward relationship for the active worker.

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| new_reward_account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'update_reward_account', {
    'new_reward_account_id': 'AccountId',
    'worker_id': 'u64',
}
)
```

---------
### update_reward_amount
Update the reward per block for the active worker.
Require signed leader origin or the root (to update leader&\#x27;s reward amount).

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| reward_per_block | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'update_reward_amount', {
    'reward_per_block': (None, 'u128'),
    'worker_id': 'u64',
}
)
```

---------
### update_role_account
Update the associated role account of the active regular worker/lead.

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| new_role_account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'update_role_account', {
    'new_role_account_id': 'AccountId',
    'worker_id': 'u64',
}
)
```

---------
### withdraw_application
Withdraw the worker application. Can be done by the worker only.

\# &lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| application_id | `ApplicationId` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'withdraw_application', {'application_id': 'u64'}
)
```

---------
### worker_remark
Worker remark message

\# &lt;weight&gt;

\#\# Weight
`O (M)` where:
- `M` is the size of `msg` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `WorkerId<T>` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'OperationsWorkingGroupAlpha', 'worker_remark', {'msg': 'Bytes', 'worker_id': 'u64'}
)
```

---------
## Events

---------
### ApplicationWithdrawn
Emits on withdrawing the application for the regular worker/lead opening.
Params:
- Job application id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ApplicationId` | ```u64```

---------
### AppliedOnOpening
Emits on adding the application for the worker opening.
Params:
- Opening parameteres
- Application id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ApplyOnOpeningParameters` | ```{'member_id': 'u64', 'opening_id': 'u64', 'role_account_id': 'AccountId', 'reward_account_id': 'AccountId', 'description': 'Bytes', 'stake_parameters': {'stake': 'u128', 'staking_account_id': 'AccountId'}}```
| None | `ApplicationId` | ```u64```

---------
### BudgetSet
Emits on setting the budget for the working group.
Params:
- new budget
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### BudgetSpending
Emits on budget from the working group being spent
Params:
- Receiver Account Id.
- Balance spent.
- Rationale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### LeadRemarked
Emits on Lead making a remark message
Params:
- message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### LeaderSet
Emits on setting the group leader.
Params:
- Group worker id.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```

---------
### LeaderUnset
Emits on un-setting the leader.
#### Attributes
No attributes

---------
### NewMissedRewardLevelReached
Emits on reaching new missed reward.
Params:
- Worker ID.
- Missed reward (optional). None means &\#x27;no missed reward&\#x27;.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Option<Balance>` | ```(None, 'u128')```

---------
### OpeningAdded
Emits on adding new job opening.
Params:
- Opening id
- Description
- Opening Type(Lead or Worker)
- Stake Policy for the opening
- Reward per block
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OpeningId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `OpeningType` | ```('Leader', 'Regular')```
| None | `StakePolicy` | ```{'stake_amount': 'u128', 'leaving_unstaking_period': 'u32'}```
| None | `Option<Balance>` | ```(None, 'u128')```

---------
### OpeningCanceled
Emits on canceling the job opening.
Params:
- Opening id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OpeningId` | ```u64```

---------
### OpeningFilled
Emits on filling the job opening.
Params:
- Worker opening id
- Worker application id to the worker id dictionary
- Applicationd ids used to fill the opening
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OpeningId` | ```u64```
| None | `ApplicationIdToWorkerIdMap` | ```scale_info::221```
| None | `BTreeSet<ApplicationId>` | ```scale_info::90```

---------
### RewardPaid
Emits on paying the reward.
Params:
- Id of the worker.
- Receiver Account Id.
- Reward
- Payment type (missed reward or regular one)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `RewardPaymentType` | ```('MissedReward', 'RegularReward')```

---------
### StakeDecreased
Emits on decreasing the regular worker/lead stake.
Params:
- regular worker/lead id.
- stake delta amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Balance` | ```u128```

---------
### StakeIncreased
Emits on increasing the regular worker/lead stake.
Params:
- regular worker/lead id.
- stake delta amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Balance` | ```u128```

---------
### StakeSlashed
Emits on slashing the regular worker/lead stake.
Params:
- regular worker/lead id.
- actual slashed balance.
- Requested slashed balance.
- Rationale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### StatusTextChanged
Emits on updating the status text of the working group.
Params:
- status text hash
- status text
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Hash` | ```scale_info::11```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### TerminatedLeader
Emits on terminating the leader.
Params:
- leader worker id.
- Penalty.
- Rationale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Option<Balance>` | ```(None, 'u128')```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### TerminatedWorker
Emits on terminating the worker.
Params:
- worker id.
- Penalty.
- Rationale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Option<Balance>` | ```(None, 'u128')```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### WorkerExited
Emits on exiting the worker.
Params:
- worker id.
- Rationale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```

---------
### WorkerRemarked
Emits on Lead making a remark message
Params:
- worker
- message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### WorkerRewardAccountUpdated
Emits on updating the reward account of the worker.
Params:
- Id of the worker.
- Reward account id of the worker.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `AccountId` | ```AccountId```

---------
### WorkerRewardAmountUpdated
Emits on updating the reward amount of the worker.
Params:
- Id of the worker.
- Reward per block
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Option<Balance>` | ```(None, 'u128')```

---------
### WorkerRoleAccountUpdated
Emits on updating the role account of the worker.
Params:
- Id of the worker.
- Role account id of the worker.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `AccountId` | ```AccountId```

---------
### WorkerStartedLeaving
Emits when worker started leaving their role.
Params:
- Worker id.
- Rationale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkerId` | ```u64```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### WorkingGroupBudgetFunded
Fund the working group budget.
Params:
- Member ID
- Amount of balance
- Rationale
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### ActiveWorkerCount
 Count of active workers.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'ActiveWorkerCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ApplicationById
 Maps identifier to worker application on opening.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'ApplicationById', ['u64']
)
```

#### Return value
```python
{
    'description_hash': 'scale_info::11',
    'member_id': 'u64',
    'opening_id': 'u64',
    'reward_account_id': 'AccountId',
    'role_account_id': 'AccountId',
    'staking_account_id': 'AccountId',
}
```
---------
### Budget
 Budget for the working group.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'Budget', []
)
```

#### Return value
```python
'u128'
```
---------
### CurrentLead
 Current group lead.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'CurrentLead', []
)
```

#### Return value
```python
'u64'
```
---------
### NextApplicationId
 Next identifier value for new worker application.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'NextApplicationId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextOpeningId
 Next identifier value for new job opening.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'NextOpeningId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextWorkerId
 Next identifier for a new worker.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'NextWorkerId', []
)
```

#### Return value
```python
'u64'
```
---------
### OpeningById
 Maps identifier to job opening.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'OpeningById', ['u64']
)
```

#### Return value
```python
{
    'created': 'u32',
    'creation_stake': 'u128',
    'description_hash': 'scale_info::11',
    'opening_type': ('Leader', 'Regular'),
    'reward_per_block': (None, 'u128'),
    'stake_policy': {
        'leaving_unstaking_period': 'u32',
        'stake_amount': 'u128',
    },
}
```
---------
### StatusTextHash
 Status text hash.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'StatusTextHash', []
)
```

#### Return value
```python
'scale_info::11'
```
---------
### WorkerById
 Maps identifier to corresponding worker.

#### Python
```python
result = substrate.query(
    'OperationsWorkingGroupAlpha', 'WorkerById', ['u64']
)
```

#### Return value
```python
{
    'created_at': 'u32',
    'job_unstaking_period': 'u32',
    'member_id': 'u64',
    'missed_reward': (None, 'u128'),
    'reward_account_id': 'AccountId',
    'reward_per_block': (None, 'u128'),
    'role_account_id': 'AccountId',
    'staking_account_id': 'AccountId',
    'started_leaving_at': (None, 'u32'),
}
```
---------
## Constants

---------
### LeaderOpeningStake
 Stake needed to create an opening.
#### Value
```python
16666666666600
```
#### Python
```python
constant = substrate.get_constant('OperationsWorkingGroupAlpha', 'LeaderOpeningStake')
```
---------
### MaxWorkerNumberLimit
 Exports const
 Max simultaneous active worker number.
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('OperationsWorkingGroupAlpha', 'MaxWorkerNumberLimit')
```
---------
### MinUnstakingPeriodLimit
 Defines min unstaking period in the group.
#### Value
```python
288000
```
#### Python
```python
constant = substrate.get_constant('OperationsWorkingGroupAlpha', 'MinUnstakingPeriodLimit')
```
---------
### MinimumApplicationStake
 Minimum stake required for applying into an opening.
#### Value
```python
3333333333320
```
#### Python
```python
constant = substrate.get_constant('OperationsWorkingGroupAlpha', 'MinimumApplicationStake')
```
---------
### RewardPeriod
 Defines the period every worker gets paid in blocks.
#### Value
```python
14460
```
#### Python
```python
constant = substrate.get_constant('OperationsWorkingGroupAlpha', 'RewardPeriod')
```
---------
### StakingHandlerLockId
 Staking handler lock id.
#### Value
```python
'0x77672d6f70657261'
```
#### Python
```python
constant = substrate.get_constant('OperationsWorkingGroupAlpha', 'StakingHandlerLockId')
```
---------
## Errors

---------
### ApplicationStakeDoesntMatchOpening
Application stake is less than required opening stake.

---------
### ApplicationsNotForOpening
Trying to fill opening with an application for other opening

---------
### ArithmeticError
Unexpected arithmetic error (overflow / underflow)

---------
### BelowMinimumStakes
Staking less than the lower bound.

---------
### CannotDecreaseStakeDeltaGreaterThanStake
Cannot decrease stake - stake delta greater than initial stake.

---------
### CannotHireLeaderWhenLeaderExists
There is leader already, cannot hire another one.

---------
### CannotHireMultipleLeaders
Cannot fill opening with multiple applications.

---------
### CannotRewardWithZero
Reward could not be zero.

---------
### CannotSpendZero
Invalid spending amount.

---------
### ConflictStakesOnAccount
Staking account contains conflicting stakes.

---------
### CurrentLeadNotSet
Current lead is not set.

---------
### InsufficientBalanceForTransfer
Cannot withdraw: insufficient budget balance.

---------
### InsufficientBalanceToCoverStake
Insufficient balance to cover stake.

---------
### InsufficientBudgetForSpending
It&\#x27;s not enough budget for this spending.

---------
### InsufficientTokensForFunding
Insufficient tokens for funding (on member controller account)

---------
### InvalidMemberOrigin
Invalid origin for a member.

---------
### InvalidStakingAccountForMember
Staking account doesn&\#x27;t belong to a member.

---------
### IsNotLeadAccount
Not a lead account.

---------
### MaxActiveWorkerNumberExceeded
Working group size limit exceeded.

---------
### NoApplicationsProvided
Cannot fill opening - no applications provided.

---------
### OpeningDoesNotExist
Opening does not exist.

---------
### OriginIsNotApplicant
Origin is not applicant.

---------
### SignerIsNotWorkerRoleAccount
Signer is not worker role account.

---------
### StakeBalanceCannotBeZero
Provided stake balance cannot be zero.

---------
### SuccessfulWorkerApplicationDoesNotExist
Successful worker application does not exist.

---------
### UnstakingPeriodLessThanMinimum
Specified unstaking period is less then minimum set for the group.

---------
### WorkerApplicationDoesNotExist
Worker application does not exist.

---------
### WorkerDoesNotExist
Worker does not exist.

---------
### WorkerHasNoReward
Worker has no recurring reward.

---------
### WorkerIsLeaving
Invalid operation - worker is leaving.

---------
### WorkerStorageValueTooLong
Worker storage text is too long.

---------
### ZeroTokensFunding
Trying to fund with zero tokens

---------