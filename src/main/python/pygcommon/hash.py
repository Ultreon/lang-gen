from __future__ import annotations
from overload import overload


 
from builtins import str
import java.nio.charset.Charset as Charset
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.hash.Funnels as _Funnels
_Funnels = _Funnels
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import com.google.common.hash.Funnel as _Funnel
_Funnel = _Funnel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Funnels():
    """com.google.common.hash.Funnels"""
 
    @staticmethod
    def _wrap(java_value: _Funnels) -> 'Funnels':
        return Funnels(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Funnels):
        """
        Dynamic initializer for Funnels.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Funnels__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Funnels__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def byteArrayFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<byte[]> com.google.common.hash.Funnels.byteArrayFunnel()"""
        return Funnel._wrap(_Funnels.byteArrayFunnel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def asOutputStream(sink: 'PrimitiveSink') -> 'OutputStream':
        """public static java.io.OutputStream com.google.common.hash.Funnels.asOutputStream(com.google.common.hash.PrimitiveSink)"""
        return OutputStream._wrap(_Funnels.asOutputStream(sink))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def sequentialFunnel(elementFunnel: 'Funnel') -> 'Funnel':
        """public static <E> com.google.common.hash.Funnel<java.lang.Iterable<? extends E>> com.google.common.hash.Funnels.sequentialFunnel(com.google.common.hash.Funnel<E>)"""
        return Funnel._wrap(_Funnels.sequentialFunnel(elementFunnel))

    @staticmethod
    @overload
    def longFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.Long> com.google.common.hash.Funnels.longFunnel()"""
        return Funnel._wrap(_Funnels.longFunnel())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stringFunnel(charset: 'Charset') -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.CharSequence> com.google.common.hash.Funnels.stringFunnel(java.nio.charset.Charset)"""
        return Funnel._wrap(_Funnels.stringFunnel(charset))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def integerFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.Integer> com.google.common.hash.Funnels.integerFunnel()"""
        return Funnel._wrap(_Funnels.integerFunnel())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def unencodedCharsFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.CharSequence> com.google.common.hash.Funnels.unencodedCharsFunnel()"""
        return Funnel._wrap(_Funnels.unencodedCharsFunnel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.hash.Funnels
from builtins import str
import java.nio.charset.Charset as Charset
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.hash.Funnels as _Funnels
_Funnels = _Funnels
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import com.google.common.hash.Funnel as _Funnel
_Funnel = _Funnel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Funnels():
    """com.google.common.hash.Funnels"""
 
    @staticmethod
    def _wrap(java_value: _Funnels) -> 'Funnels':
        return Funnels(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Funnels):
        """
        Dynamic initializer for Funnels.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Funnels__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Funnels__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def byteArrayFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<byte[]> com.google.common.hash.Funnels.byteArrayFunnel()"""
        return Funnel._wrap(_Funnels.byteArrayFunnel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def asOutputStream(sink: 'PrimitiveSink') -> 'OutputStream':
        """public static java.io.OutputStream com.google.common.hash.Funnels.asOutputStream(com.google.common.hash.PrimitiveSink)"""
        return OutputStream._wrap(_Funnels.asOutputStream(sink))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def sequentialFunnel(elementFunnel: 'Funnel') -> 'Funnel':
        """public static <E> com.google.common.hash.Funnel<java.lang.Iterable<? extends E>> com.google.common.hash.Funnels.sequentialFunnel(com.google.common.hash.Funnel<E>)"""
        return Funnel._wrap(_Funnels.sequentialFunnel(elementFunnel))

    @staticmethod
    @overload
    def longFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.Long> com.google.common.hash.Funnels.longFunnel()"""
        return Funnel._wrap(_Funnels.longFunnel())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stringFunnel(charset: 'Charset') -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.CharSequence> com.google.common.hash.Funnels.stringFunnel(java.nio.charset.Charset)"""
        return Funnel._wrap(_Funnels.stringFunnel(charset))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def integerFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.Integer> com.google.common.hash.Funnels.integerFunnel()"""
        return Funnel._wrap(_Funnels.integerFunnel())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def unencodedCharsFunnel() -> 'Funnel':
        """public static com.google.common.hash.Funnel<java.lang.CharSequence> com.google.common.hash.Funnels.unencodedCharsFunnel()"""
        return Funnel._wrap(_Funnels.unencodedCharsFunnel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.hash.Funnels 
 
 
# CLASS: com.google.common.hash.BloomFilter
from builtins import str
import java.util.function.Predicate as Predicate
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.util.stream.Collector as Collector
import java.lang.String as _String
_String = _String
import com.google.common.base.Predicate as _Predicate
_Predicate = _Predicate
import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
import com.google.common.hash.BloomFilter as _BloomFilter
_BloomFilter = _BloomFilter
import java.util.stream.Collector as _Collector
_Collector = _Collector
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BloomFilter():
    """com.google.common.hash.BloomFilter"""
 
    @staticmethod
    def _wrap(java_value: _BloomFilter) -> 'BloomFilter':
        return BloomFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BloomFilter):
        """
        Dynamic initializer for BloomFilter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BloomFilter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BloomFilter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).or(arg0))

    @overload
    def mightContain(self, object: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.mightContain(T)"""
        return bool._wrap(super(_BloomFilter, self).mightContain(object))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def apply(self, input: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.apply(T)"""
        return bool._wrap(super(_BloomFilter, self).apply(input))

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,long)"""
        return BloomFilter._wrap(_BloomFilter.create(funnel, _long.valueOf(expectedInsertions)))

    @staticmethod
    @overload
    def toBloomFilter(funnel: 'Funnel', expectedInsertions: int, fpp: float) -> 'Collector':
        """public static <T> java.util.stream.Collector<T, ?, com.google.common.hash.BloomFilter<T>> com.google.common.hash.BloomFilter.toBloomFilter(com.google.common.hash.Funnel<? super T>,long,double)"""
        return Collector._wrap(_BloomFilter.toBloomFilter(funnel, _long.valueOf(expectedInsertions), _double.valueOf(fpp)))

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int, fpp: float) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,long,double)"""
        return BloomFilter._wrap(_BloomFilter.create(funnel, _long.valueOf(expectedInsertions), _double.valueOf(fpp)))

    @overload
    def approximateElementCount(self) -> int:
        """public long com.google.common.hash.BloomFilter.approximateElementCount()"""
        return int._wrap(super(BloomFilter, self).approximateElementCount())

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
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).and(arg0))

    @overload
    def expectedFpp(self) -> float:
        """public double com.google.common.hash.BloomFilter.expectedFpp()"""
        return float._wrap(super(BloomFilter, self).expectedFpp())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.equals(java.lang.Object)"""
        return bool._wrap(super(_BloomFilter, self).equals(object))

    @overload
    def copy(self) -> 'BloomFilter':
        """public com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.copy()"""
        return 'BloomFilter'._wrap(super(BloomFilter, self).copy())

    @overload
    def isCompatible(self, that: 'BloomFilter') -> bool:
        """public boolean com.google.common.hash.BloomFilter.isCompatible(com.google.common.hash.BloomFilter<T>)"""
        return bool._wrap(super(_BloomFilter, self).isCompatible(that))

    @staticmethod
    @overload
    def readFrom(in: 'InputStream', funnel: 'Funnel') -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.readFrom(java.io.InputStream,com.google.common.hash.Funnel<? super T>) throws java.io.IOException"""
        return BloomFilter._wrap(_BloomFilter.readFrom(in, funnel))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.hash.BloomFilter.hashCode()"""
        return int._wrap(super(BloomFilter, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int, fpp: float) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,int,double)"""
        return BloomFilter._wrap(_BloomFilter.create(funnel, _int.valueOf(expectedInsertions), _double.valueOf(fpp)))

    @overload
    def writeTo(self, out: 'OutputStream'):
        """public void com.google.common.hash.BloomFilter.writeTo(java.io.OutputStream) throws java.io.IOException"""
        super(_BloomFilter, self).writeTo(out)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def test(self, input: object) -> bool:
        """public default boolean com.google.common.base.Predicate.test(T)"""
        return bool._wrap(super(_base.Predicate, self).test(input))

    @overload
    def put(self, object: object) -> bool:
        """public boolean com.google.common.hash.BloomFilter.put(T)"""
        return bool._wrap(super(_BloomFilter, self).put(object))

    @staticmethod
    @overload
    def toBloomFilter(funnel: 'Funnel', expectedInsertions: int) -> 'Collector':
        """public static <T> java.util.stream.Collector<T, ?, com.google.common.hash.BloomFilter<T>> com.google.common.hash.BloomFilter.toBloomFilter(com.google.common.hash.Funnel<? super T>,long)"""
        return Collector._wrap(_BloomFilter.toBloomFilter(funnel, _long.valueOf(expectedInsertions)))

    @override
    @overload
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'._wrap(super(Predicate, self).negate())

    @overload
    def putAll(self, that: 'BloomFilter'):
        """public void com.google.common.hash.BloomFilter.putAll(com.google.common.hash.BloomFilter<T>)"""
        super(_BloomFilter, self).putAll(that)

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

    @staticmethod
    @overload
    def create(funnel: 'Funnel', expectedInsertions: int) -> 'BloomFilter':
        """public static <T> com.google.common.hash.BloomFilter<T> com.google.common.hash.BloomFilter.create(com.google.common.hash.Funnel<? super T>,int)"""
        return BloomFilter._wrap(_BloomFilter.create(funnel, _int.valueOf(expectedInsertions))) 
 
 
# CLASS: com.google.common.hash.HashCode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.google.common.hash.HashCode as _HashCode
_HashCode = _HashCode
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashCode():
    """com.google.common.hash.HashCode"""
 
    @staticmethod
    def _wrap(java_value: _HashCode) -> 'HashCode':
        return HashCode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashCode):
        """
        Dynamic initializer for HashCode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashCode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashCode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def padToLong(self, ):
        """public abstract long com.google.common.hash.HashCode.padToLong()"""
        pass

    @overload
    def equals(self, object: object) -> bool:
        """public final boolean com.google.common.hash.HashCode.equals(java.lang.Object)"""
        return bool._wrap(super(_HashCode, self).equals(object))

    @abstractmethod
    def asLong(self, ):
        """public abstract long com.google.common.hash.HashCode.asLong()"""
        pass

    @overload
    def writeBytesTo(self, dest: bytes, offset: int, maxLength: int) -> int:
        """public int com.google.common.hash.HashCode.writeBytesTo(byte[],int,int)"""
        return int._wrap(super(_HashCode, self).writeBytesTo(bytes, _int.valueOf(offset), _int.valueOf(maxLength)))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.hash.HashCode.hashCode()"""
        return int._wrap(super(HashCode, self).hashCode())

    @abstractmethod
    def bits(self, ):
        """public abstract int com.google.common.hash.HashCode.bits()"""
        pass

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
        """public final java.lang.String com.google.common.hash.HashCode.toString()"""
        return str._wrap(super(HashCode, self).toString())

    @staticmethod
    @overload
    def fromBytes(bytes: bytes) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromBytes(byte[])"""
        return HashCode._wrap(_HashCode.fromBytes(bytes))

    @staticmethod
    @overload
    def fromLong(hash: int) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromLong(long)"""
        return HashCode._wrap(_HashCode.fromLong(_long.valueOf(hash)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def fromString(string: str) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromString(java.lang.String)"""
        return HashCode._wrap(_HashCode.fromString(string))

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

    @abstractmethod
    def asBytes(self, ):
        """public abstract byte[] com.google.common.hash.HashCode.asBytes()"""
        pass

    @staticmethod
    @overload
    def fromInt(hash: int) -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.HashCode.fromInt(int)"""
        return HashCode._wrap(_HashCode.fromInt(_int.valueOf(hash)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def asInt(self, ):
        """public abstract int com.google.common.hash.HashCode.asInt()"""
        pass 
 
 
# CLASS: com.google.common.hash.HashFunction
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
import com.google.common.hash.HashFunction as _HashFunction
_HashFunction = _HashFunction
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
 
class HashFunction():
    """com.google.common.hash.HashFunction"""
 
    @staticmethod
    def _wrap(java_value: _HashFunction) -> 'HashFunction':
        return HashFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashFunction):
        """
        Dynamic initializer for HashFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.hash.HashingOutputStream
from builtins import str
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _Object
_Object = _Object
import com.google.common.hash.HashingOutputStream as _HashingOutputStream
_HashingOutputStream = _HashingOutputStream
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.FilterOutputStream as _FilterOutputStream
_FilterOutputStream = _FilterOutputStream
from builtins import bool
import java.lang.Long as _long
import com.google.common.hash.HashCode as _HashCode
_HashCode = _HashCode
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashingOutputStream():
    """com.google.common.hash.HashingOutputStream"""
 
    @staticmethod
    def _wrap(java_value: _HashingOutputStream) -> 'HashingOutputStream':
        return HashingOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashingOutputStream):
        """
        Dynamic initializer for HashingOutputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashingOutputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashingOutputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, hashFunction: 'HashFunction', out: 'OutputStream'):
        """public com.google.common.hash.HashingOutputStream(com.google.common.hash.HashFunction,java.io.OutputStream)"""
        val = _HashingOutputStream(hashFunction, out)
        self.__wrapper = val

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream._wrap(_OutputStream.nullOutputStream())

    @override
    @overload
    def write(self, b: int):
        """public void com.google.common.hash.HashingOutputStream.write(int) throws java.io.IOException"""
        super(_HashingOutputStream, self).write(_int.valueOf(b))

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
    def close(self):
        """public void com.google.common.hash.HashingOutputStream.close() throws java.io.IOException"""
        super(HashingOutputStream, self).close()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def hash(self) -> 'HashCode':
        """public com.google.common.hash.HashCode com.google.common.hash.HashingOutputStream.hash()"""
        return 'HashCode'._wrap(super(HashingOutputStream, self).hash())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(_FilterOutputStream, self).write(bytes)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void java.io.FilterOutputStream.flush() throws java.io.IOException"""
        super(FilterOutputStream, self).flush()

    @override
    @overload
    def write(self, bytes: bytes, off: int, len: int):
        """public void com.google.common.hash.HashingOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(_HashingOutputStream, self).write(bytes, _int.valueOf(off), _int.valueOf(len))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.hash.HashingInputStream
from builtins import str
import com.google.common.hash.HashingInputStream as _HashingInputStream
_HashingInputStream = _HashingInputStream
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.FilterInputStream as _FilterInputStream
_FilterInputStream = _FilterInputStream
import java.lang.String as _String
_String = _String
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
import com.google.common.hash.HashCode as _HashCode
_HashCode = _HashCode
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashingInputStream():
    """com.google.common.hash.HashingInputStream"""
 
    @staticmethod
    def _wrap(java_value: _HashingInputStream) -> 'HashingInputStream':
        return HashingInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashingInputStream):
        """
        Dynamic initializer for HashingInputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashingInputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashingInputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def hash(self) -> 'HashCode':
        """public com.google.common.hash.HashCode com.google.common.hash.HashingInputStream.hash()"""
        return 'HashCode'._wrap(super(HashingInputStream, self).hash())

    @override
    @overload
    def read(self) -> int:
        """public int com.google.common.hash.HashingInputStream.read() throws java.io.IOException"""
        return int._wrap(super(HashingInputStream, self).read())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).transferTo(arg0))

    @overload
    def __init__(self, hashFunction: 'HashFunction', in: 'InputStream'):
        """public com.google.common.hash.HashingInputStream(com.google.common.hash.HashFunction,java.io.InputStream)"""
        val = _HashingInputStream(hashFunction, in)
        self.__wrapper = val

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int._wrap(super(FilterInputStream, self).available())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def read(self, bytes: bytes, off: int, len: int) -> int:
        """public int com.google.common.hash.HashingInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_HashingInputStream, self).read(bytes, _int.valueOf(off), _int.valueOf(len)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int]._wrap(super(InputStream, self).readAllBytes())

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.FilterInputStream.read(byte[]) throws java.io.IOException"""
        return int._wrap(super(_FilterInputStream, self).read(bytes))

    @overload
    def skip(self, arg0: int) -> int:
        """public long java.io.FilterInputStream.skip(long) throws java.io.IOException"""
        return int._wrap(super(_FilterInputStream, self).skip(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean com.google.common.hash.HashingInputStream.markSupported()"""
        return bool._wrap(super(HashingInputStream, self).markSupported())

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(_InputStream, self).skipNBytes(_long.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream._wrap(_InputStream.nullInputStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).readNBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @override
    @overload
    def reset(self):
        """public void com.google.common.hash.HashingInputStream.reset() throws java.io.IOException"""
        super(HashingInputStream, self).reset()

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int]._wrap(super(_InputStream, self).readNBytes(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self, readlimit: int):
        """public void com.google.common.hash.HashingInputStream.mark(int)"""
        super(_HashingInputStream, self).mark(_int.valueOf(readlimit))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.hash.PrimitiveSink
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
import com.google.common.hash.PrimitiveSink as _PrimitiveSink
_PrimitiveSink = _PrimitiveSink
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
 
class PrimitiveSink():
    """com.google.common.hash.PrimitiveSink"""
 
    @staticmethod
    def _wrap(java_value: _PrimitiveSink) -> 'PrimitiveSink':
        return PrimitiveSink(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrimitiveSink):
        """
        Dynamic initializer for PrimitiveSink.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrimitiveSink__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrimitiveSink__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.hash.Funnel
import com.google.common.hash.Funnel as _Funnel
_Funnel = _Funnel
from abc import abstractmethod, ABC
 
class Funnel():
    """com.google.common.hash.Funnel"""
 
    @staticmethod
    def _wrap(java_value: _Funnel) -> 'Funnel':
        return Funnel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Funnel):
        """
        Dynamic initializer for Funnel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Funnel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Funnel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def funnel(self, from: object, into: 'PrimitiveSink'):
        """public abstract void com.google.common.hash.Funnel.funnel(T,com.google.common.hash.PrimitiveSink)"""
        pass 
 
 
# CLASS: com.google.common.hash.Hasher
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
import com.google.common.hash.Hasher as _Hasher
_Hasher = _Hasher
 
class Hasher():
    """com.google.common.hash.Hasher"""
 
    @staticmethod
    def _wrap(java_value: _Hasher) -> 'Hasher':
        return Hasher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Hasher):
        """
        Dynamic initializer for Hasher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Hasher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Hasher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.hash.Hashing
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.security.Key as Key
import com.google.common.hash.Hashing as _Hashing
_Hashing = _Hashing
import java.lang.Integer as _int
import com.google.common.hash.HashFunction as _HashFunction
_HashFunction = _HashFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import com.google.common.hash.HashCode as _HashCode
_HashCode = _HashCode
import java.lang.Class as _Class
_Class = _Class
 
class Hashing():
    """com.google.common.hash.Hashing"""
 
    @staticmethod
    def _wrap(java_value: _Hashing) -> 'Hashing':
        return Hashing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Hashing):
        """
        Dynamic initializer for Hashing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Hashing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Hashing__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def hmacMd5(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacMd5(byte[])"""
        return HashFunction._wrap(_Hashing.hmacMd5(bytes))

    @staticmethod
    @overload
    def murmur3_128() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_128()"""
        return HashFunction._wrap(_Hashing.murmur3_128())

    @staticmethod
    @overload
    def sipHash24() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sipHash24()"""
        return HashFunction._wrap(_Hashing.sipHash24())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sha1() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha1()"""
        return HashFunction._wrap(_Hashing.sha1())

    @staticmethod
    @overload
    def murmur3_128(seed: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_128(int)"""
        return HashFunction._wrap(_Hashing.murmur3_128(_int.valueOf(seed)))

    @staticmethod
    @overload
    def hmacSha256(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha256(byte[])"""
        return HashFunction._wrap(_Hashing.hmacSha256(bytes))

    @staticmethod
    @overload
    def consistentHash(input: int, buckets: int) -> int:
        """public static int com.google.common.hash.Hashing.consistentHash(long,int)"""
        return int._wrap(_Hashing.consistentHash(_long.valueOf(input), _int.valueOf(buckets)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def hmacSha1(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha1(byte[])"""
        return HashFunction._wrap(_Hashing.hmacSha1(bytes))

    @staticmethod
    @overload
    def combineUnordered(hashCodes: 'Iterable') -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.Hashing.combineUnordered(java.lang.Iterable<com.google.common.hash.HashCode>)"""
        return HashCode._wrap(_Hashing.combineUnordered(hashCodes))

    @staticmethod
    @overload
    def crc32() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.crc32()"""
        return HashFunction._wrap(_Hashing.crc32())

    @staticmethod
    @overload
    def goodFastHash(minimumBits: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.goodFastHash(int)"""
        return HashFunction._wrap(_Hashing.goodFastHash(_int.valueOf(minimumBits)))

    @staticmethod
    @overload
    def murmur3_32() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32()"""
        return HashFunction._wrap(_Hashing.murmur3_32())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def farmHashFingerprint64() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.farmHashFingerprint64()"""
        return HashFunction._wrap(_Hashing.farmHashFingerprint64())

    @staticmethod
    @overload
    def murmur3_32_fixed(seed: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32_fixed(int)"""
        return HashFunction._wrap(_Hashing.murmur3_32_fixed(_int.valueOf(seed)))

    @staticmethod
    @overload
    def fingerprint2011() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.fingerprint2011()"""
        return HashFunction._wrap(_Hashing.fingerprint2011())

    @staticmethod
    @overload
    def consistentHash(hashCode: 'HashCode', buckets: int) -> int:
        """public static int com.google.common.hash.Hashing.consistentHash(com.google.common.hash.HashCode,int)"""
        return int._wrap(_Hashing.consistentHash(hashCode, _int.valueOf(buckets)))

    @staticmethod
    @overload
    def hmacMd5(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacMd5(java.security.Key)"""
        return HashFunction._wrap(_Hashing.hmacMd5(key))

    @staticmethod
    @overload
    def hmacSha512(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha512(java.security.Key)"""
        return HashFunction._wrap(_Hashing.hmacSha512(key))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def sha384() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha384()"""
        return HashFunction._wrap(_Hashing.sha384())

    @staticmethod
    @overload
    def crc32c() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.crc32c()"""
        return HashFunction._wrap(_Hashing.crc32c())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def hmacSha512(key: bytes) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha512(byte[])"""
        return HashFunction._wrap(_Hashing.hmacSha512(bytes))

    @staticmethod
    @overload
    def murmur3_32_fixed() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32_fixed()"""
        return HashFunction._wrap(_Hashing.murmur3_32_fixed())

    @staticmethod
    @overload
    def sha256() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha256()"""
        return HashFunction._wrap(_Hashing.sha256())

    @staticmethod
    @overload
    def murmur3_32(seed: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.murmur3_32(int)"""
        return HashFunction._wrap(_Hashing.murmur3_32(_int.valueOf(seed)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def adler32() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.adler32()"""
        return HashFunction._wrap(_Hashing.adler32())

    @staticmethod
    @overload
    def md5() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.md5()"""
        return HashFunction._wrap(_Hashing.md5())

    @staticmethod
    @overload
    def hmacSha256(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha256(java.security.Key)"""
        return HashFunction._wrap(_Hashing.hmacSha256(key))

    @staticmethod
    @overload
    def sha512() -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sha512()"""
        return HashFunction._wrap(_Hashing.sha512())

    @staticmethod
    @overload
    def hmacSha1(key: 'Key') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.hmacSha1(java.security.Key)"""
        return HashFunction._wrap(_Hashing.hmacSha1(key))

    @staticmethod
    @overload
    def concatenating(first: 'HashFunction', second: 'HashFunction', *rest: 'HashFunction') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.concatenating(com.google.common.hash.HashFunction,com.google.common.hash.HashFunction,com.google.common.hash.HashFunction...)"""
        return HashFunction._wrap(_Hashing.concatenating(first, second, rest))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def concatenating(hashFunctions: 'Iterable') -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.concatenating(java.lang.Iterable<com.google.common.hash.HashFunction>)"""
        return HashFunction._wrap(_Hashing.concatenating(hashFunctions))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def sipHash24(k0: int, k1: int) -> 'HashFunction':
        """public static com.google.common.hash.HashFunction com.google.common.hash.Hashing.sipHash24(long,long)"""
        return HashFunction._wrap(_Hashing.sipHash24(_long.valueOf(k0), _long.valueOf(k1)))

    @staticmethod
    @overload
    def combineOrdered(hashCodes: 'Iterable') -> 'HashCode':
        """public static com.google.common.hash.HashCode com.google.common.hash.Hashing.combineOrdered(java.lang.Iterable<com.google.common.hash.HashCode>)"""
        return HashCode._wrap(_Hashing.combineOrdered(hashCodes))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())