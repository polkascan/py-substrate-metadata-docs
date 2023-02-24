
# AMMRoute

---------
## Calls

---------
### swap_exact_tokens_for_tokens
Given input amount is fixed, the output token amount is not known in advance.

- `origin`: the trader.
- `route`: the route user inputs
- `amount_in`: the amount of trading assets
- `min_amount_out`: the minimum a trader is willing to receive
#### Attributes
| Name | Type |
| -------- | -------- | 
| route | `Vec<AssetIdOf<T, I>>` | 
| amount_in | `BalanceOf<T, I>` | 
| min_amount_out | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'AMMRoute', 'swap_exact_tokens_for_tokens', {
    'amount_in': 'u128',
    'min_amount_out': 'u128',
    'route': ['u32'],
}
)
```

---------
### swap_tokens_for_exact_tokens
Given the output token amount is fixed, the input token amount is not known.

- `origin`: the trader.
- `route`: the route user inputs
- `amount_out`: the amount of trading assets
- `max_amount_in`: the maximum a trader is willing to input
#### Attributes
| Name | Type |
| -------- | -------- | 
| route | `Vec<AssetIdOf<T, I>>` | 
| amount_out | `BalanceOf<T, I>` | 
| max_amount_in | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'AMMRoute', 'swap_tokens_for_exact_tokens', {
    'amount_out': 'u128',
    'max_amount_in': 'u128',
    'route': ['u32'],
}
)
```

---------
## Events

---------
### Traded
Event emitted when swap is successful
[sender, amount_in, route, amount_out]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T, I>` | ```u128```
| None | `Vec<AssetIdOf<T, I>>` | ```['u32']```
| None | `BalanceOf<T, I>` | ```u128```

---------
## Constants

---------
### GetNativeCurrencyId
 The asset id for native currency.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('AMMRoute', 'GetNativeCurrencyId')
```
---------
### MaxLengthRoute
 How many routes we support at most
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('AMMRoute', 'MaxLengthRoute')
```
---------
### PalletId
 Router pallet id
#### Value
```python
'0x616d6d726f757465'
```
#### Python
```python
constant = substrate.get_constant('AMMRoute', 'PalletId')
```
---------
## Errors

---------
### DuplicatedRoute
Input duplicated route

---------
### EmptyRoute
Must input one route at least

---------
### ExceedMaxLengthRoute
Exceed the max length of routes we allow

---------
### InsufficientBalance
User hasn&\#x27;t enough tokens for transaction

---------
### MaximumAmountInViolated
A more specific UnexpectedSlippage when trading exact amount out

---------
### MinimumAmountOutViolated
A more specific UnexpectedSlippage when trading exact amount in

---------
### NoPossibleRoute
Route between tokens is not possible

---------
### TokenDoesNotExists
Token doesn&\#x27;t exists in all pools

---------
### ZeroBalance
Input balance must not be zero

---------