from __future__ import annotations
from overload import overload


 
import org.apache.commons.lang3.stream.IntStreams as __IntStreams
__IntStreams = __IntStreams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class IntStreams():
    """org.apache.commons.lang3.stream.IntStreams"""
 
    @staticmethod
    def __wrap(java_value: __IntStreams) -> 'IntStreams':
        return IntStreams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntStreams):
        """
        Dynamic initializer for IntStreams.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def range(arg0: int) -> 'IntStream':
        """public static java.util.stream.IntStream org.apache.commons.lang3.stream.IntStreams.range(int)"""
        return IntStream.__wrap(__IntStreams.range(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.stream.IntStreams()"""
        val = __IntStreams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def rangeClosed(arg0: int) -> 'IntStream':
        """public static java.util.stream.IntStream org.apache.commons.lang3.stream.IntStreams.rangeClosed(int)"""
        return IntStream.__wrap(__IntStreams.rangeClosed(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.stream.IntStreams()"""
        val = __IntStreams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.stream.IntStreams
import org.apache.commons.lang3.stream.IntStreams as __IntStreams
__IntStreams = __IntStreams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class IntStreams():
    """org.apache.commons.lang3.stream.IntStreams"""
 
    @staticmethod
    def __wrap(java_value: __IntStreams) -> 'IntStreams':
        return IntStreams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntStreams):
        """
        Dynamic initializer for IntStreams.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def range(arg0: int) -> 'IntStream':
        """public static java.util.stream.IntStream org.apache.commons.lang3.stream.IntStreams.range(int)"""
        return IntStream.__wrap(__IntStreams.range(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.stream.IntStreams()"""
        val = __IntStreams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def rangeClosed(arg0: int) -> 'IntStream':
        """public static java.util.stream.IntStream org.apache.commons.lang3.stream.IntStreams.rangeClosed(int)"""
        return IntStream.__wrap(__IntStreams.rangeClosed(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.stream.IntStreams()"""
        val = __IntStreams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.stream.IntStreams 
 
 
# CLASS: org.apache.commons.lang3.stream.Streams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Collector as __Collector
__Collector = __Collector
import org.apache.commons.lang3.stream.Streams as __Streams_FailableStream
__FailableStream = __Streams_FailableStream.FailableStream
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.util.stream.Collector as Collector
from builtins import object
import java.util.Iterator as Iterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.stream.Streams as __Streams
__Streams = __Streams
import java.lang.String as __String
__String = __String
import java.util.Enumeration as Enumeration
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Streams():
    """org.apache.commons.lang3.stream.Streams"""
 
    @staticmethod
    def __wrap(java_value: __Streams) -> 'Streams':
        return Streams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Streams):
        """
        Dynamic initializer for Streams.
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
    def of(arg0: 'Enumeration') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.util.Enumeration<E>)"""
        return Stream.__wrap(__Streams.of(arg0))

    @staticmethod
    @overload
    def instancesOf(arg0: 'Class', arg1: 'Collection') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.instancesOf(java.lang.Class<? super E>,java.util.Collection<? super E>)"""
        return Stream.__wrap(__Streams.instancesOf(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def failableStream(arg0: 'Stream') -> 'FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams.failableStream(java.util.stream.Stream<T>)"""
        return FailableStream.__wrap(__Streams.failableStream(arg0))

    @staticmethod
    @overload
    def of(*arg0: object) -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.commons.lang3.stream.Streams.of(T...)"""
        return Stream.__wrap(__Streams.of(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.stream.Streams()"""
        val = __Streams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nonNull(*arg0: object) -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.nonNull(E...)"""
        return Stream.__wrap(__Streams.nonNull(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Iterable') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.lang.Iterable<E>)"""
        return Stream.__wrap(__Streams.of(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Collection') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.util.Collection<E>)"""
        return Stream.__wrap(__Streams.of(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.stream.Streams()"""
        val = __Streams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def of(arg0: 'Iterator') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.of(java.util.Iterator<E>)"""
        return Stream.__wrap(__Streams.of(arg0))

    @staticmethod
    @overload
    def failableStream(arg0: 'Collection') -> 'FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams.failableStream(java.util.Collection<T>)"""
        return FailableStream.__wrap(__Streams.failableStream(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def stream(arg0: 'Stream') -> 'FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams.stream(java.util.stream.Stream<T>)"""
        return FailableStream.__wrap(__Streams.stream(arg0))

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
    def nonNull(arg0: 'Collection') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.nonNull(java.util.Collection<E>)"""
        return Stream.__wrap(__Streams.nonNull(arg0))

    @staticmethod
    @overload
    def toArray(arg0: 'Class') -> 'Collector':
        """public static <T> java.util.stream.Collector<T, ?, T[]> org.apache.commons.lang3.stream.Streams.toArray(java.lang.Class<T>)"""
        return Collector.__wrap(__Streams.toArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nonNull(arg0: 'Stream') -> 'Stream':
        """public static <E> java.util.stream.Stream<E> org.apache.commons.lang3.stream.Streams.nonNull(java.util.stream.Stream<E>)"""
        return Stream.__wrap(__Streams.nonNull(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Collection') -> 'FailableStream':
        """public static <E> org.apache.commons.lang3.stream.Streams$FailableStream<E> org.apache.commons.lang3.stream.Streams.stream(java.util.Collection<E>)"""
        return FailableStream.__wrap(__Streams.stream(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.stream.LangCollectors
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.stream.LangCollectors as __LangCollectors
__LangCollectors = __LangCollectors
from builtins import type
import java.util.stream.Collector as __Collector
__Collector = __Collector
import java.util.stream.Collector as Collector
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LangCollectors():
    """org.apache.commons.lang3.stream.LangCollectors"""
 
    @staticmethod
    def __wrap(java_value: __LangCollectors) -> 'LangCollectors':
        return LangCollectors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LangCollectors):
        """
        Dynamic initializer for LangCollectors.
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
    def joining(arg0: 'CharSequence', arg1: 'CharSequence', arg2: 'CharSequence') -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining(java.lang.CharSequence,java.lang.CharSequence,java.lang.CharSequence)"""
        return Collector.__wrap(__LangCollectors.joining(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def joining(arg0: 'CharSequence') -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining(java.lang.CharSequence)"""
        return Collector.__wrap(__LangCollectors.joining(arg0))

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

    @staticmethod
    @overload
    def joining() -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining()"""
        return Collector.__wrap(__LangCollectors.joining())

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

    @staticmethod
    @overload
    def joining(arg0: 'CharSequence', arg1: 'CharSequence', arg2: 'CharSequence', arg3: 'Function') -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Object, ?, java.lang.String> org.apache.commons.lang3.stream.LangCollectors.joining(java.lang.CharSequence,java.lang.CharSequence,java.lang.CharSequence,java.util.function.Function<java.lang.Object, java.lang.String>)"""
        return Collector.__wrap(__LangCollectors.joining(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.stream.Streams$FailableStream
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.stream.Streams as __Streams_FailableStream
__FailableStream = __Streams_FailableStream.FailableStream
import java.util.stream.Stream as __Stream
__Stream = __Stream
from builtins import object
import java.util.stream.Collector as Collector
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.util.function.BinaryOperator as BinaryOperator
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FailableStream():
    """org.apache.commons.lang3.stream.Streams.FailableStream"""
 
    @staticmethod
    def __wrap(java_value: __FailableStream) -> 'FailableStream':
        return FailableStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableStream):
        """
        Dynamic initializer for FailableStream.
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
    def reduce(self, arg0: object, arg1: 'BinaryOperator') -> object:
        """public T org.apache.commons.lang3.stream.Streams$FailableStream.reduce(T,java.util.function.BinaryOperator<T>)"""
        return object.__wrap(super(__FailableStream, self).reduce(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def allMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.stream.Streams$FailableStream.allMatch(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return bool.__wrap(super(__FailableStream, self).allMatch(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def filter(self, arg0: 'FailablePredicate') -> 'FailableStream':
        """public org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.stream.Streams$FailableStream.filter(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return 'FailableStream'.__wrap(super(__FailableStream, self).filter(arg0))

    @overload
    def anyMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.stream.Streams$FailableStream.anyMatch(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return bool.__wrap(super(__FailableStream, self).anyMatch(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.apache.commons.lang3.stream.Streams$FailableStream.stream()"""
        return 'Stream'.__wrap(super(FailableStream, self).stream())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def forEach(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.stream.Streams$FailableStream.forEach(org.apache.commons.lang3.function.FailableConsumer<T, ?>)"""
        super(__FailableStream, self).forEach(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def collect(self, arg0: 'Collector') -> object:
        """public <A,R> R org.apache.commons.lang3.stream.Streams$FailableStream.collect(java.util.stream.Collector<? super T, A, R>)"""
        return object.__wrap(super(__FailableStream, self).collect(arg0))

    @overload
    def __init__(self, arg0: 'Stream'):
        """public org.apache.commons.lang3.stream.Streams$FailableStream(java.util.stream.Stream<T>)"""
        val = __FailableStream(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def collect(self, arg0: 'Supplier', arg1: 'BiConsumer', arg2: 'BiConsumer') -> object:
        """public <A,R> R org.apache.commons.lang3.stream.Streams$FailableStream.collect(java.util.function.Supplier<R>,java.util.function.BiConsumer<R, ? super T>,java.util.function.BiConsumer<R, R>)"""
        return object.__wrap(super(__FailableStream, self).collect(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def map(self, arg0: 'FailableFunction') -> 'FailableStream':
        """public <R> org.apache.commons.lang3.stream.Streams$FailableStream<R> org.apache.commons.lang3.stream.Streams$FailableStream.map(org.apache.commons.lang3.function.FailableFunction<T, R, ?>)"""
        return 'FailableStream'.__wrap(super(__FailableStream, self).map(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.stream.Streams$ArrayCollector
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.util.function.BinaryOperator as __BinaryOperator
__BinaryOperator = __BinaryOperator
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.function.Function as __Function
__Function = __Function
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.stream.Streams as __Streams_ArrayCollector
__ArrayCollector = __Streams_ArrayCollector.ArrayCollector
import java.util.function.BinaryOperator as BinaryOperator
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
import java.util.function.BiConsumer as __BiConsumer
__BiConsumer = __BiConsumer
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ArrayCollector():
    """org.apache.commons.lang3.stream.Streams.ArrayCollector"""
 
    @staticmethod
    def __wrap(java_value: __ArrayCollector) -> 'ArrayCollector':
        return ArrayCollector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayCollector):
        """
        Dynamic initializer for ArrayCollector.
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

    @override
    @overload
    def accumulator(self) -> 'BiConsumer':
        """public java.util.function.BiConsumer<java.util.List<E>, E> org.apache.commons.lang3.stream.Streams$ArrayCollector.accumulator()"""
        return 'BiConsumer'.__wrap(super(ArrayCollector, self).accumulator())

    @override
    @overload
    def supplier(self) -> 'Supplier':
        """public java.util.function.Supplier<java.util.List<E>> org.apache.commons.lang3.stream.Streams$ArrayCollector.supplier()"""
        return 'Supplier'.__wrap(super(ArrayCollector, self).supplier())

    @override
    @overload
    def finisher(self) -> 'Function':
        """public java.util.function.Function<java.util.List<E>, E[]> org.apache.commons.lang3.stream.Streams$ArrayCollector.finisher()"""
        return 'Function'.__wrap(super(ArrayCollector, self).finisher())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def characteristics(self) -> 'Set':
        """public java.util.Set<java.util.stream.Collector$Characteristics> org.apache.commons.lang3.stream.Streams$ArrayCollector.characteristics()"""
        return 'Set'.__wrap(super(ArrayCollector, self).characteristics())

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
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.stream.Streams$ArrayCollector(java.lang.Class<E>)"""
        val = __ArrayCollector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def combiner(self) -> 'BinaryOperator':
        """public java.util.function.BinaryOperator<java.util.List<E>> org.apache.commons.lang3.stream.Streams$ArrayCollector.combiner()"""
        return 'BinaryOperator'.__wrap(super(ArrayCollector, self).combiner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))