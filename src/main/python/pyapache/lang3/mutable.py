from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Short as Short
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.lang3.mutable.MutableShort as _MutableShort
_MutableShort = _MutableShort
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableShort():
    """org.apache.commons.lang3.mutable.MutableShort"""
 
    @staticmethod
    def _wrap(java_value: _MutableShort) -> 'MutableShort':
        return MutableShort(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableShort):
        """
        Dynamic initializer for MutableShort.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableShort__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableShort__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.addAndGet(java.lang.Number)"""
        return int._wrap(super(_MutableShort, self).addAndGet(arg0))

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.subtract(short)"""
        super(_MutableShort, self).subtract(_short.valueOf(arg0))

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableShort.decrement()"""
        super(MutableShort, self).decrement()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableShort()"""
        val = _MutableShort()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.hashCode()"""
        return int._wrap(super(MutableShort, self).hashCode())

    @overload
    def toShort(self) -> 'Short':
        """public java.lang.Short org.apache.commons.lang3.mutable.MutableShort.toShort()"""
        return _transform(super(MutableShort, self).toShort()).'Short'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableShort(java.lang.Number)"""
        val = _MutableShort(arg0)
        self.__wrapper = val

    @overload
    def decrementAndGet(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.decrementAndGet()"""
        return int._wrap(super(MutableShort, self).decrementAndGet())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableShort(short)"""
        val = _MutableShort(_short.valueOf(arg0))
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'MutableShort') -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.compareTo(org.apache.commons.lang3.mutable.MutableShort)"""
        return int._wrap(super(_MutableShort, self).compareTo(arg0))

    @override
    @overload
    def getValue(self) -> 'Short':
        """public java.lang.Short org.apache.commons.lang3.mutable.MutableShort.getValue()"""
        return _transform(super(MutableShort, self).getValue()).'Short'Value()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableShort()"""
        val = _MutableShort()
        self.__wrapper = val

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.add(short)"""
        super(_MutableShort, self).add(_short.valueOf(arg0))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.intValue()"""
        return int._wrap(super(MutableShort, self).intValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableShort.toString()"""
        return str._wrap(super(MutableShort, self).toString())

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndAdd(java.lang.Number)"""
        return int._wrap(super(_MutableShort, self).getAndAdd(arg0))

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.subtract(java.lang.Number)"""
        super(_MutableShort, self).subtract(arg0)

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableShort.increment()"""
        super(MutableShort, self).increment()

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.setValue(java.lang.Number)"""
        super(_MutableShort, self).setValue(arg0)

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndAdd(short)"""
        return int._wrap(super(_MutableShort, self).getAndAdd(_short.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.add(java.lang.Number)"""
        super(_MutableShort, self).add(arg0)

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableShort(java.lang.String)"""
        val = _MutableShort(arg0)
        self.__wrapper = val

    @override
    @overload
    def shortValue(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.shortValue()"""
        return int._wrap(super(MutableShort, self).shortValue())

    @overload
    def incrementAndGet(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.incrementAndGet()"""
        return int._wrap(super(MutableShort, self).incrementAndGet())

    @overload
    def getAndIncrement(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndIncrement()"""
        return int._wrap(super(MutableShort, self).getAndIncrement())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableShort.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableShort, self).equals(arg0))

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.setValue(short)"""
        super(_MutableShort, self).setValue(_short.valueOf(arg0))

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.addAndGet(short)"""
        return int._wrap(super(_MutableShort, self).addAndGet(_short.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableShort.longValue()"""
        return int._wrap(super(MutableShort, self).longValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableShort.floatValue()"""
        return float._wrap(super(MutableShort, self).floatValue())

    @overload
    def getAndDecrement(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndDecrement()"""
        return int._wrap(super(MutableShort, self).getAndDecrement())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableShort.doubleValue()"""
        return float._wrap(super(MutableShort, self).doubleValue())

 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableShort
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Short as Short
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.lang3.mutable.MutableShort as _MutableShort
_MutableShort = _MutableShort
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableShort():
    """org.apache.commons.lang3.mutable.MutableShort"""
 
    @staticmethod
    def _wrap(java_value: _MutableShort) -> 'MutableShort':
        return MutableShort(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableShort):
        """
        Dynamic initializer for MutableShort.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableShort__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableShort__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.addAndGet(java.lang.Number)"""
        return int._wrap(super(_MutableShort, self).addAndGet(arg0))

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.subtract(short)"""
        super(_MutableShort, self).subtract(_short.valueOf(arg0))

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableShort.decrement()"""
        super(MutableShort, self).decrement()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableShort()"""
        val = _MutableShort()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.hashCode()"""
        return int._wrap(super(MutableShort, self).hashCode())

    @overload
    def toShort(self) -> 'Short':
        """public java.lang.Short org.apache.commons.lang3.mutable.MutableShort.toShort()"""
        return _transform(super(MutableShort, self).toShort()).'Short'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableShort(java.lang.Number)"""
        val = _MutableShort(arg0)
        self.__wrapper = val

    @overload
    def decrementAndGet(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.decrementAndGet()"""
        return int._wrap(super(MutableShort, self).decrementAndGet())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableShort(short)"""
        val = _MutableShort(_short.valueOf(arg0))
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'MutableShort') -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.compareTo(org.apache.commons.lang3.mutable.MutableShort)"""
        return int._wrap(super(_MutableShort, self).compareTo(arg0))

    @override
    @overload
    def getValue(self) -> 'Short':
        """public java.lang.Short org.apache.commons.lang3.mutable.MutableShort.getValue()"""
        return _transform(super(MutableShort, self).getValue()).'Short'Value()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableShort()"""
        val = _MutableShort()
        self.__wrapper = val

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.add(short)"""
        super(_MutableShort, self).add(_short.valueOf(arg0))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.intValue()"""
        return int._wrap(super(MutableShort, self).intValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableShort.toString()"""
        return str._wrap(super(MutableShort, self).toString())

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndAdd(java.lang.Number)"""
        return int._wrap(super(_MutableShort, self).getAndAdd(arg0))

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.subtract(java.lang.Number)"""
        super(_MutableShort, self).subtract(arg0)

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableShort.increment()"""
        super(MutableShort, self).increment()

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.setValue(java.lang.Number)"""
        super(_MutableShort, self).setValue(arg0)

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndAdd(short)"""
        return int._wrap(super(_MutableShort, self).getAndAdd(_short.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.add(java.lang.Number)"""
        super(_MutableShort, self).add(arg0)

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableShort(java.lang.String)"""
        val = _MutableShort(arg0)
        self.__wrapper = val

    @override
    @overload
    def shortValue(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.shortValue()"""
        return int._wrap(super(MutableShort, self).shortValue())

    @overload
    def incrementAndGet(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.incrementAndGet()"""
        return int._wrap(super(MutableShort, self).incrementAndGet())

    @overload
    def getAndIncrement(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndIncrement()"""
        return int._wrap(super(MutableShort, self).getAndIncrement())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableShort.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableShort, self).equals(arg0))

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.setValue(short)"""
        super(_MutableShort, self).setValue(_short.valueOf(arg0))

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.addAndGet(short)"""
        return int._wrap(super(_MutableShort, self).addAndGet(_short.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableShort.longValue()"""
        return int._wrap(super(MutableShort, self).longValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableShort.floatValue()"""
        return float._wrap(super(MutableShort, self).floatValue())

    @overload
    def getAndDecrement(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndDecrement()"""
        return int._wrap(super(MutableShort, self).getAndDecrement())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableShort.doubleValue()"""
        return float._wrap(super(MutableShort, self).doubleValue())

 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableShort 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableLong
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Long as Long
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import org.apache.commons.lang3.mutable.MutableLong as _MutableLong
_MutableLong = _MutableLong
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableLong():
    """org.apache.commons.lang3.mutable.MutableLong"""
 
    @staticmethod
    def _wrap(java_value: _MutableLong) -> 'MutableLong':
        return MutableLong(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableLong):
        """
        Dynamic initializer for MutableLong.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableLong__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableLong__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableLong.toString()"""
        return str._wrap(super(MutableLong, self).toString())

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableLong.intValue()"""
        return int._wrap(super(MutableLong, self).intValue())

    @overload
    def incrementAndGet(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.incrementAndGet()"""
        return int._wrap(super(MutableLong, self).incrementAndGet())

    @overload
    def compareTo(self, arg0: 'MutableLong') -> int:
        """public int org.apache.commons.lang3.mutable.MutableLong.compareTo(org.apache.commons.lang3.mutable.MutableLong)"""
        return int._wrap(super(_MutableLong, self).compareTo(arg0))

    @overload
    def toLong(self) -> 'Long':
        """public java.lang.Long org.apache.commons.lang3.mutable.MutableLong.toLong()"""
        return _transform(super(MutableLong, self).toLong()).'Long'Value()

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableLong.increment()"""
        super(MutableLong, self).increment()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableLong.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableLong, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndAdd(java.lang.Number)"""
        return int._wrap(super(_MutableLong, self).getAndAdd(arg0))

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableLong.doubleValue()"""
        return float._wrap(super(MutableLong, self).doubleValue())

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableLong.add(java.lang.Number)"""
        super(_MutableLong, self).add(arg0)

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableLong.setValue(java.lang.Number)"""
        super(_MutableLong, self).setValue(arg0)

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.addAndGet(long)"""
        return int._wrap(super(_MutableLong, self).addAndGet(_long.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableLong()"""
        val = _MutableLong()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableLong(java.lang.String)"""
        val = _MutableLong(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableLong.hashCode()"""
        return int._wrap(super(MutableLong, self).hashCode())

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndAdd(long)"""
        return int._wrap(super(_MutableLong, self).getAndAdd(_long.valueOf(arg0)))

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableLong.subtract(java.lang.Number)"""
        super(_MutableLong, self).subtract(arg0)

    @override
    @overload
    def getValue(self) -> 'Long':
        """public java.lang.Long org.apache.commons.lang3.mutable.MutableLong.getValue()"""
        return _transform(super(MutableLong, self).getValue()).'Long'Value()

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableLong(java.lang.Number)"""
        val = _MutableLong(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAndDecrement(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndDecrement()"""
        return int._wrap(super(MutableLong, self).getAndDecrement())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableLong(long)"""
        val = _MutableLong(_long.valueOf(arg0))
        self.__wrapper = val

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableLong.subtract(long)"""
        super(_MutableLong, self).subtract(_long.valueOf(arg0))

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.longValue()"""
        return int._wrap(super(MutableLong, self).longValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableLong.floatValue()"""
        return float._wrap(super(MutableLong, self).floatValue())

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableLong.decrement()"""
        super(MutableLong, self).decrement()

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableLong.add(long)"""
        super(_MutableLong, self).add(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableLong()"""
        val = _MutableLong()
        self.__wrapper = val

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableLong.setValue(long)"""
        super(_MutableLong, self).setValue(_long.valueOf(arg0))

    @overload
    def decrementAndGet(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.decrementAndGet()"""
        return int._wrap(super(MutableLong, self).decrementAndGet())

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.addAndGet(java.lang.Number)"""
        return int._wrap(super(_MutableLong, self).addAndGet(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAndIncrement(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndIncrement()"""
        return int._wrap(super(MutableLong, self).getAndIncrement()) 
 
 
# CLASS: org.apache.commons.lang3.mutable.Mutable
import org.apache.commons.lang3.mutable.Mutable as _Mutable
_Mutable = _Mutable
from abc import abstractmethod, ABC
 
class Mutable():
    """org.apache.commons.lang3.mutable.Mutable"""
 
    @staticmethod
    def _wrap(java_value: _Mutable) -> 'Mutable':
        return Mutable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Mutable):
        """
        Dynamic initializer for Mutable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Mutable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Mutable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract void org.apache.commons.lang3.mutable.Mutable.setValue(T)"""
        pass

    @abstractmethod
    def getValue(self, ):
        """public abstract T org.apache.commons.lang3.mutable.Mutable.getValue()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableInt
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Integer as Integer
import org.apache.commons.lang3.mutable.MutableInt as _MutableInt
_MutableInt = _MutableInt
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableInt():
    """org.apache.commons.lang3.mutable.MutableInt"""
 
    @staticmethod
    def _wrap(java_value: _MutableInt) -> 'MutableInt':
        return MutableInt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableInt):
        """
        Dynamic initializer for MutableInt.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableInt__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableInt__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndAdd(int)"""
        return int._wrap(super(_MutableInt, self).getAndAdd(_int.valueOf(arg0)))

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableInt.add(int)"""
        super(_MutableInt, self).add(_int.valueOf(arg0))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.intValue()"""
        return int._wrap(super(MutableInt, self).intValue())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableInt(int)"""
        val = _MutableInt(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableInt.doubleValue()"""
        return float._wrap(super(MutableInt, self).doubleValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.addAndGet(int)"""
        return int._wrap(super(_MutableInt, self).addAndGet(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableInt.floatValue()"""
        return float._wrap(super(MutableInt, self).floatValue())

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableInt.increment()"""
        super(MutableInt, self).increment()

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @overload
    def compareTo(self, arg0: 'MutableInt') -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.compareTo(org.apache.commons.lang3.mutable.MutableInt)"""
        return int._wrap(super(_MutableInt, self).compareTo(arg0))

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableInt.subtract(java.lang.Number)"""
        super(_MutableInt, self).subtract(arg0)

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableInt.setValue(java.lang.Number)"""
        super(_MutableInt, self).setValue(arg0)

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableInt.subtract(int)"""
        super(_MutableInt, self).subtract(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableInt(java.lang.String)"""
        val = _MutableInt(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableInt.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableInt, self).equals(arg0))

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableInt.decrement()"""
        super(MutableInt, self).decrement()

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndAdd(java.lang.Number)"""
        return int._wrap(super(_MutableInt, self).getAndAdd(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableInt()"""
        val = _MutableInt()
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableInt.add(java.lang.Number)"""
        super(_MutableInt, self).add(arg0)

    @overload
    def getAndDecrement(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndDecrement()"""
        return int._wrap(super(MutableInt, self).getAndDecrement())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableInt(java.lang.Number)"""
        val = _MutableInt(arg0)
        self.__wrapper = val

    @overload
    def incrementAndGet(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.incrementAndGet()"""
        return int._wrap(super(MutableInt, self).incrementAndGet())

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableInt.longValue()"""
        return int._wrap(super(MutableInt, self).longValue())

    @overload
    def toInteger(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.mutable.MutableInt.toInteger()"""
        return _transform(super(MutableInt, self).toInteger()).'Integer'Value()

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableInt.setValue(int)"""
        super(_MutableInt, self).setValue(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableInt()"""
        val = _MutableInt()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.hashCode()"""
        return int._wrap(super(MutableInt, self).hashCode())

    @overload
    def decrementAndGet(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.decrementAndGet()"""
        return int._wrap(super(MutableInt, self).decrementAndGet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAndIncrement(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndIncrement()"""
        return int._wrap(super(MutableInt, self).getAndIncrement())

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.addAndGet(java.lang.Number)"""
        return int._wrap(super(_MutableInt, self).addAndGet(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableInt.toString()"""
        return str._wrap(super(MutableInt, self).toString())

    @override
    @overload
    def getValue(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.mutable.MutableInt.getValue()"""
        return _transform(super(MutableInt, self).getValue()).'Integer'Value() 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableDouble
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Double as _double
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.mutable.MutableDouble as _MutableDouble
_MutableDouble = _MutableDouble
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Double as Double
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableDouble():
    """org.apache.commons.lang3.mutable.MutableDouble"""
 
    @staticmethod
    def _wrap(java_value: _MutableDouble) -> 'MutableDouble':
        return MutableDouble(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableDouble):
        """
        Dynamic initializer for MutableDouble.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableDouble__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableDouble__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableDouble.longValue()"""
        return int._wrap(super(MutableDouble, self).longValue())

    @overload
    def getAndAdd(self, arg0: 'Number') -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndAdd(java.lang.Number)"""
        return float._wrap(super(_MutableDouble, self).getAndAdd(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableDouble.toString()"""
        return str._wrap(super(MutableDouble, self).toString())

    @overload
    def toDouble(self) -> 'Double':
        """public java.lang.Double org.apache.commons.lang3.mutable.MutableDouble.toDouble()"""
        return _transform(super(MutableDouble, self).toDouble()).'Double'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableDouble.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableDouble, self).equals(arg0))

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableDouble.setValue(java.lang.Number)"""
        super(_MutableDouble, self).setValue(arg0)

    @overload
    def incrementAndGet(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.incrementAndGet()"""
        return float._wrap(super(MutableDouble, self).incrementAndGet())

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableDouble.intValue()"""
        return int._wrap(super(MutableDouble, self).intValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableDouble.add(java.lang.Number)"""
        super(_MutableDouble, self).add(arg0)

    @overload
    def getAndDecrement(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndDecrement()"""
        return float._wrap(super(MutableDouble, self).getAndDecrement())

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableDouble(java.lang.String)"""
        val = _MutableDouble(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableDouble.subtract(java.lang.Number)"""
        super(_MutableDouble, self).subtract(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableDouble()"""
        val = _MutableDouble()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def decrementAndGet(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.decrementAndGet()"""
        return float._wrap(super(MutableDouble, self).decrementAndGet())

    @overload
    def add(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableDouble.add(double)"""
        super(_MutableDouble, self).add(_double.valueOf(arg0))

    @overload
    def isNaN(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableDouble.isNaN()"""
        return bool._wrap(super(MutableDouble, self).isNaN())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @override
    @overload
    def getValue(self) -> 'Double':
        """public java.lang.Double org.apache.commons.lang3.mutable.MutableDouble.getValue()"""
        return _transform(super(MutableDouble, self).getValue()).'Double'Value()

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableDouble(java.lang.Number)"""
        val = _MutableDouble(arg0)
        self.__wrapper = val

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableDouble.decrement()"""
        super(MutableDouble, self).decrement()

    @overload
    def __init__(self, arg0: float):
        """public org.apache.commons.lang3.mutable.MutableDouble(double)"""
        val = _MutableDouble(_double.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def compareTo(self, arg0: 'MutableDouble') -> int:
        """public int org.apache.commons.lang3.mutable.MutableDouble.compareTo(org.apache.commons.lang3.mutable.MutableDouble)"""
        return int._wrap(super(_MutableDouble, self).compareTo(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableDouble.hashCode()"""
        return int._wrap(super(MutableDouble, self).hashCode())

    @overload
    def isInfinite(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableDouble.isInfinite()"""
        return bool._wrap(super(MutableDouble, self).isInfinite())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.doubleValue()"""
        return float._wrap(super(MutableDouble, self).doubleValue())

    @overload
    def addAndGet(self, arg0: 'Number') -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.addAndGet(java.lang.Number)"""
        return float._wrap(super(_MutableDouble, self).addAndGet(arg0))

    @overload
    def getAndIncrement(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndIncrement()"""
        return float._wrap(super(MutableDouble, self).getAndIncrement())

    @overload
    def addAndGet(self, arg0: float) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.addAndGet(double)"""
        return float._wrap(super(_MutableDouble, self).addAndGet(_double.valueOf(arg0)))

    @overload
    def getAndAdd(self, arg0: float) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndAdd(double)"""
        return float._wrap(super(_MutableDouble, self).getAndAdd(_double.valueOf(arg0)))

    @overload
    def subtract(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableDouble.subtract(double)"""
        super(_MutableDouble, self).subtract(_double.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableDouble()"""
        val = _MutableDouble()
        self.__wrapper = val

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableDouble.increment()"""
        super(MutableDouble, self).increment()

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableDouble.floatValue()"""
        return float._wrap(super(MutableDouble, self).floatValue())

    @overload
    def setValue(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableDouble.setValue(double)"""
        super(_MutableDouble, self).setValue(_double.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableObject
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
import org.apache.commons.lang3.mutable.MutableObject as _MutableObject
_MutableObject = _MutableObject
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableObject():
    """org.apache.commons.lang3.mutable.MutableObject"""
 
    @staticmethod
    def _wrap(java_value: _MutableObject) -> 'MutableObject':
        return MutableObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableObject):
        """
        Dynamic initializer for MutableObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableObject.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableObject, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableObject()"""
        val = _MutableObject()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableObject.toString()"""
        return str._wrap(super(MutableObject, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableObject.hashCode()"""
        return int._wrap(super(MutableObject, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableObject()"""
        val = _MutableObject()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.mutable.MutableObject(T)"""
        val = _MutableObject(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> object:
        """public T org.apache.commons.lang3.mutable.MutableObject.getValue()"""
        return object._wrap(super(MutableObject, self).getValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setValue(self, arg0: object):
        """public void org.apache.commons.lang3.mutable.MutableObject.setValue(T)"""
        super(_MutableObject, self).setValue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableByte
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import org.apache.commons.lang3.mutable.MutableByte as _MutableByte
_MutableByte = _MutableByte
import java.lang.String as _String
_String = _String
import java.lang.Byte as Byte
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableByte():
    """org.apache.commons.lang3.mutable.MutableByte"""
 
    @staticmethod
    def _wrap(java_value: _MutableByte) -> 'MutableByte':
        return MutableByte(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableByte):
        """
        Dynamic initializer for MutableByte.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableByte__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableByte__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableByte.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableByte, self).equals(arg0))

    @overload
    def getAndDecrement(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndDecrement()"""
        return int._wrap(super(MutableByte, self).getAndDecrement())

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.addAndGet(java.lang.Number)"""
        return int._wrap(super(_MutableByte, self).addAndGet(arg0))

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableByte.doubleValue()"""
        return float._wrap(super(MutableByte, self).doubleValue())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableByte(byte)"""
        val = _MutableByte(_byte.valueOf(arg0))
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.setValue(java.lang.Number)"""
        super(_MutableByte, self).setValue(arg0)

    @overload
    def getAndIncrement(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndIncrement()"""
        return int._wrap(super(MutableByte, self).getAndIncrement())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.add(byte)"""
        super(_MutableByte, self).add(_byte.valueOf(arg0))

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableByte.increment()"""
        super(MutableByte, self).increment()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.add(java.lang.Number)"""
        super(_MutableByte, self).add(arg0)

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableByte()"""
        val = _MutableByte()
        self.__wrapper = val

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableByte(java.lang.Number)"""
        val = _MutableByte(arg0)
        self.__wrapper = val

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndAdd(java.lang.Number)"""
        return int._wrap(super(_MutableByte, self).getAndAdd(arg0))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.byteValue()"""
        return int._wrap(super(MutableByte, self).byteValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableByte.toString()"""
        return str._wrap(super(MutableByte, self).toString())

    @overload
    def incrementAndGet(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.incrementAndGet()"""
        return int._wrap(super(MutableByte, self).incrementAndGet())

    @overload
    def decrementAndGet(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.decrementAndGet()"""
        return int._wrap(super(MutableByte, self).decrementAndGet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableByte()"""
        val = _MutableByte()
        self.__wrapper = val

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.intValue()"""
        return int._wrap(super(MutableByte, self).intValue())

    @overload
    def compareTo(self, arg0: 'MutableByte') -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.compareTo(org.apache.commons.lang3.mutable.MutableByte)"""
        return int._wrap(super(_MutableByte, self).compareTo(arg0))

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.subtract(byte)"""
        super(_MutableByte, self).subtract(_byte.valueOf(arg0))

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.subtract(java.lang.Number)"""
        super(_MutableByte, self).subtract(arg0)

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableByte.decrement()"""
        super(MutableByte, self).decrement()

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndAdd(byte)"""
        return int._wrap(super(_MutableByte, self).getAndAdd(_byte.valueOf(arg0)))

    @overload
    def toByte(self) -> 'Byte':
        """public java.lang.Byte org.apache.commons.lang3.mutable.MutableByte.toByte()"""
        return _transform(super(MutableByte, self).toByte()).'Byte'Value()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableByte(java.lang.String)"""
        val = _MutableByte(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.hashCode()"""
        return int._wrap(super(MutableByte, self).hashCode())

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.setValue(byte)"""
        super(_MutableByte, self).setValue(_byte.valueOf(arg0))

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableByte.floatValue()"""
        return float._wrap(super(MutableByte, self).floatValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableByte.longValue()"""
        return int._wrap(super(MutableByte, self).longValue())

    @override
    @overload
    def getValue(self) -> 'Byte':
        """public java.lang.Byte org.apache.commons.lang3.mutable.MutableByte.getValue()"""
        return _transform(super(MutableByte, self).getValue()).'Byte'Value()

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.addAndGet(byte)"""
        return int._wrap(super(_MutableByte, self).addAndGet(_byte.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableBoolean
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import org.apache.commons.lang3.mutable.MutableBoolean as _MutableBoolean
_MutableBoolean = _MutableBoolean
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableBoolean():
    """org.apache.commons.lang3.mutable.MutableBoolean"""
 
    @staticmethod
    def _wrap(java_value: _MutableBoolean) -> 'MutableBoolean':
        return MutableBoolean(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableBoolean):
        """
        Dynamic initializer for MutableBoolean.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableBoolean__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableBoolean__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableBoolean.hashCode()"""
        return int._wrap(super(MutableBoolean, self).hashCode())

    @overload
    def compareTo(self, arg0: 'MutableBoolean') -> int:
        """public int org.apache.commons.lang3.mutable.MutableBoolean.compareTo(org.apache.commons.lang3.mutable.MutableBoolean)"""
        return int._wrap(super(_MutableBoolean, self).compareTo(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableBoolean()"""
        val = _MutableBoolean()
        self.__wrapper = val

    @overload
    def toBoolean(self) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.lang3.mutable.MutableBoolean.toBoolean()"""
        return 'Boolean'._wrap(super(MutableBoolean, self).toBoolean())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isFalse(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.isFalse()"""
        return bool._wrap(super(MutableBoolean, self).isFalse())

    @override
    @overload
    def getValue(self) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.lang3.mutable.MutableBoolean.getValue()"""
        return 'Boolean'._wrap(super(MutableBoolean, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Boolean'):
        """public org.apache.commons.lang3.mutable.MutableBoolean(java.lang.Boolean)"""
        val = _MutableBoolean(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool):
        """public org.apache.commons.lang3.mutable.MutableBoolean(boolean)"""
        val = _MutableBoolean(_boolean.valueOf(arg0))
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'Boolean'):
        """public void org.apache.commons.lang3.mutable.MutableBoolean.setValue(java.lang.Boolean)"""
        super(_MutableBoolean, self).setValue(arg0)

    @overload
    def booleanValue(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.booleanValue()"""
        return bool._wrap(super(MutableBoolean, self).booleanValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableBoolean.toString()"""
        return str._wrap(super(MutableBoolean, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableBoolean, self).equals(arg0))

    @overload
    def setValue(self, arg0: bool):
        """public void org.apache.commons.lang3.mutable.MutableBoolean.setValue(boolean)"""
        super(_MutableBoolean, self).setValue(_boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setFalse(self):
        """public void org.apache.commons.lang3.mutable.MutableBoolean.setFalse()"""
        super(MutableBoolean, self).setFalse()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableBoolean()"""
        val = _MutableBoolean()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTrue(self):
        """public void org.apache.commons.lang3.mutable.MutableBoolean.setTrue()"""
        super(MutableBoolean, self).setTrue()

    @overload
    def isTrue(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.isTrue()"""
        return bool._wrap(super(MutableBoolean, self).isTrue()) 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableFloat
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.mutable.MutableFloat as _MutableFloat
_MutableFloat = _MutableFloat
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.Float as Float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableFloat():
    """org.apache.commons.lang3.mutable.MutableFloat"""
 
    @staticmethod
    def _wrap(java_value: _MutableFloat) -> 'MutableFloat':
        return MutableFloat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableFloat):
        """
        Dynamic initializer for MutableFloat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableFloat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableFloat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableFloat.setValue(java.lang.Number)"""
        super(_MutableFloat, self).setValue(arg0)

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableFloat.increment()"""
        super(MutableFloat, self).increment()

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableFloat.subtract(java.lang.Number)"""
        super(_MutableFloat, self).subtract(arg0)

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.floatValue()"""
        return float._wrap(super(MutableFloat, self).floatValue())

    @overload
    def incrementAndGet(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.incrementAndGet()"""
        return float._wrap(super(MutableFloat, self).incrementAndGet())

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableFloat.intValue()"""
        return int._wrap(super(MutableFloat, self).intValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addAndGet(self, arg0: float) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.addAndGet(float)"""
        return float._wrap(super(_MutableFloat, self).addAndGet(_float.valueOf(arg0)))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableFloat.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableFloat, self).equals(arg0))

    @overload
    def isInfinite(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableFloat.isInfinite()"""
        return bool._wrap(super(MutableFloat, self).isInfinite())

    @overload
    def toFloat(self) -> 'Float':
        """public java.lang.Float org.apache.commons.lang3.mutable.MutableFloat.toFloat()"""
        return _transform(super(MutableFloat, self).toFloat()).'Float'Value()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableFloat()"""
        val = _MutableFloat()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getAndDecrement(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndDecrement()"""
        return float._wrap(super(MutableFloat, self).getAndDecrement())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compareTo(self, arg0: 'MutableFloat') -> int:
        """public int org.apache.commons.lang3.mutable.MutableFloat.compareTo(org.apache.commons.lang3.mutable.MutableFloat)"""
        return int._wrap(super(_MutableFloat, self).compareTo(arg0))

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableFloat.doubleValue()"""
        return float._wrap(super(MutableFloat, self).doubleValue())

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableFloat(java.lang.Number)"""
        val = _MutableFloat(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float):
        """public org.apache.commons.lang3.mutable.MutableFloat(float)"""
        val = _MutableFloat(_float.valueOf(arg0))
        self.__wrapper = val

    @overload
    def add(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableFloat.add(float)"""
        super(_MutableFloat, self).add(_float.valueOf(arg0))

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableFloat.add(java.lang.Number)"""
        super(_MutableFloat, self).add(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableFloat.hashCode()"""
        return int._wrap(super(MutableFloat, self).hashCode())

    @override
    @overload
    def getValue(self) -> 'Float':
        """public java.lang.Float org.apache.commons.lang3.mutable.MutableFloat.getValue()"""
        return _transform(super(MutableFloat, self).getValue()).'Float'Value()

    @overload
    def getAndAdd(self, arg0: float) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndAdd(float)"""
        return float._wrap(super(_MutableFloat, self).getAndAdd(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableFloat(java.lang.String)"""
        val = _MutableFloat(arg0)
        self.__wrapper = val

    @overload
    def getAndAdd(self, arg0: 'Number') -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndAdd(java.lang.Number)"""
        return float._wrap(super(_MutableFloat, self).getAndAdd(arg0))

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableFloat.decrement()"""
        super(MutableFloat, self).decrement()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def subtract(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableFloat.subtract(float)"""
        super(_MutableFloat, self).subtract(_float.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableFloat()"""
        val = _MutableFloat()
        self.__wrapper = val

    @overload
    def getAndIncrement(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndIncrement()"""
        return float._wrap(super(MutableFloat, self).getAndIncrement())

    @overload
    def setValue(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableFloat.setValue(float)"""
        super(_MutableFloat, self).setValue(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def decrementAndGet(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.decrementAndGet()"""
        return float._wrap(super(MutableFloat, self).decrementAndGet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableFloat.toString()"""
        return str._wrap(super(MutableFloat, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isNaN(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableFloat.isNaN()"""
        return bool._wrap(super(MutableFloat, self).isNaN())

    @overload
    def addAndGet(self, arg0: 'Number') -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.addAndGet(java.lang.Number)"""
        return float._wrap(super(_MutableFloat, self).addAndGet(arg0))

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableFloat.longValue()"""
        return int._wrap(super(MutableFloat, self).longValue())