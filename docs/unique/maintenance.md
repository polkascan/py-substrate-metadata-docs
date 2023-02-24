
# Maintenance

---------
## Calls

---------
### disable
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'disable', {}
)
```

---------
### enable
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Maintenance', 'enable', {}
)
```

---------
## Events

---------
### MaintenanceDisabled
#### Attributes
No attributes

---------
### MaintenanceEnabled
#### Attributes
No attributes

---------
## Storage functions

---------
### Enabled

#### Python
```python
result = substrate.query(
    'Maintenance', 'Enabled', []
)
```

#### Return value
```python
'bool'
```
---------