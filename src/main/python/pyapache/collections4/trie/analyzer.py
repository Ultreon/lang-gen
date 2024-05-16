from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.trie.KeyAnalyzer as __KeyAnalyzer
__KeyAnalyzer = __KeyAnalyzer
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer as __StringKeyAnalyzer
__StringKeyAnalyzer = __StringKeyAnalyzer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class StringKeyAnalyzer(collections4.__KeyAnalyzer, trie.KeyAnalyzer):
    """org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer"""
 
    @staticmethod
    def __wrap(java_value: __StringKeyAnalyzer) -> 'StringKeyAnalyzer':
        return StringKeyAnalyzer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringKeyAnalyzer):
        """
        Dynamic initializer for StringKeyAnalyzer.
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
    def __init__(self):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = __StringKeyAnalyzer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def bitsPerElement(self) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitsPerElement()"""
        return int.__wrap(super(StringKeyAnalyzer, self).bitsPerElement())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = __StringKeyAnalyzer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.trie.KeyAnalyzer.compare(K,K)"""
        return int.__wrap(super(__trie.KeyAnalyzer, self).compare(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def bitIndex(self, arg0: str, arg1: int, arg2: int, arg3: str, arg4: int, arg5: int) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitIndex(java.lang.String,int,int,java.lang.String,int,int)"""
        return int.__wrap(super(__StringKeyAnalyzer, self).bitIndex(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def isPrefix(self, arg0: str, arg1: int, arg2: int, arg3: str) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isPrefix(java.lang.String,int,int,java.lang.String)"""
        return bool.__wrap(super(__StringKeyAnalyzer, self).isPrefix(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def isBitSet(self, arg0: str, arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isBitSet(java.lang.String,int,int)"""
        return bool.__wrap(super(__StringKeyAnalyzer, self).isBitSet(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def lengthInBits(self, arg0: str) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.lengthInBits(java.lang.String)"""
        return int.__wrap(super(__StringKeyAnalyzer, self).lengthInBits(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.trie.KeyAnalyzer as __KeyAnalyzer
__KeyAnalyzer = __KeyAnalyzer
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer as __StringKeyAnalyzer
__StringKeyAnalyzer = __StringKeyAnalyzer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class StringKeyAnalyzer(collections4.__KeyAnalyzer, trie.KeyAnalyzer):
    """org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer"""
 
    @staticmethod
    def __wrap(java_value: __StringKeyAnalyzer) -> 'StringKeyAnalyzer':
        return StringKeyAnalyzer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringKeyAnalyzer):
        """
        Dynamic initializer for StringKeyAnalyzer.
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
    def __init__(self):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = __StringKeyAnalyzer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def bitsPerElement(self) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitsPerElement()"""
        return int.__wrap(super(StringKeyAnalyzer, self).bitsPerElement())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = __StringKeyAnalyzer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.trie.KeyAnalyzer.compare(K,K)"""
        return int.__wrap(super(__trie.KeyAnalyzer, self).compare(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def bitIndex(self, arg0: str, arg1: int, arg2: int, arg3: str, arg4: int, arg5: int) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitIndex(java.lang.String,int,int,java.lang.String,int,int)"""
        return int.__wrap(super(__StringKeyAnalyzer, self).bitIndex(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def isPrefix(self, arg0: str, arg1: int, arg2: int, arg3: str) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isPrefix(java.lang.String,int,int,java.lang.String)"""
        return bool.__wrap(super(__StringKeyAnalyzer, self).isPrefix(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def isBitSet(self, arg0: str, arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isBitSet(java.lang.String,int,int)"""
        return bool.__wrap(super(__StringKeyAnalyzer, self).isBitSet(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def lengthInBits(self, arg0: str) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.lengthInBits(java.lang.String)"""
        return int.__wrap(super(__StringKeyAnalyzer, self).lengthInBits(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer