
# BagsList

---------
## Calls

---------
### put_in_front_of
Move the caller&\#x27;s Id directly in front of `lighter`.

The dispatch origin for this call must be _Signed_ and can only be called by the Id of
the account going in front of `lighter`.

Only works if
- both nodes are within the same bag,
- and `origin` has a greater `Score` than `lighter`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| lighter | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'BagsList', 'put_in_front_of', {'lighter': 'AccountId'}
)
```

---------
### rebag
Declare that some `dislocated` account has, through rewards or penalties, sufficiently
changed its score that it should properly fall into a different bag than its current
one.

Anyone can call this function about any potentially dislocated account.

Will never return an error; if `dislocated` does not exist or doesn&\#x27;t need a rebag, then
it is a noop and fees are still collected from `origin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dislocated | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'BagsList', 'rebag', {'dislocated': 'AccountId'}
)
```

---------
## Events

---------
### Rebagged
Moved an account from one bag to another.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| from | `T::Score` | ```u64```
| to | `T::Score` | ```u64```

---------
## Storage functions

---------
### CounterForListNodes
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'BagsList', 'CounterForListNodes', []
)
```

#### Return value
```python
'u32'
```
---------
### ListBags
 A bag stored in storage.

 Stores a `Bag` struct, which stores head and tail pointers to itself.

#### Python
```python
result = substrate.query(
    'BagsList', 'ListBags', ['u64']
)
```

#### Return value
```python
{'head': (None, 'AccountId'), 'tail': (None, 'AccountId')}
```
---------
### ListNodes
 A single node, within some bag.

 Nodes store links forward and back within their respective bags.

#### Python
```python
result = substrate.query(
    'BagsList', 'ListNodes', ['AccountId']
)
```

#### Return value
```python
{
    'bag_upper': 'u64',
    'id': 'AccountId',
    'next': (None, 'AccountId'),
    'prev': (None, 'AccountId'),
}
```
---------
## Constants

---------
### BagThresholds
 The list of thresholds separating the various bags.

 Ids are separated into unsorted bags according to their score. This specifies the
 thresholds separating the bags. An id&#x27;s bag is the largest bag for which the id&#x27;s score
 is less than or equal to its upper threshold.

 When ids are iterated, higher bags are iterated completely before lower bags. This means
 that iteration is _semi-sorted_: ids of higher score tend to come before ids of lower
 score, but peer ids within a particular bag are sorted in insertion order.

 \# Expressing the constant

 This constant must be sorted in strictly increasing order. Duplicate items are not
 permitted.

 There is an implied upper limit of `Score::MAX`; that value does not need to be
 specified within the bag. For any two threshold lists, if one ends with
 `Score::MAX`, the other one does not, and they are otherwise equal, the two
 lists will behave identically.

 \# Calculation

 It is recommended to generate the set of thresholds in a geometric series, such that
 there exists some constant ratio such that `threshold[k + 1] == (threshold[k] *
 constant_ratio).max(threshold[k] + 1)` for all `k`.

 The helpers in the `/utils/frame/generate-bags` module can simplify this calculation.

 \# Examples

 - If `BagThresholds::get().is_empty()`, then all ids are put into the same bag, and
   iteration is strictly in insertion order.
 - If `BagThresholds::get().len() == 64`, and the thresholds are determined according to
   the procedure given above, then the constant ratio is equal to 2.
 - If `BagThresholds::get().len() == 200`, and the thresholds are determined according to
   the procedure given above, then the constant ratio is approximately equal to 1.248.
 - If the threshold list begins `[1, 2, 3, ...]`, then an id with score 0 or 1 will fall
   into bag 0, an id with score 2 will fall into bag 1, etc.

 \# Migration

 In the event that this list ever changes, a copy of the old bags list must be retained.
 With that `List::migrate` can be called, which will perform the appropriate migration.
#### Value
```python
[
    18446,
    21942,
    26101,
    31048,
    36933,
    43933,
    52260,
    62165,
    73947,
    87962,
    104634,
    124466,
    148057,
    176119,
    209500,
    249207,
    296440,
    352626,
    419461,
    498963,
    593534,
    706029,
    839846,
    999026,
    1188376,
    1413614,
    1681542,
    2000252,
    2379368,
    2830340,
    3366787,
    4004909,
    4763977,
    5666914,
    6740989,
    8018638,
    9538445,
    11346308,
    13496823,
    16054934,
    19097895,
    22717601,
    27023366,
    32145221,
    38237843,
    45485226,
    54106237,
    64361225,
    76559885,
    91070610,
    108331615,
    128864173,
    153288355,
    182341757,
    216901776,
    258012104,
    306914250,
    365085030,
    434281169,
    516592350,
    614504324,
    730973976,
    869518623,
    1034322234,
    1230361783,
    1463557553,
    1740951922,
    2070922041,
    2463432818,
    2930337854,
    3485737413,
    4146404243,
    4932290104,
    5867128298,
    6979150403,
    8301938848,
    9875441087,
    11747175984,
    13973668861,
    16622158526,
    19772627848,
    23520219194,
    27978107674,
    33280918965,
    39588794927,
    47092229797,
    56017823007,
    66635122354,
    79264764190,
    94288156458,
    112158996991,
    133416974926,
    158704069009,
    188783934983,
    224564967554,
    267127733390,
    317757603616,
    377983571284,
    449624426087,
    534843680765,
    636214907948,
    756799460576,
    900238923000,
    1070865084745,
    1273830758066,
    1515265389927,
    1802460167782,
    2144088209260,
    2550466485339,
    3033867386959,
    3608889344190,
    4292897690450,
    5106549085619,
    6074415335321,
    7225725445369,
    8595248320980,
    10224342767779,
    12162206504013,
    14467361903438,
    17209423337450,
    20471199489189,
    24351194128290,
    28966580868250,
    34456741742372,
    40987476461258,
    48756009469006,
    57996946008343,
    68989357064443,
    82065207148676,
    97619379436515,
    116121601013031,
    138130628361542,
    164311121489044,
    195453716277339,
    232498901233352,
    276565419702808,
    328984055277841,
    391337820698467,
    465509763929707,
    553739835130482,
    658692531864133,
    783537365397135,
    932044578122100,
    1108699002716354,
    1318835501517405,
    1568800076306778,
    1866141513925323,
    2219839355307693,
    2640575072470128,
    3141054642841099,
    3736392262494645,
    4444566786206049,
    5286964678557830,
    6289025872908157,
    7481012042792217,
    8898920487112374,
    10585571227925884,
    12591900150560060,
    14978497238144946,
    17817436354364432,
    21194451832815784,
    25211527604728292,
    29989977055213672,
    35674106617941108,
    42435573746695632,
    50478570872062200,
    60045991895755160,
    71426767447186216,
    84964590422813568,
    101068295314557840,
    120224204777051824,
    143010816292976128,
    170116272465353216,
    202359142529610432,
    240713142675161344,
    286336541716043456,
    340607140145005952,
    405163878918425536,
    481956334533498176,
    573303595120660160,
    681964295575472384,
    811219926750796672,
    964973934599101056,
    1147869602002174464,
    1365430273251919360,
    1624226155881144576,
    1932072737164011776,
    2298266807350686464,
    2733867217402556416,
    3252028849950646272,
    3868399889208691200,
    4601594387164468224,
    5473754397277415424,
    6511218651797905408,
    7745317976379835392,
    9213321463051765760,
    10959561975427864576,
    13036774975770695680,
    15507691105715548160,
    18446744073709551615,
]
```
#### Python
```python
constant = substrate.get_constant('BagsList', 'BagThresholds')
```
---------
## Errors

---------
### IdNotFound
Id not found in list.

---------
### NotHeavier
An Id does not have a greater score than another Id.

---------
### NotInSameBag
Attempted to place node in front of a node in another bag.

---------