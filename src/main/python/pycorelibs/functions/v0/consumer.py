from __future__ import annotations
from overload import overload


 
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import dev.ultreon.libs.functions.v0.consumer.DoubleConsumer as __DoubleConsumer
__DoubleConsumer = __DoubleConsumer
from abc import abstractmethod, ABC
import java.lang.Double as Double
import java.util.function.Consumer as Consumer
 
class DoubleConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.DoubleConsumer"""
 
    @staticmethod
    def __wrap(java_value: __DoubleConsumer) -> 'DoubleConsumer':
        return DoubleConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleConsumer):
        """
        Dynamic initializer for DoubleConsumer.
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
    def accept(self, arg0: float):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.DoubleConsumer.accept(double)"""
        pass

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Double'):
        """public default void dev.ultreon.libs.functions.v0.consumer.DoubleConsumer.accept(java.lang.Double)"""
        super(__DoubleConsumer, self).accept(arg0)

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.DoubleConsumer
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import dev.ultreon.libs.functions.v0.consumer.DoubleConsumer as __DoubleConsumer
__DoubleConsumer = __DoubleConsumer
from abc import abstractmethod, ABC
import java.lang.Double as Double
import java.util.function.Consumer as Consumer
 
class DoubleConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.DoubleConsumer"""
 
    @staticmethod
    def __wrap(java_value: __DoubleConsumer) -> 'DoubleConsumer':
        return DoubleConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleConsumer):
        """
        Dynamic initializer for DoubleConsumer.
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
    def accept(self, arg0: float):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.DoubleConsumer.accept(double)"""
        pass

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Double'):
        """public default void dev.ultreon.libs.functions.v0.consumer.DoubleConsumer.accept(java.lang.Double)"""
        super(__DoubleConsumer, self).accept(arg0)

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.DoubleConsumer 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.ByteConsumer
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import dev.ultreon.libs.functions.v0.consumer.ByteConsumer as __ByteConsumer
__ByteConsumer = __ByteConsumer
from abc import abstractmethod, ABC
import java.lang.Byte as Byte
import java.util.function.Consumer as Consumer
 
class ByteConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.ByteConsumer"""
 
    @staticmethod
    def __wrap(java_value: __ByteConsumer) -> 'ByteConsumer':
        return ByteConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteConsumer):
        """
        Dynamic initializer for ByteConsumer.
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
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Byte'):
        """public default void dev.ultreon.libs.functions.v0.consumer.ByteConsumer.accept(java.lang.Byte)"""
        super(__ByteConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.ByteConsumer.accept(byte)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.TriConsumer
import dev.ultreon.libs.functions.v0.consumer.TriConsumer as __TriConsumer
__TriConsumer = __TriConsumer
from abc import abstractmethod, ABC
 
class TriConsumer(ABC):
    """dev.ultreon.libs.functions.v0.consumer.TriConsumer"""
 
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
 
    @abstractmethod
    def accept(self, arg0: object, arg1: object, arg2: object):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.TriConsumer.accept(A,B,C)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.IntConsumer
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import java.lang.Integer as Integer
import dev.ultreon.libs.functions.v0.consumer.IntConsumer as __IntConsumer
__IntConsumer = __IntConsumer
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class IntConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.IntConsumer"""
 
    @staticmethod
    def __wrap(java_value: __IntConsumer) -> 'IntConsumer':
        return IntConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntConsumer):
        """
        Dynamic initializer for IntConsumer.
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
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Integer'):
        """public default void dev.ultreon.libs.functions.v0.consumer.IntConsumer.accept(java.lang.Integer)"""
        super(__IntConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.IntConsumer.accept(int)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.CharConsumer
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import dev.ultreon.libs.functions.v0.consumer.CharConsumer as __CharConsumer
__CharConsumer = __CharConsumer
import java.lang.Character as Character
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class CharConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.CharConsumer"""
 
    @staticmethod
    def __wrap(java_value: __CharConsumer) -> 'CharConsumer':
        return CharConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharConsumer):
        """
        Dynamic initializer for CharConsumer.
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
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: str):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.CharConsumer.accept(char)"""
        pass

    @overload
    def accept(self, arg0: 'Character'):
        """public default void dev.ultreon.libs.functions.v0.consumer.CharConsumer.accept(java.lang.Character)"""
        super(__CharConsumer, self).accept(arg0) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.BooleanConsumer
import java.lang.Boolean as Boolean
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import dev.ultreon.libs.functions.v0.consumer.BooleanConsumer as __BooleanConsumer
__BooleanConsumer = __BooleanConsumer
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class BooleanConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.BooleanConsumer"""
 
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
 
    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Boolean'):
        """public default void dev.ultreon.libs.functions.v0.consumer.BooleanConsumer.accept(java.lang.Boolean)"""
        super(__BooleanConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: bool):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.BooleanConsumer.accept(boolean)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.ShortConsumer
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import java.lang.Short as Short
import dev.ultreon.libs.functions.v0.consumer.ShortConsumer as __ShortConsumer
__ShortConsumer = __ShortConsumer
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class ShortConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.ShortConsumer"""
 
    @staticmethod
    def __wrap(java_value: __ShortConsumer) -> 'ShortConsumer':
        return ShortConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShortConsumer):
        """
        Dynamic initializer for ShortConsumer.
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
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Short'):
        """public default void dev.ultreon.libs.functions.v0.consumer.ShortConsumer.accept(java.lang.Short)"""
        super(__ShortConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.ShortConsumer.accept(short)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.FloatConsumer
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import dev.ultreon.libs.functions.v0.consumer.FloatConsumer as __FloatConsumer
__FloatConsumer = __FloatConsumer
import java.lang.Float as Float
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class FloatConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.FloatConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FloatConsumer) -> 'FloatConsumer':
        return FloatConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatConsumer):
        """
        Dynamic initializer for FloatConsumer.
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
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Float'):
        """public default void dev.ultreon.libs.functions.v0.consumer.FloatConsumer.accept(java.lang.Float)"""
        super(__FloatConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: float):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.FloatConsumer.accept(float)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.LongConsumer
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
import java.lang.Long as Long
import dev.ultreon.libs.functions.v0.consumer.LongConsumer as __LongConsumer
__LongConsumer = __LongConsumer
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class LongConsumer(ABC, __Consumer, Consumer):
    """dev.ultreon.libs.functions.v0.consumer.LongConsumer"""
 
    @staticmethod
    def __wrap(java_value: __LongConsumer) -> 'LongConsumer':
        return LongConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongConsumer):
        """
        Dynamic initializer for LongConsumer.
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
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'.__wrap(super(__Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Long'):
        """public default void dev.ultreon.libs.functions.v0.consumer.LongConsumer.accept(java.lang.Long)"""
        super(__LongConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.LongConsumer.accept(long)"""
        pass