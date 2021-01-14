TestMetaclass = type('TestMetaclass', (), {"a": True})
print(TestMetaclass)

Test1Metaclass = type('Test1Metaclass', (TestMetaclass,), {})


class Test2class(Test1Metaclass):
    pass


TC = Test2class()
print(TC)
print(TC.a)
