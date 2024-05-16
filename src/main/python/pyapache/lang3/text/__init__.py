from __future__ import annotations
from overload import overload


 
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.nio.CharBuffer as CharBuffer
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
import java.lang.Double as __double
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Readable as Readable
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
from builtins import object
import org.apache.commons.lang3.text.StrBuilder as __StrBuilder
__StrBuilder = __StrBuilder
import java.lang.Appendable as Appendable
import java.util.Iterator as Iterator
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import org.apache.commons.lang3.text.StrTokenizer as __StrTokenizer
__StrTokenizer = __StrTokenizer
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import int
 
class StrBuilder(__CharSequence, CharSequence, __Appendable, Appendable, __Serializable, Serializable, lang3.__Builder, builder.Builder):
    """org.apache.commons.lang3.text.StrBuilder"""
 
    @staticmethod
    def __wrap(java_value: __StrBuilder) -> 'StrBuilder':
        return StrBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StrBuilder):
        """
        Dynamic initializer for StrBuilder.
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
    def append(self, arg0: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char[])"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def appendln(self, arg0: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.Object)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendln(self, arg0: str, *arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String,java.lang.Object...)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__int.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: 'char', arg2: int, arg3: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char[],int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(char,int)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(__char.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def appendAll(self, *arg0: object) -> 'StrBuilder':
        """public <T> org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(T...)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendAll(arg0))

    @overload
    def deleteCharAt(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteCharAt(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteCharAt(__int.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char[])"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendNewLine(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendNewLine()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).appendNewLine())

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,long)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def getChars(self, arg0: int, arg1: int, arg2: 'char', arg3: int):
        """public void org.apache.commons.lang3.text.StrBuilder.getChars(int,int,char[],int)"""
        super(__StrBuilder, self).getChars(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def appendln(self, arg0: 'char', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char[],int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.size()"""
        return int.__wrap(super(StrBuilder, self).size())

    @overload
    def substring(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.substring(int)"""
        return str.__wrap(super(__StrBuilder, self).substring(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equals(java.lang.Object)"""
        return bool.__wrap(super(__StrBuilder, self).equals(arg0))

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(char,int)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(__char.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equals(org.apache.commons.lang3.text.StrBuilder)"""
        return bool.__wrap(super(__StrBuilder, self).equals(arg0))

    @overload
    def appendFixedWidthPadLeft(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadLeft(int,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadLeft(__int.valueOf(arg0), __int.valueOf(arg1), __char.valueOf(arg2)))

    @overload
    def appendSeparator(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(arg0, arg1))

    @overload
    def append(self, arg0: 'char', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char[],int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def append(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def appendln(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__char.valueOf(arg0)))

    @overload
    def toStringBuilder(self) -> 'StringBuilder':
        """public java.lang.StringBuilder org.apache.commons.lang3.text.StrBuilder.toStringBuilder()"""
        return 'StringBuilder'.__wrap(super(StrBuilder, self).toStringBuilder())

    @overload
    def setNullText(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setNullText(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setNullText(arg0))

    @overload
    def appendln(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(long)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__long.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,float)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def asReader(self) -> 'Reader':
        """public java.io.Reader org.apache.commons.lang3.text.StrBuilder.asReader()"""
        return 'Reader'.__wrap(super(StrBuilder, self).asReader())

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'.__wrap(super(CharSequence, self).codePoints())

    @overload
    def readFrom(self, arg0: 'Readable') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.readFrom(java.lang.Readable) throws java.io.IOException"""
        return int.__wrap(super(__StrBuilder, self).readFrom(arg0))

    @overload
    def appendFixedWidthPadRight(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadRight(int,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadRight(__int.valueOf(arg0), __int.valueOf(arg1), __char.valueOf(arg2)))

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'.__wrap(super(CharSequence, self).chars())

    @overload
    def endsWith(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.endsWith(java.lang.String)"""
        return bool.__wrap(super(__StrBuilder, self).endsWith(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def appendSeparator(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(arg0))

    @overload
    def asTokenizer(self) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrBuilder.asTokenizer()"""
        return 'StrTokenizer'.__wrap(super(StrBuilder, self).asTokenizer())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.StrBuilder()"""
        val = __StrBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def rightString(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.rightString(int)"""
        return str.__wrap(super(__StrBuilder, self).rightString(__int.valueOf(arg0)))

    @overload
    def appendWithSeparators(self, arg0: 'Iterable', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.lang.Iterable<?>,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendWithSeparators(arg0, arg1))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(java.lang.String)"""
        return bool.__wrap(super(__StrBuilder, self).contains(arg0))

    @overload
    def append(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def replace(self, arg0: 'StrMatcher', arg1: str, arg2: int, arg3: int, arg4: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replace(org.apache.commons.lang3.text.StrMatcher,java.lang.String,int,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replace(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def leftString(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.leftString(int)"""
        return str.__wrap(super(__StrBuilder, self).leftString(__int.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def minimizeCapacity(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.minimizeCapacity()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).minimizeCapacity())

    @overload
    def getChars(self, arg0: 'char') -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.getChars(char[])"""
        return List[str].__wrap(super(__StrBuilder, self).getChars(arg0))

    @overload
    def replace(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replace(int,int,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replace(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def appendNull(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendNull()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).appendNull())

    @overload
    def append(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(float)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__float.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuffer,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def insert(self, arg0: int, arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,java.lang.Object)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1))

    @overload
    def append(self, arg0: str, *arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String,java.lang.Object...)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, arg1))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(char)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(__char.valueOf(arg0)))

    @overload
    def replaceFirst(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(java.lang.String,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceFirst(arg0, arg1))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(java.lang.String)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0))

    @overload
    def append(self, arg0: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.Object)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def substring(self, arg0: int, arg1: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.substring(int,int)"""
        return str.__wrap(super(__StrBuilder, self).substring(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def deleteFirst(self, arg0: 'StrMatcher') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteFirst(arg0))

    @overload
    def append(self, arg0: 'StringBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def clear(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.clear()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).clear())

    @overload
    def getNullText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.getNullText()"""
        return str.__wrap(super(StrBuilder, self).getNullText())

    @overload
    def appendln(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def appendFixedWidthPadRight(self, arg0: object, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadRight(java.lang.Object,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadRight(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def append(self, arg0: 'CharBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.nio.CharBuffer,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def deleteFirst(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteFirst(__char.valueOf(arg0)))

    @overload
    def append(self, arg0: 'StringBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuffer)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.hashCode()"""
        return int.__wrap(super(StrBuilder, self).hashCode())

    @overload
    def replaceAll(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(char,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceAll(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def append(self, arg0: 'CharBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.nio.CharBuffer)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def lastIndexOf(self, arg0: 'StrMatcher', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(org.apache.commons.lang3.text.StrMatcher,int)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.text.StrBuilder(java.lang.String)"""
        val = __StrBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(long)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__long.valueOf(arg0)))

    @overload
    def capacity(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.capacity()"""
        return int.__wrap(super(StrBuilder, self).capacity())

    @overload
    def appendTo(self, arg0: 'Appendable'):
        """public void org.apache.commons.lang3.text.StrBuilder.appendTo(java.lang.Appendable) throws java.io.IOException"""
        super(__StrBuilder, self).appendTo(arg0)

    @overload
    def appendFixedWidthPadLeft(self, arg0: object, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadLeft(java.lang.Object,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadLeft(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.text.StrBuilder(int)"""
        val = __StrBuilder(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def appendWithSeparators(self, arg0: 'Iterator', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.util.Iterator<?>,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendWithSeparators(arg0, arg1))

    @overload
    def deleteFirst(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteFirst(arg0))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(java.lang.String)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0))

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(java.lang.String,int)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0, __int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__int.valueOf(arg0)))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(char)"""
        return bool.__wrap(super(__StrBuilder, self).contains(__char.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(double)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__double.valueOf(arg0)))

    @overload
    def ensureCapacity(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.ensureCapacity(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def appendSeparator(self, arg0: str, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(__char.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def charAt(self, arg0: int) -> str:
        """public char org.apache.commons.lang3.text.StrBuilder.charAt(int)"""
        return str.__wrap(super(__StrBuilder, self).charAt(__int.valueOf(arg0)))

    @overload
    def appendSeparator(self, arg0: str, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(arg0, __int.valueOf(arg1)))

    @overload
    def isNotEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.isNotEmpty()"""
        return bool.__wrap(super(StrBuilder, self).isNotEmpty())

    @overload
    def deleteAll(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteAll(arg0))

    @overload
    def appendln(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(float)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__float.valueOf(arg0)))

    @override
    @overload
    def length(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.length()"""
        return int.__wrap(super(StrBuilder, self).length())

    @overload
    def startsWith(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.startsWith(java.lang.String)"""
        return bool.__wrap(super(__StrBuilder, self).startsWith(arg0))

    @overload
    def appendPadding(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendPadding(int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendPadding(__int.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def deleteAll(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteAll(__char.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'StrBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(org.apache.commons.lang3.text.StrBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendln(self, arg0: 'StringBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def append(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replaceAll(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(java.lang.String,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceAll(arg0, arg1))

    @overload
    def contains(self, arg0: 'StrMatcher') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(org.apache.commons.lang3.text.StrMatcher)"""
        return bool.__wrap(super(__StrBuilder, self).contains(arg0))

    @overload
    def appendWithSeparators(self, arg0: 'Object', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.lang.Object[],java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendWithSeparators(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.isEmpty()"""
        return bool.__wrap(super(StrBuilder, self).isEmpty())

    @overload
    def append(self, arg0: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(boolean)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__boolean.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1))

    @overload
    def replaceFirst(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(char,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceFirst(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def asWriter(self) -> 'Writer':
        """public java.io.Writer org.apache.commons.lang3.text.StrBuilder.asWriter()"""
        return 'Writer'.__wrap(super(StrBuilder, self).asWriter())

    @overload
    def appendln(self, arg0: 'StringBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuffer)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendSeparator(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def append(self, arg0: 'StrBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(org.apache.commons.lang3.text.StrBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,double)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def append(self, arg0: 'CharSequence', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.CharSequence,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(java.lang.String,int)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0, __int.valueOf(arg1)))

    @overload
    def appendAll(self, arg0: 'Iterable') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(java.lang.Iterable<?>)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendAll(arg0))

    @overload
    def appendSeparator(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(__char.valueOf(arg0)))

    @overload
    def trim(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.trim()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).trim())

    @overload
    def setLength(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setLength(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setLength(__int.valueOf(arg0)))

    @overload
    def appendAll(self, arg0: 'Iterator') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(java.util.Iterator<?>)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.toString()"""
        return str.__wrap(super(StrBuilder, self).toString())

    @overload
    def toStringBuffer(self) -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.text.StrBuilder.toStringBuffer()"""
        return 'StringBuffer'.__wrap(super(StrBuilder, self).toStringBuffer())

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def midString(self, arg0: int, arg1: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.midString(int,int)"""
        return str.__wrap(super(__StrBuilder, self).midString(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.StrBuilder()"""
        val = __StrBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def appendln(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replaceFirst(self, arg0: 'StrMatcher', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(org.apache.commons.lang3.text.StrMatcher,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceFirst(arg0, arg1))

    @overload
    def equalsIgnoreCase(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equalsIgnoreCase(org.apache.commons.lang3.text.StrBuilder)"""
        return bool.__wrap(super(__StrBuilder, self).equalsIgnoreCase(arg0))

    @overload
    def setNewLineText(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setNewLineText(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setNewLineText(arg0))

    @overload
    def appendln(self, arg0: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(boolean)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__boolean.valueOf(arg0)))

    @overload
    def subSequence(self, arg0: int, arg1: int) -> 'CharSequence':
        """public java.lang.CharSequence org.apache.commons.lang3.text.StrBuilder.subSequence(int,int)"""
        return 'CharSequence'.__wrap(super(__StrBuilder, self).subSequence(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def delete(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.delete(int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).delete(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def toCharArray(self, arg0: int, arg1: int) -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.toCharArray(int,int)"""
        return List[str].__wrap(super(__StrBuilder, self).toCharArray(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: str, arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replaceAll(self, arg0: 'StrMatcher', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(org.apache.commons.lang3.text.StrMatcher,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceAll(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def append(self, arg0: 'CharSequence') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.CharSequence)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def deleteAll(self, arg0: 'StrMatcher') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteAll(arg0))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuffer,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def indexOf(self, arg0: 'StrMatcher') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(org.apache.commons.lang3.text.StrMatcher)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0))

    @overload
    def getNewLineText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.getNewLineText()"""
        return str.__wrap(super(StrBuilder, self).getNewLineText())

    @override
    @overload
    def build(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.build()"""
        return str.__wrap(super(StrBuilder, self).build())

    @overload
    def appendln(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(double)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__double.valueOf(arg0)))

    @overload
    def toCharArray(self) -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.toCharArray()"""
        return List[str].__wrap(super(StrBuilder, self).toCharArray())

    @overload
    def insert(self, arg0: int, arg1: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char[])"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__char.valueOf(arg0)))

    @overload
    def setCharAt(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setCharAt(int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setCharAt(__int.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def insert(self, arg0: int, arg1: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,boolean)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(char)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(__char.valueOf(arg0)))

    @overload
    def reverse(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.reverse()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).reverse())

    @overload
    def lastIndexOf(self, arg0: 'StrMatcher') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(org.apache.commons.lang3.text.StrMatcher)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0))

    @overload
    def indexOf(self, arg0: 'StrMatcher', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(org.apache.commons.lang3.text.StrMatcher,int)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0, __int.valueOf(arg1)))

 
 
 
# CLASS: org.apache.commons.lang3.text.StrBuilder
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.nio.CharBuffer as CharBuffer
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
import java.lang.Double as __double
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Readable as Readable
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
from builtins import object
import org.apache.commons.lang3.text.StrBuilder as __StrBuilder
__StrBuilder = __StrBuilder
import java.lang.Appendable as Appendable
import java.util.Iterator as Iterator
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import org.apache.commons.lang3.text.StrTokenizer as __StrTokenizer
__StrTokenizer = __StrTokenizer
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import int
 
class StrBuilder(__CharSequence, CharSequence, __Appendable, Appendable, __Serializable, Serializable, lang3.__Builder, builder.Builder):
    """org.apache.commons.lang3.text.StrBuilder"""
 
    @staticmethod
    def __wrap(java_value: __StrBuilder) -> 'StrBuilder':
        return StrBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StrBuilder):
        """
        Dynamic initializer for StrBuilder.
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
    def append(self, arg0: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char[])"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def appendln(self, arg0: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.Object)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendln(self, arg0: str, *arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String,java.lang.Object...)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__int.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: 'char', arg2: int, arg3: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char[],int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(char,int)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(__char.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def appendAll(self, *arg0: object) -> 'StrBuilder':
        """public <T> org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(T...)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendAll(arg0))

    @overload
    def deleteCharAt(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteCharAt(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteCharAt(__int.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char[])"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendNewLine(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendNewLine()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).appendNewLine())

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,long)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def getChars(self, arg0: int, arg1: int, arg2: 'char', arg3: int):
        """public void org.apache.commons.lang3.text.StrBuilder.getChars(int,int,char[],int)"""
        super(__StrBuilder, self).getChars(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def appendln(self, arg0: 'char', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char[],int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.size()"""
        return int.__wrap(super(StrBuilder, self).size())

    @overload
    def substring(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.substring(int)"""
        return str.__wrap(super(__StrBuilder, self).substring(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equals(java.lang.Object)"""
        return bool.__wrap(super(__StrBuilder, self).equals(arg0))

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(char,int)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(__char.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equals(org.apache.commons.lang3.text.StrBuilder)"""
        return bool.__wrap(super(__StrBuilder, self).equals(arg0))

    @overload
    def appendFixedWidthPadLeft(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadLeft(int,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadLeft(__int.valueOf(arg0), __int.valueOf(arg1), __char.valueOf(arg2)))

    @overload
    def appendSeparator(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(arg0, arg1))

    @overload
    def append(self, arg0: 'char', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char[],int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def append(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def appendln(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__char.valueOf(arg0)))

    @overload
    def toStringBuilder(self) -> 'StringBuilder':
        """public java.lang.StringBuilder org.apache.commons.lang3.text.StrBuilder.toStringBuilder()"""
        return 'StringBuilder'.__wrap(super(StrBuilder, self).toStringBuilder())

    @overload
    def setNullText(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setNullText(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setNullText(arg0))

    @overload
    def appendln(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(long)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__long.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,float)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def asReader(self) -> 'Reader':
        """public java.io.Reader org.apache.commons.lang3.text.StrBuilder.asReader()"""
        return 'Reader'.__wrap(super(StrBuilder, self).asReader())

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'.__wrap(super(CharSequence, self).codePoints())

    @overload
    def readFrom(self, arg0: 'Readable') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.readFrom(java.lang.Readable) throws java.io.IOException"""
        return int.__wrap(super(__StrBuilder, self).readFrom(arg0))

    @overload
    def appendFixedWidthPadRight(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadRight(int,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadRight(__int.valueOf(arg0), __int.valueOf(arg1), __char.valueOf(arg2)))

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'.__wrap(super(CharSequence, self).chars())

    @overload
    def endsWith(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.endsWith(java.lang.String)"""
        return bool.__wrap(super(__StrBuilder, self).endsWith(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def appendSeparator(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(arg0))

    @overload
    def asTokenizer(self) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrBuilder.asTokenizer()"""
        return 'StrTokenizer'.__wrap(super(StrBuilder, self).asTokenizer())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.StrBuilder()"""
        val = __StrBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def rightString(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.rightString(int)"""
        return str.__wrap(super(__StrBuilder, self).rightString(__int.valueOf(arg0)))

    @overload
    def appendWithSeparators(self, arg0: 'Iterable', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.lang.Iterable<?>,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendWithSeparators(arg0, arg1))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(java.lang.String)"""
        return bool.__wrap(super(__StrBuilder, self).contains(arg0))

    @overload
    def append(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def replace(self, arg0: 'StrMatcher', arg1: str, arg2: int, arg3: int, arg4: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replace(org.apache.commons.lang3.text.StrMatcher,java.lang.String,int,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replace(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def leftString(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.leftString(int)"""
        return str.__wrap(super(__StrBuilder, self).leftString(__int.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def minimizeCapacity(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.minimizeCapacity()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).minimizeCapacity())

    @overload
    def getChars(self, arg0: 'char') -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.getChars(char[])"""
        return List[str].__wrap(super(__StrBuilder, self).getChars(arg0))

    @overload
    def replace(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replace(int,int,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replace(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def appendNull(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendNull()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).appendNull())

    @overload
    def append(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(float)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__float.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuffer,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def insert(self, arg0: int, arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,java.lang.Object)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1))

    @overload
    def append(self, arg0: str, *arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String,java.lang.Object...)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, arg1))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(char)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(__char.valueOf(arg0)))

    @overload
    def replaceFirst(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(java.lang.String,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceFirst(arg0, arg1))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(java.lang.String)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0))

    @overload
    def append(self, arg0: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.Object)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def substring(self, arg0: int, arg1: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.substring(int,int)"""
        return str.__wrap(super(__StrBuilder, self).substring(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def deleteFirst(self, arg0: 'StrMatcher') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteFirst(arg0))

    @overload
    def append(self, arg0: 'StringBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def clear(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.clear()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).clear())

    @overload
    def getNullText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.getNullText()"""
        return str.__wrap(super(StrBuilder, self).getNullText())

    @overload
    def appendln(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def appendFixedWidthPadRight(self, arg0: object, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadRight(java.lang.Object,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadRight(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def append(self, arg0: 'CharBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.nio.CharBuffer,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def deleteFirst(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteFirst(__char.valueOf(arg0)))

    @overload
    def append(self, arg0: 'StringBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuffer)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.hashCode()"""
        return int.__wrap(super(StrBuilder, self).hashCode())

    @overload
    def replaceAll(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(char,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceAll(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def append(self, arg0: 'CharBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.nio.CharBuffer)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def lastIndexOf(self, arg0: 'StrMatcher', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(org.apache.commons.lang3.text.StrMatcher,int)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.text.StrBuilder(java.lang.String)"""
        val = __StrBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(long)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__long.valueOf(arg0)))

    @overload
    def capacity(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.capacity()"""
        return int.__wrap(super(StrBuilder, self).capacity())

    @overload
    def appendTo(self, arg0: 'Appendable'):
        """public void org.apache.commons.lang3.text.StrBuilder.appendTo(java.lang.Appendable) throws java.io.IOException"""
        super(__StrBuilder, self).appendTo(arg0)

    @overload
    def appendFixedWidthPadLeft(self, arg0: object, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadLeft(java.lang.Object,int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendFixedWidthPadLeft(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.text.StrBuilder(int)"""
        val = __StrBuilder(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def appendWithSeparators(self, arg0: 'Iterator', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.util.Iterator<?>,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendWithSeparators(arg0, arg1))

    @overload
    def deleteFirst(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteFirst(arg0))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(java.lang.String)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0))

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(java.lang.String,int)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0, __int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__int.valueOf(arg0)))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(char)"""
        return bool.__wrap(super(__StrBuilder, self).contains(__char.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(double)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__double.valueOf(arg0)))

    @overload
    def ensureCapacity(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.ensureCapacity(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def appendSeparator(self, arg0: str, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(__char.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def charAt(self, arg0: int) -> str:
        """public char org.apache.commons.lang3.text.StrBuilder.charAt(int)"""
        return str.__wrap(super(__StrBuilder, self).charAt(__int.valueOf(arg0)))

    @overload
    def appendSeparator(self, arg0: str, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(arg0, __int.valueOf(arg1)))

    @overload
    def isNotEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.isNotEmpty()"""
        return bool.__wrap(super(StrBuilder, self).isNotEmpty())

    @overload
    def deleteAll(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteAll(arg0))

    @overload
    def appendln(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(float)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__float.valueOf(arg0)))

    @override
    @overload
    def length(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.length()"""
        return int.__wrap(super(StrBuilder, self).length())

    @overload
    def startsWith(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.startsWith(java.lang.String)"""
        return bool.__wrap(super(__StrBuilder, self).startsWith(arg0))

    @overload
    def appendPadding(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendPadding(int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendPadding(__int.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def deleteAll(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteAll(__char.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'StrBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(org.apache.commons.lang3.text.StrBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendln(self, arg0: 'StringBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def append(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replaceAll(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(java.lang.String,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceAll(arg0, arg1))

    @overload
    def contains(self, arg0: 'StrMatcher') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(org.apache.commons.lang3.text.StrMatcher)"""
        return bool.__wrap(super(__StrBuilder, self).contains(arg0))

    @overload
    def appendWithSeparators(self, arg0: 'Object', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.lang.Object[],java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendWithSeparators(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.isEmpty()"""
        return bool.__wrap(super(StrBuilder, self).isEmpty())

    @overload
    def append(self, arg0: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(boolean)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__boolean.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1))

    @overload
    def replaceFirst(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(char,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceFirst(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def asWriter(self) -> 'Writer':
        """public java.io.Writer org.apache.commons.lang3.text.StrBuilder.asWriter()"""
        return 'Writer'.__wrap(super(StrBuilder, self).asWriter())

    @overload
    def appendln(self, arg0: 'StringBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuffer)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def appendSeparator(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def append(self, arg0: 'StrBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(org.apache.commons.lang3.text.StrBuilder)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,double)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def append(self, arg0: 'CharSequence', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.CharSequence,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(java.lang.String,int)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0, __int.valueOf(arg1)))

    @overload
    def appendAll(self, arg0: 'Iterable') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(java.lang.Iterable<?>)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendAll(arg0))

    @overload
    def appendSeparator(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendSeparator(__char.valueOf(arg0)))

    @overload
    def trim(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.trim()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).trim())

    @overload
    def setLength(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setLength(int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setLength(__int.valueOf(arg0)))

    @overload
    def appendAll(self, arg0: 'Iterator') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(java.util.Iterator<?>)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.toString()"""
        return str.__wrap(super(StrBuilder, self).toString())

    @overload
    def toStringBuffer(self) -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.text.StrBuilder.toStringBuffer()"""
        return 'StringBuffer'.__wrap(super(StrBuilder, self).toStringBuffer())

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def midString(self, arg0: int, arg1: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.midString(int,int)"""
        return str.__wrap(super(__StrBuilder, self).midString(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.StrBuilder()"""
        val = __StrBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def appendln(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replaceFirst(self, arg0: 'StrMatcher', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(org.apache.commons.lang3.text.StrMatcher,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceFirst(arg0, arg1))

    @overload
    def equalsIgnoreCase(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equalsIgnoreCase(org.apache.commons.lang3.text.StrBuilder)"""
        return bool.__wrap(super(__StrBuilder, self).equalsIgnoreCase(arg0))

    @overload
    def setNewLineText(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setNewLineText(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setNewLineText(arg0))

    @overload
    def appendln(self, arg0: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(boolean)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__boolean.valueOf(arg0)))

    @overload
    def subSequence(self, arg0: int, arg1: int) -> 'CharSequence':
        """public java.lang.CharSequence org.apache.commons.lang3.text.StrBuilder.subSequence(int,int)"""
        return 'CharSequence'.__wrap(super(__StrBuilder, self).subSequence(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def delete(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.delete(int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).delete(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0))

    @overload
    def toCharArray(self, arg0: int, arg1: int) -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.toCharArray(int,int)"""
        return List[str].__wrap(super(__StrBuilder, self).toCharArray(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: str, arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replaceAll(self, arg0: 'StrMatcher', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(org.apache.commons.lang3.text.StrMatcher,java.lang.String)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).replaceAll(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def append(self, arg0: 'CharSequence') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.CharSequence)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0))

    @overload
    def deleteAll(self, arg0: 'StrMatcher') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).deleteAll(arg0))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuffer,int,int)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def indexOf(self, arg0: 'StrMatcher') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(org.apache.commons.lang3.text.StrMatcher)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0))

    @overload
    def getNewLineText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.getNewLineText()"""
        return str.__wrap(super(StrBuilder, self).getNewLineText())

    @override
    @overload
    def build(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.build()"""
        return str.__wrap(super(StrBuilder, self).build())

    @overload
    def appendln(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(double)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).appendln(__double.valueOf(arg0)))

    @overload
    def toCharArray(self) -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.toCharArray()"""
        return List[str].__wrap(super(StrBuilder, self).toCharArray())

    @overload
    def insert(self, arg0: int, arg1: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char[])"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).append(__char.valueOf(arg0)))

    @overload
    def setCharAt(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setCharAt(int,char)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).setCharAt(__int.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def insert(self, arg0: int, arg1: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,boolean)"""
        return 'StrBuilder'.__wrap(super(__StrBuilder, self).insert(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(char)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(__char.valueOf(arg0)))

    @overload
    def reverse(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.reverse()"""
        return 'StrBuilder'.__wrap(super(StrBuilder, self).reverse())

    @overload
    def lastIndexOf(self, arg0: 'StrMatcher') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(org.apache.commons.lang3.text.StrMatcher)"""
        return int.__wrap(super(__StrBuilder, self).lastIndexOf(arg0))

    @overload
    def indexOf(self, arg0: 'StrMatcher', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(org.apache.commons.lang3.text.StrMatcher,int)"""
        return int.__wrap(super(__StrBuilder, self).indexOf(arg0, __int.valueOf(arg1)))

 
 
 
# CLASS: org.apache.commons.lang3.text.StrBuilder 
 
 
# CLASS: org.apache.commons.lang3.text.FormatFactory
import org.apache.commons.lang3.text.FormatFactory as __FormatFactory
__FormatFactory = __FormatFactory
import java.util.Locale as Locale
from abc import abstractmethod, ABC
 
class FormatFactory(ABC):
    """org.apache.commons.lang3.text.FormatFactory"""
 
    @staticmethod
    def __wrap(java_value: __FormatFactory) -> 'FormatFactory':
        return FormatFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormatFactory):
        """
        Dynamic initializer for FormatFactory.
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
    def getFormat(self, arg0: str, arg1: str, arg2: 'Locale'):
        """public abstract java.text.Format org.apache.commons.lang3.text.FormatFactory.getFormat(java.lang.String,java.lang.String,java.util.Locale)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.text.CompositeFormat
import java.text.FieldPosition as FieldPosition
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.text.CompositeFormat as __CompositeFormat
__CompositeFormat = __CompositeFormat
import java.lang.Object as __object
import java.text.AttributedCharacterIterator as AttributedCharacterIterator
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.text.ParsePosition as ParsePosition
import java.text.Format as __Format
__Format = __Format
from builtins import object
import java.text.AttributedCharacterIterator as __AttributedCharacterIterator
__AttributedCharacterIterator = __AttributedCharacterIterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.text.Format as Format
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CompositeFormat(__Format, Format):
    """org.apache.commons.lang3.text.CompositeFormat"""
 
    @staticmethod
    def __wrap(java_value: __CompositeFormat) -> 'CompositeFormat':
        return CompositeFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CompositeFormat):
        """
        Dynamic initializer for CompositeFormat.
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
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object org.apache.commons.lang3.text.CompositeFormat.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object.__wrap(super(__CompositeFormat, self).parseObject(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Format', arg1: 'Format'):
        """public org.apache.commons.lang3.text.CompositeFormat(java.text.Format,java.text.Format)"""
        val = __CompositeFormat(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def reformat(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.text.CompositeFormat.reformat(java.lang.String) throws java.text.ParseException"""
        return str.__wrap(super(__CompositeFormat, self).reformat(arg0))

    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object java.text.Format.parseObject(java.lang.String) throws java.text.ParseException"""
        return object.__wrap(super(__Format, self).parseObject(arg0))

    @overload
    def formatToCharacterIterator(self, arg0: object) -> 'AttributedCharacterIterator':
        """public java.text.AttributedCharacterIterator java.text.Format.formatToCharacterIterator(java.lang.Object)"""
        return 'AttributedCharacterIterator'.__wrap(super(__Format, self).formatToCharacterIterator(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.text.CompositeFormat.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'.__wrap(super(__CompositeFormat, self).format(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def format(self, arg0: object) -> str:
        """public final java.lang.String java.text.Format.format(java.lang.Object)"""
        return str.__wrap(super(__Format, self).format(arg0))

    @overload
    def getFormatter(self) -> 'Format':
        """public java.text.Format org.apache.commons.lang3.text.CompositeFormat.getFormatter()"""
        return 'Format'.__wrap(super(CompositeFormat, self).getFormatter())

    @overload
    def getParser(self) -> 'Format':
        """public java.text.Format org.apache.commons.lang3.text.CompositeFormat.getParser()"""
        return 'Format'.__wrap(super(CompositeFormat, self).getParser())

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
    def clone(self) -> object:
        """public java.lang.Object java.text.Format.clone()"""
        return object.__wrap(super(Format, self).clone())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.FormattableUtils
import java.util.Formatter as __Formatter
__Formatter = __Formatter
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Formatter as Formatter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.lang3.text.FormattableUtils as __FormattableUtils
__FormattableUtils = __FormattableUtils
import java.util.Formattable as Formattable
from builtins import int
 
class FormattableUtils():
    """org.apache.commons.lang3.text.FormattableUtils"""
 
    @staticmethod
    def __wrap(java_value: __FormattableUtils) -> 'FormattableUtils':
        return FormattableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormattableUtils):
        """
        Dynamic initializer for FormattableUtils.
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
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: str) -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,char)"""
        return Formatter.__wrap(__FormattableUtils.append(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __char.valueOf(arg5)))

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int) -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int)"""
        return Formatter.__wrap(__FormattableUtils.append(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: 'CharSequence') -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,java.lang.CharSequence)"""
        return Formatter.__wrap(__FormattableUtils.append(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: str, arg6: 'CharSequence') -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,char,java.lang.CharSequence)"""
        return Formatter.__wrap(__FormattableUtils.append(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __char.valueOf(arg5), arg6))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.FormattableUtils()"""
        val = __FormattableUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toString(arg0: 'Formattable') -> str:
        """public static java.lang.String org.apache.commons.lang3.text.FormattableUtils.toString(java.util.Formattable)"""
        return str.__wrap(__FormattableUtils.toString(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.text.FormattableUtils()"""
        val = __FormattableUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.StrMatcher
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.text.StrMatcher as __StrMatcher
__StrMatcher = __StrMatcher
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StrMatcher(ABC):
    """org.apache.commons.lang3.text.StrMatcher"""
 
    @staticmethod
    def __wrap(java_value: __StrMatcher) -> 'StrMatcher':
        return StrMatcher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StrMatcher):
        """
        Dynamic initializer for StrMatcher.
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

    @staticmethod
    @overload
    def stringMatcher(arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.stringMatcher(java.lang.String)"""
        return StrMatcher.__wrap(__StrMatcher.stringMatcher(arg0))

    @staticmethod
    @overload
    def doubleQuoteMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.doubleQuoteMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.doubleQuoteMatcher())

    @staticmethod
    @overload
    def tabMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.tabMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.tabMatcher())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isMatch(self, arg0: 'char', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrMatcher.isMatch(char[],int)"""
        return int.__wrap(super(__StrMatcher, self).isMatch(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def commaMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.commaMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.commaMatcher())

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
    def singleQuoteMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.singleQuoteMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.singleQuoteMatcher())

    @staticmethod
    @overload
    def trimMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.trimMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.trimMatcher())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def charSetMatcher(arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.charSetMatcher(java.lang.String)"""
        return StrMatcher.__wrap(__StrMatcher.charSetMatcher(arg0))

    @abstractmethod
    def isMatch(self, arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public abstract int org.apache.commons.lang3.text.StrMatcher.isMatch(char[],int,int,int)"""
        pass

    @staticmethod
    @overload
    def spaceMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.spaceMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.spaceMatcher())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def charSetMatcher(*arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.charSetMatcher(char...)"""
        return StrMatcher.__wrap(__StrMatcher.charSetMatcher(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def splitMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.splitMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.splitMatcher())

    @staticmethod
    @overload
    def quoteMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.quoteMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.quoteMatcher())

    @staticmethod
    @overload
    def noneMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.noneMatcher()"""
        return StrMatcher.__wrap(__StrMatcher.noneMatcher())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def charMatcher(arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.charMatcher(char)"""
        return StrMatcher.__wrap(__StrMatcher.charMatcher(__char.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.text.ExtendedMessageFormat
import java.text.FieldPosition as FieldPosition
import java.util.Locale as Locale
import java.text.AttributedCharacterIterator as AttributedCharacterIterator
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.text.Format as __Format
__Format = __Format
import java.text.ParsePosition as ParsePosition
import java.text.AttributedCharacterIterator as __AttributedCharacterIterator
__AttributedCharacterIterator = __AttributedCharacterIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.text.Format as Format
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.text.MessageFormat as __MessageFormat
__MessageFormat = __MessageFormat
from builtins import object
from typing import List
import org.apache.commons.lang3.text.ExtendedMessageFormat as __ExtendedMessageFormat
__ExtendedMessageFormat = __ExtendedMessageFormat
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
import java.util.Map as Map
from builtins import int
 
class ExtendedMessageFormat(__MessageFormat, MessageFormat):
    """org.apache.commons.lang3.text.ExtendedMessageFormat"""
 
    @staticmethod
    def __wrap(java_value: __ExtendedMessageFormat) -> 'ExtendedMessageFormat':
        return ExtendedMessageFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExtendedMessageFormat):
        """
        Dynamic initializer for ExtendedMessageFormat.
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
    def toPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.ExtendedMessageFormat.toPattern()"""
        return str.__wrap(super(ExtendedMessageFormat, self).toPattern())

    @overload
    def format(self, arg0: 'Object', arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public final java.lang.StringBuffer java.text.MessageFormat.format(java.lang.Object[],java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'.__wrap(super(__MessageFormat, self).format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: str, *arg1: object) -> str:
        """public static java.lang.String java.text.MessageFormat.format(java.lang.String,java.lang.Object...)"""
        return str.__wrap(__MessageFormat.format(arg0, arg1))

    @overload
    def formatToCharacterIterator(self, arg0: object) -> 'AttributedCharacterIterator':
        """public java.text.AttributedCharacterIterator java.text.MessageFormat.formatToCharacterIterator(java.lang.Object)"""
        return 'AttributedCharacterIterator'.__wrap(super(__MessageFormat, self).formatToCharacterIterator(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: 'Map'):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String,java.util.Map<java.lang.String, ? extends org.apache.commons.lang3.text.FormatFactory>)"""
        val = __ExtendedMessageFormat(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public final java.lang.StringBuffer java.text.MessageFormat.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'.__wrap(super(__MessageFormat, self).format(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String)"""
        val = __ExtendedMessageFormat(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition') -> List[object]:
        """public java.lang.Object[] java.text.MessageFormat.parse(java.lang.String,java.text.ParsePosition)"""
        return List[object].__wrap(super(__MessageFormat, self).parse(arg0, arg1))

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.text.MessageFormat.clone()"""
        return object.__wrap(super(MessageFormat, self).clone())

    @overload
    def format(self, arg0: object) -> str:
        """public final java.lang.String java.text.Format.format(java.lang.Object)"""
        return str.__wrap(super(__Format, self).format(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Locale'):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String,java.util.Locale)"""
        val = __ExtendedMessageFormat(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setFormatByArgumentIndex(self, arg0: int, arg1: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormatByArgumentIndex(int,java.text.Format)"""
        super(__ExtendedMessageFormat, self).setFormatByArgumentIndex(__int.valueOf(arg0), arg1)

    @override
    @overload
    def setFormats(self, arg0: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormats(java.text.Format[])"""
        super(__ExtendedMessageFormat, self).setFormats(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Locale', arg2: 'Map'):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String,java.util.Locale,java.util.Map<java.lang.String, ? extends org.apache.commons.lang3.text.FormatFactory>)"""
        val = __ExtendedMessageFormat(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def parse(self, arg0: str) -> List[object]:
        """public java.lang.Object[] java.text.MessageFormat.parse(java.lang.String) throws java.text.ParseException"""
        return List[object].__wrap(super(__MessageFormat, self).parse(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.text.ExtendedMessageFormat.hashCode()"""
        return int.__wrap(super(ExtendedMessageFormat, self).hashCode())

    @override
    @overload
    def applyPattern(self, arg0: str):
        """public final void org.apache.commons.lang3.text.ExtendedMessageFormat.applyPattern(java.lang.String)"""
        super(__ExtendedMessageFormat, self).applyPattern(arg0)

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale java.text.MessageFormat.getLocale()"""
        return 'Locale'.__wrap(super(MessageFormat, self).getLocale())

    @override
    @overload
    def setFormatsByArgumentIndex(self, arg0: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormatsByArgumentIndex(java.text.Format[])"""
        super(__ExtendedMessageFormat, self).setFormatsByArgumentIndex(arg0)

    @override
    @overload
    def getFormats(self) -> List['Format']:
        """public java.text.Format[] java.text.MessageFormat.getFormats()"""
        return List['Format'].__wrap(super(MessageFormat, self).getFormats())

    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object java.text.Format.parseObject(java.lang.String) throws java.text.ParseException"""
        return object.__wrap(super(__Format, self).parseObject(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setLocale(self, arg0: 'Locale'):
        """public void java.text.MessageFormat.setLocale(java.util.Locale)"""
        super(__MessageFormat, self).setLocale(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object java.text.MessageFormat.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object.__wrap(super(__MessageFormat, self).parseObject(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.text.ExtendedMessageFormat.equals(java.lang.Object)"""
        return bool.__wrap(super(__ExtendedMessageFormat, self).equals(arg0))

    @override
    @overload
    def setFormat(self, arg0: int, arg1: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormat(int,java.text.Format)"""
        super(__ExtendedMessageFormat, self).setFormat(__int.valueOf(arg0), arg1)

    @override
    @overload
    def getFormatsByArgumentIndex(self) -> List['Format']:
        """public java.text.Format[] java.text.MessageFormat.getFormatsByArgumentIndex()"""
        return List['Format'].__wrap(super(MessageFormat, self).getFormatsByArgumentIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.text.StrLookup
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.text.StrLookup as __StrLookup
__StrLookup = __StrLookup
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class StrLookup(ABC):
    """org.apache.commons.lang3.text.StrLookup"""
 
    @staticmethod
    def __wrap(java_value: __StrLookup) -> 'StrLookup':
        return StrLookup(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StrLookup):
        """
        Dynamic initializer for StrLookup.
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

    @staticmethod
    @overload
    def mapLookup(arg0: 'Map') -> 'StrLookup':
        """public static <V> org.apache.commons.lang3.text.StrLookup<V> org.apache.commons.lang3.text.StrLookup.mapLookup(java.util.Map<java.lang.String, V>)"""
        return StrLookup.__wrap(__StrLookup.mapLookup(arg0))

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
    def noneLookup() -> 'StrLookup':
        """public static org.apache.commons.lang3.text.StrLookup<?> org.apache.commons.lang3.text.StrLookup.noneLookup()"""
        return StrLookup.__wrap(__StrLookup.noneLookup())

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

    @abstractmethod
    def lookup(self, arg0: str):
        """public abstract java.lang.String org.apache.commons.lang3.text.StrLookup.lookup(java.lang.String)"""
        pass

    @staticmethod
    @overload
    def systemPropertiesLookup() -> 'StrLookup':
        """public static org.apache.commons.lang3.text.StrLookup<java.lang.String> org.apache.commons.lang3.text.StrLookup.systemPropertiesLookup()"""
        return StrLookup.__wrap(__StrLookup.systemPropertiesLookup())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.StrSubstitutor
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import org.apache.commons.lang3.text.StrSubstitutor as __StrSubstitutor
__StrSubstitutor = __StrSubstitutor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import org.apache.commons.lang3.text.StrLookup as __StrLookup
__StrLookup = __StrLookup
import org.apache.commons.lang3.text.StrMatcher as __StrMatcher
__StrMatcher = __StrMatcher
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class StrSubstitutor():
    """org.apache.commons.lang3.text.StrSubstitutor"""
 
    @staticmethod
    def __wrap(java_value: __StrSubstitutor) -> 'StrSubstitutor':
        return StrSubstitutor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StrSubstitutor):
        """
        Dynamic initializer for StrSubstitutor.
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
    def replace(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.String)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0))

    @overload
    def replaceIn(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return bool.__wrap(super(__StrSubstitutor, self).replaceIn(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replaceIn(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(org.apache.commons.lang3.text.StrBuilder)"""
        return bool.__wrap(super(__StrSubstitutor, self).replaceIn(arg0))

    @overload
    def isPreserveEscapes(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.isPreserveEscapes()"""
        return bool.__wrap(super(StrSubstitutor, self).isPreserveEscapes())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Map', arg1: str, arg2: str, arg3: str, arg4: str):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String,char,java.lang.String)"""
        val = __StrSubstitutor(arg0, arg1, arg2, __char.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPreserveEscapes(self, arg0: bool):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setPreserveEscapes(boolean)"""
        super(__StrSubstitutor, self).setPreserveEscapes(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def replaceIn(self, arg0: 'StringBuffer') -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuffer)"""
        return bool.__wrap(super(__StrSubstitutor, self).replaceIn(arg0))

    @overload
    def replace(self, arg0: 'CharSequence', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.CharSequence,int,int)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def replace(arg0: object, arg1: 'Properties') -> str:
        """public static java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object,java.util.Properties)"""
        return str.__wrap(__StrSubstitutor.replace(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>)"""
        val = __StrSubstitutor(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.StrSubstitutor()"""
        val = __StrSubstitutor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setVariableSuffixMatcher(self, arg0: 'StrMatcher') -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariableSuffixMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setVariableSuffixMatcher(arg0))

    @overload
    def __init__(self, arg0: 'Map', arg1: str, arg2: str, arg3: str):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String,char)"""
        val = __StrSubstitutor(arg0, arg1, arg2, __char.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def replace(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.StringBuffer,int,int)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setValueDelimiter(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setValueDelimiter(java.lang.String)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setValueDelimiter(arg0))

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: str, arg2: str, arg3: str, arg4: str):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,java.lang.String,java.lang.String,char,java.lang.String)"""
        val = __StrSubstitutor(arg0, arg1, arg2, __char.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def replaceIn(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuilder,int,int)"""
        return bool.__wrap(super(__StrSubstitutor, self).replaceIn(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getVariableResolver(self) -> 'StrLookup':
        """public org.apache.commons.lang3.text.StrLookup<?> org.apache.commons.lang3.text.StrSubstitutor.getVariableResolver()"""
        return 'StrLookup'.__wrap(super(StrSubstitutor, self).getVariableResolver())

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: 'StrMatcher', arg2: 'StrMatcher', arg3: str, arg4: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher,char,org.apache.commons.lang3.text.StrMatcher)"""
        val = __StrSubstitutor(arg0, arg1, arg2, __char.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getEscapeChar(self) -> str:
        """public char org.apache.commons.lang3.text.StrSubstitutor.getEscapeChar()"""
        return str.__wrap(super(StrSubstitutor, self).getEscapeChar())

    @overload
    def setValueDelimiter(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setValueDelimiter(char)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setValueDelimiter(__char.valueOf(arg0)))

    @overload
    def replaceIn(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuffer,int,int)"""
        return bool.__wrap(super(__StrSubstitutor, self).replaceIn(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: 'CharSequence') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.CharSequence)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0))

    @overload
    def setVariablePrefixMatcher(self, arg0: 'StrMatcher') -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariablePrefixMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setVariablePrefixMatcher(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def replace(self, arg0: 'char', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(char[],int,int)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: str, arg2: str, arg3: str):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,java.lang.String,java.lang.String,char)"""
        val = __StrSubstitutor(arg0, arg1, arg2, __char.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setEscapeChar(self, arg0: str):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setEscapeChar(char)"""
        super(__StrSubstitutor, self).setEscapeChar(__char.valueOf(arg0))

    @overload
    def replace(self, arg0: object) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0))

    @overload
    def replace(self, arg0: str, arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.String,int,int)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setVariablePrefix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariablePrefix(java.lang.String)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setVariablePrefix(arg0))

    @overload
    def getVariableSuffixMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrSubstitutor.getVariableSuffixMatcher()"""
        return 'StrMatcher'.__wrap(super(StrSubstitutor, self).getVariableSuffixMatcher())

    @overload
    def setVariableResolver(self, arg0: 'StrLookup'):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setVariableResolver(org.apache.commons.lang3.text.StrLookup<?>)"""
        super(__StrSubstitutor, self).setVariableResolver(arg0)

    @overload
    def __init__(self, arg0: 'StrLookup'):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>)"""
        val = __StrSubstitutor(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def replace(self, arg0: 'StrBuilder') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(org.apache.commons.lang3.text.StrBuilder)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def replace(self, arg0: 'StringBuffer') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.StringBuffer)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0))

    @staticmethod
    @overload
    def replace(arg0: object, arg1: 'Map', arg2: str, arg3: str) -> str:
        """public static <V> java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object,java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String)"""
        return str.__wrap(__StrSubstitutor.replace(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def replaceSystemProperties(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replaceSystemProperties(java.lang.Object)"""
        return str.__wrap(__StrSubstitutor.replaceSystemProperties(arg0))

    @overload
    def replaceIn(self, arg0: 'StringBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuilder)"""
        return bool.__wrap(super(__StrSubstitutor, self).replaceIn(arg0))

    @overload
    def setVariableSuffix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariableSuffix(java.lang.String)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setVariableSuffix(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.StrSubstitutor()"""
        val = __StrSubstitutor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def replace(arg0: object, arg1: 'Map') -> str:
        """public static <V> java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object,java.util.Map<java.lang.String, V>)"""
        return str.__wrap(__StrSubstitutor.replace(arg0, arg1))

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: 'StrMatcher', arg2: 'StrMatcher', arg3: str):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher,char)"""
        val = __StrSubstitutor(arg0, arg1, arg2, __char.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValueDelimiterMatcher(self, arg0: 'StrMatcher') -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setValueDelimiterMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setValueDelimiterMatcher(arg0))

    @overload
    def setEnableSubstitutionInVariables(self, arg0: bool):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setEnableSubstitutionInVariables(boolean)"""
        super(__StrSubstitutor, self).setEnableSubstitutionInVariables(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Map', arg1: str, arg2: str):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String)"""
        val = __StrSubstitutor(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEnableSubstitutionInVariables(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.isEnableSubstitutionInVariables()"""
        return bool.__wrap(super(StrSubstitutor, self).isEnableSubstitutionInVariables())

    @overload
    def replace(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setVariablePrefix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariablePrefix(char)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setVariablePrefix(__char.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getVariablePrefixMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrSubstitutor.getVariablePrefixMatcher()"""
        return 'StrMatcher'.__wrap(super(StrSubstitutor, self).getVariablePrefixMatcher())

    @overload
    def getValueDelimiterMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrSubstitutor.getValueDelimiterMatcher()"""
        return 'StrMatcher'.__wrap(super(StrSubstitutor, self).getValueDelimiterMatcher())

    @overload
    def replace(self, arg0: 'char') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(char[])"""
        return str.__wrap(super(__StrSubstitutor, self).replace(arg0))

    @overload
    def setVariableSuffix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariableSuffix(char)"""
        return 'StrSubstitutor'.__wrap(super(__StrSubstitutor, self).setVariableSuffix(__char.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.text.WordUtils
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.text.WordUtils as __WordUtils
__WordUtils = __WordUtils
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WordUtils():
    """org.apache.commons.lang3.text.WordUtils"""
 
    @staticmethod
    def __wrap(java_value: __WordUtils) -> 'WordUtils':
        return WordUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WordUtils):
        """
        Dynamic initializer for WordUtils.
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
    def uncapitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.uncapitalize(java.lang.String)"""
        return str.__wrap(__WordUtils.uncapitalize(arg0))

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: int, arg2: str, arg3: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.wrap(java.lang.String,int,java.lang.String,boolean)"""
        return str.__wrap(__WordUtils.wrap(arg0, __int.valueOf(arg1), arg2, __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def initials(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.initials(java.lang.String,char...)"""
        return str.__wrap(__WordUtils.initials(arg0, arg1))

    @staticmethod
    @overload
    def capitalize(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalize(java.lang.String,char...)"""
        return str.__wrap(__WordUtils.capitalize(arg0, arg1))

    @staticmethod
    @overload
    def uncapitalize(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.uncapitalize(java.lang.String,char...)"""
        return str.__wrap(__WordUtils.uncapitalize(arg0, arg1))

    @staticmethod
    @overload
    def capitalizeFully(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalizeFully(java.lang.String,char...)"""
        return str.__wrap(__WordUtils.capitalizeFully(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def capitalizeFully(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalizeFully(java.lang.String)"""
        return str.__wrap(__WordUtils.capitalizeFully(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: int, arg2: str, arg3: bool, arg4: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.wrap(java.lang.String,int,java.lang.String,boolean,java.lang.String)"""
        return str.__wrap(__WordUtils.wrap(arg0, __int.valueOf(arg1), arg2, __boolean.valueOf(arg3), arg4))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.WordUtils()"""
        val = __WordUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.wrap(java.lang.String,int)"""
        return str.__wrap(__WordUtils.wrap(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def initials(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.initials(java.lang.String)"""
        return str.__wrap(__WordUtils.initials(arg0))

    @staticmethod
    @overload
    def swapCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.swapCase(java.lang.String)"""
        return str.__wrap(__WordUtils.swapCase(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.WordUtils()"""
        val = __WordUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def capitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalize(java.lang.String)"""
        return str.__wrap(__WordUtils.capitalize(arg0))

    @staticmethod
    @overload
    def containsAllWords(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.text.WordUtils.containsAllWords(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool.__wrap(__WordUtils.containsAllWords(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.StrTokenizer
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
from typing import List
import java.util.function.Consumer as Consumer
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import org.apache.commons.lang3.text.StrTokenizer as __StrTokenizer
__StrTokenizer = __StrTokenizer
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.text.StrMatcher as __StrMatcher
__StrMatcher = __StrMatcher
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class StrTokenizer(__ListIterator, ListIterator, __Cloneable, Cloneable):
    """org.apache.commons.lang3.text.StrTokenizer"""
 
    @staticmethod
    def __wrap(java_value: __StrTokenizer) -> 'StrTokenizer':
        return StrTokenizer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StrTokenizer):
        """
        Dynamic initializer for StrTokenizer.
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
    def nextIndex(self) -> int:
        """public int org.apache.commons.lang3.text.StrTokenizer.nextIndex()"""
        return int.__wrap(super(StrTokenizer, self).nextIndex())

    @staticmethod
    @overload
    def getCSVInstance() -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getCSVInstance()"""
        return StrTokenizer.__wrap(__StrTokenizer.getCSVInstance())

    @overload
    def setDelimiterString(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setDelimiterString(java.lang.String)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setDelimiterString(arg0))

    @overload
    def previousToken(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.previousToken()"""
        return str.__wrap(super(StrTokenizer, self).previousToken())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,java.lang.String)"""
        val = __StrTokenizer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isEmptyTokenAsNull(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.isEmptyTokenAsNull()"""
        return bool.__wrap(super(StrTokenizer, self).isEmptyTokenAsNull())

    @overload
    def setTrimmerMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setTrimmerMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setTrimmerMatcher(arg0))

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,char,char)"""
        val = __StrTokenizer(arg0, __char.valueOf(arg1), __char.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setQuoteMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setQuoteMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setQuoteMatcher(arg0))

    @staticmethod
    @overload
    def getCSVInstance(arg0: 'char') -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getCSVInstance(char[])"""
        return StrTokenizer.__wrap(__StrTokenizer.getCSVInstance(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String)"""
        val = __StrTokenizer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.StrTokenizer()"""
        val = __StrTokenizer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'char'):
        """public org.apache.commons.lang3.text.StrTokenizer(char[])"""
        val = __StrTokenizer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.text.StrTokenizer.size()"""
        return int.__wrap(super(StrTokenizer, self).size())

    @overload
    def getTokenArray(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.text.StrTokenizer.getTokenArray()"""
        return List[str].__wrap(super(StrTokenizer, self).getTokenArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def nextToken(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.nextToken()"""
        return str.__wrap(super(StrTokenizer, self).nextToken())

    @staticmethod
    @overload
    def getTSVInstance(arg0: 'char') -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getTSVInstance(char[])"""
        return StrTokenizer.__wrap(__StrTokenizer.getTSVInstance(arg0))

    @staticmethod
    @overload
    def getTSVInstance(arg0: str) -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getTSVInstance(java.lang.String)"""
        return StrTokenizer.__wrap(__StrTokenizer.getTSVInstance(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.lang3.text.StrTokenizer.remove()"""
        super(StrTokenizer, self).remove()

    @overload
    def reset(self) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.reset()"""
        return 'StrTokenizer'.__wrap(super(StrTokenizer, self).reset())

    @overload
    def __init__(self, arg0: 'char', arg1: 'StrMatcher', arg2: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher)"""
        val = __StrTokenizer(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def previous(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.previous()"""
        return str.__wrap(super(StrTokenizer, self).previous())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,char)"""
        val = __StrTokenizer(arg0, __char.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTokenList(self) -> 'List':
        """public java.util.List<java.lang.String> org.apache.commons.lang3.text.StrTokenizer.getTokenList()"""
        return 'List'.__wrap(super(StrTokenizer, self).getTokenList())

    @overload
    def getDelimiterMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getDelimiterMatcher()"""
        return 'StrMatcher'.__wrap(super(StrTokenizer, self).getDelimiterMatcher())

    @overload
    def setIgnoredChar(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setIgnoredChar(char)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setIgnoredChar(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'char', arg1: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],org.apache.commons.lang3.text.StrMatcher)"""
        val = __StrTokenizer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'char', arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],char)"""
        val = __StrTokenizer(arg0, __char.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.toString()"""
        return str.__wrap(super(StrTokenizer, self).toString())

    @overload
    def reset(self, arg0: 'char') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.reset(char[])"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).reset(arg0))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.hasNext()"""
        return bool.__wrap(super(StrTokenizer, self).hasNext())

    @overload
    def clone(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.text.StrTokenizer.clone()"""
        return object.__wrap(super(StrTokenizer, self).clone())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setQuoteChar(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setQuoteChar(char)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setQuoteChar(__char.valueOf(arg0)))

    @overload
    def set(self, arg0: str):
        """public void org.apache.commons.lang3.text.StrTokenizer.set(java.lang.String)"""
        super(__StrTokenizer, self).set(arg0)

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'StrMatcher', arg2: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher)"""
        val = __StrTokenizer(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getIgnoredMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getIgnoredMatcher()"""
        return 'StrMatcher'.__wrap(super(StrTokenizer, self).getIgnoredMatcher())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.lang3.text.StrTokenizer.previousIndex()"""
        return int.__wrap(super(StrTokenizer, self).previousIndex())

    @overload
    def __init__(self, arg0: str, arg1: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,org.apache.commons.lang3.text.StrMatcher)"""
        val = __StrTokenizer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reset(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.reset(java.lang.String)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).reset(arg0))

    @overload
    def __init__(self, arg0: 'char', arg1: str, arg2: str):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],char,char)"""
        val = __StrTokenizer(arg0, __char.valueOf(arg1), __char.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setDelimiterMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setDelimiterMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setDelimiterMatcher(arg0))

    @override
    @overload
    def next(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.next()"""
        return str.__wrap(super(StrTokenizer, self).next())

    @overload
    def setIgnoredMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setIgnoredMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setIgnoredMatcher(arg0))

    @overload
    def isIgnoreEmptyTokens(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.isIgnoreEmptyTokens()"""
        return bool.__wrap(super(StrTokenizer, self).isIgnoreEmptyTokens())

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
    def getQuoteMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getQuoteMatcher()"""
        return 'StrMatcher'.__wrap(super(StrTokenizer, self).getQuoteMatcher())

    @overload
    def setEmptyTokenAsNull(self, arg0: bool) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setEmptyTokenAsNull(boolean)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setEmptyTokenAsNull(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.StrTokenizer()"""
        val = __StrTokenizer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.hasPrevious()"""
        return bool.__wrap(super(StrTokenizer, self).hasPrevious())

    @staticmethod
    @overload
    def getCSVInstance(arg0: str) -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getCSVInstance(java.lang.String)"""
        return StrTokenizer.__wrap(__StrTokenizer.getCSVInstance(arg0))

    @overload
    def __init__(self, arg0: 'char', arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],java.lang.String)"""
        val = __StrTokenizer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: str):
        """public void org.apache.commons.lang3.text.StrTokenizer.add(java.lang.String)"""
        super(__StrTokenizer, self).add(arg0)

    @overload
    def getTrimmerMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getTrimmerMatcher()"""
        return 'StrMatcher'.__wrap(super(StrTokenizer, self).getTrimmerMatcher())

    @overload
    def setDelimiterChar(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setDelimiterChar(char)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setDelimiterChar(__char.valueOf(arg0)))

    @overload
    def setIgnoreEmptyTokens(self, arg0: bool) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setIgnoreEmptyTokens(boolean)"""
        return 'StrTokenizer'.__wrap(super(__StrTokenizer, self).setIgnoreEmptyTokens(__boolean.valueOf(arg0)))

    @overload
    def getContent(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.getContent()"""
        return str.__wrap(super(StrTokenizer, self).getContent())

    @staticmethod
    @overload
    def getTSVInstance() -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getTSVInstance()"""
        return StrTokenizer.__wrap(__StrTokenizer.getTSVInstance())