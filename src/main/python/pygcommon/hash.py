from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.hash.HashCode as __HashCode
__HashCode = __HashCode
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashCode(ABC):
    """com.google.common.hash.HashCode"""
 
    @staticmethod
    def __wrap(java_value: __HashCode) -> 'HashCode':
        return HashCode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashCode):
        """
        Dynamic initializer for HashCode.
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

    @staticmethod
    @overload
    def fromLong(hash: int) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromLong(long)"""
        return HashCode.__wrap(__HashCode.fromLong(__long.valueOf(hash)))

    @abstractmethod
    def padToLong(self, ):
        """public abstract long com.google.common.hash.HashCode.padToLong()"""
        pass

    @abstractmethod
    def asLong(self, ):
        """public abstract long com.google.common.hash.HashCode.asLong()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String com.google.common.hash.HashCode.toString()"""
        return str.__wrap(super(HashCode, self).toString())

    @overload
    def equals(self, object: object) -> bool:
        """public final boolean com.google.common.hash.HashCode.equals(java.lang.Object)"""
        return bool.__wrap(super(__HashCode, self).equals(object))

    @abstractmethod
    def bits(self, ):
        """public abstract int com.google.common.hash.HashCode.bits()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def fromBytes(bytes: bytes) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromBytes(byte[])"""
        return HashCode.__wrap(__HashCode.fromBytes(bytes))

    @overload
    def writeBytesTo(self, dest: bytes, offset: int, maxLength: int) -> int:
        """public int com.google.common.hash.HashCode.writeBytesTo(byte[],int,int)"""
        return int.__wrap(super(__HashCode, self).writeBytesTo(bytes, __int.valueOf(offset), __int.valueOf(maxLength)))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.hash.HashCode.hashCode()"""
        return int.__wrap(super(HashCode, self).hashCode())

    @abstractmethod
    def asBytes(self, ):
        """public abstract byte[] com.google.common.hash.HashCode.asBytes()"""
        pass

    @staticmethod
    @overload
    def fromString(string: str) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromString(java.lang.String)"""
        return HashCode.__wrap(__HashCode.fromString(string))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def asInt(self, ):
        """public abstract int com.google.common.hash.HashCode.asInt()"""
        pass

    @staticmethod
    @overload
    def fromInt(hash: int) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromInt(int)"""
        return HashCode.__wrap(__HashCode.fromInt(__int.valueOf(hash)))

 
 
 
# CLASS: com.google.common.hash.HashCode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.hash.HashCode as __HashCode
__HashCode = __HashCode
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashCode(ABC):
    """com.google.common.hash.HashCode"""
 
    @staticmethod
    def __wrap(java_value: __HashCode) -> 'HashCode':
        return HashCode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashCode):
        """
        Dynamic initializer for HashCode.
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

    @staticmethod
    @overload
    def fromLong(hash: int) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromLong(long)"""
        return HashCode.__wrap(__HashCode.fromLong(__long.valueOf(hash)))

    @abstractmethod
    def padToLong(self, ):
        """public abstract long com.google.common.hash.HashCode.padToLong()"""
        pass

    @abstractmethod
    def asLong(self, ):
        """public abstract long com.google.common.hash.HashCode.asLong()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String com.google.common.hash.HashCode.toString()"""
        return str.__wrap(super(HashCode, self).toString())

    @overload
    def equals(self, object: object) -> bool:
        """public final boolean com.google.common.hash.HashCode.equals(java.lang.Object)"""
        return bool.__wrap(super(__HashCode, self).equals(object))

    @abstractmethod
    def bits(self, ):
        """public abstract int com.google.common.hash.HashCode.bits()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def fromBytes(bytes: bytes) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromBytes(byte[])"""
        return HashCode.__wrap(__HashCode.fromBytes(bytes))

    @overload
    def writeBytesTo(self, dest: bytes, offset: int, maxLength: int) -> int:
        """public int com.google.common.hash.HashCode.writeBytesTo(byte[],int,int)"""
        return int.__wrap(super(__HashCode, self).writeBytesTo(bytes, __int.valueOf(offset), __int.valueOf(maxLength)))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.hash.HashCode.hashCode()"""
        return int.__wrap(super(HashCode, self).hashCode())

    @abstractmethod
    def asBytes(self, ):
        """public abstract byte[] com.google.common.hash.HashCode.asBytes()"""
        pass

    @staticmethod
    @overload
    def fromString(string: str) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromString(java.lang.String)"""
        return HashCode.__wrap(__HashCode.fromString(string))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def asInt(self, ):
        """public abstract int com.google.common.hash.HashCode.asInt()"""
        pass

    @staticmethod
    @overload
    def fromInt(hash: int) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromInt(int)"""
        return HashCode.__wrap(__HashCode.fromInt(__int.valueOf(hash)))

 
 
 
# CLASS: com.google.common.hash.HashCode 
 
 
# CLASS: com.google.common.hash.HashFunction
import com.google.common.hash.HashFunction as __HashFunction
__HashFunction = __HashFunction
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
 
class HashFunction(ABC):
    """com.google.common.hash.HashFunction"""
 
    @staticmethod
    def __wrap(java_value: __HashFunction) -> 'HashFunction':
        return HashFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashFunction):
        """
        Dynamic initializer for HashFunction.
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
    def hashBytes(self, input: 'ByteBuffer'):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashBytes(java.nio.ByteBuffer)"""
        pass

    @abstractmethod
    def bits(self, ):
        """public abstract int com.google.common.hash.HashFunction.bits()"""
        pass

    @abstractmethod
    def hashObject(self, instance: object, funnel: 'Funnel'):
        """public abstract <T> com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashObject(T,com.google.common.hash.Funnel<? super T>)"""
        pass

    @abstractmethod
    def newHasher(self, expectedInputSize: int):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.HashFunction.newHasher(int)"""
        pass

    @abstractmethod
    def hashBytes(self, input: bytes, off: int, len: int):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashBytes(byte[],int,int)"""
        pass

    @abstractmethod
    def hashBytes(self, input: bytes):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashBytes(byte[])"""
        pass

    @abstractmethod
    def hashString(self, input: 'CharSequence', charset: 'Charset'):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashString(java.lang.CharSequence,java.nio.charset.Charset)"""
        pass

    @abstractmethod
    def hashLong(self, input: int):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashLong(long)"""
        pass

    @abstractmethod
    def hashInt(self, input: int):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashInt(int)"""
        pass

    @abstractmethod
    def hashUnencodedChars(self, input: 'CharSequence'):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.HashFunction.hashUnencodedChars(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def newHasher(self, ):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.HashFunction.newHasher()"""
        pass 
 
 
# CLASS: com.google.common.hash.PrimitiveSink
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
import com.google.common.hash.PrimitiveSink as __PrimitiveSink
__PrimitiveSink = __PrimitiveSink
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
 
class PrimitiveSink(ABC):
    """com.google.common.hash.PrimitiveSink"""
 
    @staticmethod
    def __wrap(java_value: __PrimitiveSink) -> 'PrimitiveSink':
        return PrimitiveSink(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrimitiveSink):
        """
        Dynamic initializer for PrimitiveSink.
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
    def putDouble(self, d: float):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putDouble(double)"""
        pass

    @abstractmethod
    def putBoolean(self, b: bool):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putBoolean(boolean)"""
        pass

    @abstractmethod
    def putShort(self, s: int):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putShort(short)"""
        pass

    @abstractmethod
    def putBytes(self, bytes: 'ByteBuffer'):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putBytes(java.nio.ByteBuffer)"""
        pass

    @abstractmethod
    def putChar(self, c: str):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putChar(char)"""
        pass

    @abstractmethod
    def putBytes(self, bytes: bytes, off: int, len: int):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putBytes(byte[],int,int)"""
        pass

    @abstractmethod
    def putUnencodedChars(self, charSequence: 'CharSequence'):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putUnencodedChars(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def putBytes(self, bytes: bytes):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putBytes(byte[])"""
        pass

    @abstractmethod
    def putInt(self, i: int):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putInt(int)"""
        pass

    @abstractmethod
    def putString(self, charSequence: 'CharSequence', charset: 'Charset'):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putString(java.lang.CharSequence,java.nio.charset.Charset)"""
        pass

    @abstractmethod
    def putFloat(self, f: float):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putFloat(float)"""
        pass

    @abstractmethod
    def putByte(self, b: int):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putByte(byte)"""
        pass

    @abstractmethod
    def putLong(self, l: int):
        """public abstract com.google.common.hash.PrimitiveSink com.google.common.hash.PrimitiveSink.putLong(long)"""
        pass 
 
 
# CLASS: com.google.common.hash.BloomFilter
import com.google.common.hash.BloomFilter as __BloomFilter
__BloomFilter = __BloomFilter
from builtins import str
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Collector as __Collector
__Collector = __Collector
from builtins import float
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import java.util.stream.Collector as Collector
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
import com.google.common.base.Predicate as __Predicate
__Predicate = __Predicate
from builtins import bool
from builtins import int
 
class BloomFilter(pygcommon.__Predicate, base.Predicate, __Serializable, Serializable):
    """com.google.common.hash.BloomFilter"""
 
    @staticmethod
    def __wrap(java_value: __BloomFilter) -> 'BloomFilter':
        return BloomFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BloomFilter):
        """
        Dynamic initializer for BloomFilter.
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

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int, fpp: float) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,int,double)"""
        return BloomFilter.__wrap(__BloomFilter.create(funnel, __int.valueOf(expectedInsertions), __double.valueOf(fpp)))

    @overload
    def isCompatible(self, that: 'BloomFilter') -> bool:
        """public boolean com.google.common.hash.BloomFilter.isCompatible(com.google.common.hash.BloomFilter<T>)"""
        return bool.__wrap(super(__BloomFilter, self).isCompatible(that))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).or(arg0))

    @staticmethod
    @overload
    def readFrom(in: 'InputStream', funnel: 'Funnel') -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.readFrom(java.io.InputStream,com.google.common.hash.Funnel<? super T>) throws java.io.IOException"""
        return BloomFilter.__wrap(__BloomFilter.readFrom(in, funnel))

    @overload
    def expectedFpp(self) -> float:
        """public double com.google.common.hash.BloomFilter.expectedFpp()"""
        return float.__wrap(super(BloomFilter, self).expectedFpp())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.equals(java.lang.Object)"""
        return bool.__wrap(super(__BloomFilter, self).equals(object))

    @overload
    def putAll(self, that: 'BloomFilter'):
        """public void com.google.common.hash.BloomFilter.putAll(com.google.common.hash.BloomFilter<T>)"""
        super(__BloomFilter, self).putAll(that)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).and(arg0))

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int, fpp: float) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,long,double)"""
        return BloomFilter.__wrap(__BloomFilter.create(funnel, __long.valueOf(expectedInsertions), __double.valueOf(fpp)))

    @overload
    def approximateElementCount(self) -> int:
        """public long com.google.common.hash.BloomFilter.approximateElementCount()"""
        return int.__wrap(super(BloomFilter, self).approximateElementCount())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.hash.BloomFilter.hashCode()"""
        return int.__wrap(super(BloomFilter, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toBloomFilter(funnel: 'Funnel', expectedInsertions: int) -> 'Collector':
        """public static <T> java.util.stream.Collector<T, ?, com.google.common.hash.BloomFilter<T>> com.google.common.hash.BloomFilter.toBloomFilter(com.google.common.hash.Funnel<? super T>,long)"""
        return Collector.__wrap(__BloomFilter.toBloomFilter(funnel, __long.valueOf(expectedInsertions)))

    @overload
    def mightContain(self, object: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.mightContain(T)"""
        return bool.__wrap(super(__BloomFilter, self).mightContain(object))

    @overload
    def copy(self) -> 'BloomFilter':
        """public com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.copy()"""
        return 'BloomFilter'.__wrap(super(BloomFilter, self).copy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def put(self, object: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.put(T)"""
        return bool.__wrap(super(__BloomFilter, self).put(object))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def writeTo(self, out: 'OutputStream'):
        """public void com.google.common.hash.BloomFilter.writeTo(java.io.OutputStream) throws java.io.IOException"""
        super(__BloomFilter, self).writeTo(out)

    @override
    @overload
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'.__wrap(super(Predicate, self).negate())

    @overload
    def test(self, input: object) -> bool:
        """public default boolean com.google.common.base.Predicate.test(T)"""
        return bool.__wrap(super(__base.Predicate, self).test(input))

    @staticmethod
    @overload
    def toBloomFilter(funnel: 'Funnel', expectedInsertions: int, fpp: float) -> 'Collector':
        """public static <T> java.util.stream.Collector<T, ?, com.google.common.hash.BloomFilter<T>> com.google.common.hash.BloomFilter.toBloomFilter(com.google.common.hash.Funnel<? super T>,long,double)"""
        return Collector.__wrap(__BloomFilter.toBloomFilter(funnel, __long.valueOf(expectedInsertions), __double.valueOf(fpp)))

    @overload
    def apply(self, input: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.apply(T)"""
        return bool.__wrap(super(__BloomFilter, self).apply(input))

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,long)"""
        return BloomFilter.__wrap(__BloomFilter.create(funnel, __long.valueOf(expectedInsertions)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,int)"""
        return BloomFilter.__wrap(__BloomFilter.create(funnel, __int.valueOf(expectedInsertions))) 
 
 
# CLASS: com.google.common.hash.HashingOutputStream
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.hash.HashingOutputStream as __HashingOutputStream
__HashingOutputStream = __HashingOutputStream
import com.google.common.hash.HashCode as __HashCode
__HashCode = __HashCode
import java.io.FilterOutputStream as __FilterOutputStream
__FilterOutputStream = __FilterOutputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashingOutputStream(__FilterOutputStream, FilterOutputStream):
    """com.google.common.hash.HashingOutputStream"""
 
    @staticmethod
    def __wrap(java_value: __HashingOutputStream) -> 'HashingOutputStream':
        return HashingOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashingOutputStream):
        """
        Dynamic initializer for HashingOutputStream.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void com.google.common.hash.HashingOutputStream.close() throws java.io.IOException"""
        super(HashingOutputStream, self).close()

    @override
    @overload
    def write(self, b: int):
        """public void com.google.common.hash.HashingOutputStream.write(int) throws java.io.IOException"""
        super(__HashingOutputStream, self).write(__int.valueOf(b))

    @overload
    def hash(self) -> 'HashCode':
        """public com.google.common.hash.HashCode com.google.common.hash.HashingOutputStream.hash()"""
        return 'HashCode'.__wrap(super(HashingOutputStream, self).hash())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, hashFunction: 'HashFunction', out: 'OutputStream'):
        """public com.google.common.hash.HashingOutputStream(com.google.common.hash.HashFunction,java.io.OutputStream)"""
        val = __HashingOutputStream(hashFunction, out)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, bytes: bytes, off: int, len: int):
        """public void com.google.common.hash.HashingOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(__HashingOutputStream, self).write(bytes, __int.valueOf(off), __int.valueOf(len))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(__FilterOutputStream, self).write(bytes)

    @override
    @overload
    def flush(self):
        """public void java.io.FilterOutputStream.flush() throws java.io.IOException"""
        super(FilterOutputStream, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.hash.Hasher
import com.google.common.hash.Hasher as __Hasher
__Hasher = __Hasher
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
 
class Hasher(ABC, __PrimitiveSink, PrimitiveSink):
    """com.google.common.hash.Hasher"""
 
    @staticmethod
    def __wrap(java_value: __Hasher) -> 'Hasher':
        return Hasher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Hasher):
        """
        Dynamic initializer for Hasher.
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
    def putByte(self, b: int):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putByte(byte)"""
        pass

    @abstractmethod
    def putUnencodedChars(self, charSequence: 'CharSequence'):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putUnencodedChars(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.hash.Hasher.hashCode()"""
        pass

    @abstractmethod
    def putLong(self, l: int):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putLong(long)"""
        pass

    @abstractmethod
    def putObject(self, instance: object, funnel: 'Funnel'):
        """public abstract <T> com.google.common.hash.Hasher com.google.common.hash.Hasher.putObject(T,com.google.common.hash.Funnel<? super T>)"""
        pass

    @abstractmethod
    def putString(self, charSequence: 'CharSequence', charset: 'Charset'):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putString(java.lang.CharSequence,java.nio.charset.Charset)"""
        pass

    @abstractmethod
    def putFloat(self, f: float):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putFloat(float)"""
        pass

    @abstractmethod
    def putBytes(self, bytes: bytes):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putBytes(byte[])"""
        pass

    @abstractmethod
    def putBytes(self, bytes: bytes, off: int, len: int):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putBytes(byte[],int,int)"""
        pass

    @abstractmethod
    def putInt(self, i: int):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putInt(int)"""
        pass

    @abstractmethod
    def hash(self, ):
        """public abstract com.google.common.hash.HashCode com.google.common.hash.Hasher.hash()"""
        pass

    @abstractmethod
    def putBytes(self, bytes: 'ByteBuffer'):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putBytes(java.nio.ByteBuffer)"""
        pass

    @abstractmethod
    def putShort(self, s: int):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putShort(short)"""
        pass

    @abstractmethod
    def putDouble(self, d: float):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putDouble(double)"""
        pass

    @abstractmethod
    def putChar(self, c: str):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putChar(char)"""
        pass

    @abstractmethod
    def putBoolean(self, b: bool):
        """public abstract com.google.common.hash.Hasher com.google.common.hash.Hasher.putBoolean(boolean)"""
        pass 
 
 
# CLASS: com.google.common.hash.Funnel
import com.google.common.hash.Funnel as __Funnel
__Funnel = __Funnel
from abc import abstractmethod, ABC
 
class Funnel(ABC, __Serializable, Serializable):
    """com.google.common.hash.Funnel"""
 
    @staticmethod
    def __wrap(java_value: __Funnel) -> 'Funnel':
        return Funnel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Funnel):
        """
        Dynamic initializer for Funnel.
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
    def funnel(self, from: object, into: 'PrimitiveSink'):
        """public abstract void com.google.common.hash.Funnel.funnel(T,com.google.common.hash.PrimitiveSink)"""
        pass 
 
 
# CLASS: com.google.common.hash.Funnels
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.hash.Funnel as __Funnel
__Funnel = __Funnel
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.hash.Funnels as __Funnels
__Funnels = __Funnels
from builtins import int
 
class Funnels():
    """com.google.common.hash.Funnels"""
 
    @staticmethod
    def __wrap(java_value: __Funnels) -> 'Funnels':
        return Funnels(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Funnels):
        """
        Dynamic initializer for Funnels.
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

    @staticmethod
    @overload
    def longFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.Long> com.google.common.hash.Funnels.longFunnel()"""
        return Funnel.__wrap(__Funnels.longFunnel())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def asOutputStream(sink: 'PrimitiveSink') -> 'OutputStream':
        """public static java.io.OutputStream com.google.common.hash.Funnels.asOutputStream(com.google.common.hash.PrimitiveSink)"""
        return OutputStream.__wrap(__Funnels.asOutputStream(sink))

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

    @staticmethod
    @overload
    def unencodedCharsFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.CharSequence> com.google.common.hash.Funnels.unencodedCharsFunnel()"""
        return Funnel.__wrap(__Funnels.unencodedCharsFunnel())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def sequentialFunnel(elementFunnel: 'Funnel') -> 'Funnel':
        """public static <E> com.google.common.hash.Funnel<java.lang.Iterable<? extends E>> com.google.common.hash.Funnels.sequentialFunnel(com.google.common.hash.Funnel<E>)"""
        return Funnel.__wrap(__Funnels.sequentialFunnel(elementFunnel))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stringFunnel(charset: 'Charset') -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.CharSequence> com.google.common.hash.Funnels.stringFunnel(java.nio.charset.Charset)"""
        return Funnel.__wrap(__Funnels.stringFunnel(charset))

    @staticmethod
    @overload
    def byteArrayFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<byte[]> com.google.common.hash.Funnels.byteArrayFunnel()"""
        return Funnel.__wrap(__Funnels.byteArrayFunnel())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def integerFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.Integer> com.google.common.hash.Funnels.integerFunnel()"""
        return Funnel.__wrap(__Funnels.integerFunnel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.hash.HashingInputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.hash.HashCode as __HashCode
__HashCode = __HashCode
import com.google.common.hash.HashingInputStream as __HashingInputStream
__HashingInputStream = __HashingInputStream
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.io.FilterInputStream as __FilterInputStream
__FilterInputStream = __FilterInputStream
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashingInputStream(__FilterInputStream, FilterInputStream):
    """com.google.common.hash.HashingInputStream"""
 
    @staticmethod
    def __wrap(java_value: __HashingInputStream) -> 'HashingInputStream':
        return HashingInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashingInputStream):
        """
        Dynamic initializer for HashingInputStream.
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

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream.__wrap(__InputStream.nullInputStream())

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.FilterInputStream.read(byte[]) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).read(bytes))

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).available())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, hashFunction: 'HashFunction', in: 'InputStream'):
        """public com.google.common.hash.HashingInputStream(com.google.common.hash.HashFunction,java.io.InputStream)"""
        val = __HashingInputStream(hashFunction, in)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int].__wrap(super(InputStream, self).readAllBytes())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def hash(self) -> 'HashCode':
        """public com.google.common.hash.HashCode com.google.common.hash.HashingInputStream.hash()"""
        return 'HashCode'.__wrap(super(HashingInputStream, self).hash())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def skip(self, arg0: int) -> int:
        """public long java.io.FilterInputStream.skip(long) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).skip(__long.valueOf(arg0)))

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).transferTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int].__wrap(super(__InputStream, self).readNBytes(__int.valueOf(arg0)))

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).readNBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def mark(self, readlimit: int):
        """public void com.google.common.hash.HashingInputStream.mark(int)"""
        super(__HashingInputStream, self).mark(__int.valueOf(readlimit))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean com.google.common.hash.HashingInputStream.markSupported()"""
        return bool.__wrap(super(HashingInputStream, self).markSupported())

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def reset(self):
        """public void com.google.common.hash.HashingInputStream.reset() throws java.io.IOException"""
        super(HashingInputStream, self).reset()

    @overload
    def read(self, bytes: bytes, off: int, len: int) -> int:
        """public int com.google.common.hash.HashingInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__HashingInputStream, self).read(bytes, __int.valueOf(off), __int.valueOf(len)))

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(__InputStream, self).skipNBytes(__long.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def read(self) -> int:
        """public int com.google.common.hash.HashingInputStream.read() throws java.io.IOException"""
        return int.__wrap(super(HashingInputStream, self).read()) 
 
 
# CLASS: com.google.common.hash.Hashing
from builtins import str
import com.google.common.hash.Hashing as __Hashing
__Hashing = __Hashing
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import com.google.common.hash.HashCode as __HashCode
__HashCode = __HashCode
import java.security.Key as Key
import com.google.common.hash.HashFunction as __HashFunction
__HashFunction = __HashFunction
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
 
class Hashing():
    """com.google.common.hash.Hashing"""
 
    @staticmethod
    def __wrap(java_value: __Hashing) -> 'Hashing':
        return Hashing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Hashing):
        """
        Dynamic initializer for Hashing.
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

    @staticmethod
    @overload
    def combineUnordered(hashCodes: 'Iterable') -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.Hashing.combineUnordered(java.lang.Iterable<com.google.common.hash.HashCode>)"""
        return HashCode.__wrap(__Hashing.combineUnordered(hashCodes))

    @staticmethod
    @overload
    def sipHash24(k0: int, k1: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sipHash24(long,long)"""
        return HashFunction.__wrap(__Hashing.sipHash24(__long.valueOf(k0), __long.valueOf(k1)))

    @staticmethod
    @overload
    def hmacSha256(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha256(byte[])"""
        return HashFunction.__wrap(__Hashing.hmacSha256(bytes))

    @staticmethod
    @overload
    def combineOrdered(hashCodes: 'Iterable') -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.Hashing.combineOrdered(java.lang.Iterable<com.google.common.hash.HashCode>)"""
        return HashCode.__wrap(__Hashing.combineOrdered(hashCodes))

    @staticmethod
    @overload
    def hmacMd5(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacMd5(java.security.Key)"""
        return HashFunction.__wrap(__Hashing.hmacMd5(key))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def hmacSha512(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha512(byte[])"""
        return HashFunction.__wrap(__Hashing.hmacSha512(bytes))

    @staticmethod
    @overload
    def hmacSha1(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha1(byte[])"""
        return HashFunction.__wrap(__Hashing.hmacSha1(bytes))

    @staticmethod
    @overload
    def crc32c() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.crc32c()"""
        return HashFunction.__wrap(__Hashing.crc32c())

    @staticmethod
    @overload
    def hmacSha512(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha512(java.security.Key)"""
        return HashFunction.__wrap(__Hashing.hmacSha512(key))

    @staticmethod
    @overload
    def md5() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.md5()"""
        return HashFunction.__wrap(__Hashing.md5())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def fingerprint2011() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.fingerprint2011()"""
        return HashFunction.__wrap(__Hashing.fingerprint2011())

    @staticmethod
    @overload
    def goodFastHash(minimumBits: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.goodFastHash(int)"""
        return HashFunction.__wrap(__Hashing.goodFastHash(__int.valueOf(minimumBits)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def murmur3_32(seed: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32(int)"""
        return HashFunction.__wrap(__Hashing.murmur3_32(__int.valueOf(seed)))

    @staticmethod
    @overload
    def sha1() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha1()"""
        return HashFunction.__wrap(__Hashing.sha1())

    @staticmethod
    @overload
    def sha384() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha384()"""
        return HashFunction.__wrap(__Hashing.sha384())

    @staticmethod
    @overload
    def sipHash24() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sipHash24()"""
        return HashFunction.__wrap(__Hashing.sipHash24())

    @staticmethod
    @overload
    def hmacMd5(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacMd5(byte[])"""
        return HashFunction.__wrap(__Hashing.hmacMd5(bytes))

    @staticmethod
    @overload
    def consistentHash(input: int, buckets: int) -> int:
        """public static int com.google.common.hash.Hashing.consistentHash(long,int)"""
        return int.__wrap(__Hashing.consistentHash(__long.valueOf(input), __int.valueOf(buckets)))

    @staticmethod
    @overload
    def concatenating(first: 'HashFunction', second: 'HashFunction', *rest: 'HashFunction') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.concatenating(com.google.common.hash.HashFunction,com.google.common.hash.HashFunction,com.google.common.hash.HashFunction...)"""
        return HashFunction.__wrap(__Hashing.concatenating(first, second, rest))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def adler32() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.adler32()"""
        return HashFunction.__wrap(__Hashing.adler32())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def hmacSha256(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha256(java.security.Key)"""
        return HashFunction.__wrap(__Hashing.hmacSha256(key))

    @staticmethod
    @overload
    def murmur3_32_fixed() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32_fixed()"""
        return HashFunction.__wrap(__Hashing.murmur3_32_fixed())

    @staticmethod
    @overload
    def murmur3_32_fixed(seed: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32_fixed(int)"""
        return HashFunction.__wrap(__Hashing.murmur3_32_fixed(__int.valueOf(seed)))

    @staticmethod
    @overload
    def sha256() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha256()"""
        return HashFunction.__wrap(__Hashing.sha256())

    @staticmethod
    @overload
    def consistentHash(hashCode: 'HashCode', buckets: int) -> int:
        """public static int com.google.common.hash.Hashing.consistentHash(com.google.common.hash.HashCode,int)"""
        return int.__wrap(__Hashing.consistentHash(hashCode, __int.valueOf(buckets)))

    @staticmethod
    @overload
    def murmur3_128() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_128()"""
        return HashFunction.__wrap(__Hashing.murmur3_128())

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

    @staticmethod
    @overload
    def sha512() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha512()"""
        return HashFunction.__wrap(__Hashing.sha512())

    @staticmethod
    @overload
    def hmacSha1(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha1(java.security.Key)"""
        return HashFunction.__wrap(__Hashing.hmacSha1(key))

    @staticmethod
    @overload
    def farmHashFingerprint64() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.farmHashFingerprint64()"""
        return HashFunction.__wrap(__Hashing.farmHashFingerprint64())

    @staticmethod
    @overload
    def murmur3_128(seed: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_128(int)"""
        return HashFunction.__wrap(__Hashing.murmur3_128(__int.valueOf(seed)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def murmur3_32() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32()"""
        return HashFunction.__wrap(__Hashing.murmur3_32())

    @staticmethod
    @overload
    def concatenating(hashFunctions: 'Iterable') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.concatenating(java.lang.Iterable<com.google.common.hash.HashFunction>)"""
        return HashFunction.__wrap(__Hashing.concatenating(hashFunctions))

    @staticmethod
    @overload
    def crc32() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.crc32()"""
        return HashFunction.__wrap(__Hashing.crc32())