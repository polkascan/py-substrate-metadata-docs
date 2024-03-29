
# BlockRewards

---------
## Calls

---------
### claim_reward
Claims the reward the associated to a currency.
The reward will be transferred to the target account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'BlockRewards', 'claim_reward', {'account_id': 'AccountId'}
)
```

---------
### set_annual_treasury_inflation_rate
Admin method to set the treasury inflation rate for the next
sessions. Current session is not affected by this call.
#### Attributes
| Name | Type |
| -------- | -------- | 
| treasury_inflation_rate | `T::Rate` | 

#### Python
```python
call = substrate.compose_call(
    'BlockRewards', 'set_annual_treasury_inflation_rate', {'treasury_inflation_rate': 'u128'}
)
```

---------
### set_collator_reward_per_session
Admin method to set the reward amount for a collator used for the
next sessions. Current session is not affected by this call.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator_reward_per_session | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'BlockRewards', 'set_collator_reward_per_session', {
    'collator_reward_per_session': 'u128',
}
)
```

---------
## Events

---------
### NewSession
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collator_reward | `T::Balance` | ```u128```
| treasury_inflation_rate | `T::Rate` | ```u128```
| last_changes | `SessionChanges<T>` | ```{'collators': {'inc': ['AccountId'], 'out': ['AccountId']}, 'collator_count': (None, 'u32'), 'collator_reward': (None, 'u128'), 'treasury_inflation_rate': (None, 'u128'), 'last_update': 'u64'}```

---------
### SessionAdvancementFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```

---------
## Storage functions

---------
### ActiveSessionData
 Data associated to the current session.

#### Python
```python
result = substrate.query(
    'BlockRewards', 'ActiveSessionData', []
)
```

#### Return value
```python
{
    'collator_count': 'u32',
    'collator_reward': 'u128',
    'last_update': 'u64',
    'treasury_inflation_rate': 'u128',
}
```
---------
### NextSessionChanges
 Pending update data used when the current session finalizes.
 Once it&#x27;s used for the update, it&#x27;s reset.

#### Python
```python
result = substrate.query(
    'BlockRewards', 'NextSessionChanges', []
)
```

#### Return value
```python
{
    'collator_count': (None, 'u32'),
    'collator_reward': (None, 'u128'),
    'collators': {'inc': ['AccountId'], 'out': ['AccountId']},
    'last_update': 'u64',
    'treasury_inflation_rate': (None, 'u128'),
}
```
---------
## Constants

---------
### ExistentialDeposit
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('BlockRewards', 'ExistentialDeposit')
```
---------
### MaxCollators
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('BlockRewards', 'MaxCollators')
```
---------
### StakeAmount
 The amount of the artificial block rewards currency which is minted
 and burned for collators.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('BlockRewards', 'StakeAmount')
```
---------
### StakeCurrencyId
 The identifier of the artificial block rewards currency which is
 minted and burned for collators.
#### Value
```python
{'Staking': 'BlockRewards'}
```
#### Python
```python
constant = substrate.get_constant('BlockRewards', 'StakeCurrencyId')
```
---------
### StakeGroupId
 The identifier of the collator group.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('BlockRewards', 'StakeGroupId')
```
---------