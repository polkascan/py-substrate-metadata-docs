
# TreasuryReward

---------
## Calls

---------
### set_current_payout
Sets the fixed treasury payout per minting interval.
#### Attributes
| Name | Type |
| -------- | -------- | 
| payout | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryReward', 'set_current_payout', {'payout': 'u128'}
)
```

---------
### set_minting_interval
Sets the treasury minting interval.
#### Attributes
| Name | Type |
| -------- | -------- | 
| interval | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryReward', 'set_minting_interval', {'interval': 'u32'}
)
```

---------
## Events

---------
### TreasuryMinting
Treasury minting event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Balance` | ```u128```
| None | `T::BlockNumber` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### CurrentPayout
 The next tree identifier up for grabs

#### Python
```python
result = substrate.query(
    'TreasuryReward', 'CurrentPayout', []
)
```

#### Return value
```python
'u128'
```
---------
### MintingInterval
 The next tree identifier up for grabs

#### Python
```python
result = substrate.query(
    'TreasuryReward', 'MintingInterval', []
)
```

#### Return value
```python
'u32'
```
---------