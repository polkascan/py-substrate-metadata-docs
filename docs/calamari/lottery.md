
# Lottery

---------
## Calls

---------
### claim_my_winnings
Allows the caller to transfer any of the account&\#x27;s previously unclaimed winnings to his their wallet

\# Errors

CannotLookup: The caller has no unclaimed winnings.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'claim_my_winnings', {}
)
```

---------
### deposit
Allows any user to deposit tokens into the lottery

\# Arguments

* `amount` - The amount of tokens to be deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'deposit', {'amount': 'u128'}
)
```

---------
### draw_lottery
Draws a lottery winner and allows them to claim their winnings later. Only the [`Config::ManageOrigin`] can execute this function.

Can only be called by the account set as [`Config::ManageOrigin`]

\# Errors

\#\# Operational
* BadOrigin: Caller is not ManageOrigin
* PotBalanceBelowGasReserve: The balance of the pot is below the gas reserve so no winner will be paid out

\#\# Fatal
* ArithmeticError::Underflow: An underflow occurred when calculating the payout.
* PotBalanceTooLow: The balance of the pot is too low.
* NoWinnerFound: Nobody was selected as winner
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'draw_lottery', {}
)
```

---------
### liquidate_lottery
Liquidates all funds held in the lottery pallet, unstaking collators, returning user deposits and paying out winnings

Can only be called by the account set as [`Config::ManageOrigin`]

Due to staking timelock, this schedules the payout of user deposits after timelock has expired.
NOTE: TODO: Any interaction with this pallet is disallowed while a liquidation is ongoing

\# Errors

* BadOrigin: Caller is not ManageOrigin
* Fails if a lottery has not been stopped and a drawing is ongoing
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'liquidate_lottery', {}
)
```

---------
### process_matured_withdrawals
This function transfers all withdrawals to user&\#x27;s wallets that are payable from unstaked collators whose timelock expired

Can only be called by the account set as [`Config::ManageOrigin`]

\# Errors

* BadOrigin: Caller is not ManageOrigin
* errors defined by the do_process_matured_withdrawals function.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'process_matured_withdrawals', {}
)
```

---------
### rebalance_stake
Maximizes staking APY and thus accrued winnings by removing staked tokens from overallocated/inactive
collators and adding to underallocated ones.

Can only be called by the account set as [`Config::ManageOrigin`]

This function should be called when the pallet&\#x27;s staked tokens are staked with overweight collators
or collators that became inactive or left the staking set.
This will withdraw the tokens from overallocated and inactive collators and wait until the funds are unlocked,
then re-allocate them to underallocated collators.

Note that this operation can run in parallel with a drawing, but it will reduce the staking revenue
generated in that drawing by the amount of funds being rebalanced.

\# Errors

* BadOrigin: Caller is not ManageOrigin
* TODO: Amount of tokens to be rebalanced would be too low.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'rebalance_stake', {}
)
```

---------
### request_withdraw
Requests a withdrawal of `amount` from the caller&\#x27;s active funds.

Withdrawal is not immediate as funds are subject to a timelock imposed by [`pallet_parachain_staking`]
It will be executed with the first [`Call::draw_lottery`] call after timelock expires

Withdrawals can NOT be cancelled because they inflict ecomomic damage on the lottery through collator unstaking
and the user causing this damage must be subjected to economic consequences for doing so

The withdrawal is paid from [`SurplusUnstakingBalance`]
If this balance is too low to handle the request, another collator is unstaked

\# Arguments

* `amount` - the amount of funds to withdraw

\# Errors

Returns an error if:
* `amount` is below the minimum withdraw amount
* `amount` is larger than the user&\#x27;s total deposit
* It is too close to the drawing
* The user has no or not enough active funds
* There are any arithmetic underflows
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'request_withdraw', {'amount': 'u128'}
)
```

---------
### set_gas_reserve
#### Attributes
| Name | Type |
| -------- | -------- | 
| gas_reserve | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'set_gas_reserve', {'gas_reserve': 'u128'}
)
```

---------
### set_min_deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_deposit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'set_min_deposit', {'min_deposit': 'u128'}
)
```

---------
### set_min_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_withdraw | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'set_min_withdraw', {'min_withdraw': 'u128'}
)
```

---------
### start_lottery
Starts the lottery by scheduling a [`Call::draw_lottery`] call

Can only be called by the account set as [`Config::ManageOrigin`]

\# Errors

Returns an error if:
* BadOrigin: Caller is not ManageOrigin
* The pallet does not have enough funds to pay for gas fees for at least the first drawing.
* The drawing interval is zero or negative.
* The Scheduler implementation failed to schedule the [`Call::draw_lottery`] call.

\# Details

This function schedules a [`Call::draw_lottery`] call with a delay specified by the [`Config::DrawingInterval`] configuration
using [`frame_support::traits::schedule::Named`] with the lottery pallet&\#x27;s pallet ID configured with [`Config::LotteryPot`] as identifier.
If the lottery is already started, this function will fail.

You can always learn what block the next drawing - if any - will happen by calling [`Self::next_drawing_at`]
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'start_lottery', {}
)
```

---------
### stop_lottery
Stops the ongoing lottery and cancels the scheduled and any future drawings.

This function cancels the scheduled drawing. Does not prevent users from interacting with the pallet

Can only be called by the account set as [`Config::ManageOrigin`]

\# Errors

* BadOrigin: Caller is not manager
* LotteryNotStarted: Nothing to stop

#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'stop_lottery', {}
)
```

---------
## Events

---------
### Claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Deposited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### LotteryStarted
#### Attributes
No attributes

---------
### LotteryStopped
#### Attributes
No attributes

---------
### LotteryWinner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### ScheduledWithdraw
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ActiveBalancePerUser

#### Python
```python
result = substrate.query(
    'Lottery', 'ActiveBalancePerUser', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### GasReserve
 NOTE: how much KMA to keep in the pallet for gas
 This must be initialized at genesis, otherwise the pallet will run out of gas at the first drawing

#### Python
```python
result = substrate.query(
    'Lottery', 'GasReserve', []
)
```

#### Return value
```python
'u128'
```
---------
### MinDeposit

#### Python
```python
result = substrate.query(
    'Lottery', 'MinDeposit', []
)
```

#### Return value
```python
'u128'
```
---------
### MinWithdraw

#### Python
```python
result = substrate.query(
    'Lottery', 'MinWithdraw', []
)
```

#### Return value
```python
'u128'
```
---------
### RebalanceInProgress

#### Python
```python
result = substrate.query(
    'Lottery', 'RebalanceInProgress', []
)
```

#### Return value
```python
'bool'
```
---------
### StakedCollators
 Incremented whenever delegating tokens to a collator
 Collators are removed from here when their funds are unlocked in [`Call::finish_unstaking_collators`]

#### Python
```python
result = substrate.query(
    'Lottery', 'StakedCollators', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### SumOfDeposits
 sum of all user&#x27;s deposits, to ensure balance never drops below
 Incremented on [`Call::deposit`]
 Decremented on withdrawal to user wallet in [`Call::process_matured_withdrawals`]

#### Python
```python
result = substrate.query(
    'Lottery', 'SumOfDeposits', []
)
```

#### Return value
```python
'u128'
```
---------
### SurplusUnstakingBalance
 This is balance unstaked from a collator that is not needed to service user&#x27;s withdrawal requests
 Incremented on initiation of a collator unstake in [`Call::request_withdraw`]
 Decremented on [`Call::request_withdraw`] (no collator unstake) and [`Call::rebalance_stake`] (restaking of surplus funds)

#### Python
```python
result = substrate.query(
    'Lottery', 'SurplusUnstakingBalance', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalPot
 Total number of token eligible to win in the current drawing cycle
 Incremented on [`Call::deposit`]
 Decremented on [`Call::request_withdraw`]

#### Python
```python
result = substrate.query(
    'Lottery', 'TotalPot', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalUnclaimedWinnings
 Free balance in the pallet that belongs to a previous lottery winner
 Incremented on winner election in the course of a drawing
 Decremented on transfer of winnings to ower wallet in [`Call::claim_my_winnings`]

#### Python
```python
result = substrate.query(
    'Lottery', 'TotalUnclaimedWinnings', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalUsers

#### Python
```python
result = substrate.query(
    'Lottery', 'TotalUsers', []
)
```

#### Return value
```python
'u32'
```
---------
### UnclaimedWinningsByAccount

#### Python
```python
result = substrate.query(
    'Lottery', 'UnclaimedWinningsByAccount', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### UnlockedUnstakingFunds
 Free balance in the pallet that was unstaked from a collator and is needed for future withdrawal requests
 Incremented on successful unstaking of a collator
 Decremented on transfer of funds to withdrawer and on restaking of funds a collator

#### Python
```python
result = substrate.query(
    'Lottery', 'UnlockedUnstakingFunds', []
)
```

#### Return value
```python
'u128'
```
---------
### UnstakingCollators

#### Python
```python
result = substrate.query(
    'Lottery', 'UnstakingCollators', []
)
```

#### Return value
```python
[{'account': 'AccountId', 'since': 'u32'}]
```
---------
### WithdrawalRequestQueue

#### Python
```python
result = substrate.query(
    'Lottery', 'WithdrawalRequestQueue', []
)
```

#### Return value
```python
[{'balance': 'u128', 'block': 'u32', 'user': 'AccountId'}]
```
---------
## Constants

---------
### DrawingFreezeout
 Time in blocks *before* a drawing in
 Depending on the randomness source, the winner might be established before the drawing, this prevents modification of the eligible winning set after the winner
 has been established but before it is selected by [`Call::draw_lottery`] which modifications of the win-eligble pool are prevented
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Lottery', 'DrawingFreezeout')
```
---------
### DrawingInterval
 Time in blocks between lottery drawings
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Lottery', 'DrawingInterval')
```
---------
### LotteryPot
 Account Identifier from which the internal Pot is generated.
#### Value
```python
'0x4c6f747279506f74'
```
#### Python
```python
constant = substrate.get_constant('Lottery', 'LotteryPot')
```
---------
### UnstakeLockTime
 Time in blocks until a collator is done unstaking
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Lottery', 'UnstakeLockTime')
```
---------
## Errors

---------
### ArithmeticOverflow
Fatal: A calculation that would overflow

---------
### ArithmeticUnderflow
Fatal: A calculation that must not be negative would underflow

---------
### CouldNotSchedule
Fatal: Could not schedule lottery drawings

---------
### DepositBelowMinAmount
Deposit amount is below minimum amount

---------
### LotteryIsRunning
Lottery has already been started

---------
### LotteryNotStarted
Lottery has not been started

---------
### NoCollatorForDeposit
Fatal: No collators found to assign this deposit to

---------
### NoCollatorForStake
Fatal: No collators found to assign this deposit to

---------
### NoCollatorForWithdrawal
Fatal: No collators found to withdraw from

---------
### NoDepositForAccount
No deposits found for this account

---------
### NoWinnerFound
Fatal: No winner could be selected

---------
### NobodyPlaying
No funds eligible to win

---------
### NotImplemented
Fatal: Functionality not yet supported

---------
### NothingToWin
No funds to win in pool

---------
### PalletMisconfigured
Fatal: Pallet configuration violates sanity checks

---------
### PotBalanceBelowGasReserve
Pallet balance is lower than the needed gas fee buffer

---------
### PotBalanceTooLow
FATAL: Assigning/Transferring winning claims
would **remove** user deposited funds from pallet

---------
### PotBalanceTooLowToPayTxFee
Pallet balance is too low to submit a needed transaction

---------
### PotBalanceTooLowToStake
FATAL: Can&\#x27;t stake the requested amount with available funds

---------
### TooCloseToDrawing
Pre-drawing freeze in effect, can&\#x27;t modify balances

---------
### WithdrawAboveDeposit
Requested to withdraw more than you deposited

---------
### WithdrawBelowMinAmount
Requested Withdrawal amount is below minimum

---------