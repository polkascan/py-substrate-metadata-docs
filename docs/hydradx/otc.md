
# OTC

---------
## Calls

---------
### cancel_order
Cancel an open OTC order
 
Parameters:
- `order_id`: ID of the order
- `asset`: Asset which is being filled
- `amount`: Amount which is being filled

Validations:
- caller is order owner

Emits `Cancelled` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'OTC', 'cancel_order', {'order_id': 'u32'}
)
```

---------
### fill_order
Fill an OTC order (completely)
 
Parameters:
- `order_id`: ID of the order

Events:
`Filled` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'OTC', 'fill_order', {'order_id': 'u32'}
)
```

---------
### partial_fill_order
Fill an OTC order (partially)
 
Parameters:
- `order_id`: ID of the order
- `amount_in`: Amount with which the order is being filled

Validations:
- order must be partially_fillable
- after the partial_fill, the remaining order.amount_in must be higher than the existential deposit
  of asset_in multiplied by ExistentialDepositMultiplier
- after the partial_fill, the remaining order.amount_out must be higher than the existential deposit
  of asset_out multiplied by ExistentialDepositMultiplier

Events:
`PartiallyFilled` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 
| amount_in | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'OTC', 'partial_fill_order', {
    'amount_in': 'u128',
    'order_id': 'u32',
}
)
```

---------
### place_order
Create a new OTC order
 
Parameters:
- `asset_in`: Asset which is being bought
- `asset_out`: Asset which is being sold
- `amount_in`: Amount that the order is seeking to buy
- `amount_out`: Amount that the order is selling
- `partially_fillable`: Flag indicating whether users can fill the order partially

Validations:
- asset_in must be registered
- amount_in must be higher than the existential deposit of asset_in multiplied by
  ExistentialDepositMultiplier
- amount_out must be higher than the existential deposit of asset_out multiplied by
  ExistentialDepositMultiplier

Events:
- `Placed` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetId` | 
| asset_out | `T::AssetId` | 
| amount_in | `Balance` | 
| amount_out | `Balance` | 
| partially_fillable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'OTC', 'place_order', {
    'amount_in': 'u128',
    'amount_out': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'partially_fillable': 'bool',
}
)
```

---------
## Events

---------
### Cancelled
An Order has been cancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u32```

---------
### Filled
An Order has been completely filled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```

---------
### PartiallyFilled
An Order has been partially filled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```

---------
### Placed
An Order has been placed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u32```
| asset_in | `T::AssetId` | ```u32```
| asset_out | `T::AssetId` | ```u32```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```
| partially_fillable | `bool` | ```bool```

---------
## Storage functions

---------
### NextOrderId
 ID sequencer for Orders

#### Python
```python
result = substrate.query(
    'OTC', 'NextOrderId', []
)
```

#### Return value
```python
'u32'
```
---------
### Orders

#### Python
```python
result = substrate.query(
    'OTC', 'Orders', ['u32']
)
```

#### Return value
```python
{
    'amount_in': 'u128',
    'amount_out': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'owner': 'AccountId',
    'partially_fillable': 'bool',
}
```
---------
## Constants

---------
### ExistentialDepositMultiplier
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('OTC', 'ExistentialDepositMultiplier')
```
---------
## Errors

---------
### AssetNotRegistered
Asset does not exist in registry

---------
### Forbidden
The caller does not have permission to complete the action

---------
### MathError
Error with math calculations

---------
### OrderAmountTooSmall
Order amount_in and amount_out must at all times be greater than the existential deposit
for the asset multiplied by the ExistentialDepositMultiplier.
A fill order may not leave behind amounts smaller than this.

---------
### OrderIdOutOfBound
Size of order ID exceeds the bound

---------
### OrderNotFound
Order cannot be found

---------
### OrderNotPartiallyFillable
Cannot partially fill an order which is not partially fillable

---------