from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer as _StringKeyAnalyzer
_StringKeyAnalyzer = _StringKeyAnalyzer
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.trie.KeyAnalyzer as _KeyAnalyzer
_KeyAnalyzer = _KeyAnalyzer
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringKeyAnalyzer():
    """org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer"""
 
    @staticmethod
    def _wrap(java_value: _StringKeyAnalyzer) -> 'StringKeyAnalyzer':
        return StringKeyAnalyzer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringKeyAnalyzer):
        """
        Dynamic initializer for StringKeyAnalyzer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringKeyAnalyzer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringKeyAnalyzer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def bitIndex(self, arg0: str, arg1: int, arg2: int, arg3: str, arg4: int, arg5: int) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitIndex(java.lang.String,int,int,java.lang.String,int,int)"""
        return int._wrap(super(_StringKeyAnalyzer, self).bitIndex(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @overload
    def isBitSet(self, arg0: str, arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isBitSet(java.lang.String,int,int)"""
        return bool._wrap(super(_StringKeyAnalyzer, self).isBitSet(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def __init__(self):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = _StringKeyAnalyzer()
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.trie.KeyAnalyzer.compare(K,K)"""
        return int._wrap(super(_trie.KeyAnalyzer, self).compare(arg0, arg1))

    @overload
    def isPrefix(self, arg0: str, arg1: int, arg2: int, arg3: str) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isPrefix(java.lang.String,int,int,java.lang.String)"""
        return bool._wrap(super(_StringKeyAnalyzer, self).isPrefix(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

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
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = _StringKeyAnalyzer()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def lengthInBits(self, arg0: str) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.lengthInBits(java.lang.String)"""
        return int._wrap(super(_StringKeyAnalyzer, self).lengthInBits(arg0))

    @override
    @overload
    def bitsPerElement(self) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitsPerElement()"""
        return int._wrap(super(StringKeyAnalyzer, self).bitsPerElement())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer as _StringKeyAnalyzer
_StringKeyAnalyzer = _StringKeyAnalyzer
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.trie.KeyAnalyzer as _KeyAnalyzer
_KeyAnalyzer = _KeyAnalyzer
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringKeyAnalyzer():
    """org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer"""
 
    @staticmethod
    def _wrap(java_value: _StringKeyAnalyzer) -> 'StringKeyAnalyzer':
        return StringKeyAnalyzer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringKeyAnalyzer):
        """
        Dynamic initializer for StringKeyAnalyzer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringKeyAnalyzer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringKeyAnalyzer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def bitIndex(self, arg0: str, arg1: int, arg2: int, arg3: str, arg4: int, arg5: int) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitIndex(java.lang.String,int,int,java.lang.String,int,int)"""
        return int._wrap(super(_StringKeyAnalyzer, self).bitIndex(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @overload
    def isBitSet(self, arg0: str, arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isBitSet(java.lang.String,int,int)"""
        return bool._wrap(super(_StringKeyAnalyzer, self).isBitSet(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def __init__(self):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = _StringKeyAnalyzer()
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.trie.KeyAnalyzer.compare(K,K)"""
        return int._wrap(super(_trie.KeyAnalyzer, self).compare(arg0, arg1))

    @overload
    def isPrefix(self, arg0: str, arg1: int, arg2: int, arg3: str) -> bool:
        """public boolean org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.isPrefix(java.lang.String,int,int,java.lang.String)"""
        return bool._wrap(super(_StringKeyAnalyzer, self).isPrefix(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

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
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer()"""
        val = _StringKeyAnalyzer()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def lengthInBits(self, arg0: str) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.lengthInBits(java.lang.String)"""
        return int._wrap(super(_StringKeyAnalyzer, self).lengthInBits(arg0))

    @override
    @overload
    def bitsPerElement(self) -> int:
        """public int org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer.bitsPerElement()"""
        return int._wrap(super(StringKeyAnalyzer, self).bitsPerElement())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer