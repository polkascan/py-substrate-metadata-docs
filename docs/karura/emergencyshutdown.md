
# EmergencyShutdown

---------
## Calls

---------
### emergency_shutdown
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EmergencyShutdown', 'emergency_shutdown', {}
)
```

---------
### open_collateral_refund
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EmergencyShutdown', 'open_collateral_refund', {}
)
```

---------
### refund_collaterals
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EmergencyShutdown', 'refund_collaterals', {'amount': 'u128'}
)
```

---------
## Events

---------
### OpenRefund
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| block_number | `BlockNumberFor<T>` | ```u32```

---------
### Refund
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| stable_coin_amount | `Balance` | ```u128```
| refund_list | `Vec<(CurrencyId, Balance)>` | ```[({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': 'scale_info::53', 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': 'scale_info::53', 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}, 'u128')]```

---------
### Shutdown
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| block_number | `BlockNumberFor<T>` | ```u32```

---------
## Storage functions

---------
### CanRefund

#### Python
```python
result = substrate.query(
    'EmergencyShutdown', 'CanRefund', []
)
```

#### Return value
```python
'bool'
```
---------
### IsShutdown

#### Python
```python
result = substrate.query(
    'EmergencyShutdown', 'IsShutdown', []
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### AlreadyShutdown

---------
### CanNotRefund

---------
### ExistPotentialSurplus

---------
### ExistUnhandledDebit

---------
### MustAfterShutdown

---------