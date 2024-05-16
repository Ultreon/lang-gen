from __future__ import annotations
from overload import overload


 
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Double as _double
import java.lang.Number as Number
from pyquantum_helper import override
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
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonWriter():
    """com.google.gson.stream.JsonWriter"""
 
    @staticmethod
    def _wrap(java_value: _JsonWriter) -> 'JsonWriter':
        return JsonWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonWriter):
        """
        Dynamic initializer for JsonWriter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonWriter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonWriter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def value(self, arg0: bool) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(boolean) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_boolean.valueOf(arg0)))

    @overload
    def isLenient(self) -> bool:
        """public boolean com.google.gson.stream.JsonWriter.isLenient()"""
        return bool._wrap(super(JsonWriter, self).isLenient())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void com.google.gson.stream.JsonWriter.close() throws java.io.IOException"""
        super(JsonWriter, self).close()

    @overload
    def beginArray(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.beginArray() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).beginArray())

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
    def setIndent(self, arg0: str):
        """public final void com.google.gson.stream.JsonWriter.setIndent(java.lang.String)"""
        super(_JsonWriter, self).setIndent(arg0)

    @overload
    def nullValue(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.nullValue() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).nullValue())

    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setLenient(boolean)"""
        super(_JsonWriter, self).setLenient(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def flush(self):
        """public void com.google.gson.stream.JsonWriter.flush() throws java.io.IOException"""
        super(JsonWriter, self).flush()

    @overload
    def jsonValue(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.jsonValue(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).jsonValue(arg0))

    @overload
    def beginObject(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.beginObject() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).beginObject())

    @overload
    def value(self, arg0: int) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(long) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def value(self, arg0: float) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(float) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_float.valueOf(arg0)))

    @overload
    def value(self, arg0: float) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(double) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_double.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setSerializeNulls(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setSerializeNulls(boolean)"""
        super(_JsonWriter, self).setSerializeNulls(_boolean.valueOf(arg0))

    @overload
    def value(self, arg0: 'Number') -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.Number) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(arg0))

    @overload
    def setHtmlSafe(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setHtmlSafe(boolean)"""
        super(_JsonWriter, self).setHtmlSafe(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Writer'):
        """public com.google.gson.stream.JsonWriter(java.io.Writer)"""
        val = _JsonWriter(arg0)
        self.__wrapper = val

    @overload
    def value(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getSerializeNulls(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.getSerializeNulls()"""
        return bool._wrap(super(JsonWriter, self).getSerializeNulls())

    @overload
    def isHtmlSafe(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.isHtmlSafe()"""
        return bool._wrap(super(JsonWriter, self).isHtmlSafe())

    @overload
    def endObject(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.endObject() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).endObject())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def name(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.name(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).name(arg0))

    @overload
    def endArray(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.endArray() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).endArray())

    @overload
    def value(self, arg0: 'Boolean') -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.Boolean) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.stream.JsonWriter
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Double as _double
import java.lang.Number as Number
from pyquantum_helper import override
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
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonWriter():
    """com.google.gson.stream.JsonWriter"""
 
    @staticmethod
    def _wrap(java_value: _JsonWriter) -> 'JsonWriter':
        return JsonWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonWriter):
        """
        Dynamic initializer for JsonWriter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonWriter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonWriter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def value(self, arg0: bool) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(boolean) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_boolean.valueOf(arg0)))

    @overload
    def isLenient(self) -> bool:
        """public boolean com.google.gson.stream.JsonWriter.isLenient()"""
        return bool._wrap(super(JsonWriter, self).isLenient())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void com.google.gson.stream.JsonWriter.close() throws java.io.IOException"""
        super(JsonWriter, self).close()

    @overload
    def beginArray(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.beginArray() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).beginArray())

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
    def setIndent(self, arg0: str):
        """public final void com.google.gson.stream.JsonWriter.setIndent(java.lang.String)"""
        super(_JsonWriter, self).setIndent(arg0)

    @overload
    def nullValue(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.nullValue() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).nullValue())

    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setLenient(boolean)"""
        super(_JsonWriter, self).setLenient(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def flush(self):
        """public void com.google.gson.stream.JsonWriter.flush() throws java.io.IOException"""
        super(JsonWriter, self).flush()

    @overload
    def jsonValue(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.jsonValue(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).jsonValue(arg0))

    @overload
    def beginObject(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.beginObject() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).beginObject())

    @overload
    def value(self, arg0: int) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(long) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def value(self, arg0: float) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(float) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_float.valueOf(arg0)))

    @overload
    def value(self, arg0: float) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(double) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(_double.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setSerializeNulls(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setSerializeNulls(boolean)"""
        super(_JsonWriter, self).setSerializeNulls(_boolean.valueOf(arg0))

    @overload
    def value(self, arg0: 'Number') -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.Number) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(arg0))

    @overload
    def setHtmlSafe(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setHtmlSafe(boolean)"""
        super(_JsonWriter, self).setHtmlSafe(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Writer'):
        """public com.google.gson.stream.JsonWriter(java.io.Writer)"""
        val = _JsonWriter(arg0)
        self.__wrapper = val

    @overload
    def value(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getSerializeNulls(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.getSerializeNulls()"""
        return bool._wrap(super(JsonWriter, self).getSerializeNulls())

    @overload
    def isHtmlSafe(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.isHtmlSafe()"""
        return bool._wrap(super(JsonWriter, self).isHtmlSafe())

    @overload
    def endObject(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.endObject() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).endObject())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def name(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.name(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).name(arg0))

    @overload
    def endArray(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.endArray() throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(JsonWriter, self).endArray())

    @overload
    def value(self, arg0: 'Boolean') -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.Boolean) throws java.io.IOException"""
        return 'JsonWriter'._wrap(super(_JsonWriter, self).value(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.stream.JsonWriter 
 
 
# CLASS: com.google.gson.stream.MalformedJsonException
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
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import com.google.gson.stream.MalformedJsonException as _MalformedJsonException
_MalformedJsonException = _MalformedJsonException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MalformedJsonException():
    """com.google.gson.stream.MalformedJsonException"""
 
    @staticmethod
    def _wrap(java_value: _MalformedJsonException) -> 'MalformedJsonException':
        return MalformedJsonException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MalformedJsonException):
        """
        Dynamic initializer for MalformedJsonException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MalformedJsonException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MalformedJsonException__wrapper":
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
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.stream.MalformedJsonException(java.lang.Throwable)"""
        val = _MalformedJsonException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.stream.MalformedJsonException(java.lang.String,java.lang.Throwable)"""
        val = _MalformedJsonException(arg0, arg1)
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.stream.MalformedJsonException(java.lang.String)"""
        val = _MalformedJsonException(arg0)
        self.__wrapper = val

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
 
 
# CLASS: com.google.gson.stream.JsonReader
from builtins import str
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
import java.io.Reader as Reader
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JsonReader():
    """com.google.gson.stream.JsonReader"""
 
    @staticmethod
    def _wrap(java_value: _JsonReader) -> 'JsonReader':
        return JsonReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonReader):
        """
        Dynamic initializer for JsonReader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonReader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonReader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def nextDouble(self) -> float:
        """public double com.google.gson.stream.JsonReader.nextDouble() throws java.io.IOException"""
        return float._wrap(super(JsonReader, self).nextDouble())

    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonReader.setLenient(boolean)"""
        super(_JsonReader, self).setLenient(_boolean.valueOf(arg0))

    @overload
    def nextNull(self):
        """public void com.google.gson.stream.JsonReader.nextNull() throws java.io.IOException"""
        super(JsonReader, self).nextNull()

    @overload
    def nextInt(self) -> int:
        """public int com.google.gson.stream.JsonReader.nextInt() throws java.io.IOException"""
        return int._wrap(super(JsonReader, self).nextInt())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getPreviousPath(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.getPreviousPath()"""
        return str._wrap(super(JsonReader, self).getPreviousPath())

    @overload
    def getPath(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.getPath()"""
        return str._wrap(super(JsonReader, self).getPath())

    @overload
    def hasNext(self) -> bool:
        """public boolean com.google.gson.stream.JsonReader.hasNext() throws java.io.IOException"""
        return bool._wrap(super(JsonReader, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void com.google.gson.stream.JsonReader.close() throws java.io.IOException"""
        super(JsonReader, self).close()

    @overload
    def nextString(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.nextString() throws java.io.IOException"""
        return str._wrap(super(JsonReader, self).nextString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nextLong(self) -> int:
        """public long com.google.gson.stream.JsonReader.nextLong() throws java.io.IOException"""
        return int._wrap(super(JsonReader, self).nextLong())

    @overload
    def isLenient(self) -> bool:
        """public final boolean com.google.gson.stream.JsonReader.isLenient()"""
        return bool._wrap(super(JsonReader, self).isLenient())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.toString()"""
        return str._wrap(super(JsonReader, self).toString())

    @overload
    def peek(self) -> 'JsonToken':
        """public com.google.gson.stream.JsonToken com.google.gson.stream.JsonReader.peek() throws java.io.IOException"""
        return 'JsonToken'._wrap(super(JsonReader, self).peek())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def beginObject(self):
        """public void com.google.gson.stream.JsonReader.beginObject() throws java.io.IOException"""
        super(JsonReader, self).beginObject()

    @overload
    def nextBoolean(self) -> bool:
        """public boolean com.google.gson.stream.JsonReader.nextBoolean() throws java.io.IOException"""
        return bool._wrap(super(JsonReader, self).nextBoolean())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def endArray(self):
        """public void com.google.gson.stream.JsonReader.endArray() throws java.io.IOException"""
        super(JsonReader, self).endArray()

    @overload
    def skipValue(self):
        """public void com.google.gson.stream.JsonReader.skipValue() throws java.io.IOException"""
        super(JsonReader, self).skipValue()

    @overload
    def beginArray(self):
        """public void com.google.gson.stream.JsonReader.beginArray() throws java.io.IOException"""
        super(JsonReader, self).beginArray()

    @overload
    def nextName(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.nextName() throws java.io.IOException"""
        return str._wrap(super(JsonReader, self).nextName())

    @overload
    def __init__(self, arg0: 'Reader'):
        """public com.google.gson.stream.JsonReader(java.io.Reader)"""
        val = _JsonReader(arg0)
        self.__wrapper = val

    @overload
    def endObject(self):
        """public void com.google.gson.stream.JsonReader.endObject() throws java.io.IOException"""
        super(JsonReader, self).endObject()

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.gson.stream.JsonToken
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.gson.stream.JsonToken as _JsonToken
_JsonToken = _JsonToken
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
 
class JsonToken():
    """com.google.gson.stream.JsonToken"""
 
    @staticmethod
    def _wrap(java_value: _JsonToken) -> 'JsonToken':
        return JsonToken(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JsonToken):
        """
        Dynamic initializer for JsonToken.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JsonToken__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JsonToken__wrapper":
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
    def valueOf(arg0: str) -> 'JsonToken':
        """public static com.google.gson.stream.JsonToken com.google.gson.stream.JsonToken.valueOf(java.lang.String)"""
        return JsonToken._wrap(_JsonToken.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['JsonToken']:
        """public static com.google.gson.stream.JsonToken[] com.google.gson.stream.JsonToken.values()"""
        return List[JsonToken]._wrap(_JsonToken.values())