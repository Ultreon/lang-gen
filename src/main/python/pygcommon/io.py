from __future__ import annotations
from overload import overload


 
import com.google.common.io.CountingOutputStream as __CountingOutputStream
__CountingOutputStream = __CountingOutputStream
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.FilterOutputStream as __FilterOutputStream
__FilterOutputStream = __FilterOutputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CountingOutputStream(__FilterOutputStream, FilterOutputStream):
    """com.google.common.io.CountingOutputStream"""
 
    @staticmethod
    def __wrap(java_value: __CountingOutputStream) -> 'CountingOutputStream':
        return CountingOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CountingOutputStream):
        """
        Dynamic initializer for CountingOutputStream.
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
    def write(self, b: int):
        """public void com.google.common.io.CountingOutputStream.write(int) throws java.io.IOException"""
        super(__CountingOutputStream, self).write(__int.valueOf(b))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getCount(self) -> int:
        """public long com.google.common.io.CountingOutputStream.getCount()"""
        return int.__wrap(super(CountingOutputStream, self).getCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, out: 'OutputStream'):
        """public com.google.common.io.CountingOutputStream(java.io.OutputStream)"""
        val = __CountingOutputStream(out)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

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

    @override
    @overload
    def close(self):
        """public void com.google.common.io.CountingOutputStream.close() throws java.io.IOException"""
        super(CountingOutputStream, self).close()

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
    def write(self, b: bytes, off: int, len: int):
        """public void com.google.common.io.CountingOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(__CountingOutputStream, self).write(bytes, __int.valueOf(off), __int.valueOf(len))

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(__FilterOutputStream, self).write(bytes)

    @override
    @overload
    def flush(self):
        """public void java.io.FilterOutputStream.flush() throws java.io.IOException"""
        super(FilterOutputStream, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.io.CountingOutputStream
import com.google.common.io.CountingOutputStream as __CountingOutputStream
__CountingOutputStream = __CountingOutputStream
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.FilterOutputStream as __FilterOutputStream
__FilterOutputStream = __FilterOutputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CountingOutputStream(__FilterOutputStream, FilterOutputStream):
    """com.google.common.io.CountingOutputStream"""
 
    @staticmethod
    def __wrap(java_value: __CountingOutputStream) -> 'CountingOutputStream':
        return CountingOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CountingOutputStream):
        """
        Dynamic initializer for CountingOutputStream.
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
    def write(self, b: int):
        """public void com.google.common.io.CountingOutputStream.write(int) throws java.io.IOException"""
        super(__CountingOutputStream, self).write(__int.valueOf(b))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getCount(self) -> int:
        """public long com.google.common.io.CountingOutputStream.getCount()"""
        return int.__wrap(super(CountingOutputStream, self).getCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, out: 'OutputStream'):
        """public com.google.common.io.CountingOutputStream(java.io.OutputStream)"""
        val = __CountingOutputStream(out)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

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

    @override
    @overload
    def close(self):
        """public void com.google.common.io.CountingOutputStream.close() throws java.io.IOException"""
        super(CountingOutputStream, self).close()

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
    def write(self, b: bytes, off: int, len: int):
        """public void com.google.common.io.CountingOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(__CountingOutputStream, self).write(bytes, __int.valueOf(off), __int.valueOf(len))

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(__FilterOutputStream, self).write(bytes)

    @override
    @overload
    def flush(self):
        """public void java.io.FilterOutputStream.flush() throws java.io.IOException"""
        super(FilterOutputStream, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.io.CountingOutputStream 
 
 
# CLASS: com.google.common.io.ByteStreams
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.io.ByteArrayDataInput as __ByteArrayDataInput
__ByteArrayDataInput = __ByteArrayDataInput
from builtins import type
import java.io.ByteArrayOutputStream as ByteArrayOutputStream
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from builtins import object
from typing import List
import com.google.common.io.ByteStreams as __ByteStreams
__ByteStreams = __ByteStreams
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.io.ByteArrayInputStream as ByteArrayInputStream
import com.google.common.io.ByteArrayDataOutput as __ByteArrayDataOutput
__ByteArrayDataOutput = __ByteArrayDataOutput
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.nio.channels.WritableByteChannel as WritableByteChannel
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.channels.ReadableByteChannel as ReadableByteChannel
from builtins import bool
from builtins import int
 
class ByteStreams():
    """com.google.common.io.ByteStreams"""
 
    @staticmethod
    def __wrap(java_value: __ByteStreams) -> 'ByteStreams':
        return ByteStreams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteStreams):
        """
        Dynamic initializer for ByteStreams.
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
    def newDataInput(byteArrayInputStream: 'ByteArrayInputStream') -> 'ByteArrayDataInput':
        """public static com.google.common.io.ByteArrayDataInput com.google.common.io.ByteStreams.newDataInput(java.io.ByteArrayInputStream)"""
        return ByteArrayDataInput.__wrap(__ByteStreams.newDataInput(byteArrayInputStream))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def newDataInput(bytes: bytes) -> 'ByteArrayDataInput':
        """public static com.google.common.io.ByteArrayDataInput com.google.common.io.ByteStreams.newDataInput(byte[])"""
        return ByteArrayDataInput.__wrap(__ByteStreams.newDataInput(bytes))

    @staticmethod
    @overload
    def toByteArray(in: 'InputStream') -> List[int]:
        """public static byte[] com.google.common.io.ByteStreams.toByteArray(java.io.InputStream) throws java.io.IOException"""
        return List[int].__wrap(__ByteStreams.toByteArray(in))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def readBytes(input: 'InputStream', processor: 'ByteProcessor') -> object:
        """public static <T> T com.google.common.io.ByteStreams.readBytes(java.io.InputStream,com.google.common.io.ByteProcessor<T>) throws java.io.IOException"""
        return object.__wrap(__ByteStreams.readBytes(input, processor))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def readFully(in: 'InputStream', b: bytes):
        """public static void com.google.common.io.ByteStreams.readFully(java.io.InputStream,byte[]) throws java.io.IOException"""
        __ByteStreams.readFully(in, bytes)

    @staticmethod
    @overload
    def limit(in: 'InputStream', limit: int) -> 'InputStream':
        """public static java.io.InputStream com.google.common.io.ByteStreams.limit(java.io.InputStream,long)"""
        return InputStream.__wrap(__ByteStreams.limit(in, __long.valueOf(limit)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def copy(from: 'ReadableByteChannel', to: 'WritableByteChannel') -> int:
        """public static long com.google.common.io.ByteStreams.copy(java.nio.channels.ReadableByteChannel,java.nio.channels.WritableByteChannel) throws java.io.IOException"""
        return int.__wrap(__ByteStreams.copy(from, to))

    @staticmethod
    @overload
    def newDataOutput(byteArrayOutputStream: 'ByteArrayOutputStream') -> 'ByteArrayDataOutput':
        """public static com.google.common.io.ByteArrayDataOutput com.google.common.io.ByteStreams.newDataOutput(java.io.ByteArrayOutputStream)"""
        return ByteArrayDataOutput.__wrap(__ByteStreams.newDataOutput(byteArrayOutputStream))

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream com.google.common.io.ByteStreams.nullOutputStream()"""
        return OutputStream.__wrap(__ByteStreams.nullOutputStream())

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

    @staticmethod
    @overload
    def read(in: 'InputStream', b: bytes, off: int, len: int) -> int:
        """public static int com.google.common.io.ByteStreams.read(java.io.InputStream,byte[],int,int) throws java.io.IOException"""
        return int.__wrap(__ByteStreams.read(in, bytes, __int.valueOf(off), __int.valueOf(len)))

    @staticmethod
    @overload
    def copy(from: 'InputStream', to: 'OutputStream') -> int:
        """public static long com.google.common.io.ByteStreams.copy(java.io.InputStream,java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(__ByteStreams.copy(from, to))

    @staticmethod
    @overload
    def readFully(in: 'InputStream', b: bytes, off: int, len: int):
        """public static void com.google.common.io.ByteStreams.readFully(java.io.InputStream,byte[],int,int) throws java.io.IOException"""
        __ByteStreams.readFully(in, bytes, __int.valueOf(off), __int.valueOf(len))

    @staticmethod
    @overload
    def exhaust(in: 'InputStream') -> int:
        """public static long com.google.common.io.ByteStreams.exhaust(java.io.InputStream) throws java.io.IOException"""
        return int.__wrap(__ByteStreams.exhaust(in))

    @staticmethod
    @overload
    def newDataOutput(size: int) -> 'ByteArrayDataOutput':
        """public static com.google.common.io.ByteArrayDataOutput com.google.common.io.ByteStreams.newDataOutput(int)"""
        return ByteArrayDataOutput.__wrap(__ByteStreams.newDataOutput(__int.valueOf(size)))

    @staticmethod
    @overload
    def newDataOutput() -> 'ByteArrayDataOutput':
        """public static com.google.common.io.ByteArrayDataOutput com.google.common.io.ByteStreams.newDataOutput()"""
        return ByteArrayDataOutput.__wrap(__ByteStreams.newDataOutput())

    @staticmethod
    @overload
    def newDataInput(bytes: bytes, start: int) -> 'ByteArrayDataInput':
        """public static com.google.common.io.ByteArrayDataInput com.google.common.io.ByteStreams.newDataInput(byte[],int)"""
        return ByteArrayDataInput.__wrap(__ByteStreams.newDataInput(bytes, __int.valueOf(start)))

    @staticmethod
    @overload
    def skipFully(in: 'InputStream', n: int):
        """public static void com.google.common.io.ByteStreams.skipFully(java.io.InputStream,long) throws java.io.IOException"""
        __ByteStreams.skipFully(in, __long.valueOf(n))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.io.Closer
import java.io.Closeable as __Closeable
__Closeable = __Closeable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.Closeable as Closeable
from builtins import type
import java.lang.RuntimeException as __RuntimeException
__RuntimeException = __RuntimeException
import com.google.common.io.Closer as __Closer
__Closer = __Closer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.RuntimeException as RuntimeException
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Closer(__Closeable, Closeable):
    """com.google.common.io.Closer"""
 
    @staticmethod
    def __wrap(java_value: __Closer) -> 'Closer':
        return Closer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Closer):
        """
        Dynamic initializer for Closer.
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
    def register(self, closeable: 'Closeable') -> 'Closeable':
        """public <C extends java.io.Closeable> C com.google.common.io.Closer.register(C)"""
        return 'Closeable'.__wrap(super(__Closer, self).register(closeable))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def create() -> 'Closer':
        """public static com.google.common.io.Closer com.google.common.io.Closer.create()"""
        return Closer.__wrap(__Closer.create())

    @override
    @overload
    def close(self):
        """public void com.google.common.io.Closer.close() throws java.io.IOException"""
        super(Closer, self).close()

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
    def rethrow(self, e: 'Throwable', declaredType: 'Class') -> 'RuntimeException':
        """public <X extends java.lang.Exception> java.lang.RuntimeException com.google.common.io.Closer.rethrow(java.lang.Throwable,java.lang.Class<X>) throws java.io.IOException,X"""
        return 'RuntimeException'.__wrap(super(__Closer, self).rethrow(e, declaredType))

    @overload
    def rethrow(self, e: 'Throwable', declaredType1: 'Class', declaredType2: 'Class') -> 'RuntimeException':
        """public <X1 extends java.lang.Exception,X2 extends java.lang.Exception> java.lang.RuntimeException com.google.common.io.Closer.rethrow(java.lang.Throwable,java.lang.Class<X1>,java.lang.Class<X2>) throws java.io.IOException,X1,X2"""
        return 'RuntimeException'.__wrap(super(__Closer, self).rethrow(e, declaredType1, declaredType2))

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
    def rethrow(self, e: 'Throwable') -> 'RuntimeException':
        """public java.lang.RuntimeException com.google.common.io.Closer.rethrow(java.lang.Throwable) throws java.io.IOException"""
        return 'RuntimeException'.__wrap(super(__Closer, self).rethrow(e))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.io.Resources
from builtins import str
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
from builtins import object
import java.net.URL as URL
from typing import List
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import com.google.common.io.CharSource as __CharSource
__CharSource = __CharSource
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.net.URL as __URL
__URL = __URL
import java.lang.Object as __Object
__Object = __Object
import com.google.common.io.Resources as __Resources
__Resources = __Resources
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Resources():
    """com.google.common.io.Resources"""
 
    @staticmethod
    def __wrap(java_value: __Resources) -> 'Resources':
        return Resources(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Resources):
        """
        Dynamic initializer for Resources.
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
    def copy(from: 'URL', to: 'OutputStream'):
        """public static void com.google.common.io.Resources.copy(java.net.URL,java.io.OutputStream) throws java.io.IOException"""
        __Resources.copy(from, to)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getResource(contextClass: 'Class', resourceName: str) -> 'URL':
        """public static java.net.URL com.google.common.io.Resources.getResource(java.lang.Class<?>,java.lang.String)"""
        return URL.__wrap(__Resources.getResource(contextClass, resourceName))

    @staticmethod
    @overload
    def getResource(resourceName: str) -> 'URL':
        """public static java.net.URL com.google.common.io.Resources.getResource(java.lang.String)"""
        return URL.__wrap(__Resources.getResource(resourceName))

    @staticmethod
    @overload
    def toByteArray(url: 'URL') -> List[int]:
        """public static byte[] com.google.common.io.Resources.toByteArray(java.net.URL) throws java.io.IOException"""
        return List[int].__wrap(__Resources.toByteArray(url))

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

    @staticmethod
    @overload
    def asCharSource(url: 'URL', charset: 'Charset') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.Resources.asCharSource(java.net.URL,java.nio.charset.Charset)"""
        return CharSource.__wrap(__Resources.asCharSource(url, charset))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toString(url: 'URL', charset: 'Charset') -> str:
        """public static java.lang.String com.google.common.io.Resources.toString(java.net.URL,java.nio.charset.Charset) throws java.io.IOException"""
        return str.__wrap(__Resources.toString(url, charset))

    @staticmethod
    @overload
    def asByteSource(url: 'URL') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.Resources.asByteSource(java.net.URL)"""
        return ByteSource.__wrap(__Resources.asByteSource(url))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def readLines(url: 'URL', charset: 'Charset') -> 'List':
        """public static java.util.List<java.lang.String> com.google.common.io.Resources.readLines(java.net.URL,java.nio.charset.Charset) throws java.io.IOException"""
        return List.__wrap(__Resources.readLines(url, charset))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def readLines(url: 'URL', charset: 'Charset', callback: 'LineProcessor') -> object:
        """public static <T> T com.google.common.io.Resources.readLines(java.net.URL,java.nio.charset.Charset,com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object.__wrap(__Resources.readLines(url, charset, callback))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.io.ByteSink
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.io.ByteSink as __ByteSink
__ByteSink = __ByteSink
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import com.google.common.io.CharSink as __CharSink
__CharSink = __CharSink
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ByteSink(ABC):
    """com.google.common.io.ByteSink"""
 
    @staticmethod
    def __wrap(java_value: __ByteSink) -> 'ByteSink':
        return ByteSink(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteSink):
        """
        Dynamic initializer for ByteSink.
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
    def openStream(self, ):
        """public abstract java.io.OutputStream com.google.common.io.ByteSink.openStream() throws java.io.IOException"""
        pass

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def write(self, bytes: bytes):
        """public void com.google.common.io.ByteSink.write(byte[]) throws java.io.IOException"""
        super(__ByteSink, self).write(bytes)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def asCharSink(self, charset: 'Charset') -> 'CharSink':
        """public com.google.common.io.CharSink com.google.common.io.ByteSink.asCharSink(java.nio.charset.Charset)"""
        return 'CharSink'.__wrap(super(__ByteSink, self).asCharSink(charset))

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
    def openBufferedStream(self) -> 'OutputStream':
        """public java.io.OutputStream com.google.common.io.ByteSink.openBufferedStream() throws java.io.IOException"""
        return 'OutputStream'.__wrap(super(ByteSink, self).openBufferedStream())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def writeFrom(self, input: 'InputStream') -> int:
        """public long com.google.common.io.ByteSink.writeFrom(java.io.InputStream) throws java.io.IOException"""
        return int.__wrap(super(__ByteSink, self).writeFrom(input))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.io.CountingInputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.io.CountingInputStream as __CountingInputStream
__CountingInputStream = __CountingInputStream
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.io.FilterInputStream as __FilterInputStream
__FilterInputStream = __FilterInputStream
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CountingInputStream(__FilterInputStream, FilterInputStream):
    """com.google.common.io.CountingInputStream"""
 
    @staticmethod
    def __wrap(java_value: __CountingInputStream) -> 'CountingInputStream':
        return CountingInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CountingInputStream):
        """
        Dynamic initializer for CountingInputStream.
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
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream.__wrap(__InputStream.nullInputStream())

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.FilterInputStream.read(byte[]) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).read(bytes))

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).available())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.FilterInputStream.markSupported()"""
        return bool.__wrap(super(FilterInputStream, self).markSupported())

    @override
    @overload
    def read(self) -> int:
        """public int com.google.common.io.CountingInputStream.read() throws java.io.IOException"""
        return int.__wrap(super(CountingInputStream, self).read())

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int].__wrap(super(InputStream, self).readAllBytes())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def skip(self, n: int) -> int:
        """public long com.google.common.io.CountingInputStream.skip(long) throws java.io.IOException"""
        return int.__wrap(super(__CountingInputStream, self).skip(__long.valueOf(n)))

    @overload
    def read(self, b: bytes, off: int, len: int) -> int:
        """public int com.google.common.io.CountingInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__CountingInputStream, self).read(bytes, __int.valueOf(off), __int.valueOf(len)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, in: 'InputStream'):
        """public com.google.common.io.CountingInputStream(java.io.InputStream)"""
        val = __CountingInputStream(in)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCount(self) -> int:
        """public long com.google.common.io.CountingInputStream.getCount()"""
        return int.__wrap(super(CountingInputStream, self).getCount())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).transferTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int].__wrap(super(__InputStream, self).readNBytes(__int.valueOf(arg0)))

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).readNBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(__InputStream, self).skipNBytes(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public synchronized void com.google.common.io.CountingInputStream.reset() throws java.io.IOException"""
        super(CountingInputStream, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def mark(self, readlimit: int):
        """public synchronized void com.google.common.io.CountingInputStream.mark(int)"""
        super(__CountingInputStream, self).mark(__int.valueOf(readlimit)) 
 
 
# CLASS: com.google.common.io.FileWriteMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.google.common.io.FileWriteMode as __FileWriteMode
__FileWriteMode = __FileWriteMode
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
 
class FileWriteMode(__Enum, Enum):
    """com.google.common.io.FileWriteMode"""
 
    @staticmethod
    def __wrap(java_value: __FileWriteMode) -> 'FileWriteMode':
        return FileWriteMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileWriteMode):
        """
        Dynamic initializer for FileWriteMode.
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
    def valueOf(name: str) -> 'FileWriteMode':
        """public static com.google.common.io.FileWriteMode com.google.common.io.FileWriteMode.valueOf(java.lang.String)"""
        return FileWriteMode.__wrap(__FileWriteMode.valueOf(name))

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

    @staticmethod
    @overload
    def values() -> List['FileWriteMode']:
        """public static com.google.common.io.FileWriteMode[] com.google.common.io.FileWriteMode.values()"""
        return List[FileWriteMode].__wrap(__FileWriteMode.values())

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
 
 
# CLASS: com.google.common.io.LineReader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.io.LineReader as __LineReader
__LineReader = __LineReader
import java.lang.Integer as __int
from builtins import bool
import java.lang.Readable as Readable
from builtins import int
 
class LineReader():
    """com.google.common.io.LineReader"""
 
    @staticmethod
    def __wrap(java_value: __LineReader) -> 'LineReader':
        return LineReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LineReader):
        """
        Dynamic initializer for LineReader.
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
    def __init__(self, readable: 'Readable'):
        """public com.google.common.io.LineReader(java.lang.Readable)"""
        val = __LineReader(readable)
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
    def readLine(self) -> str:
        """public java.lang.String com.google.common.io.LineReader.readLine() throws java.io.IOException"""
        return str.__wrap(super(LineReader, self).readLine())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.io.RecursiveDeleteOption
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import com.google.common.io.RecursiveDeleteOption as __RecursiveDeleteOption
__RecursiveDeleteOption = __RecursiveDeleteOption
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
 
class RecursiveDeleteOption(__Enum, Enum):
    """com.google.common.io.RecursiveDeleteOption"""
 
    @staticmethod
    def __wrap(java_value: __RecursiveDeleteOption) -> 'RecursiveDeleteOption':
        return RecursiveDeleteOption(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecursiveDeleteOption):
        """
        Dynamic initializer for RecursiveDeleteOption.
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
    def valueOf(name: str) -> 'RecursiveDeleteOption':
        """public static com.google.common.io.RecursiveDeleteOption com.google.common.io.RecursiveDeleteOption.valueOf(java.lang.String)"""
        return RecursiveDeleteOption.__wrap(__RecursiveDeleteOption.valueOf(name))

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

    @staticmethod
    @overload
    def values() -> List['RecursiveDeleteOption']:
        """public static com.google.common.io.RecursiveDeleteOption[] com.google.common.io.RecursiveDeleteOption.values()"""
        return List[RecursiveDeleteOption].__wrap(__RecursiveDeleteOption.values())

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
 
 
# CLASS: com.google.common.io.ByteProcessor
import com.google.common.io.ByteProcessor as __ByteProcessor
__ByteProcessor = __ByteProcessor
from abc import abstractmethod, ABC
 
class ByteProcessor(ABC):
    """com.google.common.io.ByteProcessor"""
 
    @staticmethod
    def __wrap(java_value: __ByteProcessor) -> 'ByteProcessor':
        return ByteProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteProcessor):
        """
        Dynamic initializer for ByteProcessor.
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
    def getResult(self, ):
        """public abstract T com.google.common.io.ByteProcessor.getResult()"""
        pass

    @abstractmethod
    def processBytes(self, buf: bytes, off: int, len: int):
        """public abstract boolean com.google.common.io.ByteProcessor.processBytes(byte[],int,int) throws java.io.IOException"""
        pass 
 
 
# CLASS: com.google.common.io.PatternFilenameFilter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import com.google.common.io.PatternFilenameFilter as __PatternFilenameFilter
__PatternFilenameFilter = __PatternFilenameFilter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.regex.Pattern as Pattern
from builtins import bool
from builtins import int
 
class PatternFilenameFilter(__FilenameFilter, FilenameFilter):
    """com.google.common.io.PatternFilenameFilter"""
 
    @staticmethod
    def __wrap(java_value: __PatternFilenameFilter) -> 'PatternFilenameFilter':
        return PatternFilenameFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PatternFilenameFilter):
        """
        Dynamic initializer for PatternFilenameFilter.
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
    def accept(self, dir: 'File', fileName: str) -> bool:
        """public boolean com.google.common.io.PatternFilenameFilter.accept(java.io.File,java.lang.String)"""
        return bool.__wrap(super(__PatternFilenameFilter, self).accept(dir, fileName))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, patternStr: str):
        """public com.google.common.io.PatternFilenameFilter(java.lang.String)"""
        val = __PatternFilenameFilter(patternStr)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, pattern: 'Pattern'):
        """public com.google.common.io.PatternFilenameFilter(java.util.regex.Pattern)"""
        val = __PatternFilenameFilter(pattern)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.google.common.io.ByteArrayDataOutput
import com.google.common.io.ByteArrayDataOutput as __ByteArrayDataOutput
__ByteArrayDataOutput = __ByteArrayDataOutput
from abc import abstractmethod, ABC
 
class ByteArrayDataOutput(ABC, __DataOutput, DataOutput):
    """com.google.common.io.ByteArrayDataOutput"""
 
    @staticmethod
    def __wrap(java_value: __ByteArrayDataOutput) -> 'ByteArrayDataOutput':
        return ByteArrayDataOutput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteArrayDataOutput):
        """
        Dynamic initializer for ByteArrayDataOutput.
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
    def write(self, b: int):
        """public abstract void com.google.common.io.ByteArrayDataOutput.write(int)"""
        pass

    @abstractmethod
    def writeChar(self, v: int):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeChar(int)"""
        pass

    @abstractmethod
    def writeDouble(self, v: float):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeDouble(double)"""
        pass

    @abstractmethod
    def write(self, b: bytes, off: int, len: int):
        """public abstract void com.google.common.io.ByteArrayDataOutput.write(byte[],int,int)"""
        pass

    @abstractmethod
    def writeInt(self, v: int):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeInt(int)"""
        pass

    @abstractmethod
    def writeBoolean(self, v: bool):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeBoolean(boolean)"""
        pass

    @abstractmethod
    def writeUTF(self, s: str):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeUTF(java.lang.String)"""
        pass

    @abstractmethod
    def writeLong(self, v: int):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeLong(long)"""
        pass

    @abstractmethod
    def writeByte(self, v: int):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeByte(int)"""
        pass

    @abstractmethod
    def writeShort(self, v: int):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeShort(int)"""
        pass

    @abstractmethod
    def writeFloat(self, v: float):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeFloat(float)"""
        pass

    @abstractmethod
    def writeBytes(self, s: str):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeBytes(java.lang.String)"""
        pass

    @abstractmethod
    def writeChars(self, s: str):
        """public abstract void com.google.common.io.ByteArrayDataOutput.writeChars(java.lang.String)"""
        pass

    @abstractmethod
    def toByteArray(self, ):
        """public abstract byte[] com.google.common.io.ByteArrayDataOutput.toByteArray()"""
        pass

    @abstractmethod
    def write(self, b: bytes):
        """public abstract void com.google.common.io.ByteArrayDataOutput.write(byte[])"""
        pass 
 
 
# CLASS: com.google.common.io.InsecureRecursiveDeleteException
import com.google.common.io.InsecureRecursiveDeleteException as __InsecureRecursiveDeleteException
__InsecureRecursiveDeleteException = __InsecureRecursiveDeleteException
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
import java.lang.Integer as __int
from builtins import bool
import java.nio.file.FileSystemException as __FileSystemException
__FileSystemException = __FileSystemException
from builtins import int
 
class InsecureRecursiveDeleteException(__FileSystemException, FileSystemException):
    """com.google.common.io.InsecureRecursiveDeleteException"""
 
    @staticmethod
    def __wrap(java_value: __InsecureRecursiveDeleteException) -> 'InsecureRecursiveDeleteException':
        return InsecureRecursiveDeleteException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InsecureRecursiveDeleteException):
        """
        Dynamic initializer for InsecureRecursiveDeleteException.
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
    def getReason(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getReason()"""
        return str.__wrap(super(FileSystemException, self).getReason())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getMessage()"""
        return str.__wrap(super(FileSystemException, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getOtherFile(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getOtherFile()"""
        return str.__wrap(super(FileSystemException, self).getOtherFile())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @overload
    def __init__(self, file: str):
        """public com.google.common.io.InsecureRecursiveDeleteException(java.lang.String)"""
        val = __InsecureRecursiveDeleteException(file)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getFile(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getFile()"""
        return str.__wrap(super(FileSystemException, self).getFile())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.google.common.io.CharSink
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import com.google.common.io.CharSink as __CharSink
__CharSink = __CharSink
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.lang.Readable as Readable
from builtins import bool
from builtins import int
 
class CharSink(ABC):
    """com.google.common.io.CharSink"""
 
    @staticmethod
    def __wrap(java_value: __CharSink) -> 'CharSink':
        return CharSink(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSink):
        """
        Dynamic initializer for CharSink.
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
    def openStream(self, ):
        """public abstract java.io.Writer com.google.common.io.CharSink.openStream() throws java.io.IOException"""
        pass

    @overload
    def writeLines(self, lines: 'Stream'):
        """public void com.google.common.io.CharSink.writeLines(java.util.stream.Stream<? extends java.lang.CharSequence>) throws java.io.IOException"""
        super(__CharSink, self).writeLines(lines)

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

    @overload
    def openBufferedStream(self) -> 'Writer':
        """public java.io.Writer com.google.common.io.CharSink.openBufferedStream() throws java.io.IOException"""
        return 'Writer'.__wrap(super(CharSink, self).openBufferedStream())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def writeFrom(self, readable: 'Readable') -> int:
        """public long com.google.common.io.CharSink.writeFrom(java.lang.Readable) throws java.io.IOException"""
        return int.__wrap(super(__CharSink, self).writeFrom(readable))

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
    def writeLines(self, lines: 'Iterable', lineSeparator: str):
        """public void com.google.common.io.CharSink.writeLines(java.lang.Iterable<? extends java.lang.CharSequence>,java.lang.String) throws java.io.IOException"""
        super(__CharSink, self).writeLines(lines, lineSeparator)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def write(self, charSequence: 'CharSequence'):
        """public void com.google.common.io.CharSink.write(java.lang.CharSequence) throws java.io.IOException"""
        super(__CharSink, self).write(charSequence)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def writeLines(self, lines: 'Stream', lineSeparator: str):
        """public void com.google.common.io.CharSink.writeLines(java.util.stream.Stream<? extends java.lang.CharSequence>,java.lang.String) throws java.io.IOException"""
        super(__CharSink, self).writeLines(lines, lineSeparator)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def writeLines(self, lines: 'Iterable'):
        """public void com.google.common.io.CharSink.writeLines(java.lang.Iterable<? extends java.lang.CharSequence>) throws java.io.IOException"""
        super(__CharSink, self).writeLines(lines)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.io.LittleEndianDataOutputStream
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import com.google.common.io.LittleEndianDataOutputStream as __LittleEndianDataOutputStream
__LittleEndianDataOutputStream = __LittleEndianDataOutputStream
from builtins import type
import java.io.FilterOutputStream as __FilterOutputStream
__FilterOutputStream = __FilterOutputStream
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class LittleEndianDataOutputStream(__FilterOutputStream, FilterOutputStream, __DataOutput, DataOutput):
    """com.google.common.io.LittleEndianDataOutputStream"""
 
    @staticmethod
    def __wrap(java_value: __LittleEndianDataOutputStream) -> 'LittleEndianDataOutputStream':
        return LittleEndianDataOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LittleEndianDataOutputStream):
        """
        Dynamic initializer for LittleEndianDataOutputStream.
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
    def write(self, arg0: int):
        """public void java.io.FilterOutputStream.write(int) throws java.io.IOException"""
        super(__FilterOutputStream, self).write(__int.valueOf(arg0))

    @override
    @overload
    def writeByte(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeByte(int) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeByte(__int.valueOf(v))

    @override
    @overload
    def writeFloat(self, v: float):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeFloat(float) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeFloat(__float.valueOf(v))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void com.google.common.io.LittleEndianDataOutputStream.close() throws java.io.IOException"""
        super(LittleEndianDataOutputStream, self).close()

    @override
    @overload
    def writeChar(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeChar(int) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeChar(__int.valueOf(v))

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
    def writeBytes(self, s: str):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeBytes(java.lang.String) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeBytes(s)

    @override
    @overload
    def flush(self):
        """public void java.io.FilterOutputStream.flush() throws java.io.IOException"""
        super(FilterOutputStream, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def writeShort(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeShort(int) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeShort(__int.valueOf(v))

    @override
    @overload
    def writeInt(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeInt(int) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeInt(__int.valueOf(v))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def writeUTF(self, str: str):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeUTF(java.lang.String) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeUTF(str)

    @override
    @overload
    def writeLong(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeLong(long) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeLong(__long.valueOf(v))

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

    @override
    @overload
    def writeDouble(self, v: float):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeDouble(double) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeDouble(__double.valueOf(v))

    @overload
    def __init__(self, out: 'OutputStream'):
        """public com.google.common.io.LittleEndianDataOutputStream(java.io.OutputStream)"""
        val = __LittleEndianDataOutputStream(out)
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

    @override
    @overload
    def writeBoolean(self, v: bool):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeBoolean(boolean) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeBoolean(__boolean.valueOf(v))

    @override
    @overload
    def writeChars(self, s: str):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeChars(java.lang.String) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).writeChars(s)

    @override
    @overload
    def write(self, b: bytes, off: int, len: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(__LittleEndianDataOutputStream, self).write(bytes, __int.valueOf(off), __int.valueOf(len))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(__FilterOutputStream, self).write(bytes) 
 
 
# CLASS: com.google.common.io.LittleEndianDataInputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.io.FilterInputStream as __FilterInputStream
__FilterInputStream = __FilterInputStream
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.io.LittleEndianDataInputStream as __LittleEndianDataInputStream
__LittleEndianDataInputStream = __LittleEndianDataInputStream
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LittleEndianDataInputStream(__FilterInputStream, FilterInputStream, __DataInput, DataInput):
    """com.google.common.io.LittleEndianDataInputStream"""
 
    @staticmethod
    def __wrap(java_value: __LittleEndianDataInputStream) -> 'LittleEndianDataInputStream':
        return LittleEndianDataInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LittleEndianDataInputStream):
        """
        Dynamic initializer for LittleEndianDataInputStream.
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
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream.__wrap(__InputStream.nullInputStream())

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.FilterInputStream.read(byte[]) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).read(bytes))

    @override
    @overload
    def read(self) -> int:
        """public int java.io.FilterInputStream.read() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).read())

    @override
    @overload
    def readUnsignedShort(self) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.readUnsignedShort() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianDataInputStream, self).readUnsignedShort())

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).available())

    @overload
    def skipBytes(self, n: int) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.skipBytes(int) throws java.io.IOException"""
        return int.__wrap(super(__LittleEndianDataInputStream, self).skipBytes(__int.valueOf(n)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.FilterInputStream.markSupported()"""
        return bool.__wrap(super(FilterInputStream, self).markSupported())

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int].__wrap(super(InputStream, self).readAllBytes())

    @override
    @overload
    def readLine(self) -> str:
        """public java.lang.String com.google.common.io.LittleEndianDataInputStream.readLine()"""
        return str.__wrap(super(LittleEndianDataInputStream, self).readLine())

    @override
    @overload
    def readByte(self) -> int:
        """public byte com.google.common.io.LittleEndianDataInputStream.readByte() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianDataInputStream, self).readByte())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def readDouble(self) -> float:
        """public double com.google.common.io.LittleEndianDataInputStream.readDouble() throws java.io.IOException"""
        return float.__wrap(super(LittleEndianDataInputStream, self).readDouble())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def readFully(self, b: bytes, off: int, len: int):
        """public void com.google.common.io.LittleEndianDataInputStream.readFully(byte[],int,int) throws java.io.IOException"""
        super(__LittleEndianDataInputStream, self).readFully(bytes, __int.valueOf(off), __int.valueOf(len))

    @override
    @overload
    def readUnsignedByte(self) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.readUnsignedByte() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianDataInputStream, self).readUnsignedByte())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def reset(self):
        """public void java.io.FilterInputStream.reset() throws java.io.IOException"""
        super(FilterInputStream, self).reset()

    @overload
    def skip(self, arg0: int) -> int:
        """public long java.io.FilterInputStream.skip(long) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).skip(__long.valueOf(arg0)))

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).transferTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def readChar(self) -> str:
        """public char com.google.common.io.LittleEndianDataInputStream.readChar() throws java.io.IOException"""
        return str.__wrap(super(LittleEndianDataInputStream, self).readChar())

    @override
    @overload
    def readLong(self) -> int:
        """public long com.google.common.io.LittleEndianDataInputStream.readLong() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianDataInputStream, self).readLong())

    @overload
    def __init__(self, in: 'InputStream'):
        """public com.google.common.io.LittleEndianDataInputStream(java.io.InputStream)"""
        val = __LittleEndianDataInputStream(in)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int].__wrap(super(__InputStream, self).readNBytes(__int.valueOf(arg0)))

    @override
    @overload
    def readFloat(self) -> float:
        """public float com.google.common.io.LittleEndianDataInputStream.readFloat() throws java.io.IOException"""
        return float.__wrap(super(LittleEndianDataInputStream, self).readFloat())

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).readNBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def mark(self, arg0: int):
        """public void java.io.FilterInputStream.mark(int)"""
        super(__FilterInputStream, self).mark(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def readFully(self, b: bytes):
        """public void com.google.common.io.LittleEndianDataInputStream.readFully(byte[]) throws java.io.IOException"""
        super(__LittleEndianDataInputStream, self).readFully(bytes)

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(__InputStream, self).skipNBytes(__long.valueOf(arg0))

    @override
    @overload
    def readInt(self) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.readInt() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianDataInputStream, self).readInt())

    @override
    @overload
    def readUTF(self) -> str:
        """public java.lang.String com.google.common.io.LittleEndianDataInputStream.readUTF() throws java.io.IOException"""
        return str.__wrap(super(LittleEndianDataInputStream, self).readUTF())

    @override
    @overload
    def readBoolean(self) -> bool:
        """public boolean com.google.common.io.LittleEndianDataInputStream.readBoolean() throws java.io.IOException"""
        return bool.__wrap(super(LittleEndianDataInputStream, self).readBoolean())

    @override
    @overload
    def readShort(self) -> int:
        """public short com.google.common.io.LittleEndianDataInputStream.readShort() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianDataInputStream, self).readShort())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def read(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.FilterInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).read(bytes, __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: com.google.common.io.CharStreams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import com.google.common.io.CharStreams as __CharStreams
__CharStreams = __CharStreams
from builtins import object
import java.lang.Appendable as Appendable
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Readable as Readable
from builtins import bool
from builtins import int
import java.util.List as List
 
class CharStreams():
    """com.google.common.io.CharStreams"""
 
    @staticmethod
    def __wrap(java_value: __CharStreams) -> 'CharStreams':
        return CharStreams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharStreams):
        """
        Dynamic initializer for CharStreams.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def readLines(r: 'Readable') -> 'List':
        """public static java.util.List<java.lang.String> com.google.common.io.CharStreams.readLines(java.lang.Readable) throws java.io.IOException"""
        return List.__wrap(__CharStreams.readLines(r))

    @staticmethod
    @overload
    def copy(from: 'Readable', to: 'Appendable') -> int:
        """public static long com.google.common.io.CharStreams.copy(java.lang.Readable,java.lang.Appendable) throws java.io.IOException"""
        return int.__wrap(__CharStreams.copy(from, to))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def readLines(readable: 'Readable', processor: 'LineProcessor') -> object:
        """public static <T> T com.google.common.io.CharStreams.readLines(java.lang.Readable,com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object.__wrap(__CharStreams.readLines(readable, processor))

    @staticmethod
    @overload
    def asWriter(target: 'Appendable') -> 'Writer':
        """public static java.io.Writer com.google.common.io.CharStreams.asWriter(java.lang.Appendable)"""
        return Writer.__wrap(__CharStreams.asWriter(target))

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

    @staticmethod
    @overload
    def exhaust(readable: 'Readable') -> int:
        """public static long com.google.common.io.CharStreams.exhaust(java.lang.Readable) throws java.io.IOException"""
        return int.__wrap(__CharStreams.exhaust(readable))

    @staticmethod
    @overload
    def toString(r: 'Readable') -> str:
        """public static java.lang.String com.google.common.io.CharStreams.toString(java.lang.Readable) throws java.io.IOException"""
        return str.__wrap(__CharStreams.toString(r))

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

    @staticmethod
    @overload
    def skipFully(reader: 'Reader', n: int):
        """public static void com.google.common.io.CharStreams.skipFully(java.io.Reader,long) throws java.io.IOException"""
        __CharStreams.skipFully(reader, __long.valueOf(n))

    @staticmethod
    @overload
    def nullWriter() -> 'Writer':
        """public static java.io.Writer com.google.common.io.CharStreams.nullWriter()"""
        return Writer.__wrap(__CharStreams.nullWriter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.io.MoreFiles
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

import java.nio.charset.Charset as Charset
from builtins import type
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
import com.google.common.collect.ImmutableList as __ImmutableList
__ImmutableList = __ImmutableList
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import com.google.common.io.CharSource as __CharSource
__CharSource = __CharSource
import java.nio.file.attribute.FileAttribute as FileAttribute
import com.google.common.io.MoreFiles as __MoreFiles
__MoreFiles = __MoreFiles
import com.google.common.io.CharSink as __CharSink
__CharSink = __CharSink
import java.nio.file.LinkOption as LinkOption
import com.google.common.base.Predicate as __Predicate
__Predicate = __Predicate
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.io.ByteSink as __ByteSink
__ByteSink = __ByteSink
try:
    from pygcommon import graph
except ImportError:
    graph = __import_once__("pygcommon.graph")

import java.nio.file.Path as Path
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.file.OpenOption as OpenOption
import com.google.common.graph.Traverser as __Traverser
__Traverser = __Traverser
import java.lang.Integer as __int
from builtins import int
 
class MoreFiles():
    """com.google.common.io.MoreFiles"""
 
    @staticmethod
    def __wrap(java_value: __MoreFiles) -> 'MoreFiles':
        return MoreFiles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MoreFiles):
        """
        Dynamic initializer for MoreFiles.
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
    def isDirectory(*options: 'LinkOption') -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.nio.file.Path> com.google.common.io.MoreFiles.isDirectory(java.nio.file.LinkOption...)"""
        return base.Predicate.__wrap(__MoreFiles.isDirectory(options))

    @staticmethod
    @overload
    def asCharSource(path: 'Path', charset: 'Charset', *options: 'OpenOption') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.MoreFiles.asCharSource(java.nio.file.Path,java.nio.charset.Charset,java.nio.file.OpenOption...)"""
        return CharSource.__wrap(__MoreFiles.asCharSource(path, charset, options))

    @staticmethod
    @overload
    def deleteDirectoryContents(path: 'Path', *options: 'RecursiveDeleteOption'):
        """public static void com.google.common.io.MoreFiles.deleteDirectoryContents(java.nio.file.Path,com.google.common.io.RecursiveDeleteOption...) throws java.io.IOException"""
        __MoreFiles.deleteDirectoryContents(path, options)

    @staticmethod
    @overload
    def fileTraverser() -> 'graph.Traverser':
        """public static com.google.common.graph.Traverser<java.nio.file.Path> com.google.common.io.MoreFiles.fileTraverser()"""
        return graph.Traverser.__wrap(__MoreFiles.fileTraverser())

    @staticmethod
    @overload
    def asCharSink(path: 'Path', charset: 'Charset', *options: 'OpenOption') -> 'CharSink':
        """public static com.google.common.io.CharSink com.google.common.io.MoreFiles.asCharSink(java.nio.file.Path,java.nio.charset.Charset,java.nio.file.OpenOption...)"""
        return CharSink.__wrap(__MoreFiles.asCharSink(path, charset, options))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def deleteRecursively(path: 'Path', *options: 'RecursiveDeleteOption'):
        """public static void com.google.common.io.MoreFiles.deleteRecursively(java.nio.file.Path,com.google.common.io.RecursiveDeleteOption...) throws java.io.IOException"""
        __MoreFiles.deleteRecursively(path, options)

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

    @staticmethod
    @overload
    def getNameWithoutExtension(path: 'Path') -> str:
        """public static java.lang.String com.google.common.io.MoreFiles.getNameWithoutExtension(java.nio.file.Path)"""
        return str.__wrap(__MoreFiles.getNameWithoutExtension(path))

    @staticmethod
    @overload
    def equal(path1: 'Path', path2: 'Path') -> bool:
        """public static boolean com.google.common.io.MoreFiles.equal(java.nio.file.Path,java.nio.file.Path) throws java.io.IOException"""
        return bool.__wrap(__MoreFiles.equal(path1, path2))

    @staticmethod
    @overload
    def touch(path: 'Path'):
        """public static void com.google.common.io.MoreFiles.touch(java.nio.file.Path) throws java.io.IOException"""
        __MoreFiles.touch(path)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getFileExtension(path: 'Path') -> str:
        """public static java.lang.String com.google.common.io.MoreFiles.getFileExtension(java.nio.file.Path)"""
        return str.__wrap(__MoreFiles.getFileExtension(path))

    @staticmethod
    @overload
    def isRegularFile(*options: 'LinkOption') -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.nio.file.Path> com.google.common.io.MoreFiles.isRegularFile(java.nio.file.LinkOption...)"""
        return base.Predicate.__wrap(__MoreFiles.isRegularFile(options))

    @staticmethod
    @overload
    def listFiles(dir: 'Path') -> 'pygcollect.ImmutableList':
        """public static com.google.common.collect.ImmutableList<java.nio.file.Path> com.google.common.io.MoreFiles.listFiles(java.nio.file.Path) throws java.io.IOException"""
        return pygcollect.ImmutableList.__wrap(__MoreFiles.listFiles(dir))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def asByteSink(path: 'Path', *options: 'OpenOption') -> 'ByteSink':
        """public static com.google.common.io.ByteSink com.google.common.io.MoreFiles.asByteSink(java.nio.file.Path,java.nio.file.OpenOption...)"""
        return ByteSink.__wrap(__MoreFiles.asByteSink(path, options))

    @staticmethod
    @overload
    def asByteSource(path: 'Path', *options: 'OpenOption') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.MoreFiles.asByteSource(java.nio.file.Path,java.nio.file.OpenOption...)"""
        return ByteSource.__wrap(__MoreFiles.asByteSource(path, options))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createParentDirectories(path: 'Path', *attrs: 'FileAttribute'):
        """public static void com.google.common.io.MoreFiles.createParentDirectories(java.nio.file.Path,java.nio.file.attribute.FileAttribute<?>...) throws java.io.IOException"""
        __MoreFiles.createParentDirectories(path, attrs)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.io.BaseEncoding
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.io.ByteSink as __ByteSink
__ByteSink = __ByteSink
from abc import abstractmethod, ABC
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
from typing import List
import com.google.common.io.BaseEncoding as __BaseEncoding
__BaseEncoding = __BaseEncoding
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BaseEncoding(ABC):
    """com.google.common.io.BaseEncoding"""
 
    @staticmethod
    def __wrap(java_value: __BaseEncoding) -> 'BaseEncoding':
        return BaseEncoding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseEncoding):
        """
        Dynamic initializer for BaseEncoding.
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
    def base32Hex() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base32Hex()"""
        return BaseEncoding.__wrap(__BaseEncoding.base32Hex())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def base64() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base64()"""
        return BaseEncoding.__wrap(__BaseEncoding.base64())

    @abstractmethod
    def upperCase(self, ):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.upperCase()"""
        pass

    @abstractmethod
    def withSeparator(self, separator: str, n: int):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.withSeparator(java.lang.String,int)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def decodingStream(self, reader: 'Reader'):
        """public abstract java.io.InputStream com.google.common.io.BaseEncoding.decodingStream(java.io.Reader)"""
        pass

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

    @abstractmethod
    def encodingStream(self, writer: 'Writer'):
        """public abstract java.io.OutputStream com.google.common.io.BaseEncoding.encodingStream(java.io.Writer)"""
        pass

    @abstractmethod
    def canDecode(self, chars: 'CharSequence'):
        """public abstract boolean com.google.common.io.BaseEncoding.canDecode(java.lang.CharSequence)"""
        pass

    @staticmethod
    @overload
    def base16() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base16()"""
        return BaseEncoding.__wrap(__BaseEncoding.base16())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def withPadChar(self, padChar: str):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.withPadChar(char)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def encode(self, bytes: bytes, off: int, len: int) -> str:
        """public final java.lang.String com.google.common.io.BaseEncoding.encode(byte[],int,int)"""
        return str.__wrap(super(__BaseEncoding, self).encode(bytes, __int.valueOf(off), __int.valueOf(len)))

    @overload
    def decodingSource(self, encodedSource: 'CharSource') -> 'ByteSource':
        """public final com.google.common.io.ByteSource com.google.common.io.BaseEncoding.decodingSource(com.google.common.io.CharSource)"""
        return 'ByteSource'.__wrap(super(__BaseEncoding, self).decodingSource(encodedSource))

    @abstractmethod
    def omitPadding(self, ):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.omitPadding()"""
        pass

    @abstractmethod
    def lowerCase(self, ):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.lowerCase()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def decode(self, chars: 'CharSequence') -> List[int]:
        """public final byte[] com.google.common.io.BaseEncoding.decode(java.lang.CharSequence)"""
        return List[int].__wrap(super(__BaseEncoding, self).decode(chars))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def encodingSink(self, encodedSink: 'CharSink') -> 'ByteSink':
        """public final com.google.common.io.ByteSink com.google.common.io.BaseEncoding.encodingSink(com.google.common.io.CharSink)"""
        return 'ByteSink'.__wrap(super(__BaseEncoding, self).encodingSink(encodedSink))

    @staticmethod
    @overload
    def base32() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base32()"""
        return BaseEncoding.__wrap(__BaseEncoding.base32())

    @overload
    def encode(self, bytes: bytes) -> str:
        """public java.lang.String com.google.common.io.BaseEncoding.encode(byte[])"""
        return str.__wrap(super(__BaseEncoding, self).encode(bytes))

    @abstractmethod
    def ignoreCase(self, ):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.ignoreCase()"""
        pass

    @staticmethod
    @overload
    def base64Url() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base64Url()"""
        return BaseEncoding.__wrap(__BaseEncoding.base64Url())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.io.BaseEncoding$DecodingException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.io.BaseEncoding as __BaseEncoding_DecodingException
__DecodingException = __BaseEncoding_DecodingException.DecodingException
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
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DecodingException(__IOException, IOException):
    """com.google.common.io.BaseEncoding.DecodingException"""
 
    @staticmethod
    def __wrap(java_value: __DecodingException) -> 'DecodingException':
        return DecodingException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DecodingException):
        """
        Dynamic initializer for DecodingException.
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
 
 
# CLASS: com.google.common.io.ByteArrayDataInput
import com.google.common.io.ByteArrayDataInput as __ByteArrayDataInput
__ByteArrayDataInput = __ByteArrayDataInput
from abc import abstractmethod, ABC
 
class ByteArrayDataInput(ABC, __DataInput, DataInput):
    """com.google.common.io.ByteArrayDataInput"""
 
    @staticmethod
    def __wrap(java_value: __ByteArrayDataInput) -> 'ByteArrayDataInput':
        return ByteArrayDataInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteArrayDataInput):
        """
        Dynamic initializer for ByteArrayDataInput.
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
    def readInt(self, ):
        """public abstract int com.google.common.io.ByteArrayDataInput.readInt()"""
        pass

    @abstractmethod
    def readLong(self, ):
        """public abstract long com.google.common.io.ByteArrayDataInput.readLong()"""
        pass

    @abstractmethod
    def readUTF(self, ):
        """public abstract java.lang.String com.google.common.io.ByteArrayDataInput.readUTF()"""
        pass

    @abstractmethod
    def readLine(self, ):
        """public abstract java.lang.String com.google.common.io.ByteArrayDataInput.readLine()"""
        pass

    @abstractmethod
    def readFully(self, b: bytes, off: int, len: int):
        """public abstract void com.google.common.io.ByteArrayDataInput.readFully(byte[],int,int)"""
        pass

    @abstractmethod
    def skipBytes(self, n: int):
        """public abstract int com.google.common.io.ByteArrayDataInput.skipBytes(int)"""
        pass

    @abstractmethod
    def readFully(self, b: bytes):
        """public abstract void com.google.common.io.ByteArrayDataInput.readFully(byte[])"""
        pass

    @abstractmethod
    def readChar(self, ):
        """public abstract char com.google.common.io.ByteArrayDataInput.readChar()"""
        pass

    @abstractmethod
    def readFloat(self, ):
        """public abstract float com.google.common.io.ByteArrayDataInput.readFloat()"""
        pass

    @abstractmethod
    def readBoolean(self, ):
        """public abstract boolean com.google.common.io.ByteArrayDataInput.readBoolean()"""
        pass

    @abstractmethod
    def readUnsignedByte(self, ):
        """public abstract int com.google.common.io.ByteArrayDataInput.readUnsignedByte()"""
        pass

    @abstractmethod
    def readUnsignedShort(self, ):
        """public abstract int com.google.common.io.ByteArrayDataInput.readUnsignedShort()"""
        pass

    @abstractmethod
    def readShort(self, ):
        """public abstract short com.google.common.io.ByteArrayDataInput.readShort()"""
        pass

    @abstractmethod
    def readByte(self, ):
        """public abstract byte com.google.common.io.ByteArrayDataInput.readByte()"""
        pass

    @abstractmethod
    def readDouble(self, ):
        """public abstract double com.google.common.io.ByteArrayDataInput.readDouble()"""
        pass 
 
 
# CLASS: com.google.common.io.CharSource
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

import java.nio.charset.Charset as Charset
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
from abc import abstractmethod, ABC
import java.io.BufferedReader as __BufferedReader
__BufferedReader = __BufferedReader
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
import com.google.common.collect.ImmutableList as __ImmutableList
__ImmutableList = __ImmutableList
import java.util.function.Consumer as Consumer
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import com.google.common.io.CharSource as __CharSource
__CharSource = __CharSource
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Iterator as Iterator
import java.lang.Appendable as Appendable
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import com.google.common.base.Optional as __Optional
__Optional = __Optional
from builtins import int
 
class CharSource(ABC):
    """com.google.common.io.CharSource"""
 
    @staticmethod
    def __wrap(java_value: __CharSource) -> 'CharSource':
        return CharSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSource):
        """
        Dynamic initializer for CharSource.
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
    def concat(sources: 'Iterable') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(java.lang.Iterable<? extends com.google.common.io.CharSource>)"""
        return CharSource.__wrap(__CharSource.concat(sources))

    @staticmethod
    @overload
    def empty() -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.empty()"""
        return CharSource.__wrap(__CharSource.empty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def concat(sources: 'Iterator') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(java.util.Iterator<? extends com.google.common.io.CharSource>)"""
        return CharSource.__wrap(__CharSource.concat(sources))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def read(self) -> str:
        """public java.lang.String com.google.common.io.CharSource.read() throws java.io.IOException"""
        return str.__wrap(super(CharSource, self).read())

    @overload
    def asByteSource(self, charset: 'Charset') -> 'ByteSource':
        """public com.google.common.io.ByteSource com.google.common.io.CharSource.asByteSource(java.nio.charset.Charset)"""
        return 'ByteSource'.__wrap(super(__CharSource, self).asByteSource(charset))

    @overload
    def readLines(self, processor: 'LineProcessor') -> object:
        """public <T> T com.google.common.io.CharSource.readLines(com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object.__wrap(super(__CharSource, self).readLines(processor))

    @overload
    def readLines(self) -> 'pygcollect.ImmutableList':
        """public com.google.common.collect.ImmutableList<java.lang.String> com.google.common.io.CharSource.readLines() throws java.io.IOException"""
        return 'pygcollect.ImmutableList'.__wrap(super(CharSource, self).readLines())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def lines(self) -> 'Stream':
        """public java.util.stream.Stream<java.lang.String> com.google.common.io.CharSource.lines() throws java.io.IOException"""
        return 'Stream'.__wrap(super(CharSource, self).lines())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def readFirstLine(self) -> str:
        """public java.lang.String com.google.common.io.CharSource.readFirstLine() throws java.io.IOException"""
        return str.__wrap(super(CharSource, self).readFirstLine())

    @overload
    def openBufferedStream(self) -> 'BufferedReader':
        """public java.io.BufferedReader com.google.common.io.CharSource.openBufferedStream() throws java.io.IOException"""
        return 'BufferedReader'.__wrap(super(CharSource, self).openBufferedStream())

    @overload
    def lengthIfKnown(self) -> 'base.Optional':
        """public com.google.common.base.Optional<java.lang.Long> com.google.common.io.CharSource.lengthIfKnown()"""
        return 'base.Optional'.__wrap(super(CharSource, self).lengthIfKnown())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.io.CharSource.isEmpty() throws java.io.IOException"""
        return bool.__wrap(super(CharSource, self).isEmpty())

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
    def forEachLine(self, action: 'Consumer'):
        """public void com.google.common.io.CharSource.forEachLine(java.util.function.Consumer<? super java.lang.String>) throws java.io.IOException"""
        super(__CharSource, self).forEachLine(action)

    @overload
    def copyTo(self, appendable: 'Appendable') -> int:
        """public long com.google.common.io.CharSource.copyTo(java.lang.Appendable) throws java.io.IOException"""
        return int.__wrap(super(__CharSource, self).copyTo(appendable))

    @overload
    def length(self) -> int:
        """public long com.google.common.io.CharSource.length() throws java.io.IOException"""
        return int.__wrap(super(CharSource, self).length())

    @abstractmethod
    def openStream(self, ):
        """public abstract java.io.Reader com.google.common.io.CharSource.openStream() throws java.io.IOException"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def copyTo(self, sink: 'CharSink') -> int:
        """public long com.google.common.io.CharSource.copyTo(com.google.common.io.CharSink) throws java.io.IOException"""
        return int.__wrap(super(__CharSource, self).copyTo(sink))

    @staticmethod
    @overload
    def concat(*sources: 'CharSource') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(com.google.common.io.CharSource...)"""
        return CharSource.__wrap(__CharSource.concat(sources))

    @staticmethod
    @overload
    def wrap(charSequence: 'CharSequence') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.wrap(java.lang.CharSequence)"""
        return CharSource.__wrap(__CharSource.wrap(charSequence)) 
 
 
# CLASS: com.google.common.io.Files
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

import java.nio.charset.Charset as Charset
from builtins import type
import java.io.File as File
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
import java.io.BufferedReader as __BufferedReader
__BufferedReader = __BufferedReader
import java.nio.MappedByteBuffer as MappedByteBuffer
import com.google.common.io.Files as __Files
__Files = __Files
import java.nio.MappedByteBuffer as __MappedByteBuffer
__MappedByteBuffer = __MappedByteBuffer
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import com.google.common.io.CharSource as __CharSource
__CharSource = __CharSource
import java.io.File as __File
__File = __File
import java.lang.String as __string
import com.google.common.io.CharSink as __CharSink
__CharSink = __CharSink
try:
    from pygcommon import hash
except ImportError:
    hash = __import_once__("pygcommon.hash")

import com.google.common.base.Predicate as __Predicate
__Predicate = __Predicate
from builtins import bool
from builtins import str
import java.nio.channels.FileChannel.MapMode as MapMode
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.io.ByteSink as __ByteSink
__ByteSink = __ByteSink
try:
    from pygcommon import graph
except ImportError:
    graph = __import_once__("pygcommon.graph")

import com.google.common.hash.HashCode as __HashCode
__HashCode = __HashCode
import java.io.BufferedWriter as __BufferedWriter
__BufferedWriter = __BufferedWriter
from builtins import object
import java.io.BufferedWriter as BufferedWriter
import java.lang.Appendable as Appendable
from typing import List
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.graph.Traverser as __Traverser
__Traverser = __Traverser
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class Files():
    """com.google.common.io.Files"""
 
    @staticmethod
    def __wrap(java_value: __Files) -> 'Files':
        return Files(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Files):
        """
        Dynamic initializer for Files.
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
    def simplifyPath(pathname: str) -> str:
        """public static java.lang.String com.google.common.io.Files.simplifyPath(java.lang.String)"""
        return str.__wrap(__Files.simplifyPath(pathname))

    @staticmethod
    @overload
    def asCharSource(file: 'File', charset: 'Charset') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.Files.asCharSource(java.io.File,java.nio.charset.Charset)"""
        return CharSource.__wrap(__Files.asCharSource(file, charset))

    @staticmethod
    @overload
    def getNameWithoutExtension(file: str) -> str:
        """public static java.lang.String com.google.common.io.Files.getNameWithoutExtension(java.lang.String)"""
        return str.__wrap(__Files.getNameWithoutExtension(file))

    @staticmethod
    @overload
    def newWriter(file: 'File', charset: 'Charset') -> 'BufferedWriter':
        """public static java.io.BufferedWriter com.google.common.io.Files.newWriter(java.io.File,java.nio.charset.Charset) throws java.io.FileNotFoundException"""
        return BufferedWriter.__wrap(__Files.newWriter(file, charset))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def map(file: 'File') -> 'MappedByteBuffer':
        """public static java.nio.MappedByteBuffer com.google.common.io.Files.map(java.io.File) throws java.io.IOException"""
        return MappedByteBuffer.__wrap(__Files.map(file))

    @staticmethod
    @overload
    def newReader(file: 'File', charset: 'Charset') -> 'BufferedReader':
        """public static java.io.BufferedReader com.google.common.io.Files.newReader(java.io.File,java.nio.charset.Charset) throws java.io.FileNotFoundException"""
        return BufferedReader.__wrap(__Files.newReader(file, charset))

    @staticmethod
    @overload
    def toString(file: 'File', charset: 'Charset') -> str:
        """public static java.lang.String com.google.common.io.Files.toString(java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        return str.__wrap(__Files.toString(file, charset))

    @staticmethod
    @overload
    def write(from: 'CharSequence', to: 'File', charset: 'Charset'):
        """public static void com.google.common.io.Files.write(java.lang.CharSequence,java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        __Files.write(from, to, charset)

    @staticmethod
    @overload
    def copy(from: 'File', to: 'File'):
        """public static void com.google.common.io.Files.copy(java.io.File,java.io.File) throws java.io.IOException"""
        __Files.copy(from, to)

    @staticmethod
    @overload
    def readLines(file: 'File', charset: 'Charset', callback: 'LineProcessor') -> object:
        """public static <T> T com.google.common.io.Files.readLines(java.io.File,java.nio.charset.Charset,com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object.__wrap(__Files.readLines(file, charset, callback))

    @staticmethod
    @overload
    def append(from: 'CharSequence', to: 'File', charset: 'Charset'):
        """public static void com.google.common.io.Files.append(java.lang.CharSequence,java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        __Files.append(from, to, charset)

    @staticmethod
    @overload
    def fileTraverser() -> 'graph.Traverser':
        """public static com.google.common.graph.Traverser<java.io.File> com.google.common.io.Files.fileTraverser()"""
        return graph.Traverser.__wrap(__Files.fileTraverser())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def map(file: 'File', mode: 'MapMode') -> 'MappedByteBuffer':
        """public static java.nio.MappedByteBuffer com.google.common.io.Files.map(java.io.File,java.nio.channels.FileChannel$MapMode) throws java.io.IOException"""
        return MappedByteBuffer.__wrap(__Files.map(file, mode))

    @staticmethod
    @overload
    def copy(from: 'File', charset: 'Charset', to: 'Appendable'):
        """public static void com.google.common.io.Files.copy(java.io.File,java.nio.charset.Charset,java.lang.Appendable) throws java.io.IOException"""
        __Files.copy(from, charset, to)

    @staticmethod
    @overload
    def toByteArray(file: 'File') -> List[int]:
        """public static byte[] com.google.common.io.Files.toByteArray(java.io.File) throws java.io.IOException"""
        return List[int].__wrap(__Files.toByteArray(file))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def readBytes(file: 'File', processor: 'ByteProcessor') -> object:
        """public static <T> T com.google.common.io.Files.readBytes(java.io.File,com.google.common.io.ByteProcessor<T>) throws java.io.IOException"""
        return object.__wrap(__Files.readBytes(file, processor))

    @staticmethod
    @overload
    def readLines(file: 'File', charset: 'Charset') -> 'List':
        """public static java.util.List<java.lang.String> com.google.common.io.Files.readLines(java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        return List.__wrap(__Files.readLines(file, charset))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def isDirectory() -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.io.File> com.google.common.io.Files.isDirectory()"""
        return base.Predicate.__wrap(__Files.isDirectory())

    @staticmethod
    @overload
    def touch(file: 'File'):
        """public static void com.google.common.io.Files.touch(java.io.File) throws java.io.IOException"""
        __Files.touch(file)

    @staticmethod
    @overload
    def equal(file1: 'File', file2: 'File') -> bool:
        """public static boolean com.google.common.io.Files.equal(java.io.File,java.io.File) throws java.io.IOException"""
        return bool.__wrap(__Files.equal(file1, file2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def copy(from: 'File', to: 'OutputStream'):
        """public static void com.google.common.io.Files.copy(java.io.File,java.io.OutputStream) throws java.io.IOException"""
        __Files.copy(from, to)

    @staticmethod
    @overload
    def asByteSource(file: 'File') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.Files.asByteSource(java.io.File)"""
        return ByteSource.__wrap(__Files.asByteSource(file))

    @staticmethod
    @overload
    def asCharSink(file: 'File', charset: 'Charset', *modes: 'FileWriteMode') -> 'CharSink':
        """public static com.google.common.io.CharSink com.google.common.io.Files.asCharSink(java.io.File,java.nio.charset.Charset,com.google.common.io.FileWriteMode...)"""
        return CharSink.__wrap(__Files.asCharSink(file, charset, modes))

    @staticmethod
    @overload
    def map(file: 'File', mode: 'MapMode', size: int) -> 'MappedByteBuffer':
        """public static java.nio.MappedByteBuffer com.google.common.io.Files.map(java.io.File,java.nio.channels.FileChannel$MapMode,long) throws java.io.IOException"""
        return MappedByteBuffer.__wrap(__Files.map(file, mode, __long.valueOf(size)))

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

    @staticmethod
    @overload
    def hash(file: 'File', hashFunction: 'HashFunction') -> 'hash.HashCode':
        """public static com.google.common.hash.HashCode com.google.common.io.Files.hash(java.io.File,com.google.common.hash.HashFunction) throws java.io.IOException"""
        return hash.HashCode.__wrap(__Files.hash(file, hashFunction))

    @staticmethod
    @overload
    def write(from: bytes, to: 'File'):
        """public static void com.google.common.io.Files.write(byte[],java.io.File) throws java.io.IOException"""
        __Files.write(bytes, to)

    @staticmethod
    @overload
    def isFile() -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.io.File> com.google.common.io.Files.isFile()"""
        return base.Predicate.__wrap(__Files.isFile())

    @staticmethod
    @overload
    def createParentDirs(file: 'File'):
        """public static void com.google.common.io.Files.createParentDirs(java.io.File) throws java.io.IOException"""
        __Files.createParentDirs(file)

    @staticmethod
    @overload
    def createTempDir() -> 'File':
        """public static java.io.File com.google.common.io.Files.createTempDir()"""
        return File.__wrap(__Files.createTempDir())

    @staticmethod
    @overload
    def getFileExtension(fullName: str) -> str:
        """public static java.lang.String com.google.common.io.Files.getFileExtension(java.lang.String)"""
        return str.__wrap(__Files.getFileExtension(fullName))

    @staticmethod
    @overload
    def move(from: 'File', to: 'File'):
        """public static void com.google.common.io.Files.move(java.io.File,java.io.File) throws java.io.IOException"""
        __Files.move(from, to)

    @staticmethod
    @overload
    def readFirstLine(file: 'File', charset: 'Charset') -> str:
        """public static java.lang.String com.google.common.io.Files.readFirstLine(java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        return str.__wrap(__Files.readFirstLine(file, charset))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def asByteSink(file: 'File', *modes: 'FileWriteMode') -> 'ByteSink':
        """public static com.google.common.io.ByteSink com.google.common.io.Files.asByteSink(java.io.File,com.google.common.io.FileWriteMode...)"""
        return ByteSink.__wrap(__Files.asByteSink(file, modes)) 
 
 
# CLASS: com.google.common.io.FileBackedOutputStream
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.io.FileBackedOutputStream as __FileBackedOutputStream
__FileBackedOutputStream = __FileBackedOutputStream
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FileBackedOutputStream(__OutputStream, OutputStream):
    """com.google.common.io.FileBackedOutputStream"""
 
    @staticmethod
    def __wrap(java_value: __FileBackedOutputStream) -> 'FileBackedOutputStream':
        return FileBackedOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileBackedOutputStream):
        """
        Dynamic initializer for FileBackedOutputStream.
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
    def __init__(self, fileThreshold: int, resetOnFinalize: bool):
        """public com.google.common.io.FileBackedOutputStream(int,boolean)"""
        val = __FileBackedOutputStream(__int.valueOf(fileThreshold), __boolean.valueOf(resetOnFinalize))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reset(self):
        """public synchronized void com.google.common.io.FileBackedOutputStream.reset() throws java.io.IOException"""
        super(FileBackedOutputStream, self).reset()

    @override
    @overload
    def write(self, b: bytes, off: int, len: int):
        """public synchronized void com.google.common.io.FileBackedOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(__FileBackedOutputStream, self).write(bytes, __int.valueOf(off), __int.valueOf(len))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def flush(self):
        """public synchronized void com.google.common.io.FileBackedOutputStream.flush() throws java.io.IOException"""
        super(FileBackedOutputStream, self).flush()

    @overload
    def asByteSource(self) -> 'ByteSource':
        """public com.google.common.io.ByteSource com.google.common.io.FileBackedOutputStream.asByteSource()"""
        return 'ByteSource'.__wrap(super(FileBackedOutputStream, self).asByteSource())

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, fileThreshold: int):
        """public com.google.common.io.FileBackedOutputStream(int)"""
        val = __FileBackedOutputStream(__int.valueOf(fileThreshold))
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
    def write(self, b: bytes):
        """public synchronized void com.google.common.io.FileBackedOutputStream.write(byte[]) throws java.io.IOException"""
        super(__FileBackedOutputStream, self).write(bytes)

    @override
    @overload
    def write(self, b: int):
        """public synchronized void com.google.common.io.FileBackedOutputStream.write(int) throws java.io.IOException"""
        super(__FileBackedOutputStream, self).write(__int.valueOf(b))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def close(self):
        """public synchronized void com.google.common.io.FileBackedOutputStream.close() throws java.io.IOException"""
        super(FileBackedOutputStream, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.io.Flushables
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.Flushable as Flushable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.io.Flushables as __Flushables
__Flushables = __Flushables
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Flushables():
    """com.google.common.io.Flushables"""
 
    @staticmethod
    def __wrap(java_value: __Flushables) -> 'Flushables':
        return Flushables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Flushables):
        """
        Dynamic initializer for Flushables.
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

    @staticmethod
    @overload
    def flushQuietly(flushable: 'Flushable'):
        """public static void com.google.common.io.Flushables.flushQuietly(java.io.Flushable)"""
        __Flushables.flushQuietly(flushable)

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

    @staticmethod
    @overload
    def flush(flushable: 'Flushable', swallowIOException: bool):
        """public static void com.google.common.io.Flushables.flush(java.io.Flushable,boolean) throws java.io.IOException"""
        __Flushables.flush(flushable, __boolean.valueOf(swallowIOException))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.io.ByteSource
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

import java.nio.charset.Charset as Charset
from builtins import type
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
from abc import abstractmethod, ABC
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import com.google.common.io.CharSource as __CharSource
__CharSource = __CharSource
try:
    from pygcommon import hash
except ImportError:
    hash = __import_once__("pygcommon.hash")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
import com.google.common.hash.HashCode as __HashCode
__HashCode = __HashCode
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.io.InputStream as InputStream
import java.lang.Integer as __int
import com.google.common.base.Optional as __Optional
__Optional = __Optional
from builtins import int
 
class ByteSource(ABC):
    """com.google.common.io.ByteSource"""
 
    @staticmethod
    def __wrap(java_value: __ByteSource) -> 'ByteSource':
        return ByteSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteSource):
        """
        Dynamic initializer for ByteSource.
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
    def read(self) -> List[int]:
        """public byte[] com.google.common.io.ByteSource.read() throws java.io.IOException"""
        return List[int].__wrap(super(ByteSource, self).read())

    @staticmethod
    @overload
    def concat(sources: 'Iterable') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.concat(java.lang.Iterable<? extends com.google.common.io.ByteSource>)"""
        return ByteSource.__wrap(__ByteSource.concat(sources))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def read(self, processor: 'ByteProcessor') -> object:
        """public <T> T com.google.common.io.ByteSource.read(com.google.common.io.ByteProcessor<T>) throws java.io.IOException"""
        return object.__wrap(super(__ByteSource, self).read(processor))

    @overload
    def contentEquals(self, other: 'ByteSource') -> bool:
        """public boolean com.google.common.io.ByteSource.contentEquals(com.google.common.io.ByteSource) throws java.io.IOException"""
        return bool.__wrap(super(__ByteSource, self).contentEquals(other))

    @overload
    def size(self) -> int:
        """public long com.google.common.io.ByteSource.size() throws java.io.IOException"""
        return int.__wrap(super(ByteSource, self).size())

    @overload
    def hash(self, hashFunction: 'HashFunction') -> 'hash.HashCode':
        """public com.google.common.hash.HashCode com.google.common.io.ByteSource.hash(com.google.common.hash.HashFunction) throws java.io.IOException"""
        return 'hash.HashCode'.__wrap(super(__ByteSource, self).hash(hashFunction))

    @staticmethod
    @overload
    def concat(sources: 'Iterator') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.concat(java.util.Iterator<? extends com.google.common.io.ByteSource>)"""
        return ByteSource.__wrap(__ByteSource.concat(sources))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def concat(*sources: 'ByteSource') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.concat(com.google.common.io.ByteSource...)"""
        return ByteSource.__wrap(__ByteSource.concat(sources))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def asCharSource(self, charset: 'Charset') -> 'CharSource':
        """public com.google.common.io.CharSource com.google.common.io.ByteSource.asCharSource(java.nio.charset.Charset)"""
        return 'CharSource'.__wrap(super(__ByteSource, self).asCharSource(charset))

    @overload
    def copyTo(self, output: 'OutputStream') -> int:
        """public long com.google.common.io.ByteSource.copyTo(java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(super(__ByteSource, self).copyTo(output))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def openStream(self, ):
        """public abstract java.io.InputStream com.google.common.io.ByteSource.openStream() throws java.io.IOException"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def sizeIfKnown(self) -> 'base.Optional':
        """public com.google.common.base.Optional<java.lang.Long> com.google.common.io.ByteSource.sizeIfKnown()"""
        return 'base.Optional'.__wrap(super(ByteSource, self).sizeIfKnown())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def slice(self, offset: int, length: int) -> 'ByteSource':
        """public com.google.common.io.ByteSource com.google.common.io.ByteSource.slice(long,long)"""
        return 'ByteSource'.__wrap(super(__ByteSource, self).slice(__long.valueOf(offset), __long.valueOf(length)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def empty() -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.empty()"""
        return ByteSource.__wrap(__ByteSource.empty())

    @staticmethod
    @overload
    def wrap(b: bytes) -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.wrap(byte[])"""
        return ByteSource.__wrap(__ByteSource.wrap(bytes))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.io.ByteSource.isEmpty() throws java.io.IOException"""
        return bool.__wrap(super(ByteSource, self).isEmpty())

    @overload
    def openBufferedStream(self) -> 'InputStream':
        """public java.io.InputStream com.google.common.io.ByteSource.openBufferedStream() throws java.io.IOException"""
        return 'InputStream'.__wrap(super(ByteSource, self).openBufferedStream())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def copyTo(self, sink: 'ByteSink') -> int:
        """public long com.google.common.io.ByteSource.copyTo(com.google.common.io.ByteSink) throws java.io.IOException"""
        return int.__wrap(super(__ByteSource, self).copyTo(sink)) 
 
 
# CLASS: com.google.common.io.LineProcessor
import com.google.common.io.LineProcessor as __LineProcessor
__LineProcessor = __LineProcessor
from abc import abstractmethod, ABC
 
class LineProcessor(ABC):
    """com.google.common.io.LineProcessor"""
 
    @staticmethod
    def __wrap(java_value: __LineProcessor) -> 'LineProcessor':
        return LineProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LineProcessor):
        """
        Dynamic initializer for LineProcessor.
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
    def processLine(self, line: str):
        """public abstract boolean com.google.common.io.LineProcessor.processLine(java.lang.String) throws java.io.IOException"""
        pass

    @abstractmethod
    def getResult(self, ):
        """public abstract T com.google.common.io.LineProcessor.getResult()"""
        pass 
 
 
# CLASS: com.google.common.io.Closeables
import com.google.common.io.Closeables as __Closeables
__Closeables = __Closeables
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.Closeable as Closeable
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Closeables():
    """com.google.common.io.Closeables"""
 
    @staticmethod
    def __wrap(java_value: __Closeables) -> 'Closeables':
        return Closeables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Closeables):
        """
        Dynamic initializer for Closeables.
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

    @staticmethod
    @overload
    def closeQuietly(inputStream: 'InputStream'):
        """public static void com.google.common.io.Closeables.closeQuietly(java.io.InputStream)"""
        __Closeables.closeQuietly(inputStream)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def close(closeable: 'Closeable', swallowIOException: bool):
        """public static void com.google.common.io.Closeables.close(java.io.Closeable,boolean) throws java.io.IOException"""
        __Closeables.close(closeable, __boolean.valueOf(swallowIOException))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def closeQuietly(reader: 'Reader'):
        """public static void com.google.common.io.Closeables.closeQuietly(java.io.Reader)"""
        __Closeables.closeQuietly(reader)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))