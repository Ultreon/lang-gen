from __future__ import annotations
from overload import overload


 
import org.apache.commons.lang3.function.FailableToLongFunction as _FailableToLongFunction
_FailableToLongFunction = _FailableToLongFunction
from abc import abstractmethod, ABC
 
class FailableToLongFunction():
    """org.apache.commons.lang3.function.FailableToLongFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableToLongFunction) -> 'FailableToLongFunction':
        return FailableToLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableToLongFunction):
        """
        Dynamic initializer for FailableToLongFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableToLongFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableToLongFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableToLongFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToLongFunction<T, E> org.apache.commons.lang3.function.FailableToLongFunction.nop()"""
        return FailableToLongFunction._wrap(_FailableToLongFunction.nop())

    @abstractmethod
    def applyAsLong(self, arg0: object):
        """public abstract long org.apache.commons.lang3.function.FailableToLongFunction.applyAsLong(T) throws E"""
        pass

 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToLongFunction
import org.apache.commons.lang3.function.FailableToLongFunction as _FailableToLongFunction
_FailableToLongFunction = _FailableToLongFunction
from abc import abstractmethod, ABC
 
class FailableToLongFunction():
    """org.apache.commons.lang3.function.FailableToLongFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableToLongFunction) -> 'FailableToLongFunction':
        return FailableToLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableToLongFunction):
        """
        Dynamic initializer for FailableToLongFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableToLongFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableToLongFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableToLongFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToLongFunction<T, E> org.apache.commons.lang3.function.FailableToLongFunction.nop()"""
        return FailableToLongFunction._wrap(_FailableToLongFunction.nop())

    @abstractmethod
    def applyAsLong(self, arg0: object):
        """public abstract long org.apache.commons.lang3.function.FailableToLongFunction.applyAsLong(T) throws E"""
        pass

 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToLongFunction 
 
 
# CLASS: org.apache.commons.lang3.function.FailablePredicate
import org.apache.commons.lang3.function.FailablePredicate as _FailablePredicate
_FailablePredicate = _FailablePredicate
from abc import abstractmethod, ABC
 
class FailablePredicate():
    """org.apache.commons.lang3.function.FailablePredicate"""
 
    @staticmethod
    def _wrap(java_value: _FailablePredicate) -> 'FailablePredicate':
        return FailablePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailablePredicate):
        """
        Dynamic initializer for FailablePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailablePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailablePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def and(self, arg0: 'FailablePredicate') -> 'FailablePredicate':
        """public default org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.and(org.apache.commons.lang3.function.FailablePredicate<? super T, E>)"""
        return 'FailablePredicate'._wrap(super(_FailablePredicate, self).and(arg0))

    @abstractmethod
    def test(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.function.FailablePredicate.test(T) throws E"""
        pass

    @staticmethod
    @overload
    def truePredicate() -> 'FailablePredicate':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.truePredicate()"""
        return FailablePredicate._wrap(_FailablePredicate.truePredicate())

    @overload
    def or(self, arg0: 'FailablePredicate') -> 'FailablePredicate':
        """public default org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.or(org.apache.commons.lang3.function.FailablePredicate<? super T, E>)"""
        return 'FailablePredicate'._wrap(super(_FailablePredicate, self).or(arg0))

    @staticmethod
    @overload
    def falsePredicate() -> 'FailablePredicate':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.falsePredicate()"""
        return FailablePredicate._wrap(_FailablePredicate.falsePredicate())

    @overload
    def negate(self) -> 'FailablePredicate':
        """public default org.apache.commons.lang3.function.FailablePredicate<T, E> org.apache.commons.lang3.function.FailablePredicate.negate()"""
        return 'FailablePredicate'._wrap(super(FailablePredicate, self).negate()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntFunction
import org.apache.commons.lang3.function.FailableIntFunction as _FailableIntFunction
_FailableIntFunction = _FailableIntFunction
from abc import abstractmethod, ABC
 
class FailableIntFunction():
    """org.apache.commons.lang3.function.FailableIntFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntFunction) -> 'FailableIntFunction':
        return FailableIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntFunction):
        """
        Dynamic initializer for FailableIntFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, arg0: int):
        """public abstract R org.apache.commons.lang3.function.FailableIntFunction.apply(int) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableIntFunction':
        """public static <R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntFunction<R, E> org.apache.commons.lang3.function.FailableIntFunction.nop()"""
        return FailableIntFunction._wrap(_FailableIntFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongUnaryOperator
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableLongUnaryOperator as _FailableLongUnaryOperator
_FailableLongUnaryOperator = _FailableLongUnaryOperator
 
class FailableLongUnaryOperator():
    """org.apache.commons.lang3.function.FailableLongUnaryOperator"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongUnaryOperator) -> 'FailableLongUnaryOperator':
        return FailableLongUnaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongUnaryOperator):
        """
        Dynamic initializer for FailableLongUnaryOperator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongUnaryOperator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongUnaryOperator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def identity() -> 'FailableLongUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.identity()"""
        return FailableLongUnaryOperator._wrap(_FailableLongUnaryOperator.identity())

    @staticmethod
    @overload
    def nop() -> 'FailableLongUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.nop()"""
        return FailableLongUnaryOperator._wrap(_FailableLongUnaryOperator.nop())

    @overload
    def andThen(self, arg0: 'FailableLongUnaryOperator') -> 'FailableLongUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.andThen(org.apache.commons.lang3.function.FailableLongUnaryOperator<E>)"""
        return 'FailableLongUnaryOperator'._wrap(super(_FailableLongUnaryOperator, self).andThen(arg0))

    @overload
    def compose(self, arg0: 'FailableLongUnaryOperator') -> 'FailableLongUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableLongUnaryOperator<E> org.apache.commons.lang3.function.FailableLongUnaryOperator.compose(org.apache.commons.lang3.function.FailableLongUnaryOperator<E>)"""
        return 'FailableLongUnaryOperator'._wrap(super(_FailableLongUnaryOperator, self).compose(arg0))

    @abstractmethod
    def applyAsLong(self, arg0: int):
        """public abstract long org.apache.commons.lang3.function.FailableLongUnaryOperator.applyAsLong(long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBiFunction
import org.apache.commons.lang3.function.FailableBiFunction as _FailableBiFunction
_FailableBiFunction = _FailableBiFunction
from abc import abstractmethod, ABC
 
class FailableBiFunction():
    """org.apache.commons.lang3.function.FailableBiFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableBiFunction) -> 'FailableBiFunction':
        return FailableBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableBiFunction):
        """
        Dynamic initializer for FailableBiFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableBiFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableBiFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'FailableFunction') -> 'FailableBiFunction':
        """public default <V> org.apache.commons.lang3.function.FailableBiFunction<T, U, V, E> org.apache.commons.lang3.function.FailableBiFunction.andThen(org.apache.commons.lang3.function.FailableFunction<? super R, ? extends V, E>)"""
        return 'FailableBiFunction'._wrap(super(_FailableBiFunction, self).andThen(arg0))

    @abstractmethod
    def apply(self, arg0: object, arg1: object):
        """public abstract R org.apache.commons.lang3.function.FailableBiFunction.apply(T,U) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableBiFunction':
        """public static <T,U,R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiFunction<T, U, R, E> org.apache.commons.lang3.function.FailableBiFunction.nop()"""
        return FailableBiFunction._wrap(_FailableBiFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleUnaryOperator
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableDoubleUnaryOperator as _FailableDoubleUnaryOperator
_FailableDoubleUnaryOperator = _FailableDoubleUnaryOperator
 
class FailableDoubleUnaryOperator():
    """org.apache.commons.lang3.function.FailableDoubleUnaryOperator"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoubleUnaryOperator) -> 'FailableDoubleUnaryOperator':
        return FailableDoubleUnaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoubleUnaryOperator):
        """
        Dynamic initializer for FailableDoubleUnaryOperator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoubleUnaryOperator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoubleUnaryOperator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def compose(self, arg0: 'FailableDoubleUnaryOperator') -> 'FailableDoubleUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.compose(org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E>)"""
        return 'FailableDoubleUnaryOperator'._wrap(super(_FailableDoubleUnaryOperator, self).compose(arg0))

    @overload
    def andThen(self, arg0: 'FailableDoubleUnaryOperator') -> 'FailableDoubleUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.andThen(org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E>)"""
        return 'FailableDoubleUnaryOperator'._wrap(super(_FailableDoubleUnaryOperator, self).andThen(arg0))

    @abstractmethod
    def applyAsDouble(self, arg0: float):
        """public abstract double org.apache.commons.lang3.function.FailableDoubleUnaryOperator.applyAsDouble(double) throws E"""
        pass

    @staticmethod
    @overload
    def identity() -> 'FailableDoubleUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.identity()"""
        return FailableDoubleUnaryOperator._wrap(_FailableDoubleUnaryOperator.identity())

    @staticmethod
    @overload
    def nop() -> 'FailableDoubleUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleUnaryOperator<E> org.apache.commons.lang3.function.FailableDoubleUnaryOperator.nop()"""
        return FailableDoubleUnaryOperator._wrap(_FailableDoubleUnaryOperator.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongConsumer
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableLongConsumer as _FailableLongConsumer
_FailableLongConsumer = _FailableLongConsumer
 
class FailableLongConsumer():
    """org.apache.commons.lang3.function.FailableLongConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongConsumer) -> 'FailableLongConsumer':
        return FailableLongConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongConsumer):
        """
        Dynamic initializer for FailableLongConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void org.apache.commons.lang3.function.FailableLongConsumer.accept(long) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableLongConsumer') -> 'FailableLongConsumer':
        """public default org.apache.commons.lang3.function.FailableLongConsumer<E> org.apache.commons.lang3.function.FailableLongConsumer.andThen(org.apache.commons.lang3.function.FailableLongConsumer<E>)"""
        return 'FailableLongConsumer'._wrap(super(_FailableLongConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableLongConsumer':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongConsumer<E> org.apache.commons.lang3.function.FailableLongConsumer.nop()"""
        return FailableLongConsumer._wrap(_FailableLongConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleBinaryOperator
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableDoubleBinaryOperator as _FailableDoubleBinaryOperator
_FailableDoubleBinaryOperator = _FailableDoubleBinaryOperator
 
class FailableDoubleBinaryOperator():
    """org.apache.commons.lang3.function.FailableDoubleBinaryOperator"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoubleBinaryOperator) -> 'FailableDoubleBinaryOperator':
        return FailableDoubleBinaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoubleBinaryOperator):
        """
        Dynamic initializer for FailableDoubleBinaryOperator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoubleBinaryOperator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoubleBinaryOperator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def applyAsDouble(self, arg0: float, arg1: float):
        """public abstract double org.apache.commons.lang3.function.FailableDoubleBinaryOperator.applyAsDouble(double,double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.Failable
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
import java.lang.Double as _double
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.lang3.function.Failable as _Failable
_Failable = _Failable
import java.util.function.Consumer as Consumer
import java.lang.RuntimeException as RuntimeException
import java.util.concurrent.Callable as Callable
from builtins import bool
import org.apache.commons.lang3.stream.Streams as _Streams_FailableStream
_FailableStream = _Streams_FailableStream.FailableStream
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
from builtins import float
import java.util.function.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache.lang3 import stream
except ImportError:
    stream = _import_once("pyapache.lang3.stream")

import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
import java.util.function.BiFunction as BiFunction
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
import java.lang.RuntimeException as _RuntimeException
_RuntimeException = _RuntimeException
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.BiPredicate as BiPredicate
import java.util.function.BiPredicate as _BiPredicate
_BiPredicate = _BiPredicate
import java.lang.Runnable as _Runnable
_Runnable = _Runnable
import java.util.concurrent.Callable as _Callable
_Callable = _Callable
import java.util.stream.Stream as Stream
import java.lang.Throwable as Throwable
import java.util.function.Function as Function
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Failable():
    """org.apache.commons.lang3.function.Failable"""
 
    @staticmethod
    def _wrap(java_value: _Failable) -> 'Failable':
        return Failable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Failable):
        """
        Dynamic initializer for Failable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Failable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Failable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def asPredicate(arg0: 'FailablePredicate') -> 'Predicate':
        """public static <T> java.util.function.Predicate<T> org.apache.commons.lang3.function.Failable.asPredicate(org.apache.commons.lang3.function.FailablePredicate<T, ?>)"""
        return Predicate._wrap(_Failable.asPredicate(arg0))

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', arg1: 'FailableConsumer', *arg2: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.function.Failable.tryWithResources(org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.function.FailableConsumer<java.lang.Throwable, ? extends java.lang.Throwable>,org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>...)"""
        _Failable.tryWithResources(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getAsLong(arg0: 'FailableLongSupplier') -> int:
        """public static <E extends java.lang.Throwable> long org.apache.commons.lang3.function.Failable.getAsLong(org.apache.commons.lang3.function.FailableLongSupplier<E>)"""
        return int._wrap(_Failable.getAsLong(arg0))

    @staticmethod
    @overload
    def asSupplier(arg0: 'FailableSupplier') -> 'Supplier':
        """public static <T> java.util.function.Supplier<T> org.apache.commons.lang3.function.Failable.asSupplier(org.apache.commons.lang3.function.FailableSupplier<T, ?>)"""
        return Supplier._wrap(_Failable.asSupplier(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def test(arg0: 'FailablePredicate', arg1: object) -> bool:
        """public static <T,E extends java.lang.Throwable> boolean org.apache.commons.lang3.function.Failable.test(org.apache.commons.lang3.function.FailablePredicate<T, E>,T)"""
        return bool._wrap(_Failable.test(arg0, arg1))

    @staticmethod
    @overload
    def accept(arg0: 'FailableConsumer', arg1: object):
        """public static <T,E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableConsumer<T, E>,T)"""
        _Failable.accept(arg0, arg1)

    @staticmethod
    @overload
    def asBiFunction(arg0: 'FailableBiFunction') -> 'BiFunction':
        """public static <T,U,R> java.util.function.BiFunction<T, U, R> org.apache.commons.lang3.function.Failable.asBiFunction(org.apache.commons.lang3.function.FailableBiFunction<T, U, R, ?>)"""
        return BiFunction._wrap(_Failable.asBiFunction(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def run(arg0: 'FailableRunnable'):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.run(org.apache.commons.lang3.function.FailableRunnable<E>)"""
        _Failable.run(arg0)

    @staticmethod
    @overload
    def apply(arg0: 'FailableFunction', arg1: object) -> object:
        """public static <T,R,E extends java.lang.Throwable> R org.apache.commons.lang3.function.Failable.apply(org.apache.commons.lang3.function.FailableFunction<T, R, E>,T)"""
        return object._wrap(_Failable.apply(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def test(arg0: 'FailableBiPredicate', arg1: object, arg2: object) -> bool:
        """public static <T,U,E extends java.lang.Throwable> boolean org.apache.commons.lang3.function.Failable.test(org.apache.commons.lang3.function.FailableBiPredicate<T, U, E>,T,U)"""
        return bool._wrap(_Failable.test(arg0, arg1, arg2))

    @staticmethod
    @overload
    def get(arg0: 'FailableSupplier') -> object:
        """public static <T,E extends java.lang.Throwable> T org.apache.commons.lang3.function.Failable.get(org.apache.commons.lang3.function.FailableSupplier<T, E>)"""
        return object._wrap(_Failable.get(arg0))

    @staticmethod
    @overload
    def getAsInt(arg0: 'FailableIntSupplier') -> int:
        """public static <E extends java.lang.Throwable> int org.apache.commons.lang3.function.Failable.getAsInt(org.apache.commons.lang3.function.FailableIntSupplier<E>)"""
        return int._wrap(_Failable.getAsInt(arg0))

    @staticmethod
    @overload
    def getAsBoolean(arg0: 'FailableBooleanSupplier') -> bool:
        """public static <E extends java.lang.Throwable> boolean org.apache.commons.lang3.function.Failable.getAsBoolean(org.apache.commons.lang3.function.FailableBooleanSupplier<E>)"""
        return bool._wrap(_Failable.getAsBoolean(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableLongConsumer', arg1: int):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableLongConsumer<E>,long)"""
        _Failable.accept(arg0, _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Collection') -> 'stream.Streams$FailableStream':
        """public static <E> org.apache.commons.lang3.stream.Streams$FailableStream<E> org.apache.commons.lang3.function.Failable.stream(java.util.Collection<E>)"""
        return stream.Streams$FailableStream._wrap(_Failable.stream(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableBiConsumer', arg1: object, arg2: object):
        """public static <T,U,E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableBiConsumer<T, U, E>,T,U)"""
        _Failable.accept(arg0, arg1, arg2)

    @staticmethod
    @overload
    def asBiConsumer(arg0: 'FailableBiConsumer') -> 'BiConsumer':
        """public static <T,U> java.util.function.BiConsumer<T, U> org.apache.commons.lang3.function.Failable.asBiConsumer(org.apache.commons.lang3.function.FailableBiConsumer<T, U, ?>)"""
        return BiConsumer._wrap(_Failable.asBiConsumer(arg0))

    @staticmethod
    @overload
    def call(arg0: 'FailableCallable') -> object:
        """public static <V,E extends java.lang.Throwable> V org.apache.commons.lang3.function.Failable.call(org.apache.commons.lang3.function.FailableCallable<V, E>)"""
        return object._wrap(_Failable.call(arg0))

    @staticmethod
    @overload
    def asRunnable(arg0: 'FailableRunnable') -> 'Runnable':
        """public static java.lang.Runnable org.apache.commons.lang3.function.Failable.asRunnable(org.apache.commons.lang3.function.FailableRunnable<?>)"""
        return Runnable._wrap(_Failable.asRunnable(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def asConsumer(arg0: 'FailableConsumer') -> 'Consumer':
        """public static <T> java.util.function.Consumer<T> org.apache.commons.lang3.function.Failable.asConsumer(org.apache.commons.lang3.function.FailableConsumer<T, ?>)"""
        return Consumer._wrap(_Failable.asConsumer(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableIntConsumer', arg1: int):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableIntConsumer<E>,int)"""
        _Failable.accept(arg0, _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', *arg1: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.function.Failable.tryWithResources(org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.function.FailableRunnable<? extends java.lang.Throwable>...)"""
        _Failable.tryWithResources(arg0, arg1)

    @staticmethod
    @overload
    def getAsDouble(arg0: 'FailableDoubleSupplier') -> float:
        """public static <E extends java.lang.Throwable> double org.apache.commons.lang3.function.Failable.getAsDouble(org.apache.commons.lang3.function.FailableDoubleSupplier<E>)"""
        return float._wrap(_Failable.getAsDouble(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Stream') -> 'stream.Streams$FailableStream':
        """public static <T> org.apache.commons.lang3.stream.Streams$FailableStream<T> org.apache.commons.lang3.function.Failable.stream(java.util.stream.Stream<T>)"""
        return stream.Streams$FailableStream._wrap(_Failable.stream(arg0))

    @staticmethod
    @overload
    def rethrow(arg0: 'Throwable') -> 'RuntimeException':
        """public static java.lang.RuntimeException org.apache.commons.lang3.function.Failable.rethrow(java.lang.Throwable)"""
        return RuntimeException._wrap(_Failable.rethrow(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def apply(arg0: 'FailableBiFunction', arg1: object, arg2: object) -> object:
        """public static <T,U,R,E extends java.lang.Throwable> R org.apache.commons.lang3.function.Failable.apply(org.apache.commons.lang3.function.FailableBiFunction<T, U, R, E>,T,U)"""
        return object._wrap(_Failable.apply(arg0, arg1, arg2))

    @staticmethod
    @overload
    def applyAsDouble(arg0: 'FailableDoubleBinaryOperator', arg1: float, arg2: float) -> float:
        """public static <E extends java.lang.Throwable> double org.apache.commons.lang3.function.Failable.applyAsDouble(org.apache.commons.lang3.function.FailableDoubleBinaryOperator<E>,double,double)"""
        return float._wrap(_Failable.applyAsDouble(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def asCallable(arg0: 'FailableCallable') -> 'Callable':
        """public static <V> java.util.concurrent.Callable<V> org.apache.commons.lang3.function.Failable.asCallable(org.apache.commons.lang3.function.FailableCallable<V, ?>)"""
        return Callable._wrap(_Failable.asCallable(arg0))

    @staticmethod
    @overload
    def asBiPredicate(arg0: 'FailableBiPredicate') -> 'BiPredicate':
        """public static <T,U> java.util.function.BiPredicate<T, U> org.apache.commons.lang3.function.Failable.asBiPredicate(org.apache.commons.lang3.function.FailableBiPredicate<T, U, ?>)"""
        return BiPredicate._wrap(_Failable.asBiPredicate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getAsShort(arg0: 'FailableShortSupplier') -> int:
        """public static <E extends java.lang.Throwable> short org.apache.commons.lang3.function.Failable.getAsShort(org.apache.commons.lang3.function.FailableShortSupplier<E>)"""
        return int._wrap(_Failable.getAsShort(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableDoubleConsumer', arg1: float):
        """public static <E extends java.lang.Throwable> void org.apache.commons.lang3.function.Failable.accept(org.apache.commons.lang3.function.FailableDoubleConsumer<E>,double)"""
        _Failable.accept(arg0, _double.valueOf(arg1))

    @staticmethod
    @overload
    def asFunction(arg0: 'FailableFunction') -> 'Function':
        """public static <T,R> java.util.function.Function<T, R> org.apache.commons.lang3.function.Failable.asFunction(org.apache.commons.lang3.function.FailableFunction<T, R, ?>)"""
        return Function._wrap(_Failable.asFunction(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.function.Consumers
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.function.Consumers as _Consumers
_Consumers = _Consumers
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Consumers():
    """org.apache.commons.lang3.function.Consumers"""
 
    @staticmethod
    def _wrap(java_value: _Consumers) -> 'Consumers':
        return Consumers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Consumers):
        """
        Dynamic initializer for Consumers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Consumers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Consumers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nop() -> 'Consumer':
        """public static <T> java.util.function.Consumer<T> org.apache.commons.lang3.function.Consumers.nop()"""
        return Consumer._wrap(_Consumers.nop())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongFunction
import org.apache.commons.lang3.function.FailableLongFunction as _FailableLongFunction
_FailableLongFunction = _FailableLongFunction
from abc import abstractmethod, ABC
 
class FailableLongFunction():
    """org.apache.commons.lang3.function.FailableLongFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongFunction) -> 'FailableLongFunction':
        return FailableLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongFunction):
        """
        Dynamic initializer for FailableLongFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableLongFunction':
        """public static <R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongFunction<R, E> org.apache.commons.lang3.function.FailableLongFunction.nop()"""
        return FailableLongFunction._wrap(_FailableLongFunction.nop())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract R org.apache.commons.lang3.function.FailableLongFunction.apply(long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToLongBiFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableToLongBiFunction as _FailableToLongBiFunction
_FailableToLongBiFunction = _FailableToLongBiFunction
 
class FailableToLongBiFunction():
    """org.apache.commons.lang3.function.FailableToLongBiFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableToLongBiFunction) -> 'FailableToLongBiFunction':
        return FailableToLongBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableToLongBiFunction):
        """
        Dynamic initializer for FailableToLongBiFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableToLongBiFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableToLongBiFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableToLongBiFunction':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToLongBiFunction<T, U, E> org.apache.commons.lang3.function.FailableToLongBiFunction.nop()"""
        return FailableToLongBiFunction._wrap(_FailableToLongBiFunction.nop())

    @abstractmethod
    def applyAsLong(self, arg0: object, arg1: object):
        """public abstract long org.apache.commons.lang3.function.FailableToLongBiFunction.applyAsLong(T,U) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.IntToCharFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.IntToCharFunction as _IntToCharFunction
_IntToCharFunction = _IntToCharFunction
 
class IntToCharFunction():
    """org.apache.commons.lang3.function.IntToCharFunction"""
 
    @staticmethod
    def _wrap(java_value: _IntToCharFunction) -> 'IntToCharFunction':
        return IntToCharFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntToCharFunction):
        """
        Dynamic initializer for IntToCharFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntToCharFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntToCharFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def applyAsChar(self, arg0: int):
        """public abstract char org.apache.commons.lang3.function.IntToCharFunction.applyAsChar(int)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleFunction
import org.apache.commons.lang3.function.FailableDoubleFunction as _FailableDoubleFunction
_FailableDoubleFunction = _FailableDoubleFunction
from abc import abstractmethod, ABC
 
class FailableDoubleFunction():
    """org.apache.commons.lang3.function.FailableDoubleFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoubleFunction) -> 'FailableDoubleFunction':
        return FailableDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoubleFunction):
        """
        Dynamic initializer for FailableDoubleFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoubleFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoubleFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableDoubleFunction':
        """public static <R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleFunction<R, E> org.apache.commons.lang3.function.FailableDoubleFunction.nop()"""
        return FailableDoubleFunction._wrap(_FailableDoubleFunction.nop())

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract R org.apache.commons.lang3.function.FailableDoubleFunction.apply(double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.Suppliers
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.function.Suppliers as _Suppliers
_Suppliers = _Suppliers
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Suppliers():
    """org.apache.commons.lang3.function.Suppliers"""
 
    @staticmethod
    def _wrap(java_value: _Suppliers) -> 'Suppliers':
        return Suppliers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Suppliers):
        """
        Dynamic initializer for Suppliers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Suppliers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Suppliers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public org.apache.commons.lang3.function.Suppliers()"""
        val = _Suppliers()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.function.Suppliers()"""
        val = _Suppliers()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def get(arg0: 'Supplier') -> object:
        """public static <T> T org.apache.commons.lang3.function.Suppliers.get(java.util.function.Supplier<T>)"""
        return object._wrap(_Suppliers.get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableRunnable
import org.apache.commons.lang3.function.FailableRunnable as _FailableRunnable
_FailableRunnable = _FailableRunnable
from abc import abstractmethod, ABC
 
class FailableRunnable():
    """org.apache.commons.lang3.function.FailableRunnable"""
 
    @staticmethod
    def _wrap(java_value: _FailableRunnable) -> 'FailableRunnable':
        return FailableRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableRunnable):
        """
        Dynamic initializer for FailableRunnable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableRunnable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableRunnable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def run(self, ):
        """public abstract void org.apache.commons.lang3.function.FailableRunnable.run() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableConsumer
import org.apache.commons.lang3.function.FailableConsumer as _FailableConsumer
_FailableConsumer = _FailableConsumer
from abc import abstractmethod, ABC
 
class FailableConsumer():
    """org.apache.commons.lang3.function.FailableConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableConsumer) -> 'FailableConsumer':
        return FailableConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableConsumer):
        """
        Dynamic initializer for FailableConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableConsumer':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableConsumer<T, E> org.apache.commons.lang3.function.FailableConsumer.nop()"""
        return FailableConsumer._wrap(_FailableConsumer.nop())

    @abstractmethod
    def accept(self, arg0: object):
        """public abstract void org.apache.commons.lang3.function.FailableConsumer.accept(T) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableConsumer') -> 'FailableConsumer':
        """public default org.apache.commons.lang3.function.FailableConsumer<T, E> org.apache.commons.lang3.function.FailableConsumer.andThen(org.apache.commons.lang3.function.FailableConsumer<? super T, E>)"""
        return 'FailableConsumer'._wrap(super(_FailableConsumer, self).andThen(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToIntBiFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableToIntBiFunction as _FailableToIntBiFunction
_FailableToIntBiFunction = _FailableToIntBiFunction
 
class FailableToIntBiFunction():
    """org.apache.commons.lang3.function.FailableToIntBiFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableToIntBiFunction) -> 'FailableToIntBiFunction':
        return FailableToIntBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableToIntBiFunction):
        """
        Dynamic initializer for FailableToIntBiFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableToIntBiFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableToIntBiFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def applyAsInt(self, arg0: object, arg1: object):
        """public abstract int org.apache.commons.lang3.function.FailableToIntBiFunction.applyAsInt(T,U) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableToIntBiFunction':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToIntBiFunction<T, U, E> org.apache.commons.lang3.function.FailableToIntBiFunction.nop()"""
        return FailableToIntBiFunction._wrap(_FailableToIntBiFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongPredicate
import org.apache.commons.lang3.function.FailableLongPredicate as _FailableLongPredicate
_FailableLongPredicate = _FailableLongPredicate
from abc import abstractmethod, ABC
 
class FailableLongPredicate():
    """org.apache.commons.lang3.function.FailableLongPredicate"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongPredicate) -> 'FailableLongPredicate':
        return FailableLongPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongPredicate):
        """
        Dynamic initializer for FailableLongPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def test(self, arg0: int):
        """public abstract boolean org.apache.commons.lang3.function.FailableLongPredicate.test(long) throws E"""
        pass

    @overload
    def negate(self) -> 'FailableLongPredicate':
        """public default org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.negate()"""
        return 'FailableLongPredicate'._wrap(super(FailableLongPredicate, self).negate())

    @staticmethod
    @overload
    def falsePredicate() -> 'FailableLongPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.falsePredicate()"""
        return FailableLongPredicate._wrap(_FailableLongPredicate.falsePredicate())

    @staticmethod
    @overload
    def truePredicate() -> 'FailableLongPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.truePredicate()"""
        return FailableLongPredicate._wrap(_FailableLongPredicate.truePredicate())

    @overload
    def and(self, arg0: 'FailableLongPredicate') -> 'FailableLongPredicate':
        """public default org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.and(org.apache.commons.lang3.function.FailableLongPredicate<E>)"""
        return 'FailableLongPredicate'._wrap(super(_FailableLongPredicate, self).and(arg0))

    @overload
    def or(self, arg0: 'FailableLongPredicate') -> 'FailableLongPredicate':
        """public default org.apache.commons.lang3.function.FailableLongPredicate<E> org.apache.commons.lang3.function.FailableLongPredicate.or(org.apache.commons.lang3.function.FailableLongPredicate<E>)"""
        return 'FailableLongPredicate'._wrap(super(_FailableLongPredicate, self).or(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToDoubleBiFunction
import org.apache.commons.lang3.function.FailableToDoubleBiFunction as _FailableToDoubleBiFunction
_FailableToDoubleBiFunction = _FailableToDoubleBiFunction
from abc import abstractmethod, ABC
 
class FailableToDoubleBiFunction():
    """org.apache.commons.lang3.function.FailableToDoubleBiFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableToDoubleBiFunction) -> 'FailableToDoubleBiFunction':
        return FailableToDoubleBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableToDoubleBiFunction):
        """
        Dynamic initializer for FailableToDoubleBiFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableToDoubleBiFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableToDoubleBiFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        return FailableToDoubleBiFunction._wrap(_FailableToDoubleBiFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongBinaryOperator
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableLongBinaryOperator as _FailableLongBinaryOperator
_FailableLongBinaryOperator = _FailableLongBinaryOperator
 
class FailableLongBinaryOperator():
    """org.apache.commons.lang3.function.FailableLongBinaryOperator"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongBinaryOperator) -> 'FailableLongBinaryOperator':
        return FailableLongBinaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongBinaryOperator):
        """
        Dynamic initializer for FailableLongBinaryOperator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongBinaryOperator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongBinaryOperator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def applyAsLong(self, arg0: int, arg1: int):
        """public abstract long org.apache.commons.lang3.function.FailableLongBinaryOperator.applyAsLong(long,long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntSupplier
import org.apache.commons.lang3.function.FailableIntSupplier as _FailableIntSupplier
_FailableIntSupplier = _FailableIntSupplier
from abc import abstractmethod, ABC
 
class FailableIntSupplier():
    """org.apache.commons.lang3.function.FailableIntSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntSupplier) -> 'FailableIntSupplier':
        return FailableIntSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntSupplier):
        """
        Dynamic initializer for FailableIntSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getAsInt(self, ):
        """public abstract int org.apache.commons.lang3.function.FailableIntSupplier.getAsInt() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableSupplier
import org.apache.commons.lang3.function.FailableSupplier as _FailableSupplier
_FailableSupplier = _FailableSupplier
from abc import abstractmethod, ABC
 
class FailableSupplier():
    """org.apache.commons.lang3.function.FailableSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FailableSupplier) -> 'FailableSupplier':
        return FailableSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableSupplier):
        """
        Dynamic initializer for FailableSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract R org.apache.commons.lang3.function.FailableSupplier.get() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleToIntFunction
import org.apache.commons.lang3.function.FailableDoubleToIntFunction as _FailableDoubleToIntFunction
_FailableDoubleToIntFunction = _FailableDoubleToIntFunction
from abc import abstractmethod, ABC
 
class FailableDoubleToIntFunction():
    """org.apache.commons.lang3.function.FailableDoubleToIntFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoubleToIntFunction) -> 'FailableDoubleToIntFunction':
        return FailableDoubleToIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoubleToIntFunction):
        """
        Dynamic initializer for FailableDoubleToIntFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoubleToIntFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoubleToIntFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        return FailableDoubleToIntFunction._wrap(_FailableDoubleToIntFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoublePredicate
import org.apache.commons.lang3.function.FailableDoublePredicate as _FailableDoublePredicate
_FailableDoublePredicate = _FailableDoublePredicate
from abc import abstractmethod, ABC
 
class FailableDoublePredicate():
    """org.apache.commons.lang3.function.FailableDoublePredicate"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoublePredicate) -> 'FailableDoublePredicate':
        return FailableDoublePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoublePredicate):
        """
        Dynamic initializer for FailableDoublePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoublePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoublePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def truePredicate() -> 'FailableDoublePredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.truePredicate()"""
        return FailableDoublePredicate._wrap(_FailableDoublePredicate.truePredicate())

    @overload
    def and(self, arg0: 'FailableDoublePredicate') -> 'FailableDoublePredicate':
        """public default org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.and(org.apache.commons.lang3.function.FailableDoublePredicate<E>)"""
        return 'FailableDoublePredicate'._wrap(super(_FailableDoublePredicate, self).and(arg0))

    @overload
    def or(self, arg0: 'FailableDoublePredicate') -> 'FailableDoublePredicate':
        """public default org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.or(org.apache.commons.lang3.function.FailableDoublePredicate<E>)"""
        return 'FailableDoublePredicate'._wrap(super(_FailableDoublePredicate, self).or(arg0))

    @staticmethod
    @overload
    def falsePredicate() -> 'FailableDoublePredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.falsePredicate()"""
        return FailableDoublePredicate._wrap(_FailableDoublePredicate.falsePredicate())

    @abstractmethod
    def test(self, arg0: float):
        """public abstract boolean org.apache.commons.lang3.function.FailableDoublePredicate.test(double) throws E"""
        pass

    @overload
    def negate(self) -> 'FailableDoublePredicate':
        """public default org.apache.commons.lang3.function.FailableDoublePredicate<E> org.apache.commons.lang3.function.FailableDoublePredicate.negate()"""
        return 'FailableDoublePredicate'._wrap(super(FailableDoublePredicate, self).negate()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBiPredicate
import org.apache.commons.lang3.function.FailableBiPredicate as _FailableBiPredicate
_FailableBiPredicate = _FailableBiPredicate
from abc import abstractmethod, ABC
 
class FailableBiPredicate():
    """org.apache.commons.lang3.function.FailableBiPredicate"""
 
    @staticmethod
    def _wrap(java_value: _FailableBiPredicate) -> 'FailableBiPredicate':
        return FailableBiPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableBiPredicate):
        """
        Dynamic initializer for FailableBiPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableBiPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableBiPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def negate(self) -> 'FailableBiPredicate':
        """public default org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.negate()"""
        return 'FailableBiPredicate'._wrap(super(FailableBiPredicate, self).negate())

    @overload
    def or(self, arg0: 'FailableBiPredicate') -> 'FailableBiPredicate':
        """public default org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.or(org.apache.commons.lang3.function.FailableBiPredicate<? super T, ? super U, E>)"""
        return 'FailableBiPredicate'._wrap(super(_FailableBiPredicate, self).or(arg0))

    @abstractmethod
    def test(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.lang3.function.FailableBiPredicate.test(T,U) throws E"""
        pass

    @staticmethod
    @overload
    def falsePredicate() -> 'FailableBiPredicate':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.falsePredicate()"""
        return FailableBiPredicate._wrap(_FailableBiPredicate.falsePredicate())

    @overload
    def and(self, arg0: 'FailableBiPredicate') -> 'FailableBiPredicate':
        """public default org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.and(org.apache.commons.lang3.function.FailableBiPredicate<? super T, ? super U, E>)"""
        return 'FailableBiPredicate'._wrap(super(_FailableBiPredicate, self).and(arg0))

    @staticmethod
    @overload
    def truePredicate() -> 'FailableBiPredicate':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiPredicate<T, U, E> org.apache.commons.lang3.function.FailableBiPredicate.truePredicate()"""
        return FailableBiPredicate._wrap(_FailableBiPredicate.truePredicate()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToDoubleFunction
import org.apache.commons.lang3.function.FailableToDoubleFunction as _FailableToDoubleFunction
_FailableToDoubleFunction = _FailableToDoubleFunction
from abc import abstractmethod, ABC
 
class FailableToDoubleFunction():
    """org.apache.commons.lang3.function.FailableToDoubleFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableToDoubleFunction) -> 'FailableToDoubleFunction':
        return FailableToDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableToDoubleFunction):
        """
        Dynamic initializer for FailableToDoubleFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableToDoubleFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableToDoubleFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableToDoubleFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToDoubleFunction<T, E> org.apache.commons.lang3.function.FailableToDoubleFunction.nop()"""
        return FailableToDoubleFunction._wrap(_FailableToDoubleFunction.nop())

    @abstractmethod
    def applyAsDouble(self, arg0: object):
        """public abstract double org.apache.commons.lang3.function.FailableToDoubleFunction.applyAsDouble(T) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongSupplier
import org.apache.commons.lang3.function.FailableLongSupplier as _FailableLongSupplier
_FailableLongSupplier = _FailableLongSupplier
from abc import abstractmethod, ABC
 
class FailableLongSupplier():
    """org.apache.commons.lang3.function.FailableLongSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongSupplier) -> 'FailableLongSupplier':
        return FailableLongSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongSupplier):
        """
        Dynamic initializer for FailableLongSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getAsLong(self, ):
        """public abstract long org.apache.commons.lang3.function.FailableLongSupplier.getAsLong() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleConsumer
import org.apache.commons.lang3.function.FailableDoubleConsumer as _FailableDoubleConsumer
_FailableDoubleConsumer = _FailableDoubleConsumer
from abc import abstractmethod, ABC
 
class FailableDoubleConsumer():
    """org.apache.commons.lang3.function.FailableDoubleConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoubleConsumer) -> 'FailableDoubleConsumer':
        return FailableDoubleConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoubleConsumer):
        """
        Dynamic initializer for FailableDoubleConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoubleConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoubleConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'FailableDoubleConsumer') -> 'FailableDoubleConsumer':
        """public default org.apache.commons.lang3.function.FailableDoubleConsumer<E> org.apache.commons.lang3.function.FailableDoubleConsumer.andThen(org.apache.commons.lang3.function.FailableDoubleConsumer<E>)"""
        return 'FailableDoubleConsumer'._wrap(super(_FailableDoubleConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableDoubleConsumer':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableDoubleConsumer<E> org.apache.commons.lang3.function.FailableDoubleConsumer.nop()"""
        return FailableDoubleConsumer._wrap(_FailableDoubleConsumer.nop())

    @abstractmethod
    def accept(self, arg0: float):
        """public abstract void org.apache.commons.lang3.function.FailableDoubleConsumer.accept(double) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.MethodInvokers
import java.util.function.Supplier as Supplier
import java.util.function.Function as _Function
_Function = _Function
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.lang3.function.FailableBiConsumer as _FailableBiConsumer
_FailableBiConsumer = _FailableBiConsumer
from builtins import type
import org.apache.commons.lang3.function.MethodInvokers as _MethodInvokers
_MethodInvokers = _MethodInvokers
import org.apache.commons.lang3.function.FailableFunction as _FailableFunction
_FailableFunction = _FailableFunction
from builtins import bool
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
import org.apache.commons.lang3.function.FailableBiFunction as _FailableBiFunction
_FailableBiFunction = _FailableBiFunction
import org.apache.commons.lang3.function.FailableSupplier as _FailableSupplier
_FailableSupplier = _FailableSupplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.function.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.util.function.Function as Function
import java.lang.Long as _long
import java.lang.reflect.Method as Method
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MethodInvokers():
    """org.apache.commons.lang3.function.MethodInvokers"""
 
    @staticmethod
    def _wrap(java_value: _MethodInvokers) -> 'MethodInvokers':
        return MethodInvokers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MethodInvokers):
        """
        Dynamic initializer for MethodInvokers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MethodInvokers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MethodInvokers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def asFailableBiConsumer(arg0: 'Method') -> 'FailableBiConsumer':
        """public static <T,U> org.apache.commons.lang3.function.FailableBiConsumer<T, U, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableBiConsumer(java.lang.reflect.Method)"""
        return FailableBiConsumer._wrap(_MethodInvokers.asFailableBiConsumer(arg0))

    @staticmethod
    @overload
    def asFailableBiFunction(arg0: 'Method') -> 'FailableBiFunction':
        """public static <T,U,R> org.apache.commons.lang3.function.FailableBiFunction<T, U, R, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableBiFunction(java.lang.reflect.Method)"""
        return FailableBiFunction._wrap(_MethodInvokers.asFailableBiFunction(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def asFunction(arg0: 'Method') -> 'Function':
        """public static <T,R> java.util.function.Function<T, R> org.apache.commons.lang3.function.MethodInvokers.asFunction(java.lang.reflect.Method)"""
        return Function._wrap(_MethodInvokers.asFunction(arg0))

    @staticmethod
    @overload
    def asBiFunction(arg0: 'Method') -> 'BiFunction':
        """public static <T,U,R> java.util.function.BiFunction<T, U, R> org.apache.commons.lang3.function.MethodInvokers.asBiFunction(java.lang.reflect.Method)"""
        return BiFunction._wrap(_MethodInvokers.asBiFunction(arg0))

    @staticmethod
    @overload
    def asInterfaceInstance(arg0: 'Class', arg1: 'Method') -> object:
        """public static <T> T org.apache.commons.lang3.function.MethodInvokers.asInterfaceInstance(java.lang.Class<T>,java.lang.reflect.Method)"""
        return object._wrap(_MethodInvokers.asInterfaceInstance(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def asFailableSupplier(arg0: 'Method') -> 'FailableSupplier':
        """public static <R> org.apache.commons.lang3.function.FailableSupplier<R, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableSupplier(java.lang.reflect.Method)"""
        return FailableSupplier._wrap(_MethodInvokers.asFailableSupplier(arg0))

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
    def asFailableFunction(arg0: 'Method') -> 'FailableFunction':
        """public static <T,R> org.apache.commons.lang3.function.FailableFunction<T, R, java.lang.Throwable> org.apache.commons.lang3.function.MethodInvokers.asFailableFunction(java.lang.reflect.Method)"""
        return FailableFunction._wrap(_MethodInvokers.asFailableFunction(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def asBiConsumer(arg0: 'Method') -> 'BiConsumer':
        """public static <T,U> java.util.function.BiConsumer<T, U> org.apache.commons.lang3.function.MethodInvokers.asBiConsumer(java.lang.reflect.Method)"""
        return BiConsumer._wrap(_MethodInvokers.asBiConsumer(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def asSupplier(arg0: 'Method') -> 'Supplier':
        """public static <R> java.util.function.Supplier<R> org.apache.commons.lang3.function.MethodInvokers.asSupplier(java.lang.reflect.Method)"""
        return Supplier._wrap(_MethodInvokers.asSupplier(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.function.TriFunction
import org.apache.commons.lang3.function.TriFunction as _TriFunction
_TriFunction = _TriFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class TriFunction():
    """org.apache.commons.lang3.function.TriFunction"""
 
    @staticmethod
    def _wrap(java_value: _TriFunction) -> 'TriFunction':
        return TriFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriFunction):
        """
        Dynamic initializer for TriFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'Function') -> 'TriFunction':
        """public default <W> org.apache.commons.lang3.function.TriFunction<T, U, V, W> org.apache.commons.lang3.function.TriFunction.andThen(java.util.function.Function<? super R, ? extends W>)"""
        return 'TriFunction'._wrap(super(_TriFunction, self).andThen(arg0))

    @abstractmethod
    def apply(self, arg0: object, arg1: object, arg2: object):
        """public abstract R org.apache.commons.lang3.function.TriFunction.apply(T,U,V)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableObjDoubleConsumer
import org.apache.commons.lang3.function.FailableObjDoubleConsumer as _FailableObjDoubleConsumer
_FailableObjDoubleConsumer = _FailableObjDoubleConsumer
from abc import abstractmethod, ABC
 
class FailableObjDoubleConsumer():
    """org.apache.commons.lang3.function.FailableObjDoubleConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableObjDoubleConsumer) -> 'FailableObjDoubleConsumer':
        return FailableObjDoubleConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableObjDoubleConsumer):
        """
        Dynamic initializer for FailableObjDoubleConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableObjDoubleConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableObjDoubleConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: object, arg1: float):
        """public abstract void org.apache.commons.lang3.function.FailableObjDoubleConsumer.accept(T,double) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableObjDoubleConsumer':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableObjDoubleConsumer<T, E> org.apache.commons.lang3.function.FailableObjDoubleConsumer.nop()"""
        return FailableObjDoubleConsumer._wrap(_FailableObjDoubleConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongToIntFunction
import org.apache.commons.lang3.function.FailableLongToIntFunction as _FailableLongToIntFunction
_FailableLongToIntFunction = _FailableLongToIntFunction
from abc import abstractmethod, ABC
 
class FailableLongToIntFunction():
    """org.apache.commons.lang3.function.FailableLongToIntFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongToIntFunction) -> 'FailableLongToIntFunction':
        return FailableLongToIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongToIntFunction):
        """
        Dynamic initializer for FailableLongToIntFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongToIntFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongToIntFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def applyAsInt(self, arg0: int):
        """public abstract int org.apache.commons.lang3.function.FailableLongToIntFunction.applyAsInt(long) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableLongToIntFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongToIntFunction<E> org.apache.commons.lang3.function.FailableLongToIntFunction.nop()"""
        return FailableLongToIntFunction._wrap(_FailableLongToIntFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleToLongFunction
import org.apache.commons.lang3.function.FailableDoubleToLongFunction as _FailableDoubleToLongFunction
_FailableDoubleToLongFunction = _FailableDoubleToLongFunction
from abc import abstractmethod, ABC
 
class FailableDoubleToLongFunction():
    """org.apache.commons.lang3.function.FailableDoubleToLongFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoubleToLongFunction) -> 'FailableDoubleToLongFunction':
        return FailableDoubleToLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoubleToLongFunction):
        """
        Dynamic initializer for FailableDoubleToLongFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoubleToLongFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoubleToLongFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        return FailableDoubleToLongFunction._wrap(_FailableDoubleToLongFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBiConsumer
import org.apache.commons.lang3.function.FailableBiConsumer as _FailableBiConsumer
_FailableBiConsumer = _FailableBiConsumer
from abc import abstractmethod, ABC
 
class FailableBiConsumer():
    """org.apache.commons.lang3.function.FailableBiConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableBiConsumer) -> 'FailableBiConsumer':
        return FailableBiConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableBiConsumer):
        """
        Dynamic initializer for FailableBiConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableBiConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableBiConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'FailableBiConsumer') -> 'FailableBiConsumer':
        """public default org.apache.commons.lang3.function.FailableBiConsumer<T, U, E> org.apache.commons.lang3.function.FailableBiConsumer.andThen(org.apache.commons.lang3.function.FailableBiConsumer<? super T, ? super U, E>)"""
        return 'FailableBiConsumer'._wrap(super(_FailableBiConsumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: object, arg1: object):
        """public abstract void org.apache.commons.lang3.function.FailableBiConsumer.accept(T,U) throws E"""
        pass

    @staticmethod
    @overload
    def nop() -> 'FailableBiConsumer':
        """public static <T,U,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableBiConsumer<T, U, E> org.apache.commons.lang3.function.FailableBiConsumer.nop()"""
        return FailableBiConsumer._wrap(_FailableBiConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.ToBooleanBiFunction
import org.apache.commons.lang3.function.ToBooleanBiFunction as _ToBooleanBiFunction
_ToBooleanBiFunction = _ToBooleanBiFunction
from abc import abstractmethod, ABC
 
class ToBooleanBiFunction():
    """org.apache.commons.lang3.function.ToBooleanBiFunction"""
 
    @staticmethod
    def _wrap(java_value: _ToBooleanBiFunction) -> 'ToBooleanBiFunction':
        return ToBooleanBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToBooleanBiFunction):
        """
        Dynamic initializer for ToBooleanBiFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToBooleanBiFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToBooleanBiFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def applyAsBoolean(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.lang3.function.ToBooleanBiFunction.applyAsBoolean(T,U)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntToDoubleFunction
import org.apache.commons.lang3.function.FailableIntToDoubleFunction as _FailableIntToDoubleFunction
_FailableIntToDoubleFunction = _FailableIntToDoubleFunction
from abc import abstractmethod, ABC
 
class FailableIntToDoubleFunction():
    """org.apache.commons.lang3.function.FailableIntToDoubleFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntToDoubleFunction) -> 'FailableIntToDoubleFunction':
        return FailableIntToDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntToDoubleFunction):
        """
        Dynamic initializer for FailableIntToDoubleFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntToDoubleFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntToDoubleFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        return FailableIntToDoubleFunction._wrap(_FailableIntToDoubleFunction.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableObjLongConsumer
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableObjLongConsumer as _FailableObjLongConsumer
_FailableObjLongConsumer = _FailableObjLongConsumer
 
class FailableObjLongConsumer():
    """org.apache.commons.lang3.function.FailableObjLongConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableObjLongConsumer) -> 'FailableObjLongConsumer':
        return FailableObjLongConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableObjLongConsumer):
        """
        Dynamic initializer for FailableObjLongConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableObjLongConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableObjLongConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        return FailableObjLongConsumer._wrap(_FailableObjLongConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableDoubleSupplier
import org.apache.commons.lang3.function.FailableDoubleSupplier as _FailableDoubleSupplier
_FailableDoubleSupplier = _FailableDoubleSupplier
from abc import abstractmethod, ABC
 
class FailableDoubleSupplier():
    """org.apache.commons.lang3.function.FailableDoubleSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FailableDoubleSupplier) -> 'FailableDoubleSupplier':
        return FailableDoubleSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableDoubleSupplier):
        """
        Dynamic initializer for FailableDoubleSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableDoubleSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableDoubleSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getAsDouble(self, ):
        """public abstract double org.apache.commons.lang3.function.FailableDoubleSupplier.getAsDouble() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableFunction
import org.apache.commons.lang3.function.FailableFunction as _FailableFunction
_FailableFunction = _FailableFunction
from abc import abstractmethod, ABC
 
class FailableFunction():
    """org.apache.commons.lang3.function.FailableFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableFunction) -> 'FailableFunction':
        return FailableFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableFunction):
        """
        Dynamic initializer for FailableFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def compose(self, arg0: 'FailableFunction') -> 'FailableFunction':
        """public default <V> org.apache.commons.lang3.function.FailableFunction<V, R, E> org.apache.commons.lang3.function.FailableFunction.compose(org.apache.commons.lang3.function.FailableFunction<? super V, ? extends T, E>)"""
        return 'FailableFunction'._wrap(super(_FailableFunction, self).compose(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableFunction':
        """public static <T,R,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableFunction<T, R, E> org.apache.commons.lang3.function.FailableFunction.nop()"""
        return FailableFunction._wrap(_FailableFunction.nop())

    @abstractmethod
    def apply(self, arg0: object):
        """public abstract R org.apache.commons.lang3.function.FailableFunction.apply(T) throws E"""
        pass

    @staticmethod
    @overload
    def identity() -> 'FailableFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableFunction<T, T, E> org.apache.commons.lang3.function.FailableFunction.identity()"""
        return FailableFunction._wrap(_FailableFunction.identity())

    @overload
    def andThen(self, arg0: 'FailableFunction') -> 'FailableFunction':
        """public default <V> org.apache.commons.lang3.function.FailableFunction<T, V, E> org.apache.commons.lang3.function.FailableFunction.andThen(org.apache.commons.lang3.function.FailableFunction<? super R, ? extends V, E>)"""
        return 'FailableFunction'._wrap(super(_FailableFunction, self).andThen(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntBinaryOperator
import org.apache.commons.lang3.function.FailableIntBinaryOperator as _FailableIntBinaryOperator
_FailableIntBinaryOperator = _FailableIntBinaryOperator
from abc import abstractmethod, ABC
 
class FailableIntBinaryOperator():
    """org.apache.commons.lang3.function.FailableIntBinaryOperator"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntBinaryOperator) -> 'FailableIntBinaryOperator':
        return FailableIntBinaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntBinaryOperator):
        """
        Dynamic initializer for FailableIntBinaryOperator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntBinaryOperator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntBinaryOperator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def applyAsInt(self, arg0: int, arg1: int):
        """public abstract int org.apache.commons.lang3.function.FailableIntBinaryOperator.applyAsInt(int,int) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableBooleanSupplier
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableBooleanSupplier as _FailableBooleanSupplier
_FailableBooleanSupplier = _FailableBooleanSupplier
 
class FailableBooleanSupplier():
    """org.apache.commons.lang3.function.FailableBooleanSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FailableBooleanSupplier) -> 'FailableBooleanSupplier':
        return FailableBooleanSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableBooleanSupplier):
        """
        Dynamic initializer for FailableBooleanSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableBooleanSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableBooleanSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getAsBoolean(self, ):
        """public abstract boolean org.apache.commons.lang3.function.FailableBooleanSupplier.getAsBoolean() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableObjIntConsumer
import org.apache.commons.lang3.function.FailableObjIntConsumer as _FailableObjIntConsumer
_FailableObjIntConsumer = _FailableObjIntConsumer
from abc import abstractmethod, ABC
 
class FailableObjIntConsumer():
    """org.apache.commons.lang3.function.FailableObjIntConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableObjIntConsumer) -> 'FailableObjIntConsumer':
        return FailableObjIntConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableObjIntConsumer):
        """
        Dynamic initializer for FailableObjIntConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableObjIntConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableObjIntConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        return FailableObjIntConsumer._wrap(_FailableObjIntConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableCallable
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableCallable as _FailableCallable
_FailableCallable = _FailableCallable
 
class FailableCallable():
    """org.apache.commons.lang3.function.FailableCallable"""
 
    @staticmethod
    def _wrap(java_value: _FailableCallable) -> 'FailableCallable':
        return FailableCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableCallable):
        """
        Dynamic initializer for FailableCallable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableCallable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableCallable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, ):
        """public abstract R org.apache.commons.lang3.function.FailableCallable.call() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableShortSupplier
import org.apache.commons.lang3.function.FailableShortSupplier as _FailableShortSupplier
_FailableShortSupplier = _FailableShortSupplier
from abc import abstractmethod, ABC
 
class FailableShortSupplier():
    """org.apache.commons.lang3.function.FailableShortSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FailableShortSupplier) -> 'FailableShortSupplier':
        return FailableShortSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableShortSupplier):
        """
        Dynamic initializer for FailableShortSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableShortSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableShortSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getAsShort(self, ):
        """public abstract short org.apache.commons.lang3.function.FailableShortSupplier.getAsShort() throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntPredicate
import org.apache.commons.lang3.function.FailableIntPredicate as _FailableIntPredicate
_FailableIntPredicate = _FailableIntPredicate
from abc import abstractmethod, ABC
 
class FailableIntPredicate():
    """org.apache.commons.lang3.function.FailableIntPredicate"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntPredicate) -> 'FailableIntPredicate':
        return FailableIntPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntPredicate):
        """
        Dynamic initializer for FailableIntPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def negate(self) -> 'FailableIntPredicate':
        """public default org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.negate()"""
        return 'FailableIntPredicate'._wrap(super(FailableIntPredicate, self).negate())

    @overload
    def or(self, arg0: 'FailableIntPredicate') -> 'FailableIntPredicate':
        """public default org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.or(org.apache.commons.lang3.function.FailableIntPredicate<E>)"""
        return 'FailableIntPredicate'._wrap(super(_FailableIntPredicate, self).or(arg0))

    @staticmethod
    @overload
    def truePredicate() -> 'FailableIntPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.truePredicate()"""
        return FailableIntPredicate._wrap(_FailableIntPredicate.truePredicate())

    @overload
    def and(self, arg0: 'FailableIntPredicate') -> 'FailableIntPredicate':
        """public default org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.and(org.apache.commons.lang3.function.FailableIntPredicate<E>)"""
        return 'FailableIntPredicate'._wrap(super(_FailableIntPredicate, self).and(arg0))

    @staticmethod
    @overload
    def falsePredicate() -> 'FailableIntPredicate':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntPredicate<E> org.apache.commons.lang3.function.FailableIntPredicate.falsePredicate()"""
        return FailableIntPredicate._wrap(_FailableIntPredicate.falsePredicate())

    @abstractmethod
    def test(self, arg0: int):
        """public abstract boolean org.apache.commons.lang3.function.FailableIntPredicate.test(int) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.TriConsumer
import org.apache.commons.lang3.function.TriConsumer as _TriConsumer
_TriConsumer = _TriConsumer
from abc import abstractmethod, ABC
 
class TriConsumer():
    """org.apache.commons.lang3.function.TriConsumer"""
 
    @staticmethod
    def _wrap(java_value: _TriConsumer) -> 'TriConsumer':
        return TriConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriConsumer):
        """
        Dynamic initializer for TriConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'TriConsumer') -> 'TriConsumer':
        """public default org.apache.commons.lang3.function.TriConsumer<T, U, V> org.apache.commons.lang3.function.TriConsumer.andThen(org.apache.commons.lang3.function.TriConsumer<? super T, ? super U, ? super V>)"""
        return 'TriConsumer'._wrap(super(_TriConsumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: object, arg1: object, arg2: object):
        """public abstract void org.apache.commons.lang3.function.TriConsumer.accept(T,U,V)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.BooleanConsumer
import org.apache.commons.lang3.function.BooleanConsumer as _BooleanConsumer
_BooleanConsumer = _BooleanConsumer
from abc import abstractmethod, ABC
 
class BooleanConsumer():
    """org.apache.commons.lang3.function.BooleanConsumer"""
 
    @staticmethod
    def _wrap(java_value: _BooleanConsumer) -> 'BooleanConsumer':
        return BooleanConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanConsumer):
        """
        Dynamic initializer for BooleanConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: bool):
        """public abstract void org.apache.commons.lang3.function.BooleanConsumer.accept(boolean)"""
        pass

    @overload
    def andThen(self, arg0: 'BooleanConsumer') -> 'BooleanConsumer':
        """public default org.apache.commons.lang3.function.BooleanConsumer org.apache.commons.lang3.function.BooleanConsumer.andThen(org.apache.commons.lang3.function.BooleanConsumer)"""
        return 'BooleanConsumer'._wrap(super(_BooleanConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'BooleanConsumer':
        """public static org.apache.commons.lang3.function.BooleanConsumer org.apache.commons.lang3.function.BooleanConsumer.nop()"""
        return BooleanConsumer._wrap(_BooleanConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableLongToDoubleFunction
import org.apache.commons.lang3.function.FailableLongToDoubleFunction as _FailableLongToDoubleFunction
_FailableLongToDoubleFunction = _FailableLongToDoubleFunction
from abc import abstractmethod, ABC
 
class FailableLongToDoubleFunction():
    """org.apache.commons.lang3.function.FailableLongToDoubleFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableLongToDoubleFunction) -> 'FailableLongToDoubleFunction':
        return FailableLongToDoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableLongToDoubleFunction):
        """
        Dynamic initializer for FailableLongToDoubleFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableLongToDoubleFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableLongToDoubleFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableLongToDoubleFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableLongToDoubleFunction<E> org.apache.commons.lang3.function.FailableLongToDoubleFunction.nop()"""
        return FailableLongToDoubleFunction._wrap(_FailableLongToDoubleFunction.nop())

    @abstractmethod
    def applyAsDouble(self, arg0: int):
        """public abstract double org.apache.commons.lang3.function.FailableLongToDoubleFunction.applyAsDouble(long) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntConsumer
import org.apache.commons.lang3.function.FailableIntConsumer as _FailableIntConsumer
_FailableIntConsumer = _FailableIntConsumer
from abc import abstractmethod, ABC
 
class FailableIntConsumer():
    """org.apache.commons.lang3.function.FailableIntConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntConsumer) -> 'FailableIntConsumer':
        return FailableIntConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntConsumer):
        """
        Dynamic initializer for FailableIntConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void org.apache.commons.lang3.function.FailableIntConsumer.accept(int) throws E"""
        pass

    @overload
    def andThen(self, arg0: 'FailableIntConsumer') -> 'FailableIntConsumer':
        """public default org.apache.commons.lang3.function.FailableIntConsumer<E> org.apache.commons.lang3.function.FailableIntConsumer.andThen(org.apache.commons.lang3.function.FailableIntConsumer<E>)"""
        return 'FailableIntConsumer'._wrap(super(_FailableIntConsumer, self).andThen(arg0))

    @staticmethod
    @overload
    def nop() -> 'FailableIntConsumer':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntConsumer<E> org.apache.commons.lang3.function.FailableIntConsumer.nop()"""
        return FailableIntConsumer._wrap(_FailableIntConsumer.nop()) 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntToLongFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableIntToLongFunction as _FailableIntToLongFunction
_FailableIntToLongFunction = _FailableIntToLongFunction
 
class FailableIntToLongFunction():
    """org.apache.commons.lang3.function.FailableIntToLongFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntToLongFunction) -> 'FailableIntToLongFunction':
        return FailableIntToLongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntToLongFunction):
        """
        Dynamic initializer for FailableIntToLongFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntToLongFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntToLongFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableIntToLongFunction':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntToLongFunction<E> org.apache.commons.lang3.function.FailableIntToLongFunction.nop()"""
        return FailableIntToLongFunction._wrap(_FailableIntToLongFunction.nop())

    @abstractmethod
    def applyAsLong(self, arg0: int):
        """public abstract long org.apache.commons.lang3.function.FailableIntToLongFunction.applyAsLong(int) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableToIntFunction
import org.apache.commons.lang3.function.FailableToIntFunction as _FailableToIntFunction
_FailableToIntFunction = _FailableToIntFunction
from abc import abstractmethod, ABC
 
class FailableToIntFunction():
    """org.apache.commons.lang3.function.FailableToIntFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableToIntFunction) -> 'FailableToIntFunction':
        return FailableToIntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableToIntFunction):
        """
        Dynamic initializer for FailableToIntFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableToIntFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableToIntFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableToIntFunction':
        """public static <T,E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableToIntFunction<T, E> org.apache.commons.lang3.function.FailableToIntFunction.nop()"""
        return FailableToIntFunction._wrap(_FailableToIntFunction.nop())

    @abstractmethod
    def applyAsInt(self, arg0: object):
        """public abstract int org.apache.commons.lang3.function.FailableToIntFunction.applyAsInt(T) throws E"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.function.FailableIntUnaryOperator
from abc import abstractmethod, ABC
import org.apache.commons.lang3.function.FailableIntUnaryOperator as _FailableIntUnaryOperator
_FailableIntUnaryOperator = _FailableIntUnaryOperator
 
class FailableIntUnaryOperator():
    """org.apache.commons.lang3.function.FailableIntUnaryOperator"""
 
    @staticmethod
    def _wrap(java_value: _FailableIntUnaryOperator) -> 'FailableIntUnaryOperator':
        return FailableIntUnaryOperator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableIntUnaryOperator):
        """
        Dynamic initializer for FailableIntUnaryOperator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableIntUnaryOperator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableIntUnaryOperator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nop() -> 'FailableIntUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.nop()"""
        return FailableIntUnaryOperator._wrap(_FailableIntUnaryOperator.nop())

    @staticmethod
    @overload
    def identity() -> 'FailableIntUnaryOperator':
        """public static <E extends java.lang.Throwable> org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.identity()"""
        return FailableIntUnaryOperator._wrap(_FailableIntUnaryOperator.identity())

    @overload
    def andThen(self, arg0: 'FailableIntUnaryOperator') -> 'FailableIntUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.andThen(org.apache.commons.lang3.function.FailableIntUnaryOperator<E>)"""
        return 'FailableIntUnaryOperator'._wrap(super(_FailableIntUnaryOperator, self).andThen(arg0))

    @abstractmethod
    def applyAsInt(self, arg0: int):
        """public abstract int org.apache.commons.lang3.function.FailableIntUnaryOperator.applyAsInt(int) throws E"""
        pass

    @overload
    def compose(self, arg0: 'FailableIntUnaryOperator') -> 'FailableIntUnaryOperator':
        """public default org.apache.commons.lang3.function.FailableIntUnaryOperator<E> org.apache.commons.lang3.function.FailableIntUnaryOperator.compose(org.apache.commons.lang3.function.FailableIntUnaryOperator<E>)"""
        return 'FailableIntUnaryOperator'._wrap(super(_FailableIntUnaryOperator, self).compose(arg0))