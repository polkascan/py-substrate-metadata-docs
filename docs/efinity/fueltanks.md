
# FuelTanks

---------
## Calls

---------
### add_account
Adds new account for `user_id` to fuel tank at `tank_id`. An account is
required to dispatch calls. A deposit is required, and may be paid by
the user or the fuel tank, depending on the settings.

\#\#\# Errors

- [`Error::FuelTankNotFound`] if fuel tank at `tank_id` does not exist
- [`Error::NoPermission`] if `origin` does not have permission to add an account
- [`Error::AccountAlreadyExists`] if account at `user_id` already exists
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| user_id | `LookupSourceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'add_account', {
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'user_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### batch_add_account
Similar to add_account but takes a list of
[`AccountId`](frame_system::Config::AccountId)s to insert into a fuel tank.
\#\#\# Errors
- [`Error::FuelTankNotFound`] if fuel tank at `tank_id` does not exist
- [`Error::NoPermission`] if `origin` does not have permission to add an account
- [`Error::AccountAlreadyExists`] if account at `user_id` already exists
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| user_ids | `BatchUserAccountsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'batch_add_account', {
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'user_ids': [
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ],
}
)
```

---------
### batch_remove_account
Similar to remove_account but takes a list of
[`AccountId`](frame_system::Config::AccountId)s to remove from a fuel tank.
\#\#\# Errors
- [`Error::FuelTankNotFound`] if fuel tank at `tank_id` does not exist
- [`Error::NoPermission`] if `origin` does not have permission to add an account
- [`Error::AccountNotFound`] if account at `user_id` does not exist
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| user_ids | `BatchUserAccountsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'batch_remove_account', {
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'user_ids': [
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ],
}
)
```

---------
### create_fuel_tank
Creates a fuel tank, given a descriptor

\# Errors

- [`Error::FuelTankAlreadyExists`] if `tank_id` already exists
- [`Error::DuplicateRuleKinds`] if a rule set has multiple rules of the same kind
#### Attributes
| Name | Type |
| -------- | -------- | 
| descriptor | `FuelTankDescriptorOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'create_fuel_tank', {
    'descriptor': {
        'account_rules': [
            {
                'RequireToken': {
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
                'WhitelistedCallers': 'scale_info::221',
            },
        ],
        'name': 'Bytes',
        'provides_deposit': 'bool',
        'rule_sets': 'scale_info::422',
        'user_account_management': (
            None,
            {
                'tank_reserves_account_creation_deposit': 'bool',
                'tank_reserves_existential_deposit': 'bool',
            },
        ),
    },
}
)
```

---------
### destroy_fuel_tank
Destroy the fuel tank by scheduling the deletion for `on_finalize` to execute
Only callable by owner
The fuel tank must be frozen
Can only be destroyed if all accounts are removed

\# Errors

- [`Error::FuelTankNotFound`] if tank_id does not exist
- [`Error::NoPermission`] if caller is not owner
- [`Error::DestroyUnfrozenTank`] if tank is not frozen
- [`Error::DestroyWithExistingAccounts`] if there are still accounts on the tank
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'destroy_fuel_tank', {
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### dispatch
Dispatch a call using the `tank_id` subject to the rules of `rule_set_id`

\# Errors
- [`Error::FuelTankNotFound`] if `tank_id` does not exist.
- [`Error::UsageRestricted`] if caller is not part of ruleset whitelist
- [`Error::CallerDoesNotHaveRuleSetTokenBalance`] if caller does not own the tokens to
  use the ruleset for remaining_fee when `pays_remaining_fee` is true
- [`Error::FuelTankOutOfFunds`] if the fuel tank account cannot pay fees
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `<T::Lookup as StaticLookup>::Source` | 
| rule_set_id | `T::RuleSetId` | 
| call | `Box<<T as Config>::Call>` | 
| pays_remaining_fee | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'dispatch', {
    'call': 'Call',
    'pays_remaining_fee': 'bool',
    'rule_set_id': 'u32',
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### dispatch_and_touch
Same as [dispatch](Self::dispatch), but creates an account for `origin` if it does not
exist and is allowed by the fuel tank&\#x27;s `user_account_management` settings.

\# Errors

Returns the same errors as [dispatch](Self::dispatch) and
[add_account](Self::add_account)
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `<T::Lookup as StaticLookup>::Source` | 
| rule_set_id | `T::RuleSetId` | 
| call | `Box<<T as Config>::Call>` | 
| pays_remaining_fee | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'dispatch_and_touch', {
    'call': 'Call',
    'pays_remaining_fee': 'bool',
    'rule_set_id': 'u32',
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### force_set_consumption
Force set the fuel tank consumption
If `user_id` is [`Some`], it sets the consumption for that account.
If it is [`None`], it sets the consumption on the fuel tank directly.

\# Errors

- [`Error::AccountNotFound`] if `user_id` is `Some` and account does not exist
- [`Error::FuelTankNotFound`] if tank_id does not exist
- [`Error::NoPermission`] if caller is not ForceOrigin or fuel tank owner
- [`Error::InvalidRuleSet`] if `rule_set_id` does not exist
- [`Error::MissingRequiredRule`] if `rule_set_id` does not have the required role
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| user_id | `Option<LookupSourceOf<T>>` | 
| rule_set_id | `T::RuleSetId` | 
| consumption | `ConsumptionOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'force_set_consumption', {
    'consumption': {
        'last_reset_block': (
            None,
            'u32',
        ),
        'total_consumed': 'u128',
    },
    'rule_set_id': 'u32',
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'user_id': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
}
)
```

---------
### insert_rule_set
Insert a new rule set for `tank_id` and `rule_set_id`. It can be a new rule set
or it can replace an existing one. If it is replacing a rule set, a rule that is storing
data on any accounts cannot be removed. Use [Self::remove_account_rule_data] to remove
the data first. If a rule is being replaced, it will be mutated with the new parameters,
and it will maintain any persistent data it already has.

This is only callable by the fuel tank&\#x27;s owner.
\#\#\# Errors
- [`Error::FuelTankNotFound`] if `tank_id` does not exist.
- [`Error::NoPermission`] if caller is not the fuel tank owner
- [`Error::RequiresFrozenTankOrRuleset`] if tank or rule set is not frozen
- [`Error::CannotRemoveRuleThatIsStoringAccountData`] if removing a rule that is storing
  account data
- [`Error::MaxRuleSetsExceeded`] if max number of rule sets was exceeded
- [`Error::DuplicateRuleKinds`] if adding a rule set with multiple rules of the same
  kind
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| rule_set_id | `T::RuleSetId` | 
| rules | `RuleDescriptorsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'insert_rule_set', {
    'rule_set_id': 'u32',
    'rules': [
        {
            'MaxFuelBurnPerTransaction': 'u128',
            'PermittedCalls': 'scale_info::414',
            'PermittedExtrinsics': [
                'Call',
            ],
            'RequireToken': {
                'collection_id': 'u128',
                'token_id': 'u128',
            },
            'TankFuelBudget': {
                'amount': 'u128',
                'reset_period': 'u32',
            },
            'UserFuelBudget': {
                'amount': 'u128',
                'reset_period': 'u32',
            },
            'WhitelistedCallers': 'scale_info::221',
            'WhitelistedCollections': 'scale_info::404',
        },
    ],
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### mutate_fuel_tank
Apply `mutation` to fuel tank with `tank_id`.

\# Errors

- [`Error::FuelTankNotFound`] if `tank_id` does not exist.
- [`Error::NoPermission`] if `origin` is not the fuel tank owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `<T::Lookup as StaticLookup>::Source` | 
| mutation | `T::TankMutation` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'mutate_fuel_tank', {
    'mutation': {
        'account_rules': (
            None,
            [
                {
                    'RequireToken': {
                        'collection_id': 'u128',
                        'token_id': 'u128',
                    },
                    'WhitelistedCallers': 'scale_info::221',
                },
            ],
        ),
        'provides_deposit': (
            None,
            'bool',
        ),
        'user_account_management': {
            'NoMutation': None,
            'SomeMutation': (
                None,
                {
                    'tank_reserves_account_creation_deposit': 'bool',
                    'tank_reserves_existential_deposit': 'bool',
                },
            ),
        },
    },
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_account
Removes account for `user_id` from fuel tank at `tank_id`. Any deposits
are returned.

\#\#\# Errors

- [`Error::FuelTankNotFound`] if fuel tank at `tank_id` does not exist
- [`Error::NoPermission`] if `origin` does not have permission to add an account
- [`Error::AccountNotFound`] if account at `user_id` does not exist
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| user_id | `LookupSourceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'remove_account', {
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'user_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_account_rule_data
Remove account rule data if it exists. Only callable by the fuel tank&\#x27;s owner. Requires
the fuel tank or the rule set to be frozen.

\#\#\# Errors

- [`Error::FuelTankNotFound`] if fuel tank for `tank_id` doesn&\#x27;t exist
- [`Error::NoPermission`] if called by non-owner
- [`Error::AccountNotFound`] if account does not exist for `user_id`
- [`Error::RuleSetNotFound`] if rule set does not exist for `rule_set_id`
- [`Error::RequiresFrozenTankOrRuleset`] if tank or rule set is not frozen
- [`Error::RuleNotFound`] if rule does not exist for `rule_kind`
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| user_id | `LookupSourceOf<T>` | 
| rule_set_id | `T::RuleSetId` | 
| rule_kind | `DispatchRuleKind` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'remove_account_rule_data', {
    'rule_kind': (
        'WhitelistedCallers',
        'WhitelistedCollections',
        'MaxFuelBurnPerTransaction',
        'UserFuelBudget',
        'TankFuelBudget',
        'RequireToken',
        'PermittedCalls',
        'PermittedExtrinsics',
    ),
    'rule_set_id': 'u32',
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'user_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_rule_set
Remove rule set for `tank_id` and `rule_set_id`. A rule that is storing data on
any accounts cannot be removed. Use [Self::remove_account_rule_data] to remove the
data first. This is only callable by the fuel tank&\#x27;s owner.
\# Errors

- [`Error::FuelTankNotFound`] if `tank_id` does not exist.
- [`Error::NoPermission`] if caller is not the fuel tank owner
- [`Error::RequiresFrozenTankOrRuleset`] if tank or rule set is not frozen
- [`Error::CannotRemoveRuleThatIsStoringAccountData`] if removing a rule that is storing
  account data
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `LookupSourceOf<T>` | 
| rule_set_id | `T::RuleSetId` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'remove_rule_set', {
    'rule_set_id': 'u32',
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### schedule_mutate_freeze_state
Schedule mutating of `is_frozen` state that determines if fuel tank or rule set can be
used

Additional 1 read and 1 write are added to account for `on_finalize` storage operations

\# Errors
- [`Error::FuelTankNotFound`] if `tank_id` does not exist.
- [`Error::NoPermission`] if caller is not a fuel tank owner
- [`Error::FreezeQueueFull`] if the queue is full
#### Attributes
| Name | Type |
| -------- | -------- | 
| tank_id | `<T::Lookup as StaticLookup>::Source` | 
| rule_set_id | `Option<T::RuleSetId>` | 
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'FuelTanks', 'schedule_mutate_freeze_state', {
    'is_frozen': 'bool',
    'rule_set_id': (None, 'u32'),
    'tank_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### AccountAdded
An account was added to a [`FuelTank`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| user_id | `T::AccountId` | ```AccountId```
| tank_deposit | `T::Balance` | ```u128```
| user_deposit | `T::Balance` | ```u128```

---------
### AccountRemoved
An account was removed from a [`FuelTank`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| user_id | `T::AccountId` | ```AccountId```

---------
### AccountRuleDataRemoved
Account data of [`AccountId`](frame_system::Config::AccountId) was removed from
[`RuleSetId`](Config::RuleSetId)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| user_id | `T::AccountId` | ```AccountId```
| rule_set_id | `T::RuleSetId` | ```u32```
| rule_kind | `DispatchRuleKind` | ```('WhitelistedCallers', 'WhitelistedCollections', 'MaxFuelBurnPerTransaction', 'UserFuelBudget', 'TankFuelBudget', 'RequireToken', 'PermittedCalls', 'PermittedExtrinsics')```

---------
### CallDispatched
A call was dispatched through a [`FuelTank`].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| caller | `T::AccountId` | ```AccountId```
| tank_id | `T::AccountId` | ```AccountId```

---------
### ConsumptionSet
The consumption for an account was set for a rule set on a [`FuelTank`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| user_id | `Option<T::AccountId>` | ```(None, 'AccountId')```
| rule_set_id | `T::RuleSetId` | ```u32```
| consumption | `ConsumptionOf<T>` | ```{'total_consumed': 'u128', 'last_reset_block': (None, 'u32')}```

---------
### DispatchFailed
The dispatch of a call has failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| caller | `T::AccountId` | ```AccountId```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### FreezeStateMutated
The freeze state change for fuel tank or its rule set was executed in `on_finalize`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| rule_set_id | `Option<T::RuleSetId>` | ```(None, 'u32')```
| is_frozen | `bool` | ```bool```

---------
### FuelTankCreated
A new [`FuelTank`] was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| name | `FuelTankNameOf<T>` | ```Bytes```
| tank_id | `T::AccountId` | ```AccountId```

---------
### FuelTankDestroyed
A [`FuelTank`] was destroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```

---------
### FuelTankMutated
A [`FuelTank`] was mutated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| mutation | `T::TankMutation` | ```{'user_account_management': {'NoMutation': None, 'SomeMutation': (None, {'tank_reserves_existential_deposit': 'bool', 'tank_reserves_account_creation_deposit': 'bool'})}, 'provides_deposit': (None, 'bool'), 'account_rules': (None, [{'WhitelistedCallers': 'scale_info::221', 'RequireToken': 'scale_info::222'}])}```

---------
### MutateFreezeStateScheduled
The freeze state mutation for fuel tank or its rule set was scheduled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| rule_set_id | `Option<T::RuleSetId>` | ```(None, 'u32')```
| is_frozen | `bool` | ```bool```

---------
### RuleSetInserted
A new rule set was added to [`FuelTank`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| rule_set_id | `T::RuleSetId` | ```u32```

---------
### RuleSetRemoved
A rule set was removed from [`FuelTank`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| rule_set_id | `T::RuleSetId` | ```u32```

---------
### ScheduleMutateFreezeStateFailed
The freeze state change for fuel tank or its rule set failed in `on_finalize`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tank_id | `T::AccountId` | ```AccountId```
| rule_set_id | `Option<T::RuleSetId>` | ```(None, 'u32')```
| is_frozen | `bool` | ```bool```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
## Storage functions

---------
### Accounts
 Mapping of Fuel Tanks and their user Accounts to account data

#### Python
```python
result = substrate.query(
    'FuelTanks', 'Accounts', ['AccountId', 'AccountId']
)
```

#### Return value
```python
{
    'rule_data_sets': 'scale_info::623',
    'tank_deposit': 'u128',
    'user_deposit': 'u128',
}
```
---------
### FreezeQueue
 The queue for fuel tank and rule set freezing
 Composed of (`tank_id`, `rule_set_id`, new `is_frozen` value)

#### Python
```python
result = substrate.query(
    'FuelTanks', 'FreezeQueue', []
)
```

#### Return value
```python
[{'is_frozen': 'bool', 'rule_set_id': (None, 'u32'), 'tank_id': 'AccountId'}]
```
---------
### Tanks
 Mapping of Fuel Tanks accounts to their data

#### Python
```python
result = substrate.query(
    'FuelTanks', 'Tanks', ['AccountId']
)
```

#### Return value
```python
{
    'account_count': 'u32',
    'account_rules': 'scale_info::610',
    'is_frozen': 'bool',
    'name': 'Bytes',
    'owner': 'AccountId',
    'provides_deposit': 'bool',
    'rule_sets': 'scale_info::604',
    'total_reserved': 'u128',
    'user_account_management': (
        None,
        {
            'tank_reserves_account_creation_deposit': 'bool',
            'tank_reserves_existential_deposit': 'bool',
        },
    ),
}
```
---------
## Constants

---------
### AccountCreationDeposit
 Deposit for creating an account
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'AccountCreationDeposit')
```
---------
### Levy
 The Levy applied to all transactions in Efinity.
#### Value
```python
750000000
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'Levy')
```
---------
### LevyScale
 value of a unit of the independant variable in EFI for the levy discount according to
 f(x) = (1/2)^x. Cannot be 0.
#### Value
```python
3000
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'LevyScale')
```
---------
### MaxAccountRuleDataLength
 Max length of data a rule can store per account
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxAccountRuleDataLength')
```
---------
### MaxBatchAccounts
 The maximum number of accounts for batch operations
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxBatchAccounts')
```
---------
### MaxCallFilters
 The maximum number of permitted calls
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxCallFilters')
```
---------
### MaxCallSize
 The maximum number of rule sets per fuel tank
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxCallSize')
```
---------
### MaxExtrinsicNameLength
 The maximum length for extrinsics for PermittedExtrinsic rule
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxExtrinsicNameLength')
```
---------
### MaxFreezeQueueLength
 The maximum number of fuel tank freeze state mutations that can be queued
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxFreezeQueueLength')
```
---------
### MaxFuelTankNameLength
 The maximum length for fuel tank name
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxFuelTankNameLength')
```
---------
### MaxPermittedExtrinsicLength
 The maximum number of extrinsics to allow for PermittedExtrinsic rule
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxPermittedExtrinsicLength')
```
---------
### MaxRuleSets
 The maximum number of rule sets per fuel tank
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxRuleSets')
```
---------
### MaxRulesPerSet
 Maximum number of rules in a ruleset
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxRulesPerSet')
```
---------
### MaxUserHistorySize
 The maximum number of user history that can be stored
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxUserHistorySize')
```
---------
### MaxWhitelistedCallers
 The maximum number of whitelisted callers per fuel tank
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxWhitelistedCallers')
```
---------
### MaxWhitelistedCollections
 Maximum number of whitelisted collections for a fuel tank
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'MaxWhitelistedCollections')
```
---------
### ReserveIdentifier
 The identifier used for currency reserves
#### Value
```python
'0x6675656c74616e6b'
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'ReserveIdentifier')
```
---------
### Salt
 The salt used for address generation
#### Value
```python
'0x6566696e69747979'
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'Salt')
```
---------
### TankCreationDeposit
 Deposit for creating a new fuel tank
#### Value
```python
10000000000000000000
```
#### Python
```python
constant = substrate.get_constant('FuelTanks', 'TankCreationDeposit')
```
---------
## Errors

---------
### AccountAlreadyExists
The account already exists

---------
### AccountContainsRuleData
A user cannot remove an account that is storing data for a rule

---------
### AccountNotFound
The account was not found

---------
### CallerDoesNotHaveRuleSetTokenBalance
The user does not have the token required by rule set

---------
### CannotRemoveRuleThatIsStoringAccountData
A rule cannot be removed from a rule set if it is storing data on any account

---------
### DecodeUserRuleDataFailed
The user rule data could not be decoded

---------
### DestroyUnfrozenTank
Destroying fuel tank is not possible while it is not frozen

---------
### DestroyWithExistingAccounts
Destroying fuel tank is not possible while it has existing accounts attached

---------
### DuplicateRuleKinds
A fuel tank cannot have more than one rule of the same kind

---------
### FreezeQueueFull
The queue for fuel tank and rule set freezing is full

---------
### FuelTankAlreadyExists
Fuel Tank already exists

---------
### FuelTankFrozen
The fuel tank is frozen

---------
### FuelTankNotFound
Fuel Tank not found

---------
### FuelTankOutOfFunds
Fuel tank doesnt have enough funds

---------
### InsufficientBalance
Not enough funds to perform operation

---------
### InvalidRuleSet
The rule set of the fuel tank is misconfigured. This error should never occur.

---------
### MaxRuleSetsExceeded
Max number of rules sets per fuel tank was exceeded

---------
### MintDepositCalculationError
Problems calculating the mint deposit for a call

---------
### MissingRequiredRule
A rule that is required for this operation does not exist

---------
### MissingRequiredRuleUserData
User data for the required rule does not exist

---------
### NoDataToRemove
The user does not have any data stored for rule set

---------
### NoPermission
User does not have permission to perform operation

---------
### RequiresFrozenTank
The fuel tank must be frozen for this operation

---------
### RequiresFrozenTankOrRuleset
Either the tank or ruleset must be frozen for this operation

---------
### RuleNotFound
The rule is missing

---------
### RuleSetNotFound
The rule set does not exist

---------
### UsageRestricted
Fuel tank cannot be used due to restrictions

---------
### UserRuleDataExceededMaxSize
The size of the user rule data is greater than the allowed amount

---------