from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.common.base.Optional as _Optional
_Optional = _Optional
import java.lang.reflect.Field as Field
import java.lang.String as _String
_String = _String
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import java.lang.Enum as Enum
import java.lang.reflect.Field as _Field
_Field = _Field
import java.lang.String as _string
import com.google.common.base.Enums as _Enums
_Enums = _Enums
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Enums():
    """com.google.common.base.Enums"""
 
    @staticmethod
    def _wrap(java_value: _Enums) -> 'Enums':
        return Enums(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Enums):
        """
        Dynamic initializer for Enums.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Enums__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Enums__wrapper":
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

    @staticmethod
    @overload
    def getField(enumValue: 'Enum') -> 'Field':
        """public static java.lang.reflect.Field com.google.common.base.Enums.getField(java.lang.Enum<?>)"""
        return Field._wrap(_Enums.getField(enumValue))

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
    def stringConverter(enumClass: 'Class') -> 'Converter':
        """public static <T extends java.lang.Enum<T>> com.google.common.base.Converter<java.lang.String, T> com.google.common.base.Enums.stringConverter(java.lang.Class<T>)"""
        return Converter._wrap(_Enums.stringConverter(enumClass))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getIfPresent(enumClass: 'Class', value: str) -> 'Optional':
        """public static <T extends java.lang.Enum<T>> com.google.common.base.Optional<T> com.google.common.base.Enums.getIfPresent(java.lang.Class<T>,java.lang.String)"""
        return Optional._wrap(_Enums.getIfPresent(enumClass, value))

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

 
 
 
# CLASS: com.google.common.base.Enums
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.common.base.Optional as _Optional
_Optional = _Optional
import java.lang.reflect.Field as Field
import java.lang.String as _String
_String = _String
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import java.lang.Enum as Enum
import java.lang.reflect.Field as _Field
_Field = _Field
import java.lang.String as _string
import com.google.common.base.Enums as _Enums
_Enums = _Enums
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Enums():
    """com.google.common.base.Enums"""
 
    @staticmethod
    def _wrap(java_value: _Enums) -> 'Enums':
        return Enums(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Enums):
        """
        Dynamic initializer for Enums.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Enums__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Enums__wrapper":
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

    @staticmethod
    @overload
    def getField(enumValue: 'Enum') -> 'Field':
        """public static java.lang.reflect.Field com.google.common.base.Enums.getField(java.lang.Enum<?>)"""
        return Field._wrap(_Enums.getField(enumValue))

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
    def stringConverter(enumClass: 'Class') -> 'Converter':
        """public static <T extends java.lang.Enum<T>> com.google.common.base.Converter<java.lang.String, T> com.google.common.base.Enums.stringConverter(java.lang.Class<T>)"""
        return Converter._wrap(_Enums.stringConverter(enumClass))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getIfPresent(enumClass: 'Class', value: str) -> 'Optional':
        """public static <T extends java.lang.Enum<T>> com.google.common.base.Optional<T> com.google.common.base.Enums.getIfPresent(java.lang.Class<T>,java.lang.String)"""
        return Optional._wrap(_Enums.getIfPresent(enumClass, value))

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

 
 
 
# CLASS: com.google.common.base.Enums 
 
 
# CLASS: com.google.common.base.Defaults
from builtins import str
import com.google.common.base.Defaults as _Defaults
_Defaults = _Defaults
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Defaults():
    """com.google.common.base.Defaults"""
 
    @staticmethod
    def _wrap(java_value: _Defaults) -> 'Defaults':
        return Defaults(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Defaults):
        """
        Dynamic initializer for Defaults.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Defaults__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Defaults__wrapper":
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
    def defaultValue(type: 'Class') -> object:
        """public static <T> T com.google.common.base.Defaults.defaultValue(java.lang.Class<T>)"""
        return object._wrap(_Defaults.defaultValue(type))

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
 
 
# CLASS: com.google.common.base.FinalizableReferenceQueue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.google.common.base.FinalizableReferenceQueue as _FinalizableReferenceQueue
_FinalizableReferenceQueue = _FinalizableReferenceQueue
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FinalizableReferenceQueue():
    """com.google.common.base.FinalizableReferenceQueue"""
 
    @staticmethod
    def _wrap(java_value: _FinalizableReferenceQueue) -> 'FinalizableReferenceQueue':
        return FinalizableReferenceQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FinalizableReferenceQueue):
        """
        Dynamic initializer for FinalizableReferenceQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FinalizableReferenceQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FinalizableReferenceQueue__wrapper":
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
    def close(self):
        """public void com.google.common.base.FinalizableReferenceQueue.close()"""
        super(FinalizableReferenceQueue, self).close()

    @overload
    def __init__(self, ):
        """public com.google.common.base.FinalizableReferenceQueue()"""
        val = _FinalizableReferenceQueue()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.google.common.base.FinalizableReferenceQueue()"""
        val = _FinalizableReferenceQueue()
        self.__wrapper = val 
 
 
# CLASS: com.google.common.base.CharMatcher
from builtins import str
import java.util.function.Predicate as Predicate
import java.lang.CharSequence as CharSequence
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.google.common.base.Predicate as _Predicate
_Predicate = _Predicate
import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
import com.google.common.base.CharMatcher as _CharMatcher
_CharMatcher = _CharMatcher
import java.lang.Integer as _int
import java.lang.Character as Character
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharMatcher():
    """com.google.common.base.CharMatcher"""
 
    @staticmethod
    def _wrap(java_value: _CharMatcher) -> 'CharMatcher':
        return CharMatcher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharMatcher):
        """
        Dynamic initializer for CharMatcher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharMatcher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharMatcher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def whitespace() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.whitespace()"""
        return CharMatcher._wrap(_CharMatcher.whitespace())

    @staticmethod
    @overload
    def javaDigit() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaDigit()"""
        return CharMatcher._wrap(_CharMatcher.javaDigit())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def forPredicate(predicate: 'Predicate') -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.forPredicate(com.google.common.base.Predicate<? super java.lang.Character>)"""
        return CharMatcher._wrap(_CharMatcher.forPredicate(predicate))

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
    def breakingWhitespace() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.breakingWhitespace()"""
        return CharMatcher._wrap(_CharMatcher.breakingWhitespace())

    @staticmethod
    @overload
    def invisible() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.invisible()"""
        return CharMatcher._wrap(_CharMatcher.invisible())

    @overload
    def or(self, other: 'CharMatcher') -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.or(com.google.common.base.CharMatcher)"""
        return 'CharMatcher'._wrap(super(_CharMatcher, self).or(other))

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).and(arg0))

    @overload
    def retainFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.retainFrom(java.lang.CharSequence)"""
        return str._wrap(super(_CharMatcher, self).retainFrom(sequence))

    @staticmethod
    @overload
    def anyOf(sequence: 'CharSequence') -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.anyOf(java.lang.CharSequence)"""
        return CharMatcher._wrap(_CharMatcher.anyOf(sequence))

    @overload
    def and(self, other: 'CharMatcher') -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.and(com.google.common.base.CharMatcher)"""
        return 'CharMatcher'._wrap(super(_CharMatcher, self).and(other))

    @overload
    def trimLeadingFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimLeadingFrom(java.lang.CharSequence)"""
        return str._wrap(super(_CharMatcher, self).trimLeadingFrom(sequence))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def singleWidth() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.singleWidth()"""
        return CharMatcher._wrap(_CharMatcher.singleWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.toString()"""
        return str._wrap(super(CharMatcher, self).toString())

    @abstractmethod
    def matches(self, c: str):
        """public abstract boolean com.google.common.base.CharMatcher.matches(char)"""
        pass

    @staticmethod
    @overload
    def isNot(match: str) -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.isNot(char)"""
        return CharMatcher._wrap(_CharMatcher.isNot(_char.valueOf(match)))

    @staticmethod
    @overload
    def inRange(startInclusive: str, endInclusive: str) -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.inRange(char,char)"""
        return CharMatcher._wrap(_CharMatcher.inRange(_char.valueOf(startInclusive), _char.valueOf(endInclusive)))

    @staticmethod
    @overload
    def none() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.none()"""
        return CharMatcher._wrap(_CharMatcher.none())

    @staticmethod
    @overload
    def javaLetter() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaLetter()"""
        return CharMatcher._wrap(_CharMatcher.javaLetter())

    @override
    @overload
    def negate(self) -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.negate()"""
        return 'CharMatcher'._wrap(super(CharMatcher, self).negate())

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

    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).or(arg0))

    @staticmethod
    @overload
    def noneOf(sequence: 'CharSequence') -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.noneOf(java.lang.CharSequence)"""
        return CharMatcher._wrap(_CharMatcher.noneOf(sequence))

    @overload
    def replaceFrom(self, sequence: 'CharSequence', replacement: str) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.replaceFrom(java.lang.CharSequence,char)"""
        return str._wrap(super(_CharMatcher, self).replaceFrom(sequence, _char.valueOf(replacement)))

    @overload
    def indexIn(self, sequence: 'CharSequence', start: int) -> int:
        """public int com.google.common.base.CharMatcher.indexIn(java.lang.CharSequence,int)"""
        return int._wrap(super(_CharMatcher, self).indexIn(sequence, _int.valueOf(start)))

    @overload
    def trimFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimFrom(java.lang.CharSequence)"""
        return str._wrap(super(_CharMatcher, self).trimFrom(sequence))

    @overload
    def removeFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.removeFrom(java.lang.CharSequence)"""
        return str._wrap(super(_CharMatcher, self).removeFrom(sequence))

    @overload
    def replaceFrom(self, sequence: 'CharSequence', replacement: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.replaceFrom(java.lang.CharSequence,java.lang.CharSequence)"""
        return str._wrap(super(_CharMatcher, self).replaceFrom(sequence, replacement))

    @staticmethod
    @overload
    def digit() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.digit()"""
        return CharMatcher._wrap(_CharMatcher.digit())

    @staticmethod
    @overload
    def any() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.any()"""
        return CharMatcher._wrap(_CharMatcher.any())

    @overload
    def test(self, input: object) -> bool:
        """public default boolean com.google.common.base.Predicate.test(T)"""
        return bool._wrap(super(_Predicate, self).test(input))

    @staticmethod
    @overload
    def is(match: str) -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.is(char)"""
        return CharMatcher._wrap(_CharMatcher.is(_char.valueOf(match)))

    @overload
    def lastIndexIn(self, sequence: 'CharSequence') -> int:
        """public int com.google.common.base.CharMatcher.lastIndexIn(java.lang.CharSequence)"""
        return int._wrap(super(_CharMatcher, self).lastIndexIn(sequence))

    @overload
    def trimAndCollapseFrom(self, sequence: 'CharSequence', replacement: str) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimAndCollapseFrom(java.lang.CharSequence,char)"""
        return str._wrap(super(_CharMatcher, self).trimAndCollapseFrom(sequence, _char.valueOf(replacement)))

    @overload
    def indexIn(self, sequence: 'CharSequence') -> int:
        """public int com.google.common.base.CharMatcher.indexIn(java.lang.CharSequence)"""
        return int._wrap(super(_CharMatcher, self).indexIn(sequence))

    @staticmethod
    @overload
    def javaLowerCase() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaLowerCase()"""
        return CharMatcher._wrap(_CharMatcher.javaLowerCase())

    @staticmethod
    @overload
    def javaUpperCase() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaUpperCase()"""
        return CharMatcher._wrap(_CharMatcher.javaUpperCase())

    @overload
    def matchesAllOf(self, sequence: 'CharSequence') -> bool:
        """public boolean com.google.common.base.CharMatcher.matchesAllOf(java.lang.CharSequence)"""
        return bool._wrap(super(_CharMatcher, self).matchesAllOf(sequence))

    @overload
    def countIn(self, sequence: 'CharSequence') -> int:
        """public int com.google.common.base.CharMatcher.countIn(java.lang.CharSequence)"""
        return int._wrap(super(_CharMatcher, self).countIn(sequence))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def matchesNoneOf(self, sequence: 'CharSequence') -> bool:
        """public boolean com.google.common.base.CharMatcher.matchesNoneOf(java.lang.CharSequence)"""
        return bool._wrap(super(_CharMatcher, self).matchesNoneOf(sequence))

    @overload
    def matchesAnyOf(self, sequence: 'CharSequence') -> bool:
        """public boolean com.google.common.base.CharMatcher.matchesAnyOf(java.lang.CharSequence)"""
        return bool._wrap(super(_CharMatcher, self).matchesAnyOf(sequence))

    @staticmethod
    @overload
    def ascii() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.ascii()"""
        return CharMatcher._wrap(_CharMatcher.ascii())

    @staticmethod
    @overload
    def javaLetterOrDigit() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaLetterOrDigit()"""
        return CharMatcher._wrap(_CharMatcher.javaLetterOrDigit())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def apply(self, character: 'Character') -> bool:
        """public boolean com.google.common.base.CharMatcher.apply(java.lang.Character)"""
        return bool._wrap(super(_CharMatcher, self).apply(character))

    @overload
    def trimTrailingFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimTrailingFrom(java.lang.CharSequence)"""
        return str._wrap(super(_CharMatcher, self).trimTrailingFrom(sequence))

    @overload
    def collapseFrom(self, sequence: 'CharSequence', replacement: str) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.collapseFrom(java.lang.CharSequence,char)"""
        return str._wrap(super(_CharMatcher, self).collapseFrom(sequence, _char.valueOf(replacement)))

    @overload
    def precomputed(self) -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.precomputed()"""
        return 'CharMatcher'._wrap(super(CharMatcher, self).precomputed())

    @staticmethod
    @overload
    def javaIsoControl() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaIsoControl()"""
        return CharMatcher._wrap(_CharMatcher.javaIsoControl()) 
 
 
# CLASS: com.google.common.base.Predicate
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.lang.Object as _object
from abc import abstractmethod, ABC
import com.google.common.base.Predicate as _Predicate
_Predicate = _Predicate
from builtins import bool
import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
 
class Predicate():
    """com.google.common.base.Predicate"""
 
    @staticmethod
    def _wrap(java_value: _Predicate) -> 'Predicate':
        return Predicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Predicate):
        """
        Dynamic initializer for Predicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Predicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Predicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).or(arg0))

    @abstractmethod
    def apply(self, input: object):
        """public abstract boolean com.google.common.base.Predicate.apply(T)"""
        pass

    @overload
    def test(self, input: object) -> bool:
        """public default boolean com.google.common.base.Predicate.test(T)"""
        return bool._wrap(super(_Predicate, self).test(input))

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).and(arg0))

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Predicate.equals(java.lang.Object)"""
        pass

    @override
    @overload
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'._wrap(super(Predicate, self).negate()) 
 
 
# CLASS: com.google.common.base.Ticker
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.Ticker as _Ticker
_Ticker = _Ticker
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Ticker():
    """com.google.common.base.Ticker"""
 
    @staticmethod
    def _wrap(java_value: _Ticker) -> 'Ticker':
        return Ticker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ticker):
        """
        Dynamic initializer for Ticker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ticker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ticker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def systemTicker() -> 'Ticker':
        """public static com.google.common.base.Ticker com.google.common.base.Ticker.systemTicker()"""
        return Ticker._wrap(_Ticker.systemTicker())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def read(self, ):
        """public abstract long com.google.common.base.Ticker.read()"""
        pass

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
 
 
# CLASS: com.google.common.base.Equivalence$Wrapper
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.base.Equivalence as _Equivalence_Wrapper
_Wrapper = _Equivalence_Wrapper.Wrapper
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Wrapper():
    """com.google.common.base.Equivalence.Wrapper"""
 
    @staticmethod
    def _wrap(java_value: _Wrapper) -> 'Wrapper':
        return Wrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Wrapper):
        """
        Dynamic initializer for Wrapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Wrapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Wrapper__wrapper":
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
    def get(self) -> object:
        """public T com.google.common.base.Equivalence$Wrapper.get()"""
        return object._wrap(super(Wrapper, self).get())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.base.Equivalence$Wrapper.equals(java.lang.Object)"""
        return bool._wrap(super(_Wrapper, self).equals(obj))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.base.Equivalence$Wrapper.hashCode()"""
        return int._wrap(super(Wrapper, self).hashCode())

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
        """public java.lang.String com.google.common.base.Equivalence$Wrapper.toString()"""
        return str._wrap(super(Wrapper, self).toString()) 
 
 
# CLASS: com.google.common.base.Preconditions
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.base.Preconditions as _Preconditions
_Preconditions = _Preconditions
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Preconditions():
    """com.google.common.base.Preconditions"""
 
    @staticmethod
    def _wrap(java_value: _Preconditions) -> 'Preconditions':
        return Preconditions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Preconditions):
        """
        Dynamic initializer for Preconditions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Preconditions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Preconditions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,long)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _int.valueOf(p1), _long.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,char)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, p1, _char.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,long)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, p1, _long.valueOf(p2)))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _long.valueOf(p1)))

    @staticmethod
    @overload
    def checkElementIndex(index: int, size: int) -> int:
        """public static int com.google.common.base.Preconditions.checkElementIndex(int,int)"""
        return int._wrap(_Preconditions.checkElementIndex(_int.valueOf(index), _int.valueOf(size)))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,long)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _long.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, *errorMessageArgs: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object...)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, errorMessageArgs))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,char)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, p1, _char.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,char)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _char.valueOf(p2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, p1, p2)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _char.valueOf(p1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, *errorMessageArgs: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object...)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, errorMessageArgs)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,int)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _int.valueOf(p1), _int.valueOf(p2)))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,long)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _long.valueOf(p2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, p1, p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, p1, p2)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _long.valueOf(p1), p2))

    @staticmethod
    @overload
    def checkElementIndex(index: int, size: int, desc: str) -> int:
        """public static int com.google.common.base.Preconditions.checkElementIndex(int,int,java.lang.String)"""
        return int._wrap(_Preconditions.checkElementIndex(_int.valueOf(index), _int.valueOf(size), desc))

    @staticmethod
    @overload
    def checkNotNull(reference: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T)"""
        return object._wrap(_Preconditions.checkNotNull(reference))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,int)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _long.valueOf(p1), _int.valueOf(p2)))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,int)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, p1, _int.valueOf(p2)))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,int)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _int.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,char)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _char.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,char)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _char.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,long)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _long.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _int.valueOf(p1), p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,char)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _long.valueOf(p1), _char.valueOf(p2)))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,int)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _int.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, *errorMessageArgs: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object...)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, errorMessageArgs)

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,int)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, p1, _int.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,char)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, p1, _char.valueOf(p2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,long)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _long.valueOf(p1), _long.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,long)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _long.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,char)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _char.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), p2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3, p4)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,char)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _char.valueOf(p1), _char.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, p1)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,char)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _char.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,long)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _long.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,long)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, p1, _long.valueOf(p2))

    @staticmethod
    @overload
    def checkPositionIndexes(start: int, end: int, size: int):
        """public static void com.google.common.base.Preconditions.checkPositionIndexes(int,int,int)"""
        _Preconditions.checkPositionIndexes(_int.valueOf(start), _int.valueOf(end), _int.valueOf(size))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _int.valueOf(p1)))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,char)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _int.valueOf(p1), _char.valueOf(p2)))

    @staticmethod
    @overload
    def checkState(expression: bool):
        """public static void com.google.common.base.Preconditions.checkState(boolean)"""
        _Preconditions.checkState(_boolean.valueOf(expression))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,int)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _int.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,int)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _int.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3, p4)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,long)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _char.valueOf(p1), _long.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessage: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessage)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, p1, p2, p3, p4))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessage: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessage)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,long)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, p1, _long.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,int)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _char.valueOf(p1), _int.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, p1)

    @staticmethod
    @overload
    def checkPositionIndex(index: int, size: int, desc: str) -> int:
        """public static int com.google.common.base.Preconditions.checkPositionIndex(int,int,java.lang.String)"""
        return int._wrap(_Preconditions.checkPositionIndex(_int.valueOf(index), _int.valueOf(size), desc))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,int)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, p1, _int.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessage: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessage))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,java.lang.Object)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkArgument(expression: bool):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,char)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _char.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,int)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _int.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, _char.valueOf(p1), p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,long)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _long.valueOf(p2))

    @staticmethod
    @overload
    def checkPositionIndex(index: int, size: int) -> int:
        """public static int com.google.common.base.Preconditions.checkPositionIndex(int,int)"""
        return int._wrap(_Preconditions.checkPositionIndex(_int.valueOf(index), _int.valueOf(size)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: object, p3: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, p1, p2, p3))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object)"""
        return object._wrap(_Preconditions.checkNotNull(reference, errorMessageTemplate, p1))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,int)"""
        _Preconditions.checkArgument(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _int.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char)"""
        _Preconditions.checkState(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1)) 
 
 
# CLASS: com.google.common.base.MoreObjects$ToStringHelper
from builtins import str
import java.lang.Character as _char
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.MoreObjects as _MoreObjects_ToStringHelper
_ToStringHelper = _MoreObjects_ToStringHelper.ToStringHelper
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ToStringHelper():
    """com.google.common.base.MoreObjects.ToStringHelper"""
 
    @staticmethod
    def _wrap(java_value: _ToStringHelper) -> 'ToStringHelper':
        return ToStringHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToStringHelper):
        """
        Dynamic initializer for ToStringHelper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToStringHelper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToStringHelper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, name: str, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,double)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).add(name, _double.valueOf(value)))

    @overload
    def addValue(self, value: str) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(char)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).addValue(_char.valueOf(value)))

    @overload
    def addValue(self, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(double)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).addValue(_double.valueOf(value)))

    @overload
    def add(self, name: str, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,int)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).add(name, _int.valueOf(value)))

    @overload
    def addValue(self, value: object) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(java.lang.Object)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).addValue(value))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, name: str, value: bool) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,boolean)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).add(name, _boolean.valueOf(value)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addValue(self, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(long)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).addValue(_long.valueOf(value)))

    @overload
    def addValue(self, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(int)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).addValue(_int.valueOf(value)))

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
    def add(self, name: str, value: str) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,char)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).add(name, _char.valueOf(value)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.MoreObjects$ToStringHelper.toString()"""
        return str._wrap(super(ToStringHelper, self).toString())

    @overload
    def add(self, name: str, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,float)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).add(name, _float.valueOf(value)))

    @overload
    def add(self, name: str, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,long)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).add(name, _long.valueOf(value)))

    @overload
    def omitNullValues(self) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.omitNullValues()"""
        return 'ToStringHelper'._wrap(super(ToStringHelper, self).omitNullValues())

    @overload
    def addValue(self, value: bool) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(boolean)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).addValue(_boolean.valueOf(value)))

    @overload
    def addValue(self, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(float)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).addValue(_float.valueOf(value)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, name: str, value: object) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,java.lang.Object)"""
        return 'ToStringHelper'._wrap(super(_ToStringHelper, self).add(name, value))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.StandardSystemProperty
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.StandardSystemProperty as _StandardSystemProperty
_StandardSystemProperty = _StandardSystemProperty
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
 
class StandardSystemProperty():
    """com.google.common.base.StandardSystemProperty"""
 
    @staticmethod
    def _wrap(java_value: _StandardSystemProperty) -> 'StandardSystemProperty':
        return StandardSystemProperty(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StandardSystemProperty):
        """
        Dynamic initializer for StandardSystemProperty.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StandardSystemProperty__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StandardSystemProperty__wrapper":
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

    @overload
    def value(self) -> str:
        """public java.lang.String com.google.common.base.StandardSystemProperty.value()"""
        return str._wrap(super(StandardSystemProperty, self).value())

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
    def valueOf(name: str) -> 'StandardSystemProperty':
        """public static com.google.common.base.StandardSystemProperty com.google.common.base.StandardSystemProperty.valueOf(java.lang.String)"""
        return StandardSystemProperty._wrap(_StandardSystemProperty.valueOf(name))

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

    @overload
    def key(self) -> str:
        """public java.lang.String com.google.common.base.StandardSystemProperty.key()"""
        return str._wrap(super(StandardSystemProperty, self).key())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.StandardSystemProperty.toString()"""
        return str._wrap(super(StandardSystemProperty, self).toString())

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
    def values() -> List['StandardSystemProperty']:
        """public static com.google.common.base.StandardSystemProperty[] com.google.common.base.StandardSystemProperty.values()"""
        return List[StandardSystemProperty]._wrap(_StandardSystemProperty.values()) 
 
 
# CLASS: com.google.common.base.Utf8
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.base.Utf8 as _Utf8
_Utf8 = _Utf8
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Utf8():
    """com.google.common.base.Utf8"""
 
    @staticmethod
    def _wrap(java_value: _Utf8) -> 'Utf8':
        return Utf8(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Utf8):
        """
        Dynamic initializer for Utf8.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Utf8__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Utf8__wrapper":
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
    def isWellFormed(bytes: bytes) -> bool:
        """public static boolean com.google.common.base.Utf8.isWellFormed(byte[])"""
        return bool._wrap(_Utf8.isWellFormed(bytes))

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
    def isWellFormed(bytes: bytes, off: int, len: int) -> bool:
        """public static boolean com.google.common.base.Utf8.isWellFormed(byte[],int,int)"""
        return bool._wrap(_Utf8.isWellFormed(bytes, _int.valueOf(off), _int.valueOf(len)))

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
    def encodedLength(sequence: 'CharSequence') -> int:
        """public static int com.google.common.base.Utf8.encodedLength(java.lang.CharSequence)"""
        return int._wrap(_Utf8.encodedLength(sequence))

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
 
 
# CLASS: com.google.common.base.FinalizableSoftReference
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.FinalizableReference as _FinalizableReference
_FinalizableReference = _FinalizableReference
from builtins import object
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import java.lang.ref.SoftReference as _SoftReference
_SoftReference = _SoftReference
import com.google.common.base.FinalizableSoftReference as _FinalizableSoftReference
_FinalizableSoftReference = _FinalizableSoftReference
import java.lang.ref.Reference as _Reference
_Reference = _Reference
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FinalizableSoftReference():
    """com.google.common.base.FinalizableSoftReference"""
 
    @staticmethod
    def _wrap(java_value: _FinalizableSoftReference) -> 'FinalizableSoftReference':
        return FinalizableSoftReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FinalizableSoftReference):
        """
        Dynamic initializer for FinalizableSoftReference.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FinalizableSoftReference__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FinalizableSoftReference__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEnqueued(self) -> bool:
        """public boolean java.lang.ref.Reference.isEnqueued()"""
        return bool._wrap(super(Reference, self).isEnqueued())

    @override
    @overload
    def enqueue(self) -> bool:
        """public boolean java.lang.ref.Reference.enqueue()"""
        return bool._wrap(super(Reference, self).enqueue())

    @overload
    def refersTo(self, arg0: object) -> bool:
        """public final boolean java.lang.ref.Reference.refersTo(T)"""
        return bool._wrap(super(_Reference, self).refersTo(arg0))

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
    def get(self) -> object:
        """public T java.lang.ref.SoftReference.get()"""
        return object._wrap(super(SoftReference, self).get())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def clear(self):
        """public void java.lang.ref.Reference.clear()"""
        super(Reference, self).clear()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def reachabilityFence(arg0: object):
        """public static void java.lang.ref.Reference.reachabilityFence(java.lang.Object)"""
        _Reference.reachabilityFence(arg0)

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

    @abstractmethod
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass

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
 
 
# CLASS: com.google.common.base.Charsets
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.google.common.base.Charsets as _Charsets
_Charsets = _Charsets
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Charsets():
    """com.google.common.base.Charsets"""
 
    @staticmethod
    def _wrap(java_value: _Charsets) -> 'Charsets':
        return Charsets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Charsets):
        """
        Dynamic initializer for Charsets.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Charsets__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Charsets__wrapper":
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
 
 
# CLASS: com.google.common.base.Objects
from builtins import str
from pyquantum_helper import override
import com.google.common.base.Objects as _Objects
_Objects = _Objects
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Objects():
    """com.google.common.base.Objects"""
 
    @staticmethod
    def _wrap(java_value: _Objects) -> 'Objects':
        return Objects(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Objects):
        """
        Dynamic initializer for Objects.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Objects__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Objects__wrapper":
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
    def equal(a: object, b: object) -> bool:
        """public static boolean com.google.common.base.Objects.equal(java.lang.Object,java.lang.Object)"""
        return bool._wrap(_Objects.equal(a, b))

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
    def hashCode(*objects: object) -> int:
        """public static int com.google.common.base.Objects.hashCode(java.lang.Object...)"""
        return int._wrap(_Objects.hashCode(objects))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.Ascii
from builtins import str
import java.lang.Character as _char
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.google.common.base.Ascii as _Ascii
_Ascii = _Ascii
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Ascii():
    """com.google.common.base.Ascii"""
 
    @staticmethod
    def _wrap(java_value: _Ascii) -> 'Ascii':
        return Ascii(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ascii):
        """
        Dynamic initializer for Ascii.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ascii__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ascii__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toUpperCase(string: str) -> str:
        """public static java.lang.String com.google.common.base.Ascii.toUpperCase(java.lang.String)"""
        return str._wrap(_Ascii.toUpperCase(string))

    @staticmethod
    @overload
    def isUpperCase(c: str) -> bool:
        """public static boolean com.google.common.base.Ascii.isUpperCase(char)"""
        return bool._wrap(_Ascii.isUpperCase(_char.valueOf(c)))

    @staticmethod
    @overload
    def toLowerCase(string: str) -> str:
        """public static java.lang.String com.google.common.base.Ascii.toLowerCase(java.lang.String)"""
        return str._wrap(_Ascii.toLowerCase(string))

    @staticmethod
    @overload
    def toLowerCase(chars: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Ascii.toLowerCase(java.lang.CharSequence)"""
        return str._wrap(_Ascii.toLowerCase(chars))

    @staticmethod
    @overload
    def isLowerCase(c: str) -> bool:
        """public static boolean com.google.common.base.Ascii.isLowerCase(char)"""
        return bool._wrap(_Ascii.isLowerCase(_char.valueOf(c)))

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
    def equalsIgnoreCase(s1: 'CharSequence', s2: 'CharSequence') -> bool:
        """public static boolean com.google.common.base.Ascii.equalsIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_Ascii.equalsIgnoreCase(s1, s2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toUpperCase(c: str) -> str:
        """public static char com.google.common.base.Ascii.toUpperCase(char)"""
        return str._wrap(_Ascii.toUpperCase(_char.valueOf(c)))

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
    def truncate(seq: 'CharSequence', maxLength: int, truncationIndicator: str) -> str:
        """public static java.lang.String com.google.common.base.Ascii.truncate(java.lang.CharSequence,int,java.lang.String)"""
        return str._wrap(_Ascii.truncate(seq, _int.valueOf(maxLength), truncationIndicator))

    @staticmethod
    @overload
    def toUpperCase(chars: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Ascii.toUpperCase(java.lang.CharSequence)"""
        return str._wrap(_Ascii.toUpperCase(chars))

    @staticmethod
    @overload
    def toLowerCase(c: str) -> str:
        """public static char com.google.common.base.Ascii.toLowerCase(char)"""
        return str._wrap(_Ascii.toLowerCase(_char.valueOf(c)))

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
 
 
# CLASS: com.google.common.base.Verify
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.base.Verify as _Verify
_Verify = _Verify
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Verify():
    """com.google.common.base.Verify"""
 
    @staticmethod
    def _wrap(java_value: _Verify) -> 'Verify':
        return Verify(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Verify):
        """
        Dynamic initializer for Verify.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Verify__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Verify__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, p1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def verify(expression: bool):
        """public static void com.google.common.base.Verify.verify(boolean)"""
        _Verify.verify(_boolean.valueOf(expression))

    @staticmethod
    @overload
    def verifyNotNull(reference: object) -> object:
        """public static <T> T com.google.common.base.Verify.verifyNotNull(T)"""
        return object._wrap(_Verify.verifyNotNull(reference))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,java.lang.Object)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, p1, p2)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,long)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, p1, _long.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,long)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _long.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, *errorMessageArgs: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object...)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, errorMessageArgs)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,char)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _char.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,char)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, p1, _char.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,long)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _long.valueOf(p2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,int)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, p1, _int.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,java.lang.Object)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), p2)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,long)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _long.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,int)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), _int.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,char)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _char.valueOf(p2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,int)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _int.valueOf(p2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,java.lang.Object)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1), p2)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,int)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), _int.valueOf(p2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,char)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _int.valueOf(p1), _char.valueOf(p2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def verifyNotNull(reference: object, errorMessageTemplate: str, *errorMessageArgs: object) -> object:
        """public static <T> T com.google.common.base.Verify.verifyNotNull(T,java.lang.String,java.lang.Object...)"""
        return object._wrap(_Verify.verifyNotNull(reference, errorMessageTemplate, errorMessageArgs))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,java.lang.Object)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _char.valueOf(p1), p2)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3, p4)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long)"""
        _Verify.verify(_boolean.valueOf(expression), errorMessageTemplate, _long.valueOf(p1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.Strings
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.String as _string
import java.lang.Integer as _int
import com.google.common.base.Strings as _Strings
_Strings = _Strings
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Strings():
    """com.google.common.base.Strings"""
 
    @staticmethod
    def _wrap(java_value: _Strings) -> 'Strings':
        return Strings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Strings):
        """
        Dynamic initializer for Strings.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Strings__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Strings__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def commonPrefix(a: 'CharSequence', b: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Strings.commonPrefix(java.lang.CharSequence,java.lang.CharSequence)"""
        return str._wrap(_Strings.commonPrefix(a, b))

    @staticmethod
    @overload
    def emptyToNull(string: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.emptyToNull(java.lang.String)"""
        return str._wrap(_Strings.emptyToNull(string))

    @staticmethod
    @overload
    def padStart(string: str, minLength: int, padChar: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.padStart(java.lang.String,int,char)"""
        return str._wrap(_Strings.padStart(string, _int.valueOf(minLength), _char.valueOf(padChar)))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def repeat(string: str, count: int) -> str:
        """public static java.lang.String com.google.common.base.Strings.repeat(java.lang.String,int)"""
        return str._wrap(_Strings.repeat(string, _int.valueOf(count)))

    @staticmethod
    @overload
    def lenientFormat(template: str, *args: object) -> str:
        """public static java.lang.String com.google.common.base.Strings.lenientFormat(java.lang.String,java.lang.Object...)"""
        return str._wrap(_Strings.lenientFormat(template, args))

    @staticmethod
    @overload
    def isNullOrEmpty(string: str) -> bool:
        """public static boolean com.google.common.base.Strings.isNullOrEmpty(java.lang.String)"""
        return bool._wrap(_Strings.isNullOrEmpty(string))

    @staticmethod
    @overload
    def padEnd(string: str, minLength: int, padChar: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.padEnd(java.lang.String,int,char)"""
        return str._wrap(_Strings.padEnd(string, _int.valueOf(minLength), _char.valueOf(padChar)))

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
    def nullToEmpty(string: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.nullToEmpty(java.lang.String)"""
        return str._wrap(_Strings.nullToEmpty(string))

    @staticmethod
    @overload
    def commonSuffix(a: 'CharSequence', b: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Strings.commonSuffix(java.lang.CharSequence,java.lang.CharSequence)"""
        return str._wrap(_Strings.commonSuffix(a, b))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.Throwables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import com.google.common.base.Throwables as _Throwables
_Throwables = _Throwables
import java.lang.RuntimeException as _RuntimeException
_RuntimeException = _RuntimeException
import java.lang.Integer as _int
import java.lang.RuntimeException as RuntimeException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Throwables():
    """com.google.common.base.Throwables"""
 
    @staticmethod
    def _wrap(java_value: _Throwables) -> 'Throwables':
        return Throwables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Throwables):
        """
        Dynamic initializer for Throwables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Throwables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Throwables__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lazyStackTrace(throwable: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.StackTraceElement> com.google.common.base.Throwables.lazyStackTrace(java.lang.Throwable)"""
        return List._wrap(_Throwables.lazyStackTrace(throwable))

    @staticmethod
    @overload
    def throwIfInstanceOf(throwable: 'Throwable', declaredType: 'Class'):
        """public static <X extends java.lang.Throwable> void com.google.common.base.Throwables.throwIfInstanceOf(java.lang.Throwable,java.lang.Class<X>) throws X"""
        _Throwables.throwIfInstanceOf(throwable, declaredType)

    @staticmethod
    @overload
    def lazyStackTraceIsLazy() -> bool:
        """public static boolean com.google.common.base.Throwables.lazyStackTraceIsLazy()"""
        return bool._wrap(_Throwables.lazyStackTraceIsLazy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def propagate(throwable: 'Throwable') -> 'RuntimeException':
        """public static java.lang.RuntimeException com.google.common.base.Throwables.propagate(java.lang.Throwable)"""
        return RuntimeException._wrap(_Throwables.propagate(throwable))

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
    def propagateIfPossible(throwable: 'Throwable', declaredType: 'Class'):
        """public static <X extends java.lang.Throwable> void com.google.common.base.Throwables.propagateIfPossible(java.lang.Throwable,java.lang.Class<X>) throws X"""
        _Throwables.propagateIfPossible(throwable, declaredType)

    @staticmethod
    @overload
    def getStackTraceAsString(throwable: 'Throwable') -> str:
        """public static java.lang.String com.google.common.base.Throwables.getStackTraceAsString(java.lang.Throwable)"""
        return str._wrap(_Throwables.getStackTraceAsString(throwable))

    @staticmethod
    @overload
    def propagateIfPossible(throwable: 'Throwable'):
        """public static void com.google.common.base.Throwables.propagateIfPossible(java.lang.Throwable)"""
        _Throwables.propagateIfPossible(throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def propagateIfInstanceOf(throwable: 'Throwable', declaredType: 'Class'):
        """public static <X extends java.lang.Throwable> void com.google.common.base.Throwables.propagateIfInstanceOf(java.lang.Throwable,java.lang.Class<X>) throws X"""
        _Throwables.propagateIfInstanceOf(throwable, declaredType)

    @staticmethod
    @overload
    def getRootCause(throwable: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable com.google.common.base.Throwables.getRootCause(java.lang.Throwable)"""
        return Throwable._wrap(_Throwables.getRootCause(throwable))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def propagateIfPossible(throwable: 'Throwable', declaredType1: 'Class', declaredType2: 'Class'):
        """public static <X1 extends java.lang.Throwable,X2 extends java.lang.Throwable> void com.google.common.base.Throwables.propagateIfPossible(java.lang.Throwable,java.lang.Class<X1>,java.lang.Class<X2>) throws X1,X2"""
        _Throwables.propagateIfPossible(throwable, declaredType1, declaredType2)

    @staticmethod
    @overload
    def getCausalChain(throwable: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.Throwable> com.google.common.base.Throwables.getCausalChain(java.lang.Throwable)"""
        return List._wrap(_Throwables.getCausalChain(throwable))

    @staticmethod
    @overload
    def getCauseAs(throwable: 'Throwable', expectedCauseType: 'Class') -> 'Throwable':
        """public static <X extends java.lang.Throwable> X com.google.common.base.Throwables.getCauseAs(java.lang.Throwable,java.lang.Class<X>)"""
        return Throwable._wrap(_Throwables.getCauseAs(throwable, expectedCauseType))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def throwIfUnchecked(throwable: 'Throwable'):
        """public static void com.google.common.base.Throwables.throwIfUnchecked(java.lang.Throwable)"""
        _Throwables.throwIfUnchecked(throwable)

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
 
 
# CLASS: com.google.common.base.Supplier
import com.google.common.base.Supplier as _Supplier
_Supplier = _Supplier
from abc import abstractmethod, ABC
 
class Supplier():
    """com.google.common.base.Supplier"""
 
    @staticmethod
    def _wrap(java_value: _Supplier) -> 'Supplier':
        return Supplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Supplier):
        """
        Dynamic initializer for Supplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Supplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Supplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract T com.google.common.base.Supplier.get()"""
        pass 
 
 
# CLASS: com.google.common.base.Splitter$MapSplitter
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.base.Splitter as _Splitter_MapSplitter
_MapSplitter = _Splitter_MapSplitter.MapSplitter
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapSplitter():
    """com.google.common.base.Splitter.MapSplitter"""
 
    @staticmethod
    def _wrap(java_value: _MapSplitter) -> 'MapSplitter':
        return MapSplitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapSplitter):
        """
        Dynamic initializer for MapSplitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapSplitter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapSplitter__wrapper":
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
    def split(self, sequence: 'CharSequence') -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> com.google.common.base.Splitter$MapSplitter.split(java.lang.CharSequence)"""
        return 'Map'._wrap(super(_MapSplitter, self).split(sequence))

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
 
 
# CLASS: com.google.common.base.Splitter
from builtins import str
import com.google.common.base.Splitter as _Splitter
_Splitter = _Splitter
import java.lang.CharSequence as CharSequence
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import com.google.common.base.Splitter as _Splitter_MapSplitter
_MapSplitter = _Splitter_MapSplitter.MapSplitter
import java.util.regex.Pattern as Pattern
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Splitter():
    """com.google.common.base.Splitter"""
 
    @staticmethod
    def _wrap(java_value: _Splitter) -> 'Splitter':
        return Splitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Splitter):
        """
        Dynamic initializer for Splitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Splitter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Splitter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def fixedLength(length: int) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.fixedLength(int)"""
        return Splitter._wrap(_Splitter.fixedLength(_int.valueOf(length)))

    @staticmethod
    @overload
    def on(separator: str) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(java.lang.String)"""
        return Splitter._wrap(_Splitter.on(separator))

    @overload
    def withKeyValueSeparator(self, separator: str) -> 'MapSplitter':
        """public com.google.common.base.Splitter$MapSplitter com.google.common.base.Splitter.withKeyValueSeparator(char)"""
        return 'MapSplitter'._wrap(super(_Splitter, self).withKeyValueSeparator(_char.valueOf(separator)))

    @overload
    def trimResults(self, trimmer: 'CharMatcher') -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.trimResults(com.google.common.base.CharMatcher)"""
        return 'Splitter'._wrap(super(_Splitter, self).trimResults(trimmer))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def trimResults(self) -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.trimResults()"""
        return 'Splitter'._wrap(super(Splitter, self).trimResults())

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
    def splitToList(self, sequence: 'CharSequence') -> 'List':
        """public java.util.List<java.lang.String> com.google.common.base.Splitter.splitToList(java.lang.CharSequence)"""
        return 'List'._wrap(super(_Splitter, self).splitToList(sequence))

    @overload
    def withKeyValueSeparator(self, separator: str) -> 'MapSplitter':
        """public com.google.common.base.Splitter$MapSplitter com.google.common.base.Splitter.withKeyValueSeparator(java.lang.String)"""
        return 'MapSplitter'._wrap(super(_Splitter, self).withKeyValueSeparator(separator))

    @overload
    def limit(self, maxItems: int) -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.limit(int)"""
        return 'Splitter'._wrap(super(_Splitter, self).limit(_int.valueOf(maxItems)))

    @staticmethod
    @overload
    def on(separatorPattern: 'Pattern') -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(java.util.regex.Pattern)"""
        return Splitter._wrap(_Splitter.on(separatorPattern))

    @staticmethod
    @overload
    def onPattern(separatorPattern: str) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.onPattern(java.lang.String)"""
        return Splitter._wrap(_Splitter.onPattern(separatorPattern))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def on(separator: str) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(char)"""
        return Splitter._wrap(_Splitter.on(_char.valueOf(separator)))

    @overload
    def omitEmptyStrings(self) -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.omitEmptyStrings()"""
        return 'Splitter'._wrap(super(Splitter, self).omitEmptyStrings())

    @overload
    def withKeyValueSeparator(self, keyValueSplitter: 'Splitter') -> 'MapSplitter':
        """public com.google.common.base.Splitter$MapSplitter com.google.common.base.Splitter.withKeyValueSeparator(com.google.common.base.Splitter)"""
        return 'MapSplitter'._wrap(super(_Splitter, self).withKeyValueSeparator(keyValueSplitter))

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

    @overload
    def splitToStream(self, sequence: 'CharSequence') -> 'Stream':
        """public java.util.stream.Stream<java.lang.String> com.google.common.base.Splitter.splitToStream(java.lang.CharSequence)"""
        return 'Stream'._wrap(super(_Splitter, self).splitToStream(sequence))

    @staticmethod
    @overload
    def on(separatorMatcher: 'CharMatcher') -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(com.google.common.base.CharMatcher)"""
        return Splitter._wrap(_Splitter.on(separatorMatcher))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def split(self, sequence: 'CharSequence') -> 'Iterable':
        """public java.lang.Iterable<java.lang.String> com.google.common.base.Splitter.split(java.lang.CharSequence)"""
        return 'Iterable'._wrap(super(_Splitter, self).split(sequence))

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
 
 
# CLASS: com.google.common.base.Joiner
from builtins import str
import java.lang.Character as _char
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Appendable as _Appendable
_Appendable = _Appendable
import java.lang.Iterable as Iterable
import com.google.common.base.Joiner as _Joiner
_Joiner = _Joiner
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
import java.lang.Appendable as Appendable
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
import com.google.common.base.Joiner as _Joiner_MapJoiner
_MapJoiner = _Joiner_MapJoiner.MapJoiner
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Joiner():
    """com.google.common.base.Joiner"""
 
    @staticmethod
    def _wrap(java_value: _Joiner) -> 'Joiner':
        return Joiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Joiner):
        """
        Dynamic initializer for Joiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Joiner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Joiner__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def appendTo(self, builder: 'StringBuilder', parts: 'Iterable') -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.lang.Iterable<?>)"""
        return 'StringBuilder'._wrap(super(_Joiner, self).appendTo(builder, parts))

    @overload
    def useForNull(self, nullText: str) -> 'Joiner':
        """public com.google.common.base.Joiner com.google.common.base.Joiner.useForNull(java.lang.String)"""
        return 'Joiner'._wrap(super(_Joiner, self).useForNull(nullText))

    @overload
    def withKeyValueSeparator(self, keyValueSeparator: str) -> 'MapJoiner':
        """public com.google.common.base.Joiner$MapJoiner com.google.common.base.Joiner.withKeyValueSeparator(char)"""
        return 'MapJoiner'._wrap(super(_Joiner, self).withKeyValueSeparator(_char.valueOf(keyValueSeparator)))

    @overload
    def join(self, first: object, second: object, *rest: object) -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.lang.Object,java.lang.Object,java.lang.Object...)"""
        return str._wrap(super(_Joiner, self).join(first, second, rest))

    @overload
    def appendTo(self, appendable: 'Appendable', first: object, second: object, *rest: object) -> 'Appendable':
        """public final <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.lang.Object,java.lang.Object,java.lang.Object...) throws java.io.IOException"""
        return 'Appendable'._wrap(super(_Joiner, self).appendTo(appendable, first, second, rest))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def join(self, parts: 'Object') -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.lang.Object[])"""
        return str._wrap(super(_Joiner, self).join(parts))

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Iterator') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.util.Iterator<?>) throws java.io.IOException"""
        return 'Appendable'._wrap(super(_Joiner, self).appendTo(appendable, parts))

    @overload
    def appendTo(self, builder: 'StringBuilder', parts: 'Iterator') -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.util.Iterator<?>)"""
        return 'StringBuilder'._wrap(super(_Joiner, self).appendTo(builder, parts))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Iterable') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.lang.Iterable<?>) throws java.io.IOException"""
        return 'Appendable'._wrap(super(_Joiner, self).appendTo(appendable, parts))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def appendTo(self, builder: 'StringBuilder', first: object, second: object, *rest: object) -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.lang.Object,java.lang.Object,java.lang.Object...)"""
        return 'StringBuilder'._wrap(super(_Joiner, self).appendTo(builder, first, second, rest))

    @overload
    def join(self, parts: 'Iterable') -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.lang.Iterable<?>)"""
        return str._wrap(super(_Joiner, self).join(parts))

    @overload
    def skipNulls(self) -> 'Joiner':
        """public com.google.common.base.Joiner com.google.common.base.Joiner.skipNulls()"""
        return 'Joiner'._wrap(super(Joiner, self).skipNulls())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def join(self, parts: 'Iterator') -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.util.Iterator<?>)"""
        return str._wrap(super(_Joiner, self).join(parts))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def appendTo(self, builder: 'StringBuilder', parts: 'Object') -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.lang.Object[])"""
        return 'StringBuilder'._wrap(super(_Joiner, self).appendTo(builder, parts))

    @staticmethod
    @overload
    def on(separator: str) -> 'Joiner':
        """public static com.google.common.base.Joiner com.google.common.base.Joiner.on(java.lang.String)"""
        return Joiner._wrap(_Joiner.on(separator))

    @staticmethod
    @overload
    def on(separator: str) -> 'Joiner':
        """public static com.google.common.base.Joiner com.google.common.base.Joiner.on(char)"""
        return Joiner._wrap(_Joiner.on(_char.valueOf(separator)))

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

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Object') -> 'Appendable':
        """public final <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.lang.Object[]) throws java.io.IOException"""
        return 'Appendable'._wrap(super(_Joiner, self).appendTo(appendable, parts))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def withKeyValueSeparator(self, keyValueSeparator: str) -> 'MapJoiner':
        """public com.google.common.base.Joiner$MapJoiner com.google.common.base.Joiner.withKeyValueSeparator(java.lang.String)"""
        return 'MapJoiner'._wrap(super(_Joiner, self).withKeyValueSeparator(keyValueSeparator))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.Predicates
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import com.google.common.base.Predicates as _Predicates
_Predicates = _Predicates
import com.google.common.base.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.regex.Pattern as Pattern
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Predicates():
    """com.google.common.base.Predicates"""
 
    @staticmethod
    def _wrap(java_value: _Predicates) -> 'Predicates':
        return Predicates(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Predicates):
        """
        Dynamic initializer for Predicates.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Predicates__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Predicates__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def containsPattern(pattern: str) -> 'Predicate':
        """public static com.google.common.base.Predicate<java.lang.CharSequence> com.google.common.base.Predicates.containsPattern(java.lang.String)"""
        return Predicate._wrap(_Predicates.containsPattern(pattern))

    @staticmethod
    @overload
    def and(*components: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.and(com.google.common.base.Predicate<? super T>...)"""
        return Predicate._wrap(_Predicates.and(components))

    @staticmethod
    @overload
    def subtypeOf(clazz: 'Class') -> 'Predicate':
        """public static com.google.common.base.Predicate<java.lang.Class<?>> com.google.common.base.Predicates.subtypeOf(java.lang.Class<?>)"""
        return Predicate._wrap(_Predicates.subtypeOf(clazz))

    @staticmethod
    @overload
    def in(target: 'Collection') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.in(java.util.Collection<? extends T>)"""
        return Predicate._wrap(_Predicates.in(target))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def compose(predicate: 'Predicate', function: 'Function') -> 'Predicate':
        """public static <A,B> com.google.common.base.Predicate<A> com.google.common.base.Predicates.compose(com.google.common.base.Predicate<B>,com.google.common.base.Function<A, ? extends B>)"""
        return Predicate._wrap(_Predicates.compose(predicate, function))

    @staticmethod
    @overload
    def notNull() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.notNull()"""
        return Predicate._wrap(_Predicates.notNull())

    @staticmethod
    @overload
    def and(components: 'Iterable') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.and(java.lang.Iterable<? extends com.google.common.base.Predicate<? super T>>)"""
        return Predicate._wrap(_Predicates.and(components))

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
    def not(predicate: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.not(com.google.common.base.Predicate<T>)"""
        return Predicate._wrap(_Predicates.not(predicate))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def or(components: 'Iterable') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.or(java.lang.Iterable<? extends com.google.common.base.Predicate<? super T>>)"""
        return Predicate._wrap(_Predicates.or(components))

    @staticmethod
    @overload
    def alwaysTrue() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.alwaysTrue()"""
        return Predicate._wrap(_Predicates.alwaysTrue())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def or(*components: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.or(com.google.common.base.Predicate<? super T>...)"""
        return Predicate._wrap(_Predicates.or(components))

    @staticmethod
    @overload
    def and(first: 'Predicate', second: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.and(com.google.common.base.Predicate<? super T>,com.google.common.base.Predicate<? super T>)"""
        return Predicate._wrap(_Predicates.and(first, second))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def isNull() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.isNull()"""
        return Predicate._wrap(_Predicates.isNull())

    @staticmethod
    @overload
    def or(first: 'Predicate', second: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.or(com.google.common.base.Predicate<? super T>,com.google.common.base.Predicate<? super T>)"""
        return Predicate._wrap(_Predicates.or(first, second))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def alwaysFalse() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.alwaysFalse()"""
        return Predicate._wrap(_Predicates.alwaysFalse())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def contains(pattern: 'Pattern') -> 'Predicate':
        """public static com.google.common.base.Predicate<java.lang.CharSequence> com.google.common.base.Predicates.contains(java.util.regex.Pattern)"""
        return Predicate._wrap(_Predicates.contains(pattern))

    @staticmethod
    @overload
    def equalTo(target: object) -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.equalTo(T)"""
        return Predicate._wrap(_Predicates.equalTo(target))

    @staticmethod
    @overload
    def instanceOf(clazz: 'Class') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.instanceOf(java.lang.Class<?>)"""
        return Predicate._wrap(_Predicates.instanceOf(clazz))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.CaseFormat
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.base.CaseFormat as _CaseFormat
_CaseFormat = _CaseFormat
from typing import List
import com.google.common.base.Converter as _Converter
_Converter = _Converter
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
 
class CaseFormat():
    """com.google.common.base.CaseFormat"""
 
    @staticmethod
    def _wrap(java_value: _CaseFormat) -> 'CaseFormat':
        return CaseFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CaseFormat):
        """
        Dynamic initializer for CaseFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CaseFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CaseFormat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def converterTo(self, targetFormat: 'CaseFormat') -> 'Converter':
        """public com.google.common.base.Converter<java.lang.String, java.lang.String> com.google.common.base.CaseFormat.converterTo(com.google.common.base.CaseFormat)"""
        return 'Converter'._wrap(super(_CaseFormat, self).converterTo(targetFormat))

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
    def values() -> List['CaseFormat']:
        """public static com.google.common.base.CaseFormat[] com.google.common.base.CaseFormat.values()"""
        return List[CaseFormat]._wrap(_CaseFormat.values())

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
    def to(self, format: 'CaseFormat', str: str) -> str:
        """public final java.lang.String com.google.common.base.CaseFormat.to(com.google.common.base.CaseFormat,java.lang.String)"""
        return str._wrap(super(_CaseFormat, self).to(format, str))

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
    def valueOf(name: str) -> 'CaseFormat':
        """public static com.google.common.base.CaseFormat com.google.common.base.CaseFormat.valueOf(java.lang.String)"""
        return CaseFormat._wrap(_CaseFormat.valueOf(name)) 
 
 
# CLASS: com.google.common.base.Suppliers
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import com.google.common.base.Function as _Function
_Function = _Function
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.base.Supplier as _Supplier
_Supplier = _Supplier
import com.google.common.base.Suppliers as _Suppliers
_Suppliers = _Suppliers
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Suppliers():
    """com.google.common.base.Suppliers"""
 
    @staticmethod
    def _wrap(java_value: _Suppliers) -> 'Suppliers':
        return Suppliers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Suppliers):
        """
        Dynamic initializer for Suppliers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Suppliers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Suppliers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def memoizeWithExpiration(delegate: 'Supplier', duration: int, unit: 'TimeUnit') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.memoizeWithExpiration(com.google.common.base.Supplier<T>,long,java.util.concurrent.TimeUnit)"""
        return Supplier._wrap(_Suppliers.memoizeWithExpiration(delegate, _long.valueOf(duration), unit))

    @staticmethod
    @overload
    def memoizeWithExpiration(delegate: 'Supplier', duration: 'Duration') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.memoizeWithExpiration(com.google.common.base.Supplier<T>,java.time.Duration)"""
        return Supplier._wrap(_Suppliers.memoizeWithExpiration(delegate, duration))

    @staticmethod
    @overload
    def synchronizedSupplier(delegate: 'Supplier') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.synchronizedSupplier(com.google.common.base.Supplier<T>)"""
        return Supplier._wrap(_Suppliers.synchronizedSupplier(delegate))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def supplierFunction() -> 'Function':
        """public static <T> com.google.common.base.Function<com.google.common.base.Supplier<T>, T> com.google.common.base.Suppliers.supplierFunction()"""
        return Function._wrap(_Suppliers.supplierFunction())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ofInstance(instance: object) -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.ofInstance(T)"""
        return Supplier._wrap(_Suppliers.ofInstance(instance))

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
    def memoize(delegate: 'Supplier') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.memoize(com.google.common.base.Supplier<T>)"""
        return Supplier._wrap(_Suppliers.memoize(delegate))

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
    def compose(function: 'Function', supplier: 'Supplier') -> 'Supplier':
        """public static <F,T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.compose(com.google.common.base.Function<? super F, T>,com.google.common.base.Supplier<F>)"""
        return Supplier._wrap(_Suppliers.compose(function, supplier))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.FinalizableReference
import com.google.common.base.FinalizableReference as _FinalizableReference
_FinalizableReference = _FinalizableReference
from abc import abstractmethod, ABC
 
class FinalizableReference():
    """com.google.common.base.FinalizableReference"""
 
    @staticmethod
    def _wrap(java_value: _FinalizableReference) -> 'FinalizableReference':
        return FinalizableReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FinalizableReference):
        """
        Dynamic initializer for FinalizableReference.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FinalizableReference__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FinalizableReference__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass 
 
 
# CLASS: com.google.common.base.FinalizableWeakReference
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.FinalizableReference as _FinalizableReference
_FinalizableReference = _FinalizableReference
from builtins import object
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import java.lang.ref.Reference as _Reference
_Reference = _Reference
from builtins import bool
import java.lang.Long as _long
import com.google.common.base.FinalizableWeakReference as _FinalizableWeakReference
_FinalizableWeakReference = _FinalizableWeakReference
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FinalizableWeakReference():
    """com.google.common.base.FinalizableWeakReference"""
 
    @staticmethod
    def _wrap(java_value: _FinalizableWeakReference) -> 'FinalizableWeakReference':
        return FinalizableWeakReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FinalizableWeakReference):
        """
        Dynamic initializer for FinalizableWeakReference.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FinalizableWeakReference__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FinalizableWeakReference__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEnqueued(self) -> bool:
        """public boolean java.lang.ref.Reference.isEnqueued()"""
        return bool._wrap(super(Reference, self).isEnqueued())

    @override
    @overload
    def enqueue(self) -> bool:
        """public boolean java.lang.ref.Reference.enqueue()"""
        return bool._wrap(super(Reference, self).enqueue())

    @overload
    def refersTo(self, arg0: object) -> bool:
        """public final boolean java.lang.ref.Reference.refersTo(T)"""
        return bool._wrap(super(_Reference, self).refersTo(arg0))

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
    def clear(self):
        """public void java.lang.ref.Reference.clear()"""
        super(Reference, self).clear()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def reachabilityFence(arg0: object):
        """public static void java.lang.ref.Reference.reachabilityFence(java.lang.Object)"""
        _Reference.reachabilityFence(arg0)

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

    @abstractmethod
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public T java.lang.ref.Reference.get()"""
        return object._wrap(super(Reference, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.base.Functions as _Functions
_Functions = _Functions
import com.google.common.base.Function as _Function
_Function = _Function
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """com.google.common.base.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def forMap(map: 'Map', defaultValue: object) -> 'Function':
        """public static <K,V> com.google.common.base.Function<K, V> com.google.common.base.Functions.forMap(java.util.Map<K, ? extends V>,V)"""
        return Function._wrap(_Functions.forMap(map, defaultValue))

    @staticmethod
    @overload
    def toStringFunction() -> 'Function':
        """public static com.google.common.base.Function<java.lang.Object, java.lang.String> com.google.common.base.Functions.toStringFunction()"""
        return Function._wrap(_Functions.toStringFunction())

    @staticmethod
    @overload
    def constant(value: object) -> 'Function':
        """public static <E> com.google.common.base.Function<java.lang.Object, E> com.google.common.base.Functions.constant(E)"""
        return Function._wrap(_Functions.constant(value))

    @staticmethod
    @overload
    def compose(g: 'Function', f: 'Function') -> 'Function':
        """public static <A,B,C> com.google.common.base.Function<A, C> com.google.common.base.Functions.compose(com.google.common.base.Function<B, C>,com.google.common.base.Function<A, ? extends B>)"""
        return Function._wrap(_Functions.compose(g, f))

    @staticmethod
    @overload
    def forSupplier(supplier: 'Supplier') -> 'Function':
        """public static <F,T> com.google.common.base.Function<F, T> com.google.common.base.Functions.forSupplier(com.google.common.base.Supplier<T>)"""
        return Function._wrap(_Functions.forSupplier(supplier))

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
    def identity() -> 'Function':
        """public static <E> com.google.common.base.Function<E, E> com.google.common.base.Functions.identity()"""
        return Function._wrap(_Functions.identity())

    @staticmethod
    @overload
    def forPredicate(predicate: 'Predicate') -> 'Function':
        """public static <T> com.google.common.base.Function<T, java.lang.Boolean> com.google.common.base.Functions.forPredicate(com.google.common.base.Predicate<T>)"""
        return Function._wrap(_Functions.forPredicate(predicate))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def forMap(map: 'Map') -> 'Function':
        """public static <K,V> com.google.common.base.Function<K, V> com.google.common.base.Functions.forMap(java.util.Map<K, V>)"""
        return Function._wrap(_Functions.forMap(map))

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
 
 
# CLASS: com.google.common.base.Function
import com.google.common.base.Function as _Function
_Function = _Function
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class Function():
    """com.google.common.base.Function"""
 
    @staticmethod
    def _wrap(java_value: _Function) -> 'Function':
        return Function(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Function):
        """
        Dynamic initializer for Function.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Function__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Function__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Function.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def apply(self, input: object):
        """public abstract T com.google.common.base.Function.apply(F)"""
        pass 
 
 
# CLASS: com.google.common.base.Converter
from builtins import str
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Converter():
    """com.google.common.base.Converter"""
 
    @staticmethod
    def _wrap(java_value: _Converter) -> 'Converter':
        return Converter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Converter):
        """
        Dynamic initializer for Converter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Converter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Converter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def identity() -> 'Converter':
        """public static <T> com.google.common.base.Converter<T, T> com.google.common.base.Converter.identity()"""
        return Converter._wrap(_Converter.identity())

    @overload
    def apply(self, a: object) -> object:
        """public final B com.google.common.base.Converter.apply(A)"""
        return object._wrap(super(_Converter, self).apply(a))

    @overload
    def convertAll(self, fromIterable: 'Iterable') -> 'Iterable':
        """public java.lang.Iterable<B> com.google.common.base.Converter.convertAll(java.lang.Iterable<? extends A>)"""
        return 'Iterable'._wrap(super(_Converter, self).convertAll(fromIterable))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.base.Converter.equals(java.lang.Object)"""
        return bool._wrap(super(_Converter, self).equals(object))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @overload
    def convert(self, a: object) -> object:
        """public final B com.google.common.base.Converter.convert(A)"""
        return object._wrap(super(_Converter, self).convert(a))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reverse(self) -> 'Converter':
        """public com.google.common.base.Converter<B, A> com.google.common.base.Converter.reverse()"""
        return 'Converter'._wrap(super(Converter, self).reverse())

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

    @staticmethod
    @overload
    def from(forwardFunction: 'Function', backwardFunction: 'Function') -> 'Converter':
        """public static <A,B> com.google.common.base.Converter<A, B> com.google.common.base.Converter.from(com.google.common.base.Function<? super A, ? extends B>,com.google.common.base.Function<? super B, ? extends A>)"""
        return Converter._wrap(_Converter.from(forwardFunction, backwardFunction))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

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
    def andThen(self, secondConverter: 'Converter') -> 'Converter':
        """public final <C> com.google.common.base.Converter<A, C> com.google.common.base.Converter.andThen(com.google.common.base.Converter<B, C>)"""
        return 'Converter'._wrap(super(_Converter, self).andThen(secondConverter))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.Stopwatch
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import java.time.Duration as _Duration
_Duration = _Duration
import com.google.common.base.Stopwatch as _Stopwatch
_Stopwatch = _Stopwatch
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Stopwatch():
    """com.google.common.base.Stopwatch"""
 
    @staticmethod
    def _wrap(java_value: _Stopwatch) -> 'Stopwatch':
        return Stopwatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Stopwatch):
        """
        Dynamic initializer for Stopwatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Stopwatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Stopwatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def stop(self) -> 'Stopwatch':
        """public com.google.common.base.Stopwatch com.google.common.base.Stopwatch.stop()"""
        return 'Stopwatch'._wrap(super(Stopwatch, self).stop())

    @overload
    def elapsed(self, desiredUnit: 'TimeUnit') -> int:
        """public long com.google.common.base.Stopwatch.elapsed(java.util.concurrent.TimeUnit)"""
        return int._wrap(super(_Stopwatch, self).elapsed(desiredUnit))

    @staticmethod
    @overload
    def createUnstarted() -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createUnstarted()"""
        return Stopwatch._wrap(_Stopwatch.createUnstarted())

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
    def reset(self) -> 'Stopwatch':
        """public com.google.common.base.Stopwatch com.google.common.base.Stopwatch.reset()"""
        return 'Stopwatch'._wrap(super(Stopwatch, self).reset())

    @staticmethod
    @overload
    def createStarted(ticker: 'Ticker') -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createStarted(com.google.common.base.Ticker)"""
        return Stopwatch._wrap(_Stopwatch.createStarted(ticker))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def start(self) -> 'Stopwatch':
        """public com.google.common.base.Stopwatch com.google.common.base.Stopwatch.start()"""
        return 'Stopwatch'._wrap(super(Stopwatch, self).start())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.Stopwatch.toString()"""
        return str._wrap(super(Stopwatch, self).toString())

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
    def isRunning(self) -> bool:
        """public boolean com.google.common.base.Stopwatch.isRunning()"""
        return bool._wrap(super(Stopwatch, self).isRunning())

    @overload
    def elapsed(self) -> 'Duration':
        """public java.time.Duration com.google.common.base.Stopwatch.elapsed()"""
        return 'Duration'._wrap(super(Stopwatch, self).elapsed())

    @staticmethod
    @overload
    def createUnstarted(ticker: 'Ticker') -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createUnstarted(com.google.common.base.Ticker)"""
        return Stopwatch._wrap(_Stopwatch.createUnstarted(ticker))

    @staticmethod
    @overload
    def createStarted() -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createStarted()"""
        return Stopwatch._wrap(_Stopwatch.createStarted())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.MoreObjects
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.MoreObjects as _MoreObjects_ToStringHelper
_ToStringHelper = _MoreObjects_ToStringHelper.ToStringHelper
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.base.MoreObjects as _MoreObjects
_MoreObjects = _MoreObjects
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MoreObjects():
    """com.google.common.base.MoreObjects"""
 
    @staticmethod
    def _wrap(java_value: _MoreObjects) -> 'MoreObjects':
        return MoreObjects(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MoreObjects):
        """
        Dynamic initializer for MoreObjects.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MoreObjects__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MoreObjects__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toStringHelper(className: str) -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.String)"""
        return ToStringHelper._wrap(_MoreObjects.toStringHelper(className))

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
    def toStringHelper(clazz: 'Class') -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.Class<?>)"""
        return ToStringHelper._wrap(_MoreObjects.toStringHelper(clazz))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toStringHelper(self: object) -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.Object)"""
        return ToStringHelper._wrap(_MoreObjects.toStringHelper(self))

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
    def firstNonNull(first: object, second: object) -> object:
        """public static <T> T com.google.common.base.MoreObjects.firstNonNull(T,T)"""
        return object._wrap(_MoreObjects.firstNonNull(first, second))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.Optional
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.Optional as _Optional
_Optional = _Optional
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Optional as Optional
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
 
class Optional():
    """com.google.common.base.Optional"""
 
    @staticmethod
    def _wrap(java_value: _Optional) -> 'Optional':
        return Optional(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Optional):
        """
        Dynamic initializer for Optional.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Optional__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Optional__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toJavaUtil(googleOptional: 'Optional') -> 'Optional':
        """public static <T> java.util.Optional<T> com.google.common.base.Optional.toJavaUtil(com.google.common.base.Optional<T>)"""
        return Optional._wrap(_Optional.toJavaUtil(googleOptional))

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Optional.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String com.google.common.base.Optional.toString()"""
        pass

    @abstractmethod
    def or(self, secondChoice: 'Optional'):
        """public abstract com.google.common.base.Optional<T> com.google.common.base.Optional.or(com.google.common.base.Optional<? extends T>)"""
        pass

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

    @abstractmethod
    def isPresent(self, ):
        """public abstract boolean com.google.common.base.Optional.isPresent()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.base.Optional.hashCode()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def fromNullable(nullableReference: object) -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.fromNullable(T)"""
        return Optional._wrap(_Optional.fromNullable(nullableReference))

    @abstractmethod
    def or(self, supplier: 'Supplier'):
        """public abstract T com.google.common.base.Optional.or(com.google.common.base.Supplier<? extends T>)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def absent() -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.absent()"""
        return Optional._wrap(_Optional.absent())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def of(reference: object) -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.of(T)"""
        return Optional._wrap(_Optional.of(reference))

    @staticmethod
    @overload
    def fromJavaUtil(javaUtilOptional: 'Optional') -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.fromJavaUtil(java.util.Optional<T>)"""
        return Optional._wrap(_Optional.fromJavaUtil(javaUtilOptional))

    @abstractmethod
    def or(self, defaultValue: object):
        """public abstract T com.google.common.base.Optional.or(T)"""
        pass

    @staticmethod
    @overload
    def presentInstances(optionals: 'Iterable') -> 'Iterable':
        """public static <T> java.lang.Iterable<T> com.google.common.base.Optional.presentInstances(java.lang.Iterable<? extends com.google.common.base.Optional<? extends T>>)"""
        return Iterable._wrap(_Optional.presentInstances(optionals))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def get(self, ):
        """public abstract T com.google.common.base.Optional.get()"""
        pass

    @abstractmethod
    def transform(self, function: 'Function'):
        """public abstract <V> com.google.common.base.Optional<V> com.google.common.base.Optional.transform(com.google.common.base.Function<? super T, V>)"""
        pass

    @abstractmethod
    def orNull(self, ):
        """public abstract T com.google.common.base.Optional.orNull()"""
        pass

    @abstractmethod
    def asSet(self, ):
        """public abstract java.util.Set<T> com.google.common.base.Optional.asSet()"""
        pass

    @overload
    def toJavaUtil(self) -> 'Optional':
        """public java.util.Optional<T> com.google.common.base.Optional.toJavaUtil()"""
        return 'Optional'._wrap(super(Optional, self).toJavaUtil()) 
 
 
# CLASS: com.google.common.base.Equivalence
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.base.Predicate as _Predicate
_Predicate = _Predicate
import com.google.common.base.Equivalence as _Equivalence_Wrapper
_Wrapper = _Equivalence_Wrapper.Wrapper
import java.lang.Integer as _int
import java.util.function.BiPredicate as BiPredicate
import com.google.common.base.Equivalence as _Equivalence
_Equivalence = _Equivalence
import java.util.function.BiPredicate as _BiPredicate
_BiPredicate = _BiPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Equivalence():
    """com.google.common.base.Equivalence"""
 
    @staticmethod
    def _wrap(java_value: _Equivalence) -> 'Equivalence':
        return Equivalence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Equivalence):
        """
        Dynamic initializer for Equivalence.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Equivalence__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Equivalence__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def hash(self, t: object) -> int:
        """public final int com.google.common.base.Equivalence.hash(T)"""
        return int._wrap(super(_Equivalence, self).hash(t))

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
    def and(self, arg0: 'BiPredicate') -> 'BiPredicate':
        """public default java.util.function.BiPredicate<T, U> java.util.function.BiPredicate.and(java.util.function.BiPredicate<? super T, ? super U>)"""
        return 'BiPredicate'._wrap(super(_BiPredicate, self).and(arg0))

    @overload
    def test(self, t: object, u: object) -> bool:
        """public final boolean com.google.common.base.Equivalence.test(T,T)"""
        return bool._wrap(super(_Equivalence, self).test(t, u))

    @overload
    def pairwise(self) -> 'Equivalence':
        """public final <S extends T> com.google.common.base.Equivalence<java.lang.Iterable<S>> com.google.common.base.Equivalence.pairwise()"""
        return 'Equivalence'._wrap(super(Equivalence, self).pairwise())

    @overload
    def equivalentTo(self, target: object) -> 'Predicate':
        """public final com.google.common.base.Predicate<T> com.google.common.base.Equivalence.equivalentTo(T)"""
        return 'Predicate'._wrap(super(_Equivalence, self).equivalentTo(target))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def negate(self) -> 'BiPredicate':
        """public default java.util.function.BiPredicate<T, U> java.util.function.BiPredicate.negate()"""
        return 'BiPredicate'._wrap(super(BiPredicate, self).negate())

    @overload
    def onResultOf(self, function: 'Function') -> 'Equivalence':
        """public final <F> com.google.common.base.Equivalence<F> com.google.common.base.Equivalence.onResultOf(com.google.common.base.Function<? super F, ? extends T>)"""
        return 'Equivalence'._wrap(super(_Equivalence, self).onResultOf(function))

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
    def equals() -> 'Equivalence':
        """public static com.google.common.base.Equivalence<java.lang.Object> com.google.common.base.Equivalence.equals()"""
        return Equivalence._wrap(_Equivalence.equals())

    @overload
    def wrap(self, reference: object) -> 'Wrapper':
        """public final <S extends T> com.google.common.base.Equivalence$Wrapper<S> com.google.common.base.Equivalence.wrap(S)"""
        return 'Wrapper'._wrap(super(_Equivalence, self).wrap(reference))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def identity() -> 'Equivalence':
        """public static com.google.common.base.Equivalence<java.lang.Object> com.google.common.base.Equivalence.identity()"""
        return Equivalence._wrap(_Equivalence.identity())

    @overload
    def or(self, arg0: 'BiPredicate') -> 'BiPredicate':
        """public default java.util.function.BiPredicate<T, U> java.util.function.BiPredicate.or(java.util.function.BiPredicate<? super T, ? super U>)"""
        return 'BiPredicate'._wrap(super(_BiPredicate, self).or(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equivalent(self, a: object, b: object) -> bool:
        """public final boolean com.google.common.base.Equivalence.equivalent(T,T)"""
        return bool._wrap(super(_Equivalence, self).equivalent(a, b))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.base.FinalizablePhantomReference
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.FinalizableReference as _FinalizableReference
_FinalizableReference = _FinalizableReference
from builtins import object
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.ref.PhantomReference as _PhantomReference
_PhantomReference = _PhantomReference
import java.lang.Integer as _int
import java.lang.ref.Reference as _Reference
_Reference = _Reference
import com.google.common.base.FinalizablePhantomReference as _FinalizablePhantomReference
_FinalizablePhantomReference = _FinalizablePhantomReference
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FinalizablePhantomReference():
    """com.google.common.base.FinalizablePhantomReference"""
 
    @staticmethod
    def _wrap(java_value: _FinalizablePhantomReference) -> 'FinalizablePhantomReference':
        return FinalizablePhantomReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FinalizablePhantomReference):
        """
        Dynamic initializer for FinalizablePhantomReference.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FinalizablePhantomReference__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FinalizablePhantomReference__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEnqueued(self) -> bool:
        """public boolean java.lang.ref.Reference.isEnqueued()"""
        return bool._wrap(super(Reference, self).isEnqueued())

    @override
    @overload
    def enqueue(self) -> bool:
        """public boolean java.lang.ref.Reference.enqueue()"""
        return bool._wrap(super(Reference, self).enqueue())

    @overload
    def refersTo(self, arg0: object) -> bool:
        """public final boolean java.lang.ref.Reference.refersTo(T)"""
        return bool._wrap(super(_Reference, self).refersTo(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T java.lang.ref.PhantomReference.get()"""
        return object._wrap(super(PhantomReference, self).get())

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
    def clear(self):
        """public void java.lang.ref.Reference.clear()"""
        super(Reference, self).clear()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def reachabilityFence(arg0: object):
        """public static void java.lang.ref.Reference.reachabilityFence(java.lang.Object)"""
        _Reference.reachabilityFence(arg0)

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

    @abstractmethod
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass

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
 
 
# CLASS: com.google.common.base.Joiner$MapJoiner
from builtins import str
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Appendable as _Appendable
_Appendable = _Appendable
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Appendable as Appendable
import java.lang.String as _string
import java.lang.Integer as _int
import com.google.common.base.Joiner as _Joiner_MapJoiner
_MapJoiner = _Joiner_MapJoiner.MapJoiner
import java.lang.StringBuilder as StringBuilder
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapJoiner():
    """com.google.common.base.Joiner.MapJoiner"""
 
    @staticmethod
    def _wrap(java_value: _MapJoiner) -> 'MapJoiner':
        return MapJoiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapJoiner):
        """
        Dynamic initializer for MapJoiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapJoiner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapJoiner__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def appendTo(self, appendable: 'Appendable', entries: 'Iterable') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner$MapJoiner.appendTo(A,java.lang.Iterable<? extends java.util.Map$Entry<?, ?>>) throws java.io.IOException"""
        return 'Appendable'._wrap(super(_MapJoiner, self).appendTo(appendable, entries))

    @overload
    def useForNull(self, nullText: str) -> 'MapJoiner':
        """public com.google.common.base.Joiner$MapJoiner com.google.common.base.Joiner$MapJoiner.useForNull(java.lang.String)"""
        return 'MapJoiner'._wrap(super(_MapJoiner, self).useForNull(nullText))

    @overload
    def join(self, entries: 'Iterable') -> str:
        """public java.lang.String com.google.common.base.Joiner$MapJoiner.join(java.lang.Iterable<? extends java.util.Map$Entry<?, ?>>)"""
        return str._wrap(super(_MapJoiner, self).join(entries))

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
    def join(self, entries: 'Iterator') -> str:
        """public java.lang.String com.google.common.base.Joiner$MapJoiner.join(java.util.Iterator<? extends java.util.Map$Entry<?, ?>>)"""
        return str._wrap(super(_MapJoiner, self).join(entries))

    @overload
    def join(self, map: 'Map') -> str:
        """public java.lang.String com.google.common.base.Joiner$MapJoiner.join(java.util.Map<?, ?>)"""
        return str._wrap(super(_MapJoiner, self).join(map))

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Iterator') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner$MapJoiner.appendTo(A,java.util.Iterator<? extends java.util.Map$Entry<?, ?>>) throws java.io.IOException"""
        return 'Appendable'._wrap(super(_MapJoiner, self).appendTo(appendable, parts))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def appendTo(self, builder: 'StringBuilder', map: 'Map') -> 'StringBuilder':
        """public java.lang.StringBuilder com.google.common.base.Joiner$MapJoiner.appendTo(java.lang.StringBuilder,java.util.Map<?, ?>)"""
        return 'StringBuilder'._wrap(super(_MapJoiner, self).appendTo(builder, map))

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
    def appendTo(self, appendable: 'Appendable', map: 'Map') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner$MapJoiner.appendTo(A,java.util.Map<?, ?>) throws java.io.IOException"""
        return 'Appendable'._wrap(super(_MapJoiner, self).appendTo(appendable, map))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def appendTo(self, builder: 'StringBuilder', entries: 'Iterator') -> 'StringBuilder':
        """public java.lang.StringBuilder com.google.common.base.Joiner$MapJoiner.appendTo(java.lang.StringBuilder,java.util.Iterator<? extends java.util.Map$Entry<?, ?>>)"""
        return 'StringBuilder'._wrap(super(_MapJoiner, self).appendTo(builder, entries))

    @overload
    def appendTo(self, builder: 'StringBuilder', entries: 'Iterable') -> 'StringBuilder':
        """public java.lang.StringBuilder com.google.common.base.Joiner$MapJoiner.appendTo(java.lang.StringBuilder,java.lang.Iterable<? extends java.util.Map$Entry<?, ?>>)"""
        return 'StringBuilder'._wrap(super(_MapJoiner, self).appendTo(builder, entries))

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
 
 
# CLASS: com.google.common.base.VerifyException
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
import com.google.common.base.VerifyException as _VerifyException
_VerifyException = _VerifyException
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
 
class VerifyException():
    """com.google.common.base.VerifyException"""
 
    @staticmethod
    def _wrap(java_value: _VerifyException) -> 'VerifyException':
        return VerifyException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VerifyException):
        """
        Dynamic initializer for VerifyException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VerifyException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VerifyException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, cause: 'Throwable'):
        """public com.google.common.base.VerifyException(java.lang.Throwable)"""
        val = _VerifyException(cause)
        self.__wrapper = val

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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
    def __init__(self, message: str):
        """public com.google.common.base.VerifyException(java.lang.String)"""
        val = _VerifyException(message)
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

    @overload
    def __init__(self, message: str, cause: 'Throwable'):
        """public com.google.common.base.VerifyException(java.lang.String,java.lang.Throwable)"""
        val = _VerifyException(message, cause)
        self.__wrapper = val

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
    def __init__(self):
        """public com.google.common.base.VerifyException()"""
        val = _VerifyException()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.google.common.base.VerifyException()"""
        val = _VerifyException()
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())