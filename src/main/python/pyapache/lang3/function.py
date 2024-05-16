from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableShortSupplier as __FailableShortSupplier
__FailableShortSupplier = __FailableShortSupplier
 
class FailableShortSupplier(ABC):
    """org.apache.commons.lang3.function.FailableShortSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableShortSupplier) -> 'FailableShortSupplier':
        return FailableShortSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableShortSupplier):
        """
        Dynamic initializer for FailableShortSupplier.
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
    def getAsShort(self, ):
        """public abstract short org.apache.commons.lang3.function.FailableShortSupplier.getAsShort() throws E"""
        pass

 
 
 
# CLASS: org.apache.commons.lang3.function.FailableShortSupplier
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableShortSupplier as __FailableShortSupplier
__FailableShortSupplier = __FailableShortSupplier
 
class FailableShortSupplier(ABC):
    """org.apache.commons.lang3.function.FailableShortSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableShortSupplier) -> 'FailableShortSupplier':
        return FailableShortSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableShortSupplier):
        """
        Dynamic initializer for FailableShortSupplier.
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
    def getAsShort(self, ):
        """public abstract short org.apache.commons.lang3.function.FailableShortSupplier.getAsShort() throws E"""
        pass

 
 
 
# CLASS: org.apache.commons.lang3.function.FailableShortSupplier 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleConsumer
import org.apache.commons.lang3.function.FailableDoubleConsumer as __FailableDoubleConsumer
__FailableDoubleConsumer = __FailableDoubleConsumer
from abc import abstractmethod, ABC
 
class FailableDoubleConsumer(ABC):
    """org.apache.commons.lang3.function.FailableDoubleConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoubleConsumer) -> 'FailableDoubleConsumer':
        return FailableDoubleConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoubleConsumer):
        """
        Dynamic initializer for FailableDoubleConsumer.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableDoubleConsumer':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleConsumer<E> org.apache.commons.lang3.function.FailableDoubleConsumer.nop()"""
        return FailableDoubleConsumer.__wrap(__FailableDoubleConsumer.nop())

    @overload
    def andThen(self, arg0: 'FailableDoubleConsumer') -> 'FailableDoubleConsumer':
        """public default org.apache.commons.lang3.function.FailableDoubleConsumer<E> org.apache.commons.lang3.function.FailableDoubleConsumer.andThen(org.apache.commons.lang3.function.FailableDoubleConsumer<E>)"""
        return 'FailableDoubleConsumer'.__wrap(super(__FailableDoubleConsumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: float):
        """public abstract void org.apache.commons.lang3.function.FailableDoubleConsumer.accept(double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableSupplier
import org.apache.commons.lang3.function.FailableSupplier as __FailableSupplier
__FailableSupplier = __FailableSupplier
from abc import abstractmethod, ABC
 
class FailableSupplier(ABC):
    """org.apache.commons.lang3.function.FailableSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableSupplier) -> 'FailableSupplier':
        return FailableSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableSupplier):
        """
        Dynamic initializer for FailableSupplier.
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
    def get(self, ):
        """public abstract R org.apache.commons.lang3.function.FailableSupplier.get() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.IntToCharFunction
import org.apache.commons.lang3.function.IntToCharFunction as __IntToCharFunction
__IntToCharFunction = __IntToCharFunction
from abc import abstractmethod, ABC
 
class IntToCharFunction(ABC):
    """org.apache.commons.lang3.function.IntToCharFunction"""
 
    @staticmethod
    def __wrap(java_value: __IntToCharFunction) -> 'IntToCharFunction':
        return IntToCharFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntToCharFunction):
        """
        Dynamic initializer for IntToCharFunction.
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
    def applyAsChar(self, arg0: int):
        """public abstract char org.apache.commons.lang3.function.IntToCharFunction.applyAsChar(int)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.Failable
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
from builtins import type
import org.apache.commons.lang3.stream.Streams as __Streams_FailableStream
__FailableStream = __Streams_FailableStream.FailableStream
import java.util.Collection as Collection
import java.lang.Runnable as __Runnable
__Runnable = __Runnable
import java.util.function.Consumer as Consumer
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
import java.lang.RuntimeException as RuntimeException
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
import java.util.concurrent.Callable as Callable
import java.lang.Double as __double
from builtins import bool
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Runnable as Runnable
from builtins import float
import java.util.function.BiPredicate as __BiPredicate
__BiPredicate = __BiPredicate
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
try:
    from pyapache.lang3 import stream
except ImportError:
    stream = __import_once__("pyapache.lang3.stream")

import java.util.function.BiFunction as BiFunction
import java.lang.RuntimeException as __RuntimeException
__RuntimeException = __RuntimeException
import java.lang.Long as __long
import java.util.concurrent.Callable as __Callable
__Callable = __Callable
import java.util.function.BiConsumer as BiConsumer
import java.util.function.BiPredicate as BiPredicate
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.BiConsumer as __BiConsumer
__BiConsumer = __BiConsumer
import org.apache.commons.lang3.function.Failable as __Failable
__Failable = __Failable
from builtins import int
 
class Failable():
    """org.apache.commons.lang3.function.Failable"""
 
    @staticmethod
    def __wrap(java_value: __Failable) -> 'Failable':
        return Failable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Failable):
        """
        Dynamic initializer for Failable.
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
    def asBiFunction(arg0: 'FailableBiFunction') -> 'BiFunction':
        """public static <T,U,R> java.util.function.BiFunction<T, U, R> org.apache.commons.lang3.function.Failable.asBiFunction(org.apache.commons.lang3.function.FailableBiFunction<T, U, R, ?>)"""
        return BiFunction.__wrap(__Failable.asBiFunction(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Stream') -> 'stream.Streams$FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.function.Failable.stream(java.util.stream.Stream<T>)"""
        return stream.Streams$FailableStream.__wrap(__Failable.stream(arg0))

    @staticmethod
    @overload
    def asPredicate(arg0: 'FailablePredicate') -> 'Predicate':
        """public static <T> java.util.function.Predicate<T> org.apache.commons.lang3.function.Failable.asPredicate(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return Predicate.__wrap(__Failable.asPredicate(arg0))

    @staticmethod
    @overload
    def getAsLong(arg0: 'FailableLongSupplier') -> int:
        """public static <E extends java.lang.Throwable> long org.apache.commons.lang3.function.Failable.getAsLong(org.apache.commons.lang3.function.FailableLongSupplier<E>)"""
        return int.__wrap(__Failable.getAsLong(arg0))

    @staticmethod
    @overload
    def test(arg0: 'FailablePredicate', arg1: object) -> bool:
        """public static <T,E extends java.lang.Throwable> boolean org.apache.commons.lang3.function.Failable.test(org.apache.commons.lang3.function.FailablePredicate<T, E>,T)"""
        return bool.__wrap(__Failable.test(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def get(arg0: 'FailableSupplier') -> object:
        """public static <T,E extends java.lang.Throwable> T org.apache.commons.lang3.function.Failable.get(org.apache.commons.lang3.function.FailableSupplier<T, E>)"""
        return object.__wrap(__Failable.get(arg0))

    @staticmethod
    @overload
    def asCallable(arg0: 'FailableCallable') -> 'Callable':
        """public static <V> java.util.concurrent.Callable<V> org.apache.commons.lang3.function.Failable.asCallable(org.apache.commons.lang3.function.FailableCallable<V, ?>)"""
        return Callable.__wrap(__Failable.asCallable(arg0))

    @staticmethod
    @overload
    def apply(arg0: 'FailableBiFunction', arg1: object, arg2: object) -> object:
        """public static <T,U,R,E extends java.lang.Throwable> R org.apache.commons.lang3.function.Failable.apply(org.apache.commons.lang3.function.FailableBiFunction<T, U, R, E>,T,U)"""
        return object.__wrap(__Failable.apply(arg0, arg1, arg2))

    @staticmethod
    @overload
    def test(arg0: 'FailableBiPredicate', arg1: object, arg2: object) -> bool:
        """public static <T,U,E extends java.lang.Throwable> boolean org.apache.commons.lang3.function.Failable.test(org.apache.commons.lang3.function.FailableBiPredicate<T, U, E>,T,U)"""
        return bool.__wrap(__Failable.test(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stream(arg0: 'Collection') -> 'stream.Streams$FailableStream':
        """public static <E> org.apache.commons.lang3.stream.Streams$FailableStream<E> org.apache.commons.lang3.function.Failable.stream(java.util.Collection<E>)"""
        return stream.Streams$FailableStream.__wrap(__Failable.stream(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableIntConsumer', arg1: int):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableIntConsumer<E>,int)"""
        __Failable.accept(arg0, __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def call(arg0: 'FailableCallable') -> object:
        """public static <V,E extends java.lang.Throwable> V org.apache.commons.lang3.function.Failable.call(org.apache.commons.lang3.function.FailableCallable<V, E>)"""
        return object.__wrap(__Failable.call(arg0))

    @staticmethod
    @overload
    def rethrow(arg0: 'Throwable') -> 'RuntimeException':
        """public static java.lang.RuntimeException org.apache.commons.lang3.function.Failable.rethrow(java.lang.Throwable)"""
        return RuntimeException.__wrap(__Failable.rethrow(arg0))

    @staticmethod
    @overload
    def asFunction(arg0: 'FailableFunction') -> 'Function':
        """public static <T,R> java.util.function.Function<T, R> org.apache.commons.lang3.function.Failable.asFunction(org.apache.commons.lang3.function.FailableFunction<T, R, ?>)"""
        return Function.__wrap(__Failable.asFunction(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getAsBoolean(arg0: 'FailableBooleanSupplier') -> bool:
        """public static <E extends java.lang.Throwable> boolean org.apache.commons.lang3.function.Failable.getAsBoolean(org.apache.commons.lang3.function.FailableBooleanSupplier<E>)"""
        return bool.__wrap(__Failable.getAsBoolean(arg0))

    @staticmethod
    @overload
    def applyAsDouble(arg0: 'FailableDoubleBinaryOperator', arg1: float, arg2: float) -> float:
        """public static <E extends java.lang.Throwable> double org.apache.commons.lang3.function.Failable.applyAsDouble(org.apache.commons.lang3.function.FailableDoubleBinaryOperator<E>,double,double)"""
        return float.__wrap(__Failable.applyAsDouble(arg0, __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def getAsDouble(arg0: 'FailableDoubleSupplier') -> float:
        """public static <E extends java.lang.Throwable> double org.apache.commons.lang3.function.Failable.getAsDouble(org.apache.commons.lang3.function.FailableDoubleSupplier<E>)"""
        return float.__wrap(__Failable.getAsDouble(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def accept(arg0: 'FailableLongConsumer', arg1: int):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableLongConsumer<E>,long)"""
        __Failable.accept(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def getAsInt(arg0: 'FailableIntSupplier') -> int:
        """public static <E extends java.lang.Throwable> int org.apache.commons.lang3.function.Failable.getAsInt(org.apache.commons.lang3.function.FailableIntSupplier<E>)"""
        return int.__wrap(__Failable.getAsInt(arg0))

    @staticmethod
    @overload
    def asBiConsumer(arg0: 'FailableBiConsumer') -> 'BiConsumer':
        """public static <T,U> java.util.function.BiConsumer<T, U> org.apache.commons.lang3.function.Failable.asBiConsumer(org.apache.commons.lang3.function.FailableBiConsumer<T, U, ?>)"""
        return BiConsumer.__wrap(__Failable.asBiConsumer(arg0))

    @staticmethod
    @overload
    def run(arg0: 'FailableRunnable'):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.run(org.apache.commons.lang3.function.FailableRunnable<E>)"""
        __Failable.run(arg0)

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', arg1: 'FailableConsumer', *arg2: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.function.Failable.tryWithResources(org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.function.FailableConsumer<java.lang.Throwable, ? extends java.lang.Throwable>,org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>...)"""
        __Failable.tryWithResources(arg0, arg1, arg2)

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
    def apply(arg0: 'FailableFunction', arg1: object) -> object:
        """public static <T,R,E extends java.lang.Throwable> R org.apache.commons.lang3.function.Failable.apply(org.apache.commons.lang3.function.FailableFunction<T, R, E>,T)"""
        return object.__wrap(__Failable.apply(arg0, arg1))

    @staticmethod
    @overload
    def asConsumer(arg0: 'FailableConsumer') -> 'Consumer':
        """public static <T> java.util.function.Consumer<T> org.apache.commons.lang3.function.Failable.asConsumer(org.apache.commons.lang3.function.FailableConsumer<T, ?>)"""
        return Consumer.__wrap(__Failable.asConsumer(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableConsumer', arg1: object):
        """public static <T,E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableConsumer<T, E>,T)"""
        __Failable.accept(arg0, arg1)

    @staticmethod
    @overload
    def asSupplier(arg0: 'FailableSupplier') -> 'Supplier':
        """public static <T> java.util.function.Supplier<T> org.apache.commons.lang3.function.Failable.asSupplier(org.apache.commons.lang3.function.FailableSupplier<T, ?>)"""
        return Supplier.__wrap(__Failable.asSupplier(arg0))

    @staticmethod
    @overload
    def getAsShort(arg0: 'FailableShortSupplier') -> int:
        """public static <E extends java.lang.Throwable> short org.apache.commons.lang3.function.Failable.getAsShort(org.apache.commons.lang3.function.FailableShortSupplier<E>)"""
        return int.__wrap(__Failable.getAsShort(arg0))

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', *arg1: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.function.Failable.tryWithResources(org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>...)"""
        __Failable.tryWithResources(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def accept(arg0: 'FailableDoubleConsumer', arg1: float):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableDoubleConsumer<E>,double)"""
        __Failable.accept(arg0, __double.valueOf(arg1))

    @staticmethod
    @overload
    def asBiPredicate(arg0: 'FailableBiPredicate') -> 'BiPredicate':
        """public static <T,U> java.util.function.BiPredicate<T, U> org.apache.commons.lang3.function.Failable.asBiPredicate(org.apache.commons.lang3.function.FailableBiPredicate<T, U, ?>)"""
        return BiPredicate.__wrap(__Failable.asBiPredicate(arg0))

    @staticmethod
    @overload
    def asRunnable(arg0: 'FailableRunnable') -> 'Runnable':
        """public static java.lang.Runnable org.apache.commons.lang3.function.Failable.asRunnable(org.apache.commons.lang3.function.FailableRunnable<?>)"""
        return Runnable.__wrap(__Failable.asRunnable(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableBiConsumer', arg1: object, arg2: object):
        """public static <T,U,E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableBiConsumer<T, U, E>,T,U)"""
        __Failable.accept(arg0, arg1, arg2) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongFunction
import org.apache.commons.lang3.function.FailableLongFunction as __FailableLongFunction
__FailableLongFunction = __FailableLongFunction
from abc import abstractmethod, ABC
 
class FailableLongFunction(ABC):
    """org.apache.commons.lang3.function.FailableLongFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongFunction) -> 'FailableLongFunction':
        return FailableLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongFunction):
        """
        Dynamic initializer for FailableLongFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableLongFunction':
        """public static <R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongFunction<R, E> org.apache.commons.lang3.function.FailableLongFunction.nop()"""
        return FailableLongFunction.__wrap(__FailableLongFunction.nop())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract R org.apache.commons.lang3.function.FailableLongFunction.apply(long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongBinaryOperator
import org.apache.commons.lang3.function.FailableLongBinaryOperator as __FailableLongBinaryOperator
__FailableLongBinaryOperator = __FailableLongBinaryOperator
from abc import abstractmethod, ABC
 
class FailableLongBinaryOperator(ABC):
    """org.apache.commons.lang3.function.FailableLongBinaryOperator"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongBinaryOperator) -> 'FailableLongBinaryOperator':
        return FailableLongBinaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongBinaryOperator):
        """
        Dynamic initializer for FailableLongBinaryOperator.
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
    def applyAsLong(self, arg0: int, arg1: int):
        """public abstract long org.apache.commons.lang3.function.FailableLongBinaryOperator.applyAsLong(long,long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.TriConsumer
import org.apache.commons.lang3.function.TriConsumer as __TriConsumer
__TriConsumer = __TriConsumer
from abc import abstractmethod, ABC
 
class TriConsumer(ABC):
    """org.apache.commons.lang3.function.TriConsumer"""
 
    @staticmethod
    def __wrap(java_value: __TriConsumer) -> 'TriConsumer':
        return TriConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriConsumer):
        """
        Dynamic initializer for TriConsumer.
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
 
    @overload
    def andThen(self, arg0: 'TriConsumer') -> 'TriConsumer':
        """public default org.apache.commons.lang3.function.TriConsumer<T, U, V> org.apache.commons.lang3.function.TriConsumer.andThen(org.apache.commons.lang3.function.TriConsumer<? super T, ? super U, ? super V>)"""
        return 'TriConsumer'.__wrap(super(__TriConsumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: object, arg1: object, arg2: object):
        """public abstract void org.apache.commons.lang3.function.TriConsumer.accept(T,U,V)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBooleanSupplier
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableBooleanSupplier as __FailableBooleanSupplier
__FailableBooleanSupplier = __FailableBooleanSupplier
 
class FailableBooleanSupplier(ABC):
    """org.apache.commons.lang3.function.FailableBooleanSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableBooleanSupplier) -> 'FailableBooleanSupplier':
        return FailableBooleanSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableBooleanSupplier):
        """
        Dynamic initializer for FailableBooleanSupplier.
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
    def getAsBoolean(self, ):
        """public abstract boolean org.apache.commons.lang3.function.FailableBooleanSupplier.getAsBoolean() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToIntFunction
import org.apache.commons.lang3.function.FailableToIntFunction as __FailableToIntFunction
__FailableToIntFunction = __FailableToIntFunction
from abc import abstractmethod, ABC
 
class FailableToIntFunction(ABC):
    """org.apache.commons.lang3.function.FailableToIntFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableToIntFunction) -> 'FailableToIntFunction':
        return FailableToIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableToIntFunction):
        """
        Dynamic initializer for FailableToIntFunction.
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
    def applyAsInt(self, arg0: object):
        """public abstract int org.apache.commons.lang3.function.FailableToIntFunction.applyAsInt(T) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableToIntFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToIntFunction<T, E> org.apache.commons.lang3.function.FailableToIntFunction.nop()"""
        return FailableToIntFunction.__wrap(__FailableToIntFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleFunction
import org.apache.commons.lang3.function.FailableDoubleFunction as __FailableDoubleFunction
__FailableDoubleFunction = __FailableDoubleFunction
from abc import abstractmethod, ABC
 
class FailableDoubleFunction(ABC):
    """org.apache.commons.lang3.function.FailableDoubleFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoubleFunction) -> 'FailableDoubleFunction':
        return FailableDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoubleFunction):
        """
        Dynamic initializer for FailableDoubleFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableDoubleFunction':
        """public static <R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleFunction<R, E> org.apache.commons.lang3.function.FailableDoubleFunction.nop()"""
        return FailableDoubleFunction.__wrap(__FailableDoubleFunction.nop())

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract R org.apache.commons.lang3.function.FailableDoubleFunction.apply(double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.Suppliers
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.function.Suppliers as __Suppliers
__Suppliers = __Suppliers
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Suppliers():
    """org.apache.commons.lang3.function.Suppliers"""
 
    @staticmethod
    def __wrap(java_value: __Suppliers) -> 'Suppliers':
        return Suppliers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Suppliers):
        """
        Dynamic initializer for Suppliers.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.function.Suppliers()"""
        val = __Suppliers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def get(arg0: 'Supplier') -> object:
        """public static <T> T org.apache.commons.lang3.function.Suppliers.get(java.util.function.Supplier<T>)"""
        return object.__wrap(__Suppliers.get(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.function.Suppliers()"""
        val = __Suppliers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBiConsumer
import org.apache.commons.lang3.function.FailableBiConsumer as __FailableBiConsumer
__FailableBiConsumer = __FailableBiConsumer
from abc import abstractmethod, ABC
 
class FailableBiConsumer(ABC):
    """org.apache.commons.lang3.function.FailableBiConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableBiConsumer) -> 'FailableBiConsumer':
        return FailableBiConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableBiConsumer):
        """
        Dynamic initializer for FailableBiConsumer.
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
    def accept(self, arg0: object, arg1: object):
        """public abstract void org.apache.commons.lang3.function.FailableBiConsumer.accept(T,U) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableBiConsumer') -> 'FailableBiConsumer':
        """public default org.apache.commons.lang3.function.FailableBiConsumer<T, U, E> org.apache.commons.lang3.function.FailableBiConsumer.andThen(org.apache.commons.lang3.function.FailableBiConsumer<? super T, ? super U, E>)"""
        return 'FailableBiConsumer'.__wrap(super(__FailableBiConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableBiConsumer':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiConsumer<T, U, E> org.apache.commons.lang3.function.FailableBiConsumer.nop()"""
        return FailableBiConsumer.__wrap(__FailableBiConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntToDoubleFunction
import org.apache.commons.lang3.function.FailableIntToDoubleFunction as __FailableIntToDoubleFunction
__FailableIntToDoubleFunction = __FailableIntToDoubleFunction
from abc import abstractmethod, ABC
 
class FailableIntToDoubleFunction(ABC):
    """org.apache.commons.lang3.function.FailableIntToDoubleFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntToDoubleFunction) -> 'FailableIntToDoubleFunction':
        return FailableIntToDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntToDoubleFunction):
        """
        Dynamic initializer for FailableIntToDoubleFunction.
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
    def applyAsDouble(self, arg0: int):
        """public abstract double org.apache.commons.lang3.function.FailableIntToDoubleFunction.applyAsDouble(int) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableIntToDoubleFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntToDoubleFunction<E> org.apache.commons.lang3.function.FailableIntToDoubleFunction.nop()"""
        return FailableIntToDoubleFunction.__wrap(__FailableIntToDoubleFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoublePredicate
import org.apache.commons.lang3.function.FailableDoublePredicate as __FailableDoublePredicate
__FailableDoublePredicate = __FailableDoublePredicate
from abc import abstractmethod, ABC
 
class FailableDoublePredicate(ABC):
    """org.apache.commons.lang3.function.FailableDoublePredicate"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoublePredicate) -> 'FailableDoublePredicate':
        return FailableDoublePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoublePredicate):
        """
        Dynamic initializer for FailableDoublePredicate.
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
 
    @overload
    def and(self, arg0: 'FailableDoublePredicate') -> 'FailableDoublePredicate':
        """public default org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.and(org.apache.commons.lang3.function.FailableDoublePredicate<E>)"""
        return 'FailableDoublePredicate'.__wrap(super(__FailableDoublePredicate, self).and(arg0))

    @overload
    def negate(self) -> 'FailableDoublePredicate':
        """public default org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.negate()"""
        return 'FailableDoublePredicate'.__wrap(super(FailableDoublePredicate, self).negate())

    @staticmethod
    @overload
    def falsePredicate() -> 'FailableDoublePredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.falsePredicate()"""
        return FailableDoublePredicate.__wrap(__FailableDoublePredicate.falsePredicate())

    @staticmethod
    @overload
    def truePredicate() -> 'FailableDoublePredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.truePredicate()"""
        return FailableDoublePredicate.__wrap(__FailableDoublePredicate.truePredicate())

    @overload
    def or(self, arg0: 'FailableDoublePredicate') -> 'FailableDoublePredicate':
        """public default org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.or(org.apache.commons.lang3.function.FailableDoublePredicate<E>)"""
        return 'FailableDoublePredicate'.__wrap(super(__FailableDoublePredicate, self).or(arg0))

    @abstractmethod
    def test(self, arg0: float):
        """public abstract boolean org.apache.commons.lang3.function.FailableDoublePredicate.test(double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongConsumer
import org.apache.commons.lang3.function.FailableLongConsumer as __FailableLongConsumer
__FailableLongConsumer = __FailableLongConsumer
from abc import abstractmethod, ABC
 
class FailableLongConsumer(ABC):
    """org.apache.commons.lang3.function.FailableLongConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongConsumer) -> 'FailableLongConsumer':
        return FailableLongConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongConsumer):
        """
        Dynamic initializer for FailableLongConsumer.
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
    def accept(self, arg0: int):
        """public abstract void org.apache.commons.lang3.function.FailableLongConsumer.accept(long) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableLongConsumer') -> 'FailableLongConsumer':
        """public default org.apache.commons.lang3.function.FailableLongConsumer<E> org.apache.commons.lang3.function.FailableLongConsumer.andThen(org.apache.commons.lang3.function.FailableLongConsumer<E>)"""
        return 'FailableLongConsumer'.__wrap(super(__FailableLongConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableLongConsumer':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongConsumer<E> org.apache.commons.lang3.function.FailableLongConsumer.nop()"""
        return FailableLongConsumer.__wrap(__FailableLongConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToDoubleBiFunction
import org.apache.commons.lang3.function.FailableToDoubleBiFunction as __FailableToDoubleBiFunction
__FailableToDoubleBiFunction = __FailableToDoubleBiFunction
from abc import abstractmethod, ABC
 
class FailableToDoubleBiFunction(ABC):
    """org.apache.commons.lang3.function.FailableToDoubleBiFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableToDoubleBiFunction) -> 'FailableToDoubleBiFunction':
        return FailableToDoubleBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableToDoubleBiFunction):
        """
        Dynamic initializer for FailableToDoubleBiFunction.
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
    def applyAsDouble(self, arg0: object, arg1: object):
        """public abstract double org.apache.commons.lang3.function.FailableToDoubleBiFunction.applyAsDouble(T,U) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableToDoubleBiFunction':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToDoubleBiFunction<T, U, E> org.apache.commons.lang3.function.FailableToDoubleBiFunction.nop()"""
        return FailableToDoubleBiFunction.__wrap(__FailableToDoubleBiFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBiFunction
import org.apache.commons.lang3.function.FailableBiFunction as __FailableBiFunction
__FailableBiFunction = __FailableBiFunction
from abc import abstractmethod, ABC
 
class FailableBiFunction(ABC):
    """org.apache.commons.lang3.function.FailableBiFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableBiFunction) -> 'FailableBiFunction':
        return FailableBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableBiFunction):
        """
        Dynamic initializer for FailableBiFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableBiFunction':
        """public static <T,U,R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiFunction<T, U, R, E> org.apache.commons.lang3.function.FailableBiFunction.nop()"""
        return FailableBiFunction.__wrap(__FailableBiFunction.nop())

    @abstractmethod
    def apply(self, arg0: object, arg1: object):
        """public abstract R org.apache.commons.lang3.function.FailableBiFunction.apply(T,U) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableFunction') -> 'FailableBiFunction':
        """public default <V> org.apache.commons.lang3.function.FailableBiFunction<T, U, V, E> org.apache.commons.lang3.function.FailableBiFunction.andThen(org.apache.commons.lang3.function.FailableFunction<? super R, ? extends V, E>)"""
        return 'FailableBiFunction'.__wrap(super(__FailableBiFunction, self).andThen(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntSupplier
import org.apache.commons.lang3.function.FailableIntSupplier as __FailableIntSupplier
__FailableIntSupplier = __FailableIntSupplier
from abc import abstractmethod, ABC
 
class FailableIntSupplier(ABC):
    """org.apache.commons.lang3.function.FailableIntSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntSupplier) -> 'FailableIntSupplier':
        return FailableIntSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntSupplier):
        """
        Dynamic initializer for FailableIntSupplier.
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
    def getAsInt(self, ):
        """public abstract int org.apache.commons.lang3.function.FailableIntSupplier.getAsInt() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.ToBooleanBiFunction
import org.apache.commons.lang3.function.ToBooleanBiFunction as __ToBooleanBiFunction
__ToBooleanBiFunction = __ToBooleanBiFunction
from abc import abstractmethod, ABC
 
class ToBooleanBiFunction(ABC):
    """org.apache.commons.lang3.function.ToBooleanBiFunction"""
 
    @staticmethod
    def __wrap(java_value: __ToBooleanBiFunction) -> 'ToBooleanBiFunction':
        return ToBooleanBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToBooleanBiFunction):
        """
        Dynamic initializer for ToBooleanBiFunction.
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
    def applyAsBoolean(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.lang3.function.ToBooleanBiFunction.applyAsBoolean(T,U)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleBinaryOperator
import org.apache.commons.lang3.function.FailableDoubleBinaryOperator as __FailableDoubleBinaryOperator
__FailableDoubleBinaryOperator = __FailableDoubleBinaryOperator
from abc import abstractmethod, ABC
 
class FailableDoubleBinaryOperator(ABC):
    """org.apache.commons.lang3.function.FailableDoubleBinaryOperator"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoubleBinaryOperator) -> 'FailableDoubleBinaryOperator':
        return FailableDoubleBinaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoubleBinaryOperator):
        """
        Dynamic initializer for FailableDoubleBinaryOperator.
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
    def applyAsDouble(self, arg0: float, arg1: float):
        """public abstract double org.apache.commons.lang3.function.FailableDoubleBinaryOperator.applyAsDouble(double,double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleToIntFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableDoubleToIntFunction as __FailableDoubleToIntFunction
__FailableDoubleToIntFunction = __FailableDoubleToIntFunction
 
class FailableDoubleToIntFunction(ABC):
    """org.apache.commons.lang3.function.FailableDoubleToIntFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoubleToIntFunction) -> 'FailableDoubleToIntFunction':
        return FailableDoubleToIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoubleToIntFunction):
        """
        Dynamic initializer for FailableDoubleToIntFunction.
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
    def applyAsInt(self, arg0: float):
        """public abstract int org.apache.commons.lang3.function.FailableDoubleToIntFunction.applyAsInt(double) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableDoubleToIntFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleToIntFunction<E> org.apache.commons.lang3.function.FailableDoubleToIntFunction.nop()"""
        return FailableDoubleToIntFunction.__wrap(__FailableDoubleToIntFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableCallable
import org.apache.commons.lang3.function.FailableCallable as __FailableCallable
__FailableCallable = __FailableCallable
from abc import abstractmethod, ABC
 
class FailableCallable(ABC):
    """org.apache.commons.lang3.function.FailableCallable"""
 
    @staticmethod
    def __wrap(java_value: __FailableCallable) -> 'FailableCallable':
        return FailableCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableCallable):
        """
        Dynamic initializer for FailableCallable.
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
    def call(self, ):
        """public abstract R org.apache.commons.lang3.function.FailableCallable.call() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongToIntFunction
import org.apache.commons.lang3.function.FailableLongToIntFunction as __FailableLongToIntFunction
__FailableLongToIntFunction = __FailableLongToIntFunction
from abc import abstractmethod, ABC
 
class FailableLongToIntFunction(ABC):
    """org.apache.commons.lang3.function.FailableLongToIntFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongToIntFunction) -> 'FailableLongToIntFunction':
        return FailableLongToIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongToIntFunction):
        """
        Dynamic initializer for FailableLongToIntFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableLongToIntFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongToIntFunction<E> org.apache.commons.lang3.function.FailableLongToIntFunction.nop()"""
        return FailableLongToIntFunction.__wrap(__FailableLongToIntFunction.nop())

    @abstractmethod
    def applyAsInt(self, arg0: int):
        """public abstract int org.apache.commons.lang3.function.FailableLongToIntFunction.applyAsInt(long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongSupplier
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableLongSupplier as __FailableLongSupplier
__FailableLongSupplier = __FailableLongSupplier
 
class FailableLongSupplier(ABC):
    """org.apache.commons.lang3.function.FailableLongSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongSupplier) -> 'FailableLongSupplier':
        return FailableLongSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongSupplier):
        """
        Dynamic initializer for FailableLongSupplier.
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
    def getAsLong(self, ):
        """public abstract long org.apache.commons.lang3.function.FailableLongSupplier.getAsLong() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleUnaryOperator
import org.apache.commons.lang3.function.FailableDoubleUnaryOperator as __FailableDoubleUnaryOperator
__FailableDoubleUnaryOperator = __FailableDoubleUnaryOperator
from abc import abstractmethod, ABC
 
class FailableDoubleUnaryOperator(ABC):
    """org.apache.commons.lang3.function.FailableDoubleUnaryOperator"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoubleUnaryOperator) -> 'FailableDoubleUnaryOperator':
        return FailableDoubleUnaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoubleUnaryOperator):
        """
        Dynamic initializer for FailableDoubleUnaryOperator.
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
 
    @overload
    def compose(self, arg0: 'FailableDoubleUnaryOperator') -> 'FailableDoubleUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.compose(org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E>)"""
        return 'FailableDoubleUnaryOperator'.__wrap(super(__FailableDoubleUnaryOperator, self).compose(arg0))

    @abstractmethod
    def applyAsDouble(self, arg0: float):
        """public abstract double org.apache.commons.lang3.function.FailableDoubleUnaryOperator.applyAsDouble(double) throws E"""
        pass

    @staticmethod
    @overload
    def identity() -> 'FailableDoubleUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.identity()"""
        return FailableDoubleUnaryOperator.__wrap(__FailableDoubleUnaryOperator.identity())

    @overload
    def andThen(self, arg0: 'FailableDoubleUnaryOperator') -> 'FailableDoubleUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.andThen(org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E>)"""
        return 'FailableDoubleUnaryOperator'.__wrap(super(__FailableDoubleUnaryOperator, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableDoubleUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.nop()"""
        return FailableDoubleUnaryOperator.__wrap(__FailableDoubleUnaryOperator.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntToLongFunction
import org.apache.commons.lang3.function.FailableIntToLongFunction as __FailableIntToLongFunction
__FailableIntToLongFunction = __FailableIntToLongFunction
from abc import abstractmethod, ABC
 
class FailableIntToLongFunction(ABC):
    """org.apache.commons.lang3.function.FailableIntToLongFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntToLongFunction) -> 'FailableIntToLongFunction':
        return FailableIntToLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntToLongFunction):
        """
        Dynamic initializer for FailableIntToLongFunction.
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
    def applyAsLong(self, arg0: int):
        """public abstract long org.apache.commons.lang3.function.FailableIntToLongFunction.applyAsLong(int) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableIntToLongFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntToLongFunction<E> org.apache.commons.lang3.function.FailableIntToLongFunction.nop()"""
        return FailableIntToLongFunction.__wrap(__FailableIntToLongFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToDoubleFunction
import org.apache.commons.lang3.function.FailableToDoubleFunction as __FailableToDoubleFunction
__FailableToDoubleFunction = __FailableToDoubleFunction
from abc import abstractmethod, ABC
 
class FailableToDoubleFunction(ABC):
    """org.apache.commons.lang3.function.FailableToDoubleFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableToDoubleFunction) -> 'FailableToDoubleFunction':
        return FailableToDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableToDoubleFunction):
        """
        Dynamic initializer for FailableToDoubleFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableToDoubleFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToDoubleFunction<T, E> org.apache.commons.lang3.function.FailableToDoubleFunction.nop()"""
        return FailableToDoubleFunction.__wrap(__FailableToDoubleFunction.nop())

    @abstractmethod
    def applyAsDouble(self, arg0: object):
        """public abstract double org.apache.commons.lang3.function.FailableToDoubleFunction.applyAsDouble(T) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntPredicate
import org.apache.commons.lang3.function.FailableIntPredicate as __FailableIntPredicate
__FailableIntPredicate = __FailableIntPredicate
from abc import abstractmethod, ABC
 
class FailableIntPredicate(ABC):
    """org.apache.commons.lang3.function.FailableIntPredicate"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntPredicate) -> 'FailableIntPredicate':
        return FailableIntPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntPredicate):
        """
        Dynamic initializer for FailableIntPredicate.
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
 
    @staticmethod
    @overload
    def falsePredicate() -> 'FailableIntPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.falsePredicate()"""
        return FailableIntPredicate.__wrap(__FailableIntPredicate.falsePredicate())

    @overload
    def negate(self) -> 'FailableIntPredicate':
        """public default org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.negate()"""
        return 'FailableIntPredicate'.__wrap(super(FailableIntPredicate, self).negate())

    @staticmethod
    @overload
    def truePredicate() -> 'FailableIntPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.truePredicate()"""
        return FailableIntPredicate.__wrap(__FailableIntPredicate.truePredicate())

    @overload
    def and(self, arg0: 'FailableIntPredicate') -> 'FailableIntPredicate':
        """public default org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.and(org.apache.commons.lang3.function.FailableIntPredicate<E>)"""
        return 'FailableIntPredicate'.__wrap(super(__FailableIntPredicate, self).and(arg0))

    @abstractmethod
    def test(self, arg0: int):
        """public abstract boolean org.apache.commons.lang3.function.FailableIntPredicate.test(int) throws E"""
        pass

    @overload
    def or(self, arg0: 'FailableIntPredicate') -> 'FailableIntPredicate':
        """public default org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.or(org.apache.commons.lang3.function.FailableIntPredicate<E>)"""
        return 'FailableIntPredicate'.__wrap(super(__FailableIntPredicate, self).or(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleSupplier
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableDoubleSupplier as __FailableDoubleSupplier
__FailableDoubleSupplier = __FailableDoubleSupplier
 
class FailableDoubleSupplier(ABC):
    """org.apache.commons.lang3.function.FailableDoubleSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoubleSupplier) -> 'FailableDoubleSupplier':
        return FailableDoubleSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoubleSupplier):
        """
        Dynamic initializer for FailableDoubleSupplier.
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
    def getAsDouble(self, ):
        """public abstract double org.apache.commons.lang3.function.FailableDoubleSupplier.getAsDouble() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToIntBiFunction
import org.apache.commons.lang3.function.FailableToIntBiFunction as __FailableToIntBiFunction
__FailableToIntBiFunction = __FailableToIntBiFunction
from abc import abstractmethod, ABC
 
class FailableToIntBiFunction(ABC):
    """org.apache.commons.lang3.function.FailableToIntBiFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableToIntBiFunction) -> 'FailableToIntBiFunction':
        return FailableToIntBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableToIntBiFunction):
        """
        Dynamic initializer for FailableToIntBiFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableToIntBiFunction':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToIntBiFunction<T, U, E> org.apache.commons.lang3.function.FailableToIntBiFunction.nop()"""
        return FailableToIntBiFunction.__wrap(__FailableToIntBiFunction.nop())

    @abstractmethod
    def applyAsInt(self, arg0: object, arg1: object):
        """public abstract int org.apache.commons.lang3.function.FailableToIntBiFunction.applyAsInt(T,U) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongPredicate
import org.apache.commons.lang3.function.FailableLongPredicate as __FailableLongPredicate
__FailableLongPredicate = __FailableLongPredicate
from abc import abstractmethod, ABC
 
class FailableLongPredicate(ABC):
    """org.apache.commons.lang3.function.FailableLongPredicate"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongPredicate) -> 'FailableLongPredicate':
        return FailableLongPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongPredicate):
        """
        Dynamic initializer for FailableLongPredicate.
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
 
    @overload
    def and(self, arg0: 'FailableLongPredicate') -> 'FailableLongPredicate':
        """public default org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.and(org.apache.commons.lang3.function.FailableLongPredicate<E>)"""
        return 'FailableLongPredicate'.__wrap(super(__FailableLongPredicate, self).and(arg0))

    @abstractmethod
    def test(self, arg0: int):
        """public abstract boolean org.apache.commons.lang3.function.FailableLongPredicate.test(long) throws E"""
        pass

    @overload
    def negate(self) -> 'FailableLongPredicate':
        """public default org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.negate()"""
        return 'FailableLongPredicate'.__wrap(super(FailableLongPredicate, self).negate())

    @staticmethod
    @overload
    def falsePredicate() -> 'FailableLongPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.falsePredicate()"""
        return FailableLongPredicate.__wrap(__FailableLongPredicate.falsePredicate())

    @staticmethod
    @overload
    def truePredicate() -> 'FailableLongPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.truePredicate()"""
        return FailableLongPredicate.__wrap(__FailableLongPredicate.truePredicate())

    @overload
    def or(self, arg0: 'FailableLongPredicate') -> 'FailableLongPredicate':
        """public default org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.or(org.apache.commons.lang3.function.FailableLongPredicate<E>)"""
        return 'FailableLongPredicate'.__wrap(super(__FailableLongPredicate, self).or(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongToDoubleFunction
import org.apache.commons.lang3.function.FailableLongToDoubleFunction as __FailableLongToDoubleFunction
__FailableLongToDoubleFunction = __FailableLongToDoubleFunction
from abc import abstractmethod, ABC
 
class FailableLongToDoubleFunction(ABC):
    """org.apache.commons.lang3.function.FailableLongToDoubleFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongToDoubleFunction) -> 'FailableLongToDoubleFunction':
        return FailableLongToDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongToDoubleFunction):
        """
        Dynamic initializer for FailableLongToDoubleFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableLongToDoubleFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongToDoubleFunction<E> org.apache.commons.lang3.function.FailableLongToDoubleFunction.nop()"""
        return FailableLongToDoubleFunction.__wrap(__FailableLongToDoubleFunction.nop())

    @abstractmethod
    def applyAsDouble(self, arg0: int):
        """public abstract double org.apache.commons.lang3.function.FailableLongToDoubleFunction.applyAsDouble(long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleToLongFunction
import org.apache.commons.lang3.function.FailableDoubleToLongFunction as __FailableDoubleToLongFunction
__FailableDoubleToLongFunction = __FailableDoubleToLongFunction
from abc import abstractmethod, ABC
 
class FailableDoubleToLongFunction(ABC):
    """org.apache.commons.lang3.function.FailableDoubleToLongFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableDoubleToLongFunction) -> 'FailableDoubleToLongFunction':
        return FailableDoubleToLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableDoubleToLongFunction):
        """
        Dynamic initializer for FailableDoubleToLongFunction.
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
    def applyAsLong(self, arg0: float):
        """public abstract int org.apache.commons.lang3.function.FailableDoubleToLongFunction.applyAsLong(double) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableDoubleToLongFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleToLongFunction<E> org.apache.commons.lang3.function.FailableDoubleToLongFunction.nop()"""
        return FailableDoubleToLongFunction.__wrap(__FailableDoubleToLongFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongUnaryOperator
import org.apache.commons.lang3.function.FailableLongUnaryOperator as __FailableLongUnaryOperator
__FailableLongUnaryOperator = __FailableLongUnaryOperator
from abc import abstractmethod, ABC
 
class FailableLongUnaryOperator(ABC):
    """org.apache.commons.lang3.function.FailableLongUnaryOperator"""
 
    @staticmethod
    def __wrap(java_value: __FailableLongUnaryOperator) -> 'FailableLongUnaryOperator':
        return FailableLongUnaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableLongUnaryOperator):
        """
        Dynamic initializer for FailableLongUnaryOperator.
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
 
    @staticmethod
    @overload
    def identity() -> 'FailableLongUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.identity()"""
        return FailableLongUnaryOperator.__wrap(__FailableLongUnaryOperator.identity())

    @staticmethod
    @overload
    def nop() -> 'FailableLongUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.nop()"""
        return FailableLongUnaryOperator.__wrap(__FailableLongUnaryOperator.nop())

    @overload
    def compose(self, arg0: 'FailableLongUnaryOperator') -> 'FailableLongUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.compose(org.apache.commons.lang3.function.FailableLongUnaryOperator<E>)"""
        return 'FailableLongUnaryOperator'.__wrap(super(__FailableLongUnaryOperator, self).compose(arg0))

    @abstractmethod
    def applyAsLong(self, arg0: int):
        """public abstract long org.apache.commons.lang3.function.FailableLongUnaryOperator.applyAsLong(long) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableLongUnaryOperator') -> 'FailableLongUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.andThen(org.apache.commons.lang3.function.FailableLongUnaryOperator<E>)"""
        return 'FailableLongUnaryOperator'.__wrap(super(__FailableLongUnaryOperator, self).andThen(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableIntFunction as __FailableIntFunction
__FailableIntFunction = __FailableIntFunction
 
class FailableIntFunction(ABC):
    """org.apache.commons.lang3.function.FailableIntFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntFunction) -> 'FailableIntFunction':
        return FailableIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntFunction):
        """
        Dynamic initializer for FailableIntFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableIntFunction':
        """public static <R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntFunction<R, E> org.apache.commons.lang3.function.FailableIntFunction.nop()"""
        return FailableIntFunction.__wrap(__FailableIntFunction.nop())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract R org.apache.commons.lang3.function.FailableIntFunction.apply(int) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.Consumers
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.function.Consumers as __Consumers
__Consumers = __Consumers
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Consumers():
    """org.apache.commons.lang3.function.Consumers"""
 
    @staticmethod
    def __wrap(java_value: __Consumers) -> 'Consumers':
        return Consumers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Consumers):
        """
        Dynamic initializer for Consumers.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nop() -> 'Consumer':
        """public static <T> java.util.function.Consumer<T> org.apache.commons.lang3.function.Consumers.nop()"""
        return Consumer.__wrap(__Consumers.nop())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntUnaryOperator
import org.apache.commons.lang3.function.FailableIntUnaryOperator as __FailableIntUnaryOperator
__FailableIntUnaryOperator = __FailableIntUnaryOperator
from abc import abstractmethod, ABC
 
class FailableIntUnaryOperator(ABC):
    """org.apache.commons.lang3.function.FailableIntUnaryOperator"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntUnaryOperator) -> 'FailableIntUnaryOperator':
        return FailableIntUnaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntUnaryOperator):
        """
        Dynamic initializer for FailableIntUnaryOperator.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableIntUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.nop()"""
        return FailableIntUnaryOperator.__wrap(__FailableIntUnaryOperator.nop())

    @overload
    def compose(self, arg0: 'FailableIntUnaryOperator') -> 'FailableIntUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.compose(org.apache.commons.lang3.function.FailableIntUnaryOperator<E>)"""
        return 'FailableIntUnaryOperator'.__wrap(super(__FailableIntUnaryOperator, self).compose(arg0))

    @staticmethod
    @overload
    def identity() -> 'FailableIntUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.identity()"""
        return FailableIntUnaryOperator.__wrap(__FailableIntUnaryOperator.identity())

    @abstractmethod
    def applyAsInt(self, arg0: int):
        """public abstract int org.apache.commons.lang3.function.FailableIntUnaryOperator.applyAsInt(int) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableIntUnaryOperator') -> 'FailableIntUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.andThen(org.apache.commons.lang3.function.FailableIntUnaryOperator<E>)"""
        return 'FailableIntUnaryOperator'.__wrap(super(__FailableIntUnaryOperator, self).andThen(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToLongFunction
import org.apache.commons.lang3.function.FailableToLongFunction as __FailableToLongFunction
__FailableToLongFunction = __FailableToLongFunction
from abc import abstractmethod, ABC
 
class FailableToLongFunction(ABC):
    """org.apache.commons.lang3.function.FailableToLongFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableToLongFunction) -> 'FailableToLongFunction':
        return FailableToLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableToLongFunction):
        """
        Dynamic initializer for FailableToLongFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableToLongFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToLongFunction<T, E> org.apache.commons.lang3.function.FailableToLongFunction.nop()"""
        return FailableToLongFunction.__wrap(__FailableToLongFunction.nop())

    @abstractmethod
    def applyAsLong(self, arg0: object):
        """public abstract long org.apache.commons.lang3.function.FailableToLongFunction.applyAsLong(T) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntBinaryOperator
import org.apache.commons.lang3.function.FailableIntBinaryOperator as __FailableIntBinaryOperator
__FailableIntBinaryOperator = __FailableIntBinaryOperator
from abc import abstractmethod, ABC
 
class FailableIntBinaryOperator(ABC):
    """org.apache.commons.lang3.function.FailableIntBinaryOperator"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntBinaryOperator) -> 'FailableIntBinaryOperator':
        return FailableIntBinaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntBinaryOperator):
        """
        Dynamic initializer for FailableIntBinaryOperator.
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
    def applyAsInt(self, arg0: int, arg1: int):
        """public abstract int org.apache.commons.lang3.function.FailableIntBinaryOperator.applyAsInt(int,int) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableObjLongConsumer
import org.apache.commons.lang3.function.FailableObjLongConsumer as __FailableObjLongConsumer
__FailableObjLongConsumer = __FailableObjLongConsumer
from abc import abstractmethod, ABC
 
class FailableObjLongConsumer(ABC):
    """org.apache.commons.lang3.function.FailableObjLongConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableObjLongConsumer) -> 'FailableObjLongConsumer':
        return FailableObjLongConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableObjLongConsumer):
        """
        Dynamic initializer for FailableObjLongConsumer.
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
    def accept(self, arg0: object, arg1: int):
        """public abstract void org.apache.commons.lang3.function.FailableObjLongConsumer.accept(T,long) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableObjLongConsumer':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableObjLongConsumer<T, E> org.apache.commons.lang3.function.FailableObjLongConsumer.nop()"""
        return FailableObjLongConsumer.__wrap(__FailableObjLongConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.TriFunction
import org.apache.commons.lang3.function.TriFunction as __TriFunction
__TriFunction = __TriFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class TriFunction(ABC):
    """org.apache.commons.lang3.function.TriFunction"""
 
    @staticmethod
    def __wrap(java_value: __TriFunction) -> 'TriFunction':
        return TriFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriFunction):
        """
        Dynamic initializer for TriFunction.
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
 
    @overload
    def andThen(self, arg0: 'Function') -> 'TriFunction':
        """public default <W> org.apache.commons.lang3.function.TriFunction<T, U, V, W> org.apache.commons.lang3.function.TriFunction.andThen(java.util.function.Function<? super R, ? extends W>)"""
        return 'TriFunction'.__wrap(super(__TriFunction, self).andThen(arg0))

    @abstractmethod
    def apply(self, arg0: object, arg1: object, arg2: object):
        """public abstract R org.apache.commons.lang3.function.TriFunction.apply(T,U,V)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableRunnable
import org.apache.commons.lang3.function.FailableRunnable as __FailableRunnable
__FailableRunnable = __FailableRunnable
from abc import abstractmethod, ABC
 
class FailableRunnable(ABC):
    """org.apache.commons.lang3.function.FailableRunnable"""
 
    @staticmethod
    def __wrap(java_value: __FailableRunnable) -> 'FailableRunnable':
        return FailableRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableRunnable):
        """
        Dynamic initializer for FailableRunnable.
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
    def run(self, ):
        """public abstract void org.apache.commons.lang3.function.FailableRunnable.run() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBiPredicate
import org.apache.commons.lang3.function.FailableBiPredicate as __FailableBiPredicate
__FailableBiPredicate = __FailableBiPredicate
from abc import abstractmethod, ABC
 
class FailableBiPredicate(ABC):
    """org.apache.commons.lang3.function.FailableBiPredicate"""
 
    @staticmethod
    def __wrap(java_value: __FailableBiPredicate) -> 'FailableBiPredicate':
        return FailableBiPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableBiPredicate):
        """
        Dynamic initializer for FailableBiPredicate.
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
 
    @staticmethod
    @overload
    def truePredicate() -> 'FailableBiPredicate':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.truePredicate()"""
        return FailableBiPredicate.__wrap(__FailableBiPredicate.truePredicate())

    @abstractmethod
    def test(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.lang3.function.FailableBiPredicate.test(T,U) throws E"""
        pass

    @overload
    def and(self, arg0: 'FailableBiPredicate') -> 'FailableBiPredicate':
        """public default org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.and(org.apache.commons.lang3.function.FailableBiPredicate<? super T, ? super U, E>)"""
        return 'FailableBiPredicate'.__wrap(super(__FailableBiPredicate, self).and(arg0))

    @staticmethod
    @overload
    def falsePredicate() -> 'FailableBiPredicate':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.falsePredicate()"""
        return FailableBiPredicate.__wrap(__FailableBiPredicate.falsePredicate())

    @overload
    def negate(self) -> 'FailableBiPredicate':
        """public default org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.negate()"""
        return 'FailableBiPredicate'.__wrap(super(FailableBiPredicate, self).negate())

    @overload
    def or(self, arg0: 'FailableBiPredicate') -> 'FailableBiPredicate':
        """public default org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.or(org.apache.commons.lang3.function.FailableBiPredicate<? super T, ? super U, E>)"""
        return 'FailableBiPredicate'.__wrap(super(__FailableBiPredicate, self).or(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableObjIntConsumer
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableObjIntConsumer as __FailableObjIntConsumer
__FailableObjIntConsumer = __FailableObjIntConsumer
 
class FailableObjIntConsumer(ABC):
    """org.apache.commons.lang3.function.FailableObjIntConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableObjIntConsumer) -> 'FailableObjIntConsumer':
        return FailableObjIntConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableObjIntConsumer):
        """
        Dynamic initializer for FailableObjIntConsumer.
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
    def accept(self, arg0: object, arg1: int):
        """public abstract void org.apache.commons.lang3.function.FailableObjIntConsumer.accept(T,int) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableObjIntConsumer':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableObjIntConsumer<T, E> org.apache.commons.lang3.function.FailableObjIntConsumer.nop()"""
        return FailableObjIntConsumer.__wrap(__FailableObjIntConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.BooleanConsumer
import org.apache.commons.lang3.function.BooleanConsumer as __BooleanConsumer
__BooleanConsumer = __BooleanConsumer
from abc import abstractmethod, ABC
 
class BooleanConsumer(ABC):
    """org.apache.commons.lang3.function.BooleanConsumer"""
 
    @staticmethod
    def __wrap(java_value: __BooleanConsumer) -> 'BooleanConsumer':
        return BooleanConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanConsumer):
        """
        Dynamic initializer for BooleanConsumer.
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
    def accept(self, arg0: bool):
        """public abstract void org.apache.commons.lang3.function.BooleanConsumer.accept(boolean)"""
        pass

    @overload
    def andThen(self, arg0: 'BooleanConsumer') -> 'BooleanConsumer':
        """public default org.apache.commons.lang3.function.BooleanConsumer org.apache.commons.lang3.function.BooleanConsumer.andThen(org.apache.commons.lang3.function.BooleanConsumer)"""
        return 'BooleanConsumer'.__wrap(super(__BooleanConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'BooleanConsumer':
        """public static org.apache.commons.lang3.function.BooleanConsumer org.apache.commons.lang3.function.BooleanConsumer.nop()"""
        return BooleanConsumer.__wrap(__BooleanConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntConsumer
import org.apache.commons.lang3.function.FailableIntConsumer as __FailableIntConsumer
__FailableIntConsumer = __FailableIntConsumer
from abc import abstractmethod, ABC
 
class FailableIntConsumer(ABC):
    """org.apache.commons.lang3.function.FailableIntConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableIntConsumer) -> 'FailableIntConsumer':
        return FailableIntConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableIntConsumer):
        """
        Dynamic initializer for FailableIntConsumer.
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
    def accept(self, arg0: int):
        """public abstract void org.apache.commons.lang3.function.FailableIntConsumer.accept(int) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableIntConsumer':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntConsumer<E> org.apache.commons.lang3.function.FailableIntConsumer.nop()"""
        return FailableIntConsumer.__wrap(__FailableIntConsumer.nop())

    @overload
    def andThen(self, arg0: 'FailableIntConsumer') -> 'FailableIntConsumer':
        """public default org.apache.commons.lang3.function.FailableIntConsumer<E> org.apache.commons.lang3.function.FailableIntConsumer.andThen(org.apache.commons.lang3.function.FailableIntConsumer<E>)"""
        return 'FailableIntConsumer'.__wrap(super(__FailableIntConsumer, self).andThen(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableFunction as __FailableFunction
__FailableFunction = __FailableFunction
 
class FailableFunction(ABC):
    """org.apache.commons.lang3.function.FailableFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableFunction) -> 'FailableFunction':
        return FailableFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableFunction):
        """
        Dynamic initializer for FailableFunction.
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
 
    @staticmethod
    @overload
    def identity() -> 'FailableFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableFunction<T, T, E> org.apache.commons.lang3.function.FailableFunction.identity()"""
        return FailableFunction.__wrap(__FailableFunction.identity())

    @abstractmethod
    def apply(self, arg0: object):
        """public abstract R org.apache.commons.lang3.function.FailableFunction.apply(T) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableFunction':
        """public static <T,R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableFunction<T, R, E> org.apache.commons.lang3.function.FailableFunction.nop()"""
        return FailableFunction.__wrap(__FailableFunction.nop())

    @overload
    def compose(self, arg0: 'FailableFunction') -> 'FailableFunction':
        """public default <V> org.apache.commons.lang3.function.FailableFunction<V, R, E> org.apache.commons.lang3.function.FailableFunction.compose(org.apache.commons.lang3.function.FailableFunction<? super V, ? extends T, E>)"""
        return 'FailableFunction'.__wrap(super(__FailableFunction, self).compose(arg0))

    @overload
    def andThen(self, arg0: 'FailableFunction') -> 'FailableFunction':
        """public default <V> org.apache.commons.lang3.function.FailableFunction<T, V, E> org.apache.commons.lang3.function.FailableFunction.andThen(org.apache.commons.lang3.function.FailableFunction<? super R, ? extends V, E>)"""
        return 'FailableFunction'.__wrap(super(__FailableFunction, self).andThen(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableObjDoubleConsumer
import org.apache.commons.lang3.function.FailableObjDoubleConsumer as __FailableObjDoubleConsumer
__FailableObjDoubleConsumer = __FailableObjDoubleConsumer
from abc import abstractmethod, ABC
 
class FailableObjDoubleConsumer(ABC):
    """org.apache.commons.lang3.function.FailableObjDoubleConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableObjDoubleConsumer) -> 'FailableObjDoubleConsumer':
        return FailableObjDoubleConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableObjDoubleConsumer):
        """
        Dynamic initializer for FailableObjDoubleConsumer.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableObjDoubleConsumer':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableObjDoubleConsumer<T, E> org.apache.commons.lang3.function.FailableObjDoubleConsumer.nop()"""
        return FailableObjDoubleConsumer.__wrap(__FailableObjDoubleConsumer.nop())

    @abstractmethod
    def accept(self, arg0: object, arg1: float):
        """public abstract void org.apache.commons.lang3.function.FailableObjDoubleConsumer.accept(T,double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailablePredicate
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailablePredicate as __FailablePredicate
__FailablePredicate = __FailablePredicate
 
class FailablePredicate(ABC):
    """org.apache.commons.lang3.function.FailablePredicate"""
 
    @staticmethod
    def __wrap(java_value: __FailablePredicate) -> 'FailablePredicate':
        return FailablePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailablePredicate):
        """
        Dynamic initializer for FailablePredicate.
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
    def test(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.function.FailablePredicate.test(T) throws E"""
        pass

    @overload
    def or(self, arg0: 'FailablePredicate') -> 'FailablePredicate':
        """public default org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.or(org.apache.commons.lang3.function.FailablePredicate<? super T, E>)"""
        return 'FailablePredicate'.__wrap(super(__FailablePredicate, self).or(arg0))

    @staticmethod
    @overload
    def falsePredicate() -> 'FailablePredicate':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.falsePredicate()"""
        return FailablePredicate.__wrap(__FailablePredicate.falsePredicate())

    @overload
    def negate(self) -> 'FailablePredicate':
        """public default org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.negate()"""
        return 'FailablePredicate'.__wrap(super(FailablePredicate, self).negate())

    @staticmethod
    @overload
    def truePredicate() -> 'FailablePredicate':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.truePredicate()"""
        return FailablePredicate.__wrap(__FailablePredicate.truePredicate())

    @overload
    def and(self, arg0: 'FailablePredicate') -> 'FailablePredicate':
        """public default org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.and(org.apache.commons.lang3.function.FailablePredicate<? super T, E>)"""
        return 'FailablePredicate'.__wrap(super(__FailablePredicate, self).and(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToLongBiFunction
import org.apache.commons.lang3.function.FailableToLongBiFunction as __FailableToLongBiFunction
__FailableToLongBiFunction = __FailableToLongBiFunction
from abc import abstractmethod, ABC
 
class FailableToLongBiFunction(ABC):
    """org.apache.commons.lang3.function.FailableToLongBiFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableToLongBiFunction) -> 'FailableToLongBiFunction':
        return FailableToLongBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableToLongBiFunction):
        """
        Dynamic initializer for FailableToLongBiFunction.
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
 
    @staticmethod
    @overload
    def nop() -> 'FailableToLongBiFunction':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToLongBiFunction<T, U, E> org.apache.commons.lang3.function.FailableToLongBiFunction.nop()"""
        return FailableToLongBiFunction.__wrap(__FailableToLongBiFunction.nop())

    @abstractmethod
    def applyAsLong(self, arg0: object, arg1: object):
        """public abstract long org.apache.commons.lang3.function.FailableToLongBiFunction.applyAsLong(T,U) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableConsumer
import org.apache.commons.lang3.function.FailableConsumer as __FailableConsumer
__FailableConsumer = __FailableConsumer
from abc import abstractmethod, ABC
 
class FailableConsumer(ABC):
    """org.apache.commons.lang3.function.FailableConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableConsumer) -> 'FailableConsumer':
        return FailableConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableConsumer):
        """
        Dynamic initializer for FailableConsumer.
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
    def accept(self, arg0: object):
        """public abstract void org.apache.commons.lang3.function.FailableConsumer.accept(T) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableConsumer') -> 'FailableConsumer':
        """public default org.apache.commons.lang3.function.FailableConsumer<T, E> org.apache.commons.lang3.function.FailableConsumer.andThen(org.apache.commons.lang3.function.FailableConsumer<? super T, E>)"""
        return 'FailableConsumer'.__wrap(super(__FailableConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableConsumer':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableConsumer<T, E> org.apache.commons.lang3.function.FailableConsumer.nop()"""
        return FailableConsumer.__wrap(__FailableConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.MethodInvokers
import java.util.function.Supplier as Supplier
import org.apache.commons.lang3.function.FailableBiConsumer as __FailableBiConsumer
__FailableBiConsumer = __FailableBiConsumer
import org.apache.commons.lang3.function.FailableBiFunction as __FailableBiFunction
__FailableBiFunction = __FailableBiFunction
from builtins import type
import org.apache.commons.lang3.function.FailableFunction as __FailableFunction
__FailableFunction = __FailableFunction
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
import org.apache.commons.lang3.function.FailableSupplier as __FailableSupplier
__FailableSupplier = __FailableSupplier
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.function.MethodInvokers as __MethodInvokers
__MethodInvokers = __MethodInvokers
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.util.function.BiConsumer as __BiConsumer
__BiConsumer = __BiConsumer
import java.lang.Integer as __int
import java.lang.reflect.Method as Method
from builtins import int
 
class MethodInvokers():
    """org.apache.commons.lang3.function.MethodInvokers"""
 
    @staticmethod
    def __wrap(java_value: __MethodInvokers) -> 'MethodInvokers':
        return MethodInvokers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MethodInvokers):
        """
        Dynamic initializer for MethodInvokers.
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
    def asFailableFunction(arg0: 'Method') -> 'FailableFunction':
        """public static <T,R> org.apache.commons.lang3.function.FailableFunction<T, R, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableFunction(java.lang.reflect.Method)"""
        return FailableFunction.__wrap(__MethodInvokers.asFailableFunction(arg0))

    @staticmethod
    @overload
    def asBiConsumer(arg0: 'Method') -> 'BiConsumer':
        """public static <T,U> java.util.function.BiConsumer<T, U> org.apache.commons.lang3.function.MethodInvokers.asBiConsumer(java.lang.reflect.Method)"""
        return BiConsumer.__wrap(__MethodInvokers.asBiConsumer(arg0))

    @staticmethod
    @overload
    def asFailableBiFunction(arg0: 'Method') -> 'FailableBiFunction':
        """public static <T,U,R> org.apache.commons.lang3.function.FailableBiFunction<T, U, R, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableBiFunction(java.lang.reflect.Method)"""
        return FailableBiFunction.__wrap(__MethodInvokers.asFailableBiFunction(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def asBiFunction(arg0: 'Method') -> 'BiFunction':
        """public static <T,U,R> java.util.function.BiFunction<T, U, R> org.apache.commons.lang3.function.MethodInvokers.asBiFunction(java.lang.reflect.Method)"""
        return BiFunction.__wrap(__MethodInvokers.asBiFunction(arg0))

    @staticmethod
    @overload
    def asFunction(arg0: 'Method') -> 'Function':
        """public static <T,R> java.util.function.Function<T, R> org.apache.commons.lang3.function.MethodInvokers.asFunction(java.lang.reflect.Method)"""
        return Function.__wrap(__MethodInvokers.asFunction(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def asInterfaceInstance(arg0: 'Class', arg1: 'Method') -> object:
        """public static <T> T org.apache.commons.lang3.function.MethodInvokers.asInterfaceInstance(java.lang.Class<T>,java.lang.reflect.Method)"""
        return object.__wrap(__MethodInvokers.asInterfaceInstance(arg0, arg1))

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
    def asFailableBiConsumer(arg0: 'Method') -> 'FailableBiConsumer':
        """public static <T,U> org.apache.commons.lang3.function.FailableBiConsumer<T, U, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableBiConsumer(java.lang.reflect.Method)"""
        return FailableBiConsumer.__wrap(__MethodInvokers.asFailableBiConsumer(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def asSupplier(arg0: 'Method') -> 'Supplier':
        """public static <R> java.util.function.Supplier<R> org.apache.commons.lang3.function.MethodInvokers.asSupplier(java.lang.reflect.Method)"""
        return Supplier.__wrap(__MethodInvokers.asSupplier(arg0))

    @staticmethod
    @overload
    def asFailableSupplier(arg0: 'Method') -> 'FailableSupplier':
        """public static <R> org.apache.commons.lang3.function.FailableSupplier<R, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableSupplier(java.lang.reflect.Method)"""
        return FailableSupplier.__wrap(__MethodInvokers.asFailableSupplier(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))