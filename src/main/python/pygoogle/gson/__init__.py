from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.reflect.Type as Type
import com.google.gson.internal.Excluder as _Excluder
_Excluder = _Excluder
import java.lang.String as _string
try:
    from pygson import reflect
except ImportError:
    reflect = _import_once("pygson.reflect")

from builtins import bool
import com.google.gson.GsonBuilder as _GsonBuilder
_GsonBuilder = _GsonBuilder
from builtins import str
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import com.google.gson.stream.JsonReader as _JsonReader
_JsonReader = _JsonReader
import java.lang.Object as _object
import com.google.gson.Gson as _Gson
_Gson = _Gson
import java.lang.String as _String
_String = _String
from builtins import object
try:
    from pygson import internal
except ImportError:
    internal = _import_once("pygson.internal")

import com.google.gson.stream.JsonWriter as _JsonWriter
_JsonWriter = _JsonWriter
import java.lang.Appendable as Appendable
import com.google.gson.FieldNamingStrategy as _FieldNamingStrategy
_FieldNamingStrategy = _FieldNamingStrategy
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Gson():
    """com.google.gson.Gson"""
 
    @staticmethod
    def _wrap(java_value: _Gson) -> 'Gson':
        return Gson(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Gson):
        """
        Dynamic initializer for Gson.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Gson__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Gson__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def fromJson(self, arg0: str, arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: object) -> str:
        """public java.lang.String com.google.gson.Gson.toJson(java.lang.Object)"""
        return str._wrap(super(_Gson, self).toJson(arg0))

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def excluder(self) -> 'internal.Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.Gson.excluder()"""
        return 'internal.Excluder'._wrap(super(Gson, self).excluder())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def fromJson(self, arg0: str, arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJsonTree(self, arg0: object, arg1: 'Type') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.Gson.toJsonTree(java.lang.Object,java.lang.reflect.Type)"""
        return 'JsonElement'._wrap(super(_Gson, self).toJsonTree(arg0, arg1))

    @overload
    def toJson(self, arg0: object, arg1: 'Type', arg2: 'Appendable'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1, arg2)

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,java.lang.reflect.Type) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

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
    def newJsonWriter(self, arg0: 'Writer') -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.Gson.newJsonWriter(java.io.Writer) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_Gson, self).newJsonWriter(arg0))

    @overload
    def htmlSafe(self) -> bool:
        """public boolean com.google.gson.Gson.htmlSafe()"""
        return bool._wrap(super(Gson, self).htmlSafe())

    @overload
    def newJsonReader(self, arg0: 'Reader') -> 'stream.JsonReader':
        """public com.google.gson.stream.JsonReader com.google.gson.Gson.newJsonReader(java.io.Reader)"""
        return 'stream.JsonReader'._wrap(super(_Gson, self).newJsonReader(arg0))

    @overload
    def fromJson(self, arg0: str, arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,java.lang.reflect.Type) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: 'JsonElement', arg1: 'JsonWriter'):
        """public void com.google.gson.Gson.toJson(com.google.gson.JsonElement,com.google.gson.stream.JsonWriter) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1)

    @overload
    def __init__(self):
        """public com.google.gson.Gson()"""
        val = _Gson()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getDelegateAdapter(self, arg0: 'TypeAdapterFactory', arg1: 'TypeToken') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getDelegateAdapter(com.google.gson.TypeAdapterFactory,com.google.gson.reflect.TypeToken<T>)"""
        return 'TypeAdapter'._wrap(super(_Gson, self).getDelegateAdapter(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException,com.google.gson.JsonIOException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'JsonReader', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.stream.JsonReader,java.lang.reflect.Type) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def getAdapter(self, arg0: 'TypeToken') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getAdapter(com.google.gson.reflect.TypeToken<T>)"""
        return 'TypeAdapter'._wrap(super(_Gson, self).getAdapter(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,java.lang.reflect.Type) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def getAdapter(self, arg0: 'Class') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getAdapter(java.lang.Class<T>)"""
        return 'TypeAdapter'._wrap(super(_Gson, self).getAdapter(arg0))

    @overload
    def newBuilder(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.Gson.newBuilder()"""
        return 'GsonBuilder'._wrap(super(Gson, self).newBuilder())

    @overload
    def fromJson(self, arg0: 'JsonReader', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.stream.JsonReader,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: object, arg1: 'Appendable'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1)

    @overload
    def toJsonTree(self, arg0: object) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.Gson.toJsonTree(java.lang.Object)"""
        return 'JsonElement'._wrap(super(_Gson, self).toJsonTree(arg0))

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: 'JsonElement', arg1: 'Appendable'):
        """public void com.google.gson.Gson.toJson(com.google.gson.JsonElement,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object, arg1: 'Type', arg2: 'JsonWriter'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type,com.google.gson.stream.JsonWriter) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.Gson.toString()"""
        return str._wrap(super(Gson, self).toString())

    @overload
    def fieldNamingStrategy(self) -> 'FieldNamingStrategy':
        """public com.google.gson.FieldNamingStrategy com.google.gson.Gson.fieldNamingStrategy()"""
        return 'FieldNamingStrategy'._wrap(super(Gson, self).fieldNamingStrategy())

    @overload
    def toJson(self, arg0: 'JsonElement') -> str:
        """public java.lang.String com.google.gson.Gson.toJson(com.google.gson.JsonElement)"""
        return str._wrap(super(_Gson, self).toJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.gson.Gson()"""
        val = _Gson()
        self.__wrapper = val

    @overload
    def serializeNulls(self) -> bool:
        """public boolean com.google.gson.Gson.serializeNulls()"""
        return bool._wrap(super(Gson, self).serializeNulls())

    @overload
    def toJson(self, arg0: object, arg1: 'Type') -> str:
        """public java.lang.String com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type)"""
        return str._wrap(super(_Gson, self).toJson(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.Gson
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.reflect.Type as Type
import com.google.gson.internal.Excluder as _Excluder
_Excluder = _Excluder
import java.lang.String as _string
try:
    from pygson import reflect
except ImportError:
    reflect = _import_once("pygson.reflect")

from builtins import bool
import com.google.gson.GsonBuilder as _GsonBuilder
_GsonBuilder = _GsonBuilder
from builtins import str
from pyquantum_helper import override
import com.google.gson.TypeAdapter as _TypeAdapter
_TypeAdapter = _TypeAdapter
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import com.google.gson.stream.JsonReader as _JsonReader
_JsonReader = _JsonReader
import java.lang.Object as _object
import com.google.gson.Gson as _Gson
_Gson = _Gson
import java.lang.String as _String
_String = _String
from builtins import object
try:
    from pygson import internal
except ImportError:
    internal = _import_once("pygson.internal")

import com.google.gson.stream.JsonWriter as _JsonWriter
_JsonWriter = _JsonWriter
import java.lang.Appendable as Appendable
import com.google.gson.FieldNamingStrategy as _FieldNamingStrategy
_FieldNamingStrategy = _FieldNamingStrategy
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Gson():
    """com.google.gson.Gson"""
 
    @staticmethod
    def _wrap(java_value: _Gson) -> 'Gson':
        return Gson(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Gson):
        """
        Dynamic initializer for Gson.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Gson__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Gson__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def fromJson(self, arg0: str, arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: object) -> str:
        """public java.lang.String com.google.gson.Gson.toJson(java.lang.Object)"""
        return str._wrap(super(_Gson, self).toJson(arg0))

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def excluder(self) -> 'internal.Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.Gson.excluder()"""
        return 'internal.Excluder'._wrap(super(Gson, self).excluder())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def fromJson(self, arg0: str, arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJsonTree(self, arg0: object, arg1: 'Type') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.Gson.toJsonTree(java.lang.Object,java.lang.reflect.Type)"""
        return 'JsonElement'._wrap(super(_Gson, self).toJsonTree(arg0, arg1))

    @overload
    def toJson(self, arg0: object, arg1: 'Type', arg2: 'Appendable'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1, arg2)

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,java.lang.reflect.Type) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

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
    def newJsonWriter(self, arg0: 'Writer') -> 'stream.JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.Gson.newJsonWriter(java.io.Writer) throws java.io.IOException"""
        return 'stream.JsonWriter'._wrap(super(_Gson, self).newJsonWriter(arg0))

    @overload
    def htmlSafe(self) -> bool:
        """public boolean com.google.gson.Gson.htmlSafe()"""
        return bool._wrap(super(Gson, self).htmlSafe())

    @overload
    def newJsonReader(self, arg0: 'Reader') -> 'stream.JsonReader':
        """public com.google.gson.stream.JsonReader com.google.gson.Gson.newJsonReader(java.io.Reader)"""
        return 'stream.JsonReader'._wrap(super(_Gson, self).newJsonReader(arg0))

    @overload
    def fromJson(self, arg0: str, arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.lang.String,java.lang.reflect.Type) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: 'JsonElement', arg1: 'JsonWriter'):
        """public void com.google.gson.Gson.toJson(com.google.gson.JsonElement,com.google.gson.stream.JsonWriter) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1)

    @overload
    def __init__(self):
        """public com.google.gson.Gson()"""
        val = _Gson()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getDelegateAdapter(self, arg0: 'TypeAdapterFactory', arg1: 'TypeToken') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getDelegateAdapter(com.google.gson.TypeAdapterFactory,com.google.gson.reflect.TypeToken<T>)"""
        return 'TypeAdapter'._wrap(super(_Gson, self).getDelegateAdapter(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'Class') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,java.lang.Class<T>) throws com.google.gson.JsonSyntaxException,com.google.gson.JsonIOException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'JsonReader', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.stream.JsonReader,java.lang.reflect.Type) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def getAdapter(self, arg0: 'TypeToken') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getAdapter(com.google.gson.reflect.TypeToken<T>)"""
        return 'TypeAdapter'._wrap(super(_Gson, self).getAdapter(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'Type') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,java.lang.reflect.Type) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def getAdapter(self, arg0: 'Class') -> 'TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.Gson.getAdapter(java.lang.Class<T>)"""
        return 'TypeAdapter'._wrap(super(_Gson, self).getAdapter(arg0))

    @overload
    def newBuilder(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.Gson.newBuilder()"""
        return 'GsonBuilder'._wrap(super(Gson, self).newBuilder())

    @overload
    def fromJson(self, arg0: 'JsonReader', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.stream.JsonReader,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: object, arg1: 'Appendable'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1)

    @overload
    def toJsonTree(self, arg0: object) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.Gson.toJsonTree(java.lang.Object)"""
        return 'JsonElement'._wrap(super(_Gson, self).toJsonTree(arg0))

    @overload
    def fromJson(self, arg0: 'Reader', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(java.io.Reader,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: 'JsonElement', arg1: 'Appendable'):
        """public void com.google.gson.Gson.toJson(com.google.gson.JsonElement,java.lang.Appendable) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: 'JsonElement', arg1: 'TypeToken') -> object:
        """public <T> T com.google.gson.Gson.fromJson(com.google.gson.JsonElement,com.google.gson.reflect.TypeToken<T>) throws com.google.gson.JsonSyntaxException"""
        return object._wrap(super(_Gson, self).fromJson(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toJson(self, arg0: object, arg1: 'Type', arg2: 'JsonWriter'):
        """public void com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type,com.google.gson.stream.JsonWriter) throws com.google.gson.JsonIOException"""
        super(_Gson, self).toJson(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.Gson.toString()"""
        return str._wrap(super(Gson, self).toString())

    @overload
    def fieldNamingStrategy(self) -> 'FieldNamingStrategy':
        """public com.google.gson.FieldNamingStrategy com.google.gson.Gson.fieldNamingStrategy()"""
        return 'FieldNamingStrategy'._wrap(super(Gson, self).fieldNamingStrategy())

    @overload
    def toJson(self, arg0: 'JsonElement') -> str:
        """public java.lang.String com.google.gson.Gson.toJson(com.google.gson.JsonElement)"""
        return str._wrap(super(_Gson, self).toJson(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.gson.Gson()"""
        val = _Gson()
        self.__wrapper = val

    @overload
    def serializeNulls(self) -> bool:
        """public boolean com.google.gson.Gson.serializeNulls()"""
        return bool._wrap(super(Gson, self).serializeNulls())

    @overload
    def toJson(self, arg0: object, arg1: 'Type') -> str:
        """public java.lang.String com.google.gson.Gson.toJson(java.lang.Object,java.lang.reflect.Type)"""
        return str._wrap(super(_Gson, self).toJson(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.Gson 
 
 
# CLASS: com.google.gson.FieldNamingPolicy
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.reflect.Field as Field
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import com.google.gson.FieldNamingPolicy as _FieldNamingPolicy
_FieldNamingPolicy = _FieldNamingPolicy
import com.google.gson.FieldNamingStrategy as _FieldNamingStrategy
_FieldNamingStrategy = _FieldNamingStrategy
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FieldNamingPolicy():
    """com.google.gson.FieldNamingPolicy"""
 
    @staticmethod
    def _wrap(java_value: _FieldNamingPolicy) -> 'FieldNamingPolicy':
        return FieldNamingPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldNamingPolicy):
        """
        Dynamic initializer for FieldNamingPolicy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldNamingPolicy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldNamingPolicy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FieldNamingPolicy':
        """public static com.google.gson.FieldNamingPolicy com.google.gson.FieldNamingPolicy.valueOf(java.lang.String)"""
        return FieldNamingPolicy._wrap(_FieldNamingPolicy.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @abstractmethod
    def translateName(self, arg0: 'Field'):
        """public abstract java.lang.String com.google.gson.FieldNamingStrategy.translateName(java.lang.reflect.Field)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['FieldNamingPolicy']:
        """public static com.google.gson.FieldNamingPolicy[] com.google.gson.FieldNamingPolicy.values()"""
        return List[FieldNamingPolicy]._wrap(_FieldNamingPolicy.values()) 
 
 
# CLASS: com.google.gson.TypeAdapterFactory
from pyquantum_helper import import_once as _import_once
import com.google.gson.TypeAdapterFactory as _TypeAdapterFactory
_TypeAdapterFactory = _TypeAdapterFactory
try:
    from pygson import reflect
except ImportError:
    reflect = _import_once("pygson.reflect")

from abc import abstractmethod, ABC
 
class TypeAdapterFactory():
    """com.google.gson.TypeAdapterFactory"""
 
    @staticmethod
    def _wrap(java_value: _TypeAdapterFactory) -> 'TypeAdapterFactory':
        return TypeAdapterFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeAdapterFactory):
        """
        Dynamic initializer for TypeAdapterFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeAdapterFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeAdapterFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, arg0: 'Gson', arg1: 'TypeToken'):
        """public abstract <T> com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapterFactory.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        pass 
 
 
# CLASS: com.google.gson.JsonSerializationContext
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
import com.google.gson.JsonSerializationContext as _JsonSerializationContext
_JsonSerializationContext = _JsonSerializationContext
 
class JsonSerializationContext():
    """com.google.gson.JsonSerializationContext"""
 
    @staticmethod
    def _wrap(java_value: _JsonSerializationContext) -> 'JsonSerializationContext':
        return JsonSerializationContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonSerializationContext):
        """
        Dynamic initializer for JsonSerializationContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonSerializationContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonSerializationContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.gson.JsonParseException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import com.google.gson.JsonParseException as _JsonParseException
_JsonParseException = _JsonParseException
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonParseException():
    """com.google.gson.JsonParseException"""
 
    @staticmethod
    def _wrap(java_value: _JsonParseException) -> 'JsonParseException':
        return JsonParseException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonParseException):
        """
        Dynamic initializer for JsonParseException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonParseException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonParseException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonParseException(java.lang.String)"""
        val = _JsonParseException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.JsonParseException(java.lang.Throwable)"""
        val = _JsonParseException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.JsonParseException(java.lang.String,java.lang.Throwable)"""
        val = _JsonParseException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.LongSerializationPolicy
from builtins import str
import java.lang.Long as Long
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.google.gson.LongSerializationPolicy as _LongSerializationPolicy
_LongSerializationPolicy = _LongSerializationPolicy
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongSerializationPolicy():
    """com.google.gson.LongSerializationPolicy"""
 
    @staticmethod
    def _wrap(java_value: _LongSerializationPolicy) -> 'LongSerializationPolicy':
        return LongSerializationPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongSerializationPolicy):
        """
        Dynamic initializer for LongSerializationPolicy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongSerializationPolicy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongSerializationPolicy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['LongSerializationPolicy']:
        """public static com.google.gson.LongSerializationPolicy[] com.google.gson.LongSerializationPolicy.values()"""
        return List[LongSerializationPolicy]._wrap(_LongSerializationPolicy.values())

    @abstractmethod
    def serialize(self, arg0: 'Long'):
        """public abstract com.google.gson.JsonElement com.google.gson.LongSerializationPolicy.serialize(java.lang.Long)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'LongSerializationPolicy':
        """public static com.google.gson.LongSerializationPolicy com.google.gson.LongSerializationPolicy.valueOf(java.lang.String)"""
        return LongSerializationPolicy._wrap(_LongSerializationPolicy.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.gson.JsonStreamParser
from builtins import str
from pyquantum_helper import override
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
import com.google.gson.JsonStreamParser as _JsonStreamParser
_JsonStreamParser = _JsonStreamParser
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonStreamParser():
    """com.google.gson.JsonStreamParser"""
 
    @staticmethod
    def _wrap(java_value: _JsonStreamParser) -> 'JsonStreamParser':
        return JsonStreamParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonStreamParser):
        """
        Dynamic initializer for JsonStreamParser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonStreamParser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonStreamParser__wrapper":
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
    def next(self) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonStreamParser.next() throws com.google.gson.JsonParseException"""
        return 'JsonElement'._wrap(super(JsonStreamParser, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonStreamParser(java.lang.String)"""
        val = _JsonStreamParser(arg0)
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.google.gson.JsonStreamParser.hasNext()"""
        return bool._wrap(super(JsonStreamParser, self).hasNext())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

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

    @overload
    def __init__(self, arg0: 'Reader'):
        """public com.google.gson.JsonStreamParser(java.io.Reader)"""
        val = _JsonStreamParser(arg0)
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
 
 
# CLASS: com.google.gson.JsonElement
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import com.google.gson.JsonObject as _JsonObject
_JsonObject = _JsonObject
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.google.gson.JsonArray as _JsonArray
_JsonArray = _JsonArray
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import com.google.gson.JsonPrimitive as _JsonPrimitive
_JsonPrimitive = _JsonPrimitive
import java.math.BigDecimal as BigDecimal
from builtins import bool
import com.google.gson.JsonNull as _JsonNull
_JsonNull = _JsonNull
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonElement():
    """com.google.gson.JsonElement"""
 
    @staticmethod
    def _wrap(java_value: _JsonElement) -> 'JsonElement':
        return JsonElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonElement):
        """
        Dynamic initializer for JsonElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonElement.getAsLong()"""
        return int._wrap(super(JsonElement, self).getAsLong())

    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonElement.getAsBoolean()"""
        return bool._wrap(super(JsonElement, self).getAsBoolean())

    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonElement.getAsBigDecimal()"""
        return _transform(super(JsonElement, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonElement.getAsDouble()"""
        return float._wrap(super(JsonElement, self).getAsDouble())

    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonElement.getAsInt()"""
        return int._wrap(super(JsonElement, self).getAsInt())

    @abstractmethod
    def deepCopy(self, ):
        """public abstract com.google.gson.JsonElement com.google.gson.JsonElement.deepCopy()"""
        pass

    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool._wrap(super(JsonElement, self).isJsonArray())

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonElement()"""
        val = _JsonElement()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool._wrap(super(JsonElement, self).isJsonObject())

    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'._wrap(super(JsonElement, self).getAsJsonNull())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonElement.getAsFloat()"""
        return float._wrap(super(JsonElement, self).getAsFloat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'._wrap(super(JsonElement, self).getAsJsonObject())

    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonElement.getAsNumber()"""
        return _transform(super(JsonElement, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool._wrap(super(JsonElement, self).isJsonNull())

    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonElement.getAsBigInteger()"""
        return _transform(super(JsonElement, self).getAsBigInteger()).'BigInteger'Value()

    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'._wrap(super(JsonElement, self).getAsJsonPrimitive())

    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonElement.getAsShort()"""
        return int._wrap(super(JsonElement, self).getAsShort())

    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool._wrap(super(JsonElement, self).isJsonPrimitive())

    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.getAsString()"""
        return str._wrap(super(JsonElement, self).getAsString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.google.gson.JsonElement()"""
        val = _JsonElement()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str._wrap(super(JsonElement, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonElement.getAsByte()"""
        return int._wrap(super(JsonElement, self).getAsByte())

    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonElement.getAsCharacter()"""
        return str._wrap(super(JsonElement, self).getAsCharacter())

    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'._wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.ReflectionAccessFilter
import com.google.gson.ReflectionAccessFilter as _ReflectionAccessFilter
_ReflectionAccessFilter = _ReflectionAccessFilter
from builtins import type
from abc import abstractmethod, ABC
 
class ReflectionAccessFilter():
    """com.google.gson.ReflectionAccessFilter"""
 
    @staticmethod
    def _wrap(java_value: _ReflectionAccessFilter) -> 'ReflectionAccessFilter':
        return ReflectionAccessFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectionAccessFilter):
        """
        Dynamic initializer for ReflectionAccessFilter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectionAccessFilter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectionAccessFilter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def check(self, arg0: 'Class'):
        """public abstract com.google.gson.ReflectionAccessFilter$FilterResult com.google.gson.ReflectionAccessFilter.check(java.lang.Class<?>)"""
        pass 
 
 
# CLASS: com.google.gson.InstanceCreator
import com.google.gson.InstanceCreator as _InstanceCreator
_InstanceCreator = _InstanceCreator
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
 
class InstanceCreator():
    """com.google.gson.InstanceCreator"""
 
    @staticmethod
    def _wrap(java_value: _InstanceCreator) -> 'InstanceCreator':
        return InstanceCreator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InstanceCreator):
        """
        Dynamic initializer for InstanceCreator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InstanceCreator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InstanceCreator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def createInstance(self, arg0: 'Type'):
        """public abstract T com.google.gson.InstanceCreator.createInstance(java.lang.reflect.Type)"""
        pass 
 
 
# CLASS: com.google.gson.JsonObject
import com.google.gson.JsonObject as _JsonObject
_JsonObject = _JsonObject
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import com.google.gson.JsonArray as _JsonArray
_JsonArray = _JsonArray
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import com.google.gson.JsonPrimitive as _JsonPrimitive
_JsonPrimitive = _JsonPrimitive
import java.lang.Character as Character
from builtins import bool
import com.google.gson.JsonNull as _JsonNull
_JsonNull = _JsonNull
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.Set as Set
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.math.BigDecimal as BigDecimal
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonObject():
    """com.google.gson.JsonObject"""
 
    @staticmethod
    def _wrap(java_value: _JsonObject) -> 'JsonObject':
        return JsonObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonObject):
        """
        Dynamic initializer for JsonObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonElement.getAsNumber()"""
        return _transform(super(JsonElement, self).getAsNumber()).'Number'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonObject.equals(java.lang.Object)"""
        return bool._wrap(super(_JsonObject, self).equals(arg0))

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonElement.getAsFloat()"""
        return float._wrap(super(JsonElement, self).getAsFloat())

    @override
    @overload
    def deepCopy(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonObject.deepCopy()"""
        return 'JsonObject'._wrap(super(JsonObject, self).deepCopy())

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'._wrap(super(JsonElement, self).getAsJsonObject())

    @override
    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool._wrap(super(JsonElement, self).isJsonArray())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addProperty(self, arg0: str, arg1: 'Character'):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.Character)"""
        super(_JsonObject, self).addProperty(arg0, arg1)

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonElement.getAsBoolean()"""
        return bool._wrap(super(JsonElement, self).getAsBoolean())

    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonElement.getAsBigInteger()"""
        return _transform(super(JsonElement, self).getAsBigInteger()).'BigInteger'Value()

    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<java.lang.String, com.google.gson.JsonElement>> com.google.gson.JsonObject.entrySet()"""
        return 'Set'._wrap(super(JsonObject, self).entrySet())

    @overload
    def getAsJsonObject(self, arg0: str) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonObject.getAsJsonObject(java.lang.String)"""
        return 'JsonObject'._wrap(super(_JsonObject, self).getAsJsonObject(arg0))

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonElement.getAsInt()"""
        return int._wrap(super(JsonElement, self).getAsInt())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonObject.hashCode()"""
        return int._wrap(super(JsonObject, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addProperty(self, arg0: str, arg1: 'Boolean'):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.Boolean)"""
        super(_JsonObject, self).addProperty(arg0, arg1)

    @overload
    def addProperty(self, arg0: str, arg1: 'Number'):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.Number)"""
        super(_JsonObject, self).addProperty(arg0, arg1)

    @overload
    def addProperty(self, arg0: str, arg1: str):
        """public void com.google.gson.JsonObject.addProperty(java.lang.String,java.lang.String)"""
        super(_JsonObject, self).addProperty(arg0, arg1)

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool._wrap(super(JsonElement, self).isJsonObject())

    @overload
    def remove(self, arg0: str) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonObject.remove(java.lang.String)"""
        return 'JsonElement'._wrap(super(_JsonObject, self).remove(arg0))

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonElement.getAsCharacter()"""
        return str._wrap(super(JsonElement, self).getAsCharacter())

    @overload
    def get(self, arg0: str) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonObject.get(java.lang.String)"""
        return 'JsonElement'._wrap(super(_JsonObject, self).get(arg0))

    @overload
    def has(self, arg0: str) -> bool:
        """public boolean com.google.gson.JsonObject.has(java.lang.String)"""
        return bool._wrap(super(_JsonObject, self).has(arg0))

    @override
    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonElement.getAsBigDecimal()"""
        return _transform(super(JsonElement, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'._wrap(super(JsonElement, self).getAsJsonPrimitive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAsJsonArray(self, arg0: str) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonObject.getAsJsonArray(java.lang.String)"""
        return 'JsonArray'._wrap(super(_JsonObject, self).getAsJsonArray(arg0))

    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonElement.getAsByte()"""
        return int._wrap(super(JsonElement, self).getAsByte())

    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, com.google.gson.JsonElement> com.google.gson.JsonObject.asMap()"""
        return 'Map'._wrap(super(JsonObject, self).asMap())

    @override
    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonElement.getAsDouble()"""
        return float._wrap(super(JsonElement, self).getAsDouble())

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonElement.getAsLong()"""
        return int._wrap(super(JsonElement, self).getAsLong())

    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<java.lang.String> com.google.gson.JsonObject.keySet()"""
        return 'Set'._wrap(super(JsonObject, self).keySet())

    @overload
    def getAsJsonPrimitive(self, arg0: str) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonObject.getAsJsonPrimitive(java.lang.String)"""
        return 'JsonPrimitive'._wrap(super(_JsonObject, self).getAsJsonPrimitive(arg0))

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.getAsString()"""
        return str._wrap(super(JsonElement, self).getAsString())

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonObject()"""
        val = _JsonObject()
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.gson.JsonObject.isEmpty()"""
        return bool._wrap(super(JsonObject, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def size(self) -> int:
        """public int com.google.gson.JsonObject.size()"""
        return int._wrap(super(JsonObject, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str._wrap(super(JsonElement, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: str, arg1: 'JsonElement'):
        """public void com.google.gson.JsonObject.add(java.lang.String,com.google.gson.JsonElement)"""
        super(_JsonObject, self).add(arg0, arg1)

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool._wrap(super(JsonElement, self).isJsonPrimitive())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'._wrap(super(JsonElement, self).getAsJsonNull())

    @overload
    def __init__(self):
        """public com.google.gson.JsonObject()"""
        val = _JsonObject()
        self.__wrapper = val

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'._wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool._wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonElement.getAsShort()"""
        return int._wrap(super(JsonElement, self).getAsShort()) 
 
 
# CLASS: com.google.gson.GsonBuilder
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.Gson as _Gson
_Gson = _Gson
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.google.gson.GsonBuilder as _GsonBuilder
_GsonBuilder = _GsonBuilder
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GsonBuilder():
    """com.google.gson.GsonBuilder"""
 
    @staticmethod
    def _wrap(java_value: _GsonBuilder) -> 'GsonBuilder':
        return GsonBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GsonBuilder):
        """
        Dynamic initializer for GsonBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GsonBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GsonBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def serializeNulls(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.serializeNulls()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).serializeNulls())

    @overload
    def registerTypeAdapterFactory(self, arg0: 'TypeAdapterFactory') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.registerTypeAdapterFactory(com.google.gson.TypeAdapterFactory)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).registerTypeAdapterFactory(arg0))

    @overload
    def registerTypeAdapter(self, arg0: 'Type', arg1: object) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.registerTypeAdapter(java.lang.reflect.Type,java.lang.Object)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).registerTypeAdapter(arg0, arg1))

    @overload
    def __init__(self, ):
        """public com.google.gson.GsonBuilder()"""
        val = _GsonBuilder()
        self.__wrapper = val

    @overload
    def registerTypeHierarchyAdapter(self, arg0: 'Class', arg1: object) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.registerTypeHierarchyAdapter(java.lang.Class<?>,java.lang.Object)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).registerTypeHierarchyAdapter(arg0, arg1))

    @overload
    def enableComplexMapKeySerialization(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.enableComplexMapKeySerialization()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).enableComplexMapKeySerialization())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDateFormat(self, arg0: int, arg1: int) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setDateFormat(int,int)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setDateFormat(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def setNumberToNumberStrategy(self, arg0: 'ToNumberStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setNumberToNumberStrategy(com.google.gson.ToNumberStrategy)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setNumberToNumberStrategy(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setPrettyPrinting(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setPrettyPrinting()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).setPrettyPrinting())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setLenient(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setLenient()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).setLenient())

    @overload
    def generateNonExecutableJson(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.generateNonExecutableJson()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).generateNonExecutableJson())

    @overload
    def addReflectionAccessFilter(self, arg0: 'ReflectionAccessFilter') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.addReflectionAccessFilter(com.google.gson.ReflectionAccessFilter)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).addReflectionAccessFilter(arg0))

    @overload
    def addDeserializationExclusionStrategy(self, arg0: 'ExclusionStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.addDeserializationExclusionStrategy(com.google.gson.ExclusionStrategy)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).addDeserializationExclusionStrategy(arg0))

    @overload
    def setVersion(self, arg0: float) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setVersion(double)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setVersion(_double.valueOf(arg0)))

    @overload
    def setDateFormat(self, arg0: int) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setDateFormat(int)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setDateFormat(_int.valueOf(arg0)))

    @overload
    def setExclusionStrategies(self, *arg0: 'ExclusionStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setExclusionStrategies(com.google.gson.ExclusionStrategy...)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setExclusionStrategies(arg0))

    @overload
    def setDateFormat(self, arg0: str) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setDateFormat(java.lang.String)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setDateFormat(arg0))

    @overload
    def setLongSerializationPolicy(self, arg0: 'LongSerializationPolicy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setLongSerializationPolicy(com.google.gson.LongSerializationPolicy)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setLongSerializationPolicy(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def disableHtmlEscaping(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.disableHtmlEscaping()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).disableHtmlEscaping())

    @overload
    def disableInnerClassSerialization(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.disableInnerClassSerialization()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).disableInnerClassSerialization())

    @overload
    def disableJdkUnsafe(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.disableJdkUnsafe()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).disableJdkUnsafe())

    @overload
    def addSerializationExclusionStrategy(self, arg0: 'ExclusionStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.addSerializationExclusionStrategy(com.google.gson.ExclusionStrategy)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).addSerializationExclusionStrategy(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setFieldNamingPolicy(self, arg0: 'FieldNamingPolicy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setFieldNamingPolicy(com.google.gson.FieldNamingPolicy)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setFieldNamingPolicy(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setFieldNamingStrategy(self, arg0: 'FieldNamingStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setFieldNamingStrategy(com.google.gson.FieldNamingStrategy)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setFieldNamingStrategy(arg0))

    @overload
    def serializeSpecialFloatingPointValues(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.serializeSpecialFloatingPointValues()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).serializeSpecialFloatingPointValues())

    @overload
    def excludeFieldsWithModifiers(self, *arg0: int) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.excludeFieldsWithModifiers(int...)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).excludeFieldsWithModifiers(arg0))

    @overload
    def create(self) -> 'Gson':
        """public com.google.gson.Gson com.google.gson.GsonBuilder.create()"""
        return 'Gson'._wrap(super(GsonBuilder, self).create())

    @overload
    def excludeFieldsWithoutExposeAnnotation(self) -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.excludeFieldsWithoutExposeAnnotation()"""
        return 'GsonBuilder'._wrap(super(GsonBuilder, self).excludeFieldsWithoutExposeAnnotation())

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
    def setObjectToNumberStrategy(self, arg0: 'ToNumberStrategy') -> 'GsonBuilder':
        """public com.google.gson.GsonBuilder com.google.gson.GsonBuilder.setObjectToNumberStrategy(com.google.gson.ToNumberStrategy)"""
        return 'GsonBuilder'._wrap(super(_GsonBuilder, self).setObjectToNumberStrategy(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.GsonBuilder()"""
        val = _GsonBuilder()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.JsonDeserializationContext
import com.google.gson.JsonDeserializationContext as _JsonDeserializationContext
_JsonDeserializationContext = _JsonDeserializationContext
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
 
class JsonDeserializationContext():
    """com.google.gson.JsonDeserializationContext"""
 
    @staticmethod
    def _wrap(java_value: _JsonDeserializationContext) -> 'JsonDeserializationContext':
        return JsonDeserializationContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonDeserializationContext):
        """
        Dynamic initializer for JsonDeserializationContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonDeserializationContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonDeserializationContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def deserialize(self, arg0: 'JsonElement', arg1: 'Type'):
        """public abstract <T> T com.google.gson.JsonDeserializationContext.deserialize(com.google.gson.JsonElement,java.lang.reflect.Type) throws com.google.gson.JsonParseException"""
        pass 
 
 
# CLASS: com.google.gson.JsonPrimitive
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import com.google.gson.JsonObject as _JsonObject
_JsonObject = _JsonObject
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.google.gson.JsonArray as _JsonArray
_JsonArray = _JsonArray
import java.lang.String as _string
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import com.google.gson.JsonPrimitive as _JsonPrimitive
_JsonPrimitive = _JsonPrimitive
import java.math.BigDecimal as BigDecimal
import java.lang.Character as Character
from builtins import bool
import com.google.gson.JsonNull as _JsonNull
_JsonNull = _JsonNull
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonPrimitive():
    """com.google.gson.JsonPrimitive"""
 
    @staticmethod
    def _wrap(java_value: _JsonPrimitive) -> 'JsonPrimitive':
        return JsonPrimitive(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonPrimitive):
        """
        Dynamic initializer for JsonPrimitive.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonPrimitive__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonPrimitive__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonPrimitive.getAsBigInteger()"""
        return _transform(super(JsonPrimitive, self).getAsBigInteger()).'BigInteger'Value()

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'._wrap(super(JsonElement, self).getAsJsonObject())

    @override
    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool._wrap(super(JsonElement, self).isJsonArray())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonPrimitive.equals(java.lang.Object)"""
        return bool._wrap(super(_JsonPrimitive, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonPrimitive.getAsLong()"""
        return int._wrap(super(JsonPrimitive, self).getAsLong())

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.getAsBoolean()"""
        return bool._wrap(super(JsonPrimitive, self).getAsBoolean())

    @overload
    def isBoolean(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.isBoolean()"""
        return bool._wrap(super(JsonPrimitive, self).isBoolean())

    @overload
    def __init__(self, arg0: 'Number'):
        """public com.google.gson.JsonPrimitive(java.lang.Number)"""
        val = _JsonPrimitive(arg0)
        self.__wrapper = val

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool._wrap(super(JsonElement, self).isJsonObject())

    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonPrimitive.getAsNumber()"""
        return _transform(super(JsonPrimitive, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'._wrap(super(JsonElement, self).getAsJsonPrimitive())

    @overload
    def __init__(self, arg0: 'Boolean'):
        """public com.google.gson.JsonPrimitive(java.lang.Boolean)"""
        val = _JsonPrimitive(arg0)
        self.__wrapper = val

    @override
    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonPrimitive.getAsDouble()"""
        return float._wrap(super(JsonPrimitive, self).getAsDouble())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Character'):
        """public com.google.gson.JsonPrimitive(java.lang.Character)"""
        val = _JsonPrimitive(arg0)
        self.__wrapper = val

    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonPrimitive.getAsByte()"""
        return int._wrap(super(JsonPrimitive, self).getAsByte())

    @override
    @overload
    def deepCopy(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonPrimitive.deepCopy()"""
        return 'JsonPrimitive'._wrap(super(JsonPrimitive, self).deepCopy())

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonPrimitive(java.lang.String)"""
        val = _JsonPrimitive(arg0)
        self.__wrapper = val

    @overload
    def isString(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.isString()"""
        return bool._wrap(super(JsonPrimitive, self).isString())

    @override
    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonPrimitive.getAsBigDecimal()"""
        return _transform(super(JsonPrimitive, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonPrimitive.getAsInt()"""
        return int._wrap(super(JsonPrimitive, self).getAsInt())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonPrimitive.hashCode()"""
        return int._wrap(super(JsonPrimitive, self).hashCode())

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonPrimitive.getAsFloat()"""
        return float._wrap(super(JsonPrimitive, self).getAsFloat())

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonPrimitive.getAsCharacter()"""
        return str._wrap(super(JsonPrimitive, self).getAsCharacter())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str._wrap(super(JsonElement, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool._wrap(super(JsonElement, self).isJsonPrimitive())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'._wrap(super(JsonElement, self).getAsJsonNull())

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'._wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool._wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonPrimitive.getAsString()"""
        return str._wrap(super(JsonPrimitive, self).getAsString())

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonPrimitive.getAsShort()"""
        return int._wrap(super(JsonPrimitive, self).getAsShort())

    @overload
    def isNumber(self) -> bool:
        """public boolean com.google.gson.JsonPrimitive.isNumber()"""
        return bool._wrap(super(JsonPrimitive, self).isNumber()) 
 
 
# CLASS: com.google.gson.JsonIOException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import com.google.gson.JsonIOException as _JsonIOException
_JsonIOException = _JsonIOException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonIOException():
    """com.google.gson.JsonIOException"""
 
    @staticmethod
    def _wrap(java_value: _JsonIOException) -> 'JsonIOException':
        return JsonIOException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonIOException):
        """
        Dynamic initializer for JsonIOException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonIOException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonIOException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.JsonIOException(java.lang.String,java.lang.Throwable)"""
        val = _JsonIOException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonIOException(java.lang.String)"""
        val = _JsonIOException(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.JsonIOException(java.lang.Throwable)"""
        val = _JsonIOException(arg0)
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
 
 
# CLASS: com.google.gson.FieldNamingStrategy
import com.google.gson.FieldNamingStrategy as _FieldNamingStrategy
_FieldNamingStrategy = _FieldNamingStrategy
import java.lang.reflect.Field as Field
from abc import abstractmethod, ABC
 
class FieldNamingStrategy():
    """com.google.gson.FieldNamingStrategy"""
 
    @staticmethod
    def _wrap(java_value: _FieldNamingStrategy) -> 'FieldNamingStrategy':
        return FieldNamingStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldNamingStrategy):
        """
        Dynamic initializer for FieldNamingStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldNamingStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldNamingStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def translateName(self, arg0: 'Field'):
        """public abstract java.lang.String com.google.gson.FieldNamingStrategy.translateName(java.lang.reflect.Field)"""
        pass 
 
 
# CLASS: com.google.gson.TypeAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
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
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TypeAdapter():
    """com.google.gson.TypeAdapter"""
 
    @staticmethod
    def _wrap(java_value: _TypeAdapter) -> 'TypeAdapter':
        return TypeAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeAdapter):
        """
        Dynamic initializer for TypeAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def fromJson(self, arg0: str) -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.lang.String) throws java.io.IOException"""
        return object._wrap(super(_TypeAdapter, self).fromJson(arg0))

    @overload
    def toJson(self, arg0: object) -> str:
        """public final java.lang.String com.google.gson.TypeAdapter.toJson(T)"""
        return str._wrap(super(_TypeAdapter, self).toJson(arg0))

    @overload
    def fromJson(self, arg0: 'Reader') -> object:
        """public final T com.google.gson.TypeAdapter.fromJson(java.io.Reader) throws java.io.IOException"""
        return object._wrap(super(_TypeAdapter, self).fromJson(arg0))

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
        return object._wrap(super(_TypeAdapter, self).fromJsonTree(arg0))

    @overload
    def nullSafe(self) -> 'TypeAdapter':
        """public final com.google.gson.TypeAdapter<T> com.google.gson.TypeAdapter.nullSafe()"""
        return 'TypeAdapter'._wrap(super(TypeAdapter, self).nullSafe())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def toJsonTree(self, arg0: object) -> 'JsonElement':
        """public final com.google.gson.JsonElement com.google.gson.TypeAdapter.toJsonTree(T)"""
        return 'JsonElement'._wrap(super(_TypeAdapter, self).toJsonTree(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.google.gson.TypeAdapter()"""
        val = _TypeAdapter()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.google.gson.TypeAdapter()"""
        val = _TypeAdapter()
        self.__wrapper = val

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def read(self, arg0: 'JsonReader'):
        """public abstract T com.google.gson.TypeAdapter.read(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass

    @overload
    def toJson(self, arg0: 'Writer', arg1: object):
        """public final void com.google.gson.TypeAdapter.toJson(java.io.Writer,T) throws java.io.IOException"""
        super(_TypeAdapter, self).toJson(arg0, arg1)

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
 
 
# CLASS: com.google.gson.ReflectionAccessFilter$FilterResult
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
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FilterResult():
    """com.google.gson.ReflectionAccessFilter.FilterResult"""
 
    @staticmethod
    def _wrap(java_value: _FilterResult) -> 'FilterResult':
        return FilterResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FilterResult):
        """
        Dynamic initializer for FilterResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FilterResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FilterResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FilterResult':
        """public static com.google.gson.ReflectionAccessFilter$FilterResult com.google.gson.ReflectionAccessFilter$FilterResult.valueOf(java.lang.String)"""
        return FilterResult._wrap(_FilterResult.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['FilterResult']:
        """public static com.google.gson.ReflectionAccessFilter$FilterResult[] com.google.gson.ReflectionAccessFilter$FilterResult.values()"""
        return List[FilterResult]._wrap(_FilterResult.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.gson.ToNumberStrategy
from pyquantum_helper import import_once as _import_once
from abc import abstractmethod, ABC
import com.google.gson.ToNumberStrategy as _ToNumberStrategy
_ToNumberStrategy = _ToNumberStrategy
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

 
class ToNumberStrategy():
    """com.google.gson.ToNumberStrategy"""
 
    @staticmethod
    def _wrap(java_value: _ToNumberStrategy) -> 'ToNumberStrategy':
        return ToNumberStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToNumberStrategy):
        """
        Dynamic initializer for ToNumberStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToNumberStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToNumberStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def readNumber(self, arg0: 'JsonReader'):
        """public abstract java.lang.Number com.google.gson.ToNumberStrategy.readNumber(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass 
 
 
# CLASS: com.google.gson.ToNumberPolicy
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.ToNumberPolicy as _ToNumberPolicy
_ToNumberPolicy = _ToNumberPolicy
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.google.gson.ToNumberStrategy as _ToNumberStrategy
_ToNumberStrategy = _ToNumberStrategy
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ToNumberPolicy():
    """com.google.gson.ToNumberPolicy"""
 
    @staticmethod
    def _wrap(java_value: _ToNumberPolicy) -> 'ToNumberPolicy':
        return ToNumberPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToNumberPolicy):
        """
        Dynamic initializer for ToNumberPolicy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToNumberPolicy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToNumberPolicy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['ToNumberPolicy']:
        """public static com.google.gson.ToNumberPolicy[] com.google.gson.ToNumberPolicy.values()"""
        return List[ToNumberPolicy]._wrap(_ToNumberPolicy.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ToNumberPolicy':
        """public static com.google.gson.ToNumberPolicy com.google.gson.ToNumberPolicy.valueOf(java.lang.String)"""
        return ToNumberPolicy._wrap(_ToNumberPolicy.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def readNumber(self, arg0: 'JsonReader'):
        """public abstract java.lang.Number com.google.gson.ToNumberStrategy.readNumber(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass 
 
 
# CLASS: com.google.gson.JsonParser
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.JsonParser as _JsonParser
_JsonParser = _JsonParser
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = _import_once("pygson.stream")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonParser():
    """com.google.gson.JsonParser"""
 
    @staticmethod
    def _wrap(java_value: _JsonParser) -> 'JsonParser':
        return JsonParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonParser):
        """
        Dynamic initializer for JsonParser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonParser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonParser__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseReader(arg0: 'Reader') -> 'JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.JsonParser.parseReader(java.io.Reader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return JsonElement._wrap(_JsonParser.parseReader(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def parse(self, arg0: 'Reader') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonParser.parse(java.io.Reader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return 'JsonElement'._wrap(super(_JsonParser, self).parse(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.google.gson.JsonParser()"""
        val = _JsonParser()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def parseString(arg0: str) -> 'JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.JsonParser.parseString(java.lang.String) throws com.google.gson.JsonSyntaxException"""
        return JsonElement._wrap(_JsonParser.parseString(arg0))

    @staticmethod
    @overload
    def parseReader(arg0: 'JsonReader') -> 'JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.JsonParser.parseReader(com.google.gson.stream.JsonReader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return JsonElement._wrap(_JsonParser.parseReader(arg0))

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
    def parse(self, arg0: 'JsonReader') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonParser.parse(com.google.gson.stream.JsonReader) throws com.google.gson.JsonIOException,com.google.gson.JsonSyntaxException"""
        return 'JsonElement'._wrap(super(_JsonParser, self).parse(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonParser()"""
        val = _JsonParser()
        self.__wrapper = val

    @overload
    def parse(self, arg0: str) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonParser.parse(java.lang.String) throws com.google.gson.JsonSyntaxException"""
        return 'JsonElement'._wrap(super(_JsonParser, self).parse(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.JsonDeserializer
import com.google.gson.JsonDeserializer as _JsonDeserializer
_JsonDeserializer = _JsonDeserializer
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
 
class JsonDeserializer():
    """com.google.gson.JsonDeserializer"""
 
    @staticmethod
    def _wrap(java_value: _JsonDeserializer) -> 'JsonDeserializer':
        return JsonDeserializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonDeserializer):
        """
        Dynamic initializer for JsonDeserializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonDeserializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonDeserializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def deserialize(self, arg0: 'JsonElement', arg1: 'Type', arg2: 'JsonDeserializationContext'):
        """public abstract T com.google.gson.JsonDeserializer.deserialize(com.google.gson.JsonElement,java.lang.reflect.Type,com.google.gson.JsonDeserializationContext) throws com.google.gson.JsonParseException"""
        pass 
 
 
# CLASS: com.google.gson.ExclusionStrategy
from builtins import type
import com.google.gson.ExclusionStrategy as _ExclusionStrategy
_ExclusionStrategy = _ExclusionStrategy
from abc import abstractmethod, ABC
 
class ExclusionStrategy():
    """com.google.gson.ExclusionStrategy"""
 
    @staticmethod
    def _wrap(java_value: _ExclusionStrategy) -> 'ExclusionStrategy':
        return ExclusionStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExclusionStrategy):
        """
        Dynamic initializer for ExclusionStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExclusionStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExclusionStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.gson.JsonSerializer
import java.lang.reflect.Type as Type
from abc import abstractmethod, ABC
import com.google.gson.JsonSerializer as _JsonSerializer
_JsonSerializer = _JsonSerializer
 
class JsonSerializer():
    """com.google.gson.JsonSerializer"""
 
    @staticmethod
    def _wrap(java_value: _JsonSerializer) -> 'JsonSerializer':
        return JsonSerializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonSerializer):
        """
        Dynamic initializer for JsonSerializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonSerializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonSerializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def serialize(self, arg0: object, arg1: 'Type', arg2: 'JsonSerializationContext'):
        """public abstract com.google.gson.JsonElement com.google.gson.JsonSerializer.serialize(T,java.lang.reflect.Type,com.google.gson.JsonSerializationContext)"""
        pass 
 
 
# CLASS: com.google.gson.JsonArray
import com.google.gson.JsonObject as _JsonObject
_JsonObject = _JsonObject
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.gson.JsonArray as _JsonArray
_JsonArray = _JsonArray
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import com.google.gson.JsonPrimitive as _JsonPrimitive
_JsonPrimitive = _JsonPrimitive
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import java.lang.Character as Character
from builtins import bool
import com.google.gson.JsonNull as _JsonNull
_JsonNull = _JsonNull
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _object
from builtins import float
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.math.BigDecimal as BigDecimal
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class JsonArray():
    """com.google.gson.JsonArray"""
 
    @staticmethod
    def _wrap(java_value: _JsonArray) -> 'JsonArray':
        return JsonArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonArray):
        """
        Dynamic initializer for JsonArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonArray.getAsByte()"""
        return int._wrap(super(JsonArray, self).getAsByte())

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'._wrap(super(JsonElement, self).getAsJsonObject())

    @overload
    def asList(self) -> 'List':
        """public java.util.List<com.google.gson.JsonElement> com.google.gson.JsonArray.asList()"""
        return 'List'._wrap(super(JsonArray, self).asList())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonArray.getAsBigDecimal()"""
        return _transform(super(JsonArray, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def deepCopy(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonArray.deepCopy()"""
        return 'JsonArray'._wrap(super(JsonArray, self).deepCopy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def addAll(self, arg0: 'JsonArray'):
        """public void com.google.gson.JsonArray.addAll(com.google.gson.JsonArray)"""
        super(_JsonArray, self).addAll(arg0)

    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonArray.getAsNumber()"""
        return _transform(super(JsonArray, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonArray.getAsShort()"""
        return int._wrap(super(JsonArray, self).getAsShort())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonArray.getAsBigInteger()"""
        return _transform(super(JsonArray, self).getAsBigInteger()).'BigInteger'Value()

    @overload
    def add(self, arg0: 'JsonElement'):
        """public void com.google.gson.JsonArray.add(com.google.gson.JsonElement)"""
        super(_JsonArray, self).add(arg0)

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool._wrap(super(JsonElement, self).isJsonObject())

    @overload
    def remove(self, arg0: int) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonArray.remove(int)"""
        return 'JsonElement'._wrap(super(_JsonArray, self).remove(_int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.gson.JsonArray.isEmpty()"""
        return bool._wrap(super(JsonArray, self).isEmpty())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.google.gson.JsonElement> com.google.gson.JsonArray.iterator()"""
        return 'Iterator'._wrap(super(JsonArray, self).iterator())

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonArray.getAsString()"""
        return str._wrap(super(JsonArray, self).getAsString())

    @overload
    def remove(self, arg0: 'JsonElement') -> bool:
        """public boolean com.google.gson.JsonArray.remove(com.google.gson.JsonElement)"""
        return bool._wrap(super(_JsonArray, self).remove(arg0))

    @overload
    def add(self, arg0: 'Boolean'):
        """public void com.google.gson.JsonArray.add(java.lang.Boolean)"""
        super(_JsonArray, self).add(arg0)

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonArray.getAsFloat()"""
        return float._wrap(super(JsonArray, self).getAsFloat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool._wrap(super(JsonElement, self).isJsonPrimitive())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'._wrap(super(JsonElement, self).getAsJsonNull())

    @override
    @overload
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool._wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonArray.getAsInt()"""
        return int._wrap(super(JsonArray, self).getAsInt())

    @overload
    def __init__(self, arg0: int):
        """public com.google.gson.JsonArray(int)"""
        val = _JsonArray(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int com.google.gson.JsonArray.size()"""
        return int._wrap(super(JsonArray, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonArray.equals(java.lang.Object)"""
        return bool._wrap(super(_JsonArray, self).equals(arg0))

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonArray.getAsCharacter()"""
        return str._wrap(super(JsonArray, self).getAsCharacter())

    @override
    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool._wrap(super(JsonElement, self).isJsonArray())

    @overload
    def __init__(self):
        """public com.google.gson.JsonArray()"""
        val = _JsonArray()
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonArray.get(int)"""
        return 'JsonElement'._wrap(super(_JsonArray, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonArray.getAsLong()"""
        return int._wrap(super(JsonArray, self).getAsLong())

    @overload
    def set(self, arg0: int, arg1: 'JsonElement') -> 'JsonElement':
        """public com.google.gson.JsonElement com.google.gson.JsonArray.set(int,com.google.gson.JsonElement)"""
        return 'JsonElement'._wrap(super(_JsonArray, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonArray.hashCode()"""
        return int._wrap(super(JsonArray, self).hashCode())

    @overload
    def add(self, arg0: 'Character'):
        """public void com.google.gson.JsonArray.add(java.lang.Character)"""
        super(_JsonArray, self).add(arg0)

    @overload
    def contains(self, arg0: 'JsonElement') -> bool:
        """public boolean com.google.gson.JsonArray.contains(com.google.gson.JsonElement)"""
        return bool._wrap(super(_JsonArray, self).contains(arg0))

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'._wrap(super(JsonElement, self).getAsJsonPrimitive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonArray.getAsDouble()"""
        return float._wrap(super(JsonArray, self).getAsDouble())

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonArray.getAsBoolean()"""
        return bool._wrap(super(JsonArray, self).getAsBoolean())

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonArray()"""
        val = _JsonArray()
        self.__wrapper = val

    @overload
    def add(self, arg0: str):
        """public void com.google.gson.JsonArray.add(java.lang.String)"""
        super(_JsonArray, self).add(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def add(self, arg0: 'Number'):
        """public void com.google.gson.JsonArray.add(java.lang.Number)"""
        super(_JsonArray, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str._wrap(super(JsonElement, self).toString())

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'._wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: com.google.gson.FieldAttributes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.Field as Field
import java.util.Collection as Collection
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.annotation.Annotation as Annotation
import java.lang.reflect.Type as _Type
_Type = _Type
import com.google.gson.FieldAttributes as _FieldAttributes
_FieldAttributes = _FieldAttributes
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
from builtins import int
 
class FieldAttributes():
    """com.google.gson.FieldAttributes"""
 
    @staticmethod
    def _wrap(java_value: _FieldAttributes) -> 'FieldAttributes':
        return FieldAttributes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldAttributes):
        """
        Dynamic initializer for FieldAttributes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldAttributes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldAttributes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getName(self) -> str:
        """public java.lang.String com.google.gson.FieldAttributes.getName()"""
        return str._wrap(super(FieldAttributes, self).getName())

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class<?> com.google.gson.FieldAttributes.getDeclaringClass()"""
        return 'type.Class'._wrap(super(FieldAttributes, self).getDeclaringClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public <T extends java.lang.annotation.Annotation> T com.google.gson.FieldAttributes.getAnnotation(java.lang.Class<T>)"""
        return 'Annotation'._wrap(super(_FieldAttributes, self).getAnnotation(arg0))

    @overload
    def getDeclaredType(self) -> 'Type':
        """public java.lang.reflect.Type com.google.gson.FieldAttributes.getDeclaredType()"""
        return 'Type'._wrap(super(FieldAttributes, self).getDeclaredType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Field'):
        """public com.google.gson.FieldAttributes(java.lang.reflect.Field)"""
        val = _FieldAttributes(arg0)
        self.__wrapper = val

    @overload
    def getAnnotations(self) -> 'Collection':
        """public java.util.Collection<java.lang.annotation.Annotation> com.google.gson.FieldAttributes.getAnnotations()"""
        return 'Collection'._wrap(super(FieldAttributes, self).getAnnotations())

    @overload
    def getDeclaredClass(self) -> 'type.Class':
        """public java.lang.Class<?> com.google.gson.FieldAttributes.getDeclaredClass()"""
        return 'type.Class'._wrap(super(FieldAttributes, self).getDeclaredClass())

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
    def hasModifier(self, arg0: int) -> bool:
        """public boolean com.google.gson.FieldAttributes.hasModifier(int)"""
        return bool._wrap(super(_FieldAttributes, self).hasModifier(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.FieldAttributes.toString()"""
        return str._wrap(super(FieldAttributes, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.JsonSyntaxException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import com.google.gson.JsonSyntaxException as _JsonSyntaxException
_JsonSyntaxException = _JsonSyntaxException
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonSyntaxException():
    """com.google.gson.JsonSyntaxException"""
 
    @staticmethod
    def _wrap(java_value: _JsonSyntaxException) -> 'JsonSyntaxException':
        return JsonSyntaxException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonSyntaxException):
        """
        Dynamic initializer for JsonSyntaxException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonSyntaxException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonSyntaxException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.JsonSyntaxException(java.lang.String,java.lang.Throwable)"""
        val = _JsonSyntaxException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.JsonSyntaxException(java.lang.Throwable)"""
        val = _JsonSyntaxException(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.JsonSyntaxException(java.lang.String)"""
        val = _JsonSyntaxException(arg0)
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
 
 
# CLASS: com.google.gson.JsonNull
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import com.google.gson.JsonObject as _JsonObject
_JsonObject = _JsonObject
import com.google.gson.JsonElement as _JsonElement
_JsonElement = _JsonElement
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.google.gson.JsonArray as _JsonArray
_JsonArray = _JsonArray
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import com.google.gson.JsonPrimitive as _JsonPrimitive
_JsonPrimitive = _JsonPrimitive
import java.math.BigDecimal as BigDecimal
import com.google.gson.JsonNull as _JsonNull
_JsonNull = _JsonNull
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonNull():
    """com.google.gson.JsonNull"""
 
    @staticmethod
    def _wrap(java_value: _JsonNull) -> 'JsonNull':
        return JsonNull(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonNull):
        """
        Dynamic initializer for JsonNull.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonNull__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonNull__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAsNumber(self) -> 'Number':
        """public java.lang.Number com.google.gson.JsonElement.getAsNumber()"""
        return _transform(super(JsonElement, self).getAsNumber()).'Number'Value()

    @override
    @overload
    def getAsFloat(self) -> float:
        """public float com.google.gson.JsonElement.getAsFloat()"""
        return float._wrap(super(JsonElement, self).getAsFloat())

    @override
    @overload
    def getAsJsonObject(self) -> 'JsonObject':
        """public com.google.gson.JsonObject com.google.gson.JsonElement.getAsJsonObject()"""
        return 'JsonObject'._wrap(super(JsonElement, self).getAsJsonObject())

    @override
    @overload
    def deepCopy(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonNull.deepCopy()"""
        return 'JsonNull'._wrap(super(JsonNull, self).deepCopy())

    @override
    @overload
    def isJsonArray(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonArray()"""
        return bool._wrap(super(JsonElement, self).isJsonArray())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean com.google.gson.JsonElement.getAsBoolean()"""
        return bool._wrap(super(JsonElement, self).getAsBoolean())

    @override
    @overload
    def getAsBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.gson.JsonElement.getAsBigInteger()"""
        return _transform(super(JsonElement, self).getAsBigInteger()).'BigInteger'Value()

    @override
    @overload
    def getAsInt(self) -> int:
        """public int com.google.gson.JsonElement.getAsInt()"""
        return int._wrap(super(JsonElement, self).getAsInt())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.JsonNull.equals(java.lang.Object)"""
        return bool._wrap(super(_JsonNull, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isJsonObject(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonObject()"""
        return bool._wrap(super(JsonElement, self).isJsonObject())

    @override
    @overload
    def getAsCharacter(self) -> str:
        """public char com.google.gson.JsonElement.getAsCharacter()"""
        return str._wrap(super(JsonElement, self).getAsCharacter())

    @override
    @overload
    def getAsBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal com.google.gson.JsonElement.getAsBigDecimal()"""
        return _transform(super(JsonElement, self).getAsBigDecimal()).'BigDecimal'Value()

    @override
    @overload
    def getAsJsonPrimitive(self) -> 'JsonPrimitive':
        """public com.google.gson.JsonPrimitive com.google.gson.JsonElement.getAsJsonPrimitive()"""
        return 'JsonPrimitive'._wrap(super(JsonElement, self).getAsJsonPrimitive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getAsByte(self) -> int:
        """public byte com.google.gson.JsonElement.getAsByte()"""
        return int._wrap(super(JsonElement, self).getAsByte())

    @overload
    def __init__(self, ):
        """public com.google.gson.JsonNull()"""
        val = _JsonNull()
        self.__wrapper = val

    @override
    @overload
    def getAsDouble(self) -> float:
        """public double com.google.gson.JsonElement.getAsDouble()"""
        return float._wrap(super(JsonElement, self).getAsDouble())

    @override
    @overload
    def getAsLong(self) -> int:
        """public long com.google.gson.JsonElement.getAsLong()"""
        return int._wrap(super(JsonElement, self).getAsLong())

    @override
    @overload
    def getAsString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.getAsString()"""
        return str._wrap(super(JsonElement, self).getAsString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.JsonNull.hashCode()"""
        return int._wrap(super(JsonNull, self).hashCode())

    @overload
    def __init__(self):
        """public com.google.gson.JsonNull()"""
        val = _JsonNull()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.JsonElement.toString()"""
        return str._wrap(super(JsonElement, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isJsonPrimitive(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonPrimitive()"""
        return bool._wrap(super(JsonElement, self).isJsonPrimitive())

    @override
    @overload
    def getAsJsonNull(self) -> 'JsonNull':
        """public com.google.gson.JsonNull com.google.gson.JsonElement.getAsJsonNull()"""
        return 'JsonNull'._wrap(super(JsonElement, self).getAsJsonNull())

    @override
    @overload
    def getAsJsonArray(self) -> 'JsonArray':
        """public com.google.gson.JsonArray com.google.gson.JsonElement.getAsJsonArray()"""
        return 'JsonArray'._wrap(super(JsonElement, self).getAsJsonArray())

    @override
    @overload
    def isJsonNull(self) -> bool:
        """public boolean com.google.gson.JsonElement.isJsonNull()"""
        return bool._wrap(super(JsonElement, self).isJsonNull())

    @override
    @overload
    def getAsShort(self) -> int:
        """public short com.google.gson.JsonElement.getAsShort()"""
        return int._wrap(super(JsonElement, self).getAsShort())