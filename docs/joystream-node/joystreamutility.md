
# JoystreamUtility

---------
## Calls

---------
### burn_account_tokens
Burns token for caller account
&lt;weight&gt;

\#\# Weight
`O (1)` Doesn&\#x27;t depend on the state or parameters
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'JoystreamUtility', 'burn_account_tokens', {'amount': 'u128'}
)
```

---------
### execute_runtime_upgrade_proposal
Runtime upgrade proposal extrinsic.
Should be used as callable object to pass to the `engine` module.
&lt;weight&gt;

\#\# Weight
`O (C)` where:
- `C` is the length of `wasm`
However, we treat this as a full block as `frame_system::Module::set_code` does
\# &lt;/weight&gt;
\#[weight = (T::BlockWeights::get().get(DispatchClass::Operational).base_extrinsic, DispatchClass::Operational)]
#### Attributes
| Name | Type |
| -------- | -------- | 
| wasm | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'JoystreamUtility', 'execute_runtime_upgrade_proposal', {'wasm': 'Bytes'}
)
```

---------
### execute_signal_proposal
Signal proposal extrinsic. Should be used as callable object to pass to the `engine` module.

&lt;weight&gt;

\#\# Weight
`O (S)` where:
- `S` is the size of the signal in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| signal | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'JoystreamUtility', 'execute_signal_proposal', {'signal': 'Bytes'}
)
```

---------
### update_working_group_budget
Update working group budget
&lt;weight&gt;

\#\# Weight
`O (1)` Doesn&\#x27;t depend on the state or parameters
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| working_group | `WorkingGroup` | 
| amount | `BalanceOf<T>` | 
| balance_kind | `BalanceKind` | 

#### Python
```python
call = substrate.compose_call(
    'JoystreamUtility', 'update_working_group_budget', {
    'amount': 'u128',
    'balance_kind': (
        'Positive',
        'Negative',
    ),
    'working_group': (
        'Forum',
        'Storage',
        'Content',
        'OperationsAlpha',
        'App',
        'Distribution',
        'OperationsBeta',
        'OperationsGamma',
        'Membership',
    ),
}
)
```

---------
## Events

---------
### RuntimeUpgraded
A runtime upgrade was executed
Params:
- New code encoded in bytes
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### Signaled
A signal proposal was executed
Params:
- Signal given when creating the corresponding proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### TokensBurned
An account burned tokens
Params:
- Account Id of the burning tokens
- Balance burned from that account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### UpdatedWorkingGroupBudget
An `Update Working Group Budget` proposal was executed
Params:
- Working group which budget is being updated
- Amount of balance being moved
- Enum variant with positive indicating funds moved torwards working group and negative
and negative funds moving from the working group
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `WorkingGroup` | ```('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')```
| None | `Balance` | ```u128```
| None | `BalanceKind` | ```('Positive', 'Negative')```

---------
## Storage functions

---------
## Errors

---------
### InsufficientFundsForBudgetUpdate
Insufficient funds for &\#x27;Update Working Group Budget&\#x27; proposal execution

---------
### InsufficientFundsForBurn
Insufficient funds for burning

---------
### ZeroTokensBurn
Trying to burn zero tokens

---------