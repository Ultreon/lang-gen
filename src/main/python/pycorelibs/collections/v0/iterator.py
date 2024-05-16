from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.collections.v0.iterator.DoubleIterator as _DoubleIterator
_DoubleIterator = _DoubleIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import java.lang.Double as Double
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class DoubleIterator():
    """dev.ultreon.libs.collections.v0.iterator.DoubleIterator"""
 
    @staticmethod
    def _wrap(java_value: _DoubleIterator) -> 'DoubleIterator':
        return DoubleIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleIterator):
        """
        Dynamic initializer for DoubleIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def forEachRemaining(self, arg0: 'DoubleConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.DoubleIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.DoubleConsumer)"""
        super(_DoubleIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.collections.v0.iterator.DoubleIterator.next()"""
        return _transform(super(DoubleIterator, self).next()).'Double'Value()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def nextDouble(self, ):
        """public abstract double dev.ultreon.libs.collections.v0.iterator.DoubleIterator.nextDouble()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.DoubleIterator
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.collections.v0.iterator.DoubleIterator as _DoubleIterator
_DoubleIterator = _DoubleIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import java.lang.Double as Double
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class DoubleIterator():
    """dev.ultreon.libs.collections.v0.iterator.DoubleIterator"""
 
    @staticmethod
    def _wrap(java_value: _DoubleIterator) -> 'DoubleIterator':
        return DoubleIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleIterator):
        """
        Dynamic initializer for DoubleIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def forEachRemaining(self, arg0: 'DoubleConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.DoubleIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.DoubleConsumer)"""
        super(_DoubleIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.collections.v0.iterator.DoubleIterator.next()"""
        return _transform(super(DoubleIterator, self).next()).'Double'Value()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def nextDouble(self, ):
        """public abstract double dev.ultreon.libs.collections.v0.iterator.DoubleIterator.nextDouble()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.DoubleIterator 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.CharIterator
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import java.lang.Character as _Character
_Character = _Character
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import dev.ultreon.libs.collections.v0.iterator.CharIterator as _CharIterator
_CharIterator = _CharIterator
import java.lang.Character as Character
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class CharIterator():
    """dev.ultreon.libs.collections.v0.iterator.CharIterator"""
 
    @staticmethod
    def _wrap(java_value: _CharIterator) -> 'CharIterator':
        return CharIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharIterator):
        """
        Dynamic initializer for CharIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def nextChar(self, ):
        """public abstract char dev.ultreon.libs.collections.v0.iterator.CharIterator.nextChar()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @overload
    def forEachRemaining(self, arg0: 'CharConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.CharIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.CharConsumer)"""
        super(_CharIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @override
    @overload
    def next(self) -> 'Character':
        """public default java.lang.Character dev.ultreon.libs.collections.v0.iterator.CharIterator.next()"""
        return 'Character'._wrap(super(CharIterator, self).next())

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.DoubleIterable
from pyquantum_helper import import_once as _import_once
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.DoubleIterable as _DoubleIterable
_DoubleIterable = _DoubleIterable
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class DoubleIterable():
    """dev.ultreon.libs.collections.v0.iterator.DoubleIterable"""
 
    @staticmethod
    def _wrap(java_value: _DoubleIterable) -> 'DoubleIterable':
        return DoubleIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleIterable):
        """
        Dynamic initializer for DoubleIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.DoubleIterator dev.ultreon.libs.collections.v0.iterator.DoubleIterable.iterator()"""
        pass

    @overload
    def forEach(self, arg0: 'DoubleConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.DoubleIterable.forEach(dev.ultreon.libs.functions.v0.consumer.DoubleConsumer)"""
        super(_DoubleIterable, self).forEach(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.LongIterator
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Long as Long
import dev.ultreon.libs.collections.v0.iterator.LongIterator as _LongIterator
_LongIterator = _LongIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class LongIterator():
    """dev.ultreon.libs.collections.v0.iterator.LongIterator"""
 
    @staticmethod
    def _wrap(java_value: _LongIterator) -> 'LongIterator':
        return LongIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongIterator):
        """
        Dynamic initializer for LongIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.collections.v0.iterator.LongIterator.next()"""
        return _transform(super(LongIterator, self).next()).'Long'Value()

    @abstractmethod
    def nextLong(self, ):
        """public abstract long dev.ultreon.libs.collections.v0.iterator.LongIterator.nextLong()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass

    @overload
    def forEachRemaining(self, arg0: 'LongConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.LongIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.LongConsumer)"""
        super(_LongIterator, self).forEachRemaining(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ByteIterator
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.collections.v0.iterator.ByteIterator as _ByteIterator
_ByteIterator = _ByteIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import java.lang.Byte as Byte
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class ByteIterator():
    """dev.ultreon.libs.collections.v0.iterator.ByteIterator"""
 
    @staticmethod
    def _wrap(java_value: _ByteIterator) -> 'ByteIterator':
        return ByteIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteIterator):
        """
        Dynamic initializer for ByteIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.collections.v0.iterator.ByteIterator.next()"""
        return _transform(super(ByteIterator, self).next()).'Byte'Value()

    @overload
    def forEachRemaining(self, arg0: 'ByteConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ByteIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        super(_ByteIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def nextByte(self, ):
        """public abstract byte dev.ultreon.libs.collections.v0.iterator.ByteIterator.nextByte()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.BooleanIterator
from pyquantum_helper import import_once as _import_once
import java.lang.Boolean as Boolean
import dev.ultreon.libs.collections.v0.iterator.BooleanIterator as _BooleanIterator
_BooleanIterator = _BooleanIterator
from pyquantum_helper import override
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class BooleanIterator():
    """dev.ultreon.libs.collections.v0.iterator.BooleanIterator"""
 
    @staticmethod
    def _wrap(java_value: _BooleanIterator) -> 'BooleanIterator':
        return BooleanIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanIterator):
        """
        Dynamic initializer for BooleanIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def nextBoolean(self, ):
        """public abstract boolean dev.ultreon.libs.collections.v0.iterator.BooleanIterator.nextBoolean()"""
        pass

    @overload
    def forEachRemaining(self, arg0: 'BooleanConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.BooleanIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        super(_BooleanIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Boolean':
        """public default java.lang.Boolean dev.ultreon.libs.collections.v0.iterator.BooleanIterator.next()"""
        return 'Boolean'._wrap(super(BooleanIterator, self).next())

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.LongIterable
from pyquantum_helper import import_once as _import_once
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import dev.ultreon.libs.collections.v0.iterator.LongIterable as _LongIterable
_LongIterable = _LongIterable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class LongIterable():
    """dev.ultreon.libs.collections.v0.iterator.LongIterable"""
 
    @staticmethod
    def _wrap(java_value: _LongIterable) -> 'LongIterable':
        return LongIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongIterable):
        """
        Dynamic initializer for LongIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def forEach(self, arg0: 'LongConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.LongIterable.forEach(dev.ultreon.libs.functions.v0.consumer.LongConsumer)"""
        super(_LongIterable, self).forEach(arg0)

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.LongIterator dev.ultreon.libs.collections.v0.iterator.LongIterable.iterator()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ShortIterable
from pyquantum_helper import import_once as _import_once
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import dev.ultreon.libs.collections.v0.iterator.ShortIterable as _ShortIterable
_ShortIterable = _ShortIterable
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class ShortIterable():
    """dev.ultreon.libs.collections.v0.iterator.ShortIterable"""
 
    @staticmethod
    def _wrap(java_value: _ShortIterable) -> 'ShortIterable':
        return ShortIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShortIterable):
        """
        Dynamic initializer for ShortIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShortIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShortIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def forEach(self, arg0: 'ShortConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ShortIterable.forEach(dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        super(_ShortIterable, self).forEach(arg0)

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.ShortIterator dev.ultreon.libs.collections.v0.iterator.ShortIterable.iterator()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.IntIterable
from pyquantum_helper import import_once as _import_once
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import dev.ultreon.libs.collections.v0.iterator.IntIterable as _IntIterable
_IntIterable = _IntIterable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class IntIterable():
    """dev.ultreon.libs.collections.v0.iterator.IntIterable"""
 
    @staticmethod
    def _wrap(java_value: _IntIterable) -> 'IntIterable':
        return IntIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntIterable):
        """
        Dynamic initializer for IntIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.IntIterator dev.ultreon.libs.collections.v0.iterator.IntIterable.iterator()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def forEach(self, arg0: 'IntConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.IntIterable.forEach(dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        super(_IntIterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.BooleanIterable
from pyquantum_helper import import_once as _import_once
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.BooleanIterable as _BooleanIterable
_BooleanIterable = _BooleanIterable
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class BooleanIterable():
    """dev.ultreon.libs.collections.v0.iterator.BooleanIterable"""
 
    @staticmethod
    def _wrap(java_value: _BooleanIterable) -> 'BooleanIterable':
        return BooleanIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanIterable):
        """
        Dynamic initializer for BooleanIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.BooleanIterator dev.ultreon.libs.collections.v0.iterator.BooleanIterable.iterator()"""
        pass

    @overload
    def forEach(self, arg0: 'BooleanConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.BooleanIterable.forEach(dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        super(_BooleanIterable, self).forEach(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ByteIterable
from pyquantum_helper import import_once as _import_once
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import dev.ultreon.libs.collections.v0.iterator.ByteIterable as _ByteIterable
_ByteIterable = _ByteIterable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class ByteIterable():
    """dev.ultreon.libs.collections.v0.iterator.ByteIterable"""
 
    @staticmethod
    def _wrap(java_value: _ByteIterable) -> 'ByteIterable':
        return ByteIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteIterable):
        """
        Dynamic initializer for ByteIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def forEach(self, arg0: 'ByteConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ByteIterable.forEach(dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        super(_ByteIterable, self).forEach(arg0)

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.ByteIterator dev.ultreon.libs.collections.v0.iterator.ByteIterable.iterator()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.FloatIterator
from pyquantum_helper import import_once as _import_once
import dev.ultreon.libs.collections.v0.iterator.FloatIterator as _FloatIterator
_FloatIterator = _FloatIterator
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Float as Float
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class FloatIterator():
    """dev.ultreon.libs.collections.v0.iterator.FloatIterator"""
 
    @staticmethod
    def _wrap(java_value: _FloatIterator) -> 'FloatIterator':
        return FloatIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatIterator):
        """
        Dynamic initializer for FloatIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def nextFloat(self, ):
        """public abstract float dev.ultreon.libs.collections.v0.iterator.FloatIterator.nextFloat()"""
        pass

    @overload
    def forEachRemaining(self, arg0: 'FloatConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.FloatIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        super(_FloatIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.collections.v0.iterator.FloatIterator.next()"""
        return _transform(super(FloatIterator, self).next()).'Float'Value()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ShortIterator
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Short as Short
import dev.ultreon.libs.collections.v0.iterator.ShortIterator as _ShortIterator
_ShortIterator = _ShortIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class ShortIterator():
    """dev.ultreon.libs.collections.v0.iterator.ShortIterator"""
 
    @staticmethod
    def _wrap(java_value: _ShortIterator) -> 'ShortIterator':
        return ShortIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShortIterator):
        """
        Dynamic initializer for ShortIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShortIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShortIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @overload
    def forEachRemaining(self, arg0: 'ShortConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ShortIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        super(_ShortIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def nextShort(self, ):
        """public abstract short dev.ultreon.libs.collections.v0.iterator.ShortIterator.nextShort()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass

    @override
    @overload
    def next(self) -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.collections.v0.iterator.ShortIterator.next()"""
        return _transform(super(ShortIterator, self).next()).'Short'Value() 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.CharIterable
from pyquantum_helper import import_once as _import_once
import dev.ultreon.libs.collections.v0.iterator.CharIterable as _CharIterable
_CharIterable = _CharIterable
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class CharIterable():
    """dev.ultreon.libs.collections.v0.iterator.CharIterable"""
 
    @staticmethod
    def _wrap(java_value: _CharIterable) -> 'CharIterable':
        return CharIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharIterable):
        """
        Dynamic initializer for CharIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def forEach(self, arg0: 'CharConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.CharIterable.forEach(dev.ultreon.libs.functions.v0.consumer.CharConsumer)"""
        super(_CharIterable, self).forEach(arg0)

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.CharIterator dev.ultreon.libs.collections.v0.iterator.CharIterable.iterator()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.IntIterator
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Integer as Integer
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.IntIterator as _IntIterator
_IntIterator = _IntIterator
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class IntIterator():
    """dev.ultreon.libs.collections.v0.iterator.IntIterator"""
 
    @staticmethod
    def _wrap(java_value: _IntIterator) -> 'IntIterator':
        return IntIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntIterator):
        """
        Dynamic initializer for IntIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def forEachRemaining(self, arg0: 'IntConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.IntIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        super(_IntIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.collections.v0.iterator.IntIterator.next()"""
        return _transform(super(IntIterator, self).next()).'Integer'Value()

    @abstractmethod
    def nextInt(self, ):
        """public abstract int dev.ultreon.libs.collections.v0.iterator.IntIterator.nextInt()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.FloatIterable
from pyquantum_helper import import_once as _import_once
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import dev.ultreon.libs.collections.v0.iterator.FloatIterable as _FloatIterable
_FloatIterable = _FloatIterable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class FloatIterable():
    """dev.ultreon.libs.collections.v0.iterator.FloatIterable"""
 
    @staticmethod
    def _wrap(java_value: _FloatIterable) -> 'FloatIterable':
        return FloatIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatIterable):
        """
        Dynamic initializer for FloatIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.FloatIterator dev.ultreon.libs.collections.v0.iterator.FloatIterable.iterator()"""
        pass

    @overload
    def forEach(self, arg0: 'FloatConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.FloatIterable.forEach(dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        super(_FloatIterable, self).forEach(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())