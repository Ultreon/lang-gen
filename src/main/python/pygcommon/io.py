from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ImmutableList as _ImmutableList
_ImmutableList = _ImmutableList
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.io.BufferedReader as _BufferedReader
_BufferedReader = _BufferedReader
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.base.Optional as _Optional
_Optional = _Optional
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
import java.lang.Appendable as Appendable
import java.io.BufferedReader as BufferedReader
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharSource():
    """com.google.common.io.CharSource"""
 
    @staticmethod
    def _wrap(java_value: _CharSource) -> 'CharSource':
        return CharSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSource):
        """
        Dynamic initializer for CharSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def asByteSource(self, charset: 'Charset') -> 'ByteSource':
        """public com.google.common.io.ByteSource com.google.common.io.CharSource.asByteSource(java.nio.charset.Charset)"""
        return 'ByteSource'._wrap(super(_CharSource, self).asByteSource(charset))

    @overload
    def openBufferedStream(self) -> 'BufferedReader':
        """public java.io.BufferedReader com.google.common.io.CharSource.openBufferedStream() throws java.io.IOException"""
        return 'BufferedReader'._wrap(super(CharSource, self).openBufferedStream())

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
    def read(self) -> str:
        """public java.lang.String com.google.common.io.CharSource.read() throws java.io.IOException"""
        return str._wrap(super(CharSource, self).read())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def wrap(charSequence: 'CharSequence') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.wrap(java.lang.CharSequence)"""
        return CharSource._wrap(_CharSource.wrap(charSequence))

    @overload
    def readFirstLine(self) -> str:
        """public java.lang.String com.google.common.io.CharSource.readFirstLine() throws java.io.IOException"""
        return str._wrap(super(CharSource, self).readFirstLine())

    @staticmethod
    @overload
    def concat(sources: 'Iterable') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(java.lang.Iterable<? extends com.google.common.io.CharSource>)"""
        return CharSource._wrap(_CharSource.concat(sources))

    @overload
    def readLines(self) -> 'pygcollect.ImmutableList':
        """public com.google.common.collect.ImmutableList<java.lang.String> com.google.common.io.CharSource.readLines() throws java.io.IOException"""
        return 'pygcollect.ImmutableList'._wrap(super(CharSource, self).readLines())

    @overload
    def lines(self) -> 'Stream':
        """public java.util.stream.Stream<java.lang.String> com.google.common.io.CharSource.lines() throws java.io.IOException"""
        return 'Stream'._wrap(super(CharSource, self).lines())

    @overload
    def lengthIfKnown(self) -> 'base.Optional':
        """public com.google.common.base.Optional<java.lang.Long> com.google.common.io.CharSource.lengthIfKnown()"""
        return 'base.Optional'._wrap(super(CharSource, self).lengthIfKnown())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def concat(sources: 'Iterator') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(java.util.Iterator<? extends com.google.common.io.CharSource>)"""
        return CharSource._wrap(_CharSource.concat(sources))

    @overload
    def copyTo(self, sink: 'CharSink') -> int:
        """public long com.google.common.io.CharSource.copyTo(com.google.common.io.CharSink) throws java.io.IOException"""
        return int._wrap(super(_CharSource, self).copyTo(sink))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def forEachLine(self, action: 'Consumer'):
        """public void com.google.common.io.CharSource.forEachLine(java.util.function.Consumer<? super java.lang.String>) throws java.io.IOException"""
        super(_CharSource, self).forEachLine(action)

    @staticmethod
    @overload
    def empty() -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.empty()"""
        return CharSource._wrap(_CharSource.empty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def copyTo(self, appendable: 'Appendable') -> int:
        """public long com.google.common.io.CharSource.copyTo(java.lang.Appendable) throws java.io.IOException"""
        return int._wrap(super(_CharSource, self).copyTo(appendable))

    @abstractmethod
    def openStream(self, ):
        """public abstract java.io.Reader com.google.common.io.CharSource.openStream() throws java.io.IOException"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def length(self) -> int:
        """public long com.google.common.io.CharSource.length() throws java.io.IOException"""
        return int._wrap(super(CharSource, self).length())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def readLines(self, processor: 'LineProcessor') -> object:
        """public <T> T com.google.common.io.CharSource.readLines(com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object._wrap(super(_CharSource, self).readLines(processor))

    @staticmethod
    @overload
    def concat(*sources: 'CharSource') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(com.google.common.io.CharSource...)"""
        return CharSource._wrap(_CharSource.concat(sources))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.io.CharSource.isEmpty() throws java.io.IOException"""
        return bool._wrap(super(CharSource, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.io.CharSource
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ImmutableList as _ImmutableList
_ImmutableList = _ImmutableList
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.io.BufferedReader as _BufferedReader
_BufferedReader = _BufferedReader
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.base.Optional as _Optional
_Optional = _Optional
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
import java.lang.Appendable as Appendable
import java.io.BufferedReader as BufferedReader
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharSource():
    """com.google.common.io.CharSource"""
 
    @staticmethod
    def _wrap(java_value: _CharSource) -> 'CharSource':
        return CharSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSource):
        """
        Dynamic initializer for CharSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def asByteSource(self, charset: 'Charset') -> 'ByteSource':
        """public com.google.common.io.ByteSource com.google.common.io.CharSource.asByteSource(java.nio.charset.Charset)"""
        return 'ByteSource'._wrap(super(_CharSource, self).asByteSource(charset))

    @overload
    def openBufferedStream(self) -> 'BufferedReader':
        """public java.io.BufferedReader com.google.common.io.CharSource.openBufferedStream() throws java.io.IOException"""
        return 'BufferedReader'._wrap(super(CharSource, self).openBufferedStream())

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
    def read(self) -> str:
        """public java.lang.String com.google.common.io.CharSource.read() throws java.io.IOException"""
        return str._wrap(super(CharSource, self).read())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def wrap(charSequence: 'CharSequence') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.wrap(java.lang.CharSequence)"""
        return CharSource._wrap(_CharSource.wrap(charSequence))

    @overload
    def readFirstLine(self) -> str:
        """public java.lang.String com.google.common.io.CharSource.readFirstLine() throws java.io.IOException"""
        return str._wrap(super(CharSource, self).readFirstLine())

    @staticmethod
    @overload
    def concat(sources: 'Iterable') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(java.lang.Iterable<? extends com.google.common.io.CharSource>)"""
        return CharSource._wrap(_CharSource.concat(sources))

    @overload
    def readLines(self) -> 'pygcollect.ImmutableList':
        """public com.google.common.collect.ImmutableList<java.lang.String> com.google.common.io.CharSource.readLines() throws java.io.IOException"""
        return 'pygcollect.ImmutableList'._wrap(super(CharSource, self).readLines())

    @overload
    def lines(self) -> 'Stream':
        """public java.util.stream.Stream<java.lang.String> com.google.common.io.CharSource.lines() throws java.io.IOException"""
        return 'Stream'._wrap(super(CharSource, self).lines())

    @overload
    def lengthIfKnown(self) -> 'base.Optional':
        """public com.google.common.base.Optional<java.lang.Long> com.google.common.io.CharSource.lengthIfKnown()"""
        return 'base.Optional'._wrap(super(CharSource, self).lengthIfKnown())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def concat(sources: 'Iterator') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(java.util.Iterator<? extends com.google.common.io.CharSource>)"""
        return CharSource._wrap(_CharSource.concat(sources))

    @overload
    def copyTo(self, sink: 'CharSink') -> int:
        """public long com.google.common.io.CharSource.copyTo(com.google.common.io.CharSink) throws java.io.IOException"""
        return int._wrap(super(_CharSource, self).copyTo(sink))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def forEachLine(self, action: 'Consumer'):
        """public void com.google.common.io.CharSource.forEachLine(java.util.function.Consumer<? super java.lang.String>) throws java.io.IOException"""
        super(_CharSource, self).forEachLine(action)

    @staticmethod
    @overload
    def empty() -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.empty()"""
        return CharSource._wrap(_CharSource.empty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def copyTo(self, appendable: 'Appendable') -> int:
        """public long com.google.common.io.CharSource.copyTo(java.lang.Appendable) throws java.io.IOException"""
        return int._wrap(super(_CharSource, self).copyTo(appendable))

    @abstractmethod
    def openStream(self, ):
        """public abstract java.io.Reader com.google.common.io.CharSource.openStream() throws java.io.IOException"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def length(self) -> int:
        """public long com.google.common.io.CharSource.length() throws java.io.IOException"""
        return int._wrap(super(CharSource, self).length())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def readLines(self, processor: 'LineProcessor') -> object:
        """public <T> T com.google.common.io.CharSource.readLines(com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object._wrap(super(_CharSource, self).readLines(processor))

    @staticmethod
    @overload
    def concat(*sources: 'CharSource') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.CharSource.concat(com.google.common.io.CharSource...)"""
        return CharSource._wrap(_CharSource.concat(sources))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.io.CharSource.isEmpty() throws java.io.IOException"""
        return bool._wrap(super(CharSource, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.io.CharSource 
 
 
# CLASS: com.google.common.io.FileBackedOutputStream
from builtins import str
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import com.google.common.io.FileBackedOutputStream as _FileBackedOutputStream
_FileBackedOutputStream = _FileBackedOutputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileBackedOutputStream():
    """com.google.common.io.FileBackedOutputStream"""
 
    @staticmethod
    def _wrap(java_value: _FileBackedOutputStream) -> 'FileBackedOutputStream':
        return FileBackedOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileBackedOutputStream):
        """
        Dynamic initializer for FileBackedOutputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileBackedOutputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileBackedOutputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def reset(self):
        """public synchronized void com.google.common.io.FileBackedOutputStream.reset() throws java.io.IOException"""
        super(FileBackedOutputStream, self).reset()

    @override
    @overload
    def write(self, b: bytes):
        """public synchronized void com.google.common.io.FileBackedOutputStream.write(byte[]) throws java.io.IOException"""
        super(_FileBackedOutputStream, self).write(bytes)

    @override
    @overload
    def write(self, b: int):
        """public synchronized void com.google.common.io.FileBackedOutputStream.write(int) throws java.io.IOException"""
        super(_FileBackedOutputStream, self).write(_int.valueOf(b))

    @override
    @overload
    def flush(self):
        """public synchronized void com.google.common.io.FileBackedOutputStream.flush() throws java.io.IOException"""
        super(FileBackedOutputStream, self).flush()

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream._wrap(_OutputStream.nullOutputStream())

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

    @overload
    def asByteSource(self) -> 'ByteSource':
        """public com.google.common.io.ByteSource com.google.common.io.FileBackedOutputStream.asByteSource()"""
        return 'ByteSource'._wrap(super(FileBackedOutputStream, self).asByteSource())

    @overload
    def __init__(self, fileThreshold: int):
        """public com.google.common.io.FileBackedOutputStream(int)"""
        val = _FileBackedOutputStream(_int.valueOf(fileThreshold))
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, fileThreshold: int, resetOnFinalize: bool):
        """public com.google.common.io.FileBackedOutputStream(int,boolean)"""
        val = _FileBackedOutputStream(_int.valueOf(fileThreshold), _boolean.valueOf(resetOnFinalize))
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public synchronized void com.google.common.io.FileBackedOutputStream.close() throws java.io.IOException"""
        super(FileBackedOutputStream, self).close()

    @override
    @overload
    def write(self, b: bytes, off: int, len: int):
        """public synchronized void com.google.common.io.FileBackedOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(_FileBackedOutputStream, self).write(bytes, _int.valueOf(off), _int.valueOf(len))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.PatternFilenameFilter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.google.common.io.PatternFilenameFilter as _PatternFilenameFilter
_PatternFilenameFilter = _PatternFilenameFilter
import java.util.regex.Pattern as Pattern
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PatternFilenameFilter():
    """com.google.common.io.PatternFilenameFilter"""
 
    @staticmethod
    def _wrap(java_value: _PatternFilenameFilter) -> 'PatternFilenameFilter':
        return PatternFilenameFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PatternFilenameFilter):
        """
        Dynamic initializer for PatternFilenameFilter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PatternFilenameFilter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PatternFilenameFilter__wrapper":
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

    @overload
    def __init__(self, patternStr: str):
        """public com.google.common.io.PatternFilenameFilter(java.lang.String)"""
        val = _PatternFilenameFilter(patternStr)
        self.__wrapper = val

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
    def __init__(self, pattern: 'Pattern'):
        """public com.google.common.io.PatternFilenameFilter(java.util.regex.Pattern)"""
        val = _PatternFilenameFilter(pattern)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def accept(self, dir: 'File', fileName: str) -> bool:
        """public boolean com.google.common.io.PatternFilenameFilter.accept(java.io.File,java.lang.String)"""
        return bool._wrap(super(_PatternFilenameFilter, self).accept(dir, fileName))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.ByteSink
from builtins import str
import java.nio.charset.Charset as Charset
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.google.common.io.ByteSink as _ByteSink
_ByteSink = _ByteSink
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import com.google.common.io.CharSink as _CharSink
_CharSink = _CharSink
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ByteSink():
    """com.google.common.io.ByteSink"""
 
    @staticmethod
    def _wrap(java_value: _ByteSink) -> 'ByteSink':
        return ByteSink(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteSink):
        """
        Dynamic initializer for ByteSink.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteSink__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteSink__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def openStream(self, ):
        """public abstract java.io.OutputStream com.google.common.io.ByteSink.openStream() throws java.io.IOException"""
        pass

    @overload
    def openBufferedStream(self) -> 'OutputStream':
        """public java.io.OutputStream com.google.common.io.ByteSink.openBufferedStream() throws java.io.IOException"""
        return 'OutputStream'._wrap(super(ByteSink, self).openBufferedStream())

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

    @overload
    def write(self, bytes: bytes):
        """public void com.google.common.io.ByteSink.write(byte[]) throws java.io.IOException"""
        super(_ByteSink, self).write(bytes)

    @overload
    def writeFrom(self, input: 'InputStream') -> int:
        """public long com.google.common.io.ByteSink.writeFrom(java.io.InputStream) throws java.io.IOException"""
        return int._wrap(super(_ByteSink, self).writeFrom(input))

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
    def asCharSink(self, charset: 'Charset') -> 'CharSink':
        """public com.google.common.io.CharSink com.google.common.io.ByteSink.asCharSink(java.nio.charset.Charset)"""
        return 'CharSink'._wrap(super(_ByteSink, self).asCharSink(charset))

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
 
 
# CLASS: com.google.common.io.CharSink
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Writer as Writer
import com.google.common.io.CharSink as _CharSink
_CharSink = _CharSink
import java.util.stream.Stream as Stream
import java.lang.Readable as Readable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharSink():
    """com.google.common.io.CharSink"""
 
    @staticmethod
    def _wrap(java_value: _CharSink) -> 'CharSink':
        return CharSink(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSink):
        """
        Dynamic initializer for CharSink.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSink__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSink__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def openStream(self, ):
        """public abstract java.io.Writer com.google.common.io.CharSink.openStream() throws java.io.IOException"""
        pass

    @overload
    def writeLines(self, lines: 'Iterable'):
        """public void com.google.common.io.CharSink.writeLines(java.lang.Iterable<? extends java.lang.CharSequence>) throws java.io.IOException"""
        super(_CharSink, self).writeLines(lines)

    @overload
    def write(self, charSequence: 'CharSequence'):
        """public void com.google.common.io.CharSink.write(java.lang.CharSequence) throws java.io.IOException"""
        super(_CharSink, self).write(charSequence)

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

    @overload
    def writeLines(self, lines: 'Stream', lineSeparator: str):
        """public void com.google.common.io.CharSink.writeLines(java.util.stream.Stream<? extends java.lang.CharSequence>,java.lang.String) throws java.io.IOException"""
        super(_CharSink, self).writeLines(lines, lineSeparator)

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
    def openBufferedStream(self) -> 'Writer':
        """public java.io.Writer com.google.common.io.CharSink.openBufferedStream() throws java.io.IOException"""
        return 'Writer'._wrap(super(CharSink, self).openBufferedStream())

    @overload
    def writeLines(self, lines: 'Iterable', lineSeparator: str):
        """public void com.google.common.io.CharSink.writeLines(java.lang.Iterable<? extends java.lang.CharSequence>,java.lang.String) throws java.io.IOException"""
        super(_CharSink, self).writeLines(lines, lineSeparator)

    @overload
    def writeLines(self, lines: 'Stream'):
        """public void com.google.common.io.CharSink.writeLines(java.util.stream.Stream<? extends java.lang.CharSequence>) throws java.io.IOException"""
        super(_CharSink, self).writeLines(lines)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def writeFrom(self, readable: 'Readable') -> int:
        """public long com.google.common.io.CharSink.writeFrom(java.lang.Readable) throws java.io.IOException"""
        return int._wrap(super(_CharSink, self).writeFrom(readable))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.RecursiveDeleteOption
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.common.io.RecursiveDeleteOption as _RecursiveDeleteOption
_RecursiveDeleteOption = _RecursiveDeleteOption
import java.lang.Object as _object
from builtins import type
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
 
class RecursiveDeleteOption():
    """com.google.common.io.RecursiveDeleteOption"""
 
    @staticmethod
    def _wrap(java_value: _RecursiveDeleteOption) -> 'RecursiveDeleteOption':
        return RecursiveDeleteOption(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecursiveDeleteOption):
        """
        Dynamic initializer for RecursiveDeleteOption.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecursiveDeleteOption__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecursiveDeleteOption__wrapper":
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

    @staticmethod
    @overload
    def valueOf(name: str) -> 'RecursiveDeleteOption':
        """public static com.google.common.io.RecursiveDeleteOption com.google.common.io.RecursiveDeleteOption.valueOf(java.lang.String)"""
        return RecursiveDeleteOption._wrap(_RecursiveDeleteOption.valueOf(name))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['RecursiveDeleteOption']:
        """public static com.google.common.io.RecursiveDeleteOption[] com.google.common.io.RecursiveDeleteOption.values()"""
        return List[RecursiveDeleteOption]._wrap(_RecursiveDeleteOption.values()) 
 
 
# CLASS: com.google.common.io.Closer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.io.Closeable as Closeable
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.io.Closeable as _Closeable
_Closeable = _Closeable
import com.google.common.io.Closer as _Closer
_Closer = _Closer
import java.lang.RuntimeException as _RuntimeException
_RuntimeException = _RuntimeException
import java.lang.Integer as _int
import java.lang.RuntimeException as RuntimeException
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Closer():
    """com.google.common.io.Closer"""
 
    @staticmethod
    def _wrap(java_value: _Closer) -> 'Closer':
        return Closer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Closer):
        """
        Dynamic initializer for Closer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Closer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Closer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rethrow(self, e: 'Throwable', declaredType1: 'Class', declaredType2: 'Class') -> 'RuntimeException':
        """public <X1 extends java.lang.Exception,X2 extends java.lang.Exception> java.lang.RuntimeException com.google.common.io.Closer.rethrow(java.lang.Throwable,java.lang.Class<X1>,java.lang.Class<X2>) throws java.io.IOException,X1,X2"""
        return 'RuntimeException'._wrap(super(_Closer, self).rethrow(e, declaredType1, declaredType2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def register(self, closeable: 'Closeable') -> 'Closeable':
        """public <C extends java.io.Closeable> C com.google.common.io.Closer.register(C)"""
        return 'Closeable'._wrap(super(_Closer, self).register(closeable))

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

    @staticmethod
    @overload
    def create() -> 'Closer':
        """public static com.google.common.io.Closer com.google.common.io.Closer.create()"""
        return Closer._wrap(_Closer.create())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def rethrow(self, e: 'Throwable') -> 'RuntimeException':
        """public java.lang.RuntimeException com.google.common.io.Closer.rethrow(java.lang.Throwable) throws java.io.IOException"""
        return 'RuntimeException'._wrap(super(_Closer, self).rethrow(e))

    @overload
    def rethrow(self, e: 'Throwable', declaredType: 'Class') -> 'RuntimeException':
        """public <X extends java.lang.Exception> java.lang.RuntimeException com.google.common.io.Closer.rethrow(java.lang.Throwable,java.lang.Class<X>) throws java.io.IOException,X"""
        return 'RuntimeException'._wrap(super(_Closer, self).rethrow(e, declaredType))

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
 
 
# CLASS: com.google.common.io.ByteArrayDataInput
import com.google.common.io.ByteArrayDataInput as _ByteArrayDataInput
_ByteArrayDataInput = _ByteArrayDataInput
from abc import abstractmethod, ABC
 
class ByteArrayDataInput():
    """com.google.common.io.ByteArrayDataInput"""
 
    @staticmethod
    def _wrap(java_value: _ByteArrayDataInput) -> 'ByteArrayDataInput':
        return ByteArrayDataInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteArrayDataInput):
        """
        Dynamic initializer for ByteArrayDataInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteArrayDataInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteArrayDataInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.io.InsecureRecursiveDeleteException
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
import com.google.common.io.InsecureRecursiveDeleteException as _InsecureRecursiveDeleteException
_InsecureRecursiveDeleteException = _InsecureRecursiveDeleteException
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.nio.file.FileSystemException as _FileSystemException
_FileSystemException = _FileSystemException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InsecureRecursiveDeleteException():
    """com.google.common.io.InsecureRecursiveDeleteException"""
 
    @staticmethod
    def _wrap(java_value: _InsecureRecursiveDeleteException) -> 'InsecureRecursiveDeleteException':
        return InsecureRecursiveDeleteException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InsecureRecursiveDeleteException):
        """
        Dynamic initializer for InsecureRecursiveDeleteException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InsecureRecursiveDeleteException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InsecureRecursiveDeleteException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getMessage()"""
        return str._wrap(super(FileSystemException, self).getMessage())

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
    def getFile(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getFile()"""
        return str._wrap(super(FileSystemException, self).getFile())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, file: str):
        """public com.google.common.io.InsecureRecursiveDeleteException(java.lang.String)"""
        val = _InsecureRecursiveDeleteException(file)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def getOtherFile(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getOtherFile()"""
        return str._wrap(super(FileSystemException, self).getOtherFile())

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
    def getReason(self) -> str:
        """public java.lang.String java.nio.file.FileSystemException.getReason()"""
        return str._wrap(super(FileSystemException, self).getReason())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.LineReader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.io.LineReader as _LineReader
_LineReader = _LineReader
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Readable as Readable
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LineReader():
    """com.google.common.io.LineReader"""
 
    @staticmethod
    def _wrap(java_value: _LineReader) -> 'LineReader':
        return LineReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LineReader):
        """
        Dynamic initializer for LineReader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LineReader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LineReader__wrapper":
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
    def __init__(self, readable: 'Readable'):
        """public com.google.common.io.LineReader(java.lang.Readable)"""
        val = _LineReader(readable)
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
    def readLine(self) -> str:
        """public java.lang.String com.google.common.io.LineReader.readLine() throws java.io.IOException"""
        return str._wrap(super(LineReader, self).readLine())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.ByteProcessor
import com.google.common.io.ByteProcessor as _ByteProcessor
_ByteProcessor = _ByteProcessor
from abc import abstractmethod, ABC
 
class ByteProcessor():
    """com.google.common.io.ByteProcessor"""
 
    @staticmethod
    def _wrap(java_value: _ByteProcessor) -> 'ByteProcessor':
        return ByteProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteProcessor):
        """
        Dynamic initializer for ByteProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.io.LittleEndianDataOutputStream
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.io.LittleEndianDataOutputStream as _LittleEndianDataOutputStream
_LittleEndianDataOutputStream = _LittleEndianDataOutputStream
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.FilterOutputStream as _FilterOutputStream
_FilterOutputStream = _FilterOutputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LittleEndianDataOutputStream():
    """com.google.common.io.LittleEndianDataOutputStream"""
 
    @staticmethod
    def _wrap(java_value: _LittleEndianDataOutputStream) -> 'LittleEndianDataOutputStream':
        return LittleEndianDataOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LittleEndianDataOutputStream):
        """
        Dynamic initializer for LittleEndianDataOutputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LittleEndianDataOutputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LittleEndianDataOutputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def writeByte(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeByte(int) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeByte(_int.valueOf(v))

    @override
    @overload
    def writeInt(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeInt(int) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeInt(_int.valueOf(v))

    @override
    @overload
    def write(self, b: bytes, off: int, len: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).write(bytes, _int.valueOf(off), _int.valueOf(len))

    @override
    @overload
    def writeFloat(self, v: float):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeFloat(float) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeFloat(_float.valueOf(v))

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
    def writeLong(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeLong(long) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeLong(_long.valueOf(v))

    @override
    @overload
    def writeChar(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeChar(int) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeChar(_int.valueOf(v))

    @override
    @overload
    def writeUTF(self, str: str):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeUTF(java.lang.String) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeUTF(str)

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
    def writeShort(self, v: int):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeShort(int) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeShort(_int.valueOf(v))

    @override
    @overload
    def writeBoolean(self, v: bool):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeBoolean(boolean) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeBoolean(_boolean.valueOf(v))

    @override
    @overload
    def write(self, arg0: int):
        """public void java.io.FilterOutputStream.write(int) throws java.io.IOException"""
        super(_FilterOutputStream, self).write(_int.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(_FilterOutputStream, self).write(bytes)

    @override
    @overload
    def flush(self):
        """public void java.io.FilterOutputStream.flush() throws java.io.IOException"""
        super(FilterOutputStream, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, out: 'OutputStream'):
        """public com.google.common.io.LittleEndianDataOutputStream(java.io.OutputStream)"""
        val = _LittleEndianDataOutputStream(out)
        self.__wrapper = val

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream._wrap(_OutputStream.nullOutputStream())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def writeChars(self, s: str):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeChars(java.lang.String) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeChars(s)

    @override
    @overload
    def writeBytes(self, s: str):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeBytes(java.lang.String) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeBytes(s)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def writeDouble(self, v: float):
        """public void com.google.common.io.LittleEndianDataOutputStream.writeDouble(double) throws java.io.IOException"""
        super(_LittleEndianDataOutputStream, self).writeDouble(_double.valueOf(v))

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
 
 
# CLASS: com.google.common.io.BaseEncoding
import com.google.common.io.BaseEncoding as _BaseEncoding
_BaseEncoding = _BaseEncoding
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import com.google.common.io.ByteSink as _ByteSink
_ByteSink = _ByteSink
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseEncoding():
    """com.google.common.io.BaseEncoding"""
 
    @staticmethod
    def _wrap(java_value: _BaseEncoding) -> 'BaseEncoding':
        return BaseEncoding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseEncoding):
        """
        Dynamic initializer for BaseEncoding.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseEncoding__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseEncoding__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def base32() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base32()"""
        return BaseEncoding._wrap(_BaseEncoding.base32())

    @staticmethod
    @overload
    def base64() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base64()"""
        return BaseEncoding._wrap(_BaseEncoding.base64())

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

    @overload
    def encodingSink(self, encodedSink: 'CharSink') -> 'ByteSink':
        """public final com.google.common.io.ByteSink com.google.common.io.BaseEncoding.encodingSink(com.google.common.io.CharSink)"""
        return 'ByteSink'._wrap(super(_BaseEncoding, self).encodingSink(encodedSink))

    @abstractmethod
    def decodingStream(self, reader: 'Reader'):
        """public abstract java.io.InputStream com.google.common.io.BaseEncoding.decodingStream(java.io.Reader)"""
        pass

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
    def encodingStream(self, writer: 'Writer'):
        """public abstract java.io.OutputStream com.google.common.io.BaseEncoding.encodingStream(java.io.Writer)"""
        pass

    @overload
    def decodingSource(self, encodedSource: 'CharSource') -> 'ByteSource':
        """public final com.google.common.io.ByteSource com.google.common.io.BaseEncoding.decodingSource(com.google.common.io.CharSource)"""
        return 'ByteSource'._wrap(super(_BaseEncoding, self).decodingSource(encodedSource))

    @abstractmethod
    def canDecode(self, chars: 'CharSequence'):
        """public abstract boolean com.google.common.io.BaseEncoding.canDecode(java.lang.CharSequence)"""
        pass

    @overload
    def encode(self, bytes: bytes, off: int, len: int) -> str:
        """public final java.lang.String com.google.common.io.BaseEncoding.encode(byte[],int,int)"""
        return str._wrap(super(_BaseEncoding, self).encode(bytes, _int.valueOf(off), _int.valueOf(len)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def withPadChar(self, padChar: str):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.withPadChar(char)"""
        pass

    @abstractmethod
    def omitPadding(self, ):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.omitPadding()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def base32Hex() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base32Hex()"""
        return BaseEncoding._wrap(_BaseEncoding.base32Hex())

    @abstractmethod
    def lowerCase(self, ):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.lowerCase()"""
        pass

    @staticmethod
    @overload
    def base64Url() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base64Url()"""
        return BaseEncoding._wrap(_BaseEncoding.base64Url())

    @overload
    def decode(self, chars: 'CharSequence') -> List[int]:
        """public final byte[] com.google.common.io.BaseEncoding.decode(java.lang.CharSequence)"""
        return List[int]._wrap(super(_BaseEncoding, self).decode(chars))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def ignoreCase(self, ):
        """public abstract com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.ignoreCase()"""
        pass

    @overload
    def encode(self, bytes: bytes) -> str:
        """public java.lang.String com.google.common.io.BaseEncoding.encode(byte[])"""
        return str._wrap(super(_BaseEncoding, self).encode(bytes))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def base16() -> 'BaseEncoding':
        """public static com.google.common.io.BaseEncoding com.google.common.io.BaseEncoding.base16()"""
        return BaseEncoding._wrap(_BaseEncoding.base16())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.LittleEndianDataInputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.google.common.io.LittleEndianDataInputStream as _LittleEndianDataInputStream
_LittleEndianDataInputStream = _LittleEndianDataInputStream
import java.io.FilterInputStream as _FilterInputStream
_FilterInputStream = _FilterInputStream
import java.lang.String as _String
_String = _String
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LittleEndianDataInputStream():
    """com.google.common.io.LittleEndianDataInputStream"""
 
    @staticmethod
    def _wrap(java_value: _LittleEndianDataInputStream) -> 'LittleEndianDataInputStream':
        return LittleEndianDataInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LittleEndianDataInputStream):
        """
        Dynamic initializer for LittleEndianDataInputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LittleEndianDataInputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LittleEndianDataInputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def readByte(self) -> int:
        """public byte com.google.common.io.LittleEndianDataInputStream.readByte() throws java.io.IOException"""
        return int._wrap(super(LittleEndianDataInputStream, self).readByte())

    @override
    @overload
    def readUnsignedByte(self) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.readUnsignedByte() throws java.io.IOException"""
        return int._wrap(super(LittleEndianDataInputStream, self).readUnsignedByte())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).transferTo(arg0))

    @overload
    def __init__(self, in: 'InputStream'):
        """public com.google.common.io.LittleEndianDataInputStream(java.io.InputStream)"""
        val = _LittleEndianDataInputStream(in)
        self.__wrapper = val

    @overload
    def skipBytes(self, n: int) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.skipBytes(int) throws java.io.IOException"""
        return int._wrap(super(_LittleEndianDataInputStream, self).skipBytes(_int.valueOf(n)))

    @override
    @overload
    def readFloat(self) -> float:
        """public float com.google.common.io.LittleEndianDataInputStream.readFloat() throws java.io.IOException"""
        return float._wrap(super(LittleEndianDataInputStream, self).readFloat())

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int._wrap(super(FilterInputStream, self).available())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.FilterInputStream.markSupported()"""
        return bool._wrap(super(FilterInputStream, self).markSupported())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int]._wrap(super(InputStream, self).readAllBytes())

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.FilterInputStream.read(byte[]) throws java.io.IOException"""
        return int._wrap(super(_FilterInputStream, self).read(bytes))

    @override
    @overload
    def readShort(self) -> int:
        """public short com.google.common.io.LittleEndianDataInputStream.readShort() throws java.io.IOException"""
        return int._wrap(super(LittleEndianDataInputStream, self).readShort())

    @overload
    def skip(self, arg0: int) -> int:
        """public long java.io.FilterInputStream.skip(long) throws java.io.IOException"""
        return int._wrap(super(_FilterInputStream, self).skip(_long.valueOf(arg0)))

    @override
    @overload
    def readBoolean(self) -> bool:
        """public boolean com.google.common.io.LittleEndianDataInputStream.readBoolean() throws java.io.IOException"""
        return bool._wrap(super(LittleEndianDataInputStream, self).readBoolean())

    @override
    @overload
    def readFully(self, b: bytes, off: int, len: int):
        """public void com.google.common.io.LittleEndianDataInputStream.readFully(byte[],int,int) throws java.io.IOException"""
        super(_LittleEndianDataInputStream, self).readFully(bytes, _int.valueOf(off), _int.valueOf(len))

    @override
    @overload
    def readUnsignedShort(self) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.readUnsignedShort() throws java.io.IOException"""
        return int._wrap(super(LittleEndianDataInputStream, self).readUnsignedShort())

    @override
    @overload
    def readLong(self) -> int:
        """public long com.google.common.io.LittleEndianDataInputStream.readLong() throws java.io.IOException"""
        return int._wrap(super(LittleEndianDataInputStream, self).readLong())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def readChar(self) -> str:
        """public char com.google.common.io.LittleEndianDataInputStream.readChar() throws java.io.IOException"""
        return str._wrap(super(LittleEndianDataInputStream, self).readChar())

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(_InputStream, self).skipNBytes(_long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void java.io.FilterInputStream.reset() throws java.io.IOException"""
        super(FilterInputStream, self).reset()

    @override
    @overload
    def readFully(self, b: bytes):
        """public void com.google.common.io.LittleEndianDataInputStream.readFully(byte[]) throws java.io.IOException"""
        super(_LittleEndianDataInputStream, self).readFully(bytes)

    @override
    @overload
    def mark(self, arg0: int):
        """public void java.io.FilterInputStream.mark(int)"""
        super(_FilterInputStream, self).mark(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def readLine(self) -> str:
        """public java.lang.String com.google.common.io.LittleEndianDataInputStream.readLine()"""
        return str._wrap(super(LittleEndianDataInputStream, self).readLine())

    @overload
    def read(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.FilterInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_FilterInputStream, self).read(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream._wrap(_InputStream.nullInputStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).readNBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @override
    @overload
    def read(self) -> int:
        """public int java.io.FilterInputStream.read() throws java.io.IOException"""
        return int._wrap(super(FilterInputStream, self).read())

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int]._wrap(super(_InputStream, self).readNBytes(_int.valueOf(arg0)))

    @override
    @overload
    def readInt(self) -> int:
        """public int com.google.common.io.LittleEndianDataInputStream.readInt() throws java.io.IOException"""
        return int._wrap(super(LittleEndianDataInputStream, self).readInt())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def readDouble(self) -> float:
        """public double com.google.common.io.LittleEndianDataInputStream.readDouble() throws java.io.IOException"""
        return float._wrap(super(LittleEndianDataInputStream, self).readDouble())

    @override
    @overload
    def readUTF(self) -> str:
        """public java.lang.String com.google.common.io.LittleEndianDataInputStream.readUTF() throws java.io.IOException"""
        return str._wrap(super(LittleEndianDataInputStream, self).readUTF())

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
 
 
# CLASS: com.google.common.io.Resources
from builtins import str
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.net.URL as URL
from typing import List
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import java.lang.String as _string
import java.net.URL as _URL
_URL = _URL
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
from builtins import bool
import com.google.common.io.Resources as _Resources
_Resources = _Resources
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Resources():
    """com.google.common.io.Resources"""
 
    @staticmethod
    def _wrap(java_value: _Resources) -> 'Resources':
        return Resources(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Resources):
        """
        Dynamic initializer for Resources.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Resources__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Resources__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toString(url: 'URL', charset: 'Charset') -> str:
        """public static java.lang.String com.google.common.io.Resources.toString(java.net.URL,java.nio.charset.Charset) throws java.io.IOException"""
        return str._wrap(_Resources.toString(url, charset))

    @staticmethod
    @overload
    def readLines(url: 'URL', charset: 'Charset') -> 'List':
        """public static java.util.List<java.lang.String> com.google.common.io.Resources.readLines(java.net.URL,java.nio.charset.Charset) throws java.io.IOException"""
        return List._wrap(_Resources.readLines(url, charset))

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

    @staticmethod
    @overload
    def asCharSource(url: 'URL', charset: 'Charset') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.Resources.asCharSource(java.net.URL,java.nio.charset.Charset)"""
        return CharSource._wrap(_Resources.asCharSource(url, charset))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getResource(resourceName: str) -> 'URL':
        """public static java.net.URL com.google.common.io.Resources.getResource(java.lang.String)"""
        return URL._wrap(_Resources.getResource(resourceName))

    @staticmethod
    @overload
    def getResource(contextClass: 'Class', resourceName: str) -> 'URL':
        """public static java.net.URL com.google.common.io.Resources.getResource(java.lang.Class<?>,java.lang.String)"""
        return URL._wrap(_Resources.getResource(contextClass, resourceName))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def toByteArray(url: 'URL') -> List[int]:
        """public static byte[] com.google.common.io.Resources.toByteArray(java.net.URL) throws java.io.IOException"""
        return List[int]._wrap(_Resources.toByteArray(url))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def copy(from: 'URL', to: 'OutputStream'):
        """public static void com.google.common.io.Resources.copy(java.net.URL,java.io.OutputStream) throws java.io.IOException"""
        _Resources.copy(from, to)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def asByteSource(url: 'URL') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.Resources.asByteSource(java.net.URL)"""
        return ByteSource._wrap(_Resources.asByteSource(url))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def readLines(url: 'URL', charset: 'Charset', callback: 'LineProcessor') -> object:
        """public static <T> T com.google.common.io.Resources.readLines(java.net.URL,java.nio.charset.Charset,com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object._wrap(_Resources.readLines(url, charset, callback))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.CharStreams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.lang.Appendable as Appendable
import java.lang.Integer as _int
import java.io.Writer as Writer
import java.io.Reader as Reader
import com.google.common.io.CharStreams as _CharStreams
_CharStreams = _CharStreams
import java.lang.Readable as Readable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class CharStreams():
    """com.google.common.io.CharStreams"""
 
    @staticmethod
    def _wrap(java_value: _CharStreams) -> 'CharStreams':
        return CharStreams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharStreams):
        """
        Dynamic initializer for CharStreams.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharStreams__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharStreams__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def exhaust(readable: 'Readable') -> int:
        """public static long com.google.common.io.CharStreams.exhaust(java.lang.Readable) throws java.io.IOException"""
        return int._wrap(_CharStreams.exhaust(readable))

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
    def toString(r: 'Readable') -> str:
        """public static java.lang.String com.google.common.io.CharStreams.toString(java.lang.Readable) throws java.io.IOException"""
        return str._wrap(_CharStreams.toString(r))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nullWriter() -> 'Writer':
        """public static java.io.Writer com.google.common.io.CharStreams.nullWriter()"""
        return Writer._wrap(_CharStreams.nullWriter())

    @staticmethod
    @overload
    def skipFully(reader: 'Reader', n: int):
        """public static void com.google.common.io.CharStreams.skipFully(java.io.Reader,long) throws java.io.IOException"""
        _CharStreams.skipFully(reader, _long.valueOf(n))

    @staticmethod
    @overload
    def readLines(readable: 'Readable', processor: 'LineProcessor') -> object:
        """public static <T> T com.google.common.io.CharStreams.readLines(java.lang.Readable,com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object._wrap(_CharStreams.readLines(readable, processor))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def asWriter(target: 'Appendable') -> 'Writer':
        """public static java.io.Writer com.google.common.io.CharStreams.asWriter(java.lang.Appendable)"""
        return Writer._wrap(_CharStreams.asWriter(target))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def copy(from: 'Readable', to: 'Appendable') -> int:
        """public static long com.google.common.io.CharStreams.copy(java.lang.Readable,java.lang.Appendable) throws java.io.IOException"""
        return int._wrap(_CharStreams.copy(from, to))

    @staticmethod
    @overload
    def readLines(r: 'Readable') -> 'List':
        """public static java.util.List<java.lang.String> com.google.common.io.CharStreams.readLines(java.lang.Readable) throws java.io.IOException"""
        return List._wrap(_CharStreams.readLines(r))

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
 
 
# CLASS: com.google.common.io.FileWriteMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.io.FileWriteMode as _FileWriteMode
_FileWriteMode = _FileWriteMode
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
 
class FileWriteMode():
    """com.google.common.io.FileWriteMode"""
 
    @staticmethod
    def _wrap(java_value: _FileWriteMode) -> 'FileWriteMode':
        return FileWriteMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileWriteMode):
        """
        Dynamic initializer for FileWriteMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileWriteMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileWriteMode__wrapper":
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

    @staticmethod
    @overload
    def valueOf(name: str) -> 'FileWriteMode':
        """public static com.google.common.io.FileWriteMode com.google.common.io.FileWriteMode.valueOf(java.lang.String)"""
        return FileWriteMode._wrap(_FileWriteMode.valueOf(name))

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
    def values() -> List['FileWriteMode']:
        """public static com.google.common.io.FileWriteMode[] com.google.common.io.FileWriteMode.values()"""
        return List[FileWriteMode]._wrap(_FileWriteMode.values())

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
 
 
# CLASS: com.google.common.io.ByteSource
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import java.io.OutputStream as OutputStream
try:
    from pygcommon import hash
except ImportError:
    hash = _import_once("pygcommon.hash")

from builtins import bool
import com.google.common.hash.HashCode as _HashCode
_HashCode = _HashCode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.base.Optional as _Optional
_Optional = _Optional
import java.lang.Iterable as Iterable
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ByteSource():
    """com.google.common.io.ByteSource"""
 
    @staticmethod
    def _wrap(java_value: _ByteSource) -> 'ByteSource':
        return ByteSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteSource):
        """
        Dynamic initializer for ByteSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def asCharSource(self, charset: 'Charset') -> 'CharSource':
        """public com.google.common.io.CharSource com.google.common.io.ByteSource.asCharSource(java.nio.charset.Charset)"""
        return 'CharSource'._wrap(super(_ByteSource, self).asCharSource(charset))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def concat(*sources: 'ByteSource') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.concat(com.google.common.io.ByteSource...)"""
        return ByteSource._wrap(_ByteSource.concat(sources))

    @staticmethod
    @overload
    def concat(sources: 'Iterable') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.concat(java.lang.Iterable<? extends com.google.common.io.ByteSource>)"""
        return ByteSource._wrap(_ByteSource.concat(sources))

    @staticmethod
    @overload
    def wrap(b: bytes) -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.wrap(byte[])"""
        return ByteSource._wrap(_ByteSource.wrap(bytes))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.io.ByteSource.isEmpty() throws java.io.IOException"""
        return bool._wrap(super(ByteSource, self).isEmpty())

    @abstractmethod
    def openStream(self, ):
        """public abstract java.io.InputStream com.google.common.io.ByteSource.openStream() throws java.io.IOException"""
        pass

    @staticmethod
    @overload
    def empty() -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.empty()"""
        return ByteSource._wrap(_ByteSource.empty())

    @overload
    def slice(self, offset: int, length: int) -> 'ByteSource':
        """public com.google.common.io.ByteSource com.google.common.io.ByteSource.slice(long,long)"""
        return 'ByteSource'._wrap(super(_ByteSource, self).slice(_long.valueOf(offset), _long.valueOf(length)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def openBufferedStream(self) -> 'InputStream':
        """public java.io.InputStream com.google.common.io.ByteSource.openBufferedStream() throws java.io.IOException"""
        return 'InputStream'._wrap(super(ByteSource, self).openBufferedStream())

    @overload
    def sizeIfKnown(self) -> 'base.Optional':
        """public com.google.common.base.Optional<java.lang.Long> com.google.common.io.ByteSource.sizeIfKnown()"""
        return 'base.Optional'._wrap(super(ByteSource, self).sizeIfKnown())

    @overload
    def size(self) -> int:
        """public long com.google.common.io.ByteSource.size() throws java.io.IOException"""
        return int._wrap(super(ByteSource, self).size())

    @overload
    def contentEquals(self, other: 'ByteSource') -> bool:
        """public boolean com.google.common.io.ByteSource.contentEquals(com.google.common.io.ByteSource) throws java.io.IOException"""
        return bool._wrap(super(_ByteSource, self).contentEquals(other))

    @overload
    def copyTo(self, output: 'OutputStream') -> int:
        """public long com.google.common.io.ByteSource.copyTo(java.io.OutputStream) throws java.io.IOException"""
        return int._wrap(super(_ByteSource, self).copyTo(output))

    @overload
    def hash(self, hashFunction: 'HashFunction') -> 'hash.HashCode':
        """public com.google.common.hash.HashCode com.google.common.io.ByteSource.hash(com.google.common.hash.HashFunction) throws java.io.IOException"""
        return 'hash.HashCode'._wrap(super(_ByteSource, self).hash(hashFunction))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def concat(sources: 'Iterator') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.ByteSource.concat(java.util.Iterator<? extends com.google.common.io.ByteSource>)"""
        return ByteSource._wrap(_ByteSource.concat(sources))

    @overload
    def copyTo(self, sink: 'ByteSink') -> int:
        """public long com.google.common.io.ByteSource.copyTo(com.google.common.io.ByteSink) throws java.io.IOException"""
        return int._wrap(super(_ByteSource, self).copyTo(sink))

    @overload
    def read(self, processor: 'ByteProcessor') -> object:
        """public <T> T com.google.common.io.ByteSource.read(com.google.common.io.ByteProcessor<T>) throws java.io.IOException"""
        return object._wrap(super(_ByteSource, self).read(processor))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def read(self) -> List[int]:
        """public byte[] com.google.common.io.ByteSource.read() throws java.io.IOException"""
        return List[int]._wrap(super(ByteSource, self).read())

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
 
 
# CLASS: com.google.common.io.Closeables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.io.Closeable as Closeable
import java.lang.Object as _object
from builtins import type
import com.google.common.io.Closeables as _Closeables
_Closeables = _Closeables
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Closeables():
    """com.google.common.io.Closeables"""
 
    @staticmethod
    def _wrap(java_value: _Closeables) -> 'Closeables':
        return Closeables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Closeables):
        """
        Dynamic initializer for Closeables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Closeables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Closeables__wrapper":
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
    def closeQuietly(reader: 'Reader'):
        """public static void com.google.common.io.Closeables.closeQuietly(java.io.Reader)"""
        _Closeables.closeQuietly(reader)

    @staticmethod
    @overload
    def closeQuietly(inputStream: 'InputStream'):
        """public static void com.google.common.io.Closeables.closeQuietly(java.io.InputStream)"""
        _Closeables.closeQuietly(inputStream)

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

    @staticmethod
    @overload
    def close(closeable: 'Closeable', swallowIOException: bool):
        """public static void com.google.common.io.Closeables.close(java.io.Closeable,boolean) throws java.io.IOException"""
        _Closeables.close(closeable, _boolean.valueOf(swallowIOException))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.CountingInputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.FilterInputStream as _FilterInputStream
_FilterInputStream = _FilterInputStream
import java.lang.String as _String
_String = _String
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import com.google.common.io.CountingInputStream as _CountingInputStream
_CountingInputStream = _CountingInputStream
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CountingInputStream():
    """com.google.common.io.CountingInputStream"""
 
    @staticmethod
    def _wrap(java_value: _CountingInputStream) -> 'CountingInputStream':
        return CountingInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CountingInputStream):
        """
        Dynamic initializer for CountingInputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CountingInputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CountingInputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mark(self, readlimit: int):
        """public synchronized void com.google.common.io.CountingInputStream.mark(int)"""
        super(_CountingInputStream, self).mark(_int.valueOf(readlimit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).transferTo(arg0))

    @overload
    def getCount(self) -> int:
        """public long com.google.common.io.CountingInputStream.getCount()"""
        return int._wrap(super(CountingInputStream, self).getCount())

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int._wrap(super(FilterInputStream, self).available())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.FilterInputStream.markSupported()"""
        return bool._wrap(super(FilterInputStream, self).markSupported())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int]._wrap(super(InputStream, self).readAllBytes())

    @overload
    def skip(self, n: int) -> int:
        """public long com.google.common.io.CountingInputStream.skip(long) throws java.io.IOException"""
        return int._wrap(super(_CountingInputStream, self).skip(_long.valueOf(n)))

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.FilterInputStream.read(byte[]) throws java.io.IOException"""
        return int._wrap(super(_FilterInputStream, self).read(bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(_InputStream, self).skipNBytes(_long.valueOf(arg0))

    @override
    @overload
    def read(self) -> int:
        """public int com.google.common.io.CountingInputStream.read() throws java.io.IOException"""
        return int._wrap(super(CountingInputStream, self).read())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def read(self, b: bytes, off: int, len: int) -> int:
        """public int com.google.common.io.CountingInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_CountingInputStream, self).read(bytes, _int.valueOf(off), _int.valueOf(len)))

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream._wrap(_InputStream.nullInputStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).readNBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int]._wrap(super(_InputStream, self).readNBytes(_int.valueOf(arg0)))

    @override
    @overload
    def reset(self):
        """public synchronized void com.google.common.io.CountingInputStream.reset() throws java.io.IOException"""
        super(CountingInputStream, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, in: 'InputStream'):
        """public com.google.common.io.CountingInputStream(java.io.InputStream)"""
        val = _CountingInputStream(in)
        self.__wrapper = val

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
 
 
# CLASS: com.google.common.io.ByteArrayDataOutput
import com.google.common.io.ByteArrayDataOutput as _ByteArrayDataOutput
_ByteArrayDataOutput = _ByteArrayDataOutput
from abc import abstractmethod, ABC
 
class ByteArrayDataOutput():
    """com.google.common.io.ByteArrayDataOutput"""
 
    @staticmethod
    def _wrap(java_value: _ByteArrayDataOutput) -> 'ByteArrayDataOutput':
        return ByteArrayDataOutput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteArrayDataOutput):
        """
        Dynamic initializer for ByteArrayDataOutput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteArrayDataOutput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteArrayDataOutput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.io.CountingOutputStream
from builtins import str
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.FilterOutputStream as _FilterOutputStream
_FilterOutputStream = _FilterOutputStream
import com.google.common.io.CountingOutputStream as _CountingOutputStream
_CountingOutputStream = _CountingOutputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CountingOutputStream():
    """com.google.common.io.CountingOutputStream"""
 
    @staticmethod
    def _wrap(java_value: _CountingOutputStream) -> 'CountingOutputStream':
        return CountingOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CountingOutputStream):
        """
        Dynamic initializer for CountingOutputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CountingOutputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CountingOutputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, out: 'OutputStream'):
        """public com.google.common.io.CountingOutputStream(java.io.OutputStream)"""
        val = _CountingOutputStream(out)
        self.__wrapper = val

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream._wrap(_OutputStream.nullOutputStream())

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

    @overload
    def getCount(self) -> int:
        """public long com.google.common.io.CountingOutputStream.getCount()"""
        return int._wrap(super(CountingOutputStream, self).getCount())

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
    def close(self):
        """public void com.google.common.io.CountingOutputStream.close() throws java.io.IOException"""
        super(CountingOutputStream, self).close()

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(_FilterOutputStream, self).write(bytes)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, b: bytes, off: int, len: int):
        """public void com.google.common.io.CountingOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(_CountingOutputStream, self).write(bytes, _int.valueOf(off), _int.valueOf(len))

    @override
    @overload
    def write(self, b: int):
        """public void com.google.common.io.CountingOutputStream.write(int) throws java.io.IOException"""
        super(_CountingOutputStream, self).write(_int.valueOf(b))

    @override
    @overload
    def flush(self):
        """public void java.io.FilterOutputStream.flush() throws java.io.IOException"""
        super(FilterOutputStream, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.Flushables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.common.io.Flushables as _Flushables
_Flushables = _Flushables
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.io.Flushable as Flushable
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Flushables():
    """com.google.common.io.Flushables"""
 
    @staticmethod
    def _wrap(java_value: _Flushables) -> 'Flushables':
        return Flushables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Flushables):
        """
        Dynamic initializer for Flushables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Flushables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Flushables__wrapper":
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
    def flush(flushable: 'Flushable', swallowIOException: bool):
        """public static void com.google.common.io.Flushables.flush(java.io.Flushable,boolean) throws java.io.IOException"""
        _Flushables.flush(flushable, _boolean.valueOf(swallowIOException))

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
    def flushQuietly(flushable: 'Flushable'):
        """public static void com.google.common.io.Flushables.flushQuietly(java.io.Flushable)"""
        _Flushables.flushQuietly(flushable)

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
 
 
# CLASS: com.google.common.io.MoreFiles
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

import com.google.common.graph.Traverser as _Traverser
_Traverser = _Traverser
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ImmutableList as _ImmutableList
_ImmutableList = _ImmutableList
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import com.google.common.io.ByteSink as _ByteSink
_ByteSink = _ByteSink
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.nio.file.attribute.FileAttribute as FileAttribute
import com.google.common.io.CharSink as _CharSink
_CharSink = _CharSink
import java.nio.file.LinkOption as LinkOption
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pygcommon import graph
except ImportError:
    graph = _import_once("pygcommon.graph")

import java.nio.file.Path as Path
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.String as _String
_String = _String
import com.google.common.base.Predicate as _Predicate
_Predicate = _Predicate
import com.google.common.io.MoreFiles as _MoreFiles
_MoreFiles = _MoreFiles
import java.lang.Integer as _int
import java.nio.file.OpenOption as OpenOption
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MoreFiles():
    """com.google.common.io.MoreFiles"""
 
    @staticmethod
    def _wrap(java_value: _MoreFiles) -> 'MoreFiles':
        return MoreFiles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MoreFiles):
        """
        Dynamic initializer for MoreFiles.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MoreFiles__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MoreFiles__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def asByteSink(path: 'Path', *options: 'OpenOption') -> 'ByteSink':
        """public static com.google.common.io.ByteSink com.google.common.io.MoreFiles.asByteSink(java.nio.file.Path,java.nio.file.OpenOption...)"""
        return ByteSink._wrap(_MoreFiles.asByteSink(path, options))

    @staticmethod
    @overload
    def equal(path1: 'Path', path2: 'Path') -> bool:
        """public static boolean com.google.common.io.MoreFiles.equal(java.nio.file.Path,java.nio.file.Path) throws java.io.IOException"""
        return bool._wrap(_MoreFiles.equal(path1, path2))

    @staticmethod
    @overload
    def asCharSink(path: 'Path', charset: 'Charset', *options: 'OpenOption') -> 'CharSink':
        """public static com.google.common.io.CharSink com.google.common.io.MoreFiles.asCharSink(java.nio.file.Path,java.nio.charset.Charset,java.nio.file.OpenOption...)"""
        return CharSink._wrap(_MoreFiles.asCharSink(path, charset, options))

    @staticmethod
    @overload
    def asByteSource(path: 'Path', *options: 'OpenOption') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.MoreFiles.asByteSource(java.nio.file.Path,java.nio.file.OpenOption...)"""
        return ByteSource._wrap(_MoreFiles.asByteSource(path, options))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isRegularFile(*options: 'LinkOption') -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.nio.file.Path> com.google.common.io.MoreFiles.isRegularFile(java.nio.file.LinkOption...)"""
        return base.Predicate._wrap(_MoreFiles.isRegularFile(options))

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
    def touch(path: 'Path'):
        """public static void com.google.common.io.MoreFiles.touch(java.nio.file.Path) throws java.io.IOException"""
        _MoreFiles.touch(path)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getFileExtension(path: 'Path') -> str:
        """public static java.lang.String com.google.common.io.MoreFiles.getFileExtension(java.nio.file.Path)"""
        return str._wrap(_MoreFiles.getFileExtension(path))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isDirectory(*options: 'LinkOption') -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.nio.file.Path> com.google.common.io.MoreFiles.isDirectory(java.nio.file.LinkOption...)"""
        return base.Predicate._wrap(_MoreFiles.isDirectory(options))

    @staticmethod
    @overload
    def getNameWithoutExtension(path: 'Path') -> str:
        """public static java.lang.String com.google.common.io.MoreFiles.getNameWithoutExtension(java.nio.file.Path)"""
        return str._wrap(_MoreFiles.getNameWithoutExtension(path))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createParentDirectories(path: 'Path', *attrs: 'FileAttribute'):
        """public static void com.google.common.io.MoreFiles.createParentDirectories(java.nio.file.Path,java.nio.file.attribute.FileAttribute<?>...) throws java.io.IOException"""
        _MoreFiles.createParentDirectories(path, attrs)

    @staticmethod
    @overload
    def deleteRecursively(path: 'Path', *options: 'RecursiveDeleteOption'):
        """public static void com.google.common.io.MoreFiles.deleteRecursively(java.nio.file.Path,com.google.common.io.RecursiveDeleteOption...) throws java.io.IOException"""
        _MoreFiles.deleteRecursively(path, options)

    @staticmethod
    @overload
    def deleteDirectoryContents(path: 'Path', *options: 'RecursiveDeleteOption'):
        """public static void com.google.common.io.MoreFiles.deleteDirectoryContents(java.nio.file.Path,com.google.common.io.RecursiveDeleteOption...) throws java.io.IOException"""
        _MoreFiles.deleteDirectoryContents(path, options)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def asCharSource(path: 'Path', charset: 'Charset', *options: 'OpenOption') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.MoreFiles.asCharSource(java.nio.file.Path,java.nio.charset.Charset,java.nio.file.OpenOption...)"""
        return CharSource._wrap(_MoreFiles.asCharSource(path, charset, options))

    @staticmethod
    @overload
    def listFiles(dir: 'Path') -> 'pygcollect.ImmutableList':
        """public static com.google.common.collect.ImmutableList<java.nio.file.Path> com.google.common.io.MoreFiles.listFiles(java.nio.file.Path) throws java.io.IOException"""
        return pygcollect.ImmutableList._wrap(_MoreFiles.listFiles(dir))

    @staticmethod
    @overload
    def fileTraverser() -> 'graph.Traverser':
        """public static com.google.common.graph.Traverser<java.nio.file.Path> com.google.common.io.MoreFiles.fileTraverser()"""
        return graph.Traverser._wrap(_MoreFiles.fileTraverser())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.BaseEncoding$DecodingException
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
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import com.google.common.io.BaseEncoding as _BaseEncoding_DecodingException
_DecodingException = _BaseEncoding_DecodingException.DecodingException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DecodingException():
    """com.google.common.io.BaseEncoding.DecodingException"""
 
    @staticmethod
    def _wrap(java_value: _DecodingException) -> 'DecodingException':
        return DecodingException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DecodingException):
        """
        Dynamic initializer for DecodingException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DecodingException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DecodingException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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
 
 
# CLASS: com.google.common.io.LineProcessor
from abc import abstractmethod, ABC
import com.google.common.io.LineProcessor as _LineProcessor
_LineProcessor = _LineProcessor
 
class LineProcessor():
    """com.google.common.io.LineProcessor"""
 
    @staticmethod
    def _wrap(java_value: _LineProcessor) -> 'LineProcessor':
        return LineProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LineProcessor):
        """
        Dynamic initializer for LineProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LineProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LineProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.io.Files
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

import com.google.common.graph.Traverser as _Traverser
_Traverser = _Traverser
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.io.File as File
import com.google.common.io.Files as _Files
_Files = _Files
import java.nio.MappedByteBuffer as MappedByteBuffer
import java.io.BufferedReader as _BufferedReader
_BufferedReader = _BufferedReader
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import com.google.common.io.ByteSink as _ByteSink
_ByteSink = _ByteSink
import java.io.BufferedWriter as _BufferedWriter
_BufferedWriter = _BufferedWriter
import java.lang.String as _string
import java.io.OutputStream as OutputStream
import com.google.common.io.CharSink as _CharSink
_CharSink = _CharSink
try:
    from pygcommon import hash
except ImportError:
    hash = _import_once("pygcommon.hash")

from builtins import bool
import com.google.common.hash.HashCode as _HashCode
_HashCode = _HashCode
from builtins import str
import java.nio.channels.FileChannel.MapMode as MapMode
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pygcommon import graph
except ImportError:
    graph = _import_once("pygcommon.graph")

import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.String as _String
_String = _String
from builtins import object
import java.io.BufferedWriter as BufferedWriter
import com.google.common.base.Predicate as _Predicate
_Predicate = _Predicate
import java.util.List as _List
_List = _List
import java.lang.Appendable as Appendable
from typing import List
import java.io.BufferedReader as BufferedReader
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.nio.MappedByteBuffer as _MappedByteBuffer
_MappedByteBuffer = _MappedByteBuffer
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Files():
    """com.google.common.io.Files"""
 
    @staticmethod
    def _wrap(java_value: _Files) -> 'Files':
        return Files(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Files):
        """
        Dynamic initializer for Files.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Files__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Files__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def asByteSource(file: 'File') -> 'ByteSource':
        """public static com.google.common.io.ByteSource com.google.common.io.Files.asByteSource(java.io.File)"""
        return ByteSource._wrap(_Files.asByteSource(file))

    @staticmethod
    @overload
    def simplifyPath(pathname: str) -> str:
        """public static java.lang.String com.google.common.io.Files.simplifyPath(java.lang.String)"""
        return str._wrap(_Files.simplifyPath(pathname))

    @staticmethod
    @overload
    def toByteArray(file: 'File') -> List[int]:
        """public static byte[] com.google.common.io.Files.toByteArray(java.io.File) throws java.io.IOException"""
        return List[int]._wrap(_Files.toByteArray(file))

    @staticmethod
    @overload
    def isDirectory() -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.io.File> com.google.common.io.Files.isDirectory()"""
        return base.Predicate._wrap(_Files.isDirectory())

    @staticmethod
    @overload
    def asByteSink(file: 'File', *modes: 'FileWriteMode') -> 'ByteSink':
        """public static com.google.common.io.ByteSink com.google.common.io.Files.asByteSink(java.io.File,com.google.common.io.FileWriteMode...)"""
        return ByteSink._wrap(_Files.asByteSink(file, modes))

    @staticmethod
    @overload
    def write(from: 'CharSequence', to: 'File', charset: 'Charset'):
        """public static void com.google.common.io.Files.write(java.lang.CharSequence,java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        _Files.write(from, to, charset)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createTempDir() -> 'File':
        """public static java.io.File com.google.common.io.Files.createTempDir()"""
        return File._wrap(_Files.createTempDir())

    @staticmethod
    @overload
    def asCharSink(file: 'File', charset: 'Charset', *modes: 'FileWriteMode') -> 'CharSink':
        """public static com.google.common.io.CharSink com.google.common.io.Files.asCharSink(java.io.File,java.nio.charset.Charset,com.google.common.io.FileWriteMode...)"""
        return CharSink._wrap(_Files.asCharSink(file, charset, modes))

    @staticmethod
    @overload
    def map(file: 'File', mode: 'MapMode', size: int) -> 'MappedByteBuffer':
        """public static java.nio.MappedByteBuffer com.google.common.io.Files.map(java.io.File,java.nio.channels.FileChannel$MapMode,long) throws java.io.IOException"""
        return MappedByteBuffer._wrap(_Files.map(file, mode, _long.valueOf(size)))

    @staticmethod
    @overload
    def readLines(file: 'File', charset: 'Charset', callback: 'LineProcessor') -> object:
        """public static <T> T com.google.common.io.Files.readLines(java.io.File,java.nio.charset.Charset,com.google.common.io.LineProcessor<T>) throws java.io.IOException"""
        return object._wrap(_Files.readLines(file, charset, callback))

    @staticmethod
    @overload
    def write(from: bytes, to: 'File'):
        """public static void com.google.common.io.Files.write(byte[],java.io.File) throws java.io.IOException"""
        _Files.write(bytes, to)

    @staticmethod
    @overload
    def readLines(file: 'File', charset: 'Charset') -> 'List':
        """public static java.util.List<java.lang.String> com.google.common.io.Files.readLines(java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        return List._wrap(_Files.readLines(file, charset))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createParentDirs(file: 'File'):
        """public static void com.google.common.io.Files.createParentDirs(java.io.File) throws java.io.IOException"""
        _Files.createParentDirs(file)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def map(file: 'File') -> 'MappedByteBuffer':
        """public static java.nio.MappedByteBuffer com.google.common.io.Files.map(java.io.File) throws java.io.IOException"""
        return MappedByteBuffer._wrap(_Files.map(file))

    @staticmethod
    @overload
    def touch(file: 'File'):
        """public static void com.google.common.io.Files.touch(java.io.File) throws java.io.IOException"""
        _Files.touch(file)

    @staticmethod
    @overload
    def copy(from: 'File', charset: 'Charset', to: 'Appendable'):
        """public static void com.google.common.io.Files.copy(java.io.File,java.nio.charset.Charset,java.lang.Appendable) throws java.io.IOException"""
        _Files.copy(from, charset, to)

    @staticmethod
    @overload
    def getFileExtension(fullName: str) -> str:
        """public static java.lang.String com.google.common.io.Files.getFileExtension(java.lang.String)"""
        return str._wrap(_Files.getFileExtension(fullName))

    @staticmethod
    @overload
    def newWriter(file: 'File', charset: 'Charset') -> 'BufferedWriter':
        """public static java.io.BufferedWriter com.google.common.io.Files.newWriter(java.io.File,java.nio.charset.Charset) throws java.io.FileNotFoundException"""
        return BufferedWriter._wrap(_Files.newWriter(file, charset))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def copy(from: 'File', to: 'OutputStream'):
        """public static void com.google.common.io.Files.copy(java.io.File,java.io.OutputStream) throws java.io.IOException"""
        _Files.copy(from, to)

    @staticmethod
    @overload
    def isFile() -> 'base.Predicate':
        """public static com.google.common.base.Predicate<java.io.File> com.google.common.io.Files.isFile()"""
        return base.Predicate._wrap(_Files.isFile())

    @staticmethod
    @overload
    def copy(from: 'File', to: 'File'):
        """public static void com.google.common.io.Files.copy(java.io.File,java.io.File) throws java.io.IOException"""
        _Files.copy(from, to)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def toString(file: 'File', charset: 'Charset') -> str:
        """public static java.lang.String com.google.common.io.Files.toString(java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        return str._wrap(_Files.toString(file, charset))

    @staticmethod
    @overload
    def move(from: 'File', to: 'File'):
        """public static void com.google.common.io.Files.move(java.io.File,java.io.File) throws java.io.IOException"""
        _Files.move(from, to)

    @staticmethod
    @overload
    def append(from: 'CharSequence', to: 'File', charset: 'Charset'):
        """public static void com.google.common.io.Files.append(java.lang.CharSequence,java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        _Files.append(from, to, charset)

    @staticmethod
    @overload
    def newReader(file: 'File', charset: 'Charset') -> 'BufferedReader':
        """public static java.io.BufferedReader com.google.common.io.Files.newReader(java.io.File,java.nio.charset.Charset) throws java.io.FileNotFoundException"""
        return BufferedReader._wrap(_Files.newReader(file, charset))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def equal(file1: 'File', file2: 'File') -> bool:
        """public static boolean com.google.common.io.Files.equal(java.io.File,java.io.File) throws java.io.IOException"""
        return bool._wrap(_Files.equal(file1, file2))

    @staticmethod
    @overload
    def hash(file: 'File', hashFunction: 'HashFunction') -> 'hash.HashCode':
        """public static com.google.common.hash.HashCode com.google.common.io.Files.hash(java.io.File,com.google.common.hash.HashFunction) throws java.io.IOException"""
        return hash.HashCode._wrap(_Files.hash(file, hashFunction))

    @staticmethod
    @overload
    def readFirstLine(file: 'File', charset: 'Charset') -> str:
        """public static java.lang.String com.google.common.io.Files.readFirstLine(java.io.File,java.nio.charset.Charset) throws java.io.IOException"""
        return str._wrap(_Files.readFirstLine(file, charset))

    @staticmethod
    @overload
    def readBytes(file: 'File', processor: 'ByteProcessor') -> object:
        """public static <T> T com.google.common.io.Files.readBytes(java.io.File,com.google.common.io.ByteProcessor<T>) throws java.io.IOException"""
        return object._wrap(_Files.readBytes(file, processor))

    @staticmethod
    @overload
    def fileTraverser() -> 'graph.Traverser':
        """public static com.google.common.graph.Traverser<java.io.File> com.google.common.io.Files.fileTraverser()"""
        return graph.Traverser._wrap(_Files.fileTraverser())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def map(file: 'File', mode: 'MapMode') -> 'MappedByteBuffer':
        """public static java.nio.MappedByteBuffer com.google.common.io.Files.map(java.io.File,java.nio.channels.FileChannel$MapMode) throws java.io.IOException"""
        return MappedByteBuffer._wrap(_Files.map(file, mode))

    @staticmethod
    @overload
    def asCharSource(file: 'File', charset: 'Charset') -> 'CharSource':
        """public static com.google.common.io.CharSource com.google.common.io.Files.asCharSource(java.io.File,java.nio.charset.Charset)"""
        return CharSource._wrap(_Files.asCharSource(file, charset))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getNameWithoutExtension(file: str) -> str:
        """public static java.lang.String com.google.common.io.Files.getNameWithoutExtension(java.lang.String)"""
        return str._wrap(_Files.getNameWithoutExtension(file))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.io.ByteStreams
from builtins import str
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.ByteArrayOutputStream as ByteArrayOutputStream
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import com.google.common.io.ByteArrayDataOutput as _ByteArrayDataOutput
_ByteArrayDataOutput = _ByteArrayDataOutput
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.io.ByteArrayInputStream as ByteArrayInputStream
import com.google.common.io.ByteArrayDataInput as _ByteArrayDataInput
_ByteArrayDataInput = _ByteArrayDataInput
import java.io.InputStream as InputStream
import java.nio.channels.WritableByteChannel as WritableByteChannel
import com.google.common.io.ByteStreams as _ByteStreams
_ByteStreams = _ByteStreams
import java.nio.channels.ReadableByteChannel as ReadableByteChannel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ByteStreams():
    """com.google.common.io.ByteStreams"""
 
    @staticmethod
    def _wrap(java_value: _ByteStreams) -> 'ByteStreams':
        return ByteStreams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteStreams):
        """
        Dynamic initializer for ByteStreams.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteStreams__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteStreams__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def newDataOutput(byteArrayOutputStream: 'ByteArrayOutputStream') -> 'ByteArrayDataOutput':
        """public static com.google.common.io.ByteArrayDataOutput com.google.common.io.ByteStreams.newDataOutput(java.io.ByteArrayOutputStream)"""
        return ByteArrayDataOutput._wrap(_ByteStreams.newDataOutput(byteArrayOutputStream))

    @staticmethod
    @overload
    def toByteArray(in: 'InputStream') -> List[int]:
        """public static byte[] com.google.common.io.ByteStreams.toByteArray(java.io.InputStream) throws java.io.IOException"""
        return List[int]._wrap(_ByteStreams.toByteArray(in))

    @staticmethod
    @overload
    def newDataInput(byteArrayInputStream: 'ByteArrayInputStream') -> 'ByteArrayDataInput':
        """public static com.google.common.io.ByteArrayDataInput com.google.common.io.ByteStreams.newDataInput(java.io.ByteArrayInputStream)"""
        return ByteArrayDataInput._wrap(_ByteStreams.newDataInput(byteArrayInputStream))

    @staticmethod
    @overload
    def newDataOutput() -> 'ByteArrayDataOutput':
        """public static com.google.common.io.ByteArrayDataOutput com.google.common.io.ByteStreams.newDataOutput()"""
        return ByteArrayDataOutput._wrap(_ByteStreams.newDataOutput())

    @staticmethod
    @overload
    def copy(from: 'InputStream', to: 'OutputStream') -> int:
        """public static long com.google.common.io.ByteStreams.copy(java.io.InputStream,java.io.OutputStream) throws java.io.IOException"""
        return int._wrap(_ByteStreams.copy(from, to))

    @staticmethod
    @overload
    def skipFully(in: 'InputStream', n: int):
        """public static void com.google.common.io.ByteStreams.skipFully(java.io.InputStream,long) throws java.io.IOException"""
        _ByteStreams.skipFully(in, _long.valueOf(n))

    @staticmethod
    @overload
    def exhaust(in: 'InputStream') -> int:
        """public static long com.google.common.io.ByteStreams.exhaust(java.io.InputStream) throws java.io.IOException"""
        return int._wrap(_ByteStreams.exhaust(in))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def newDataOutput(size: int) -> 'ByteArrayDataOutput':
        """public static com.google.common.io.ByteArrayDataOutput com.google.common.io.ByteStreams.newDataOutput(int)"""
        return ByteArrayDataOutput._wrap(_ByteStreams.newDataOutput(_int.valueOf(size)))

    @staticmethod
    @overload
    def newDataInput(bytes: bytes) -> 'ByteArrayDataInput':
        """public static com.google.common.io.ByteArrayDataInput com.google.common.io.ByteStreams.newDataInput(byte[])"""
        return ByteArrayDataInput._wrap(_ByteStreams.newDataInput(bytes))

    @staticmethod
    @overload
    def limit(in: 'InputStream', limit: int) -> 'InputStream':
        """public static java.io.InputStream com.google.common.io.ByteStreams.limit(java.io.InputStream,long)"""
        return InputStream._wrap(_ByteStreams.limit(in, _long.valueOf(limit)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def readFully(in: 'InputStream', b: bytes, off: int, len: int):
        """public static void com.google.common.io.ByteStreams.readFully(java.io.InputStream,byte[],int,int) throws java.io.IOException"""
        _ByteStreams.readFully(in, bytes, _int.valueOf(off), _int.valueOf(len))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def copy(from: 'ReadableByteChannel', to: 'WritableByteChannel') -> int:
        """public static long com.google.common.io.ByteStreams.copy(java.nio.channels.ReadableByteChannel,java.nio.channels.WritableByteChannel) throws java.io.IOException"""
        return int._wrap(_ByteStreams.copy(from, to))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream com.google.common.io.ByteStreams.nullOutputStream()"""
        return OutputStream._wrap(_ByteStreams.nullOutputStream())

    @staticmethod
    @overload
    def newDataInput(bytes: bytes, start: int) -> 'ByteArrayDataInput':
        """public static com.google.common.io.ByteArrayDataInput com.google.common.io.ByteStreams.newDataInput(byte[],int)"""
        return ByteArrayDataInput._wrap(_ByteStreams.newDataInput(bytes, _int.valueOf(start)))

    @staticmethod
    @overload
    def readBytes(input: 'InputStream', processor: 'ByteProcessor') -> object:
        """public static <T> T com.google.common.io.ByteStreams.readBytes(java.io.InputStream,com.google.common.io.ByteProcessor<T>) throws java.io.IOException"""
        return object._wrap(_ByteStreams.readBytes(input, processor))

    @staticmethod
    @overload
    def readFully(in: 'InputStream', b: bytes):
        """public static void com.google.common.io.ByteStreams.readFully(java.io.InputStream,byte[]) throws java.io.IOException"""
        _ByteStreams.readFully(in, bytes)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def read(in: 'InputStream', b: bytes, off: int, len: int) -> int:
        """public static int com.google.common.io.ByteStreams.read(java.io.InputStream,byte[],int,int) throws java.io.IOException"""
        return int._wrap(_ByteStreams.read(in, bytes, _int.valueOf(off), _int.valueOf(len)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())