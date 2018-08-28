#!coding=utf8
import unittest
from expect import *


class ExpectTest(unittest.TestCase):

    def test_int(self):
        ExpectInt().validate(1)

        ExpectInt(value=1).validate(1)
        with self.assertRaises(AssertionError) as error:
            ExpectInt(value=2).validate(1)

        ExpectInt(min=1, max=2).validate(1)
        ExpectInt(min=1, max=2).validate(2)
        with self.assertRaises(AssertionError) as error:
            ExpectInt(min=1, max=2).validate(0)

        ExpectInt(enum=(1, 2)).validate(1)
        with self.assertRaises(AssertionError) as error:
            ExpectInt(enum=(1, 2)).validate(3)

        ExpectInt(noneable=True).validate(None)
        with self.assertRaises(AssertionError) as error:
            ExpectInt().validate(None)

    def test_float(self):
        ExpectFloat().validate(1.0)

        ExpectFloat(value=1.0).validate(1.0)
        with self.assertRaises(AssertionError) as error:
            ExpectFloat(value=2.0).validate(1.0)

        ExpectFloat(min=1.0, max=2.0).validate(1.0)
        ExpectFloat(min=1.0, max=2.0).validate(2.0)
        with self.assertRaises(AssertionError) as error:
            ExpectFloat(min=1.0, max=2.0).validate(0.0)

        ExpectFloat(enum=(1.0, 2.0)).validate(1.0)
        with self.assertRaises(AssertionError) as error:
            ExpectFloat(enum=(1.0, 2.0)).validate(3.0)

        ExpectFloat(noneable=True).validate(None)
        with self.assertRaises(AssertionError) as error:
            ExpectFloat().validate(None)

    def test_str(self):
        ExpectStr().validate("test_str")
        ExpectStr(value="test_str").validate("test_str")
        with self.assertRaises(AssertionError) as error:
            ExpectStr(value="test_str").validate("test_str1")

        ExpectStr(min_length=2, max_length=10).validate("test_str")
        with self.assertRaises(AssertionError) as error:
            ExpectStr(min_length=2, max_length=5).validate("test_str")

        ExpectStr(enum=("str1", "str2")).validate("str2")
        with self.assertRaises(AssertionError) as error:
            ExpectStr(enum=("str1", "str2")).validate("str3")

        ExpectStr(noneable=True).validate(None)
        with self.assertRaises(AssertionError) as error:
            ExpectStr().validate(None)

        ExpectStr().validate(u"test_str")
        ExpectStr(value="test_str").validate(u"test_str")
        with self.assertRaises(AssertionError) as error:
            ExpectStr(value="test_str").validate(u"test_str1")

        ExpectStr(min_length=2, max_length=10).validate(u"test_str")
        with self.assertRaises(AssertionError) as error:
            ExpectStr(min_length=2, max_length=5).validate(u"test_str")

        ExpectStr(enum=("str1", "str2")).validate(u"str2")
        with self.assertRaises(AssertionError) as error:
            ExpectStr(enum=("str1", "str2")).validate(u"str3")

    def test_bool(self):
        ExpectBool().validate(True)
        with self.assertRaises(AssertionError) as error:
            ExpectBool().validate(1)
        with self.assertRaises(AssertionError) as error:
            ExpectBool().validate("str")

        ExpectBool(noneable=True).validate(None)
        with self.assertRaises(AssertionError) as error:
            ExpectBool().validate(None)

    def test_none(self):
        ExpectNone().validate(None)
        with self.assertRaises(AssertionError) as error:
            ExpectNone().validate(1)

    def test_list(self):
        ExpectList().validate([])

        ExpectList(int).validate([1, 2, 3, 4, 5])
        with self.assertRaises(AssertionError) as error:
            ExpectList(int).validate([1, 1, 1, "2"])

        ExpectList(bool).validate([True, True, True])
        with self.assertRaises(AssertionError) as error:
            ExpectList(bool).validate([True, False, 1])

        ExpectList([]).validate([[1]])
        ExpectList([int]).validate([[1]])
        with self.assertRaises(AssertionError) as error:
            ExpectList([str]).validate([[1]])

        ExpectList([[]]).validate([[[None]]])
        with self.assertRaises(AssertionError) as error:
            ExpectList([]).validate([1])

        ExpectList(int, min_length=1, max_length=2).validate([1, 2])
        with self.assertRaises(AssertionError) as error:
            ExpectList(1).validate([1, 1, 1, 2])

        ExpectList(ExpectDict({
            "name": ExpectStr(min_length=2, max_length=60),
            "age": ExpectInt(min=6, max=130, noneable=True),
            "address": ExpectStr(min_length=2, max_length=200),
        })).validate([{
            "name": u"区旧地",
            "age": 20,
            "address": u"区旧地区旧地区旧地",
        }])

        ExpectList(noneable=True).validate(None)
        with self.assertRaises(AssertionError) as error:
            ExpectList().validate(None)

    def test_dict(self):
        ExpectDict().validate({})
        ExpectDict({
            "int_key": int,
            "float_key": float,
            "str_key": str,
            "bool_key": bool,
            "list_key": list,
            "dict_key": dict,
        }).validate({
            "int_key": 1,
            "float_key": 1.0,
            "str_key": 'str',
            "bool_key": True,
            "list_key": [],
            "dict_key": {},
        })

        ExpectDict({
            "int_key": ExpectInt(),
            "float_key": ExpectFloat(),
            "str_key": ExpectStr(),
            "bool_key": ExpectBool(),
            "list_key": ExpectList(),
            "dict_key": ExpectDict(),
        }).validate({
            "int_key": 1,
            "float_key": 1.0,
            "str_key": 'str',
            "bool_key": True,
            "list_key": [],
            "dict_key": {},
        })


if __name__ == '__main__':
    unittest.main()
