
# Maintenance

---------
## Calls

---------
### switch_maintenance_mode_off
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'switch_maintenance_mode_off', {}
)
```

---------
### switch_maintenance_mode_on
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'switch_maintenance_mode_on', {}
)
```

---------
### switch_upgradability_in_maintenance_mode_off
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'switch_upgradability_in_maintenance_mode_off', {}
)
```

---------
### switch_upgradability_in_maintenance_mode_on
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'switch_upgradability_in_maintenance_mode_on', {}
)
```

---------
## Events

---------
### MaintenanceModeSwitchedOff
Maintenance mode has been switched off
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### MaintenanceModeSwitchedOn
Maintenance mode has been switched on
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### UpgradabilityInMaintenanceModeSwitchedOff
Upgradablilty in maintenance mode has been switched off
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### UpgradabilityInMaintenanceModeSwitchedOn
Upgradablilty in maintenance mode has been switched on
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### MaintenanceStatus

#### Python
```python
result = substrate.query(
    'Maintenance', 'MaintenanceStatus', []
)
```

#### Return value
```python
{'is_maintenance': 'bool', 'is_upgradable_in_maintenance': 'bool'}
```
---------
## Errors

---------
### AlreadyInMaintenanceMode
Already in maintenance mode

---------
### AlreadyNotUpgradableInMaintenanceMode
Already not upgradable in maintenance mode

---------
### AlreadyUpgradableInMaintenanceMode
Already upgradable in maintenance mode

---------
### NotFoundationAccount
Timeouts were incorrectly initialized

---------
### NotInMaintenanceMode
Not in maintenance mode

---------