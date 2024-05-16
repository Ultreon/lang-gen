from __future__ import annotations
from overload import overload


 
import org.apache.commons.lang3.text.FormattableUtils as _FormattableUtils
_FormattableUtils = _FormattableUtils
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Formatter as _Formatter
_Formatter = _Formatter
import java.lang.String as _String
_String = _String
import java.util.Formatter as Formatter
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.Formattable as Formattable
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FormattableUtils():
    """org.apache.commons.lang3.text.FormattableUtils"""
 
    @staticmethod
    def _wrap(java_value: _FormattableUtils) -> 'FormattableUtils':
        return FormattableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormattableUtils):
        """
        Dynamic initializer for FormattableUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormattableUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormattableUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: str, arg6: 'CharSequence') -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,char,java.lang.CharSequence)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _char.valueOf(arg5), arg6))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.FormattableUtils()"""
        val = _FormattableUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: str) -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,char)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _char.valueOf(arg5)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int) -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.FormattableUtils()"""
        val = _FormattableUtils()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: 'CharSequence') -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,java.lang.CharSequence)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

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
    def toString(arg0: 'Formattable') -> str:
        """public static java.lang.String org.apache.commons.lang3.text.FormattableUtils.toString(java.util.Formattable)"""
        return str._wrap(_FormattableUtils.toString(arg0))

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

 
 
 
# CLASS: org.apache.commons.lang3.text.FormattableUtils
import org.apache.commons.lang3.text.FormattableUtils as _FormattableUtils
_FormattableUtils = _FormattableUtils
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Formatter as _Formatter
_Formatter = _Formatter
import java.lang.String as _String
_String = _String
import java.util.Formatter as Formatter
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.Formattable as Formattable
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FormattableUtils():
    """org.apache.commons.lang3.text.FormattableUtils"""
 
    @staticmethod
    def _wrap(java_value: _FormattableUtils) -> 'FormattableUtils':
        return FormattableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormattableUtils):
        """
        Dynamic initializer for FormattableUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormattableUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormattableUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: str, arg6: 'CharSequence') -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,char,java.lang.CharSequence)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _char.valueOf(arg5), arg6))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.FormattableUtils()"""
        val = _FormattableUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: str) -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,char)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _char.valueOf(arg5)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int) -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.FormattableUtils()"""
        val = _FormattableUtils()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def append(arg0: 'CharSequence', arg1: 'Formatter', arg2: int, arg3: int, arg4: int, arg5: 'CharSequence') -> 'Formatter':
        """public static java.util.Formatter org.apache.commons.lang3.text.FormattableUtils.append(java.lang.CharSequence,java.util.Formatter,int,int,int,java.lang.CharSequence)"""
        return Formatter._wrap(_FormattableUtils.append(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

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
    def toString(arg0: 'Formattable') -> str:
        """public static java.lang.String org.apache.commons.lang3.text.FormattableUtils.toString(java.util.Formattable)"""
        return str._wrap(_FormattableUtils.toString(arg0))

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

 
 
 
# CLASS: org.apache.commons.lang3.text.FormattableUtils 
 
 
# CLASS: org.apache.commons.lang3.text.StrLookup
from builtins import str
import org.apache.commons.lang3.text.StrLookup as _StrLookup
_StrLookup = _StrLookup
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StrLookup():
    """org.apache.commons.lang3.text.StrLookup"""
 
    @staticmethod
    def _wrap(java_value: _StrLookup) -> 'StrLookup':
        return StrLookup(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StrLookup):
        """
        Dynamic initializer for StrLookup.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StrLookup__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StrLookup__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def noneLookup() -> 'StrLookup':
        """public static org.apache.commons.lang3.text.StrLookup<?> org.apache.commons.lang3.text.StrLookup.noneLookup()"""
        return StrLookup._wrap(_StrLookup.noneLookup())

    @staticmethod
    @overload
    def systemPropertiesLookup() -> 'StrLookup':
        """public static org.apache.commons.lang3.text.StrLookup<java.lang.String> org.apache.commons.lang3.text.StrLookup.systemPropertiesLookup()"""
        return StrLookup._wrap(_StrLookup.systemPropertiesLookup())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def lookup(self, arg0: str):
        """public abstract java.lang.String org.apache.commons.lang3.text.StrLookup.lookup(java.lang.String)"""
        pass

    @staticmethod
    @overload
    def mapLookup(arg0: 'Map') -> 'StrLookup':
        """public static <V> org.apache.commons.lang3.text.StrLookup<V> org.apache.commons.lang3.text.StrLookup.mapLookup(java.util.Map<java.lang.String, V>)"""
        return StrLookup._wrap(_StrLookup.mapLookup(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.text.StrTokenizer
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
from typing import List
import java.util.function.Consumer as Consumer
import org.apache.commons.lang3.text.StrTokenizer as _StrTokenizer
_StrTokenizer = _StrTokenizer
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.commons.lang3.text.StrMatcher as _StrMatcher
_StrMatcher = _StrMatcher
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class StrTokenizer():
    """org.apache.commons.lang3.text.StrTokenizer"""
 
    @staticmethod
    def _wrap(java_value: _StrTokenizer) -> 'StrTokenizer':
        return StrTokenizer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StrTokenizer):
        """
        Dynamic initializer for StrTokenizer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StrTokenizer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StrTokenizer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getCSVInstance() -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getCSVInstance()"""
        return StrTokenizer._wrap(_StrTokenizer.getCSVInstance())

    @overload
    def getTrimmerMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getTrimmerMatcher()"""
        return 'StrMatcher'._wrap(super(StrTokenizer, self).getTrimmerMatcher())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDelimiterMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setDelimiterMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setDelimiterMatcher(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.StrTokenizer()"""
        val = _StrTokenizer()
        self.__wrapper = val

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.lang3.text.StrTokenizer.nextIndex()"""
        return int._wrap(super(StrTokenizer, self).nextIndex())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.hasPrevious()"""
        return bool._wrap(super(StrTokenizer, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.toString()"""
        return str._wrap(super(StrTokenizer, self).toString())

    @overload
    def getIgnoredMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getIgnoredMatcher()"""
        return 'StrMatcher'._wrap(super(StrTokenizer, self).getIgnoredMatcher())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.lang3.text.StrTokenizer.previousIndex()"""
        return int._wrap(super(StrTokenizer, self).previousIndex())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.StrTokenizer()"""
        val = _StrTokenizer()
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.hasNext()"""
        return bool._wrap(super(StrTokenizer, self).hasNext())

    @overload
    def previousToken(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.previousToken()"""
        return str._wrap(super(StrTokenizer, self).previousToken())

    @overload
    def reset(self, arg0: 'char') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.reset(char[])"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).reset(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.lang3.text.StrTokenizer.remove()"""
        super(StrTokenizer, self).remove()

    @staticmethod
    @overload
    def getCSVInstance(arg0: str) -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getCSVInstance(java.lang.String)"""
        return StrTokenizer._wrap(_StrTokenizer.getCSVInstance(arg0))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,java.lang.String)"""
        val = _StrTokenizer(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'char', arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],java.lang.String)"""
        val = _StrTokenizer(arg0, arg1)
        self.__wrapper = val

    @overload
    def setIgnoredMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setIgnoredMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setIgnoredMatcher(arg0))

    @overload
    def setDelimiterString(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setDelimiterString(java.lang.String)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setDelimiterString(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,org.apache.commons.lang3.text.StrMatcher)"""
        val = _StrTokenizer(arg0, arg1)
        self.__wrapper = val

    @overload
    def getDelimiterMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getDelimiterMatcher()"""
        return 'StrMatcher'._wrap(super(StrTokenizer, self).getDelimiterMatcher())

    @overload
    def getQuoteMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrTokenizer.getQuoteMatcher()"""
        return 'StrMatcher'._wrap(super(StrTokenizer, self).getQuoteMatcher())

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String)"""
        val = _StrTokenizer(arg0)
        self.__wrapper = val

    @overload
    def setTrimmerMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setTrimmerMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setTrimmerMatcher(arg0))

    @overload
    def __init__(self, arg0: 'char', arg1: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],org.apache.commons.lang3.text.StrMatcher)"""
        val = _StrTokenizer(arg0, arg1)
        self.__wrapper = val

    @overload
    def reset(self) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.reset()"""
        return 'StrTokenizer'._wrap(super(StrTokenizer, self).reset())

    @overload
    def isEmptyTokenAsNull(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.isEmptyTokenAsNull()"""
        return bool._wrap(super(StrTokenizer, self).isEmptyTokenAsNull())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isIgnoreEmptyTokens(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrTokenizer.isIgnoreEmptyTokens()"""
        return bool._wrap(super(StrTokenizer, self).isIgnoreEmptyTokens())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,char,char)"""
        val = _StrTokenizer(arg0, _char.valueOf(arg1), _char.valueOf(arg2))
        self.__wrapper = val

    @staticmethod
    @overload
    def getTSVInstance(arg0: 'char') -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getTSVInstance(char[])"""
        return StrTokenizer._wrap(_StrTokenizer.getTSVInstance(arg0))

    @override
    @overload
    def next(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.next()"""
        return str._wrap(super(StrTokenizer, self).next())

    @overload
    def setQuoteMatcher(self, arg0: 'StrMatcher') -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setQuoteMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setQuoteMatcher(arg0))

    @overload
    def __init__(self, arg0: 'char', arg1: str, arg2: str):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],char,char)"""
        val = _StrTokenizer(arg0, _char.valueOf(arg1), _char.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getTokenList(self) -> 'List':
        """public java.util.List<java.lang.String> org.apache.commons.lang3.text.StrTokenizer.getTokenList()"""
        return 'List'._wrap(super(StrTokenizer, self).getTokenList())

    @override
    @overload
    def previous(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.previous()"""
        return str._wrap(super(StrTokenizer, self).previous())

    @staticmethod
    @overload
    def getTSVInstance() -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getTSVInstance()"""
        return StrTokenizer._wrap(_StrTokenizer.getTSVInstance())

    @overload
    def __init__(self, arg0: str, arg1: 'StrMatcher', arg2: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher)"""
        val = _StrTokenizer(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def add(self, arg0: str):
        """public void org.apache.commons.lang3.text.StrTokenizer.add(java.lang.String)"""
        super(_StrTokenizer, self).add(arg0)

    @overload
    def reset(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.reset(java.lang.String)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).reset(arg0))

    @staticmethod
    @overload
    def getCSVInstance(arg0: 'char') -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getCSVInstance(char[])"""
        return StrTokenizer._wrap(_StrTokenizer.getCSVInstance(arg0))

    @overload
    def setIgnoredChar(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setIgnoredChar(char)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setIgnoredChar(_char.valueOf(arg0)))

    @overload
    def clone(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.text.StrTokenizer.clone()"""
        return object._wrap(super(StrTokenizer, self).clone())

    @staticmethod
    @overload
    def getTSVInstance(arg0: str) -> 'StrTokenizer':
        """public static org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.getTSVInstance(java.lang.String)"""
        return StrTokenizer._wrap(_StrTokenizer.getTSVInstance(arg0))

    @overload
    def __init__(self, arg0: 'char'):
        """public org.apache.commons.lang3.text.StrTokenizer(char[])"""
        val = _StrTokenizer(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setDelimiterChar(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setDelimiterChar(char)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setDelimiterChar(_char.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'char', arg1: 'StrMatcher', arg2: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher)"""
        val = _StrTokenizer(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def nextToken(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.nextToken()"""
        return str._wrap(super(StrTokenizer, self).nextToken())

    @overload
    def setEmptyTokenAsNull(self, arg0: bool) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setEmptyTokenAsNull(boolean)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setEmptyTokenAsNull(_boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(java.lang.String,char)"""
        val = _StrTokenizer(arg0, _char.valueOf(arg1))
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.text.StrTokenizer.size()"""
        return int._wrap(super(StrTokenizer, self).size())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @overload
    def getTokenArray(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.text.StrTokenizer.getTokenArray()"""
        return List[str]._wrap(super(StrTokenizer, self).getTokenArray())

    @overload
    def setIgnoreEmptyTokens(self, arg0: bool) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setIgnoreEmptyTokens(boolean)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setIgnoreEmptyTokens(_boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'char', arg1: str):
        """public org.apache.commons.lang3.text.StrTokenizer(char[],char)"""
        val = _StrTokenizer(arg0, _char.valueOf(arg1))
        self.__wrapper = val

    @overload
    def set(self, arg0: str):
        """public void org.apache.commons.lang3.text.StrTokenizer.set(java.lang.String)"""
        super(_StrTokenizer, self).set(arg0)

    @overload
    def getContent(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrTokenizer.getContent()"""
        return str._wrap(super(StrTokenizer, self).getContent())

    @overload
    def setQuoteChar(self, arg0: str) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrTokenizer.setQuoteChar(char)"""
        return 'StrTokenizer'._wrap(super(_StrTokenizer, self).setQuoteChar(_char.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.text.ExtendedMessageFormat
import java.text.FieldPosition as FieldPosition
import java.util.Locale as Locale
import java.lang.StringBuffer as _StringBuffer
_StringBuffer = _StringBuffer
import java.lang.Object as _Object
_Object = _Object
import java.text.AttributedCharacterIterator as AttributedCharacterIterator
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.text.ParsePosition as ParsePosition
import java.text.AttributedCharacterIterator as _AttributedCharacterIterator
_AttributedCharacterIterator = _AttributedCharacterIterator
import java.lang.String as _string
import java.text.Format as Format
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.text.Format as _Format
_Format = _Format
import java.lang.Object as _object
import org.apache.commons.lang3.text.ExtendedMessageFormat as _ExtendedMessageFormat
_ExtendedMessageFormat = _ExtendedMessageFormat
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Integer as _int
import java.text.MessageFormat as _MessageFormat
_MessageFormat = _MessageFormat
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.Locale as _Locale
_Locale = _Locale
import java.lang.Class as _Class
_Class = _Class
 
class ExtendedMessageFormat():
    """org.apache.commons.lang3.text.ExtendedMessageFormat"""
 
    @staticmethod
    def _wrap(java_value: _ExtendedMessageFormat) -> 'ExtendedMessageFormat':
        return ExtendedMessageFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExtendedMessageFormat):
        """
        Dynamic initializer for ExtendedMessageFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExtendedMessageFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExtendedMessageFormat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition') -> List[object]:
        """public java.lang.Object[] java.text.MessageFormat.parse(java.lang.String,java.text.ParsePosition)"""
        return List[object]._wrap(super(_MessageFormat, self).parse(arg0, arg1))

    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object java.text.Format.parseObject(java.lang.String) throws java.text.ParseException"""
        return object._wrap(super(_Format, self).parseObject(arg0))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String)"""
        val = _ExtendedMessageFormat(arg0)
        self.__wrapper = val

    @override
    @overload
    def setFormatByArgumentIndex(self, arg0: int, arg1: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormatByArgumentIndex(int,java.text.Format)"""
        super(_ExtendedMessageFormat, self).setFormatByArgumentIndex(_int.valueOf(arg0), arg1)

    @override
    @overload
    def setLocale(self, arg0: 'Locale'):
        """public void java.text.MessageFormat.setLocale(java.util.Locale)"""
        super(_MessageFormat, self).setLocale(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: 'Locale'):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String,java.util.Locale)"""
        val = _ExtendedMessageFormat(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def setFormat(self, arg0: int, arg1: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormat(int,java.text.Format)"""
        super(_ExtendedMessageFormat, self).setFormat(_int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: str, arg1: 'Map'):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String,java.util.Map<java.lang.String, ? extends org.apache.commons.lang3.text.FormatFactory>)"""
        val = _ExtendedMessageFormat(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def applyPattern(self, arg0: str):
        """public final void org.apache.commons.lang3.text.ExtendedMessageFormat.applyPattern(java.lang.String)"""
        super(_ExtendedMessageFormat, self).applyPattern(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public final java.lang.StringBuffer java.text.MessageFormat.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'._wrap(super(_MessageFormat, self).format(arg0, arg1, arg2))

    @override
    @overload
    def getFormatsByArgumentIndex(self) -> List['Format']:
        """public java.text.Format[] java.text.MessageFormat.getFormatsByArgumentIndex()"""
        return List['Format']._wrap(super(MessageFormat, self).getFormatsByArgumentIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def format(arg0: str, *arg1: object) -> str:
        """public static java.lang.String java.text.MessageFormat.format(java.lang.String,java.lang.Object...)"""
        return str._wrap(_MessageFormat.format(arg0, arg1))

    @override
    @overload
    def getFormats(self) -> List['Format']:
        """public java.text.Format[] java.text.MessageFormat.getFormats()"""
        return List['Format']._wrap(super(MessageFormat, self).getFormats())

    @overload
    def formatToCharacterIterator(self, arg0: object) -> 'AttributedCharacterIterator':
        """public java.text.AttributedCharacterIterator java.text.MessageFormat.formatToCharacterIterator(java.lang.Object)"""
        return 'AttributedCharacterIterator'._wrap(super(_MessageFormat, self).formatToCharacterIterator(arg0))

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.text.MessageFormat.clone()"""
        return object._wrap(super(MessageFormat, self).clone())

    @override
    @overload
    def setFormats(self, arg0: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormats(java.text.Format[])"""
        super(_ExtendedMessageFormat, self).setFormats(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object java.text.MessageFormat.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object._wrap(super(_MessageFormat, self).parseObject(arg0, arg1))

    @overload
    def parse(self, arg0: str) -> List[object]:
        """public java.lang.Object[] java.text.MessageFormat.parse(java.lang.String) throws java.text.ParseException"""
        return List[object]._wrap(super(_MessageFormat, self).parse(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def format(self, arg0: object) -> str:
        """public final java.lang.String java.text.Format.format(java.lang.Object)"""
        return str._wrap(super(_Format, self).format(arg0))

    @override
    @overload
    def toPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.ExtendedMessageFormat.toPattern()"""
        return str._wrap(super(ExtendedMessageFormat, self).toPattern())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'Locale', arg2: 'Map'):
        """public org.apache.commons.lang3.text.ExtendedMessageFormat(java.lang.String,java.util.Locale,java.util.Map<java.lang.String, ? extends org.apache.commons.lang3.text.FormatFactory>)"""
        val = _ExtendedMessageFormat(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.text.ExtendedMessageFormat.equals(java.lang.Object)"""
        return bool._wrap(super(_ExtendedMessageFormat, self).equals(arg0))

    @overload
    def format(self, arg0: 'Object', arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public final java.lang.StringBuffer java.text.MessageFormat.format(java.lang.Object[],java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'._wrap(super(_MessageFormat, self).format(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.text.ExtendedMessageFormat.hashCode()"""
        return int._wrap(super(ExtendedMessageFormat, self).hashCode())

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale java.text.MessageFormat.getLocale()"""
        return 'Locale'._wrap(super(MessageFormat, self).getLocale())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setFormatsByArgumentIndex(self, arg0: 'Format'):
        """public void org.apache.commons.lang3.text.ExtendedMessageFormat.setFormatsByArgumentIndex(java.text.Format[])"""
        super(_ExtendedMessageFormat, self).setFormatsByArgumentIndex(arg0) 
 
 
# CLASS: org.apache.commons.lang3.text.StrBuilder
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.StringBuffer as _StringBuffer
_StringBuffer = _StringBuffer
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import org.apache.commons.lang3.text.StrBuilder as _StrBuilder
_StrBuilder = _StrBuilder
import java.lang.String as _string
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import java.lang.Boolean as _boolean
import java.nio.CharBuffer as CharBuffer
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Readable as Readable
from builtins import str
import java.io.Reader as _Reader
_Reader = _Reader
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Appendable as Appendable
import java.util.Iterator as Iterator
from typing import List
import java.lang.Float as _float
import org.apache.commons.lang3.text.StrTokenizer as _StrTokenizer
_StrTokenizer = _StrTokenizer
import java.lang.Integer as _int
import java.io.Writer as Writer
import java.io.Reader as Reader
import java.lang.StringBuilder as StringBuilder
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StrBuilder():
    """org.apache.commons.lang3.text.StrBuilder"""
 
    @staticmethod
    def _wrap(java_value: _StrBuilder) -> 'StrBuilder':
        return StrBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StrBuilder):
        """
        Dynamic initializer for StrBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StrBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StrBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(java.lang.String,int)"""
        return int._wrap(super(_StrBuilder, self).lastIndexOf(arg0, _int.valueOf(arg1)))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(java.lang.String)"""
        return int._wrap(super(_StrBuilder, self).lastIndexOf(arg0))

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(char,int)"""
        return int._wrap(super(_StrBuilder, self).indexOf(_char.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def ensureCapacity(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.ensureCapacity(int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).ensureCapacity(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), arg1))

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,long)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def append(self, arg0: str, *arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String,java.lang.Object...)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, arg1))

    @overload
    def appendln(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(_int.valueOf(arg0)))

    @overload
    def appendln(self, arg0: str, *arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String,java.lang.Object...)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0, arg1))

    @overload
    def appendln(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(long)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(_long.valueOf(arg0)))

    @overload
    def appendWithSeparators(self, arg0: 'Object', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.lang.Object[],java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendWithSeparators(arg0, arg1))

    @overload
    def appendln(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(double)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(_double.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'char', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char[],int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,double)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def append(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def deleteCharAt(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteCharAt(int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).deleteCharAt(_int.valueOf(arg0)))

    @overload
    def clear(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.clear()"""
        return 'StrBuilder'._wrap(super(StrBuilder, self).clear())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.hashCode()"""
        return int._wrap(super(StrBuilder, self).hashCode())

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(char)"""
        return int._wrap(super(_StrBuilder, self).indexOf(_char.valueOf(arg0)))

    @overload
    def startsWith(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.startsWith(java.lang.String)"""
        return bool._wrap(super(_StrBuilder, self).startsWith(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.isEmpty()"""
        return bool._wrap(super(StrBuilder, self).isEmpty())

    @overload
    def capacity(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.capacity()"""
        return int._wrap(super(StrBuilder, self).capacity())

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'._wrap(super(CharSequence, self).chars())

    @overload
    def contains(self, arg0: 'StrMatcher') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(org.apache.commons.lang3.text.StrMatcher)"""
        return bool._wrap(super(_StrBuilder, self).contains(arg0))

    @overload
    def indexOf(self, arg0: 'StrMatcher') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(org.apache.commons.lang3.text.StrMatcher)"""
        return int._wrap(super(_StrBuilder, self).indexOf(arg0))

    @overload
    def appendNewLine(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendNewLine()"""
        return 'StrBuilder'._wrap(super(StrBuilder, self).appendNewLine())

    @overload
    def asReader(self) -> 'Reader':
        """public java.io.Reader org.apache.commons.lang3.text.StrBuilder.asReader()"""
        return 'Reader'._wrap(super(StrBuilder, self).asReader())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.StrBuilder()"""
        val = _StrBuilder()
        self.__wrapper = val

    @overload
    def append(self, arg0: 'StringBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuilder)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def delete(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.delete(int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).delete(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuffer,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def append(self, arg0: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(boolean)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(_boolean.valueOf(arg0)))

    @overload
    def appendSeparator(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendSeparator(arg0, arg1))

    @overload
    def deleteAll(self, arg0: 'StrMatcher') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).deleteAll(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def appendFixedWidthPadLeft(self, arg0: object, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadLeft(java.lang.Object,int,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendFixedWidthPadLeft(arg0, _int.valueOf(arg1), _char.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.String,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def isNotEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.isNotEmpty()"""
        return bool._wrap(super(StrBuilder, self).isNotEmpty())

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(char)"""
        return bool._wrap(super(_StrBuilder, self).contains(_char.valueOf(arg0)))

    @overload
    def append(self, arg0: 'CharBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.nio.CharBuffer)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def deleteFirst(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).deleteFirst(arg0))

    @overload
    def appendln(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(float)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(_float.valueOf(arg0)))

    @overload
    def append(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(_char.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char[])"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), arg1))

    @overload
    def appendln(self, arg0: 'StrBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(org.apache.commons.lang3.text.StrBuilder)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.text.StrBuilder(java.lang.String)"""
        val = _StrBuilder(arg0)
        self.__wrapper = val

    @overload
    def replaceFirst(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(char,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replaceFirst(_char.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def lastIndexOf(self, arg0: 'StrMatcher', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(org.apache.commons.lang3.text.StrMatcher,int)"""
        return int._wrap(super(_StrBuilder, self).lastIndexOf(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.StrBuilder()"""
        val = _StrBuilder()
        self.__wrapper = val

    @overload
    def readFrom(self, arg0: 'Readable') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.readFrom(java.lang.Readable) throws java.io.IOException"""
        return int._wrap(super(_StrBuilder, self).readFrom(arg0))

    @overload
    def appendWithSeparators(self, arg0: 'Iterable', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.lang.Iterable<?>,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendWithSeparators(arg0, arg1))

    @overload
    def append(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(double)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(_double.valueOf(arg0)))

    @overload
    def appendln(self, arg0: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.Object)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0))

    @overload
    def appendln(self, arg0: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(boolean)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(_boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def rightString(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.rightString(int)"""
        return str._wrap(super(_StrBuilder, self).rightString(_int.valueOf(arg0)))

    @override
    @overload
    def length(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.length()"""
        return int._wrap(super(StrBuilder, self).length())

    @overload
    def minimizeCapacity(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.minimizeCapacity()"""
        return 'StrBuilder'._wrap(super(StrBuilder, self).minimizeCapacity())

    @overload
    def replaceAll(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(java.lang.String,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replaceAll(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(long)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(_long.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def insert(self, arg0: int, arg1: 'char', arg2: int, arg3: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char[],int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def build(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.build()"""
        return str._wrap(super(StrBuilder, self).build())

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(java.lang.String,int)"""
        return int._wrap(super(_StrBuilder, self).indexOf(arg0, _int.valueOf(arg1)))

    @overload
    def equalsIgnoreCase(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equalsIgnoreCase(org.apache.commons.lang3.text.StrBuilder)"""
        return bool._wrap(super(_StrBuilder, self).equalsIgnoreCase(arg0))

    @overload
    def appendAll(self, arg0: 'Iterator') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(java.util.Iterator<?>)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendAll(arg0))

    @overload
    def trim(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.trim()"""
        return 'StrBuilder'._wrap(super(StrBuilder, self).trim())

    @overload
    def reverse(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.reverse()"""
        return 'StrBuilder'._wrap(super(StrBuilder, self).reverse())

    @overload
    def appendln(self, arg0: 'StringBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuilder)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.toString()"""
        return str._wrap(super(StrBuilder, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def asTokenizer(self) -> 'StrTokenizer':
        """public org.apache.commons.lang3.text.StrTokenizer org.apache.commons.lang3.text.StrBuilder.asTokenizer()"""
        return 'StrTokenizer'._wrap(super(StrBuilder, self).asTokenizer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def replaceFirst(self, arg0: 'StrMatcher', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(org.apache.commons.lang3.text.StrMatcher,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replaceFirst(arg0, arg1))

    @overload
    def appendAll(self, arg0: 'Iterable') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(java.lang.Iterable<?>)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendAll(arg0))

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'._wrap(super(CharSequence, self).codePoints())

    @overload
    def deleteFirst(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).deleteFirst(_char.valueOf(arg0)))

    @overload
    def append(self, arg0: 'StringBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuffer)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def appendSeparator(self, arg0: str, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendSeparator(_char.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def replace(self, arg0: 'StrMatcher', arg1: str, arg2: int, arg3: int, arg4: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replace(org.apache.commons.lang3.text.StrMatcher,java.lang.String,int,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replace(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def appendln(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuilder,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getChars(self, arg0: int, arg1: int, arg2: 'char', arg3: int):
        """public void org.apache.commons.lang3.text.StrBuilder.getChars(int,int,char[],int)"""
        super(_StrBuilder, self).getChars(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def lastIndexOf(self, arg0: 'StrMatcher') -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(org.apache.commons.lang3.text.StrMatcher)"""
        return int._wrap(super(_StrBuilder, self).lastIndexOf(arg0))

    @overload
    def asWriter(self) -> 'Writer':
        """public java.io.Writer org.apache.commons.lang3.text.StrBuilder.asWriter()"""
        return 'Writer'._wrap(super(StrBuilder, self).asWriter())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.text.StrBuilder(int)"""
        val = _StrBuilder(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def append(self, arg0: 'CharSequence') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.CharSequence)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.contains(java.lang.String)"""
        return bool._wrap(super(_StrBuilder, self).contains(arg0))

    @overload
    def appendNull(self) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendNull()"""
        return 'StrBuilder'._wrap(super(StrBuilder, self).appendNull())

    @overload
    def getNullText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.getNullText()"""
        return str._wrap(super(StrBuilder, self).getNullText())

    @overload
    def deleteAll(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).deleteAll(arg0))

    @overload
    def append(self, arg0: 'CharSequence', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.CharSequence,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def appendFixedWidthPadRight(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadRight(int,int,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendFixedWidthPadRight(_int.valueOf(arg0), _int.valueOf(arg1), _char.valueOf(arg2)))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.size()"""
        return int._wrap(super(StrBuilder, self).size())

    @overload
    def getNewLineText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.getNewLineText()"""
        return str._wrap(super(StrBuilder, self).getNewLineText())

    @overload
    def toStringBuffer(self) -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.text.StrBuilder.toStringBuffer()"""
        return 'StringBuffer'._wrap(super(StrBuilder, self).toStringBuffer())

    @overload
    def appendFixedWidthPadRight(self, arg0: object, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadRight(java.lang.Object,int,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendFixedWidthPadRight(arg0, _int.valueOf(arg1), _char.valueOf(arg2)))

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(_char.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuffer,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def leftString(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.leftString(int)"""
        return str._wrap(super(_StrBuilder, self).leftString(_int.valueOf(arg0)))

    @overload
    def appendln(self, arg0: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(char[])"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0))

    @overload
    def setNullText(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setNullText(java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).setNullText(arg0))

    @overload
    def replace(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replace(int,int,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replace(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def appendSeparator(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendSeparator(_char.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def midString(self, arg0: int, arg1: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.midString(int,int)"""
        return str._wrap(super(_StrBuilder, self).midString(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def insert(self, arg0: int, arg1: bool) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,boolean)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def indexOf(self, arg0: 'StrMatcher', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(org.apache.commons.lang3.text.StrMatcher,int)"""
        return int._wrap(super(_StrBuilder, self).indexOf(arg0, _int.valueOf(arg1)))

    @overload
    def getChars(self, arg0: 'char') -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.getChars(char[])"""
        return List[str]._wrap(super(_StrBuilder, self).getChars(arg0))

    @overload
    def appendTo(self, arg0: 'Appendable'):
        """public void org.apache.commons.lang3.text.StrBuilder.appendTo(java.lang.Appendable) throws java.io.IOException"""
        super(_StrBuilder, self).appendTo(arg0)

    @overload
    def appendSeparator(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendSeparator(_char.valueOf(arg0)))

    @overload
    def toStringBuilder(self) -> 'StringBuilder':
        """public java.lang.StringBuilder org.apache.commons.lang3.text.StrBuilder.toStringBuilder()"""
        return 'StringBuilder'._wrap(super(StrBuilder, self).toStringBuilder())

    @overload
    def deleteFirst(self, arg0: 'StrMatcher') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteFirst(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).deleteFirst(arg0))

    @overload
    def subSequence(self, arg0: int, arg1: int) -> 'CharSequence':
        """public java.lang.CharSequence org.apache.commons.lang3.text.StrBuilder.subSequence(int,int)"""
        return 'CharSequence'._wrap(super(_StrBuilder, self).subSequence(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(char)"""
        return int._wrap(super(_StrBuilder, self).lastIndexOf(_char.valueOf(arg0)))

    @overload
    def replaceAll(self, arg0: 'StrMatcher', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(org.apache.commons.lang3.text.StrMatcher,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replaceAll(arg0, arg1))

    @overload
    def appendFixedWidthPadLeft(self, arg0: int, arg1: int, arg2: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendFixedWidthPadLeft(int,int,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendFixedWidthPadLeft(_int.valueOf(arg0), _int.valueOf(arg1), _char.valueOf(arg2)))

    @overload
    def replaceAll(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceAll(char,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replaceAll(_char.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equals(java.lang.Object)"""
        return bool._wrap(super(_StrBuilder, self).equals(arg0))

    @overload
    def append(self, arg0: 'CharBuffer', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.nio.CharBuffer,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def setLength(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setLength(int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).setLength(_int.valueOf(arg0)))

    @overload
    def appendSeparator(self, arg0: str, arg1: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendSeparator(arg0, _int.valueOf(arg1)))

    @overload
    def appendln(self, arg0: 'StringBuffer') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.StringBuffer)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0))

    @overload
    def deleteAll(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.deleteAll(char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).deleteAll(_char.valueOf(arg0)))

    @overload
    def append(self, arg0: 'char', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char[],int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def replaceFirst(self, arg0: str, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.replaceFirst(java.lang.String,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).replaceFirst(arg0, arg1))

    @overload
    def appendPadding(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendPadding(int,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendPadding(_int.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.lastIndexOf(char,int)"""
        return int._wrap(super(_StrBuilder, self).lastIndexOf(_char.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int org.apache.commons.lang3.text.StrBuilder.indexOf(java.lang.String)"""
        return int._wrap(super(_StrBuilder, self).indexOf(arg0))

    @overload
    def setNewLineText(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setNewLineText(java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).setNewLineText(arg0))

    @overload
    def endsWith(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.endsWith(java.lang.String)"""
        return bool._wrap(super(_StrBuilder, self).endsWith(arg0))

    @overload
    def appendAll(self, *arg0: object) -> 'StrBuilder':
        """public <T> org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendAll(T...)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendAll(arg0))

    @overload
    def appendSeparator(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendSeparator(java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendSeparator(arg0))

    @overload
    def equals(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrBuilder.equals(org.apache.commons.lang3.text.StrBuilder)"""
        return bool._wrap(super(_StrBuilder, self).equals(arg0))

    @overload
    def append(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def append(self, arg0: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.Object)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def insert(self, arg0: int, arg1: object) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,java.lang.Object)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), arg1))

    @overload
    def substring(self, arg0: int, arg1: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.substring(int,int)"""
        return str._wrap(super(_StrBuilder, self).substring(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def substring(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrBuilder.substring(int)"""
        return str._wrap(super(_StrBuilder, self).substring(_int.valueOf(arg0)))

    @overload
    def appendWithSeparators(self, arg0: 'Iterator', arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendWithSeparators(java.util.Iterator<?>,java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendWithSeparators(arg0, arg1))

    @overload
    def setCharAt(self, arg0: int, arg1: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.setCharAt(int,char)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).setCharAt(_int.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def append(self, arg0: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(_int.valueOf(arg0)))

    @overload
    def append(self, arg0: 'char') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(char[])"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def appendln(self, arg0: str, arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def charAt(self, arg0: int) -> str:
        """public char org.apache.commons.lang3.text.StrBuilder.charAt(int)"""
        return str._wrap(super(_StrBuilder, self).charAt(_int.valueOf(arg0)))

    @overload
    def appendln(self, arg0: str) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.appendln(java.lang.String)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).appendln(arg0))

    @overload
    def toCharArray(self, arg0: int, arg1: int) -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.toCharArray(int,int)"""
        return List[str]._wrap(super(_StrBuilder, self).toCharArray(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def append(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(java.lang.StringBuilder,int,int)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.insert(int,float)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).insert(_int.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def append(self, arg0: float) -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(float)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(_float.valueOf(arg0)))

    @overload
    def append(self, arg0: 'StrBuilder') -> 'StrBuilder':
        """public org.apache.commons.lang3.text.StrBuilder org.apache.commons.lang3.text.StrBuilder.append(org.apache.commons.lang3.text.StrBuilder)"""
        return 'StrBuilder'._wrap(super(_StrBuilder, self).append(arg0))

    @overload
    def toCharArray(self) -> List[str]:
        """public char[] org.apache.commons.lang3.text.StrBuilder.toCharArray()"""
        return List[str]._wrap(super(StrBuilder, self).toCharArray()) 
 
 
# CLASS: org.apache.commons.lang3.text.FormatFactory
import java.util.Locale as Locale
import org.apache.commons.lang3.text.FormatFactory as _FormatFactory
_FormatFactory = _FormatFactory
from abc import abstractmethod, ABC
 
class FormatFactory():
    """org.apache.commons.lang3.text.FormatFactory"""
 
    @staticmethod
    def _wrap(java_value: _FormatFactory) -> 'FormatFactory':
        return FormatFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormatFactory):
        """
        Dynamic initializer for FormatFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormatFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormatFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, arg0: str, arg1: str, arg2: 'Locale'):
        """public abstract java.text.Format org.apache.commons.lang3.text.FormatFactory.getFormat(java.lang.String,java.lang.String,java.util.Locale)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.text.CompositeFormat
import java.text.FieldPosition as FieldPosition
from builtins import str
import java.lang.StringBuffer as _StringBuffer
_StringBuffer = _StringBuffer
from pyquantum_helper import override
import java.text.Format as _Format
_Format = _Format
import java.lang.Object as _Object
_Object = _Object
import java.text.AttributedCharacterIterator as AttributedCharacterIterator
import java.lang.Object as _object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.text.ParsePosition as ParsePosition
import java.text.AttributedCharacterIterator as _AttributedCharacterIterator
_AttributedCharacterIterator = _AttributedCharacterIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import org.apache.commons.lang3.text.CompositeFormat as _CompositeFormat
_CompositeFormat = _CompositeFormat
import java.lang.Integer as _int
import java.text.Format as Format
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CompositeFormat():
    """org.apache.commons.lang3.text.CompositeFormat"""
 
    @staticmethod
    def _wrap(java_value: _CompositeFormat) -> 'CompositeFormat':
        return CompositeFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CompositeFormat):
        """
        Dynamic initializer for CompositeFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CompositeFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CompositeFormat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object java.text.Format.parseObject(java.lang.String) throws java.text.ParseException"""
        return object._wrap(super(_Format, self).parseObject(arg0))

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.text.Format.clone()"""
        return object._wrap(super(Format, self).clone())

    @overload
    def getFormatter(self) -> 'Format':
        """public java.text.Format org.apache.commons.lang3.text.CompositeFormat.getFormatter()"""
        return 'Format'._wrap(super(CompositeFormat, self).getFormatter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def reformat(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.text.CompositeFormat.reformat(java.lang.String) throws java.text.ParseException"""
        return str._wrap(super(_CompositeFormat, self).reformat(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.text.CompositeFormat.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'._wrap(super(_CompositeFormat, self).format(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def formatToCharacterIterator(self, arg0: object) -> 'AttributedCharacterIterator':
        """public java.text.AttributedCharacterIterator java.text.Format.formatToCharacterIterator(java.lang.Object)"""
        return 'AttributedCharacterIterator'._wrap(super(_Format, self).formatToCharacterIterator(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Format', arg1: 'Format'):
        """public org.apache.commons.lang3.text.CompositeFormat(java.text.Format,java.text.Format)"""
        val = _CompositeFormat(arg0, arg1)
        self.__wrapper = val

    @overload
    def format(self, arg0: object) -> str:
        """public final java.lang.String java.text.Format.format(java.lang.Object)"""
        return str._wrap(super(_Format, self).format(arg0))

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
    def getParser(self) -> 'Format':
        """public java.text.Format org.apache.commons.lang3.text.CompositeFormat.getParser()"""
        return 'Format'._wrap(super(CompositeFormat, self).getParser())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object org.apache.commons.lang3.text.CompositeFormat.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object._wrap(super(_CompositeFormat, self).parseObject(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.WordUtils
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.WordUtils as _WordUtils
_WordUtils = _WordUtils
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WordUtils():
    """org.apache.commons.lang3.text.WordUtils"""
 
    @staticmethod
    def _wrap(java_value: _WordUtils) -> 'WordUtils':
        return WordUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WordUtils):
        """
        Dynamic initializer for WordUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WordUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WordUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def uncapitalize(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.uncapitalize(java.lang.String,char...)"""
        return str._wrap(_WordUtils.uncapitalize(arg0, arg1))

    @staticmethod
    @overload
    def initials(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.initials(java.lang.String,char...)"""
        return str._wrap(_WordUtils.initials(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: int, arg2: str, arg3: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.wrap(java.lang.String,int,java.lang.String,boolean)"""
        return str._wrap(_WordUtils.wrap(arg0, _int.valueOf(arg1), arg2, _boolean.valueOf(arg3)))

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
    def wrap(arg0: str, arg1: int, arg2: str, arg3: bool, arg4: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.wrap(java.lang.String,int,java.lang.String,boolean,java.lang.String)"""
        return str._wrap(_WordUtils.wrap(arg0, _int.valueOf(arg1), arg2, _boolean.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.wrap(java.lang.String,int)"""
        return str._wrap(_WordUtils.wrap(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def capitalizeFully(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalizeFully(java.lang.String,char...)"""
        return str._wrap(_WordUtils.capitalizeFully(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.WordUtils()"""
        val = _WordUtils()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.WordUtils()"""
        val = _WordUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def swapCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.swapCase(java.lang.String)"""
        return str._wrap(_WordUtils.swapCase(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def capitalize(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalize(java.lang.String,char...)"""
        return str._wrap(_WordUtils.capitalize(arg0, arg1))

    @staticmethod
    @overload
    def capitalizeFully(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalizeFully(java.lang.String)"""
        return str._wrap(_WordUtils.capitalizeFully(arg0))

    @staticmethod
    @overload
    def uncapitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.uncapitalize(java.lang.String)"""
        return str._wrap(_WordUtils.uncapitalize(arg0))

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
    def capitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.capitalize(java.lang.String)"""
        return str._wrap(_WordUtils.capitalize(arg0))

    @staticmethod
    @overload
    def initials(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.WordUtils.initials(java.lang.String)"""
        return str._wrap(_WordUtils.initials(arg0))

    @staticmethod
    @overload
    def containsAllWords(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.text.WordUtils.containsAllWords(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool._wrap(_WordUtils.containsAllWords(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.StrSubstitutor
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as _char
import org.apache.commons.lang3.text.StrLookup as _StrLookup
_StrLookup = _StrLookup
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.text.StrSubstitutor as _StrSubstitutor
_StrSubstitutor = _StrSubstitutor
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.Properties as Properties
import org.apache.commons.lang3.text.StrMatcher as _StrMatcher
_StrMatcher = _StrMatcher
import java.lang.StringBuilder as StringBuilder
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StrSubstitutor():
    """org.apache.commons.lang3.text.StrSubstitutor"""
 
    @staticmethod
    def _wrap(java_value: _StrSubstitutor) -> 'StrSubstitutor':
        return StrSubstitutor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StrSubstitutor):
        """
        Dynamic initializer for StrSubstitutor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StrSubstitutor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StrSubstitutor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Map'):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>)"""
        val = _StrSubstitutor(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def replaceSystemProperties(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replaceSystemProperties(java.lang.Object)"""
        return str._wrap(_StrSubstitutor.replaceSystemProperties(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.StrSubstitutor()"""
        val = _StrSubstitutor()
        self.__wrapper = val

    @overload
    def replace(self, arg0: str, arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.String,int,int)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: 'StrMatcher', arg2: 'StrMatcher', arg3: str, arg4: 'StrMatcher'):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher,char,org.apache.commons.lang3.text.StrMatcher)"""
        val = _StrSubstitutor(arg0, arg1, arg2, _char.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def replace(self, arg0: 'char') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(char[])"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0))

    @overload
    def replace(self, arg0: 'char', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(char[],int,int)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def setPreserveEscapes(self, arg0: bool):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setPreserveEscapes(boolean)"""
        super(_StrSubstitutor, self).setPreserveEscapes(_boolean.valueOf(arg0))

    @overload
    def getEscapeChar(self) -> str:
        """public char org.apache.commons.lang3.text.StrSubstitutor.getEscapeChar()"""
        return str._wrap(super(StrSubstitutor, self).getEscapeChar())

    @overload
    def setVariableSuffixMatcher(self, arg0: 'StrMatcher') -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariableSuffixMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setVariableSuffixMatcher(arg0))

    @overload
    def getValueDelimiterMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrSubstitutor.getValueDelimiterMatcher()"""
        return 'StrMatcher'._wrap(super(StrSubstitutor, self).getValueDelimiterMatcher())

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: 'StrMatcher', arg2: 'StrMatcher', arg3: str):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,org.apache.commons.lang3.text.StrMatcher,org.apache.commons.lang3.text.StrMatcher,char)"""
        val = _StrSubstitutor(arg0, arg1, arg2, _char.valueOf(arg3))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getVariableResolver(self) -> 'StrLookup':
        """public org.apache.commons.lang3.text.StrLookup<?> org.apache.commons.lang3.text.StrSubstitutor.getVariableResolver()"""
        return 'StrLookup'._wrap(super(StrSubstitutor, self).getVariableResolver())

    @overload
    def replace(self, arg0: 'CharSequence') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.CharSequence)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0))

    @overload
    def setValueDelimiterMatcher(self, arg0: 'StrMatcher') -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setValueDelimiterMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setValueDelimiterMatcher(arg0))

    @overload
    def setVariableSuffix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariableSuffix(char)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setVariableSuffix(_char.valueOf(arg0)))

    @overload
    def replace(self, arg0: object) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0))

    @overload
    def replace(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.String)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0))

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: str, arg2: str, arg3: str):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,java.lang.String,java.lang.String,char)"""
        val = _StrSubstitutor(arg0, arg1, arg2, _char.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setVariablePrefix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariablePrefix(char)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setVariablePrefix(_char.valueOf(arg0)))

    @overload
    def replace(self, arg0: 'StrBuilder') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(org.apache.commons.lang3.text.StrBuilder)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0))

    @overload
    def setEscapeChar(self, arg0: str):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setEscapeChar(char)"""
        super(_StrSubstitutor, self).setEscapeChar(_char.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'StrLookup', arg1: str, arg2: str, arg3: str, arg4: str):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>,java.lang.String,java.lang.String,char,java.lang.String)"""
        val = _StrSubstitutor(arg0, arg1, arg2, _char.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def isEnableSubstitutionInVariables(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.isEnableSubstitutionInVariables()"""
        return bool._wrap(super(StrSubstitutor, self).isEnableSubstitutionInVariables())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setVariablePrefix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariablePrefix(java.lang.String)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setVariablePrefix(arg0))

    @overload
    def __init__(self, arg0: 'StrLookup'):
        """public org.apache.commons.lang3.text.StrSubstitutor(org.apache.commons.lang3.text.StrLookup<?>)"""
        val = _StrSubstitutor(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def replace(arg0: object, arg1: 'Properties') -> str:
        """public static java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object,java.util.Properties)"""
        return str._wrap(_StrSubstitutor.replace(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map', arg1: str, arg2: str, arg3: str):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String,char)"""
        val = _StrSubstitutor(arg0, arg1, arg2, _char.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def replace(self, arg0: 'CharSequence', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.CharSequence,int,int)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getVariableSuffixMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrSubstitutor.getVariableSuffixMatcher()"""
        return 'StrMatcher'._wrap(super(StrSubstitutor, self).getVariableSuffixMatcher())

    @overload
    def setVariableSuffix(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariableSuffix(java.lang.String)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setVariableSuffix(arg0))

    @overload
    def replaceIn(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return bool._wrap(super(_StrSubstitutor, self).replaceIn(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def replace(self, arg0: 'StrBuilder', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(org.apache.commons.lang3.text.StrBuilder,int,int)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def setEnableSubstitutionInVariables(self, arg0: bool):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setEnableSubstitutionInVariables(boolean)"""
        super(_StrSubstitutor, self).setEnableSubstitutionInVariables(_boolean.valueOf(arg0))

    @overload
    def isPreserveEscapes(self) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.isPreserveEscapes()"""
        return bool._wrap(super(StrSubstitutor, self).isPreserveEscapes())

    @overload
    def replace(self, arg0: 'StringBuffer') -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.StringBuffer)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0))

    @overload
    def replaceIn(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuffer,int,int)"""
        return bool._wrap(super(_StrSubstitutor, self).replaceIn(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def replace(arg0: object, arg1: 'Map') -> str:
        """public static <V> java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object,java.util.Map<java.lang.String, V>)"""
        return str._wrap(_StrSubstitutor.replace(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map', arg1: str, arg2: str, arg3: str, arg4: str):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String,char,java.lang.String)"""
        val = _StrSubstitutor(arg0, arg1, arg2, _char.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def setVariablePrefixMatcher(self, arg0: 'StrMatcher') -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setVariablePrefixMatcher(org.apache.commons.lang3.text.StrMatcher)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setVariablePrefixMatcher(arg0))

    @overload
    def __init__(self, arg0: 'Map', arg1: str, arg2: str):
        """public <V> org.apache.commons.lang3.text.StrSubstitutor(java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String)"""
        val = _StrSubstitutor(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.StrSubstitutor()"""
        val = _StrSubstitutor()
        self.__wrapper = val

    @overload
    def getVariablePrefixMatcher(self) -> 'StrMatcher':
        """public org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrSubstitutor.getVariablePrefixMatcher()"""
        return 'StrMatcher'._wrap(super(StrSubstitutor, self).getVariablePrefixMatcher())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def replace(arg0: object, arg1: 'Map', arg2: str, arg3: str) -> str:
        """public static <V> java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.Object,java.util.Map<java.lang.String, V>,java.lang.String,java.lang.String)"""
        return str._wrap(_StrSubstitutor.replace(arg0, arg1, arg2, arg3))

    @overload
    def replaceIn(self, arg0: 'StringBuffer') -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuffer)"""
        return bool._wrap(super(_StrSubstitutor, self).replaceIn(arg0))

    @overload
    def replaceIn(self, arg0: 'StrBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(org.apache.commons.lang3.text.StrBuilder)"""
        return bool._wrap(super(_StrSubstitutor, self).replaceIn(arg0))

    @overload
    def replace(self, arg0: 'StringBuffer', arg1: int, arg2: int) -> str:
        """public java.lang.String org.apache.commons.lang3.text.StrSubstitutor.replace(java.lang.StringBuffer,int,int)"""
        return str._wrap(super(_StrSubstitutor, self).replace(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def setVariableResolver(self, arg0: 'StrLookup'):
        """public void org.apache.commons.lang3.text.StrSubstitutor.setVariableResolver(org.apache.commons.lang3.text.StrLookup<?>)"""
        super(_StrSubstitutor, self).setVariableResolver(arg0)

    @overload
    def replaceIn(self, arg0: 'StringBuilder') -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuilder)"""
        return bool._wrap(super(_StrSubstitutor, self).replaceIn(arg0))

    @overload
    def replaceIn(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> bool:
        """public boolean org.apache.commons.lang3.text.StrSubstitutor.replaceIn(java.lang.StringBuilder,int,int)"""
        return bool._wrap(super(_StrSubstitutor, self).replaceIn(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setValueDelimiter(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setValueDelimiter(java.lang.String)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setValueDelimiter(arg0))

    @overload
    def setValueDelimiter(self, arg0: str) -> 'StrSubstitutor':
        """public org.apache.commons.lang3.text.StrSubstitutor org.apache.commons.lang3.text.StrSubstitutor.setValueDelimiter(char)"""
        return 'StrSubstitutor'._wrap(super(_StrSubstitutor, self).setValueDelimiter(_char.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.text.StrMatcher
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.lang3.text.StrMatcher as _StrMatcher
_StrMatcher = _StrMatcher
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StrMatcher():
    """org.apache.commons.lang3.text.StrMatcher"""
 
    @staticmethod
    def _wrap(java_value: _StrMatcher) -> 'StrMatcher':
        return StrMatcher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StrMatcher):
        """
        Dynamic initializer for StrMatcher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StrMatcher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StrMatcher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def doubleQuoteMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.doubleQuoteMatcher()"""
        return StrMatcher._wrap(_StrMatcher.doubleQuoteMatcher())

    @staticmethod
    @overload
    def stringMatcher(arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.stringMatcher(java.lang.String)"""
        return StrMatcher._wrap(_StrMatcher.stringMatcher(arg0))

    @staticmethod
    @overload
    def singleQuoteMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.singleQuoteMatcher()"""
        return StrMatcher._wrap(_StrMatcher.singleQuoteMatcher())

    @staticmethod
    @overload
    def charSetMatcher(*arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.charSetMatcher(char...)"""
        return StrMatcher._wrap(_StrMatcher.charSetMatcher(arg0))

    @overload
    def isMatch(self, arg0: 'char', arg1: int) -> int:
        """public int org.apache.commons.lang3.text.StrMatcher.isMatch(char[],int)"""
        return int._wrap(super(_StrMatcher, self).isMatch(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def commaMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.commaMatcher()"""
        return StrMatcher._wrap(_StrMatcher.commaMatcher())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def charMatcher(arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.charMatcher(char)"""
        return StrMatcher._wrap(_StrMatcher.charMatcher(_char.valueOf(arg0)))

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
    def spaceMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.spaceMatcher()"""
        return StrMatcher._wrap(_StrMatcher.spaceMatcher())

    @abstractmethod
    def isMatch(self, arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public abstract int org.apache.commons.lang3.text.StrMatcher.isMatch(char[],int,int,int)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def splitMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.splitMatcher()"""
        return StrMatcher._wrap(_StrMatcher.splitMatcher())

    @staticmethod
    @overload
    def quoteMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.quoteMatcher()"""
        return StrMatcher._wrap(_StrMatcher.quoteMatcher())

    @staticmethod
    @overload
    def noneMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.noneMatcher()"""
        return StrMatcher._wrap(_StrMatcher.noneMatcher())

    @staticmethod
    @overload
    def trimMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.trimMatcher()"""
        return StrMatcher._wrap(_StrMatcher.trimMatcher())

    @staticmethod
    @overload
    def charSetMatcher(arg0: str) -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.charSetMatcher(java.lang.String)"""
        return StrMatcher._wrap(_StrMatcher.charSetMatcher(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def tabMatcher() -> 'StrMatcher':
        """public static org.apache.commons.lang3.text.StrMatcher org.apache.commons.lang3.text.StrMatcher.tabMatcher()"""
        return StrMatcher._wrap(_StrMatcher.tabMatcher())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())