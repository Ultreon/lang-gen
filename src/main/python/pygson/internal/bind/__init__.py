from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import com.google.gson.internal.bind.DateTypeAdapter as _DateTypeAdapter
_DateTypeAdapter = _DateTypeAdapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Date as Date
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.util.Date as _Date
_Date = _Date
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DateTypeAdapter():
    """com.google.gson.internal.bind.DateTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _DateTypeAdapter) -> 'DateTypeAdapter':
        return DateTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DateTypeAdapter):
        """
        Dynamic initializer for DateTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DateTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DateTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.DateTypeAdapter()"""
        val = _DateTypeAdapter()
        self.__wrapper = val

    @overload
    def read(self, arg0: 'JsonReader') -> 'Date':
        """public java.util.Date com.google.gson.internal.bind.DateTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return 'Date'._wrap(super(_DateTypeAdapter, self).read(arg0))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def write(self, arg0: 'JsonWriter', arg1: 'Date'):
        """public void com.google.gson.internal.bind.DateTypeAdapter.write(com.google.gson.stream.JsonWriter,java.util.Date) throws java.io.IOException"""
        super(_DateTypeAdapter, self).write(arg0, arg1)

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.DateTypeAdapter()"""
        val = _DateTypeAdapter()
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

 
 
 
# CLASS: com.google.gson.internal.bind.DateTypeAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import com.google.gson.internal.bind.DateTypeAdapter as _DateTypeAdapter
_DateTypeAdapter = _DateTypeAdapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Date as Date
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.util.Date as _Date
_Date = _Date
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DateTypeAdapter():
    """com.google.gson.internal.bind.DateTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _DateTypeAdapter) -> 'DateTypeAdapter':
        return DateTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DateTypeAdapter):
        """
        Dynamic initializer for DateTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DateTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DateTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.DateTypeAdapter()"""
        val = _DateTypeAdapter()
        self.__wrapper = val

    @overload
    def read(self, arg0: 'JsonReader') -> 'Date':
        """public java.util.Date com.google.gson.internal.bind.DateTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return 'Date'._wrap(super(_DateTypeAdapter, self).read(arg0))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def write(self, arg0: 'JsonWriter', arg1: 'Date'):
        """public void com.google.gson.internal.bind.DateTypeAdapter.write(com.google.gson.stream.JsonWriter,java.util.Date) throws java.io.IOException"""
        super(_DateTypeAdapter, self).write(arg0, arg1)

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.DateTypeAdapter()"""
        val = _DateTypeAdapter()
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

 
 
 
# CLASS: com.google.gson.internal.bind.DateTypeAdapter 
 
 
# CLASS: com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory
from pyquantum_helper import import_once as _import_once
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pygson import internal
except ImportError:
    internal = _import_once("pygson.internal")

import com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory as _JsonAdapterAnnotationTypeAdapterFactory
_JsonAdapterAnnotationTypeAdapterFactory = _JsonAdapterAnnotationTypeAdapterFactory
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
 
class JsonAdapterAnnotationTypeAdapterFactory():
    """com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory"""
 
    @staticmethod
    def _wrap(java_value: _JsonAdapterAnnotationTypeAdapterFactory) -> 'JsonAdapterAnnotationTypeAdapterFactory':
        return JsonAdapterAnnotationTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonAdapterAnnotationTypeAdapterFactory):
        """
        Dynamic initializer for JsonAdapterAnnotationTypeAdapterFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonAdapterAnnotationTypeAdapterFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonAdapterAnnotationTypeAdapterFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'._wrap(super(_JsonAdapterAnnotationTypeAdapterFactory, self).create(arg0, arg1))

    @overload
    def __init__(self, arg0: 'ConstructorConstructor'):
        """public com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor)"""
        val = _JsonAdapterAnnotationTypeAdapterFactory(arg0)
        self.__wrapper = val

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
 
 
# CLASS: com.google.gson.internal.bind.MapTypeAdapterFactory
from pyquantum_helper import import_once as _import_once
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pygson import internal
except ImportError:
    internal = _import_once("pygson.internal")

import com.google.gson.internal.bind.MapTypeAdapterFactory as _MapTypeAdapterFactory
_MapTypeAdapterFactory = _MapTypeAdapterFactory
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
 
class MapTypeAdapterFactory():
    """com.google.gson.internal.bind.MapTypeAdapterFactory"""
 
    @staticmethod
    def _wrap(java_value: _MapTypeAdapterFactory) -> 'MapTypeAdapterFactory':
        return MapTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapTypeAdapterFactory):
        """
        Dynamic initializer for MapTypeAdapterFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapTypeAdapterFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapTypeAdapterFactory__wrapper":
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
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.MapTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'._wrap(super(_MapTypeAdapterFactory, self).create(arg0, arg1))

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
    def __init__(self, arg0: 'ConstructorConstructor', arg1: bool):
        """public com.google.gson.internal.bind.MapTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor,boolean)"""
        val = _MapTypeAdapterFactory(arg0, _boolean.valueOf(arg1))
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
 
 
# CLASS: com.google.gson.internal.bind.JsonTreeReader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from pyquantum_helper import override
import com.google.gson.stream.JsonReader as _JsonReader
_JsonReader = _JsonReader
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.stream.JsonToken as _JsonToken
_JsonToken = _JsonToken
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.google.gson.internal.bind.JsonTreeReader as _JsonTreeReader
_JsonTreeReader = _JsonTreeReader
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonTreeReader():
    """com.google.gson.internal.bind.JsonTreeReader"""
 
    @staticmethod
    def _wrap(java_value: _JsonTreeReader) -> 'JsonTreeReader':
        return JsonTreeReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonTreeReader):
        """
        Dynamic initializer for JsonTreeReader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonTreeReader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonTreeReader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isLenient(self) -> bool:
        """public final boolean com.google.gson.stream.JsonReader.isLenient()"""
        return bool._wrap(super(stream.JsonReader, self).isLenient())

    @override
    @overload
    def nextBoolean(self) -> bool:
        """public boolean com.google.gson.internal.bind.JsonTreeReader.nextBoolean() throws java.io.IOException"""
        return bool._wrap(super(JsonTreeReader, self).nextBoolean())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.toString()"""
        return str._wrap(super(JsonTreeReader, self).toString())

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
    def nextDouble(self) -> float:
        """public double com.google.gson.internal.bind.JsonTreeReader.nextDouble() throws java.io.IOException"""
        return float._wrap(super(JsonTreeReader, self).nextDouble())

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
    def close(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.close() throws java.io.IOException"""
        super(JsonTreeReader, self).close()

    @overload
    def __init__(self, arg0: 'JsonElement'):
        """public com.google.gson.internal.bind.JsonTreeReader(com.google.gson.JsonElement)"""
        val = _JsonTreeReader(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def nextString(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.nextString() throws java.io.IOException"""
        return str._wrap(super(JsonTreeReader, self).nextString())

    @override
    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonReader.setLenient(boolean)"""
        super(_stream.JsonReader, self).setLenient(_boolean.valueOf(arg0))

    @override
    @overload
    def nextName(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.nextName() throws java.io.IOException"""
        return str._wrap(super(JsonTreeReader, self).nextName())

    @override
    @overload
    def getPreviousPath(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.getPreviousPath()"""
        return str._wrap(super(JsonTreeReader, self).getPreviousPath())

    @override
    @overload
    def peek(self) -> 'stream.JsonToken':
        """public com.google.gson.stream.JsonToken com.google.gson.internal.bind.JsonTreeReader.peek() throws java.io.IOException"""
        return 'stream.JsonToken'._wrap(super(JsonTreeReader, self).peek())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.google.gson.internal.bind.JsonTreeReader.hasNext() throws java.io.IOException"""
        return bool._wrap(super(JsonTreeReader, self).hasNext())

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.JsonTreeReader.getPath()"""
        return str._wrap(super(JsonTreeReader, self).getPath())

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
    def nextInt(self) -> int:
        """public int com.google.gson.internal.bind.JsonTreeReader.nextInt() throws java.io.IOException"""
        return int._wrap(super(JsonTreeReader, self).nextInt())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.google.gson.internal.bind.JsonTreeReader.nextLong() throws java.io.IOException"""
        return int._wrap(super(JsonTreeReader, self).nextLong())

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
    def nextNull(self):
        """public void com.google.gson.internal.bind.JsonTreeReader.nextNull() throws java.io.IOException"""
        super(JsonTreeReader, self).nextNull()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.bind.NumberTypeAdapter
from pyquantum_helper import import_once as _import_once
import com.google.gson.TypeAdapterFactory as _TypeAdapterFactory
_TypeAdapterFactory = _TypeAdapterFactory
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.gson.internal.bind.NumberTypeAdapter as _NumberTypeAdapter
_NumberTypeAdapter = _NumberTypeAdapter
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NumberTypeAdapter():
    """com.google.gson.internal.bind.NumberTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _NumberTypeAdapter) -> 'NumberTypeAdapter':
        return NumberTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NumberTypeAdapter):
        """
        Dynamic initializer for NumberTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NumberTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NumberTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @staticmethod
    @overload
    def getFactory(arg0: 'ToNumberStrategy') -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.NumberTypeAdapter.getFactory(com.google.gson.ToNumberStrategy)"""
        return pygson.TypeAdapterFactory._wrap(_NumberTypeAdapter.getFactory(arg0))

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def read(self, arg0: 'JsonReader') -> 'Number':
        """public java.lang.Number com.google.gson.internal.bind.NumberTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return _transform(super(_NumberTypeAdapter, self).read(arg0)).'Number'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def write(self, arg0: 'JsonWriter', arg1: 'Number'):
        """public void com.google.gson.internal.bind.NumberTypeAdapter.write(com.google.gson.stream.JsonWriter,java.lang.Number) throws java.io.IOException"""
        super(_NumberTypeAdapter, self).write(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.bind.TypeAdapters
from pyquantum_helper import import_once as _import_once
import com.google.gson.TypeAdapterFactory as _TypeAdapterFactory
_TypeAdapterFactory = _TypeAdapterFactory
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.gson.internal.bind.TypeAdapters as _TypeAdapters
_TypeAdapters = _TypeAdapters
import java.lang.String as _String
_String = _String
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
 
class TypeAdapters():
    """com.google.gson.internal.bind.TypeAdapters"""
 
    @staticmethod
    def _wrap(java_value: _TypeAdapters) -> 'TypeAdapters':
        return TypeAdapters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeAdapters):
        """
        Dynamic initializer for TypeAdapters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeAdapters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeAdapters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def newTypeHierarchyFactory(arg0: 'Class', arg1: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <T1> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newTypeHierarchyFactory(java.lang.Class<T1>,com.google.gson.TypeAdapter<T1>)"""
        return pygson.TypeAdapterFactory._wrap(_TypeAdapters.newTypeHierarchyFactory(arg0, arg1))

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
    def newFactory(arg0: 'TypeToken', arg1: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactory(com.google.gson.reflect.TypeToken<TT>,com.google.gson.TypeAdapter<TT>)"""
        return pygson.TypeAdapterFactory._wrap(_TypeAdapters.newFactory(arg0, arg1))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def newFactory(arg0: 'Class', arg1: 'Class', arg2: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactory(java.lang.Class<TT>,java.lang.Class<TT>,com.google.gson.TypeAdapter<? super TT>)"""
        return pygson.TypeAdapterFactory._wrap(_TypeAdapters.newFactory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def newFactoryForMultipleTypes(arg0: 'Class', arg1: 'Class', arg2: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactoryForMultipleTypes(java.lang.Class<TT>,java.lang.Class<? extends TT>,com.google.gson.TypeAdapter<? super TT>)"""
        return pygson.TypeAdapterFactory._wrap(_TypeAdapters.newFactoryForMultipleTypes(arg0, arg1, arg2))

    @staticmethod
    @overload
    def newFactory(arg0: 'Class', arg1: 'TypeAdapter') -> 'pygson.TypeAdapterFactory':
        """public static <TT> com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TypeAdapters.newFactory(java.lang.Class<TT>,com.google.gson.TypeAdapter<TT>)"""
        return pygson.TypeAdapterFactory._wrap(_TypeAdapters.newFactory(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.bind.DefaultDateTypeAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

import com.google.gson.internal.bind.DefaultDateTypeAdapter as _DefaultDateTypeAdapter
_DefaultDateTypeAdapter = _DefaultDateTypeAdapter
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Date as Date
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.util.Date as _Date
_Date = _Date
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultDateTypeAdapter():
    """com.google.gson.internal.bind.DefaultDateTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _DefaultDateTypeAdapter) -> 'DefaultDateTypeAdapter':
        return DefaultDateTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultDateTypeAdapter):
        """
        Dynamic initializer for DefaultDateTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultDateTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultDateTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def write(self, arg0: 'JsonWriter', arg1: 'Date'):
        """public void com.google.gson.internal.bind.DefaultDateTypeAdapter.write(com.google.gson.stream.JsonWriter,java.util.Date) throws java.io.IOException"""
        super(_DefaultDateTypeAdapter, self).write(arg0, arg1)

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.bind.DefaultDateTypeAdapter.toString()"""
        return str._wrap(super(DefaultDateTypeAdapter, self).toString())

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

    @overload
    def read(self, arg0: 'JsonReader') -> 'Date':
        """public T com.google.gson.internal.bind.DefaultDateTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return 'Date'._wrap(super(_DefaultDateTypeAdapter, self).read(arg0))

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
 
 
# CLASS: com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType
from pyquantum_helper import import_once as _import_once
import com.google.gson.TypeAdapterFactory as _TypeAdapterFactory
_TypeAdapterFactory = _TypeAdapterFactory
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.internal.bind.DefaultDateTypeAdapter as _DefaultDateTypeAdapter_DateType
_DateType = _DefaultDateTypeAdapter_DateType.DateType
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DateType():
    """com.google.gson.internal.bind.DefaultDateTypeAdapter.DateType"""
 
    @staticmethod
    def _wrap(java_value: _DateType) -> 'DateType':
        return DateType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DateType):
        """
        Dynamic initializer for DateType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DateType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DateType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createAdapterFactory(self, arg0: str) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createAdapterFactory(java.lang.String)"""
        return 'pygson.TypeAdapterFactory'._wrap(super(_DateType, self).createAdapterFactory(arg0))

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
    def createAdapterFactory(self, arg0: int, arg1: int) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createAdapterFactory(int,int)"""
        return 'pygson.TypeAdapterFactory'._wrap(super(_DateType, self).createAdapterFactory(_int.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def createDefaultsAdapterFactory(self) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createDefaultsAdapterFactory()"""
        return 'pygson.TypeAdapterFactory'._wrap(super(DateType, self).createDefaultsAdapterFactory())

    @overload
    def createAdapterFactory(self, arg0: int) -> 'pygson.TypeAdapterFactory':
        """public final com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.DefaultDateTypeAdapter$DateType.createAdapterFactory(int)"""
        return 'pygson.TypeAdapterFactory'._wrap(super(_DateType, self).createAdapterFactory(_int.valueOf(arg0)))

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
 
 
# CLASS: com.google.gson.internal.bind.TreeTypeAdapter
from pyquantum_helper import import_once as _import_once
import com.google.gson.TypeAdapterFactory as _TypeAdapterFactory
_TypeAdapterFactory = _TypeAdapterFactory
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
import com.google.gson.internal.bind.TreeTypeAdapter as _TreeTypeAdapter
_TreeTypeAdapter = _TreeTypeAdapter
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
try:
    from pygson import reflect
except ImportError:
    reflect = _import_once("pygson.reflect")

from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TreeTypeAdapter():
    """com.google.gson.internal.bind.TreeTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _TreeTypeAdapter) -> 'TreeTypeAdapter':
        return TreeTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TreeTypeAdapter):
        """
        Dynamic initializer for TreeTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TreeTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TreeTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'JsonSerializer', arg1: 'JsonDeserializer', arg2: 'Gson', arg3: 'TypeToken', arg4: 'TypeAdapterFactory', arg5: bool):
        """public com.google.gson.internal.bind.TreeTypeAdapter(com.google.gson.JsonSerializer<T>,com.google.gson.JsonDeserializer<T>,com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>,com.google.gson.TypeAdapterFactory,boolean)"""
        val = _TreeTypeAdapter(arg0, arg1, arg2, arg3, arg4, _boolean.valueOf(arg5))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'JsonSerializer', arg1: 'JsonDeserializer', arg2: 'Gson', arg3: 'TypeToken', arg4: 'TypeAdapterFactory'):
        """public com.google.gson.internal.bind.TreeTypeAdapter(com.google.gson.JsonSerializer<T>,com.google.gson.JsonDeserializer<T>,com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>,com.google.gson.TypeAdapterFactory)"""
        val = _TreeTypeAdapter(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

    @override
    @overload
    def getSerializationDelegate(self) -> 'pygson.TypeAdapter':
        """public com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.TreeTypeAdapter.getSerializationDelegate()"""
        return 'pygson.TypeAdapter'._wrap(super(TreeTypeAdapter, self).getSerializationDelegate())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @staticmethod
    @overload
    def newFactory(arg0: 'TypeToken', arg1: object) -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TreeTypeAdapter.newFactory(com.google.gson.reflect.TypeToken<?>,java.lang.Object)"""
        return pygson.TypeAdapterFactory._wrap(_TreeTypeAdapter.newFactory(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.TreeTypeAdapter.write(com.google.gson.stream.JsonWriter,T) throws java.io.IOException"""
        super(_TreeTypeAdapter, self).write(arg0, arg1)

    @staticmethod
    @overload
    def newTypeHierarchyFactory(arg0: 'Class', arg1: object) -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TreeTypeAdapter.newTypeHierarchyFactory(java.lang.Class<?>,java.lang.Object)"""
        return pygson.TypeAdapterFactory._wrap(_TreeTypeAdapter.newTypeHierarchyFactory(arg0, arg1))

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def newFactoryWithMatchRawType(arg0: 'TypeToken', arg1: object) -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.TreeTypeAdapter.newFactoryWithMatchRawType(com.google.gson.reflect.TypeToken<?>,java.lang.Object)"""
        return pygson.TypeAdapterFactory._wrap(_TreeTypeAdapter.newFactoryWithMatchRawType(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

    @overload
    def read(self, arg0: 'JsonReader') -> object:
        """public T com.google.gson.internal.bind.TreeTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object._wrap(super(_TreeTypeAdapter, self).read(arg0))

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
 
 
# CLASS: com.google.gson.internal.bind.ArrayTypeAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.gson.internal.bind.ArrayTypeAdapter as _ArrayTypeAdapter
_ArrayTypeAdapter = _ArrayTypeAdapter
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayTypeAdapter():
    """com.google.gson.internal.bind.ArrayTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _ArrayTypeAdapter) -> 'ArrayTypeAdapter':
        return ArrayTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayTypeAdapter):
        """
        Dynamic initializer for ArrayTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Gson', arg1: 'TypeAdapter', arg2: 'Class'):
        """public com.google.gson.internal.bind.ArrayTypeAdapter(com.google.gson.Gson,com.google.gson.TypeAdapter<E>,java.lang.Class<E>)"""
        val = _ArrayTypeAdapter(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.ArrayTypeAdapter.write(com.google.gson.stream.JsonWriter,java.lang.Object) throws java.io.IOException"""
        super(_ArrayTypeAdapter, self).write(arg0, arg1)

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def read(self, arg0: 'JsonReader') -> object:
        """public java.lang.Object com.google.gson.internal.bind.ArrayTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object._wrap(super(_ArrayTypeAdapter, self).read(arg0))

    @overload
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

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
 
 
# CLASS: com.google.gson.internal.bind.ObjectTypeAdapter
from pyquantum_helper import import_once as _import_once
import com.google.gson.TypeAdapterFactory as _TypeAdapterFactory
_TypeAdapterFactory = _TypeAdapterFactory
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
import com.google.gson.internal.bind.ObjectTypeAdapter as _ObjectTypeAdapter
_ObjectTypeAdapter = _ObjectTypeAdapter
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectTypeAdapter():
    """com.google.gson.internal.bind.ObjectTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _ObjectTypeAdapter) -> 'ObjectTypeAdapter':
        return ObjectTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectTypeAdapter):
        """
        Dynamic initializer for ObjectTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getFactory(arg0: 'ToNumberStrategy') -> 'pygson.TypeAdapterFactory':
        """public static com.google.gson.TypeAdapterFactory com.google.gson.internal.bind.ObjectTypeAdapter.getFactory(com.google.gson.ToNumberStrategy)"""
        return pygson.TypeAdapterFactory._wrap(_ObjectTypeAdapter.getFactory(arg0))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.ObjectTypeAdapter.write(com.google.gson.stream.JsonWriter,java.lang.Object) throws java.io.IOException"""
        super(_ObjectTypeAdapter, self).write(arg0, arg1)

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @overload
    def read(self, arg0: 'JsonReader') -> object:
        """public java.lang.Object com.google.gson.internal.bind.ObjectTypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object._wrap(super(_ObjectTypeAdapter, self).read(arg0))

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

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
 
 
# CLASS: com.google.gson.internal.bind.ReflectiveTypeAdapterFactory
from pyquantum_helper import import_once as _import_once
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pygson import internal
except ImportError:
    internal = _import_once("pygson.internal")

import com.google.gson.internal.bind.ReflectiveTypeAdapterFactory as _ReflectiveTypeAdapterFactory
_ReflectiveTypeAdapterFactory = _ReflectiveTypeAdapterFactory
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
import java.util.List as List
 
class ReflectiveTypeAdapterFactory():
    """com.google.gson.internal.bind.ReflectiveTypeAdapterFactory"""
 
    @staticmethod
    def _wrap(java_value: _ReflectiveTypeAdapterFactory) -> 'ReflectiveTypeAdapterFactory':
        return ReflectiveTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectiveTypeAdapterFactory):
        """
        Dynamic initializer for ReflectiveTypeAdapterFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectiveTypeAdapterFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectiveTypeAdapterFactory__wrapper":
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

    @overload
    def __init__(self, arg0: 'ConstructorConstructor', arg1: 'FieldNamingStrategy', arg2: 'Excluder', arg3: 'JsonAdapterAnnotationTypeAdapterFactory', arg4: 'List'):
        """public com.google.gson.internal.bind.ReflectiveTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor,com.google.gson.FieldNamingStrategy,com.google.gson.internal.Excluder,com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory,java.util.List<com.google.gson.ReflectionAccessFilter>)"""
        val = _ReflectiveTypeAdapterFactory(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

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
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.ReflectiveTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'._wrap(super(_ReflectiveTypeAdapterFactory, self).create(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import com.google.gson.internal.bind.ReflectiveTypeAdapterFactory as _ReflectiveTypeAdapterFactory_Adapter
_Adapter = _ReflectiveTypeAdapterFactory_Adapter.Adapter
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Adapter():
    """com.google.gson.internal.bind.ReflectiveTypeAdapterFactory.Adapter"""
 
    @staticmethod
    def _wrap(java_value: _Adapter) -> 'Adapter':
        return Adapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Adapter):
        """
        Dynamic initializer for Adapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Adapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Adapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def read(self, arg0: 'JsonReader') -> object:
        """public T com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        return object._wrap(super(_Adapter, self).read(arg0))

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @override
    @overload
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public void com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter.write(com.google.gson.stream.JsonWriter,T) throws java.io.IOException"""
        super(_Adapter, self).write(arg0, arg1)

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

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
 
 
# CLASS: com.google.gson.internal.bind.SerializationDelegatingTypeAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
import com.google.gson.internal.bind.SerializationDelegatingTypeAdapter as _SerializationDelegatingTypeAdapter
_SerializationDelegatingTypeAdapter = _SerializationDelegatingTypeAdapter
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SerializationDelegatingTypeAdapter():
    """com.google.gson.internal.bind.SerializationDelegatingTypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _SerializationDelegatingTypeAdapter) -> 'SerializationDelegatingTypeAdapter':
        return SerializationDelegatingTypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SerializationDelegatingTypeAdapter):
        """
        Dynamic initializer for SerializationDelegatingTypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SerializationDelegatingTypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SerializationDelegatingTypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.SerializationDelegatingTypeAdapter()"""
        val = _SerializationDelegatingTypeAdapter()
        self.__wrapper = val

    @override
    @overload
    def nullSafe(self) -> 'pygson.TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'pygson.TypeAdapter'._wrap(super(pygson.TypeAdapter, self).nullSafe())

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
    def fromJsonTree(self, arg0: 'JsonElement') -> object:
        """public final T com.google.gson.TypeAdapter.fromJsonTree(com.google.gson.JsonElement)"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJsonTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def getSerializationDelegate(self, ):
        """public abstract com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.SerializationDelegatingTypeAdapter.getSerializationDelegate()"""
        pass

    @override
    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_pygson.TypeAdapter, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

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

    @abstractmethod
    def write(self, arg0: 'JsonWriter', arg1: object):
        """public abstract void com.google.gson.TypeAdapter.write(com.google.gson.stream.JsonWriter,T) throws java.io.IOException"""
        pass

    @overload
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_pygson.TypeAdapter, self).fromJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.SerializationDelegatingTypeAdapter()"""
        val = _SerializationDelegatingTypeAdapter()
        self.__wrapper = val

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_pygson.TypeAdapter, self).toJson(arg0))

    @abstractmethod
    def read(self, arg0: 'JsonReader'):
        """public abstract T com.google.gson.TypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass

    @overload
    def toJsonTree(self, arg0: object) -> 'pygson.JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'pygson.JsonElement'._wrap(super(_pygson.TypeAdapter, self).toJsonTree(arg0))

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
 
 
# CLASS: com.google.gson.internal.bind.CollectionTypeAdapterFactory
from pyquantum_helper import import_once as _import_once
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.internal.bind.CollectionTypeAdapterFactory as _CollectionTypeAdapterFactory
_CollectionTypeAdapterFactory = _CollectionTypeAdapterFactory
import java.lang.String as _String
_String = _String
try:
    from pygson import internal
except ImportError:
    internal = _import_once("pygson.internal")

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
 
class CollectionTypeAdapterFactory():
    """com.google.gson.internal.bind.CollectionTypeAdapterFactory"""
 
    @staticmethod
    def _wrap(java_value: _CollectionTypeAdapterFactory) -> 'CollectionTypeAdapterFactory':
        return CollectionTypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollectionTypeAdapterFactory):
        """
        Dynamic initializer for CollectionTypeAdapterFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollectionTypeAdapterFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollectionTypeAdapterFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ConstructorConstructor'):
        """public com.google.gson.internal.bind.CollectionTypeAdapterFactory(com.google.gson.internal.ConstructorConstructor)"""
        val = _CollectionTypeAdapterFactory(arg0)
        self.__wrapper = val

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

    @overload
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.bind.CollectionTypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'._wrap(super(_CollectionTypeAdapterFactory, self).create(arg0, arg1))

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
 
 
# CLASS: com.google.gson.internal.bind.JsonTreeWriter
from pyquantum_helper import import_once as _import_once
import java.lang.Boolean as Boolean
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
import java.lang.Number as Number
import java.lang.Double as _double
from pyquantum_helper import override
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.gson.stream.JsonWriter as _JsonWriter
_JsonWriter = _JsonWriter
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.google.gson.internal.bind.JsonTreeWriter as _JsonTreeWriter
_JsonTreeWriter = _JsonTreeWriter
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonTreeWriter():
    """com.google.gson.internal.bind.JsonTreeWriter"""
 
    @staticmethod
    def _wrap(java_value: _JsonTreeWriter) -> 'JsonTreeWriter':
        return JsonTreeWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonTreeWriter):
        """
        Dynamic initializer for JsonTreeWriter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonTreeWriter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonTreeWriter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def jsonValue(self, arg0: str) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.jsonValue(java.lang.String) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).jsonValue(arg0))

    @override
    @overload
    def isLenient(self) -> bool:
        """public boolean com.google.gson.stream.JsonWriter.isLenient()"""
        return bool._wrap(super(stream.JsonWriter, self).isLenient())

    @overload
    def value(self, arg0: float) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(double) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).value(_double.valueOf(arg0)))

    @override
    @overload
    def beginObject(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.beginObject() throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(JsonTreeWriter, self).beginObject())

    @overload
    def value(self, arg0: int) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(long) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).value(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.JsonTreeWriter()"""
        val = _JsonTreeWriter()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def isHtmlSafe(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.isHtmlSafe()"""
        return bool._wrap(super(stream.JsonWriter, self).isHtmlSafe())

    @overload
    def value(self, arg0: float) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(float) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).value(_float.valueOf(arg0)))

    @overload
    def get(self) -> 'pygson.JsonElement':
        """public com.google.gson.JsonElement com.google.gson.internal.bind.JsonTreeWriter.get()"""
        return 'pygson.JsonElement'._wrap(super(JsonTreeWriter, self).get())

    @overload
    def value(self, arg0: str) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(java.lang.String) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).value(arg0))

    @override
    @overload
    def setHtmlSafe(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setHtmlSafe(boolean)"""
        super(_stream.JsonWriter, self).setHtmlSafe(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setSerializeNulls(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setSerializeNulls(boolean)"""
        super(_stream.JsonWriter, self).setSerializeNulls(_boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.JsonTreeWriter()"""
        val = _JsonTreeWriter()
        self.__wrapper = val

    @override
    @overload
    def getSerializeNulls(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.getSerializeNulls()"""
        return bool._wrap(super(stream.JsonWriter, self).getSerializeNulls())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def value(self, arg0: 'Number') -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(java.lang.Number) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).value(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setIndent(self, arg0: str):
        """public final void com.google.gson.stream.JsonWriter.setIndent(java.lang.String)"""
        super(_stream.JsonWriter, self).setIndent(arg0)

    @override
    @overload
    def endArray(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.endArray() throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(JsonTreeWriter, self).endArray())

    @overload
    def name(self, arg0: str) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.name(java.lang.String) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).name(arg0))

    @override
    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setLenient(boolean)"""
        super(_stream.JsonWriter, self).setLenient(_boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def value(self, arg0: bool) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(boolean) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).value(_boolean.valueOf(arg0)))

    @override
    @overload
    def beginArray(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.beginArray() throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(JsonTreeWriter, self).beginArray())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def endObject(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.endObject() throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(JsonTreeWriter, self).endObject())

    @overload
    def value(self, arg0: 'Boolean') -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.value(java.lang.Boolean) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_JsonTreeWriter, self).value(arg0))

    @override
    @overload
    def close(self):
        """public void com.google.gson.internal.bind.JsonTreeWriter.close() throws java.io.IOException"""
        super(JsonTreeWriter, self).close()

    @override
    @overload
    def nullValue(self) -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.internal.bind.JsonTreeWriter.nullValue() throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(JsonTreeWriter, self).nullValue())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())