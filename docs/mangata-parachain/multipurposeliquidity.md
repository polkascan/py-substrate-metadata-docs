
# MultiPurposeLiquidity

---------
## Calls

---------
### reserve_vesting_liquidity_tokens
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 
| liquidity_token_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'MultiPurposeLiquidity', 'reserve_vesting_liquidity_tokens', {
    'liquidity_token_amount': 'u128',
    'liquidity_token_id': 'u32',
}
)
```

---------
### reserve_vesting_liquidity_tokens_by_vesting_index
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 
| liquidity_token_vesting_index | `u32` | 
| liquidity_token_unlock_some_amount_or_all | `Option<Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiPurposeLiquidity', 'reserve_vesting_liquidity_tokens_by_vesting_index', {
    'liquidity_token_id': 'u32',
    'liquidity_token_unlock_some_amount_or_all': (
        None,
        'u128',
    ),
    'liquidity_token_vesting_index': 'u32',
}
)
```

---------
### unreserve_and_relock_instance
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 
| relock_instance_index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'MultiPurposeLiquidity', 'unreserve_and_relock_instance', {
    'liquidity_token_id': 'u32',
    'relock_instance_index': 'u32',
}
)
```

---------
## Events

---------
### TokensRelockedFromReserve
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### VestingTokensReserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### RelockStatus

#### Python
```python
result = substrate.query(
    'MultiPurposeLiquidity', 'RelockStatus', ['AccountId', 'u32']
)
```

#### Return value
```python
[
    {
        'amount': 'u128',
        'ending_block_as_balance': 'u128',
        'starting_block': 'u32',
    },
]
```
---------
### ReserveStatus

#### Python
```python
result = substrate.query(
    'MultiPurposeLiquidity', 'ReserveStatus', ['AccountId', 'u32']
)
```

#### Return value
```python
{
    'activated_unstaked_reserves': 'u128',
    'relock_amount': 'u128',
    'staked_and_activated_reserves': 'u128',
    'staked_unactivated_reserves': 'u128',
    'unspent_reserves': 'u128',
}
```
---------
## Errors

---------
### MathError
Math error

---------
### NotALiquidityToken
The token is not a liquidity token

---------
### NotEnoughTokens
Not enough tokens

---------
### NotEnoughUnspentReserves
Not enough unspend reserves

---------
### RelockCountLimitExceeded
The limit on the maximum number of relocks was exceeded

---------
### RelockInstanceIndexOOB
Provided index for relock is out of bounds

---------