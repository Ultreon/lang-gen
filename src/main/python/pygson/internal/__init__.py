from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.google.gson.internal. as __Gson_Preconditions
_$Gson$Preconditions = __Gson_Preconditions.Gson.Preconditions
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class $Gson$Preconditions():
    """com.google.gson.internal..Gson.Preconditions"""
 
    @staticmethod
    def _wrap(java_value: _$Gson$Preconditions) -> '$Gson$Preconditions':
        return $Gson$Preconditions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _$Gson$Preconditions):
        """
        Dynamic initializer for $Gson$Preconditions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_$Gson$Preconditions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_$Gson$Preconditions__wrapper":
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
    def checkNotNull(arg0: object) -> object:
        """public static <T> T com.google.gson.internal.$Gson$Preconditions.checkNotNull(T)"""
        return object._wrap(_$Gson$Preconditions.checkNotNull(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def checkArgument(arg0: bool):
        """public static void com.google.gson.internal.$Gson$Preconditions.checkArgument(boolean)"""
        _$Gson$Preconditions.checkArgument(_boolean.valueOf(arg0))

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

 
 
 
# CLASS: com.google.gson.internal.$Gson$Preconditions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.google.gson.internal. as __Gson_Preconditions
_$Gson$Preconditions = __Gson_Preconditions.Gson.Preconditions
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class $Gson$Preconditions():
    """com.google.gson.internal..Gson.Preconditions"""
 
    @staticmethod
    def _wrap(java_value: _$Gson$Preconditions) -> '$Gson$Preconditions':
        return $Gson$Preconditions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _$Gson$Preconditions):
        """
        Dynamic initializer for $Gson$Preconditions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_$Gson$Preconditions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_$Gson$Preconditions__wrapper":
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
    def checkNotNull(arg0: object) -> object:
        """public static <T> T com.google.gson.internal.$Gson$Preconditions.checkNotNull(T)"""
        return object._wrap(_$Gson$Preconditions.checkNotNull(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def checkArgument(arg0: bool):
        """public static void com.google.gson.internal.$Gson$Preconditions.checkArgument(boolean)"""
        _$Gson$Preconditions.checkArgument(_boolean.valueOf(arg0))

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

 
 
 
# CLASS: com.google.gson.internal.$Gson$Preconditions 
 
 
# CLASS: com.google.gson.internal.JavaVersion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.google.gson.internal.JavaVersion as _JavaVersion
_JavaVersion = _JavaVersion
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JavaVersion():
    """com.google.gson.internal.JavaVersion"""
 
    @staticmethod
    def _wrap(java_value: _JavaVersion) -> 'JavaVersion':
        return JavaVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JavaVersion):
        """
        Dynamic initializer for JavaVersion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JavaVersion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JavaVersion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def isJava9OrLater() -> bool:
        """public static boolean com.google.gson.internal.JavaVersion.isJava9OrLater()"""
        return bool._wrap(_JavaVersion.isJava9OrLater())

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
    def getMajorJavaVersion() -> int:
        """public static int com.google.gson.internal.JavaVersion.getMajorJavaVersion()"""
        return int._wrap(_JavaVersion.getMajorJavaVersion())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.JsonReaderInternalAccess
from pyquantum_helper import import_once as _import_once
import com.google.gson.internal.JsonReaderInternalAccess as _JsonReaderInternalAccess
_JsonReaderInternalAccess = _JsonReaderInternalAccess
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonReaderInternalAccess():
    """com.google.gson.internal.JsonReaderInternalAccess"""
 
    @staticmethod
    def _wrap(java_value: _JsonReaderInternalAccess) -> 'JsonReaderInternalAccess':
        return JsonReaderInternalAccess(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonReaderInternalAccess):
        """
        Dynamic initializer for JsonReaderInternalAccess.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonReaderInternalAccess__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonReaderInternalAccess__wrapper":
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

    @overload
    def __init__(self):
        """public com.google.gson.internal.JsonReaderInternalAccess()"""
        val = _JsonReaderInternalAccess()
        self.__wrapper = val

    @abstractmethod
    def promoteNameToValue(self, arg0: 'JsonReader'):
        """public abstract void com.google.gson.internal.JsonReaderInternalAccess.promoteNameToValue(com.google.gson.stream.JsonReader) throws java.io.IOException"""
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.JsonReaderInternalAccess()"""
        val = _JsonReaderInternalAccess()
        self.__wrapper = val

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
 
 
# CLASS: com.google.gson.internal.PreJava9DateFormatProvider
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.internal.PreJava9DateFormatProvider as _PreJava9DateFormatProvider
_PreJava9DateFormatProvider = _PreJava9DateFormatProvider
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.text.DateFormat as DateFormat
import java.text.DateFormat as _DateFormat
_DateFormat = _DateFormat
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PreJava9DateFormatProvider():
    """com.google.gson.internal.PreJava9DateFormatProvider"""
 
    @staticmethod
    def _wrap(java_value: _PreJava9DateFormatProvider) -> 'PreJava9DateFormatProvider':
        return PreJava9DateFormatProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PreJava9DateFormatProvider):
        """
        Dynamic initializer for PreJava9DateFormatProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PreJava9DateFormatProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PreJava9DateFormatProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getUSDateFormat(arg0: int) -> 'DateFormat':
        """public static java.text.DateFormat com.google.gson.internal.PreJava9DateFormatProvider.getUSDateFormat(int)"""
        return DateFormat._wrap(_PreJava9DateFormatProvider.getUSDateFormat(_int.valueOf(arg0)))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.PreJava9DateFormatProvider()"""
        val = _PreJava9DateFormatProvider()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getUSDateTimeFormat(arg0: int, arg1: int) -> 'DateFormat':
        """public static java.text.DateFormat com.google.gson.internal.PreJava9DateFormatProvider.getUSDateTimeFormat(int,int)"""
        return DateFormat._wrap(_PreJava9DateFormatProvider.getUSDateTimeFormat(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.google.gson.internal.PreJava9DateFormatProvider()"""
        val = _PreJava9DateFormatProvider()
        self.__wrapper = val 
 
 
# CLASS: com.google.gson.internal.LinkedTreeMap
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import com.google.gson.internal.LinkedTreeMap as _LinkedTreeMap
_LinkedTreeMap = _LinkedTreeMap
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.lang.Boolean as _boolean
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.AbstractMap as _AbstractMap
_AbstractMap = _AbstractMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinkedTreeMap():
    """com.google.gson.internal.LinkedTreeMap"""
 
    @staticmethod
    def _wrap(java_value: _LinkedTreeMap) -> 'LinkedTreeMap':
        return LinkedTreeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkedTreeMap):
        """
        Dynamic initializer for LinkedTreeMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkedTreeMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkedTreeMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> com.google.gson.internal.LinkedTreeMap.keySet()"""
        return 'Set'._wrap(super(LinkedTreeMap, self).keySet())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractMap.isEmpty()"""
        return bool._wrap(super(AbstractMap, self).isEmpty())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public com.google.gson.internal.LinkedTreeMap(java.util.Comparator<? super K>,boolean)"""
        val = _LinkedTreeMap(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.LinkedTreeMap()"""
        val = _LinkedTreeMap()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractMap.toString()"""
        return str._wrap(super(AbstractMap, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.get(java.lang.Object)"""
        return object._wrap(super(_LinkedTreeMap, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: bool):
        """public com.google.gson.internal.LinkedTreeMap(boolean)"""
        val = _LinkedTreeMap(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> com.google.gson.internal.LinkedTreeMap.entrySet()"""
        return 'Set'._wrap(super(LinkedTreeMap, self).entrySet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).equals(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.put(K,V)"""
        return object._wrap(super(_LinkedTreeMap, self).put(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.LinkedTreeMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_LinkedTreeMap, self).containsKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> java.util.AbstractMap.values()"""
        return 'Collection'._wrap(super(AbstractMap, self).values())

    @overload
    def remove(self, arg0: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.remove(java.lang.Object)"""
        return object._wrap(super(_LinkedTreeMap, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void java.util.AbstractMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMap, self).putAll(arg0)

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).containsValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int com.google.gson.internal.LinkedTreeMap.size()"""
        return int._wrap(super(LinkedTreeMap, self).size())

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
    def __init__(self):
        """public com.google.gson.internal.LinkedTreeMap()"""
        val = _LinkedTreeMap()
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.google.gson.internal.LinkedTreeMap.clear()"""
        super(LinkedTreeMap, self).clear()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int._wrap(super(AbstractMap, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: com.google.gson.internal.UnsafeAllocator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.gson.internal.UnsafeAllocator as _UnsafeAllocator
_UnsafeAllocator = _UnsafeAllocator
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsafeAllocator():
    """com.google.gson.internal.UnsafeAllocator"""
 
    @staticmethod
    def _wrap(java_value: _UnsafeAllocator) -> 'UnsafeAllocator':
        return UnsafeAllocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsafeAllocator):
        """
        Dynamic initializer for UnsafeAllocator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsafeAllocator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsafeAllocator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def newInstance(self, arg0: 'Class'):
        """public abstract <T> T com.google.gson.internal.UnsafeAllocator.newInstance(java.lang.Class<T>) throws java.lang.Exception"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.google.gson.internal.UnsafeAllocator()"""
        val = _UnsafeAllocator()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.UnsafeAllocator()"""
        val = _UnsafeAllocator()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.Excluder
from pyquantum_helper import import_once as _import_once
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.Field as Field
import java.lang.String as _String
_String = _String
import com.google.gson.internal.Excluder as _Excluder
_Excluder = _Excluder
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygson import reflect
except ImportError:
    reflect = _import_once("pygson.reflect")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Excluder():
    """com.google.gson.internal.Excluder"""
 
    @staticmethod
    def _wrap(java_value: _Excluder) -> 'Excluder':
        return Excluder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Excluder):
        """
        Dynamic initializer for Excluder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Excluder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Excluder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def withVersion(self, arg0: float) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.withVersion(double)"""
        return 'Excluder'._wrap(super(_Excluder, self).withVersion(_double.valueOf(arg0)))

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

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.Excluder()"""
        val = _Excluder()
        self.__wrapper = val

    @overload
    def disableInnerClassSerialization(self) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.disableInnerClassSerialization()"""
        return 'Excluder'._wrap(super(Excluder, self).disableInnerClassSerialization())

    @overload
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.Excluder.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'._wrap(super(_Excluder, self).create(arg0, arg1))

    @overload
    def withModifiers(self, *arg0: int) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.withModifiers(int...)"""
        return 'Excluder'._wrap(super(_Excluder, self).withModifiers(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def excludeClass(self, arg0: 'Class', arg1: bool) -> bool:
        """public boolean com.google.gson.internal.Excluder.excludeClass(java.lang.Class<?>,boolean)"""
        return bool._wrap(super(_Excluder, self).excludeClass(arg0, _boolean.valueOf(arg1)))

    @overload
    def excludeFieldsWithoutExposeAnnotation(self) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.excludeFieldsWithoutExposeAnnotation()"""
        return 'Excluder'._wrap(super(Excluder, self).excludeFieldsWithoutExposeAnnotation())

    @overload
    def __init__(self):
        """public com.google.gson.internal.Excluder()"""
        val = _Excluder()
        self.__wrapper = val

    @overload
    def excludeField(self, arg0: 'Field', arg1: bool) -> bool:
        """public boolean com.google.gson.internal.Excluder.excludeField(java.lang.reflect.Field,boolean)"""
        return bool._wrap(super(_Excluder, self).excludeField(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def withExclusionStrategy(self, arg0: 'ExclusionStrategy', arg1: bool, arg2: bool) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.withExclusionStrategy(com.google.gson.ExclusionStrategy,boolean,boolean)"""
        return 'Excluder'._wrap(super(_Excluder, self).withExclusionStrategy(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

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
 
 
# CLASS: com.google.gson.internal.Primitives
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.gson.internal.Primitives as _Primitives
_Primitives = _Primitives
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Primitives():
    """com.google.gson.internal.Primitives"""
 
    @staticmethod
    def _wrap(java_value: _Primitives) -> 'Primitives':
        return Primitives(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Primitives):
        """
        Dynamic initializer for Primitives.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Primitives__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Primitives__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def wrap(arg0: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.gson.internal.Primitives.wrap(java.lang.Class<T>)"""
        return type.Class._wrap(_Primitives.wrap(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def isWrapperType(arg0: 'Type') -> bool:
        """public static boolean com.google.gson.internal.Primitives.isWrapperType(java.lang.reflect.Type)"""
        return bool._wrap(_Primitives.isWrapperType(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def unwrap(arg0: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.gson.internal.Primitives.unwrap(java.lang.Class<T>)"""
        return type.Class._wrap(_Primitives.unwrap(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def isPrimitive(arg0: 'Type') -> bool:
        """public static boolean com.google.gson.internal.Primitives.isPrimitive(java.lang.reflect.Type)"""
        return bool._wrap(_Primitives.isPrimitive(arg0))

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
 
 
# CLASS: com.google.gson.internal.ConstructorConstructor
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.google.gson.internal.ObjectConstructor as _ObjectConstructor
_ObjectConstructor = _ObjectConstructor
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.gson.internal.ConstructorConstructor as _ConstructorConstructor
_ConstructorConstructor = _ConstructorConstructor
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygson import reflect
except ImportError:
    reflect = _import_once("pygson.reflect")

from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class ConstructorConstructor():
    """com.google.gson.internal.ConstructorConstructor"""
 
    @staticmethod
    def _wrap(java_value: _ConstructorConstructor) -> 'ConstructorConstructor':
        return ConstructorConstructor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstructorConstructor):
        """
        Dynamic initializer for ConstructorConstructor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstructorConstructor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstructorConstructor__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.ConstructorConstructor.toString()"""
        return str._wrap(super(ConstructorConstructor, self).toString())

    @overload
    def get(self, arg0: 'TypeToken') -> 'ObjectConstructor':
        """public <T> com.google.gson.internal.ObjectConstructor<T> com.google.gson.internal.ConstructorConstructor.get(com.google.gson.reflect.TypeToken<T>)"""
        return 'ObjectConstructor'._wrap(super(_ConstructorConstructor, self).get(arg0))

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
    def __init__(self, arg0: 'Map', arg1: bool, arg2: 'List'):
        """public com.google.gson.internal.ConstructorConstructor(java.util.Map<java.lang.reflect.Type, com.google.gson.InstanceCreator<?>>,boolean,java.util.List<com.google.gson.ReflectionAccessFilter>)"""
        val = _ConstructorConstructor(arg0, _boolean.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.GsonBuildConfig
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import com.google.gson.internal.GsonBuildConfig as _GsonBuildConfig
_GsonBuildConfig = _GsonBuildConfig
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GsonBuildConfig():
    """com.google.gson.internal.GsonBuildConfig"""
 
    @staticmethod
    def _wrap(java_value: _GsonBuildConfig) -> 'GsonBuildConfig':
        return GsonBuildConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GsonBuildConfig):
        """
        Dynamic initializer for GsonBuildConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GsonBuildConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GsonBuildConfig__wrapper":
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
 
 
# CLASS: com.google.gson.internal.Streams
from pyquantum_helper import import_once as _import_once
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Appendable as Appendable
import java.lang.Integer as _int
import java.io.Writer as Writer
import com.google.gson.internal.Streams as _Streams
_Streams = _Streams
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Streams():
    """com.google.gson.internal.Streams"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def write(arg0: 'JsonElement', arg1: 'JsonWriter'):
        """public static void com.google.gson.internal.Streams.write(com.google.gson.JsonElement,com.google.gson.stream.JsonWriter) throws java.io.IOException"""
        _Streams.write(arg0, arg1)

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
    def parse(arg0: 'JsonReader') -> 'pygson.JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.internal.Streams.parse(com.google.gson.stream.JsonReader) throws com.google.gson.JsonParseException"""
        return pygson.JsonElement._wrap(_Streams.parse(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def writerForAppendable(arg0: 'Appendable') -> 'Writer':
        """public static java.io.Writer com.google.gson.internal.Streams.writerForAppendable(java.lang.Appendable)"""
        return Writer._wrap(_Streams.writerForAppendable(arg0))

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
 
 
# CLASS: com.google.gson.internal.NonNullElementWrapperList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.AbstractList as _AbstractList
_AbstractList = _AbstractList
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import com.google.gson.internal.NonNullElementWrapperList as _NonNullElementWrapperList
_NonNullElementWrapperList = _NonNullElementWrapperList
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.ArrayList as ArrayList
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class NonNullElementWrapperList():
    """com.google.gson.internal.NonNullElementWrapperList"""
 
    @staticmethod
    def _wrap(java_value: _NonNullElementWrapperList) -> 'NonNullElementWrapperList':
        return NonNullElementWrapperList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NonNullElementWrapperList):
        """
        Dynamic initializer for NonNullElementWrapperList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NonNullElementWrapperList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NonNullElementWrapperList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E com.google.gson.internal.NonNullElementWrapperList.get(int)"""
        return object._wrap(super(_NonNullElementWrapperList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.contains(java.lang.Object)"""
        return bool._wrap(super(_NonNullElementWrapperList, self).contains(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.equals(java.lang.Object)"""
        return bool._wrap(super(_NonNullElementWrapperList, self).equals(arg0))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.AbstractList.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractList, self).listIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.AbstractList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_AbstractList, self).listIterator(_int.valueOf(arg0)))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_NonNullElementWrapperList, self).removeAll(arg0))

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
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.AbstractList.subList(int,int)"""
        return 'List'._wrap(super(_AbstractList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @overload
    def __init__(self, arg0: 'ArrayList'):
        """public com.google.gson.internal.NonNullElementWrapperList(java.util.ArrayList<E>)"""
        val = _NonNullElementWrapperList(arg0)
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] com.google.gson.internal.NonNullElementWrapperList.toArray(T[])"""
        return List[object]._wrap(super(_NonNullElementWrapperList, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_NonNullElementWrapperList, self).retainAll(arg0))

    @override
    @overload
    def clear(self):
        """public void com.google.gson.internal.NonNullElementWrapperList.clear()"""
        super(NonNullElementWrapperList, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @overload
    def remove(self, arg0: int) -> object:
        """public E com.google.gson.internal.NonNullElementWrapperList.remove(int)"""
        return object._wrap(super(_NonNullElementWrapperList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.hashCode()"""
        return int._wrap(super(NonNullElementWrapperList, self).hashCode())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.add(E)"""
        return bool._wrap(super(_AbstractList, self).add(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_NonNullElementWrapperList, self).lastIndexOf(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.gson.internal.NonNullElementWrapperList.toArray()"""
        return List[object]._wrap(super(NonNullElementWrapperList, self).toArray())

    @override
    @overload
    def size(self) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.size()"""
        return int._wrap(super(NonNullElementWrapperList, self).size())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.remove(java.lang.Object)"""
        return bool._wrap(super(_NonNullElementWrapperList, self).remove(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void com.google.gson.internal.NonNullElementWrapperList.add(int,E)"""
        super(_NonNullElementWrapperList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.AbstractList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.AbstractList.iterator()"""
        return 'Iterator'._wrap(super(AbstractList, self).iterator())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.indexOf(java.lang.Object)"""
        return int._wrap(super(_NonNullElementWrapperList, self).indexOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E com.google.gson.internal.NonNullElementWrapperList.set(int,E)"""
        return object._wrap(super(_NonNullElementWrapperList, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: com.google.gson.internal.ReflectionAccessFilterHelper
from pyquantum_helper import import_once as _import_once
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.ReflectionAccessFilter as _ReflectionAccessFilter_FilterResult
_FilterResult = _ReflectionAccessFilter_FilterResult.FilterResult
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.lang.reflect.AccessibleObject as AccessibleObject
import com.google.gson.internal.ReflectionAccessFilterHelper as _ReflectionAccessFilterHelper
_ReflectionAccessFilterHelper = _ReflectionAccessFilterHelper
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReflectionAccessFilterHelper():
    """com.google.gson.internal.ReflectionAccessFilterHelper"""
 
    @staticmethod
    def _wrap(java_value: _ReflectionAccessFilterHelper) -> 'ReflectionAccessFilterHelper':
        return ReflectionAccessFilterHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectionAccessFilterHelper):
        """
        Dynamic initializer for ReflectionAccessFilterHelper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectionAccessFilterHelper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectionAccessFilterHelper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isAndroidType(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.isAndroidType(java.lang.Class<?>)"""
        return bool._wrap(_ReflectionAccessFilterHelper.isAndroidType(arg0))

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

    @staticmethod
    @overload
    def getFilterResult(arg0: 'List', arg1: 'Class') -> 'pygson.ReflectionAccessFilter$FilterResult':
        """public static com.google.gson.ReflectionAccessFilter$FilterResult com.google.gson.internal.ReflectionAccessFilterHelper.getFilterResult(java.util.List<com.google.gson.ReflectionAccessFilter>,java.lang.Class<?>)"""
        return pygson.ReflectionAccessFilter$FilterResult._wrap(_ReflectionAccessFilterHelper.getFilterResult(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def isJavaType(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.isJavaType(java.lang.Class<?>)"""
        return bool._wrap(_ReflectionAccessFilterHelper.isJavaType(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def canAccess(arg0: 'AccessibleObject', arg1: object) -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.canAccess(java.lang.reflect.AccessibleObject,java.lang.Object)"""
        return bool._wrap(_ReflectionAccessFilterHelper.canAccess(arg0, arg1))

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
    def isAnyPlatformType(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.isAnyPlatformType(java.lang.Class<?>)"""
        return bool._wrap(_ReflectionAccessFilterHelper.isAnyPlatformType(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.$Gson$Types
import java.lang.reflect.GenericArrayType as GenericArrayType
from builtins import str
import java.lang.reflect.WildcardType as WildcardType
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.ParameterizedType as ParameterizedType
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.reflect.Type as _Type
_Type = _Type
import java.lang.reflect.GenericArrayType as _GenericArrayType
_GenericArrayType = _GenericArrayType
import java.lang.reflect.WildcardType as _WildcardType
_WildcardType = _WildcardType
from typing import List
import com.google.gson.internal. as __Gson_Types
_$Gson$Types = __Gson_Types.Gson.Types
import java.lang.Integer as _int
from builtins import bool
import java.lang.reflect.ParameterizedType as _ParameterizedType
_ParameterizedType = _ParameterizedType
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class $Gson$Types():
    """com.google.gson.internal..Gson.Types"""
 
    @staticmethod
    def _wrap(java_value: _$Gson$Types) -> '$Gson$Types':
        return $Gson$Types(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _$Gson$Types):
        """
        Dynamic initializer for $Gson$Types.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_$Gson$Types__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_$Gson$Types__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def arrayOf(arg0: 'Type') -> 'GenericArrayType':
        """public static java.lang.reflect.GenericArrayType com.google.gson.internal.$Gson$Types.arrayOf(java.lang.reflect.Type)"""
        return GenericArrayType._wrap(_$Gson$Types.arrayOf(arg0))

    @staticmethod
    @overload
    def canonicalize(arg0: 'Type') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.canonicalize(java.lang.reflect.Type)"""
        return Type._wrap(_$Gson$Types.canonicalize(arg0))

    @staticmethod
    @overload
    def getCollectionElementType(arg0: 'Type', arg1: 'Class') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.getCollectionElementType(java.lang.reflect.Type,java.lang.Class<?>)"""
        return Type._wrap(_$Gson$Types.getCollectionElementType(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getRawType(arg0: 'Type') -> 'type.Class':
        """public static java.lang.Class<?> com.google.gson.internal.$Gson$Types.getRawType(java.lang.reflect.Type)"""
        return type.Class._wrap(_$Gson$Types.getRawType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def newParameterizedTypeWithOwner(arg0: 'Type', arg1: 'Type', *arg2: 'Type') -> 'ParameterizedType':
        """public static java.lang.reflect.ParameterizedType com.google.gson.internal.$Gson$Types.newParameterizedTypeWithOwner(java.lang.reflect.Type,java.lang.reflect.Type,java.lang.reflect.Type...)"""
        return ParameterizedType._wrap(_$Gson$Types.newParameterizedTypeWithOwner(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getMapKeyAndValueTypes(arg0: 'Type', arg1: 'Class') -> List['Type']:
        """public static java.lang.reflect.Type[] com.google.gson.internal.$Gson$Types.getMapKeyAndValueTypes(java.lang.reflect.Type,java.lang.Class<?>)"""
        return List[Type]._wrap(_$Gson$Types.getMapKeyAndValueTypes(arg0, arg1))

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
    def equals(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean com.google.gson.internal.$Gson$Types.equals(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool._wrap(_$Gson$Types.equals(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def supertypeOf(arg0: 'Type') -> 'WildcardType':
        """public static java.lang.reflect.WildcardType com.google.gson.internal.$Gson$Types.supertypeOf(java.lang.reflect.Type)"""
        return WildcardType._wrap(_$Gson$Types.supertypeOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getArrayComponentType(arg0: 'Type') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.getArrayComponentType(java.lang.reflect.Type)"""
        return Type._wrap(_$Gson$Types.getArrayComponentType(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def typeToString(arg0: 'Type') -> str:
        """public static java.lang.String com.google.gson.internal.$Gson$Types.typeToString(java.lang.reflect.Type)"""
        return str._wrap(_$Gson$Types.typeToString(arg0))

    @staticmethod
    @overload
    def resolve(arg0: 'Type', arg1: 'Class', arg2: 'Type') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.resolve(java.lang.reflect.Type,java.lang.Class<?>,java.lang.reflect.Type)"""
        return Type._wrap(_$Gson$Types.resolve(arg0, arg1, arg2))

    @staticmethod
    @overload
    def subtypeOf(arg0: 'Type') -> 'WildcardType':
        """public static java.lang.reflect.WildcardType com.google.gson.internal.$Gson$Types.subtypeOf(java.lang.reflect.Type)"""
        return WildcardType._wrap(_$Gson$Types.subtypeOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.LazilyParsedNumber
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.google.gson.internal.LazilyParsedNumber as _LazilyParsedNumber
_LazilyParsedNumber = _LazilyParsedNumber
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazilyParsedNumber():
    """com.google.gson.internal.LazilyParsedNumber"""
 
    @staticmethod
    def _wrap(java_value: _LazilyParsedNumber) -> 'LazilyParsedNumber':
        return LazilyParsedNumber(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazilyParsedNumber):
        """
        Dynamic initializer for LazilyParsedNumber.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazilyParsedNumber__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazilyParsedNumber__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def longValue(self) -> int:
        """public long com.google.gson.internal.LazilyParsedNumber.longValue()"""
        return int._wrap(super(LazilyParsedNumber, self).longValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.LazilyParsedNumber.toString()"""
        return str._wrap(super(LazilyParsedNumber, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.internal.LazilyParsedNumber(java.lang.String)"""
        val = _LazilyParsedNumber(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float com.google.gson.internal.LazilyParsedNumber.floatValue()"""
        return float._wrap(super(LazilyParsedNumber, self).floatValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.LazilyParsedNumber.equals(java.lang.Object)"""
        return bool._wrap(super(_LazilyParsedNumber, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.internal.LazilyParsedNumber.hashCode()"""
        return int._wrap(super(LazilyParsedNumber, self).hashCode())

    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.gson.internal.LazilyParsedNumber.doubleValue()"""
        return float._wrap(super(LazilyParsedNumber, self).doubleValue())

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
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def intValue(self) -> int:
        """public int com.google.gson.internal.LazilyParsedNumber.intValue()"""
        return int._wrap(super(LazilyParsedNumber, self).intValue()) 
 
 
# CLASS: com.google.gson.internal.ObjectConstructor
import com.google.gson.internal.ObjectConstructor as _ObjectConstructor
_ObjectConstructor = _ObjectConstructor
from abc import abstractmethod, ABC
 
class ObjectConstructor():
    """com.google.gson.internal.ObjectConstructor"""
 
    @staticmethod
    def _wrap(java_value: _ObjectConstructor) -> 'ObjectConstructor':
        return ObjectConstructor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectConstructor):
        """
        Dynamic initializer for ObjectConstructor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectConstructor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectConstructor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def construct(self, ):
        """public abstract T com.google.gson.internal.ObjectConstructor.construct()"""
        pass