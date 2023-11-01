
# PriceCollector

---------
## Storage functions

---------
### Collection
 Storage that contains the data values of a collection.

#### Python
```python
result = substrate.query(
    'PriceCollector', 'Collection', ['u64']
)
```

#### Return value
```python
'scale_info::658'
```
---------
### Listening
 Storage that contains the registering information

#### Python
```python
result = substrate.query(
    'PriceCollector', 'Listening', [{'Isin': '[u8; 12]'}]
)
```

#### Return value
```python
'scale_info::653'
```
---------
## Constants

---------
### MaxCollectionSize
 Max size of a data collection
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('PriceCollector', 'MaxCollectionSize')
```
---------
### MaxCollections
 Max number of collections
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('PriceCollector', 'MaxCollections')
```
---------
## Errors

---------
### DataIdNotInCollection
The used data ID is not in the collection.

---------
### DataIdWithoutData
The data ID doesn&\#x27;t have data associated to it.
The data was never set for the Id.

---------
### MaxCollectionNumber
Max collection number exceeded

---------
### MaxCollectionSize
Max collection size exceeded

---------