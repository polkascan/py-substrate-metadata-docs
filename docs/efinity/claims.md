
# Claims

---------
## Calls

---------
### mint_enj_from_native_efi
Bridge EFI from the Efinity parachain to the Enjin Relay Chain

Parameters:
- `origin`: The account initiating the claim and from which EFI will be burned.
- `amount`: Number of EFIs to burn in order to bridge to the Enjin Relay Chain. The
conversion rate will be according to the `ExchangeRate` storage on the Enjin Relay
Chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'mint_enj_from_native_efi', {'amount': 'u128'}
)
```

---------
## Events

---------
### ClaimedEnj
A user burned EFI in order to begin a claim of ENJ.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| early_bird_amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### MaxEfiForEarlyBirdRewards
 Stores maximum eligible EFI for early bird bonus

#### Python
```python
result = substrate.query(
    'Claims', 'MaxEfiForEarlyBirdRewards', []
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### AmountZero
Amount is zero

---------
### ClaimCouldNotBeSettled
The claim could not be settled

---------
### NotEnoughBalance
The account does not have enough balance to claim

---------