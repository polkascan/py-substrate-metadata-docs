
# LighteningRedeem

---------
## Calls

---------
### add_ksm_to_pool
Anyone can add KSM to the pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LighteningRedeem', 'add_ksm_to_pool', {'token_amount': 'u128'}
)
```

---------
### edit_exchange_price
#### Attributes
| Name | Type |
| -------- | -------- | 
| price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LighteningRedeem', 'edit_exchange_price', {'price': 'u128'}
)
```

---------
### edit_release_per_day
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_per_day | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LighteningRedeem', 'edit_release_per_day', {'amount_per_day': 'u128'}
)
```

---------
### edit_release_start_and_end_block
#### Attributes
| Name | Type |
| -------- | -------- | 
| start | `BlockNumberFor<T>` | 
| end | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LighteningRedeem', 'edit_release_start_and_end_block', {'end': 'u32', 'start': 'u32'}
)
```

---------
### exchange_for_ksm
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LighteningRedeem', 'exchange_for_ksm', {'token_amount': 'u128'}
)
```

---------
## Events

---------
### BlockIntervalEdited
[start, end]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BlockNumberFor<T>` | ```u32```
| None | `BlockNumberFor<T>` | ```u32```

---------
### KSMAdded
[adder, ksm_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### KSMExchanged
[exchanger, ksm_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### PriceEdited
[original_prce, new_price]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### ReleasedPerDayEdited
[originla_amount_per_day, amount_per_day]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ExchangePriceDiscount
 Exchange price discount: vsbond + vstoken =&gt; token

#### Python
```python
result = substrate.query(
    'LighteningRedeem', 'ExchangePriceDiscount', []
)
```

#### Return value
```python
'u8'
```
---------
### PoolAmount
 The remaining amount which can be exchanged for

#### Python
```python
result = substrate.query(
    'LighteningRedeem', 'PoolAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### StartEndReleaseBlock
 Token release start block

#### Python
```python
result = substrate.query(
    'LighteningRedeem', 'StartEndReleaseBlock', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### TokenReleasePerDay
 token amount that is released everyday.

#### Python
```python
result = substrate.query(
    'LighteningRedeem', 'TokenReleasePerDay', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### PalletId
 ModuleID for creating sub account
#### Value
```python
'0x62662f6c746e7264'
```
#### Python
```python
constant = substrate.get_constant('LighteningRedeem', 'PalletId')
```
---------
## Errors

---------
### DenominatorZero

---------
### ExceedPoolAmount

---------
### InvalidReleaseInterval

---------
### NotEnoughBalance

---------
### NotGreaterThanZero

---------
### NotKSM

---------
### Overflow

---------