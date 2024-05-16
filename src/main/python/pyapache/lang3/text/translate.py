from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.lang3.text.translate.UnicodeUnescaper as _UnicodeUnescaper
_UnicodeUnescaper = _UnicodeUnescaper
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnicodeUnescaper():
    """org.apache.commons.lang3.text.translate.UnicodeUnescaper"""
 
    @staticmethod
    def _wrap(java_value: _UnicodeUnescaper) -> 'UnicodeUnescaper':
        return UnicodeUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnicodeUnescaper):
        """
        Dynamic initializer for UnicodeUnescaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnicodeUnescaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnicodeUnescaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.UnicodeUnescaper()"""
        val = _UnicodeUnescaper()
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.UnicodeUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_UnicodeUnescaper, self).translate(arg0, _int.valueOf(arg1), arg2))

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
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.UnicodeUnescaper()"""
        val = _UnicodeUnescaper()
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.text.translate.UnicodeUnescaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.lang3.text.translate.UnicodeUnescaper as _UnicodeUnescaper
_UnicodeUnescaper = _UnicodeUnescaper
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnicodeUnescaper():
    """org.apache.commons.lang3.text.translate.UnicodeUnescaper"""
 
    @staticmethod
    def _wrap(java_value: _UnicodeUnescaper) -> 'UnicodeUnescaper':
        return UnicodeUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnicodeUnescaper):
        """
        Dynamic initializer for UnicodeUnescaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnicodeUnescaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnicodeUnescaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.UnicodeUnescaper()"""
        val = _UnicodeUnescaper()
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.UnicodeUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_UnicodeUnescaper, self).translate(arg0, _int.valueOf(arg1), arg2))

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
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.UnicodeUnescaper()"""
        val = _UnicodeUnescaper()
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.text.translate.UnicodeUnescaper 
 
 
# CLASS: org.apache.commons.lang3.text.translate.CodePointTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.Writer as Writer
import org.apache.commons.lang3.text.translate.CodePointTranslator as _CodePointTranslator
_CodePointTranslator = _CodePointTranslator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CodePointTranslator():
    """org.apache.commons.lang3.text.translate.CodePointTranslator"""
 
    @staticmethod
    def _wrap(java_value: _CodePointTranslator) -> 'CodePointTranslator':
        return CodePointTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CodePointTranslator):
        """
        Dynamic initializer for CodePointTranslator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CodePointTranslator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CodePointTranslator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.CodePointTranslator()"""
        val = _CodePointTranslator()
        self.__wrapper = val

    @abstractmethod
    def translate(self, arg0: int, arg1: 'Writer'):
        """public abstract boolean org.apache.commons.lang3.text.translate.CodePointTranslator.translate(int,java.io.Writer) throws java.io.IOException"""
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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.CodePointTranslator()"""
        val = _CodePointTranslator()
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_CodePointTranslator, self).translate(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
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
import org.apache.commons.lang3.text.translate.NumericEntityUnescaper as _NumericEntityUnescaper_OPTION
_OPTION = _NumericEntityUnescaper_OPTION.OPTION
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OPTION():
    """org.apache.commons.lang3.text.translate.NumericEntityUnescaper.OPTION"""
 
    @staticmethod
    def _wrap(java_value: _OPTION) -> 'OPTION':
        return OPTION(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OPTION):
        """
        Dynamic initializer for OPTION.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OPTION__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OPTION__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'OPTION':
        """public static org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION.valueOf(java.lang.String)"""
        return OPTION._wrap(_OPTION.valueOf(arg0))

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
    def values() -> List['OPTION']:
        """public static org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION[] org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION.values()"""
        return List[OPTION]._wrap(_OPTION.values())

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
 
 
# CLASS: org.apache.commons.lang3.text.translate.CharSequenceTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharSequenceTranslator():
    """org.apache.commons.lang3.text.translate.CharSequenceTranslator"""
 
    @staticmethod
    def _wrap(java_value: _CharSequenceTranslator) -> 'CharSequenceTranslator':
        return CharSequenceTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSequenceTranslator):
        """
        Dynamic initializer for CharSequenceTranslator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSequenceTranslator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSequenceTranslator__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer'):
        """public abstract int org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.CharSequenceTranslator()"""
        val = _CharSequenceTranslator()
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.CharSequenceTranslator()"""
        val = _CharSequenceTranslator()
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover as _UnicodeUnpairedSurrogateRemover
_UnicodeUnpairedSurrogateRemover = _UnicodeUnpairedSurrogateRemover
import java.lang.Integer as _int
import java.io.Writer as Writer
import org.apache.commons.lang3.text.translate.CodePointTranslator as _CodePointTranslator
_CodePointTranslator = _CodePointTranslator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnicodeUnpairedSurrogateRemover():
    """org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover"""
 
    @staticmethod
    def _wrap(java_value: _UnicodeUnpairedSurrogateRemover) -> 'UnicodeUnpairedSurrogateRemover':
        return UnicodeUnpairedSurrogateRemover(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnicodeUnpairedSurrogateRemover):
        """
        Dynamic initializer for UnicodeUnpairedSurrogateRemover.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnicodeUnpairedSurrogateRemover__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnicodeUnpairedSurrogateRemover__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool._wrap(super(_UnicodeUnpairedSurrogateRemover, self).translate(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover()"""
        val = _UnicodeUnpairedSurrogateRemover()
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

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_CodePointTranslator, self).translate(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover()"""
        val = _UnicodeUnpairedSurrogateRemover()
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
 
 
# CLASS: org.apache.commons.lang3.text.translate.NumericEntityEscaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.text.translate.NumericEntityEscaper as _NumericEntityEscaper
_NumericEntityEscaper = _NumericEntityEscaper
import java.lang.Integer as _int
import java.io.Writer as Writer
import org.apache.commons.lang3.text.translate.CodePointTranslator as _CodePointTranslator
_CodePointTranslator = _CodePointTranslator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NumericEntityEscaper():
    """org.apache.commons.lang3.text.translate.NumericEntityEscaper"""
 
    @staticmethod
    def _wrap(java_value: _NumericEntityEscaper) -> 'NumericEntityEscaper':
        return NumericEntityEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NumericEntityEscaper):
        """
        Dynamic initializer for NumericEntityEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NumericEntityEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NumericEntityEscaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.NumericEntityEscaper()"""
        val = _NumericEntityEscaper()
        self.__wrapper = val

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
    def below(arg0: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.below(int)"""
        return NumericEntityEscaper._wrap(_NumericEntityEscaper.below(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def above(arg0: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.above(int)"""
        return NumericEntityEscaper._wrap(_NumericEntityEscaper.above(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def outsideOf(arg0: int, arg1: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.outsideOf(int,int)"""
        return NumericEntityEscaper._wrap(_NumericEntityEscaper.outsideOf(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.NumericEntityEscaper.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool._wrap(super(_NumericEntityEscaper, self).translate(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.NumericEntityEscaper()"""
        val = _NumericEntityEscaper()
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

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_CodePointTranslator, self).translate(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.between(int,int)"""
        return NumericEntityEscaper._wrap(_NumericEntityEscaper.between(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.OctalUnescaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.OctalUnescaper as _OctalUnescaper
_OctalUnescaper = _OctalUnescaper
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OctalUnescaper():
    """org.apache.commons.lang3.text.translate.OctalUnescaper"""
 
    @staticmethod
    def _wrap(java_value: _OctalUnescaper) -> 'OctalUnescaper':
        return OctalUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OctalUnescaper):
        """
        Dynamic initializer for OctalUnescaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OctalUnescaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OctalUnescaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.OctalUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_OctalUnescaper, self).translate(arg0, _int.valueOf(arg1), arg2))

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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.OctalUnescaper()"""
        val = _OctalUnescaper()
        self.__wrapper = val

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.OctalUnescaper()"""
        val = _OctalUnescaper()
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.NumericEntityUnescaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.text.translate.NumericEntityUnescaper as _NumericEntityUnescaper
_NumericEntityUnescaper = _NumericEntityUnescaper
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NumericEntityUnescaper():
    """org.apache.commons.lang3.text.translate.NumericEntityUnescaper"""
 
    @staticmethod
    def _wrap(java_value: _NumericEntityUnescaper) -> 'NumericEntityUnescaper':
        return NumericEntityUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NumericEntityUnescaper):
        """
        Dynamic initializer for NumericEntityUnescaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NumericEntityUnescaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NumericEntityUnescaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, *arg0: 'OPTION'):
        """public org.apache.commons.lang3.text.translate.NumericEntityUnescaper(org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION...)"""
        val = _NumericEntityUnescaper(arg0)
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.NumericEntityUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_NumericEntityUnescaper, self).translate(arg0, _int.valueOf(arg1), arg2))

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
    def isSet(self, arg0: 'OPTION') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.NumericEntityUnescaper.isSet(org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION)"""
        return bool._wrap(super(_NumericEntityUnescaper, self).isSet(arg0))

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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.JavaUnicodeEscaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.text.translate.JavaUnicodeEscaper as _JavaUnicodeEscaper
_JavaUnicodeEscaper = _JavaUnicodeEscaper
import org.apache.commons.lang3.text.translate.UnicodeEscaper as _UnicodeEscaper
_UnicodeEscaper = _UnicodeEscaper
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
import org.apache.commons.lang3.text.translate.CodePointTranslator as _CodePointTranslator
_CodePointTranslator = _CodePointTranslator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JavaUnicodeEscaper():
    """org.apache.commons.lang3.text.translate.JavaUnicodeEscaper"""
 
    @staticmethod
    def _wrap(java_value: _JavaUnicodeEscaper) -> 'JavaUnicodeEscaper':
        return JavaUnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JavaUnicodeEscaper):
        """
        Dynamic initializer for JavaUnicodeEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JavaUnicodeEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JavaUnicodeEscaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.between(int,int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.between(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def below(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.below(int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.below(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def above(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.above(int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.above(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def below(arg0: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.below(int)"""
        return JavaUnicodeEscaper._wrap(_JavaUnicodeEscaper.below(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.UnicodeEscaper.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool._wrap(super(_UnicodeEscaper, self).translate(_int.valueOf(arg0), arg1))

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
    def outsideOf(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.outsideOf(int,int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.outsideOf(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_CodePointTranslator, self).translate(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @staticmethod
    @overload
    def above(arg0: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.above(int)"""
        return JavaUnicodeEscaper._wrap(_JavaUnicodeEscaper.above(_int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.between(int,int)"""
        return JavaUnicodeEscaper._wrap(_JavaUnicodeEscaper.between(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def outsideOf(arg0: int, arg1: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.outsideOf(int,int)"""
        return JavaUnicodeEscaper._wrap(_JavaUnicodeEscaper.outsideOf(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool):
        """public org.apache.commons.lang3.text.translate.JavaUnicodeEscaper(int,int,boolean)"""
        val = _JavaUnicodeEscaper(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))
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
 
 
# CLASS: org.apache.commons.lang3.text.translate.UnicodeEscaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.text.translate.UnicodeEscaper as _UnicodeEscaper
_UnicodeEscaper = _UnicodeEscaper
import java.lang.Integer as _int
import java.io.Writer as Writer
import org.apache.commons.lang3.text.translate.CodePointTranslator as _CodePointTranslator
_CodePointTranslator = _CodePointTranslator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnicodeEscaper():
    """org.apache.commons.lang3.text.translate.UnicodeEscaper"""
 
    @staticmethod
    def _wrap(java_value: _UnicodeEscaper) -> 'UnicodeEscaper':
        return UnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnicodeEscaper):
        """
        Dynamic initializer for UnicodeEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnicodeEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnicodeEscaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.UnicodeEscaper()"""
        val = _UnicodeEscaper()
        self.__wrapper = val

    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.between(int,int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.between(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def below(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.below(int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.below(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def above(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.above(int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.above(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.UnicodeEscaper()"""
        val = _UnicodeEscaper()
        self.__wrapper = val

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
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.UnicodeEscaper.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool._wrap(super(_UnicodeEscaper, self).translate(_int.valueOf(arg0), arg1))

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
    def outsideOf(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.outsideOf(int,int)"""
        return UnicodeEscaper._wrap(_UnicodeEscaper.outsideOf(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_CodePointTranslator, self).translate(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.LookupTranslator
import org.apache.commons.lang3.text.translate.LookupTranslator as _LookupTranslator
_LookupTranslator = _LookupTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LookupTranslator():
    """org.apache.commons.lang3.text.translate.LookupTranslator"""
 
    @staticmethod
    def _wrap(java_value: _LookupTranslator) -> 'LookupTranslator':
        return LookupTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LookupTranslator):
        """
        Dynamic initializer for LookupTranslator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LookupTranslator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LookupTranslator__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, *arg0: List['CharSequence']):
        """public org.apache.commons.lang3.text.translate.LookupTranslator(java.lang.CharSequence[]...)"""
        val = _LookupTranslator(arg0)
        self.__wrapper = val

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.LookupTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_LookupTranslator, self).translate(arg0, _int.valueOf(arg1), arg2))

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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.EntityArrays
import org.apache.commons.lang3.text.translate.EntityArrays as _EntityArrays
_EntityArrays = _EntityArrays
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityArrays():
    """org.apache.commons.lang3.text.translate.EntityArrays"""
 
    @staticmethod
    def _wrap(java_value: _EntityArrays) -> 'EntityArrays':
        return EntityArrays(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityArrays):
        """
        Dynamic initializer for EntityArrays.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityArrays__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityArrays__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.EntityArrays()"""
        val = _EntityArrays()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.EntityArrays()"""
        val = _EntityArrays()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ISO8859_1_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.ISO8859_1_ESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.ISO8859_1_ESCAPE())

    @staticmethod
    @overload
    def JAVA_CTRL_CHARS_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.JAVA_CTRL_CHARS_UNESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.JAVA_CTRL_CHARS_UNESCAPE())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ISO8859_1_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.ISO8859_1_UNESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.ISO8859_1_UNESCAPE())

    @staticmethod
    @overload
    def HTML40_EXTENDED_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.HTML40_EXTENDED_ESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.HTML40_EXTENDED_ESCAPE())

    @staticmethod
    @overload
    def JAVA_CTRL_CHARS_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.JAVA_CTRL_CHARS_ESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.JAVA_CTRL_CHARS_ESCAPE())

    @staticmethod
    @overload
    def HTML40_EXTENDED_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.HTML40_EXTENDED_UNESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.HTML40_EXTENDED_UNESCAPE())

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
    def BASIC_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.BASIC_ESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.BASIC_ESCAPE())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def BASIC_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.BASIC_UNESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.BASIC_UNESCAPE())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def invert(arg0: 'String') -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.invert(java.lang.String[][])"""
        return List[List[str]]._wrap(_EntityArrays.invert(arg0))

    @staticmethod
    @overload
    def APOS_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.APOS_ESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.APOS_ESCAPE())

    @staticmethod
    @overload
    def APOS_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.APOS_UNESCAPE()"""
        return List[List[str]]._wrap(_EntityArrays.APOS_UNESCAPE())

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
 
 
# CLASS: org.apache.commons.lang3.text.translate.AggregateTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as _CharSequenceTranslator
_CharSequenceTranslator = _CharSequenceTranslator
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.text.translate.AggregateTranslator as _AggregateTranslator
_AggregateTranslator = _AggregateTranslator
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AggregateTranslator():
    """org.apache.commons.lang3.text.translate.AggregateTranslator"""
 
    @staticmethod
    def _wrap(java_value: _AggregateTranslator) -> 'AggregateTranslator':
        return AggregateTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AggregateTranslator):
        """
        Dynamic initializer for AggregateTranslator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AggregateTranslator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AggregateTranslator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, *arg0: 'CharSequenceTranslator'):
        """public org.apache.commons.lang3.text.translate.AggregateTranslator(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        val = _AggregateTranslator(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.AggregateTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int._wrap(super(_AggregateTranslator, self).translate(arg0, _int.valueOf(arg1), arg2))

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

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(_CharSequenceTranslator, self).translate(arg0, arg1)

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str._wrap(super(_CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'._wrap(super(_CharSequenceTranslator, self).with(arg0))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str._wrap(_CharSequenceTranslator.hex(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())