from __future__ import annotations
from overload import overload


 
import org.apache.commons.lang3.stream.Streams as _Streams_ArrayCollector
_ArrayCollector = _Streams_ArrayCollector.ArrayCollector
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.function.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.util.function.BinaryOperator as BinaryOperator
import java.util.function.BinaryOperator as _BinaryOperator
_BinaryOperator = _BinaryOperator
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayCollector():
    """org.apache.commons.lang3.stream.Streams.ArrayCollector"""
 
    @staticmethod
    def _wrap(java_value: _ArrayCollector) -> 'ArrayCollector':
        return ArrayCollector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayCollector):
        """
        Dynamic initializer for ArrayCollector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayCollector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayCollector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def characteristics(self) -> 'Set':
        """public java.util.Set<java.util.stream.Collector$Characteristics> org.apache.commons.lang3.stream.Streams$ArrayCollector.characteristics()"""
        return 'Set'._wrap(super(ArrayCollector, self).characteristics())

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

    @override
    @overload
    def finisher(self) -> 'Function':
        """public java.util.function.Function<java.util.List<E>, E[]> org.apache.commons.lang3.stream.Streams$ArrayCollector.finisher()"""
        return 'Function'._wrap(super(ArrayCollector, self).finisher())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def accumulator(self) -> 'BiConsumer':
        """public java.util.function.BiConsumer<java.util.List<E>, E> org.apache.commons.lang3.stream.Streams$ArrayCollector.accumulator()"""
        return 'BiConsumer'._wrap(super(ArrayCollector, self).accumulator())

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.stream.Streams$ArrayCollector(java.lang.Class<E>)"""
        val = _ArrayCollector(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def combiner(self) -> 'BinaryOperator':
        """public java.util.function.BinaryOperator<java.util.List<E>> org.apache.commons.lang3.stream.Streams$ArrayCollector.combiner()"""
        return 'BinaryOperator'._wrap(super(ArrayCollector, self).combiner())

    @override
    @overload
    def supplier(self) -> 'Supplier':
        """public java.util.function.Supplier<java.util.List<E>> org.apache.commons.lang3.stream.Streams$ArrayCollector.supplier()"""
        return 'Supplier'._wrap(super(ArrayCollector, self).supplier())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.stream.Streams$ArrayCollector
import org.apache.commons.lang3.stream.Streams as _Streams_ArrayCollector
_ArrayCollector = _Streams_ArrayCollector.ArrayCollector
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.function.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.util.function.BinaryOperator as BinaryOperator
import java.util.function.BinaryOperator as _BinaryOperator
_BinaryOperator = _BinaryOperator
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayCollector():
    """org.apache.commons.lang3.stream.Streams.ArrayCollector"""
 
    @staticmethod
    def _wrap(java_value: _ArrayCollector) -> 'ArrayCollector':
        return ArrayCollector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayCollector):
        """
        Dynamic initializer for ArrayCollector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayCollector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayCollector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def characteristics(self) -> 'Set':
        """public java.util.Set<java.util.stream.Collector$Characteristics> org.apache.commons.lang3.stream.Streams$ArrayCollector.characteristics()"""
        return 'Set'._wrap(super(ArrayCollector, self).characteristics())

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

    @override
    @overload
    def finisher(self) -> 'Function':
        """public java.util.function.Function<java.util.List<E>, E[]> org.apache.commons.lang3.stream.Streams$ArrayCollector.finisher()"""
        return 'Function'._wrap(super(ArrayCollector, self).finisher())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def accumulator(self) -> 'BiConsumer':
        """public java.util.function.BiConsumer<java.util.List<E>, E> org.apache.commons.lang3.stream.Streams$ArrayCollector.accumulator()"""
        return 'BiConsumer'._wrap(super(ArrayCollector, self).accumulator())

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.stream.Streams$ArrayCollector(java.lang.Class<E>)"""
        val = _ArrayCollector(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def combiner(self) -> 'BinaryOperator':
        """public java.util.function.BinaryOperator<java.util.List<E>> org.apache.commons.lang3.stream.Streams$ArrayCollector.combiner()"""
        return 'BinaryOperator'._wrap(super(ArrayCollector, self).combiner())

    @override
    @overload
    def supplier(self) -> 'Supplier':
        """public java.util.function.Supplier<java.util.List<E>> org.apache.commons.lang3.stream.Streams$ArrayCollector.supplier()"""
        return 'Supplier'._wrap(super(ArrayCollector, self).supplier())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.stream.Streams$ArrayCollector 
 
 
# CLASS: org.apache.commons.lang3.stream.Streams$FailableStream
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.util.stream.Collector as Collector
import java.lang.String as _String
_String = _String
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.util.function.BinaryOperator as BinaryOperator
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.lang3.stream.Streams as _Streams_FailableStream
_FailableStream = _Streams_FailableStream.FailableStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FailableStream():
    """org.apache.commons.lang3.stream.Streams.FailableStream"""
 
    @staticmethod
    def _wrap(java_value: _FailableStream) -> 'FailableStream':
        return FailableStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableStream):
        """
        Dynamic initializer for FailableStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.apache.commons.lang3.stream.Streams$FailableStream.stream()"""
        return 'Stream'._wrap(super(FailableStream, self).stream())

    @overload
    def map(self, arg0: 'FailableFunction') -> 'FailableStream':
        """public <R> org.apache.commons.lang3.stream.Streams$FailableStream<R> org.apache.commons.lang3.stream.Streams$FailableStream.map(org.apache.commons.lang3.function.FailableFunction<T, R, ?>)"""
        return 'FailableStream'._wrap(super(_FailableStream, self).map(arg0))

    @overload
    def filter(self, arg0: 'FailablePredicate') -> 'FailableStream':
        """public org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams$FailableStream.filter(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return 'FailableStream'._wrap(super(_FailableStream, self).filter(arg0))

    @overload
    def __init__(self, arg0: 'Stream'):
        """public org.apache.commons.lang3.stream.Streams$FailableStream(java.util.stream.Stream<T>)"""
        val = _FailableStream(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def anyMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.stream.Streams$FailableStream.anyMatch(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return bool._wrap(super(_FailableStream, self).anyMatch(arg0))

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

    @overload
    def reduce(self, arg0: object, arg1: 'BinaryOperator') -> object:
        """public T org.apache.commons.lang3.stream.Streams$FailableStream.reduce(T,java.util.function.BinaryOperator<T>)"""
        return object._wrap(super(_FailableStream, self).reduce(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def forEach(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.stream.Streams$FailableStream.forEach(org.apache.commons.lang3.function.FailableConsumer<T, ?>)"""
        super(_FailableStream, self).forEach(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def allMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.stream.Streams$FailableStream.allMatch(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return bool._wrap(super(_FailableStream, self).allMatch(arg0))

    @overload
    def collect(self, arg0: 'Collector') -> object:
        """public <A,R> R org.apache.commons.lang3.stream.Streams$FailableStream.collect(java.util.stream.Collector<? super T, A, R>)"""
        return object._wrap(super(_FailableStream, self).collect(arg0))

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
    def collect(self, arg0: 'Supplier', arg1: 'BiConsumer', arg2: 'BiConsumer') -> object:
        """public <A,R> R org.apache.commons.lang3.stream.Streams$FailableStream.collect(java.util.function.Supplier<R>,java.util.function.BiConsumer<R, ? super T>,java.util.function.BiConsumer<R, R>)"""
        return object._wrap(super(_FailableStream, self).collect(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.stream.Streams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.util.stream.Collector as Collector
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.stream.Collector as _Collector
_Collector = _Collector
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.util.Enumeration as Enumeration
import java.util.stream.Stream as _Stream
_Stream = _Stream
import org.apache.commons.lang3.stream.Streams as _Streams
_Streams = _Streams
import java.util.stream.Stream as Stream
import org.apache.commons.lang3.stream.Streams as _Streams_FailableStream
_FailableStream = _Streams_FailableStream.FailableStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Streams():
    """org.apache.commons.lang3.stream.Streams"""
 
    @staticmethod
    def _wrap(java_value: _Streams) -> 'Streams':
        return Streams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Streams):
        """
        Dynamic initializer for Streams.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Streams__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Streams__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(arg0: 'Enumeration') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.util.Enumeration<E>)"""
        return Stream._wrap(_Streams.of(arg0))

    @staticmethod
    @overload
    def failableStream(arg0: 'Collection') -> 'FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams.failableStream(java.util.Collection<T>)"""
        return FailableStream._wrap(_Streams.failableStream(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def of(arg0: 'Collection') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.util.Collection<E>)"""
        return Stream._wrap(_Streams.of(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Collection') -> 'FailableStream':
        """public static <E> org.apache.commons.lang3.stream.Streams$FailableStream<E> org.apache.commons.lang3.stream.Streams.stream(java.util.Collection<E>)"""
        return FailableStream._wrap(_Streams.stream(arg0))

    @staticmethod
    @overload
    def nonNull(*arg0: object) -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.nonNull(E...)"""
        return Stream._wrap(_Streams.nonNull(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Stream') -> 'FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams.stream(java.util.stream.Stream<T>)"""
        return FailableStream._wrap(_Streams.stream(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.stream.Streams()"""
        val = _Streams()
        self.__wrapper = val

    @staticmethod
    @overload
    def of(arg0: 'Iterator') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.util.Iterator<E>)"""
        return Stream._wrap(_Streams.of(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Iterable') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.lang.Iterable<E>)"""
        return Stream._wrap(_Streams.of(arg0))

    @staticmethod
    @overload
    def of(*arg0: object) -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.commons.lang3.stream.Streams.of(T...)"""
        return Stream._wrap(_Streams.of(arg0))

    @staticmethod
    @overload
    def failableStream(arg0: 'Stream') -> 'FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams.failableStream(java.util.stream.Stream<T>)"""
        return FailableStream._wrap(_Streams.failableStream(arg0))

    @staticmethod
    @overload
    def instancesOf(arg0: 'Class', arg1: 'Collection') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.instancesOf(java.lang.Class<? super E>,java.util.Collection<? super E>)"""
        return Stream._wrap(_Streams.instancesOf(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.stream.Streams()"""
        val = _Streams()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def toArray(arg0: 'Class') -> 'Collector':
        """public static <T> java.util.stream.Collector<T, ?, T[]> org.apache.commons.lang3.stream.Streams.toArray(java.lang.Class<T>)"""
        return Collector._wrap(_Streams.toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nonNull(arg0: 'Collection') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.nonNull(java.util.Collection<E>)"""
        return Stream._wrap(_Streams.nonNull(arg0))

    @staticmethod
    @overload
    def nonNull(arg0: 'Stream') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.nonNull(java.util.stream.Stream<E>)"""
        return Stream._wrap(_Streams.nonNull(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.stream.LangCollectors
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.stream.Collector as Collector
import java.lang.String as _String
_String = _String
import java.util.stream.Collector as _Collector
_Collector = _Collector
import java.lang.Integer as _int
import org.apache.commons.lang3.stream.LangCollectors as _LangCollectors
_LangCollectors = _LangCollectors
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LangCollectors():
    """org.apache.commons.lang3.stream.LangCollectors"""
 
    @staticmethod
    def _wrap(java_value: _LangCollectors) -> 'LangCollectors':
        return LangCollectors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LangCollectors):
        """
        Dynamic initializer for LangCollectors.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LangCollectors__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LangCollectors__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def joining(arg0: 'CharSequence') -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining(java.lang.CharSequence)"""
        return Collector._wrap(_LangCollectors.joining(arg0))

    @staticmethod
    @overload
    def joining(arg0: 'CharSequence', arg1: 'CharSequence', arg2: 'CharSequence') -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining(java.lang.CharSequence,java.lang.CharSequence,java.lang.CharSequence)"""
        return Collector._wrap(_LangCollectors.joining(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def joining(arg0: 'CharSequence', arg1: 'CharSequence', arg2: 'CharSequence', arg3: 'Function') -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining(java.lang.CharSequence,java.lang.CharSequence,java.lang.CharSequence,java.util.function.Function<java.lang.Object, java.lang.String>)"""
        return Collector._wrap(_LangCollectors.joining(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def joining() -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining()"""
        return Collector._wrap(_LangCollectors.joining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.stream.IntStreams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import org.apache.commons.lang3.stream.IntStreams as _IntStreams
_IntStreams = _IntStreams
import java.lang.Integer as _int
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntStreams():
    """org.apache.commons.lang3.stream.IntStreams"""
 
    @staticmethod
    def _wrap(java_value: _IntStreams) -> 'IntStreams':
        return IntStreams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntStreams):
        """
        Dynamic initializer for IntStreams.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntStreams__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntStreams__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def range(arg0: int) -> 'IntStream':
        """public static java.util.stream.IntStream org.apache.commons.lang3.stream.IntStreams.range(int)"""
        return IntStream._wrap(_IntStreams.range(_int.valueOf(arg0)))

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

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.stream.IntStreams()"""
        val = _IntStreams()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.stream.IntStreams()"""
        val = _IntStreams()
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def rangeClosed(arg0: int) -> 'IntStream':
        """public static java.util.stream.IntStream org.apache.commons.lang3.stream.IntStreams.rangeClosed(int)"""
        return IntStream._wrap(_IntStreams.rangeClosed(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())