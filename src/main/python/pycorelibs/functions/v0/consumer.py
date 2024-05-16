from __future__ import annotations
from overload import overload


 
import dev.ultreon.libs.functions.v0.consumer.LongConsumer as _LongConsumer
_LongConsumer = _LongConsumer
import java.lang.Long as Long
from pyquantum_helper import override
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class LongConsumer():
    """dev.ultreon.libs.functions.v0.consumer.LongConsumer"""
 
    @staticmethod
    def _wrap(java_value: _LongConsumer) -> 'LongConsumer':
        return LongConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongConsumer):
        """
        Dynamic initializer for LongConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'Long'):
        """public default void dev.ultreon.libs.functions.v0.consumer.LongConsumer.accept(java.lang.Long)"""
        super(_LongConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.LongConsumer.accept(long)"""
        pass

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.LongConsumer
import dev.ultreon.libs.functions.v0.consumer.LongConsumer as _LongConsumer
_LongConsumer = _LongConsumer
import java.lang.Long as Long
from pyquantum_helper import override
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class LongConsumer():
    """dev.ultreon.libs.functions.v0.consumer.LongConsumer"""
 
    @staticmethod
    def _wrap(java_value: _LongConsumer) -> 'LongConsumer':
        return LongConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongConsumer):
        """
        Dynamic initializer for LongConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'Long'):
        """public default void dev.ultreon.libs.functions.v0.consumer.LongConsumer.accept(java.lang.Long)"""
        super(_LongConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.LongConsumer.accept(long)"""
        pass

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.LongConsumer 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.TriConsumer
import dev.ultreon.libs.functions.v0.consumer.TriConsumer as _TriConsumer
_TriConsumer = _TriConsumer
from abc import abstractmethod, ABC
 
class TriConsumer():
    """dev.ultreon.libs.functions.v0.consumer.TriConsumer"""
 
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
 
    @abstractmethod
    def accept(self, arg0: object, arg1: object, arg2: object):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.TriConsumer.accept(A,B,C)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.BooleanConsumer
import java.lang.Boolean as Boolean
import dev.ultreon.libs.functions.v0.consumer.BooleanConsumer as _BooleanConsumer
_BooleanConsumer = _BooleanConsumer
from pyquantum_helper import override
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class BooleanConsumer():
    """dev.ultreon.libs.functions.v0.consumer.BooleanConsumer"""
 
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
 
    @overload
    def accept(self, arg0: 'Boolean'):
        """public default void dev.ultreon.libs.functions.v0.consumer.BooleanConsumer.accept(java.lang.Boolean)"""
        super(_BooleanConsumer, self).accept(arg0)

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: bool):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.BooleanConsumer.accept(boolean)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.FloatConsumer
from pyquantum_helper import override
import java.lang.Float as Float
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.consumer.FloatConsumer as _FloatConsumer
_FloatConsumer = _FloatConsumer
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class FloatConsumer():
    """dev.ultreon.libs.functions.v0.consumer.FloatConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FloatConsumer) -> 'FloatConsumer':
        return FloatConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatConsumer):
        """
        Dynamic initializer for FloatConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'Float'):
        """public default void dev.ultreon.libs.functions.v0.consumer.FloatConsumer.accept(java.lang.Float)"""
        super(_FloatConsumer, self).accept(arg0)

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: float):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.FloatConsumer.accept(float)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.CharConsumer
from pyquantum_helper import override
import java.lang.Character as Character
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.consumer.CharConsumer as _CharConsumer
_CharConsumer = _CharConsumer
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class CharConsumer():
    """dev.ultreon.libs.functions.v0.consumer.CharConsumer"""
 
    @staticmethod
    def _wrap(java_value: _CharConsumer) -> 'CharConsumer':
        return CharConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharConsumer):
        """
        Dynamic initializer for CharConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Character'):
        """public default void dev.ultreon.libs.functions.v0.consumer.CharConsumer.accept(java.lang.Character)"""
        super(_CharConsumer, self).accept(arg0)

    @abstractmethod
    def accept(self, arg0: str):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.CharConsumer.accept(char)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.IntConsumer
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.consumer.IntConsumer as _IntConsumer
_IntConsumer = _IntConsumer
import java.lang.Integer as Integer
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class IntConsumer():
    """dev.ultreon.libs.functions.v0.consumer.IntConsumer"""
 
    @staticmethod
    def _wrap(java_value: _IntConsumer) -> 'IntConsumer':
        return IntConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntConsumer):
        """
        Dynamic initializer for IntConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'Integer'):
        """public default void dev.ultreon.libs.functions.v0.consumer.IntConsumer.accept(java.lang.Integer)"""
        super(_IntConsumer, self).accept(arg0)

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.IntConsumer.accept(int)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.DoubleConsumer
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.consumer.DoubleConsumer as _DoubleConsumer
_DoubleConsumer = _DoubleConsumer
from abc import abstractmethod, ABC
import java.lang.Double as Double
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class DoubleConsumer():
    """dev.ultreon.libs.functions.v0.consumer.DoubleConsumer"""
 
    @staticmethod
    def _wrap(java_value: _DoubleConsumer) -> 'DoubleConsumer':
        return DoubleConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleConsumer):
        """
        Dynamic initializer for DoubleConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: float):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.DoubleConsumer.accept(double)"""
        pass

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

    @overload
    def accept(self, arg0: 'Double'):
        """public default void dev.ultreon.libs.functions.v0.consumer.DoubleConsumer.accept(java.lang.Double)"""
        super(_DoubleConsumer, self).accept(arg0) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.ShortConsumer
from pyquantum_helper import override
import java.lang.Short as Short
import dev.ultreon.libs.functions.v0.consumer.ShortConsumer as _ShortConsumer
_ShortConsumer = _ShortConsumer
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class ShortConsumer():
    """dev.ultreon.libs.functions.v0.consumer.ShortConsumer"""
 
    @staticmethod
    def _wrap(java_value: _ShortConsumer) -> 'ShortConsumer':
        return ShortConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShortConsumer):
        """
        Dynamic initializer for ShortConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShortConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShortConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'Short'):
        """public default void dev.ultreon.libs.functions.v0.consumer.ShortConsumer.accept(java.lang.Short)"""
        super(_ShortConsumer, self).accept(arg0)

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.ShortConsumer.accept(short)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.consumer.ByteConsumer
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.consumer.ByteConsumer as _ByteConsumer
_ByteConsumer = _ByteConsumer
from abc import abstractmethod, ABC
import java.lang.Byte as Byte
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
 
class ByteConsumer():
    """dev.ultreon.libs.functions.v0.consumer.ByteConsumer"""
 
    @staticmethod
    def _wrap(java_value: _ByteConsumer) -> 'ByteConsumer':
        return ByteConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteConsumer):
        """
        Dynamic initializer for ByteConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'Byte'):
        """public default void dev.ultreon.libs.functions.v0.consumer.ByteConsumer.accept(java.lang.Byte)"""
        super(_ByteConsumer, self).accept(arg0)

    @overload
    def andThen(self, arg0: 'Consumer') -> 'Consumer':
        """public default java.util.function.Consumer<T> java.util.function.Consumer.andThen(java.util.function.Consumer<? super T>)"""
        return 'Consumer'._wrap(super(_Consumer, self).andThen(arg0))

    @abstractmethod
    def accept(self, arg0: int):
        """public abstract void dev.ultreon.libs.functions.v0.consumer.ByteConsumer.accept(byte)"""
        pass