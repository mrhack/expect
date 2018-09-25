# expect

Python validate tool for json. Raise `AssertionError` if target is invalid.

### Installation

    $ pip install py-expect


### Docs

#### Expect
#### ExpectDict(item={}, strict=False, noneable=False)
```
# valid value as dict, and has a key "name"
ExpectDict({"name": str}).validate(value)
```
Validate `value` with `item`.  `item` should be a dict and it's sub item value could be an instance of `Expect` or type or normal value

If `strict` is True, `value` keys must equal the same with `item` keys.  
If `noneable` is True, `value` can be `None`. 
#### ExpectList(item=None, min_length=None, max_length=None, noneable=False)
```
#Validate `value` as `int` list. 
ExpectList(item=int).validate(value)

```
Validate `value` as `int` list. 

`value` value must be a list. 
`min_length` min length of `value`
`max_length` max length of `value`
If `noneable` is True, `value` could be `None`

#### ExpectStr
#### ExpectNumber
#### ExpectInt
#### ExpectFloat
#### ExpectBool
#### ExpectNone
#### ExpectInstance


### Example
```python
from py_expect import ExpectDict


expect = ExpectDict({
    "name": str,
    "age": int,
})

# valid example
result = {
    "name": "mrhack"
    "age": 20
}
expect.validate(result)
print "result is valid"


# invalid example
result2 = {
    "name": "mrhack"
    "age": "20"
}
try:
    expect.validate(result)
except Exception as e:
    print "result2 is invalid"
```

### Tests

To run test cases:

     python test.py
