
# Investments

---------
## Calls

---------
### collect_investments
Collect the results of a users invest orders for the given investment.
If any amounts are not fulfilled they are directly appended to the next active
order for this investment.
#### Attributes
| Name | Type |
| -------- | -------- | 
| investment_id | `T::InvestmentId` | 

#### Python
```python
call = substrate.compose_call(
    'Investments', 'collect_investments', {
    'investment_id': {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
}
)
```

---------
### collect_investments_for
Collect the results of another users invest orders for the given investment.
If any amounts are not fulfilled they are directly appended to the next active
order for this investment.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| investment_id | `T::InvestmentId` | 

#### Python
```python
call = substrate.compose_call(
    'Investments', 'collect_investments_for', {
    'investment_id': {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
    'who': 'AccountId',
}
)
```

---------
### collect_redemptions
Collect the results of a users redeem orders for the given investment.
If any amounts are not fulfilled they are directly appended to the next active
order for this investment.
#### Attributes
| Name | Type |
| -------- | -------- | 
| investment_id | `T::InvestmentId` | 

#### Python
```python
call = substrate.compose_call(
    'Investments', 'collect_redemptions', {
    'investment_id': {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
}
)
```

---------
### collect_redemptions_for
Collect the results of another users redeem orders for the given investment.
If any amounts are not fulfilled they are directly appended to the next active
order for this investment.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| investment_id | `T::InvestmentId` | 

#### Python
```python
call = substrate.compose_call(
    'Investments', 'collect_redemptions_for', {
    'investment_id': {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
    'who': 'AccountId',
}
)
```

---------
### update_invest_order
Update an order to invest into a given investment.

If the requested amount is greater than the current
investment order, the balance will be transferred from
the calling account to the pool. If the requested
amount is less than the current order, the balance
will be transferred from the pool to the calling
account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| investment_id | `T::InvestmentId` | 
| amount | `T::Amount` | 

#### Python
```python
call = substrate.compose_call(
    'Investments', 'update_invest_order', {
    'amount': 'u128',
    'investment_id': {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
}
)
```

---------
### update_redeem_order
Update an order to redeem from a given investment.

If the requested amount is greater than the current
investment order, the balance will be transferred from
the calling account to the pool. If the requested
amount is less than the current order, the balance
will be transferred from the pool to the calling
account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| investment_id | `T::InvestmentId` | 
| amount | `T::Amount` | 

#### Python
```python
call = substrate.compose_call(
    'Investments', 'update_redeem_order', {
    'amount': 'u128',
    'investment_id': {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
}
)
```

---------
## Events

---------
### InvestCollectedForNonClearedOrderId
A collect call for the investments happened, but the current OrderId
is not yet cleared
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```

---------
### InvestCollectedWithoutActivePosition
Signals that a collect of investments call was successful but there
was no order of a user to collect from
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```

---------
### InvestOrderUpdated
An invest order was updated. [investment_id, order_id, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| submitted_at | `OrderId` | ```u64```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Amount` | ```u128```

---------
### InvestOrdersCleared
TotalOrders of investments were fulfilled [investment_id, order_id, FulfillmentWithPrice]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| order_id | `OrderId` | ```u64```
| fulfillment | `FulfillmentWithPrice<T::BalanceRatio>` | ```{'of_amount': 'u64', 'price': 'u128'}```

---------
### InvestOrdersCollected
Fulfilled orders were collected.
[investment_id, who, collected_orders, Collection, CollectOutcome]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| who | `T::AccountId` | ```AccountId```
| processed_orders | `Vec<OrderId>` | ```['u64']```
| collection | `InvestCollection<T::Amount>` | ```{'payout_investment_invest': 'u128', 'remaining_investment_invest': 'u128'}```
| outcome | `CollectOutcome` | ```('FullyCollected', 'PartiallyCollected')```

---------
### InvestOrdersInProcessing
TotalOrders of investments are in processing state [investment_id, order_id, TotalOrder]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| order_id | `OrderId` | ```u64```
| total_order | `TotalOrder<T::Amount>` | ```{'amount': 'u128'}```

---------
### RedeemCollectedForNonClearedOrderId
A collect call for the redemptions happened, but the current OrderId
is not yet cleared
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```

---------
### RedeemCollectedWithoutActivePosition
Signals that a collect of redemptions call was successful but there
was no order of a user to collect from
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```

---------
### RedeemOrderUpdated
An invest order was updated. [investment_id, order_id, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| submitted_at | `OrderId` | ```u64```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Amount` | ```u128```

---------
### RedeemOrdersCleared
TotalOrders of redemptions were fulfilled [investment_id, order_id, FulfillmentWithPrice]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| order_id | `OrderId` | ```u64```
| fulfillment | `FulfillmentWithPrice<T::BalanceRatio>` | ```{'of_amount': 'u64', 'price': 'u128'}```

---------
### RedeemOrdersCollected
Fulfilled orders were collected.
[investment_id, who, collected_orders, Collection, CollectOutcome]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| who | `T::AccountId` | ```AccountId```
| processed_orders | `Vec<OrderId>` | ```['u64']```
| collection | `RedeemCollection<T::Amount>` | ```{'payout_investment_redeem': 'u128', 'remaining_investment_redeem': 'u128'}```
| outcome | `CollectOutcome` | ```('FullyCollected', 'PartiallyCollected')```

---------
### RedeemOrdersInProcessing
TotalOrders of redemptions in processing state [investment_id, order_id, TotalOrder]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| order_id | `OrderId` | ```u64```
| total_order | `TotalOrder<T::Amount>` | ```{'amount': 'u128'}```

---------
## Storage functions

---------
### ActiveInvestOrders

#### Python
```python
result = substrate.query(
    'Investments', 'ActiveInvestOrders', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount': 'u128'}
```
---------
### ActiveRedeemOrders

#### Python
```python
result = substrate.query(
    'Investments', 'ActiveRedeemOrders', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount': 'u128'}
```
---------
### ClearedInvestOrders

#### Python
```python
result = substrate.query(
    'Investments', 'ClearedInvestOrders', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
    'u64',
]
)
```

#### Return value
```python
{'of_amount': 'u64', 'price': 'u128'}
```
---------
### ClearedRedeemOrders

#### Python
```python
result = substrate.query(
    'Investments', 'ClearedRedeemOrders', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
    'u64',
]
)
```

#### Return value
```python
{'of_amount': 'u64', 'price': 'u128'}
```
---------
### InProcessingInvestOrders

#### Python
```python
result = substrate.query(
    'Investments', 'InProcessingInvestOrders', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount': 'u128'}
```
---------
### InProcessingRedeemOrders

#### Python
```python
result = substrate.query(
    'Investments', 'InProcessingRedeemOrders', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount': 'u128'}
```
---------
### InvestOrderId

#### Python
```python
result = substrate.query(
    'Investments', 'InvestOrderId', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
'u64'
```
---------
### InvestOrders

#### Python
```python
result = substrate.query(
    'Investments', 'InvestOrders', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount': 'u128', 'submitted_at': 'u64'}
```
---------
### RedeemOrderId

#### Python
```python
result = substrate.query(
    'Investments', 'RedeemOrderId', [
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
'u64'
```
---------
### RedeemOrders

#### Python
```python
result = substrate.query(
    'Investments', 'RedeemOrders', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount': 'u128', 'submitted_at': 'u64'}
```
---------
## Errors

---------
### CollectRequired
The user has to many uncollected orders. Before
submitting new orders, a collect of those is required.

---------
### NoActiveInvestOrder
User has currently no invest orders active and can not collect

---------
### NoActiveRedeemOrder
User has currently no redeem orders active and can not collect

---------
### NoNewOrder
Update of order was not a new order

---------
### OrderInProcessing
Order is not yet cleared and must be processed first
before requesting new orders is allowed

---------
### OrderNotCleared
The order has not been marked as cleared. It&\#x27;s either active or
in processing

---------
### OrderNotInProcessing
Order is still active and can not be processed further

---------
### OrderStillActive
The order a user tried to collect for is still active and
needs to be put in processing and then be cleared before
a collect is possible

---------
### UnknownInvestment
IvestmentManager does not now given investment

---------
### ZeroPricedInvestment
A fulfillment happened with an investment price of zero.
The order will be discarded

---------