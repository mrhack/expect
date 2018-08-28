# expect

Python validate tool for json.

### Installation

    $ pip install py-expect

### Docs
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
