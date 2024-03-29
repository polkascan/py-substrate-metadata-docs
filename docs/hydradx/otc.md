
# OTC

---------
## Calls

---------
### cancel_order
See [`Pallet::cancel_order`].
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
See [`Pallet::fill_order`].
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
See [`Pallet::partial_fill_order`].
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
See [`Pallet::place_order`].
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
### InsufficientReservedAmount
Reserved amount not sufficient.

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