from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.iterator.CharIterator as __CharIterator
__CharIterator = __CharIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Character as __Character
__Character = __Character
import java.lang.Character as Character
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class CharIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.CharIterator"""
 
    @staticmethod
    def __wrap(java_value: __CharIterator) -> 'CharIterator':
        return CharIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharIterator):
        """
        Dynamic initializer for CharIterator.
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
    def forEachRemaining(self, arg0: 'CharConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.CharIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.CharConsumer)"""
        super(__CharIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def nextChar(self, ):
        """public abstract char dev.ultreon.libs.collections.v0.iterator.CharIterator.nextChar()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @override
    @overload
    def next(self) -> 'Character':
        """public default java.lang.Character dev.ultreon.libs.collections.v0.iterator.CharIterator.next()"""
        return 'Character'.__wrap(super(CharIterator, self).next())

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.CharIterator
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.iterator.CharIterator as __CharIterator
__CharIterator = __CharIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Character as __Character
__Character = __Character
import java.lang.Character as Character
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class CharIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.CharIterator"""
 
    @staticmethod
    def __wrap(java_value: __CharIterator) -> 'CharIterator':
        return CharIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharIterator):
        """
        Dynamic initializer for CharIterator.
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
    def forEachRemaining(self, arg0: 'CharConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.CharIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.CharConsumer)"""
        super(__CharIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def nextChar(self, ):
        """public abstract char dev.ultreon.libs.collections.v0.iterator.CharIterator.nextChar()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @override
    @overload
    def next(self) -> 'Character':
        """public default java.lang.Character dev.ultreon.libs.collections.v0.iterator.CharIterator.next()"""
        return 'Character'.__wrap(super(CharIterator, self).next())

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.CharIterator 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ShortIterable
from pyquantum_helper import import_once as __import_once__
import java.util.Spliterator as Spliterator
import dev.ultreon.libs.collections.v0.iterator.ShortIterable as __ShortIterable
__ShortIterable = __ShortIterable
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class ShortIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.ShortIterable"""
 
    @staticmethod
    def __wrap(java_value: __ShortIterable) -> 'ShortIterable':
        return ShortIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShortIterable):
        """
        Dynamic initializer for ShortIterable.
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
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.ShortIterator dev.ultreon.libs.collections.v0.iterator.ShortIterable.iterator()"""
        pass

    @overload
    def forEach(self, arg0: 'ShortConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ShortIterable.forEach(dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        super(__ShortIterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.FloatIterable
from pyquantum_helper import import_once as __import_once__
import java.util.Spliterator as Spliterator
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.FloatIterable as __FloatIterable
__FloatIterable = __FloatIterable
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class FloatIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.FloatIterable"""
 
    @staticmethod
    def __wrap(java_value: __FloatIterable) -> 'FloatIterable':
        return FloatIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatIterable):
        """
        Dynamic initializer for FloatIterable.
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
    def forEach(self, arg0: 'FloatConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.FloatIterable.forEach(dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        super(__FloatIterable, self).forEach(arg0)

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.FloatIterator dev.ultreon.libs.collections.v0.iterator.FloatIterable.iterator()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.FloatIterator
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.iterator.FloatIterator as __FloatIterator
__FloatIterator = __FloatIterator
from pyquantum_helper import transform as __transform
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Float as Float
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class FloatIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.FloatIterator"""
 
    @staticmethod
    def __wrap(java_value: __FloatIterator) -> 'FloatIterator':
        return FloatIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatIterator):
        """
        Dynamic initializer for FloatIterator.
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
    def nextFloat(self, ):
        """public abstract float dev.ultreon.libs.collections.v0.iterator.FloatIterator.nextFloat()"""
        pass

    @override
    @overload
    def next(self) -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.collections.v0.iterator.FloatIterator.next()"""
        return __transform(super(FloatIterator, self).next()).'Float'Value()

    @overload
    def forEachRemaining(self, arg0: 'FloatConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.FloatIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        super(__FloatIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.DoubleIterable
from pyquantum_helper import import_once as __import_once__
import java.util.Spliterator as Spliterator
import dev.ultreon.libs.collections.v0.iterator.DoubleIterable as __DoubleIterable
__DoubleIterable = __DoubleIterable
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class DoubleIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.DoubleIterable"""
 
    @staticmethod
    def __wrap(java_value: __DoubleIterable) -> 'DoubleIterable':
        return DoubleIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleIterable):
        """
        Dynamic initializer for DoubleIterable.
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
    def forEach(self, arg0: 'DoubleConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.DoubleIterable.forEach(dev.ultreon.libs.functions.v0.consumer.DoubleConsumer)"""
        super(__DoubleIterable, self).forEach(arg0)

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.DoubleIterator dev.ultreon.libs.collections.v0.iterator.DoubleIterable.iterator()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.DoubleIterator
from pyquantum_helper import import_once as __import_once__
from pyquantum_helper import transform as __transform
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import dev.ultreon.libs.collections.v0.iterator.DoubleIterator as __DoubleIterator
__DoubleIterator = __DoubleIterator
from abc import abstractmethod, ABC
import java.lang.Double as Double
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class DoubleIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.DoubleIterator"""
 
    @staticmethod
    def __wrap(java_value: __DoubleIterator) -> 'DoubleIterator':
        return DoubleIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleIterator):
        """
        Dynamic initializer for DoubleIterator.
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
    def next(self) -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.collections.v0.iterator.DoubleIterator.next()"""
        return __transform(super(DoubleIterator, self).next()).'Double'Value()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @overload
    def forEachRemaining(self, arg0: 'DoubleConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.DoubleIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.DoubleConsumer)"""
        super(__DoubleIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def nextDouble(self, ):
        """public abstract double dev.ultreon.libs.collections.v0.iterator.DoubleIterator.nextDouble()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.IntIterable
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.iterator.IntIterable as __IntIterable
__IntIterable = __IntIterable
import java.util.Spliterator as Spliterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class IntIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.IntIterable"""
 
    @staticmethod
    def __wrap(java_value: __IntIterable) -> 'IntIterable':
        return IntIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntIterable):
        """
        Dynamic initializer for IntIterable.
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
    def forEach(self, arg0: 'IntConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.IntIterable.forEach(dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        super(__IntIterable, self).forEach(arg0)

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.IntIterator dev.ultreon.libs.collections.v0.iterator.IntIterable.iterator()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.CharIterable
from pyquantum_helper import import_once as __import_once__
import java.util.Spliterator as Spliterator
import dev.ultreon.libs.collections.v0.iterator.CharIterable as __CharIterable
__CharIterable = __CharIterable
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class CharIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.CharIterable"""
 
    @staticmethod
    def __wrap(java_value: __CharIterable) -> 'CharIterable':
        return CharIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharIterable):
        """
        Dynamic initializer for CharIterable.
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
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.CharIterator dev.ultreon.libs.collections.v0.iterator.CharIterable.iterator()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def forEach(self, arg0: 'CharConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.CharIterable.forEach(dev.ultreon.libs.functions.v0.consumer.CharConsumer)"""
        super(__CharIterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.LongIterator
from pyquantum_helper import import_once as __import_once__
from pyquantum_helper import transform as __transform
import java.lang.Long as Long
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.LongIterator as __LongIterator
__LongIterator = __LongIterator
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class LongIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.LongIterator"""
 
    @staticmethod
    def __wrap(java_value: __LongIterator) -> 'LongIterator':
        return LongIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongIterator):
        """
        Dynamic initializer for LongIterator.
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
    def forEachRemaining(self, arg0: 'LongConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.LongIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.LongConsumer)"""
        super(__LongIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def nextLong(self, ):
        """public abstract long dev.ultreon.libs.collections.v0.iterator.LongIterator.nextLong()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.collections.v0.iterator.LongIterator.next()"""
        return __transform(super(LongIterator, self).next()).'Long'Value()

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
from pyquantum_helper import import_once as __import_once__
import java.util.Spliterator as Spliterator
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.LongIterable as __LongIterable
__LongIterable = __LongIterable
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class LongIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.LongIterable"""
 
    @staticmethod
    def __wrap(java_value: __LongIterable) -> 'LongIterable':
        return LongIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongIterable):
        """
        Dynamic initializer for LongIterable.
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
    def forEach(self, arg0: 'LongConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.LongIterable.forEach(dev.ultreon.libs.functions.v0.consumer.LongConsumer)"""
        super(__LongIterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.LongIterator dev.ultreon.libs.collections.v0.iterator.LongIterable.iterator()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.BooleanIterable
from pyquantum_helper import import_once as __import_once__
import java.util.Spliterator as Spliterator
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.BooleanIterable as __BooleanIterable
__BooleanIterable = __BooleanIterable
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class BooleanIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.BooleanIterable"""
 
    @staticmethod
    def __wrap(java_value: __BooleanIterable) -> 'BooleanIterable':
        return BooleanIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanIterable):
        """
        Dynamic initializer for BooleanIterable.
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
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.BooleanIterator dev.ultreon.libs.collections.v0.iterator.BooleanIterable.iterator()"""
        pass

    @overload
    def forEach(self, arg0: 'BooleanConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.BooleanIterable.forEach(dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        super(__BooleanIterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ByteIterator
from pyquantum_helper import import_once as __import_once__
from pyquantum_helper import transform as __transform
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import dev.ultreon.libs.collections.v0.iterator.ByteIterator as __ByteIterator
__ByteIterator = __ByteIterator
from abc import abstractmethod, ABC
import java.lang.Byte as Byte
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class ByteIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.ByteIterator"""
 
    @staticmethod
    def __wrap(java_value: __ByteIterator) -> 'ByteIterator':
        return ByteIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteIterator):
        """
        Dynamic initializer for ByteIterator.
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
    def forEachRemaining(self, arg0: 'ByteConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ByteIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        super(__ByteIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def nextByte(self, ):
        """public abstract byte dev.ultreon.libs.collections.v0.iterator.ByteIterator.nextByte()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @override
    @overload
    def next(self) -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.collections.v0.iterator.ByteIterator.next()"""
        return __transform(super(ByteIterator, self).next()).'Byte'Value()

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.IntIterator
from pyquantum_helper import import_once as __import_once__
from pyquantum_helper import transform as __transform
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Integer as Integer
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.iterator.IntIterator as __IntIterator
__IntIterator = __IntIterator
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class IntIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.IntIterator"""
 
    @staticmethod
    def __wrap(java_value: __IntIterator) -> 'IntIterator':
        return IntIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntIterator):
        """
        Dynamic initializer for IntIterator.
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
    def next(self) -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.collections.v0.iterator.IntIterator.next()"""
        return __transform(super(IntIterator, self).next()).'Integer'Value()

    @abstractmethod
    def nextInt(self, ):
        """public abstract int dev.ultreon.libs.collections.v0.iterator.IntIterator.nextInt()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def forEachRemaining(self, arg0: 'IntConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.IntIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        super(__IntIterator, self).forEachRemaining(arg0)

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
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as Boolean
import dev.ultreon.libs.collections.v0.iterator.BooleanIterator as __BooleanIterator
__BooleanIterator = __BooleanIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class BooleanIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.BooleanIterator"""
 
    @staticmethod
    def __wrap(java_value: __BooleanIterator) -> 'BooleanIterator':
        return BooleanIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanIterator):
        """
        Dynamic initializer for BooleanIterator.
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
    def nextBoolean(self, ):
        """public abstract boolean dev.ultreon.libs.collections.v0.iterator.BooleanIterator.nextBoolean()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Boolean':
        """public default java.lang.Boolean dev.ultreon.libs.collections.v0.iterator.BooleanIterator.next()"""
        return 'Boolean'.__wrap(super(BooleanIterator, self).next())

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @overload
    def forEachRemaining(self, arg0: 'BooleanConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.BooleanIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        super(__BooleanIterator, self).forEachRemaining(arg0)

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ByteIterable
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.iterator.ByteIterable as __ByteIterable
__ByteIterable = __ByteIterable
import java.util.Spliterator as Spliterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.function.Consumer as Consumer
 
class ByteIterable(ABC, __Iterable, Iterable):
    """dev.ultreon.libs.collections.v0.iterator.ByteIterable"""
 
    @staticmethod
    def __wrap(java_value: __ByteIterable) -> 'ByteIterable':
        return ByteIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteIterable):
        """
        Dynamic initializer for ByteIterable.
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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @abstractmethod
    def iterator(self, ):
        """public abstract dev.ultreon.libs.collections.v0.iterator.ByteIterator dev.ultreon.libs.collections.v0.iterator.ByteIterable.iterator()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def forEach(self, arg0: 'ByteConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ByteIterable.forEach(dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        super(__ByteIterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.iterator.ShortIterator
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.iterator.ShortIterator as __ShortIterator
__ShortIterator = __ShortIterator
from pyquantum_helper import transform as __transform
import java.lang.Short as Short
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from abc import abstractmethod, ABC
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
 
class ShortIterator(ABC, __Iterator, Iterator):
    """dev.ultreon.libs.collections.v0.iterator.ShortIterator"""
 
    @staticmethod
    def __wrap(java_value: __ShortIterator) -> 'ShortIterator':
        return ShortIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShortIterator):
        """
        Dynamic initializer for ShortIterator.
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
    def next(self) -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.collections.v0.iterator.ShortIterator.next()"""
        return __transform(super(ShortIterator, self).next()).'Short'Value()

    @overload
    def forEachRemaining(self, arg0: 'ShortConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.ShortIterator.forEachRemaining(dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        super(__ShortIterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def nextShort(self, ):
        """public abstract short dev.ultreon.libs.collections.v0.iterator.ShortIterator.nextShort()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass