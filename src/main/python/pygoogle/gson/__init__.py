from __future__ import annotations
from overload import overload


 
import java.lang.reflect.Field as Field
import com.google.gson.FieldNamingStrategy as __FieldNamingStrategy
__FieldNamingStrategy = __FieldNamingStrategy
from abc import abstractmethod, ABC
 
class FieldNamingStrategy(ABC):
    """com.google.gson.FieldNamingStrategy"""
 
    @staticmethod
    def __wrap(java_value: __FieldNamingStrategy) -> 'FieldNamingStrategy':
        return FieldNamingStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldNamingStrategy):
        """
        Dynamic initializer for FieldNamingStrategy.
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
    def translateName(self, arg0: 'Field'):
        """public abstract java.lang.String com.google.gson.FieldNamingStrategy.translateName(java.lang.reflect.Field)"""
        pass

 
 
 
# CLASS: com.google.gson.FieldNamingStrategy
import java.lang.reflect.Field as Field
import com.google.gson.FieldNamingStrategy as __FieldNamingStrategy
__FieldNamingStrategy = __FieldNamingStrategy
from abc import abstractmethod, ABC
 
class FieldNamingStrategy(ABC):
    """com.google.gson.FieldNamingStrategy"""
 
    @staticmethod
    def __wrap(java_value: __FieldNamingStrategy) -> 'FieldNamingStrategy':
        return FieldNamingStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldNamingStrategy):
        """
        Dynamic initializer for FieldNamingStrategy.
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
    def translateName(self, arg0: 'Field'):
        """public abstract java.lang.String com.google.gson.FieldNamingStrategy.translateName(java.lang.reflect.Field)"""
        pass

 
 
 
# CLASS: com.google.gson.FieldNamingStrategy 
 
 
# CLASS: com.google.gson.JsonStreamParser
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.gson.JsonStreamParser as __JsonStreamParser
__JsonStreamParser = __JsonStreamParser
from builtins import int
 
class JsonStreamParser():
    """com.google.gson.JsonStreamParser"""
 
    @staticmethod
    def __wrap(java_value: __JsonStreamParser) -> 'JsonStreamParser':
        return JsonStreamParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonStreamParser):
        """
        Dynamic initializer for JsonStreamParser.
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
    def hasNext(self) -> bool:
        """public boolean com.google.gson.JsonStreamParser.hasNext()"""
        return bool.__wrap(super(JsonStreamParser, self).hasNext())

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
    def next(self) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonStreamParser.next() throws com.google.gson.JsonParseException"""
        return 'JsonElement'.__wrap(super(JsonStreamParser, self).next())

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

    @overload
    def __init__(self, arg0: 'Reader'):
        """public com.google.gson.JsonStreamParser(java.io.Reader)"""
        val = __JsonStreamParser(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void com.google.gson.JsonStreamParser.remove()"""
        super(JsonStreamParser, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonStreamParser(java.lang.String)"""
        val = __JsonStreamParser(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.InstanceCreator
import java.lang.reflect.Type as Type
import com.google.gson.InstanceCreator as __InstanceCreator
__InstanceCreator = __InstanceCreator
from abc import abstractmethod, ABC
 
class InstanceCreator(ABC):
    """com.google.gson.InstanceCreator"""
 
    @staticmethod
    def __wrap(java_value: __InstanceCreator) -> 'InstanceCreator':
        return InstanceCreator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InstanceCreator):
        """
        Dynamic initializer for InstanceCreator.
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
    def createInstance(self, arg0: 'Type'):
        """public abstract T com.google.gson.InstanceCreator.createInstance(java.lang.reflect.Type)"""
        pass 
 
 
# CLASS: com.google.gson.JsonPrimitive
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.gson.JsonObject as __JsonObject
__JsonObject = __JsonObject
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import com.google.gson.JsonArray as __JsonArray
__JsonArray = __JsonArray
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.google.gson.JsonNull as __JsonNull
__JsonNull = __JsonNull
import com.google.gson.JsonPrimitive as __JsonPrimitive
__JsonPrimitive = __JsonPrimitive
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
import java.lang.Character as Character
from builtins import bool
from builtins import int
 
class JsonPrimitive():
    """com.google.gson.JsonPrimitive"""
 
    @staticmethod
    def __wrap(java_value: __JsonPrimitive) -> 'JsonPrimitive':
        return JsonPrimitive(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonPrimitive):
        """
        Dynamic initializer for JsonPrimitive.
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
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool.__wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonPrimitive.getAsDouble()"""
        return float.__wrap(super(JsonPrimitive, self).getAsDouble())

    @overload
    def __init__(self, arg0: 'Character'):
        """public com.google.gson.JsonPrimitive(java.lang.Character)"""
        val = __JsonPrimitive(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isNumber(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.isNumber()"""
        return bool.__wrap(super(JsonPrimitive, self).isNumber())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonPrimitive.hashCode()"""
        return int.__wrap(super(JsonPrimitive, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isString(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.isString()"""
        return bool.__wrap(super(JsonPrimitive, self).isString())

    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonPrimitive.getAsBigInteger()"""
        return __transform(super(JsonPrimitive, self).getAsBigInteger()).'BigInteger'Value()

    @override
    @overload
    def deepCopy(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonPrimitive.deepCopy()"""
        return 'JsonPrimitive'.__wrap(super(JsonPrimitive, self).deepCopy())

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonPrimitive.getAsLong()"""
        return int.__wrap(super(JsonPrimitive, self).getAsLong())

    @overload
    def __init__(self, arg0: 'Boolean'):
        """public com.google.gson.JsonPrimitive(java.lang.Boolean)"""
        val = __JsonPrimitive(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonPrimitive.getAsFloat()"""
        return float.__wrap(super(JsonPrimitive, self).getAsFloat())

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'.__wrap(super(JsonElement, self).getAsJsonPrimitive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str.__wrap(super(JsonElement, self).toString())

    @overload
    def __init__(self, arg0: 'Number'):
        """public com.google.gson.JsonPrimitive(java.lang.Number)"""
        val = __JsonPrimitive(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.getAsBoolean()"""
        return bool.__wrap(super(JsonPrimitive, self).getAsBoolean())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonPrimitive.equals(java.lang.Object)"""
        return bool.__wrap(super(__JsonPrimitive, self).equals(arg0))

    @overload
    def isBoolean(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.isBoolean()"""
        return bool.__wrap(super(JsonPrimitive, self).isBoolean())

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonPrimitive.getAsCharacter()"""
        return str.__wrap(super(JsonPrimitive, self).getAsCharacter())

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonPrimitive.getAsString()"""
        return str.__wrap(super(JsonPrimitive, self).getAsString())

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonPrimitive.getAsShort()"""
        return int.__wrap(super(JsonPrimitive, self).getAsShort())

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool.__wrap(super(JsonElement, self).isJsonPrimitive())

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'.__wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'.__wrap(super(JsonElement, self).getAsJsonNull())

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
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonPrimitive.getAsBigDecimal()"""
        return __transform(super(JsonPrimitive, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonPrimitive.getAsByte()"""
        return int.__wrap(super(JsonPrimitive, self).getAsByte())

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonPrimitive.getAsInt()"""
        return int.__wrap(super(JsonPrimitive, self).getAsInt())

    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonPrimitive.getAsNumber()"""
        return __transform(super(JsonPrimitive, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool.__wrap(super(JsonElement, self).isJsonArray())

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'.__wrap(super(JsonElement, self).getAsJsonObject())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool.__wrap(super(JsonElement, self).isJsonObject())

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonPrimitive(java.lang.String)"""
        val = __JsonPrimitive(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.google.gson.LongSerializationPolicy
import com.google.gson.LongSerializationPolicy as __LongSerializationPolicy
__LongSerializationPolicy = __LongSerializationPolicy
from builtins import str
import java.lang.Long as Long
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from abc import abstractmethod, ABC
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class LongSerializationPolicy(ABC):
    """com.google.gson.LongSerializationPolicy"""
 
    @staticmethod
    def __wrap(java_value: __LongSerializationPolicy) -> 'LongSerializationPolicy':
        return LongSerializationPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongSerializationPolicy):
        """
        Dynamic initializer for LongSerializationPolicy.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'LongSerializationPolicy':
        """public static com.google.gson.LongSerializationPolicy com.google.gson.LongSerializationPolicy.valueOf(java.lang.String)"""
        return LongSerializationPolicy.__wrap(__LongSerializationPolicy.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def serialize(self, arg0: 'Long'):
        """public abstract com.google.gson.JsonElement com.google.gson.LongSerializationPolicy.serialize(java.lang.Long)"""
        pass

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['LongSerializationPolicy']:
        """public static com.google.gson.LongSerializationPolicy[] com.google.gson.LongSerializationPolicy.values()"""
        return List[LongSerializationPolicy].__wrap(__LongSerializationPolicy.values()) 
 
 
# CLASS: com.google.gson.JsonElement
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.gson.JsonObject as __JsonObject
__JsonObject = __JsonObject
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
from abc import abstractmethod, ABC
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import com.google.gson.JsonArray as __JsonArray
__JsonArray = __JsonArray
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.gson.JsonNull as __JsonNull
__JsonNull = __JsonNull
import com.google.gson.JsonPrimitive as __JsonPrimitive
__JsonPrimitive = __JsonPrimitive
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonElement(ABC):
    """com.google.gson.JsonElement"""
 
    @staticmethod
    def __wrap(java_value: __JsonElement) -> 'JsonElement':
        return JsonElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonElement):
        """
        Dynamic initializer for JsonElement.
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
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonElement.getAsInt()"""
        return int.__wrap(super(JsonElement, self).getAsInt())

    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonElement.getAsBoolean()"""
        return bool.__wrap(super(JsonElement, self).getAsBoolean())

    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.getAsString()"""
        return str.__wrap(super(JsonElement, self).getAsString())

    @overload
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool.__wrap(super(JsonElement, self).isJsonNull())

    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonElement.getAsShort()"""
        return int.__wrap(super(JsonElement, self).getAsShort())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonElement.getAsNumber()"""
        return __transform(super(JsonElement, self).getAsNumber()).'Number'Value()

    @abstractmethod
    def deepCopy(self, ):
        """public abstract com.google.gson.JsonElement com.google.gson.JsonElement.deepCopy()"""
        pass

    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonElement.getAsCharacter()"""
        return str.__wrap(super(JsonElement, self).getAsCharacter())

    @overload
    def __init__(self):
        """public com.google.gson.JsonElement()"""
        val = __JsonElement()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonElement.getAsLong()"""
        return int.__wrap(super(JsonElement, self).getAsLong())

    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool.__wrap(super(JsonElement, self).isJsonArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonElement()"""
        val = __JsonElement()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonElement.getAsBigInteger()"""
        return __transform(super(JsonElement, self).getAsBigInteger()).'BigInteger'Value()

    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool.__wrap(super(JsonElement, self).isJsonObject())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str.__wrap(super(JsonElement, self).toString())

    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'.__wrap(super(JsonElement, self).getAsJsonArray())

    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'.__wrap(super(JsonElement, self).getAsJsonNull())

    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonElement.getAsDouble()"""
        return float.__wrap(super(JsonElement, self).getAsDouble())

    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonElement.getAsByte()"""
        return int.__wrap(super(JsonElement, self).getAsByte())

    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonElement.getAsBigDecimal()"""
        return __transform(super(JsonElement, self).getAsBigDecimal()).'BigDecimal'Value()

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

    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonElement.getAsFloat()"""
        return float.__wrap(super(JsonElement, self).getAsFloat())

    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool.__wrap(super(JsonElement, self).isJsonPrimitive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'.__wrap(super(JsonElement, self).getAsJsonPrimitive())

    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'.__wrap(super(JsonElement, self).getAsJsonObject()) 
 
 
# CLASS: com.google.gson.ReflectionAccessFilter
import com.google.gson.ReflectionAccessFilter as __ReflectionAccessFilter
__ReflectionAccessFilter = __ReflectionAccessFilter
from builtins import type
from abc import abstractmethod, ABC
 
class ReflectionAccessFilter(ABC):
    """com.google.gson.ReflectionAccessFilter"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionAccessFilter) -> 'ReflectionAccessFilter':
        return ReflectionAccessFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionAccessFilter):
        """
        Dynamic initializer for ReflectionAccessFilter.
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
    def check(self, arg0: 'Class'):
        """public abstract com.google.gson.ReflectionAccessFilter$FilterResult com.google.gson.ReflectionAccessFilter.check(java.lang.Class<?>)"""
        pass 
 
 
# CLASS: com.google.gson.ReflectionAccessFilter$FilterResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import com.google.gson.ReflectionAccessFilter as __ReflectionAccessFilter_FilterResult
__FilterResult = __ReflectionAccessFilter_FilterResult.FilterResult
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class FilterResult():
    """com.google.gson.ReflectionAccessFilter.FilterResult"""
 
    @staticmethod
    def __wrap(java_value: __FilterResult) -> 'FilterResult':
        return FilterResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FilterResult):
        """
        Dynamic initializer for FilterResult.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def values() -> List['FilterResult']:
        """public static com.google.gson.ReflectionAccessFilter$FilterResult[] com.google.gson.ReflectionAccessFilter$FilterResult.values()"""
        return List[FilterResult].__wrap(__FilterResult.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FilterResult':
        """public static com.google.gson.ReflectionAccessFilter$FilterResult com.google.gson.ReflectionAccessFilter$FilterResult.valueOf(java.lang.String)"""
        return FilterResult.__wrap(__FilterResult.valueOf(arg0)) 
 
 
# CLASS: com.google.gson.JsonObject
from pyquantum_helper import transform as __transform
from builtins import type
import java.util.Map as __Map
__Map = __Map
import com.google.gson.JsonArray as __JsonArray
__JsonArray = __JsonArray
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.google.gson.JsonNull as __JsonNull
__JsonNull = __JsonNull
import com.google.gson.JsonPrimitive as __JsonPrimitive
__JsonPrimitive = __JsonPrimitive
import java.lang.Character as Character
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import float
import com.google.gson.JsonObject as __JsonObject
__JsonObject = __JsonObject
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.util.Set as Set
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class JsonObject():
    """com.google.gson.JsonObject"""
 
    @staticmethod
    def __wrap(java_value: __JsonObject) -> 'JsonObject':
        return JsonObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonObject):
        """
        Dynamic initializer for JsonObject.
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
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool.__wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def deepCopy(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonObject.deepCopy()"""
        return 'JsonObject'.__wrap(super(JsonObject, self).deepCopy())

    @overload
    def getAsJsonObject(self, arg0: str) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonObject.getAsJsonObject(java.lang.String)"""
        return 'JsonObject'.__wrap(super(__JsonObject, self).getAsJsonObject(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonElement.getAsDouble()"""
        return float.__wrap(super(JsonElement, self).getAsDouble())

    @overload
    def addProperty(self, arg0: str, arg1: 'Boolean'):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.Boolean)"""
        super(__JsonObject, self).addProperty(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonObject.hashCode()"""
        return int.__wrap(super(JsonObject, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonObject.equals(java.lang.Object)"""
        return bool.__wrap(super(__JsonObject, self).equals(arg0))

    @overload
    def addProperty(self, arg0: str, arg1: 'Character'):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.Character)"""
        super(__JsonObject, self).addProperty(arg0, arg1)

    @overload
    def getAsJsonArray(self, arg0: str) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonObject.getAsJsonArray(java.lang.String)"""
        return 'JsonArray'.__wrap(super(__JsonObject, self).getAsJsonArray(arg0))

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonElement.getAsCharacter()"""
        return str.__wrap(super(JsonElement, self).getAsCharacter())

    @overload
    def addProperty(self, arg0: str, arg1: 'Number'):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.Number)"""
        super(__JsonObject, self).addProperty(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonObject()"""
        val = __JsonObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonElement.getAsBigInteger()"""
        return __transform(super(JsonElement, self).getAsBigInteger()).'BigInteger'Value()

    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonElement.getAsNumber()"""
        return __transform(super(JsonElement, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonElement.getAsByte()"""
        return int.__wrap(super(JsonElement, self).getAsByte())

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.getAsString()"""
        return str.__wrap(super(JsonElement, self).getAsString())

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'.__wrap(super(JsonElement, self).getAsJsonPrimitive())

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonElement.getAsInt()"""
        return int.__wrap(super(JsonElement, self).getAsInt())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str.__wrap(super(JsonElement, self).toString())

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonElement.getAsLong()"""
        return int.__wrap(super(JsonElement, self).getAsLong())

    @overload
    def remove(self, arg0: str) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonObject.remove(java.lang.String)"""
        return 'JsonElement'.__wrap(super(__JsonObject, self).remove(arg0))

    @overload
    def addProperty(self, arg0: str, arg1: str):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.String)"""
        super(__JsonObject, self).addProperty(arg0, arg1)

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool.__wrap(super(JsonElement, self).isJsonPrimitive())

    @overload
    def has(self, arg0: str) -> bool:
        """public boolean com.google.gson.JsonObject.has(java.lang.String)"""
        return bool.__wrap(super(__JsonObject, self).has(arg0))

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonElement.getAsBoolean()"""
        return bool.__wrap(super(JsonElement, self).getAsBoolean())

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'.__wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'.__wrap(super(JsonElement, self).getAsJsonNull())

    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<java.lang.String, com.google.gson.JsonElement>> com.google.gson.JsonObject.entrySet()"""
        return 'Set'.__wrap(super(JsonObject, self).entrySet())

    @overload
    def get(self, arg0: str) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonObject.get(java.lang.String)"""
        return 'JsonElement'.__wrap(super(__JsonObject, self).get(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonElement.getAsBigDecimal()"""
        return __transform(super(JsonElement, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonElement.getAsShort()"""
        return int.__wrap(super(JsonElement, self).getAsShort())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.gson.JsonObject.isEmpty()"""
        return bool.__wrap(super(JsonObject, self).isEmpty())

    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, com.google.gson.JsonElement> com.google.gson.JsonObject.asMap()"""
        return 'Map'.__wrap(super(JsonObject, self).asMap())

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonElement.getAsFloat()"""
        return float.__wrap(super(JsonElement, self).getAsFloat())

    @overload
    def add(self, arg0: str, arg1: 'JsonElement'):
        """public void com.google.gson.JsonObject.add(java.lang.String,com.google.gson.JsonElement)"""
        super(__JsonObject, self).add(arg0, arg1)

    @override
    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool.__wrap(super(JsonElement, self).isJsonArray())

    @overload
    def size(self) -> int:
        """public int com.google.gson.JsonObject.size()"""
        return int.__wrap(super(JsonObject, self).size())

    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<java.lang.String> com.google.gson.JsonObject.keySet()"""
        return 'Set'.__wrap(super(JsonObject, self).keySet())

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'.__wrap(super(JsonElement, self).getAsJsonObject())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.gson.JsonObject()"""
        val = __JsonObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAsJsonPrimitive(self, arg0: str) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonObject.getAsJsonPrimitive(java.lang.String)"""
        return 'JsonPrimitive'.__wrap(super(__JsonObject, self).getAsJsonPrimitive(arg0))

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool.__wrap(super(JsonElement, self).isJsonObject()) 
 
 
# CLASS: com.google.gson.JsonParser
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import com.google.gson.JsonParser as __JsonParser
__JsonParser = __JsonParser
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class JsonParser():
    """com.google.gson.JsonParser"""
 
    @staticmethod
    def __wrap(java_value: __JsonParser) -> 'JsonParser':
        return JsonParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonParser):
        """
        Dynamic initializer for JsonParser.
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
    def parse(self, arg0: 'Reader') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonParser.parse(java.io.Reader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return 'JsonElement'.__wrap(super(__JsonParser, self).parse(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def parseString(arg0: str) -> 'JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.JsonParser.parseString(java.lang.String) throws com.google.gson.JsonSyntaxException"""
        return JsonElement.__wrap(__JsonParser.parseString(arg0))

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonParser()"""
        val = __JsonParser()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parseReader(arg0: 'Reader') -> 'JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.JsonParser.parseReader(java.io.Reader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return JsonElement.__wrap(__JsonParser.parseReader(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def parseReader(arg0: 'JsonReader') -> 'JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.JsonParser.parseReader(com.google.gson.stream.JsonReader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return JsonElement.__wrap(__JsonParser.parseReader(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.JsonParser()"""
        val = __JsonParser()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def parse(self, arg0: 'JsonReader') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonParser.parse(com.google.gson.stream.JsonReader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return 'JsonElement'.__wrap(super(__JsonParser, self).parse(arg0))

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

    @overload
    def parse(self, arg0: str) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonParser.parse(java.lang.String) throws com.google.gson.JsonSyntaxException"""
        return 'JsonElement'.__wrap(super(__JsonParser, self).parse(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.GsonBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as Type
import com.google.gson.GsonBuilder as __GsonBuilder
__GsonBuilder = __GsonBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.google.gson.Gson as __Gson
__Gson = __Gson
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GsonBuilder():
    """com.google.gson.GsonBuilder"""
 
    @staticmethod
    def __wrap(java_value: __GsonBuilder) -> 'GsonBuilder':
        return GsonBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GsonBuilder):
        """
        Dynamic initializer for GsonBuilder.
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
    def enableComplexMapKeySerialization(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.enableComplexMapKeySerialization()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).enableComplexMapKeySerialization())

    @overload
    def registerTypeAdapter(self, arg0: 'Type', arg1: object) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.registerTypeAdapter(java.lang.reflect.Type,java.lang.Object)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).registerTypeAdapter(arg0, arg1))

    @overload
    def setObjectToNumberStrategy(self, arg0: 'ToNumberStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setObjectToNumberStrategy(com.google.gson.ToNumberStrategy)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setObjectToNumberStrategy(arg0))

    @overload
    def addReflectionAccessFilter(self, arg0: 'ReflectionAccessFilter') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.addReflectionAccessFilter(com.google.gson.ReflectionAccessFilter)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).addReflectionAccessFilter(arg0))

    @overload
    def disableInnerClassSerialization(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.disableInnerClassSerialization()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).disableInnerClassSerialization())

    @overload
    def setDateFormat(self, arg0: int, arg1: int) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setDateFormat(int,int)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setDateFormat(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def create(self) -> 'Gson':
        """public com.google.gson.Gson com.google.gson.GsonBuilder.create()"""
        return 'Gson'.__wrap(super(GsonBuilder, self).create())

    @overload
    def generateNonExecutableJson(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.generateNonExecutableJson()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).generateNonExecutableJson())

    @overload
    def setExclusionStrategies(self, *arg0: 'ExclusionStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setExclusionStrategies(com.google.gson.ExclusionStrategy...)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setExclusionStrategies(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.GsonBuilder()"""
        val = __GsonBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def serializeNulls(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.serializeNulls()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).serializeNulls())

    @overload
    def serializeSpecialFloatingPointValues(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.serializeSpecialFloatingPointValues()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).serializeSpecialFloatingPointValues())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def disableJdkUnsafe(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.disableJdkUnsafe()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).disableJdkUnsafe())

    @overload
    def disableHtmlEscaping(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.disableHtmlEscaping()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).disableHtmlEscaping())

    @overload
    def setPrettyPrinting(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setPrettyPrinting()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).setPrettyPrinting())

    @overload
    def setFieldNamingStrategy(self, arg0: 'FieldNamingStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setFieldNamingStrategy(com.google.gson.FieldNamingStrategy)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setFieldNamingStrategy(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def excludeFieldsWithModifiers(self, *arg0: int) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.excludeFieldsWithModifiers(int...)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).excludeFieldsWithModifiers(arg0))

    @overload
    def registerTypeAdapterFactory(self, arg0: 'TypeAdapterFactory') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.registerTypeAdapterFactory(com.google.gson.TypeAdapterFactory)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).registerTypeAdapterFactory(arg0))

    @overload
    def addSerializationExclusionStrategy(self, arg0: 'ExclusionStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.addSerializationExclusionStrategy(com.google.gson.ExclusionStrategy)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).addSerializationExclusionStrategy(arg0))

    @overload
    def excludeFieldsWithoutExposeAnnotation(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.excludeFieldsWithoutExposeAnnotation()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).excludeFieldsWithoutExposeAnnotation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setLenient(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setLenient()"""
        return 'GsonBuilder'.__wrap(super(GsonBuilder, self).setLenient())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setDateFormat(self, arg0: str) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setDateFormat(java.lang.String)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setDateFormat(arg0))

    @overload
    def __init__(self, ):
        """public com.google.gson.GsonBuilder()"""
        val = __GsonBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setNumberToNumberStrategy(self, arg0: 'ToNumberStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setNumberToNumberStrategy(com.google.gson.ToNumberStrategy)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setNumberToNumberStrategy(arg0))

    @overload
    def setLongSerializationPolicy(self, arg0: 'LongSerializationPolicy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setLongSerializationPolicy(com.google.gson.LongSerializationPolicy)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setLongSerializationPolicy(arg0))

    @overload
    def setDateFormat(self, arg0: int) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setDateFormat(int)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setDateFormat(__int.valueOf(arg0)))

    @overload
    def setVersion(self, arg0: float) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setVersion(double)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setVersion(__double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setFieldNamingPolicy(self, arg0: 'FieldNamingPolicy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setFieldNamingPolicy(com.google.gson.FieldNamingPolicy)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).setFieldNamingPolicy(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def registerTypeHierarchyAdapter(self, arg0: 'Class', arg1: object) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.registerTypeHierarchyAdapter(java.lang.Class<?>,java.lang.Object)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).registerTypeHierarchyAdapter(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addDeserializationExclusionStrategy(self, arg0: 'ExclusionStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.addDeserializationExclusionStrategy(com.google.gson.ExclusionStrategy)"""
        return 'GsonBuilder'.__wrap(super(__GsonBuilder, self).addDeserializationExclusionStrategy(arg0)) 
 
 
# CLASS: com.google.gson.ToNumberStrategy
from pyquantum_helper import import_once as __import_once__
import com.google.gson.ToNumberStrategy as __ToNumberStrategy
__ToNumberStrategy = __ToNumberStrategy
from abc import abstractmethod, ABC
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

 
class ToNumberStrategy(ABC):
    """com.google.gson.ToNumberStrategy"""
 
    @staticmethod
    def __wrap(java_value: __ToNumberStrategy) -> 'ToNumberStrategy':
        return ToNumberStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToNumberStrategy):
        """
        Dynamic initializer for ToNumberStrategy.
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
    def readNumber(self, arg0: 'JsonReader'):
        """public abstract java.lang.Number com.google.gson.ToNumberStrategy.readNumber(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass 
 
 
# CLASS: com.google.gson.TypeAdapter
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
from abc import abstractmethod, ABC
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class TypeAdapter(ABC):
    """com.google.gson.TypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __TypeAdapter) -> 'TypeAdapter':
        return TypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeAdapter):
        """
        Dynamic initializer for TypeAdapter.
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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__TypeAdapter, self).fromJsonTree(arg0))

    @overload
    def nullSafe(self) -> 'TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'TypeAdapter'.__wrap(super(TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'JsonElement'.__wrap(super(__TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.google.gson.TypeAdapter()"""
        val = __TypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.google.gson.TypeAdapter()"""
        val = __TypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__TypeAdapter, self).toJson(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public abstract void com.google.gson.TypeAdapter.write(com.google.gson.stream.JsonWriter,T) throws java.io.IOException"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def read(self, arg0: 'JsonReader'):
        """public abstract T com.google.gson.TypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__TypeAdapter, self).fromJson(arg0))

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__TypeAdapter, self).fromJson(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.FieldAttributes
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Field as Field
import java.util.Collection as Collection
import java.lang.reflect.Type as Type
import java.lang.annotation.Annotation as Annotation
import com.google.gson.FieldAttributes as __FieldAttributes
__FieldAttributes = __FieldAttributes
import java.util.Collection as __Collection
__Collection = __Collection
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
 
class FieldAttributes():
    """com.google.gson.FieldAttributes"""
 
    @staticmethod
    def __wrap(java_value: __FieldAttributes) -> 'FieldAttributes':
        return FieldAttributes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldAttributes):
        """
        Dynamic initializer for FieldAttributes.
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
        """public java.lang.String com.google.gson.FieldAttributes.toString()"""
        return str.__wrap(super(FieldAttributes, self).toString())

    @overload
    def __init__(self, arg0: 'Field'):
        """public com.google.gson.FieldAttributes(java.lang.reflect.Field)"""
        val = __FieldAttributes(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class<?> com.google.gson.FieldAttributes.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(FieldAttributes, self).getDeclaringClass())

    @overload
    def getDeclaredType(self) -> 'Type':
        """public java.lang.reflect.Type com.google.gson.FieldAttributes.getDeclaredType()"""
        return 'Type'.__wrap(super(FieldAttributes, self).getDeclaredType())

    @overload
    def hasModifier(self, arg0: int) -> bool:
        """public boolean com.google.gson.FieldAttributes.hasModifier(int)"""
        return bool.__wrap(super(__FieldAttributes, self).hasModifier(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getName(self) -> str:
        """public java.lang.String com.google.gson.FieldAttributes.getName()"""
        return str.__wrap(super(FieldAttributes, self).getName())

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

    @overload
    def getDeclaredClass(self) -> 'type.Class':
        """public java.lang.Class<?> com.google.gson.FieldAttributes.getDeclaredClass()"""
        return 'type.Class'.__wrap(super(FieldAttributes, self).getDeclaredClass())

    @overload
    def getAnnotations(self) -> 'Collection':
        """public java.util.Collection<java.lang.annotation.Annotation> com.google.gson.FieldAttributes.getAnnotations()"""
        return 'Collection'.__wrap(super(FieldAttributes, self).getAnnotations())

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
    def getAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public <T extends java.lang.annotation.Annotation> T com.google.gson.FieldAttributes.getAnnotation(java.lang.Class<T>)"""
        return 'Annotation'.__wrap(super(__FieldAttributes, self).getAnnotation(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.JsonArray
from pyquantum_helper import transform as __transform
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import com.google.gson.JsonArray as __JsonArray
__JsonArray = __JsonArray
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.google.gson.JsonNull as __JsonNull
__JsonNull = __JsonNull
import com.google.gson.JsonPrimitive as __JsonPrimitive
__JsonPrimitive = __JsonPrimitive
import java.lang.Character as Character
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import float
import com.google.gson.JsonObject as __JsonObject
__JsonObject = __JsonObject
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.List as __List
__List = __List
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class JsonArray():
    """com.google.gson.JsonArray"""
 
    @staticmethod
    def __wrap(java_value: __JsonArray) -> 'JsonArray':
        return JsonArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonArray):
        """
        Dynamic initializer for JsonArray.
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
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonArray.getAsDouble()"""
        return float.__wrap(super(JsonArray, self).getAsDouble())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public com.google.gson.JsonArray(int)"""
        val = __JsonArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'Number'):
        """public void com.google.gson.JsonArray.add(java.lang.Number)"""
        super(__JsonArray, self).add(arg0)

    @overload
    def asList(self) -> 'List':
        """public java.util.List<com.google.gson.JsonElement> com.google.gson.JsonArray.asList()"""
        return 'List'.__wrap(super(JsonArray, self).asList())

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonArray.getAsBoolean()"""
        return bool.__wrap(super(JsonArray, self).getAsBoolean())

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'.__wrap(super(JsonElement, self).getAsJsonPrimitive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str.__wrap(super(JsonElement, self).toString())

    @overload
    def contains(self, arg0: 'JsonElement') -> bool:
        """public boolean com.google.gson.JsonArray.contains(com.google.gson.JsonElement)"""
        return bool.__wrap(super(__JsonArray, self).contains(arg0))

    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonArray.getAsNumber()"""
        return __transform(super(JsonArray, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'.__wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'.__wrap(super(JsonElement, self).getAsJsonNull())

    @override
    @overload
    def deepCopy(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonArray.deepCopy()"""
        return 'JsonArray'.__wrap(super(JsonArray, self).deepCopy())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.google.gson.JsonElement> com.google.gson.JsonArray.iterator()"""
        return 'Iterator'.__wrap(super(JsonArray, self).iterator())

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonArray.getAsInt()"""
        return int.__wrap(super(JsonArray, self).getAsInt())

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonArray()"""
        val = __JsonArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonArray.get(int)"""
        return 'JsonElement'.__wrap(super(__JsonArray, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'.__wrap(super(JsonElement, self).getAsJsonObject())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonArray.getAsByte()"""
        return int.__wrap(super(JsonArray, self).getAsByte())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool.__wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonArray.hashCode()"""
        return int.__wrap(super(JsonArray, self).hashCode())

    @overload
    def remove(self, arg0: int) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonArray.remove(int)"""
        return 'JsonElement'.__wrap(super(__JsonArray, self).remove(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__JsonArray, self).equals(arg0))

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonArray.getAsFloat()"""
        return float.__wrap(super(JsonArray, self).getAsFloat())

    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonArray.getAsBigInteger()"""
        return __transform(super(JsonArray, self).getAsBigInteger()).'BigInteger'Value()

    @overload
    def size(self) -> int:
        """public int com.google.gson.JsonArray.size()"""
        return int.__wrap(super(JsonArray, self).size())

    @overload
    def remove(self, arg0: 'JsonElement') -> bool:
        """public boolean com.google.gson.JsonArray.remove(com.google.gson.JsonElement)"""
        return bool.__wrap(super(__JsonArray, self).remove(arg0))

    @overload
    def add(self, arg0: 'JsonElement'):
        """public void com.google.gson.JsonArray.add(com.google.gson.JsonElement)"""
        super(__JsonArray, self).add(arg0)

    @overload
    def __init__(self):
        """public com.google.gson.JsonArray()"""
        val = __JsonArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: 'JsonElement') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonArray.set(int,com.google.gson.JsonElement)"""
        return 'JsonElement'.__wrap(super(__JsonArray, self).set(__int.valueOf(arg0), arg1))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.gson.JsonArray.isEmpty()"""
        return bool.__wrap(super(JsonArray, self).isEmpty())

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonArray.getAsString()"""
        return str.__wrap(super(JsonArray, self).getAsString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def addAll(self, arg0: 'JsonArray'):
        """public void com.google.gson.JsonArray.addAll(com.google.gson.JsonArray)"""
        super(__JsonArray, self).addAll(arg0)

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonArray.getAsLong()"""
        return int.__wrap(super(JsonArray, self).getAsLong())

    @override
    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonArray.getAsBigDecimal()"""
        return __transform(super(JsonArray, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonArray.getAsShort()"""
        return int.__wrap(super(JsonArray, self).getAsShort())

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool.__wrap(super(JsonElement, self).isJsonPrimitive())

    @overload
    def add(self, arg0: 'Boolean'):
        """public void com.google.gson.JsonArray.add(java.lang.Boolean)"""
        super(__JsonArray, self).add(arg0)

    @overload
    def add(self, arg0: str):
        """public void com.google.gson.JsonArray.add(java.lang.String)"""
        super(__JsonArray, self).add(arg0)

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
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool.__wrap(super(JsonElement, self).isJsonArray())

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonArray.getAsCharacter()"""
        return str.__wrap(super(JsonArray, self).getAsCharacter())

    @overload
    def add(self, arg0: 'Character'):
        """public void com.google.gson.JsonArray.add(java.lang.Character)"""
        super(__JsonArray, self).add(arg0)

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool.__wrap(super(JsonElement, self).isJsonObject()) 
 
 
# CLASS: com.google.gson.FieldNamingPolicy
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import java.lang.reflect.Field as Field
from abc import abstractmethod, ABC
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.google.gson.FieldNamingPolicy as __FieldNamingPolicy
__FieldNamingPolicy = __FieldNamingPolicy
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.google.gson.FieldNamingStrategy as __FieldNamingStrategy
__FieldNamingStrategy = __FieldNamingStrategy
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class FieldNamingPolicy(ABC):
    """com.google.gson.FieldNamingPolicy"""
 
    @staticmethod
    def __wrap(java_value: __FieldNamingPolicy) -> 'FieldNamingPolicy':
        return FieldNamingPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldNamingPolicy):
        """
        Dynamic initializer for FieldNamingPolicy.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FieldNamingPolicy':
        """public static com.google.gson.FieldNamingPolicy com.google.gson.FieldNamingPolicy.valueOf(java.lang.String)"""
        return FieldNamingPolicy.__wrap(__FieldNamingPolicy.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @abstractmethod
    def translateName(self, arg0: 'Field'):
        """public abstract java.lang.String com.google.gson.FieldNamingStrategy.translateName(java.lang.reflect.Field)"""
        pass

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['FieldNamingPolicy']:
        """public static com.google.gson.FieldNamingPolicy[] com.google.gson.FieldNamingPolicy.values()"""
        return List[FieldNamingPolicy].__wrap(__FieldNamingPolicy.values()) 
 
 
# CLASS: com.google.gson.JsonSyntaxException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import com.google.gson.JsonSyntaxException as __JsonSyntaxException
__JsonSyntaxException = __JsonSyntaxException
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonSyntaxException():
    """com.google.gson.JsonSyntaxException"""
 
    @staticmethod
    def __wrap(java_value: __JsonSyntaxException) -> 'JsonSyntaxException':
        return JsonSyntaxException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonSyntaxException):
        """
        Dynamic initializer for JsonSyntaxException.
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
    def __init__(self, arg0: str):
        """public com.google.gson.JsonSyntaxException(java.lang.String)"""
        val = __JsonSyntaxException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.JsonSyntaxException(java.lang.String,java.lang.Throwable)"""
        val = __JsonSyntaxException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.JsonSyntaxException(java.lang.Throwable)"""
        val = __JsonSyntaxException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.google.gson.TypeAdapterFactory
from pyquantum_helper import import_once as __import_once__
import com.google.gson.TypeAdapterFactory as __TypeAdapterFactory
__TypeAdapterFactory = __TypeAdapterFactory
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

from abc import abstractmethod, ABC
 
class TypeAdapterFactory(ABC):
    """com.google.gson.TypeAdapterFactory"""
 
    @staticmethod
    def __wrap(java_value: __TypeAdapterFactory) -> 'TypeAdapterFactory':
        return TypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeAdapterFactory):
        """
        Dynamic initializer for TypeAdapterFactory.
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
    def create(self, arg0: 'Gson', arg1: 'TypeToken'):
        """public abstract <T> com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        pass 
 
 
# CLASS: com.google.gson.ExclusionStrategy
import com.google.gson.ExclusionStrategy as __ExclusionStrategy
__ExclusionStrategy = __ExclusionStrategy
from builtins import type
from abc import abstractmethod, ABC
 
class ExclusionStrategy(ABC):
    """com.google.gson.ExclusionStrategy"""
 
    @staticmethod
    def __wrap(java_value: __ExclusionStrategy) -> 'ExclusionStrategy':
        return ExclusionStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExclusionStrategy):
        """
        Dynamic initializer for ExclusionStrategy.
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
    def shouldSkipClass(self, arg0: 'Class'):
        """public abstract boolean com.google.gson.ExclusionStrategy.shouldSkipClass(java.lang.Class<?>)"""
        pass

    @abstractmethod
    def shouldSkipField(self, arg0: 'FieldAttributes'):
        """public abstract boolean com.google.gson.ExclusionStrategy.shouldSkipField(com.google.gson.FieldAttributes)"""
        pass 
 
 
# CLASS: com.google.gson.JsonParseException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import com.google.gson.JsonParseException as __JsonParseException
__JsonParseException = __JsonParseException
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonParseException():
    """com.google.gson.JsonParseException"""
 
    @staticmethod
    def __wrap(java_value: __JsonParseException) -> 'JsonParseException':
        return JsonParseException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonParseException):
        """
        Dynamic initializer for JsonParseException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.JsonParseException(java.lang.String,java.lang.Throwable)"""
        val = __JsonParseException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonParseException(java.lang.String)"""
        val = __JsonParseException(arg0)
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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.JsonParseException(java.lang.Throwable)"""
        val = __JsonParseException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.google.gson.JsonSerializationContext
import com.google.gson.JsonSerializationContext as __JsonSerializationContext
__JsonSerializationContext = __JsonSerializationContext
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
 
class JsonSerializationContext(ABC):
    """com.google.gson.JsonSerializationContext"""
 
    @staticmethod
    def __wrap(java_value: __JsonSerializationContext) -> 'JsonSerializationContext':
        return JsonSerializationContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonSerializationContext):
        """
        Dynamic initializer for JsonSerializationContext.
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
    def serialize(self, arg0: object):
        """public abstract com.google.gson.JsonElement com.google.gson.JsonSerializationContext.serialize(java.lang.Object)"""
        pass

    @abstractmethod
    def serialize(self, arg0: object, arg1: 'Type'):
        """public abstract com.google.gson.JsonElement com.google.gson.JsonSerializationContext.serialize(java.lang.Object,java.lang.reflect.Type)"""
        pass 
 
 
# CLASS: com.google.gson.JsonSerializer
import com.google.gson.JsonSerializer as __JsonSerializer
__JsonSerializer = __JsonSerializer
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
 
class JsonSerializer(ABC):
    """com.google.gson.JsonSerializer"""
 
    @staticmethod
    def __wrap(java_value: __JsonSerializer) -> 'JsonSerializer':
        return JsonSerializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonSerializer):
        """
        Dynamic initializer for JsonSerializer.
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
    def serialize(self, arg0: object, arg1: 'Type', arg2: 'JsonSerializationContext'):
        """public abstract com.google.gson.JsonElement com.google.gson.JsonSerializer.serialize(T,java.lang.reflect.Type,com.google.gson.JsonSerializationContext)"""
        pass 
 
 
# CLASS: com.google.gson.JsonIOException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import com.google.gson.JsonIOException as __JsonIOException
__JsonIOException = __JsonIOException
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonIOException():
    """com.google.gson.JsonIOException"""
 
    @staticmethod
    def __wrap(java_value: __JsonIOException) -> 'JsonIOException':
        return JsonIOException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonIOException):
        """
        Dynamic initializer for JsonIOException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.JsonIOException(java.lang.Throwable)"""
        val = __JsonIOException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonIOException(java.lang.String)"""
        val = __JsonIOException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.JsonIOException(java.lang.String,java.lang.Throwable)"""
        val = __JsonIOException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.google.gson.ToNumberPolicy
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.ToNumberStrategy as __ToNumberStrategy
__ToNumberStrategy = __ToNumberStrategy
import java.util.Optional as __Optional
__Optional = __Optional
from abc import abstractmethod, ABC
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

import com.google.gson.ToNumberPolicy as __ToNumberPolicy
__ToNumberPolicy = __ToNumberPolicy
from builtins import int
 
class ToNumberPolicy(ABC):
    """com.google.gson.ToNumberPolicy"""
 
    @staticmethod
    def __wrap(java_value: __ToNumberPolicy) -> 'ToNumberPolicy':
        return ToNumberPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToNumberPolicy):
        """
        Dynamic initializer for ToNumberPolicy.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ToNumberPolicy':
        """public static com.google.gson.ToNumberPolicy com.google.gson.ToNumberPolicy.valueOf(java.lang.String)"""
        return ToNumberPolicy.__wrap(__ToNumberPolicy.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['ToNumberPolicy']:
        """public static com.google.gson.ToNumberPolicy[] com.google.gson.ToNumberPolicy.values()"""
        return List[ToNumberPolicy].__wrap(__ToNumberPolicy.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def readNumber(self, arg0: 'JsonReader'):
        """public abstract java.lang.Number com.google.gson.ToNumberStrategy.readNumber(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.google.gson.Gson
from pyquantum_helper import import_once as __import_once__
from builtins import type
import com.google.gson.internal.Excluder as __Excluder
__Excluder = __Excluder
import java.lang.reflect.Type as Type
import com.google.gson.GsonBuilder as __GsonBuilder
__GsonBuilder = __GsonBuilder
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.google.gson.Gson as __Gson
__Gson = __Gson
import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.gson.stream.JsonReader as __JsonReader
__JsonReader = __JsonReader
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
from builtins import object
try:
    from pygson import internal
except ImportError:
    internal = __import_once__("pygson.internal")

import java.lang.Appendable as Appendable
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import com.google.gson.FieldNamingStrategy as __FieldNamingStrategy
__FieldNamingStrategy = __FieldNamingStrategy
import com.google.gson.stream.JsonWriter as __JsonWriter
__JsonWriter = __JsonWriter
import java.lang.Integer as __int
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class Gson():
    """com.google.gson.Gson"""
 
    @staticmethod
    def __wrap(java_value: __Gson) -> 'Gson':
        return Gson(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Gson):
        """
        Dynamic initializer for Gson.
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
    def fromJson(self, arg0: 'JsonElement', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,java.lang.reflect.Type) throws com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,java.lang.reflect.Type) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toJsonTree(self, arg0: object) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.Gson.toJsonTree(java.lang.Object)"""
        return 'JsonElement'.__wrap(super(__Gson, self).toJsonTree(arg0))

    @overload
    def toJson(self, arg0: object, arg1: 'Type', arg2: 'JsonWriter'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type,com.google.gson.stream.JsonWriter) throws com.google.gson.JsonIOException"""
        super(__Gson, self).toJson(arg0, arg1, arg2)

    @overload
    def excluder(self) -> 'internal.Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.Gson.excluder()"""
        return 'internal.Excluder'.__wrap(super(Gson, self).excluder())

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException,com.google.gson.JsonIOException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def fromJson(self, arg0: str, arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,java.lang.reflect.Type) throws com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def fromJson(self, arg0: str, arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: 'JsonElement', arg1: 'Appendable'):
        """public void com.google.gson.Gson.toJson(com.google.gson.JsonElement,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(__Gson, self).toJson(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def htmlSafe(self) -> bool:
        """public boolean com.google.gson.Gson.htmlSafe()"""
        return bool.__wrap(super(Gson, self).htmlSafe())

    @overload
    def fieldNamingStrategy(self) -> 'FieldNamingStrategy':
        """public com.google.gson.FieldNamingStrategy com.google.gson.Gson.fieldNamingStrategy()"""
        return 'FieldNamingStrategy'.__wrap(super(Gson, self).fieldNamingStrategy())

    @overload
    def toJson(self, arg0: 'JsonElement') -> str:
        """public java.lang.String com.google.gson.Gson.toJson(com.google.gson.JsonElement)"""
        return str.__wrap(super(__Gson, self).toJson(arg0))

    @overload
    def getAdapter(self, arg0: 'TypeToken') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getAdapter(com.google.gson.reflect.TypeToken<T>)"""
        return 'TypeAdapter'.__wrap(super(__Gson, self).getAdapter(arg0))

    @overload
    def toJson(self, arg0: object) -> str:
        """public java.lang.String com.google.gson.Gson.toJson(java.lang.Object)"""
        return str.__wrap(super(__Gson, self).toJson(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def fromJson(self, arg0: 'JsonReader', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.stream.JsonReader,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: 'JsonElement', arg1: 'JsonWriter'):
        """public void com.google.gson.Gson.toJson(com.google.gson.JsonElement,com.google.gson.stream.JsonWriter) throws com.google.gson.JsonIOException"""
        super(__Gson, self).toJson(arg0, arg1)

    @overload
    def getDelegateAdapter(self, arg0: 'TypeAdapterFactory', arg1: 'TypeToken') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getDelegateAdapter(com.google.gson.TypeAdapterFactory,com.google.gson.reflect.TypeToken<T>)"""
        return 'TypeAdapter'.__wrap(super(__Gson, self).getDelegateAdapter(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.Gson.toString()"""
        return str.__wrap(super(Gson, self).toString())

    @overload
    def toJson(self, arg0: object, arg1: 'Type', arg2: 'Appendable'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(__Gson, self).toJson(arg0, arg1, arg2)

    @overload
    def fromJson(self, arg0: str, arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def newJsonWriter(self, arg0: 'Writer') -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.Gson.newJsonWriter(java.io.Writer) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__Gson, self).newJsonWriter(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toJson(self, arg0: object, arg1: 'Appendable'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(__Gson, self).toJson(arg0, arg1)

    @overload
    def toJson(self, arg0: object, arg1: 'Type') -> str:
        """public java.lang.String com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type)"""
        return str.__wrap(super(__Gson, self).toJson(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'JsonReader', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.stream.JsonReader,java.lang.reflect.Type) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object.__wrap(super(__Gson, self).fromJson(arg0, arg1))

    @overload
    def toJsonTree(self, arg0: object, arg1: 'Type') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.Gson.toJsonTree(java.lang.Object,java.lang.reflect.Type)"""
        return 'JsonElement'.__wrap(super(__Gson, self).toJsonTree(arg0, arg1))

    @overload
    def newJsonReader(self, arg0: 'Reader') -> 'stream.JsonReader':
        """public com.google.gson.stream.JsonReader com.google.gson.Gson.newJsonReader(java.io.Reader)"""
        return 'stream.JsonReader'.__wrap(super(__Gson, self).newJsonReader(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.Gson()"""
        val = __Gson()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newBuilder(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.Gson.newBuilder()"""
        return 'GsonBuilder'.__wrap(super(Gson, self).newBuilder())

    @overload
    def serializeNulls(self) -> bool:
        """public boolean com.google.gson.Gson.serializeNulls()"""
        return bool.__wrap(super(Gson, self).serializeNulls())

    @overload
    def getAdapter(self, arg0: 'Class') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getAdapter(java.lang.Class<T>)"""
        return 'TypeAdapter'.__wrap(super(__Gson, self).getAdapter(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.gson.Gson()"""
        val = __Gson()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.google.gson.JsonDeserializationContext
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
import com.google.gson.JsonDeserializationContext as __JsonDeserializationContext
__JsonDeserializationContext = __JsonDeserializationContext
 
class JsonDeserializationContext(ABC):
    """com.google.gson.JsonDeserializationContext"""
 
    @staticmethod
    def __wrap(java_value: __JsonDeserializationContext) -> 'JsonDeserializationContext':
        return JsonDeserializationContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonDeserializationContext):
        """
        Dynamic initializer for JsonDeserializationContext.
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
    def deserialize(self, arg0: 'JsonElement', arg1: 'Type'):
        """public abstract <T> T com.google.gson.JsonDeserializationContext.deserialize(com.google.gson.JsonElement,java.lang.reflect.Type) throws com.google.gson.JsonParseException"""
        pass 
 
 
# CLASS: com.google.gson.JsonNull
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.gson.JsonObject as __JsonObject
__JsonObject = __JsonObject
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import com.google.gson.JsonArray as __JsonArray
__JsonArray = __JsonArray
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.gson.JsonNull as __JsonNull
__JsonNull = __JsonNull
import com.google.gson.JsonPrimitive as __JsonPrimitive
__JsonPrimitive = __JsonPrimitive
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonNull():
    """com.google.gson.JsonNull"""
 
    @staticmethod
    def __wrap(java_value: __JsonNull) -> 'JsonNull':
        return JsonNull(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonNull):
        """
        Dynamic initializer for JsonNull.
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
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool.__wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonNull.hashCode()"""
        return int.__wrap(super(JsonNull, self).hashCode())

    @overload
    def __init__(self):
        """public com.google.gson.JsonNull()"""
        val = __JsonNull()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonElement.getAsDouble()"""
        return float.__wrap(super(JsonElement, self).getAsDouble())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonNull.equals(java.lang.Object)"""
        return bool.__wrap(super(__JsonNull, self).equals(arg0))

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonElement.getAsCharacter()"""
        return str.__wrap(super(JsonElement, self).getAsCharacter())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonNull()"""
        val = __JsonNull()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonElement.getAsBigInteger()"""
        return __transform(super(JsonElement, self).getAsBigInteger()).'BigInteger'Value()

    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonElement.getAsNumber()"""
        return __transform(super(JsonElement, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonElement.getAsByte()"""
        return int.__wrap(super(JsonElement, self).getAsByte())

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.getAsString()"""
        return str.__wrap(super(JsonElement, self).getAsString())

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'.__wrap(super(JsonElement, self).getAsJsonPrimitive())

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonElement.getAsInt()"""
        return int.__wrap(super(JsonElement, self).getAsInt())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str.__wrap(super(JsonElement, self).toString())

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonElement.getAsLong()"""
        return int.__wrap(super(JsonElement, self).getAsLong())

    @override
    @overload
    def deepCopy(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonNull.deepCopy()"""
        return 'JsonNull'.__wrap(super(JsonNull, self).deepCopy())

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool.__wrap(super(JsonElement, self).isJsonPrimitive())

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonElement.getAsBoolean()"""
        return bool.__wrap(super(JsonElement, self).getAsBoolean())

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'.__wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'.__wrap(super(JsonElement, self).getAsJsonNull())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonElement.getAsBigDecimal()"""
        return __transform(super(JsonElement, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonElement.getAsShort()"""
        return int.__wrap(super(JsonElement, self).getAsShort())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonElement.getAsFloat()"""
        return float.__wrap(super(JsonElement, self).getAsFloat())

    @override
    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool.__wrap(super(JsonElement, self).isJsonArray())

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'.__wrap(super(JsonElement, self).getAsJsonObject())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool.__wrap(super(JsonElement, self).isJsonObject()) 
 
 
# CLASS: com.google.gson.JsonDeserializer
import com.google.gson.JsonDeserializer as __JsonDeserializer
__JsonDeserializer = __JsonDeserializer
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
 
class JsonDeserializer(ABC):
    """com.google.gson.JsonDeserializer"""
 
    @staticmethod
    def __wrap(java_value: __JsonDeserializer) -> 'JsonDeserializer':
        return JsonDeserializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonDeserializer):
        """
        Dynamic initializer for JsonDeserializer.
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
    def deserialize(self, arg0: 'JsonElement', arg1: 'Type', arg2: 'JsonDeserializationContext'):
        """public abstract T com.google.gson.JsonDeserializer.deserialize(com.google.gson.JsonElement,java.lang.reflect.Type,com.google.gson.JsonDeserializationContext) throws com.google.gson.JsonParseException"""
        pass