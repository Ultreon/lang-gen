from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

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
import com.google.gson.internal.bind.SerializationDelegatingTypeAdapter as __SerializationDelegatingTypeAdapter
__SerializationDelegatingTypeAdapter = __SerializationDelegatingTypeAdapter
import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class SerializationDelegatingTypeAdapter(ABC, pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.SerializationDelegatingTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __SerializationDelegatingTypeAdapter) -> 'SerializationDelegatingTypeAdapter':
        return SerializationDelegatingTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializationDelegatingTypeAdapter):
        """
        Dynamic initializer for SerializationDelegatingTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def getSerializationDelegate(self, ):
        """public abstract com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.SerializationDelegatingTypeAdapter.getSerializationDelegate()"""
        pass

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.SerializationDelegatingTypeAdapter()"""
        val = __SerializationDelegatingTypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.SerializationDelegatingTypeAdapter()"""
        val = __SerializationDelegatingTypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

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

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.gson.internal.bind.SerializationDelegatingTypeAdapter
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

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
import com.google.gson.internal.bind.SerializationDelegatingTypeAdapter as __SerializationDelegatingTypeAdapter
__SerializationDelegatingTypeAdapter = __SerializationDelegatingTypeAdapter
import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class SerializationDelegatingTypeAdapter(ABC, pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.SerializationDelegatingTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __SerializationDelegatingTypeAdapter) -> 'SerializationDelegatingTypeAdapter':
        return SerializationDelegatingTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializationDelegatingTypeAdapter):
        """
        Dynamic initializer for SerializationDelegatingTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def getSerializationDelegate(self, ):
        """public abstract com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.SerializationDelegatingTypeAdapter.getSerializationDelegate()"""
        pass

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.SerializationDelegatingTypeAdapter()"""
        val = __SerializationDelegatingTypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.SerializationDelegatingTypeAdapter()"""
        val = __SerializationDelegatingTypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

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

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.gson.internal.bind.SerializationDelegatingTypeAdapter 
 
 
# CLASS: com.google.gson.internal.bind.NumberTypeAdapter
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as __transform
import com.google.gson.internal.bind.NumberTypeAdapter as __NumberTypeAdapter
__NumberTypeAdapter = __NumberTypeAdapter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.TypeAdapterFactory as __TypeAdapterFactory
__TypeAdapterFactory = __TypeAdapterFactory
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
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
 
class NumberTypeAdapter(pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.NumberTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __NumberTypeAdapter) -> 'NumberTypeAdapter':
        return NumberTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NumberTypeAdapter):
        """
        Dynamic initializer for NumberTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def read(self, arg0: 'JsonReader') -> 'Number':
        """public java.lang.Number com.google.gson.internal.bind.NumberTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return __transform(super(__NumberTypeAdapter, self).read(arg0)).'Number'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

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

    @staticmethod
    @overload
    def getFactory(arg0: 'ToNumberStrategy') -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.NumberTypeAdapter.getFactory(com.google.gson.ToNumberStrategy)"""
        return pygson.TypeAdapterFactory.__wrap(__NumberTypeAdapter.getFactory(arg0))

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def write(self, arg0: 'JsonWriter', arg1: 'Number'):
        """public void com.google.gson.internal.bind.NumberTypeAdapter.write(com.google.gson.stream.JsonWriter,java.lang.Number) throws java.io.IOException"""
        super(__NumberTypeAdapter, self).write(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.TypeAdapters
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.TypeAdapterFactory as __TypeAdapterFactory
__TypeAdapterFactory = __TypeAdapterFactory
import com.google.gson.internal.bind.TypeAdapters as __TypeAdapters
__TypeAdapters = __TypeAdapters
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TypeAdapters():
    """com.google.gson.internal.bind.TypeAdapters"""
 
    @staticmethod
    def __wrap(java_value: __TypeAdapters) -> 'TypeAdapters':
        return TypeAdapters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeAdapters):
        """
        Dynamic initializer for TypeAdapters.
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
    def newFactoryForMultipleTypes(arg0: 'Class', arg1: 'Class', arg2: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactoryForMultipleTypes(java.lang.Class<TT>,java.lang.Class<? extends TT>,com.google.gson.TypeAdapter<? super TT>)"""
        return pygson.TypeAdapterFactory.__wrap(__TypeAdapters.newFactoryForMultipleTypes(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def newTypeHierarchyFactory(arg0: 'Class', arg1: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <T1> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newTypeHierarchyFactory(java.lang.Class<T1>,com.google.gson.TypeAdapter<T1>)"""
        return pygson.TypeAdapterFactory.__wrap(__TypeAdapters.newTypeHierarchyFactory(arg0, arg1))

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

    @staticmethod
    @overload
    def newFactory(arg0: 'TypeToken', arg1: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactory(com.google.gson.reflect.TypeToken<TT>,com.google.gson.TypeAdapter<TT>)"""
        return pygson.TypeAdapterFactory.__wrap(__TypeAdapters.newFactory(arg0, arg1))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def newFactory(arg0: 'Class', arg1: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactory(java.lang.Class<TT>,com.google.gson.TypeAdapter<TT>)"""
        return pygson.TypeAdapterFactory.__wrap(__TypeAdapters.newFactory(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def newFactory(arg0: 'Class', arg1: 'Class', arg2: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactory(java.lang.Class<TT>,java.lang.Class<TT>,com.google.gson.TypeAdapter<? super TT>)"""
        return pygson.TypeAdapterFactory.__wrap(__TypeAdapters.newFactory(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.MapTypeAdapterFactory
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.gson.internal.bind.MapTypeAdapterFactory as __MapTypeAdapterFactory
__MapTypeAdapterFactory = __MapTypeAdapterFactory
try:
    from pygson import internal
except ImportError:
    internal = __import_once__("pygson.internal")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MapTypeAdapterFactory(pygson.__TypeAdapterFactory, pygson.TypeAdapterFactory):
    """com.google.gson.internal.bind.MapTypeAdapterFactory"""
 
    @staticmethod
    def __wrap(java_value: __MapTypeAdapterFactory) -> 'MapTypeAdapterFactory':
        return MapTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapTypeAdapterFactory):
        """
        Dynamic initializer for MapTypeAdapterFactory.
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

    @overload
    def __init__(self, arg0: 'ConstructorConstructor', arg1: bool):
        """public com.google.gson.internal.bind.MapTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor,boolean)"""
        val = __MapTypeAdapterFactory(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.MapTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'.__wrap(super(__MapTypeAdapterFactory, self).create(arg0, arg1))

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
 
 
# CLASS: com.google.gson.internal.bind.JsonTreeWriter
from pyquantum_helper import import_once as __import_once__
import com.google.gson.internal.bind.JsonTreeWriter as __JsonTreeWriter
__JsonTreeWriter = __JsonTreeWriter
import java.lang.Boolean as Boolean
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.gson.stream.JsonWriter as __JsonWriter
__JsonWriter = __JsonWriter
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class JsonTreeWriter(pygson.__JsonWriter, stream.JsonWriter):
    """com.google.gson.internal.bind.JsonTreeWriter"""
 
    @staticmethod
    def __wrap(java_value: __JsonTreeWriter) -> 'JsonTreeWriter':
        return JsonTreeWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonTreeWriter):
        """
        Dynamic initializer for JsonTreeWriter.
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
    def value(self, arg0: bool) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(boolean) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).value(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def beginObject(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.beginObject() throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(JsonTreeWriter, self).beginObject())

    @overload
    def name(self, arg0: str) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.name(java.lang.String) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).name(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def endObject(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.endObject() throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(JsonTreeWriter, self).endObject())

    @override
    @overload
    def isHtmlSafe(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.isHtmlSafe()"""
        return bool.__wrap(super(stream.JsonWriter, self).isHtmlSafe())

    @overload
    def jsonValue(self, arg0: str) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.jsonValue(java.lang.String) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).jsonValue(arg0))

    @override
    @overload
    def getSerializeNulls(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.getSerializeNulls()"""
        return bool.__wrap(super(stream.JsonWriter, self).getSerializeNulls())

    @override
    @overload
    def setSerializeNulls(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setSerializeNulls(boolean)"""
        super(__stream.JsonWriter, self).setSerializeNulls(__boolean.valueOf(arg0))

    @override
    @overload
    def nullValue(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.nullValue() throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(JsonTreeWriter, self).nullValue())

    @overload
    def get(self) -> 'pygson.JsonElement':
        """public com.google.gson.JsonElement com.google.gson.internal.bind.JsonTreeWriter.get()"""
        return 'pygson.JsonElement'.__wrap(super(JsonTreeWriter, self).get())

    @override
    @overload
    def flush(self):
        """public void com.google.gson.internal.bind.JsonTreeWriter.flush() throws java.io.IOException"""
        super(JsonTreeWriter, self).flush()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def endArray(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.endArray() throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(JsonTreeWriter, self).endArray())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def beginArray(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.beginArray() throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(JsonTreeWriter, self).beginArray())

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.JsonTreeWriter()"""
        val = __JsonTreeWriter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def value(self, arg0: 'Boolean') -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(java.lang.Boolean) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).value(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setIndent(self, arg0: str):
        """public final void com.google.gson.stream.JsonWriter.setIndent(java.lang.String)"""
        super(__stream.JsonWriter, self).setIndent(arg0)

    @overload
    def value(self, arg0: 'Number') -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(java.lang.Number) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).value(arg0))

    @overload
    def value(self, arg0: float) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(float) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).value(__float.valueOf(arg0)))

    @override
    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setLenient(boolean)"""
        super(__stream.JsonWriter, self).setLenient(__boolean.valueOf(arg0))

    @override
    @overload
    def setHtmlSafe(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setHtmlSafe(boolean)"""
        super(__stream.JsonWriter, self).setHtmlSafe(__boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isLenient(self) -> bool:
        """public boolean com.google.gson.stream.JsonWriter.isLenient()"""
        return bool.__wrap(super(stream.JsonWriter, self).isLenient())

    @overload
    def value(self, arg0: str) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(java.lang.String) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).value(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.JsonTreeWriter()"""
        val = __JsonTreeWriter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def value(self, arg0: float) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(double) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).value(__double.valueOf(arg0)))

    @overload
    def value(self, arg0: int) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(long) throws java.io.IOException"""
        return 'stream.JsonWriter'.__wrap(super(__JsonTreeWriter, self).value(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public void com.google.gson.internal.bind.JsonTreeWriter.close() throws java.io.IOException"""
        super(JsonTreeWriter, self).close() 
 
 
# CLASS: com.google.gson.internal.bind.DefaultDateTypeAdapter
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
from builtins import object
import com.google.gson.internal.bind.DefaultDateTypeAdapter as __DefaultDateTypeAdapter
__DefaultDateTypeAdapter = __DefaultDateTypeAdapter
import java.util.Date as Date
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.util.Date as __Date
__Date = __Date
import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class DefaultDateTypeAdapter(pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.DefaultDateTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __DefaultDateTypeAdapter) -> 'DefaultDateTypeAdapter':
        return DefaultDateTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultDateTypeAdapter):
        """
        Dynamic initializer for DefaultDateTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.DefaultDateTypeAdapter.toString()"""
        return str.__wrap(super(DefaultDateTypeAdapter, self).toString())

    @overload
    def read(self, arg0: 'JsonReader') -> 'Date':
        """public T com.google.gson.internal.bind.DefaultDateTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return 'Date'.__wrap(super(__DefaultDateTypeAdapter, self).read(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

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
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def write(self, arg0: 'JsonWriter', arg1: 'Date'):
        """public void com.google.gson.internal.bind.DefaultDateTypeAdapter.write(com.google.gson.stream.JsonWriter,java.util.Date) throws java.io.IOException"""
        super(__DefaultDateTypeAdapter, self).write(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.ObjectTypeAdapter
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.TypeAdapterFactory as __TypeAdapterFactory
__TypeAdapterFactory = __TypeAdapterFactory
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
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
import com.google.gson.internal.bind.ObjectTypeAdapter as __ObjectTypeAdapter
__ObjectTypeAdapter = __ObjectTypeAdapter
import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class ObjectTypeAdapter(pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.ObjectTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __ObjectTypeAdapter) -> 'ObjectTypeAdapter':
        return ObjectTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectTypeAdapter):
        """
        Dynamic initializer for ObjectTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.ObjectTypeAdapter.write(com.google.gson.stream.JsonWriter,java.lang.Object) throws java.io.IOException"""
        super(__ObjectTypeAdapter, self).write(arg0, arg1)

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def read(self, arg0: 'JsonReader') -> object:
        """public java.lang.Object com.google.gson.internal.bind.ObjectTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object.__wrap(super(__ObjectTypeAdapter, self).read(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getFactory(arg0: 'ToNumberStrategy') -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.ObjectTypeAdapter.getFactory(com.google.gson.ToNumberStrategy)"""
        return pygson.TypeAdapterFactory.__wrap(__ObjectTypeAdapter.getFactory(arg0))

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.JsonTreeReader
from pyquantum_helper import import_once as __import_once__
import com.google.gson.stream.JsonToken as __JsonToken
__JsonToken = __JsonToken
from builtins import str
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.gson.stream.JsonReader as __JsonReader
__JsonReader = __JsonReader
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.gson.internal.bind.JsonTreeReader as __JsonTreeReader
__JsonTreeReader = __JsonTreeReader
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class JsonTreeReader(pygson.__JsonReader, stream.JsonReader):
    """com.google.gson.internal.bind.JsonTreeReader"""
 
    @staticmethod
    def __wrap(java_value: __JsonTreeReader) -> 'JsonTreeReader':
        return JsonTreeReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonTreeReader):
        """
        Dynamic initializer for JsonTreeReader.
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
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonReader.setLenient(boolean)"""
        super(__stream.JsonReader, self).setLenient(__boolean.valueOf(arg0))

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.getPath()"""
        return str.__wrap(super(JsonTreeReader, self).getPath())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def endArray(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.endArray() throws java.io.IOException"""
        super(JsonTreeReader, self).endArray()

    @override
    @overload
    def nextBoolean(self) -> bool:
        """public boolean com.google.gson.internal.bind.JsonTreeReader.nextBoolean() throws java.io.IOException"""
        return bool.__wrap(super(JsonTreeReader, self).nextBoolean())

    @override
    @overload
    def beginArray(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.beginArray() throws java.io.IOException"""
        super(JsonTreeReader, self).beginArray()

    @override
    @overload
    def skipValue(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.skipValue() throws java.io.IOException"""
        super(JsonTreeReader, self).skipValue()

    @overload
    def promoteNameToValue(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.promoteNameToValue() throws java.io.IOException"""
        super(JsonTreeReader, self).promoteNameToValue()

    @override
    @overload
    def getPreviousPath(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.getPreviousPath()"""
        return str.__wrap(super(JsonTreeReader, self).getPreviousPath())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isLenient(self) -> bool:
        """public final boolean com.google.gson.stream.JsonReader.isLenient()"""
        return bool.__wrap(super(stream.JsonReader, self).isLenient())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.google.gson.internal.bind.JsonTreeReader.hasNext() throws java.io.IOException"""
        return bool.__wrap(super(JsonTreeReader, self).hasNext())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def nextString(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.nextString() throws java.io.IOException"""
        return str.__wrap(super(JsonTreeReader, self).nextString())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.google.gson.internal.bind.JsonTreeReader.nextInt() throws java.io.IOException"""
        return int.__wrap(super(JsonTreeReader, self).nextInt())

    @override
    @overload
    def close(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.close() throws java.io.IOException"""
        super(JsonTreeReader, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.google.gson.internal.bind.JsonTreeReader.nextDouble() throws java.io.IOException"""
        return float.__wrap(super(JsonTreeReader, self).nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.toString()"""
        return str.__wrap(super(JsonTreeReader, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.google.gson.internal.bind.JsonTreeReader.nextLong() throws java.io.IOException"""
        return int.__wrap(super(JsonTreeReader, self).nextLong())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def beginObject(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.beginObject() throws java.io.IOException"""
        super(JsonTreeReader, self).beginObject()

    @override
    @overload
    def endObject(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.endObject() throws java.io.IOException"""
        super(JsonTreeReader, self).endObject()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'JsonElement'):
        """public com.google.gson.internal.bind.JsonTreeReader(com.google.gson.JsonElement)"""
        val = __JsonTreeReader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def peek(self) -> 'stream.JsonToken':
        """public com.google.gson.stream.JsonToken com.google.gson.internal.bind.JsonTreeReader.peek() throws java.io.IOException"""
        return 'stream.JsonToken'.__wrap(super(JsonTreeReader, self).peek())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextNull(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.nextNull() throws java.io.IOException"""
        super(JsonTreeReader, self).nextNull()

    @override
    @overload
    def nextName(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.nextName() throws java.io.IOException"""
        return str.__wrap(super(JsonTreeReader, self).nextName()) 
 
 
# CLASS: com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
import com.google.gson.internal.bind.ReflectiveTypeAdapterFactory as __ReflectiveTypeAdapterFactory_Adapter
__Adapter = __ReflectiveTypeAdapterFactory_Adapter.Adapter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
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
 
class Adapter(ABC, pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.ReflectiveTypeAdapterFactory.Adapter"""
 
    @staticmethod
    def __wrap(java_value: __Adapter) -> 'Adapter':
        return Adapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Adapter):
        """
        Dynamic initializer for Adapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def read(self, arg0: 'JsonReader') -> object:
        """public T com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object.__wrap(super(__Adapter, self).read(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter.write(com.google.gson.stream.JsonWriter,T) throws java.io.IOException"""
        super(__Adapter, self).write(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.DateTypeAdapter
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
from builtins import object
import java.util.Date as Date
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
import java.util.Date as __Date
__Date = __Date
import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
import com.google.gson.internal.bind.DateTypeAdapter as __DateTypeAdapter
__DateTypeAdapter = __DateTypeAdapter
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class DateTypeAdapter(pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.DateTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __DateTypeAdapter) -> 'DateTypeAdapter':
        return DateTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DateTypeAdapter):
        """
        Dynamic initializer for DateTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @overload
    def read(self, arg0: 'JsonReader') -> 'Date':
        """public java.util.Date com.google.gson.internal.bind.DateTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return 'Date'.__wrap(super(__DateTypeAdapter, self).read(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def write(self, arg0: 'JsonWriter', arg1: 'Date'):
        """public void com.google.gson.internal.bind.DateTypeAdapter.write(com.google.gson.stream.JsonWriter,java.util.Date) throws java.io.IOException"""
        super(__DateTypeAdapter, self).write(arg0, arg1)

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

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
    def __init__(self):
        """public com.google.gson.internal.bind.DateTypeAdapter()"""
        val = __DateTypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.DateTypeAdapter()"""
        val = __DateTypeAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType
from pyquantum_helper import import_once as __import_once__
import com.google.gson.internal.bind.DefaultDateTypeAdapter as __DefaultDateTypeAdapter_DateType
__DateType = __DefaultDateTypeAdapter_DateType.DateType
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.TypeAdapterFactory as __TypeAdapterFactory
__TypeAdapterFactory = __TypeAdapterFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DateType(ABC):
    """com.google.gson.internal.bind.DefaultDateTypeAdapter.DateType"""
 
    @staticmethod
    def __wrap(java_value: __DateType) -> 'DateType':
        return DateType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DateType):
        """
        Dynamic initializer for DateType.
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
    def createAdapterFactory(self, arg0: str) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createAdapterFactory(java.lang.String)"""
        return 'pygson.TypeAdapterFactory'.__wrap(super(__DateType, self).createAdapterFactory(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createDefaultsAdapterFactory(self) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createDefaultsAdapterFactory()"""
        return 'pygson.TypeAdapterFactory'.__wrap(super(DateType, self).createDefaultsAdapterFactory())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def createAdapterFactory(self, arg0: int) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createAdapterFactory(int)"""
        return 'pygson.TypeAdapterFactory'.__wrap(super(__DateType, self).createAdapterFactory(__int.valueOf(arg0)))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def createAdapterFactory(self, arg0: int, arg1: int) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createAdapterFactory(int,int)"""
        return 'pygson.TypeAdapterFactory'.__wrap(super(__DateType, self).createAdapterFactory(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.ReflectiveTypeAdapterFactory
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.internal.bind.ReflectiveTypeAdapterFactory as __ReflectiveTypeAdapterFactory
__ReflectiveTypeAdapterFactory = __ReflectiveTypeAdapterFactory
import java.lang.Object as __object
from builtins import type
try:
    from pygson import internal
except ImportError:
    internal = __import_once__("pygson.internal")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class ReflectiveTypeAdapterFactory(pygson.__TypeAdapterFactory, pygson.TypeAdapterFactory):
    """com.google.gson.internal.bind.ReflectiveTypeAdapterFactory"""
 
    @staticmethod
    def __wrap(java_value: __ReflectiveTypeAdapterFactory) -> 'ReflectiveTypeAdapterFactory':
        return ReflectiveTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectiveTypeAdapterFactory):
        """
        Dynamic initializer for ReflectiveTypeAdapterFactory.
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

    @overload
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.ReflectiveTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'.__wrap(super(__ReflectiveTypeAdapterFactory, self).create(arg0, arg1))

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

    @overload
    def __init__(self, arg0: 'ConstructorConstructor', arg1: 'FieldNamingStrategy', arg2: 'Excluder', arg3: 'JsonAdapterAnnotationTypeAdapterFactory', arg4: 'List'):
        """public com.google.gson.internal.bind.ReflectiveTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor,com.google.gson.FieldNamingStrategy,com.google.gson.internal.Excluder,com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory,java.util.List<com.google.gson.ReflectionAccessFilter>)"""
        val = __ReflectiveTypeAdapterFactory(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.google.gson.internal.bind.ArrayTypeAdapter
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import com.google.gson.internal.bind.ArrayTypeAdapter as __ArrayTypeAdapter
__ArrayTypeAdapter = __ArrayTypeAdapter
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
 
class ArrayTypeAdapter(pygson.__TypeAdapter, pygson.TypeAdapter):
    """com.google.gson.internal.bind.ArrayTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __ArrayTypeAdapter) -> 'ArrayTypeAdapter':
        return ArrayTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayTypeAdapter):
        """
        Dynamic initializer for ArrayTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

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
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Gson', arg1: 'TypeAdapter', arg2: 'Class'):
        """public com.google.gson.internal.bind.ArrayTypeAdapter(com.google.gson.Gson,com.google.gson.TypeAdapter<E>,java.lang.Class<E>)"""
        val = __ArrayTypeAdapter(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.ArrayTypeAdapter.write(com.google.gson.stream.JsonWriter,java.lang.Object) throws java.io.IOException"""
        super(__ArrayTypeAdapter, self).write(arg0, arg1)

    @overload
    def read(self, arg0: 'JsonReader') -> object:
        """public java.lang.Object com.google.gson.internal.bind.ArrayTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object.__wrap(super(__ArrayTypeAdapter, self).read(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory as __JsonAdapterAnnotationTypeAdapterFactory
__JsonAdapterAnnotationTypeAdapterFactory = __JsonAdapterAnnotationTypeAdapterFactory
try:
    from pygson import internal
except ImportError:
    internal = __import_once__("pygson.internal")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonAdapterAnnotationTypeAdapterFactory(pygson.__TypeAdapterFactory, pygson.TypeAdapterFactory):
    """com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory"""
 
    @staticmethod
    def __wrap(java_value: __JsonAdapterAnnotationTypeAdapterFactory) -> 'JsonAdapterAnnotationTypeAdapterFactory':
        return JsonAdapterAnnotationTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonAdapterAnnotationTypeAdapterFactory):
        """
        Dynamic initializer for JsonAdapterAnnotationTypeAdapterFactory.
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

    @overload
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'.__wrap(super(__JsonAdapterAnnotationTypeAdapterFactory, self).create(arg0, arg1))

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
    def __init__(self, arg0: 'ConstructorConstructor'):
        """public com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor)"""
        val = __JsonAdapterAnnotationTypeAdapterFactory(arg0)
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
 
 
# CLASS: com.google.gson.internal.bind.TreeTypeAdapter
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.gson.TypeAdapterFactory as __TypeAdapterFactory
__TypeAdapterFactory = __TypeAdapterFactory
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import com.google.gson.internal.bind.TreeTypeAdapter as __TreeTypeAdapter
__TreeTypeAdapter = __TreeTypeAdapter
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class TreeTypeAdapter(__SerializationDelegatingTypeAdapter, SerializationDelegatingTypeAdapter):
    """com.google.gson.internal.bind.TreeTypeAdapter"""
 
    @staticmethod
    def __wrap(java_value: __TreeTypeAdapter) -> 'TreeTypeAdapter':
        return TreeTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TreeTypeAdapter):
        """
        Dynamic initializer for TreeTypeAdapter.
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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'JsonSerializer', arg1: 'JsonDeserializer', arg2: 'Gson', arg3: 'TypeToken', arg4: 'TypeAdapterFactory', arg5: bool):
        """public com.google.gson.internal.bind.TreeTypeAdapter(com.google.gson.JsonSerializer<T>,com.google.gson.JsonDeserializer<T>,com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>,com.google.gson.TypeAdapterFactory,boolean)"""
        val = __TreeTypeAdapter(arg0, arg1, arg2, arg3, arg4, __boolean.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'.__wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str.__wrap(super(__pygson.TypeAdapter, self).toJson(arg0))

    @staticmethod
    @overload
    def newFactory(arg0: 'TypeToken', arg1: object) -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TreeTypeAdapter.newFactory(com.google.gson.reflect.TypeToken<?>,java.lang.Object)"""
        return pygson.TypeAdapterFactory.__wrap(__TreeTypeAdapter.newFactory(arg0, arg1))

    @override
    @overload
    def getSerializationDelegate(self) -> 'pygson.TypeAdapter':
        """public com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.TreeTypeAdapter.getSerializationDelegate()"""
        return 'pygson.TypeAdapter'.__wrap(super(TreeTypeAdapter, self).getSerializationDelegate())

    @staticmethod
    @overload
    def newTypeHierarchyFactory(arg0: 'Class', arg1: object) -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TreeTypeAdapter.newTypeHierarchyFactory(java.lang.Class<?>,java.lang.Object)"""
        return pygson.TypeAdapterFactory.__wrap(__TreeTypeAdapter.newTypeHierarchyFactory(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'.__wrap(super(__pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(__pygson.TypeAdapter, self).toJson(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def newFactoryWithMatchRawType(arg0: 'TypeToken', arg1: object) -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TreeTypeAdapter.newFactoryWithMatchRawType(com.google.gson.reflect.TypeToken<?>,java.lang.Object)"""
        return pygson.TypeAdapterFactory.__wrap(__TreeTypeAdapter.newFactoryWithMatchRawType(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJsonTree(arg0))

    @overload
    def read(self, arg0: 'JsonReader') -> object:
        """public T com.google.gson.internal.bind.TreeTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object.__wrap(super(__TreeTypeAdapter, self).read(arg0))

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
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.TreeTypeAdapter.write(com.google.gson.stream.JsonWriter,T) throws java.io.IOException"""
        super(__TreeTypeAdapter, self).write(arg0, arg1)

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object.__wrap(super(__pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'JsonSerializer', arg1: 'JsonDeserializer', arg2: 'Gson', arg3: 'TypeToken', arg4: 'TypeAdapterFactory'):
        """public com.google.gson.internal.bind.TreeTypeAdapter(com.google.gson.JsonSerializer<T>,com.google.gson.JsonDeserializer<T>,com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>,com.google.gson.TypeAdapterFactory)"""
        val = __TreeTypeAdapter(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.bind.CollectionTypeAdapterFactory
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygson import internal
except ImportError:
    internal = __import_once__("pygson.internal")

import com.google.gson.internal.bind.CollectionTypeAdapterFactory as __CollectionTypeAdapterFactory
__CollectionTypeAdapterFactory = __CollectionTypeAdapterFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CollectionTypeAdapterFactory(pygson.__TypeAdapterFactory, pygson.TypeAdapterFactory):
    """com.google.gson.internal.bind.CollectionTypeAdapterFactory"""
 
    @staticmethod
    def __wrap(java_value: __CollectionTypeAdapterFactory) -> 'CollectionTypeAdapterFactory':
        return CollectionTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollectionTypeAdapterFactory):
        """
        Dynamic initializer for CollectionTypeAdapterFactory.
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
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.CollectionTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'.__wrap(super(__CollectionTypeAdapterFactory, self).create(arg0, arg1))

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

    @overload
    def __init__(self, arg0: 'ConstructorConstructor'):
        """public com.google.gson.internal.bind.CollectionTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor)"""
        val = __CollectionTypeAdapterFactory(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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