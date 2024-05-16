from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import com.google.gson.stream.MalformedJsonException as __MalformedJsonException
__MalformedJsonException = __MalformedJsonException
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MalformedJsonException(__IOException, IOException):
    """com.google.gson.stream.MalformedJsonException"""
 
    @staticmethod
    def __wrap(java_value: __MalformedJsonException) -> 'MalformedJsonException':
        return MalformedJsonException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MalformedJsonException):
        """
        Dynamic initializer for MalformedJsonException.
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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.stream.MalformedJsonException(java.lang.String,java.lang.Throwable)"""
        val = __MalformedJsonException(arg0, arg1)
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.stream.MalformedJsonException(java.lang.String)"""
        val = __MalformedJsonException(arg0)
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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.stream.MalformedJsonException(java.lang.Throwable)"""
        val = __MalformedJsonException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: com.google.gson.stream.MalformedJsonException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import com.google.gson.stream.MalformedJsonException as __MalformedJsonException
__MalformedJsonException = __MalformedJsonException
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MalformedJsonException(__IOException, IOException):
    """com.google.gson.stream.MalformedJsonException"""
 
    @staticmethod
    def __wrap(java_value: __MalformedJsonException) -> 'MalformedJsonException':
        return MalformedJsonException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MalformedJsonException):
        """
        Dynamic initializer for MalformedJsonException.
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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.google.gson.stream.MalformedJsonException(java.lang.String,java.lang.Throwable)"""
        val = __MalformedJsonException(arg0, arg1)
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.stream.MalformedJsonException(java.lang.String)"""
        val = __MalformedJsonException(arg0)
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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.google.gson.stream.MalformedJsonException(java.lang.Throwable)"""
        val = __MalformedJsonException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: com.google.gson.stream.MalformedJsonException 
 
 
# CLASS: com.google.gson.stream.JsonWriter
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import com.google.gson.stream.JsonWriter as __JsonWriter
__JsonWriter = __JsonWriter
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonWriter(__Closeable, Closeable, __Flushable, Flushable):
    """com.google.gson.stream.JsonWriter"""
 
    @staticmethod
    def __wrap(java_value: __JsonWriter) -> 'JsonWriter':
        return JsonWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonWriter):
        """
        Dynamic initializer for JsonWriter.
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
    def __init__(self, arg0: 'Writer'):
        """public com.google.gson.stream.JsonWriter(java.io.Writer)"""
        val = __JsonWriter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def value(self, arg0: float) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(double) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(__double.valueOf(arg0)))

    @overload
    def name(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.name(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).name(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def endArray(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.endArray() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).endArray())

    @override
    @overload
    def close(self):
        """public void com.google.gson.stream.JsonWriter.close() throws java.io.IOException"""
        super(JsonWriter, self).close()

    @overload
    def jsonValue(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.jsonValue(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).jsonValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def value(self, arg0: float) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(float) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(__float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isHtmlSafe(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.isHtmlSafe()"""
        return bool.__wrap(super(JsonWriter, self).isHtmlSafe())

    @overload
    def getSerializeNulls(self) -> bool:
        """public final boolean com.google.gson.stream.JsonWriter.getSerializeNulls()"""
        return bool.__wrap(super(JsonWriter, self).getSerializeNulls())

    @overload
    def setIndent(self, arg0: str):
        """public final void com.google.gson.stream.JsonWriter.setIndent(java.lang.String)"""
        super(__JsonWriter, self).setIndent(arg0)

    @overload
    def endObject(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.endObject() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).endObject())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def value(self, arg0: bool) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(boolean) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(__boolean.valueOf(arg0)))

    @overload
    def value(self, arg0: 'Number') -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.Number) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(arg0))

    @overload
    def isLenient(self) -> bool:
        """public boolean com.google.gson.stream.JsonWriter.isLenient()"""
        return bool.__wrap(super(JsonWriter, self).isLenient())

    @overload
    def beginObject(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.beginObject() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).beginObject())

    @override
    @overload
    def flush(self):
        """public void com.google.gson.stream.JsonWriter.flush() throws java.io.IOException"""
        super(JsonWriter, self).flush()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def beginArray(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.beginArray() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).beginArray())

    @overload
    def value(self, arg0: int) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(long) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(__long.valueOf(arg0)))

    @overload
    def nullValue(self) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.nullValue() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).nullValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setHtmlSafe(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setHtmlSafe(boolean)"""
        super(__JsonWriter, self).setHtmlSafe(__boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def value(self, arg0: str) -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(arg0))

    @overload
    def value(self, arg0: 'Boolean') -> 'JsonWriter':
        """public com.google.gson.stream.JsonWriter com.google.gson.stream.JsonWriter.value(java.lang.Boolean) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(arg0))

    @overload
    def setSerializeNulls(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setSerializeNulls(boolean)"""
        super(__JsonWriter, self).setSerializeNulls(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonWriter.setLenient(boolean)"""
        super(__JsonWriter, self).setLenient(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.google.gson.stream.JsonToken
import com.google.gson.stream.JsonToken as __JsonToken
__JsonToken = __JsonToken
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
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
 
class JsonToken(__Enum, Enum):
    """com.google.gson.stream.JsonToken"""
 
    @staticmethod
    def __wrap(java_value: __JsonToken) -> 'JsonToken':
        return JsonToken(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonToken):
        """
        Dynamic initializer for JsonToken.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JsonToken':
        """public static com.google.gson.stream.JsonToken com.google.gson.stream.JsonToken.valueOf(java.lang.String)"""
        return JsonToken.__wrap(__JsonToken.valueOf(arg0))

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
    def values() -> List['JsonToken']:
        """public static com.google.gson.stream.JsonToken[] com.google.gson.stream.JsonToken.values()"""
        return List[JsonToken].__wrap(__JsonToken.values()) 
 
 
# CLASS: com.google.gson.stream.JsonReader
import com.google.gson.stream.JsonToken as __JsonToken
__JsonToken = __JsonToken
from builtins import str
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
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonReader(__Closeable, Closeable):
    """com.google.gson.stream.JsonReader"""
 
    @staticmethod
    def __wrap(java_value: __JsonReader) -> 'JsonReader':
        return JsonReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonReader):
        """
        Dynamic initializer for JsonReader.
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
    def getPath(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.getPath()"""
        return str.__wrap(super(JsonReader, self).getPath())

    @overload
    def nextNull(self):
        """public void com.google.gson.stream.JsonReader.nextNull() throws java.io.IOException"""
        super(JsonReader, self).nextNull()

    @overload
    def peek(self) -> 'JsonToken':
        """public com.google.gson.stream.JsonToken com.google.gson.stream.JsonReader.peek() throws java.io.IOException"""
        return 'JsonToken'.__wrap(super(JsonReader, self).peek())

    @overload
    def nextInt(self) -> int:
        """public int com.google.gson.stream.JsonReader.nextInt() throws java.io.IOException"""
        return int.__wrap(super(JsonReader, self).nextInt())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def nextDouble(self) -> float:
        """public double com.google.gson.stream.JsonReader.nextDouble() throws java.io.IOException"""
        return float.__wrap(super(JsonReader, self).nextDouble())

    @overload
    def nextLong(self) -> int:
        """public long com.google.gson.stream.JsonReader.nextLong() throws java.io.IOException"""
        return int.__wrap(super(JsonReader, self).nextLong())

    @overload
    def __init__(self, arg0: 'Reader'):
        """public com.google.gson.stream.JsonReader(java.io.Reader)"""
        val = __JsonReader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public void com.google.gson.stream.JsonReader.close() throws java.io.IOException"""
        super(JsonReader, self).close()

    @overload
    def nextBoolean(self) -> bool:
        """public boolean com.google.gson.stream.JsonReader.nextBoolean() throws java.io.IOException"""
        return bool.__wrap(super(JsonReader, self).nextBoolean())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.toString()"""
        return str.__wrap(super(JsonReader, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def beginObject(self):
        """public void com.google.gson.stream.JsonReader.beginObject() throws java.io.IOException"""
        super(JsonReader, self).beginObject()

    @overload
    def endArray(self):
        """public void com.google.gson.stream.JsonReader.endArray() throws java.io.IOException"""
        super(JsonReader, self).endArray()

    @overload
    def skipValue(self):
        """public void com.google.gson.stream.JsonReader.skipValue() throws java.io.IOException"""
        super(JsonReader, self).skipValue()

    @overload
    def setLenient(self, arg0: bool):
        """public final void com.google.gson.stream.JsonReader.setLenient(boolean)"""
        super(__JsonReader, self).setLenient(__boolean.valueOf(arg0))

    @overload
    def beginArray(self):
        """public void com.google.gson.stream.JsonReader.beginArray() throws java.io.IOException"""
        super(JsonReader, self).beginArray()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def endObject(self):
        """public void com.google.gson.stream.JsonReader.endObject() throws java.io.IOException"""
        super(JsonReader, self).endObject()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def nextString(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.nextString() throws java.io.IOException"""
        return str.__wrap(super(JsonReader, self).nextString())

    @overload
    def getPreviousPath(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.getPreviousPath()"""
        return str.__wrap(super(JsonReader, self).getPreviousPath())

    @overload
    def hasNext(self) -> bool:
        """public boolean com.google.gson.stream.JsonReader.hasNext() throws java.io.IOException"""
        return bool.__wrap(super(JsonReader, self).hasNext())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isLenient(self) -> bool:
        """public final boolean com.google.gson.stream.JsonReader.isLenient()"""
        return bool.__wrap(super(JsonReader, self).isLenient())

    @overload
    def nextName(self) -> str:
        """public java.lang.String com.google.gson.stream.JsonReader.nextName() throws java.io.IOException"""
        return str.__wrap(super(JsonReader, self).nextName())