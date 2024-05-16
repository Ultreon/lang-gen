from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import transform as __transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Byte as Byte
import org.apache.commons.lang3.mutable.MutableByte as __MutableByte
__MutableByte = __MutableByte
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Byte as __byte
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class MutableByte(__Number, Number, __Comparable, Comparable, __Mutable, Mutable):
    """org.apache.commons.lang3.mutable.MutableByte"""
 
    @staticmethod
    def __wrap(java_value: __MutableByte) -> 'MutableByte':
        return MutableByte(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableByte):
        """
        Dynamic initializer for MutableByte.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndAdd(java.lang.Number)"""
        return int.__wrap(super(__MutableByte, self).getAndAdd(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.add(byte)"""
        super(__MutableByte, self).add(__byte.valueOf(arg0))

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.addAndGet(java.lang.Number)"""
        return int.__wrap(super(__MutableByte, self).addAndGet(arg0))

    @overload
    def compareTo(self, arg0: 'MutableByte') -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.compareTo(org.apache.commons.lang3.mutable.MutableByte)"""
        return int.__wrap(super(__MutableByte, self).compareTo(arg0))

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableByte.doubleValue()"""
        return float.__wrap(super(MutableByte, self).doubleValue())

    @overload
    def incrementAndGet(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.incrementAndGet()"""
        return int.__wrap(super(MutableByte, self).incrementAndGet())

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableByte.increment()"""
        super(MutableByte, self).increment()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableByte()"""
        val = __MutableByte()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableByte.longValue()"""
        return int.__wrap(super(MutableByte, self).longValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAndIncrement(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndIncrement()"""
        return int.__wrap(super(MutableByte, self).getAndIncrement())

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableByte(java.lang.Number)"""
        val = __MutableByte(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def decrementAndGet(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.decrementAndGet()"""
        return int.__wrap(super(MutableByte, self).decrementAndGet())

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.setValue(byte)"""
        super(__MutableByte, self).setValue(__byte.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableByte()"""
        val = __MutableByte()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.setValue(java.lang.Number)"""
        super(__MutableByte, self).setValue(arg0)

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.subtract(java.lang.Number)"""
        super(__MutableByte, self).subtract(arg0)

    @override
    @overload
    def getValue(self) -> 'Byte':
        """public java.lang.Byte org.apache.commons.lang3.mutable.MutableByte.getValue()"""
        return __transform(super(MutableByte, self).getValue()).'Byte'Value()

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.add(java.lang.Number)"""
        super(__MutableByte, self).add(arg0)

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableByte(byte)"""
        val = __MutableByte(__byte.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableByte.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableByte, self).equals(arg0))

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.addAndGet(byte)"""
        return int.__wrap(super(__MutableByte, self).addAndGet(__byte.valueOf(arg0)))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.intValue()"""
        return int.__wrap(super(MutableByte, self).intValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableByte.floatValue()"""
        return float.__wrap(super(MutableByte, self).floatValue())

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.subtract(byte)"""
        super(__MutableByte, self).subtract(__byte.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.byteValue()"""
        return int.__wrap(super(MutableByte, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndAdd(byte)"""
        return int.__wrap(super(__MutableByte, self).getAndAdd(__byte.valueOf(arg0)))

    @overload
    def toByte(self) -> 'Byte':
        """public java.lang.Byte org.apache.commons.lang3.mutable.MutableByte.toByte()"""
        return __transform(super(MutableByte, self).toByte()).'Byte'Value()

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableByte.decrement()"""
        super(MutableByte, self).decrement()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableByte.toString()"""
        return str.__wrap(super(MutableByte, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.hashCode()"""
        return int.__wrap(super(MutableByte, self).hashCode())

    @overload
    def getAndDecrement(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndDecrement()"""
        return int.__wrap(super(MutableByte, self).getAndDecrement())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableByte(java.lang.String)"""
        val = __MutableByte(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableByte
from builtins import str
from pyquantum_helper import transform as __transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Byte as Byte
import org.apache.commons.lang3.mutable.MutableByte as __MutableByte
__MutableByte = __MutableByte
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Byte as __byte
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class MutableByte(__Number, Number, __Comparable, Comparable, __Mutable, Mutable):
    """org.apache.commons.lang3.mutable.MutableByte"""
 
    @staticmethod
    def __wrap(java_value: __MutableByte) -> 'MutableByte':
        return MutableByte(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableByte):
        """
        Dynamic initializer for MutableByte.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndAdd(java.lang.Number)"""
        return int.__wrap(super(__MutableByte, self).getAndAdd(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.add(byte)"""
        super(__MutableByte, self).add(__byte.valueOf(arg0))

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.addAndGet(java.lang.Number)"""
        return int.__wrap(super(__MutableByte, self).addAndGet(arg0))

    @overload
    def compareTo(self, arg0: 'MutableByte') -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.compareTo(org.apache.commons.lang3.mutable.MutableByte)"""
        return int.__wrap(super(__MutableByte, self).compareTo(arg0))

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableByte.doubleValue()"""
        return float.__wrap(super(MutableByte, self).doubleValue())

    @overload
    def incrementAndGet(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.incrementAndGet()"""
        return int.__wrap(super(MutableByte, self).incrementAndGet())

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableByte.increment()"""
        super(MutableByte, self).increment()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableByte()"""
        val = __MutableByte()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableByte.longValue()"""
        return int.__wrap(super(MutableByte, self).longValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAndIncrement(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndIncrement()"""
        return int.__wrap(super(MutableByte, self).getAndIncrement())

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableByte(java.lang.Number)"""
        val = __MutableByte(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def decrementAndGet(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.decrementAndGet()"""
        return int.__wrap(super(MutableByte, self).decrementAndGet())

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.setValue(byte)"""
        super(__MutableByte, self).setValue(__byte.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableByte()"""
        val = __MutableByte()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.setValue(java.lang.Number)"""
        super(__MutableByte, self).setValue(arg0)

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.subtract(java.lang.Number)"""
        super(__MutableByte, self).subtract(arg0)

    @override
    @overload
    def getValue(self) -> 'Byte':
        """public java.lang.Byte org.apache.commons.lang3.mutable.MutableByte.getValue()"""
        return __transform(super(MutableByte, self).getValue()).'Byte'Value()

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableByte.add(java.lang.Number)"""
        super(__MutableByte, self).add(arg0)

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableByte(byte)"""
        val = __MutableByte(__byte.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableByte.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableByte, self).equals(arg0))

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.addAndGet(byte)"""
        return int.__wrap(super(__MutableByte, self).addAndGet(__byte.valueOf(arg0)))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.intValue()"""
        return int.__wrap(super(MutableByte, self).intValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableByte.floatValue()"""
        return float.__wrap(super(MutableByte, self).floatValue())

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableByte.subtract(byte)"""
        super(__MutableByte, self).subtract(__byte.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.byteValue()"""
        return int.__wrap(super(MutableByte, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndAdd(byte)"""
        return int.__wrap(super(__MutableByte, self).getAndAdd(__byte.valueOf(arg0)))

    @overload
    def toByte(self) -> 'Byte':
        """public java.lang.Byte org.apache.commons.lang3.mutable.MutableByte.toByte()"""
        return __transform(super(MutableByte, self).toByte()).'Byte'Value()

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableByte.decrement()"""
        super(MutableByte, self).decrement()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableByte.toString()"""
        return str.__wrap(super(MutableByte, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableByte.hashCode()"""
        return int.__wrap(super(MutableByte, self).hashCode())

    @overload
    def getAndDecrement(self) -> int:
        """public byte org.apache.commons.lang3.mutable.MutableByte.getAndDecrement()"""
        return int.__wrap(super(MutableByte, self).getAndDecrement())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableByte(java.lang.String)"""
        val = __MutableByte(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableByte 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableLong
from builtins import str
from pyquantum_helper import transform as __transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Long as Long
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.mutable.MutableLong as __MutableLong
__MutableLong = __MutableLong
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class MutableLong(__Number, Number, __Comparable, Comparable, __Mutable, Mutable):
    """org.apache.commons.lang3.mutable.MutableLong"""
 
    @staticmethod
    def __wrap(java_value: __MutableLong) -> 'MutableLong':
        return MutableLong(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableLong):
        """
        Dynamic initializer for MutableLong.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableLong()"""
        val = __MutableLong()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableLong.add(long)"""
        super(__MutableLong, self).add(__long.valueOf(arg0))

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableLong.increment()"""
        super(MutableLong, self).increment()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.addAndGet(java.lang.Number)"""
        return int.__wrap(super(__MutableLong, self).addAndGet(arg0))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableLong(long)"""
        val = __MutableLong(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableLong.add(java.lang.Number)"""
        super(__MutableLong, self).add(arg0)

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableLong.setValue(java.lang.Number)"""
        super(__MutableLong, self).setValue(arg0)

    @overload
    def getAndDecrement(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndDecrement()"""
        return int.__wrap(super(MutableLong, self).getAndDecrement())

    @overload
    def compareTo(self, arg0: 'MutableLong') -> int:
        """public int org.apache.commons.lang3.mutable.MutableLong.compareTo(org.apache.commons.lang3.mutable.MutableLong)"""
        return int.__wrap(super(__MutableLong, self).compareTo(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableLong.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableLong, self).equals(arg0))

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.addAndGet(long)"""
        return int.__wrap(super(__MutableLong, self).addAndGet(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableLong.floatValue()"""
        return float.__wrap(super(MutableLong, self).floatValue())

    @overload
    def toLong(self) -> 'Long':
        """public java.lang.Long org.apache.commons.lang3.mutable.MutableLong.toLong()"""
        return __transform(super(MutableLong, self).toLong()).'Long'Value()

    @override
    @overload
    def getValue(self) -> 'Long':
        """public java.lang.Long org.apache.commons.lang3.mutable.MutableLong.getValue()"""
        return __transform(super(MutableLong, self).getValue()).'Long'Value()

    @overload
    def incrementAndGet(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.incrementAndGet()"""
        return int.__wrap(super(MutableLong, self).incrementAndGet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableLong.hashCode()"""
        return int.__wrap(super(MutableLong, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableLong(java.lang.String)"""
        val = __MutableLong(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableLong.setValue(long)"""
        super(__MutableLong, self).setValue(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableLong.toString()"""
        return str.__wrap(super(MutableLong, self).toString())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.longValue()"""
        return int.__wrap(super(MutableLong, self).longValue())

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndAdd(long)"""
        return int.__wrap(super(__MutableLong, self).getAndAdd(__long.valueOf(arg0)))

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableLong.subtract(long)"""
        super(__MutableLong, self).subtract(__long.valueOf(arg0))

    @overload
    def decrementAndGet(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.decrementAndGet()"""
        return int.__wrap(super(MutableLong, self).decrementAndGet())

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableLong.decrement()"""
        super(MutableLong, self).decrement()

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableLong.subtract(java.lang.Number)"""
        super(__MutableLong, self).subtract(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableLong()"""
        val = __MutableLong()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableLong.intValue()"""
        return int.__wrap(super(MutableLong, self).intValue())

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableLong.doubleValue()"""
        return float.__wrap(super(MutableLong, self).doubleValue())

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndAdd(java.lang.Number)"""
        return int.__wrap(super(__MutableLong, self).getAndAdd(arg0))

    @overload
    def getAndIncrement(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableLong.getAndIncrement()"""
        return int.__wrap(super(MutableLong, self).getAndIncrement())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableLong(java.lang.Number)"""
        val = __MutableLong(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableFloat
from builtins import str
from pyquantum_helper import transform as __transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Float as Float
import org.apache.commons.lang3.mutable.MutableFloat as __MutableFloat
__MutableFloat = __MutableFloat
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class MutableFloat(__Number, Number, __Comparable, Comparable, __Mutable, Mutable):
    """org.apache.commons.lang3.mutable.MutableFloat"""
 
    @staticmethod
    def __wrap(java_value: __MutableFloat) -> 'MutableFloat':
        return MutableFloat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableFloat):
        """
        Dynamic initializer for MutableFloat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.floatValue()"""
        return float.__wrap(super(MutableFloat, self).floatValue())

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableFloat.add(java.lang.Number)"""
        super(__MutableFloat, self).add(arg0)

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableFloat.increment()"""
        super(MutableFloat, self).increment()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableFloat.toString()"""
        return str.__wrap(super(MutableFloat, self).toString())

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableFloat(java.lang.Number)"""
        val = __MutableFloat(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAndAdd(self, arg0: float) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndAdd(float)"""
        return float.__wrap(super(__MutableFloat, self).getAndAdd(__float.valueOf(arg0)))

    @overload
    def incrementAndGet(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.incrementAndGet()"""
        return float.__wrap(super(MutableFloat, self).incrementAndGet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableFloat.doubleValue()"""
        return float.__wrap(super(MutableFloat, self).doubleValue())

    @overload
    def addAndGet(self, arg0: float) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.addAndGet(float)"""
        return float.__wrap(super(__MutableFloat, self).addAndGet(__float.valueOf(arg0)))

    @overload
    def getAndIncrement(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndIncrement()"""
        return float.__wrap(super(MutableFloat, self).getAndIncrement())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableFloat()"""
        val = __MutableFloat()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isInfinite(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableFloat.isInfinite()"""
        return bool.__wrap(super(MutableFloat, self).isInfinite())

    @overload
    def add(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableFloat.add(float)"""
        super(__MutableFloat, self).add(__float.valueOf(arg0))

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableFloat.setValue(java.lang.Number)"""
        super(__MutableFloat, self).setValue(arg0)

    @overload
    def getAndAdd(self, arg0: 'Number') -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndAdd(java.lang.Number)"""
        return float.__wrap(super(__MutableFloat, self).getAndAdd(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableFloat()"""
        val = __MutableFloat()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableFloat.hashCode()"""
        return int.__wrap(super(MutableFloat, self).hashCode())

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableFloat.subtract(java.lang.Number)"""
        super(__MutableFloat, self).subtract(arg0)

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @overload
    def isNaN(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableFloat.isNaN()"""
        return bool.__wrap(super(MutableFloat, self).isNaN())

    @overload
    def getAndDecrement(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.getAndDecrement()"""
        return float.__wrap(super(MutableFloat, self).getAndDecrement())

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableFloat.decrement()"""
        super(MutableFloat, self).decrement()

    @overload
    def compareTo(self, arg0: 'MutableFloat') -> int:
        """public int org.apache.commons.lang3.mutable.MutableFloat.compareTo(org.apache.commons.lang3.mutable.MutableFloat)"""
        return int.__wrap(super(__MutableFloat, self).compareTo(arg0))

    @overload
    def decrementAndGet(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.decrementAndGet()"""
        return float.__wrap(super(MutableFloat, self).decrementAndGet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def subtract(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableFloat.subtract(float)"""
        super(__MutableFloat, self).subtract(__float.valueOf(arg0))

    @overload
    def toFloat(self) -> 'Float':
        """public java.lang.Float org.apache.commons.lang3.mutable.MutableFloat.toFloat()"""
        return __transform(super(MutableFloat, self).toFloat()).'Float'Value()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableFloat.intValue()"""
        return int.__wrap(super(MutableFloat, self).intValue())

    @overload
    def __init__(self, arg0: float):
        """public org.apache.commons.lang3.mutable.MutableFloat(float)"""
        val = __MutableFloat(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAndGet(self, arg0: 'Number') -> float:
        """public float org.apache.commons.lang3.mutable.MutableFloat.addAndGet(java.lang.Number)"""
        return float.__wrap(super(__MutableFloat, self).addAndGet(arg0))

    @overload
    def setValue(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableFloat.setValue(float)"""
        super(__MutableFloat, self).setValue(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getValue(self) -> 'Float':
        """public java.lang.Float org.apache.commons.lang3.mutable.MutableFloat.getValue()"""
        return __transform(super(MutableFloat, self).getValue()).'Float'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableFloat.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableFloat, self).equals(arg0))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableFloat(java.lang.String)"""
        val = __MutableFloat(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableFloat.longValue()"""
        return int.__wrap(super(MutableFloat, self).longValue()) 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableInt
from builtins import str
from pyquantum_helper import transform as __transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import org.apache.commons.lang3.mutable.MutableInt as __MutableInt
__MutableInt = __MutableInt
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class MutableInt(__Number, Number, __Comparable, Comparable, __Mutable, Mutable):
    """org.apache.commons.lang3.mutable.MutableInt"""
 
    @staticmethod
    def __wrap(java_value: __MutableInt) -> 'MutableInt':
        return MutableInt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableInt):
        """
        Dynamic initializer for MutableInt.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.hashCode()"""
        return int.__wrap(super(MutableInt, self).hashCode())

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndAdd(java.lang.Number)"""
        return int.__wrap(super(__MutableInt, self).getAndAdd(arg0))

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableInt.subtract(java.lang.Number)"""
        super(__MutableInt, self).subtract(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableInt()"""
        val = __MutableInt()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableInt.longValue()"""
        return int.__wrap(super(MutableInt, self).longValue())

    @overload
    def getAndIncrement(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndIncrement()"""
        return int.__wrap(super(MutableInt, self).getAndIncrement())

    @override
    @overload
    def getValue(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.mutable.MutableInt.getValue()"""
        return __transform(super(MutableInt, self).getValue()).'Integer'Value()

    @overload
    def decrementAndGet(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.decrementAndGet()"""
        return int.__wrap(super(MutableInt, self).decrementAndGet())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableInt.floatValue()"""
        return float.__wrap(super(MutableInt, self).floatValue())

    @overload
    def compareTo(self, arg0: 'MutableInt') -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.compareTo(org.apache.commons.lang3.mutable.MutableInt)"""
        return int.__wrap(super(__MutableInt, self).compareTo(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableInt.doubleValue()"""
        return float.__wrap(super(MutableInt, self).doubleValue())

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableInt.add(java.lang.Number)"""
        super(__MutableInt, self).add(arg0)

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableInt.add(int)"""
        super(__MutableInt, self).add(__int.valueOf(arg0))

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableInt.setValue(java.lang.Number)"""
        super(__MutableInt, self).setValue(arg0)

    @overload
    def incrementAndGet(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.incrementAndGet()"""
        return int.__wrap(super(MutableInt, self).incrementAndGet())

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.addAndGet(int)"""
        return int.__wrap(super(__MutableInt, self).addAndGet(__int.valueOf(arg0)))

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableInt.increment()"""
        super(MutableInt, self).increment()

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.intValue()"""
        return int.__wrap(super(MutableInt, self).intValue())

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndAdd(int)"""
        return int.__wrap(super(__MutableInt, self).getAndAdd(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableInt(java.lang.String)"""
        val = __MutableInt(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableInt(java.lang.Number)"""
        val = __MutableInt(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAndDecrement(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.getAndDecrement()"""
        return int.__wrap(super(MutableInt, self).getAndDecrement())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableInt(int)"""
        val = __MutableInt(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableInt.decrement()"""
        super(MutableInt, self).decrement()

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableInt.subtract(int)"""
        super(__MutableInt, self).subtract(__int.valueOf(arg0))

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableInt.setValue(int)"""
        super(__MutableInt, self).setValue(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableInt.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableInt, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableInt.toString()"""
        return str.__wrap(super(MutableInt, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toInteger(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.mutable.MutableInt.toInteger()"""
        return __transform(super(MutableInt, self).toInteger()).'Integer'Value()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableInt()"""
        val = __MutableInt()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public int org.apache.commons.lang3.mutable.MutableInt.addAndGet(java.lang.Number)"""
        return int.__wrap(super(__MutableInt, self).addAndGet(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableObject
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.mutable.MutableObject as __MutableObject
__MutableObject = __MutableObject
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MutableObject(__Mutable, Mutable, __Serializable, Serializable):
    """org.apache.commons.lang3.mutable.MutableObject"""
 
    @staticmethod
    def __wrap(java_value: __MutableObject) -> 'MutableObject':
        return MutableObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableObject):
        """
        Dynamic initializer for MutableObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.mutable.MutableObject(T)"""
        val = __MutableObject(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableObject.toString()"""
        return str.__wrap(super(MutableObject, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableObject()"""
        val = __MutableObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getValue(self) -> object:
        """public T org.apache.commons.lang3.mutable.MutableObject.getValue()"""
        return object.__wrap(super(MutableObject, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableObject.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableObject, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableObject.hashCode()"""
        return int.__wrap(super(MutableObject, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setValue(self, arg0: object):
        """public void org.apache.commons.lang3.mutable.MutableObject.setValue(T)"""
        super(__MutableObject, self).setValue(arg0)

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableObject()"""
        val = __MutableObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableDouble
from builtins import str
from pyquantum_helper import transform as __transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import org.apache.commons.lang3.mutable.MutableDouble as __MutableDouble
__MutableDouble = __MutableDouble
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
import java.lang.Double as Double
from builtins import int
 
class MutableDouble(__Number, Number, __Comparable, Comparable, __Mutable, Mutable):
    """org.apache.commons.lang3.mutable.MutableDouble"""
 
    @staticmethod
    def __wrap(java_value: __MutableDouble) -> 'MutableDouble':
        return MutableDouble(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableDouble):
        """
        Dynamic initializer for MutableDouble.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def compareTo(self, arg0: 'MutableDouble') -> int:
        """public int org.apache.commons.lang3.mutable.MutableDouble.compareTo(org.apache.commons.lang3.mutable.MutableDouble)"""
        return int.__wrap(super(__MutableDouble, self).compareTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableDouble.toString()"""
        return str.__wrap(super(MutableDouble, self).toString())

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableDouble.setValue(java.lang.Number)"""
        super(__MutableDouble, self).setValue(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> 'Double':
        """public java.lang.Double org.apache.commons.lang3.mutable.MutableDouble.getValue()"""
        return __transform(super(MutableDouble, self).getValue()).'Double'Value()

    @overload
    def isInfinite(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableDouble.isInfinite()"""
        return bool.__wrap(super(MutableDouble, self).isInfinite())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableDouble()"""
        val = __MutableDouble()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAndAdd(self, arg0: float) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndAdd(double)"""
        return float.__wrap(super(__MutableDouble, self).getAndAdd(__double.valueOf(arg0)))

    @overload
    def getAndIncrement(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndIncrement()"""
        return float.__wrap(super(MutableDouble, self).getAndIncrement())

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableDouble.add(java.lang.Number)"""
        super(__MutableDouble, self).add(arg0)

    @overload
    def getAndDecrement(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndDecrement()"""
        return float.__wrap(super(MutableDouble, self).getAndDecrement())

    @overload
    def incrementAndGet(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.incrementAndGet()"""
        return float.__wrap(super(MutableDouble, self).incrementAndGet())

    @overload
    def setValue(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableDouble.setValue(double)"""
        super(__MutableDouble, self).setValue(__double.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableDouble.intValue()"""
        return int.__wrap(super(MutableDouble, self).intValue())

    @overload
    def getAndAdd(self, arg0: 'Number') -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.getAndAdd(java.lang.Number)"""
        return float.__wrap(super(__MutableDouble, self).getAndAdd(arg0))

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableDouble(java.lang.Number)"""
        val = __MutableDouble(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableDouble.longValue()"""
        return int.__wrap(super(MutableDouble, self).longValue())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.doubleValue()"""
        return float.__wrap(super(MutableDouble, self).doubleValue())

    @overload
    def __init__(self, arg0: float):
        """public org.apache.commons.lang3.mutable.MutableDouble(double)"""
        val = __MutableDouble(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableDouble.floatValue()"""
        return float.__wrap(super(MutableDouble, self).floatValue())

    @overload
    def addAndGet(self, arg0: 'Number') -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.addAndGet(java.lang.Number)"""
        return float.__wrap(super(__MutableDouble, self).addAndGet(arg0))

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableDouble.decrement()"""
        super(MutableDouble, self).decrement()

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableDouble(java.lang.String)"""
        val = __MutableDouble(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toDouble(self) -> 'Double':
        """public java.lang.Double org.apache.commons.lang3.mutable.MutableDouble.toDouble()"""
        return __transform(super(MutableDouble, self).toDouble()).'Double'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableDouble.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableDouble, self).equals(arg0))

    @overload
    def addAndGet(self, arg0: float) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.addAndGet(double)"""
        return float.__wrap(super(__MutableDouble, self).addAndGet(__double.valueOf(arg0)))

    @overload
    def add(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableDouble.add(double)"""
        super(__MutableDouble, self).add(__double.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableDouble.hashCode()"""
        return int.__wrap(super(MutableDouble, self).hashCode())

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableDouble.increment()"""
        super(MutableDouble, self).increment()

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableDouble.subtract(java.lang.Number)"""
        super(__MutableDouble, self).subtract(arg0)

    @overload
    def isNaN(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableDouble.isNaN()"""
        return bool.__wrap(super(MutableDouble, self).isNaN())

    @overload
    def decrementAndGet(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableDouble.decrementAndGet()"""
        return float.__wrap(super(MutableDouble, self).decrementAndGet())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableDouble()"""
        val = __MutableDouble()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def subtract(self, arg0: float):
        """public void org.apache.commons.lang3.mutable.MutableDouble.subtract(double)"""
        super(__MutableDouble, self).subtract(__double.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.mutable.Mutable
import org.apache.commons.lang3.mutable.Mutable as __Mutable
__Mutable = __Mutable
from abc import abstractmethod, ABC
 
class Mutable(ABC):
    """org.apache.commons.lang3.mutable.Mutable"""
 
    @staticmethod
    def __wrap(java_value: __Mutable) -> 'Mutable':
        return Mutable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Mutable):
        """
        Dynamic initializer for Mutable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableShort
from builtins import str
from pyquantum_helper import transform as __transform
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Short as Short
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.lang3.mutable.MutableShort as __MutableShort
__MutableShort = __MutableShort
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class MutableShort(__Number, Number, __Comparable, Comparable, __Mutable, Mutable):
    """org.apache.commons.lang3.mutable.MutableShort"""
 
    @staticmethod
    def __wrap(java_value: __MutableShort) -> 'MutableShort':
        return MutableShort(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableShort):
        """
        Dynamic initializer for MutableShort.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableShort.toString()"""
        return str.__wrap(super(MutableShort, self).toString())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.mutable.MutableShort.doubleValue()"""
        return float.__wrap(super(MutableShort, self).doubleValue())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableShort()"""
        val = __MutableShort()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableShort.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableShort, self).equals(arg0))

    @overload
    def decrement(self):
        """public void org.apache.commons.lang3.mutable.MutableShort.decrement()"""
        super(MutableShort, self).decrement()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def subtract(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.subtract(short)"""
        super(__MutableShort, self).subtract(__short.valueOf(arg0))

    @overload
    def incrementAndGet(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.incrementAndGet()"""
        return int.__wrap(super(MutableShort, self).incrementAndGet())

    @overload
    def add(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.add(java.lang.Number)"""
        super(__MutableShort, self).add(arg0)

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.mutable.MutableShort(java.lang.String)"""
        val = __MutableShort(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAndDecrement(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndDecrement()"""
        return int.__wrap(super(MutableShort, self).getAndDecrement())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.mutable.MutableShort.longValue()"""
        return int.__wrap(super(MutableShort, self).longValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.mutable.MutableShort.floatValue()"""
        return float.__wrap(super(MutableShort, self).floatValue())

    @overload
    def setValue(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.setValue(java.lang.Number)"""
        super(__MutableShort, self).setValue(arg0)

    @overload
    def getAndAdd(self, arg0: 'Number') -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndAdd(java.lang.Number)"""
        return int.__wrap(super(__MutableShort, self).getAndAdd(arg0))

    @overload
    def addAndGet(self, arg0: 'Number') -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.addAndGet(java.lang.Number)"""
        return int.__wrap(super(__MutableShort, self).addAndGet(arg0))

    @override
    @overload
    def getValue(self) -> 'Short':
        """public java.lang.Short org.apache.commons.lang3.mutable.MutableShort.getValue()"""
        return __transform(super(MutableShort, self).getValue()).'Short'Value()

    @overload
    def getAndAdd(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndAdd(short)"""
        return int.__wrap(super(__MutableShort, self).getAndAdd(__short.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.hashCode()"""
        return int.__wrap(super(MutableShort, self).hashCode())

    @overload
    def increment(self):
        """public void org.apache.commons.lang3.mutable.MutableShort.increment()"""
        super(MutableShort, self).increment()

    @overload
    def subtract(self, arg0: 'Number'):
        """public void org.apache.commons.lang3.mutable.MutableShort.subtract(java.lang.Number)"""
        super(__MutableShort, self).subtract(arg0)

    @overload
    def toShort(self) -> 'Short':
        """public java.lang.Short org.apache.commons.lang3.mutable.MutableShort.toShort()"""
        return __transform(super(MutableShort, self).toShort()).'Short'Value()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableShort()"""
        val = __MutableShort()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def add(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.add(short)"""
        super(__MutableShort, self).add(__short.valueOf(arg0))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.intValue()"""
        return int.__wrap(super(MutableShort, self).intValue())

    @overload
    def getAndIncrement(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.getAndIncrement()"""
        return int.__wrap(super(MutableShort, self).getAndIncrement())

    @overload
    def __init__(self, arg0: 'Number'):
        """public org.apache.commons.lang3.mutable.MutableShort(java.lang.Number)"""
        val = __MutableShort(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def decrementAndGet(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.decrementAndGet()"""
        return int.__wrap(super(MutableShort, self).decrementAndGet())

    @overload
    def compareTo(self, arg0: 'MutableShort') -> int:
        """public int org.apache.commons.lang3.mutable.MutableShort.compareTo(org.apache.commons.lang3.mutable.MutableShort)"""
        return int.__wrap(super(__MutableShort, self).compareTo(arg0))

    @overload
    def setValue(self, arg0: int):
        """public void org.apache.commons.lang3.mutable.MutableShort.setValue(short)"""
        super(__MutableShort, self).setValue(__short.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def shortValue(self) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.shortValue()"""
        return int.__wrap(super(MutableShort, self).shortValue())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.mutable.MutableShort(short)"""
        val = __MutableShort(__short.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAndGet(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.mutable.MutableShort.addAndGet(short)"""
        return int.__wrap(super(__MutableShort, self).addAndGet(__short.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.mutable.MutableBoolean
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import org.apache.commons.lang3.mutable.MutableBoolean as __MutableBoolean
__MutableBoolean = __MutableBoolean
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MutableBoolean(__Mutable, Mutable, __Serializable, Serializable, __Comparable, Comparable):
    """org.apache.commons.lang3.mutable.MutableBoolean"""
 
    @staticmethod
    def __wrap(java_value: __MutableBoolean) -> 'MutableBoolean':
        return MutableBoolean(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableBoolean):
        """
        Dynamic initializer for MutableBoolean.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.mutable.MutableBoolean.hashCode()"""
        return int.__wrap(super(MutableBoolean, self).hashCode())

    @overload
    def booleanValue(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.booleanValue()"""
        return bool.__wrap(super(MutableBoolean, self).booleanValue())

    @overload
    def isTrue(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.isTrue()"""
        return bool.__wrap(super(MutableBoolean, self).isTrue())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.mutable.MutableBoolean()"""
        val = __MutableBoolean()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableBoolean, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.mutable.MutableBoolean.toString()"""
        return str.__wrap(super(MutableBoolean, self).toString())

    @overload
    def __init__(self, arg0: 'Boolean'):
        """public org.apache.commons.lang3.mutable.MutableBoolean(java.lang.Boolean)"""
        val = __MutableBoolean(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toBoolean(self) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.lang3.mutable.MutableBoolean.toBoolean()"""
        return 'Boolean'.__wrap(super(MutableBoolean, self).toBoolean())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def isFalse(self) -> bool:
        """public boolean org.apache.commons.lang3.mutable.MutableBoolean.isFalse()"""
        return bool.__wrap(super(MutableBoolean, self).isFalse())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setValue(self, arg0: 'Boolean'):
        """public void org.apache.commons.lang3.mutable.MutableBoolean.setValue(java.lang.Boolean)"""
        super(__MutableBoolean, self).setValue(arg0)

    @overload
    def __init__(self, arg0: bool):
        """public org.apache.commons.lang3.mutable.MutableBoolean(boolean)"""
        val = __MutableBoolean(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'MutableBoolean') -> int:
        """public int org.apache.commons.lang3.mutable.MutableBoolean.compareTo(org.apache.commons.lang3.mutable.MutableBoolean)"""
        return int.__wrap(super(__MutableBoolean, self).compareTo(arg0))

    @overload
    def setFalse(self):
        """public void org.apache.commons.lang3.mutable.MutableBoolean.setFalse()"""
        super(MutableBoolean, self).setFalse()

    @overload
    def setValue(self, arg0: bool):
        """public void org.apache.commons.lang3.mutable.MutableBoolean.setValue(boolean)"""
        super(__MutableBoolean, self).setValue(__boolean.valueOf(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.mutable.MutableBoolean()"""
        val = __MutableBoolean()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.lang3.mutable.MutableBoolean.getValue()"""
        return 'Boolean'.__wrap(super(MutableBoolean, self).getValue())